# Practice — SQL Topic 3: SELECT · WHERE · NULL

> Reproduce every NULL trap **with your own eyes** on OrderIQ in DuckDB, then build
> a real data-quality report. Predict → run → explain. Output ≠ proof.
>
> `con = duckdb.connect("datasets/orderiq.duckdb")` (from Topic 1 setup).

---

## 🟢 Easy 1 — three-valued logic, live

Predict each, then run:

```python
con.sql("SELECT 5 = 5 AS a, 5 = NULL AS b, NULL = NULL AS c, NULL IS NULL AS d").show()
```

1. What are `a, b, c, d`? Explain `b` and `c` in one line.

<details><summary>Answer</summary>

`a = true`, `b = NULL`, `c = NULL`, `d = true`. Any `=` comparison **with** NULL is
`UNKNOWN` (shown as NULL), because "unknown = anything" can't be confirmed. Only
`IS NULL` gives a real boolean.
</details>

---

## 🟢 Easy 2 — `= NULL` vs `IS NULL` on real data

```python
con.sql("SELECT COUNT(*) FROM orders WHERE city = NULL").show()      # A
con.sql("SELECT COUNT(*) FROM orders WHERE city IS NULL").show()     # B
```

1. Why does A return 0 even though OrderIQ has missing cities (generator injects ~1%)?
2. What does B return, and which is correct?

<details><summary>Answer</summary>

A = 0 always — `city = NULL` is `UNKNOWN`, never TRUE, so no rows pass. B returns
the real count of missing cities. **B is correct**; `= NULL` is a silent bug.
</details>

---

## 🟡 Medium 1 — the `NOT IN` disappearing act

Build a small "flagged" list that includes a NULL, then watch results vanish:

```python
con.sql("""
    WITH flagged(sid) AS (VALUES ('SELLER_1'), ('SELLER_2'), (NULL))
    SELECT COUNT(*) FROM orders
    WHERE seller_id NOT IN (SELECT sid FROM flagged)
""").show()
```

1. What count comes back, and why is it **0** (or far too low)?
2. Rewrite it **two ways** so it works: (a) filter the NULL out, (b) use `NOT EXISTS`.

<details><summary>Answer</summary>

1. `NOT IN (…, NULL)` expands to `… AND seller_id <> NULL`, which is `UNKNOWN`, so
   the whole `AND` can never be TRUE → **0 rows**. One NULL empties the result.
2. Fixes:
```python
# (a) filter NULL out of the list
con.sql("""
    WITH flagged(sid) AS (VALUES ('SELLER_1'),('SELLER_2'),(NULL))
    SELECT COUNT(*) FROM orders
    WHERE seller_id NOT IN (SELECT sid FROM flagged WHERE sid IS NOT NULL)
""").show()

# (b) NOT EXISTS — NULL-safe by construction
con.sql("""
    WITH flagged(sid) AS (VALUES ('SELLER_1'),('SELLER_2'),(NULL))
    SELECT COUNT(*) FROM orders o
    WHERE NOT EXISTS (SELECT 1 FROM flagged f WHERE f.sid = o.seller_id)
""").show()
```
</details>

---

## 🟡 Medium 2 — COUNT and AVG with NULL

```python
con.sql("""
    SELECT COUNT(*) AS all_rows,
           COUNT(amount) AS non_null_amt,
           SUM(amount) AS total,
           AVG(amount) AS avg_amt
    FROM orders
""").show()
```

1. Why is `non_null_amt` less than `all_rows`?
2. `AVG(amount)` — is it `total / all_rows` or `total / non_null_amt`? Verify by
   hand from the two counts.
3. If the business wants missing amounts treated as **0**, rewrite `AVG` to do that.

<details><summary>Answer</summary>

1. The generator injects some NULL amounts; `COUNT(amount)` skips them.
2. `AVG = total / non_null_amt` (NULLs ignored, not counted as 0). Confirm:
   `total / non_null_amt` matches `avg_amt`, but `total / all_rows` does not.
3. Treat NULL as 0: `AVG(COALESCE(amount, 0))` → now divides by all rows.
   (Which is "correct" depends on the business definition — never assume.)
</details>

---

## 🔴 Hard — real data-quality report + a precedence bug

**Part A — build a missing-value report** (a real DE first-look at any dataset):

Write one query returning, for `orders`: total rows, missing_city count,
missing_amount count, and `pct_missing_city` rounded to 2 decimals.

**Part B — fix a precedence bug.** A colleague wrote this to get "delivered orders
that are either big or from Pune" but the numbers look too high:

```python
con.sql("""
    SELECT COUNT(*) FROM orders
    WHERE status = 'delivered' AND amount > 1000 OR city = 'Pune'
""").show()
```

1. Explain what this actually counts (walk the precedence).
2. Rewrite it to match the real intent.
3. **Break-it:** in your fixed query, are rows with `city IS NULL` and
   `amount IS NULL` included or excluded? Explain using three-valued logic.

<details><summary>Answers</summary>

**Part A:**
```python
con.sql("""
    SELECT COUNT(*) AS total_rows,
           COUNT(*) - COUNT(city)   AS missing_city,
           COUNT(*) - COUNT(amount) AS missing_amount,
           ROUND(100.0 * (COUNT(*)-COUNT(city)) / COUNT(*), 2) AS pct_missing_city
    FROM orders
""").show()
```

**Part B:**
1. `AND` binds tighter than `OR`, so it reads:
   `(status='delivered' AND amount>1000) OR city='Pune'` — meaning **every Pune
   order** is counted regardless of status or amount. That inflates the count.
2. Intended:
```python
con.sql("""
    SELECT COUNT(*) FROM orders
    WHERE status = 'delivered' AND (amount > 1000 OR city = 'Pune')
""").show()
```
3. A row with `amount IS NULL` and `city IS NULL`: `amount > 1000` → UNKNOWN,
   `city = 'Pune'` → UNKNOWN, so `(UNKNOWN OR UNKNOWN)` → UNKNOWN, and
   `TRUE AND UNKNOWN` → UNKNOWN → **row dropped**. NULLs silently fall out of the
   filter — which may or may not be what you want. Decide deliberately (e.g.
   `COALESCE(city,'') = 'Pune'`).
</details>

---

### ✅ Mastery check for Topic 3

Without notes:

- explain why `= NULL` is always a bug and use `IS NULL`,
- explain (and fix) the `NOT IN … NULL` empty-result trap,
- choose `COUNT(*)` vs `COUNT(col)` and predict `AVG` with NULLs,
- fix an `AND`/`OR` precedence bug, and reason about NULLs falling out of a filter.

Passed? → **Topic 4 — Sorting, DISTINCT, LIMIT & Pagination** (finishes Phase 0;
includes where NULLs sort).

*Back to the [lesson](./README.md).*
