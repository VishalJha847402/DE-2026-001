# Practice — SQL Topic 4: Sorting · DISTINCT · LIMIT · Pagination

> See NULLs crash a top-10, make ties flip your results, race OFFSET vs keyset —
> all on OrderIQ in DuckDB. Predict → run → explain. Ends with the **Phase-0 gate**.
>
> `con = duckdb.connect("datasets/orderiq.duckdb")`

---

## 🟢 Easy 1 — where do NULLs sort?

Predict, then run:

```python
con.sql("SELECT x FROM (VALUES (1),(3),(NULL),(2)) t(x) ORDER BY x DESC").show()
con.sql("SELECT x FROM (VALUES (1),(3),(NULL),(2)) t(x) ORDER BY x DESC NULLS LAST").show()
```

1. Where did NULL land in the first query?
2. Now the real damage — run a naive top-10 on OrderIQ:

```python
con.sql("SELECT order_id, amount FROM orders ORDER BY amount DESC LIMIT 10").show()
```

Are there NULL amounts sitting above your real biggest orders? Fix the query.

<details><summary>Answer</summary>

1. In DuckDB/Postgres, `DESC` puts NULLs **first** — they sort as if largest.
2. Yes — the injected ~0.5% NULL amounts crown the "top 10." Fix:

```python
con.sql("""
    SELECT order_id, amount FROM orders
    ORDER BY amount DESC NULLS LAST, order_id
    LIMIT 10
""").show()
```
(`NULLS LAST` seats the gatecrashers; `order_id` makes ties deterministic.)
</details>

---

## 🟢 Easy 2 — DISTINCT is whole-row

Predict the difference, then run:

```python
con.sql("SELECT COUNT(*) FROM (SELECT DISTINCT city FROM orders)").show()
con.sql("SELECT COUNT(*) FROM (SELECT DISTINCT city, status FROM orders)").show()
```

1. Why is the second count bigger?
2. Rewrite `SELECT DISTINCT city FROM orders` using `GROUP BY` — same result?

<details><summary>Answer</summary>

1. The second dedups **(city, status) combinations** — each city appears once per
   status it has. DISTINCT applies to the whole selected row, not just column 1.
2. `SELECT city FROM orders GROUP BY city` — identical output; DISTINCT with no
   aggregates ≡ GROUP BY on all selected columns.
</details>

---

## 🟡 Medium 1 — ties make "top N" lie

```python
# How many orders share the most common order_date?
con.sql("""
    SELECT order_date, COUNT(*) AS n FROM orders
    GROUP BY order_date ORDER BY n DESC LIMIT 3
""").show()

# Now a naive "latest 5":
con.sql("SELECT order_id, order_date FROM orders ORDER BY order_date DESC LIMIT 5").show()
```

1. Given dozens of orders share the latest date, what's non-deterministic about the
   "latest 5"? Why might it differ between runs/engines?
2. Make it deterministic.
3. Why does this matter for a nightly export job specifically?

<details><summary>Answer</summary>

1. The engine may return **any 5** of the tied rows — order among equal keys is
   unspecified and can change with the plan, parallelism, or version.
2. `ORDER BY order_date DESC, order_id DESC LIMIT 5` — the PK breaks ties.
3. An export that pages by a tied sort can **skip or duplicate rows** between
   pages/runs — silent data loss in the downstream system.
</details>

---

## 🟡 Medium 2 — the OFFSET cliff (measure it)

```python
import time
def t(q):
    s = time.time(); con.sql(q).fetchall(); return round((time.time()-s)*1000)

print("page 1:   ", t("SELECT * FROM orders ORDER BY order_id LIMIT 100 OFFSET 0"), "ms")
print("page 500: ", t("SELECT * FROM orders ORDER BY order_id LIMIT 100 OFFSET 49900"), "ms")
print("keyset:   ", t("SELECT * FROM orders WHERE order_id > 49900 ORDER BY order_id LIMIT 100"), "ms")
```

1. Compare the three timings. Why does deep OFFSET cost more? (On 100k rows DuckDB
   is fast — imagine 100M in Postgres.)
2. Besides speed, what *correctness* problem does OFFSET have that keyset doesn't?

<details><summary>Answer</summary>

1. `OFFSET 49900` must produce and discard 49,900 rows before returning yours —
   work grows with depth. Keyset's `WHERE order_id > 49900` seeks straight to the
   position (index-friendly), constant cost at any depth.
2. **Drift:** inserts/deletes between page requests shift OFFSET positions → rows
   duplicated or skipped across pages. Keyset's bookmark is immune — "after id X"
   stays meaningful.
</details>

---

## 🔴 Hard — build the incremental export (the real DE pattern)

OrderIQ's nightly job must export **new delivered orders** to a downstream system,
50,000 rows max per run, resuming from where the last run stopped.

1. Write the query using a `:last_loaded_id` bookmark (use a literal, e.g. `1000`,
   to test). Requirements: deterministic order, NULL-safe if you sort by anything
   nullable, seek not skip.
2. After a run returns rows, what exactly do you persist as tomorrow's bookmark?
3. **Break-it (a):** a teammate implements it with
   `LIMIT 50000 OFFSET :runs_so_far * 50000`. Give two concrete failure modes.
4. **Break-it (b):** another teammate bookmarks on `order_date` (not unique)
   with `WHERE order_date > :last_date`. What rows get lost? How do you fix a
   timestamp-based bookmark properly?

<details><summary>Answers</summary>

1. ```python
   con.sql("""
       SELECT order_id, customer_id, city, amount, order_date
       FROM orders
       WHERE status = 'delivered'
         AND order_id > 1000            -- the bookmark: seek past last loaded
       ORDER BY order_id                -- unique ⇒ deterministic, no NULLS issue
       LIMIT 50000
   """).show()
   ```
2. The **max `order_id` of the rows actually exported** — that's the new bookmark.
3. OFFSET version fails because: (a) **cost** — each nightly run re-produces and
   discards everything before its page; run 100 scans ~5M rows to skip them.
   (b) **drift** — rows inserted/updated between runs shift the offsets → some
   orders exported twice, others never. (Also a crash mid-run can't resume safely.)
4. `order_date > :last_date` **loses all-but-the-first rows sharing the boundary
   date** (they're `=`, not `>`). Timestamp bookmarks must use a **composite
   keyset**: `WHERE (order_date, order_id) > (:last_date, :last_id)
   ORDER BY order_date, order_id` — the unique id disambiguates within the tied
   timestamp. (Same fix as the ties rule: always end in a unique key.)
</details>

---

## ✅ THE PHASE-0 GATE — SQL foundations complete?

From memory, no notes. Miss one → redo that topic's Hard problem.

- [ ] **T1:** point out PK / composite key / FKs in OrderIQ; explain the fan-out
      double-count and the aggregate-then-join fix.
- [ ] **T2:** recite `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`
      and explain why an alias fails in WHERE but works in ORDER BY.
- [ ] **T3:** explain three-valued logic; why `= NULL` matches nothing and one NULL
      empties a `NOT IN`; `COUNT(*)` vs `COUNT(col)`.
- [ ] **T4:** write a deterministic, NULL-safe top-N; explain the OFFSET cliff and
      the keyset/incremental-export pattern.

**All four green → Phase 0 done.** Next: **Phase 1 — JOINs Deep**, where the
relational model (T1) and execution order (T2) pay off immediately.

*Back to the [lesson](./README.md).*
