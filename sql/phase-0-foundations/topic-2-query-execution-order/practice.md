# Practice — SQL Topic 2: Query Execution Order

> The goal here is unusual: **trigger each error on purpose**, understand *which
> step* caused it, then fix it. Predicting the failure before you run it is what
> burns the execution order into memory.
>
> Environment: DuckDB with the OrderIQ dataset (set up in Topic 1's practice). Open
> a notebook: `import duckdb; con = duckdb.connect("datasets/orderiq.duckdb")`.

Rule for every problem: **predict first** (will it work? if not, which step?),
*then* run.

---

## 🟢 Easy 1 — the alias-in-WHERE trap

**Predict**, then run:

```python
con.sql("""
    SELECT amount * 0.18 AS gst
    FROM orders
    WHERE gst > 100
""").show()
```

1. Does it work? If not, **which step** caused it and why?
2. Fix it **two ways**: (a) without a CTE, (b) with a CTE.

<details><summary>Answer</summary>

Fails — `WHERE` (step 2) runs before `SELECT` (step 5) makes the alias `gst`.

```python
# (a) repeat the expression
con.sql("SELECT amount*0.18 AS gst FROM orders WHERE amount*0.18 > 100").show()

# (b) CTE
con.sql("""
    WITH calc AS (SELECT amount*0.18 AS gst FROM orders)
    SELECT gst FROM calc WHERE gst > 100
""").show()
```
</details>

---

## 🟢 Easy 2 — the same alias in ORDER BY (works!)

**Predict**, then run:

```python
con.sql("""
    SELECT city, COUNT(*) AS order_count
    FROM orders
    GROUP BY city
    ORDER BY order_count DESC
    LIMIT 5
""").show()
```

1. Does it work? Why does `order_count` work **here** but the alias failed in
   Easy 1? (Name the two step numbers.)

<details><summary>Answer</summary>

Works. `ORDER BY` is step 6, *after* `SELECT` (step 5) creates the alias — so
`order_count` exists. In Easy 1, `WHERE` was step 2, *before* the alias existed.
Same alias, opposite result, purely due to *when* the clause runs.
</details>

---

## 🟡 Medium 1 — WHERE vs HAVING

**Predict** each, then run:

```python
# Query A
con.sql("""
    SELECT city, COUNT(*) AS n
    FROM orders
    WHERE COUNT(*) > 100
    GROUP BY city
""").show()

# Query B
con.sql("""
    SELECT city, COUNT(*) AS n
    FROM orders
    GROUP BY city
    HAVING COUNT(*) > 100
""").show()
```

1. Which one errors, and exactly why?
2. Rewrite Query B to *also* only count `delivered` orders — and put that condition
   in the **most efficient** place. Justify the placement.

<details><summary>Answer</summary>

1. **Query A errors** — `WHERE` (step 2) can't use `COUNT(*)`; aggregation happens
   at steps 3–4. Query B is correct (`HAVING` filters groups after aggregation).
2. Put `status = 'delivered'` in `WHERE`, not `HAVING`:

```python
con.sql("""
    SELECT city, COUNT(*) AS n
    FROM orders
    WHERE status = 'delivered'    -- row filter BEFORE grouping = fewer rows = faster
    GROUP BY city
    HAVING COUNT(*) > 100         -- group filter needs the aggregate
""").show()
```
`status` is a raw-row condition → `WHERE` removes rows before grouping (less work).
`COUNT(*) > 100` needs the aggregate → must be `HAVING`.
</details>

---

## 🟡 Medium 2 — the GROUP BY "loose column" rule

**Predict**, then run:

```python
con.sql("""
    SELECT city, status, COUNT(*) AS n
    FROM orders
    GROUP BY city
""").show()
```

1. Does it work? Why or why not, in terms of "one row per group"?
2. Give **two** correct rewrites that keep `status` visible.

<details><summary>Answer</summary>

Fails — group `city='Pune'` holds many `status` values; the single output row has
no unique `status` to show, so the DB refuses.

```python
# (a) group by it too → one row per (city, status)
con.sql("SELECT city, status, COUNT(*) n FROM orders GROUP BY city, status").show()
# (b) aggregate it → collapse to one value per city
con.sql("SELECT city, MAX(status) status, COUNT(*) n FROM orders GROUP BY city").show()
```
</details>

---

## 🔴 Hard — full pipeline + reason about the order end to end

Write **one** query that answers: *"For delivered orders only, show the top 3
cities by total revenue, but only cities with more than 50 delivered orders, and
show revenue rounded to whole rupees."*

Requirements — and for each, state which **step** enforces it:

1. Only `delivered` orders.
2. Group by city.
3. Only cities with > 50 delivered orders.
4. Sort by total revenue, highest first.
5. Top 3 only.
6. The revenue column should be named `revenue` and you must be able to sort by
   that alias.

Then answer the **Break-its**:

- (a) Move the `status = 'delivered'` condition from `WHERE` into `HAVING`. Does it
  still run? Does the result change? Is it slower — why?
- (b) Try `ORDER BY ROUND(SUM(amount))` vs `ORDER BY revenue`. Do both work? Why?
- (c) Add `SELECT DISTINCT city` and try to `ORDER BY SUM(amount)`. Predict the
  outcome before running.

<details><summary>Reference solution</summary>

```python
con.sql("""
    SELECT   city,
             ROUND(SUM(amount)) AS revenue          -- step 5: alias made here
    FROM     orders                                 -- step 1
    WHERE    status = 'delivered'                   -- step 2: row filter
    GROUP BY city                                   -- step 3
    HAVING   COUNT(*) > 50                           -- step 4: group filter
    ORDER BY revenue DESC                            -- step 6: alias visible
    LIMIT    3                                        -- step 7
""").show()
```

Step map: (1) `WHERE status='delivered'` → step 2. (2) `GROUP BY city` → step 3.
(3) `HAVING COUNT(*)>50` → step 4. (4) `ORDER BY revenue DESC` → step 6. (5)
`LIMIT 3` → step 7. (6) alias `revenue` created at step 5, used at step 6 ✅.

**Break-it answers:**
- (a) `HAVING status = 'delivered'` still *runs* here (status is a grouped-ish
  scalar) but it's the **wrong place**: it would filter *after* grouping, meaning
  the DB grouped ALL statuses first then discarded most groups' work — more rows
  grouped = slower. In strict engines it can also error if `status` isn't grouped.
  Correct place is `WHERE` (fewer rows before grouping). Result *value* is the same
  when it runs; the **cost** is higher.
- (b) Both work. `ORDER BY` (step 6) can use either the alias `revenue` OR re-state
  the expression `ROUND(SUM(amount))` — both are available after `SELECT`.
- (c) `SELECT DISTINCT city ... ORDER BY SUM(amount)` **fails** — after
  `DISTINCT city`, only `city` survives; `SUM(amount)` isn't in the selected set,
  so `ORDER BY` can't reference it.
</details>

---

### ✅ Mastery check for Topic 2

You own it when you can, from memory:

- recite `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`,
- explain why an alias fails in `WHERE` but works in `ORDER BY` (by step number),
- choose `WHERE` vs `HAVING` correctly *and* for performance,
- and debug a "must appear in GROUP BY" error by naming the step.

Passed? → **Topic 3: SELECT · WHERE · operators · NULL basics** (where the famous
`NULL` traps live — even seniors miss `NOT IN (… NULL …)`).

*Back to the [lesson](./README.md).*
