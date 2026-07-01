# Topic 3 — SELECT · WHERE · Filtering · Operators · NULL Basics

> **SQL · Phase 0 · Foundations · Lesson 3 of 4.** Now you write real queries. The
> star of this lesson isn't `SELECT` — it's **`NULL`**, the single most common
> source of silent wrong answers in data engineering. Even seniors miss it.

> 🎯 **First principle:** you don't own this until you can **BUILD** the queries on
> OrderIQ, **BREAK** them with the `NULL` traps (`= NULL`, `NOT IN (…NULL…)`), and
> **EXPLAIN** three-valued logic in plain words. [`practice.md`](./practice.md) makes you.

---

## 0. WHY this exists

You "write queries to fetch data" already. So the goal here is not `SELECT * FROM`.
The goal is the stuff that makes your `WHERE` **silently return the wrong rows** —
because SQL's `NULL` does not behave like anything in Python or Excel.

🗣️ **In plain words:** a wrong `WHERE` doesn't throw an error. It just quietly gives
you fewer rows (or more) than reality — and your dashboard is wrong and nobody
knows. This lesson is about not being that person.

**Where a DE uses this:** every filter in every pipeline, every data-quality check,
every "why is my count off by 3%?" investigation. It's usually a `NULL`.

---

## 1. SELECT — choosing columns

```sql
SELECT order_id, city, amount FROM orders;   -- specific columns (do this)
SELECT * FROM orders;                        -- all columns (avoid in pipelines)
```

**DE rule:** avoid `SELECT *` in real pipelines. It pulls columns you don't need
(slower, more memory), and it breaks silently when someone adds/reorders columns
upstream. Name your columns.

### Aliases and computed columns

```sql
SELECT
    order_id,
    amount,
    amount * 0.18 AS gst,          -- computed column, named with AS
    status AS order_status
FROM orders;
```

Remember Topic 2: the alias `gst` is created at the `SELECT` step — so `WHERE`
can't use it, but `ORDER BY` can.

---

## 2. WHERE — filtering rows + the operators

```sql
SELECT * FROM orders
WHERE amount > 1000
  AND status = 'delivered';
```

### Comparison & logical operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` `<>` / `!=` | equal / not equal | `status = 'delivered'` |
| `<` `>` `<=` `>=` | comparisons | `amount >= 500` |
| `AND` `OR` `NOT` | combine conditions | `a AND (b OR c)` |
| `BETWEEN x AND y` | range, **inclusive** | `amount BETWEEN 100 AND 500` |
| `IN (…)` | matches any in a list | `city IN ('Pune','Delhi')` |
| `LIKE` | pattern match | `city LIKE 'M%'` (starts with M) |
| `IS NULL` / `IS NOT NULL` | missing-value test | `city IS NULL` |

### `AND` / `OR` precedence trap

`AND` binds tighter than `OR`. This changes results:

```sql
-- These are DIFFERENT:
WHERE status = 'delivered' AND amount > 1000 OR city = 'Pune'
-- reads as: (status='delivered' AND amount>1000) OR city='Pune'   ← ALL Pune rows sneak in

-- What you probably meant:
WHERE status = 'delivered' AND (amount > 1000 OR city = 'Pune')
```

🗣️ **In plain words:** always wrap your `OR` groups in parentheses. Without them,
`AND` "wins" and your filter means something you didn't intend.

### `LIKE` patterns

- `%` = any number of characters: `'M%'` → Mumbai, Meerut. `'%pur'` → Kanpur, Nagpur.
- `_` = exactly one character: `'B_A'` → BBA, BCA (3 chars, middle any).
- Case sensitivity varies by engine (Postgres `LIKE` is case-sensitive; use `ILIKE` for insensitive).

---

## 3. NULL — the heart of this lesson ⭐

**`NULL` means "unknown / missing," NOT zero and NOT empty string.** A `NULL` city
isn't "" — it's "we don't know this city."

This one idea creates **three-valued logic**: every condition is `TRUE`, `FALSE`,
or **`UNKNOWN`**. And `WHERE` keeps a row **only when the condition is exactly `TRUE`**
— `UNKNOWN` rows are dropped.

### Trap #1 — you cannot use `=` with NULL

```sql
WHERE city = NULL      -- ❌ ALWAYS returns nothing (evaluates to UNKNOWN)
WHERE city IS NULL     -- ✅ correct way to find missing cities
WHERE city IS NOT NULL -- ✅ correct way to exclude them
```

Why: `NULL = NULL` is **not** `TRUE` — it's `UNKNOWN`, because "unknown = unknown"
can't be confirmed. So `= NULL` matches zero rows, silently.

🗣️ **In plain words:** two people both refuse to tell you their city. Are they from
the same city? You *can't say* — that's `UNKNOWN`, not "yes." SQL agrees. So you
must ask `IS NULL`, never `= NULL`.

### Trap #2 — NULL breaks `NOT IN` (the senior-killer)

```sql
-- Suppose (SELECT seller_id FROM flagged) returns: 'S1', 'S2', NULL
SELECT * FROM orders
WHERE seller_id NOT IN (SELECT seller_id FROM flagged);   -- ❌ returns ZERO rows!
```

Why: `NOT IN (S1, S2, NULL)` becomes `seller_id <> S1 AND seller_id <> S2 AND seller_id <> NULL`.
That last `<> NULL` is `UNKNOWN`, so the whole `AND` can never be `TRUE` → **every
row is dropped**. A single `NULL` in the list silently empties your result.

**Fixes:** use `NOT EXISTS`, or filter `NULL` out of the subquery:

```sql
WHERE seller_id NOT IN (SELECT seller_id FROM flagged WHERE seller_id IS NOT NULL);
-- or, better:
WHERE NOT EXISTS (SELECT 1 FROM flagged f WHERE f.seller_id = orders.seller_id);
```

### Trap #3 — NULL in arithmetic and aggregates

- **Arithmetic:** `amount + NULL = NULL`. Any math with `NULL` yields `NULL`.
- **Aggregates ignore NULL:** `AVG(amount)`, `SUM(amount)`, `COUNT(amount)` skip
  `NULL` rows. But `COUNT(*)` counts **all** rows including `NULL`s.

```sql
-- amounts: 100, 200, NULL
SELECT
  COUNT(*)        AS all_rows,     -- 3
  COUNT(amount)   AS non_null_amt, -- 2  (NULL skipped)
  SUM(amount)     AS total,        -- 300
  AVG(amount)     AS avg_amt;      -- 150  (300/2, NOT 300/3!)
```

🗣️ **In plain words:** `AVG` divides by the count of *known* values, not all rows.
If you expected 100 (300÷3) you'd be wrong — it's 150 (300÷2). Knowing whether
`NULL` should count as 0 or be ignored is a **business rule**, not a default.

### Trap #4 — `COUNT(column)` vs `COUNT(*)`

`COUNT(*)` = number of rows. `COUNT(city)` = number of rows where `city IS NOT NULL`.
People use them interchangeably and get different numbers. Pick deliberately.

---

## 4. Handling NULL — COALESCE, NULLIF, IS DISTINCT FROM

```sql
COALESCE(city, 'UNKNOWN')        -- first non-NULL value → replaces NULL with 'UNKNOWN'
COALESCE(a, b, c, 0)             -- returns the first of a,b,c that isn't NULL, else 0
NULLIF(amount, 0)                -- returns NULL if amount = 0 (useful to avoid /0)
amount IS DISTINCT FROM NULL     -- NULL-safe comparison: treats NULL as a real value
```

- **`COALESCE`** — your everyday "give me a default when it's missing." Used
  constantly to clean data before display or math.
- **`NULLIF(x, y)`** — returns `NULL` when `x = y`. Classic use:
  `revenue / NULLIF(orders, 0)` avoids divide-by-zero (division by `NULL` → `NULL`
  instead of an error).
- **`IS DISTINCT FROM`** — a comparison where `NULL` behaves like a normal value
  (`NULL IS DISTINCT FROM NULL` is `FALSE`; `NULL IS DISTINCT FROM 5` is `TRUE`).

---

## 5. The 3-step example — from mechanic to real DE work

### Step 1 — tiny mechanic

```sql
SELECT 5 = 5   AS a,    -- true
       5 = NULL AS b,   -- NULL (unknown!)
       NULL = NULL AS c;-- NULL (unknown!)
```

### Step 2 — OrderIQ e-commerce

```sql
-- "Delivered orders over ₹1000 in Pune or Delhi, treating missing city as UNKNOWN"
SELECT order_id, COALESCE(city,'UNKNOWN') AS city, amount
FROM orders
WHERE status = 'delivered'
  AND amount > 1000
  AND city IN ('Pune','Delhi');    -- note: NULL cities are NOT matched here
```

### Step 3 — data-quality check (real DE task)

```sql
-- How dirty is our data? Count missing values per column — a real DQ probe.
SELECT
  COUNT(*)                                    AS total_rows,
  COUNT(*) - COUNT(city)                      AS missing_city,
  COUNT(*) - COUNT(amount)                    AS missing_amount,
  ROUND(100.0 * (COUNT(*)-COUNT(city)) / COUNT(*), 2) AS pct_missing_city
FROM orders;
```

Step 3 is a pattern you'll run on *every* new dataset before trusting it — and it's
built entirely on `COUNT(*)` vs `COUNT(col)` understanding `NULL`.

---

## 6. Diagram — three-valued logic

```mermaid
flowchart TD
    C["condition in WHERE"] --> E{"evaluates to?"}
    E -->|TRUE| K["row KEPT ✅"]
    E -->|FALSE| D["row dropped ❌"]
    E -->|UNKNOWN<br/>(any comparison with NULL)| D2["row dropped ❌<br/>(this is the silent trap)"]

    N["city = NULL"] -.->|UNKNOWN| D2
    N2["city IS NULL"] -.->|TRUE/FALSE| K
```

The whole lesson in one picture: `WHERE` keeps only `TRUE`. Any comparison touching
`NULL` is `UNKNOWN` → dropped. Use `IS NULL`, not `= NULL`.

---

## 7. 🗣️ Plain-words recap

- `SELECT` named columns, not `*`, in pipelines.
- `WHERE` keeps a row only when the condition is **exactly TRUE**.
- Wrap `OR` groups in **parentheses** — `AND` binds tighter.
- **`NULL` = unknown**, not 0, not "". You get **three-valued logic** (TRUE/FALSE/UNKNOWN).
- Never `= NULL` → use **`IS NULL` / `IS NOT NULL`**.
- **`NOT IN` with a NULL in the list returns nothing** — filter NULLs out or use `NOT EXISTS`.
- Aggregates **skip NULL**; `COUNT(*)` counts all rows, `COUNT(col)` counts non-NULLs; `AVG` divides by non-NULL count.
- Clean with **`COALESCE`**, avoid /0 with **`NULLIF`**, compare NULL-safely with **`IS DISTINCT FROM`**.

---

## 8. Revision — read before closing

The trap that will actually cost you in production is `NULL`. It is "unknown," so
any comparison with it is `UNKNOWN`, and `WHERE` silently drops `UNKNOWN` rows — no
error, just a wrong count. That is why you write `IS NULL` not `= NULL`, why a
single `NULL` inside a `NOT IN` list empties your whole result, and why `AVG`
divides by the count of *known* values (which may not be what the business wants).
Whenever a count looks "off by a few percent," your first suspect is a `NULL` doing
something you didn't expect. `COALESCE` to set defaults, `NULLIF` to dodge
divide-by-zero, and always choose `COUNT(*)` vs `COUNT(col)` on purpose. Next lesson
finishes Phase 0: sorting, `DISTINCT`, `LIMIT`, and pagination — including how
`NULL` sorts (first or last?).

---

## 9. Test yourself — 10 questions (answers hidden — think first)

<details><summary>1. What does <code>NULL</code> actually mean, and what does it NOT mean?</summary>

"Unknown / missing." It is NOT zero and NOT an empty string `''`.
</details>

<details><summary>2. Why does <code>WHERE city = NULL</code> return no rows?</summary>

`= NULL` evaluates to `UNKNOWN` (not TRUE), and `WHERE` keeps only TRUE rows. Use
`IS NULL`.
</details>

<details><summary>3. Explain three-valued logic in one line.</summary>

Every condition is TRUE, FALSE, or UNKNOWN; `WHERE` keeps only TRUE.
</details>

<details><summary>4. Why can <code>NOT IN (SELECT …)</code> return zero rows unexpectedly?</summary>

If the subquery contains a `NULL`, `NOT IN` becomes `… AND col <> NULL`, which is
`UNKNOWN`, so no row is ever TRUE → all dropped. Filter NULLs or use `NOT EXISTS`.
</details>

<details><summary>5. Difference between <code>COUNT(*)</code> and <code>COUNT(city)</code>?</summary>

`COUNT(*)` = all rows. `COUNT(city)` = rows where city IS NOT NULL.
</details>

<details><summary>6. amounts are 100, 200, NULL. What are SUM and AVG?</summary>

SUM = 300, AVG = 150 (300 ÷ 2 non-NULL rows — NULL is ignored, not treated as 0).
</details>

<details><summary>7. What does <code>COALESCE(a, b, 0)</code> return?</summary>

The first of `a`, `b` that is not NULL; if both NULL, returns `0`.
</details>

<details><summary>8. How do you safely avoid divide-by-zero in <code>revenue / orders</code>?</summary>

`revenue / NULLIF(orders, 0)` → denominator becomes NULL when 0, result is NULL
instead of an error.
</details>

<details><summary>9. Why wrap OR conditions in parentheses?</summary>

`AND` has higher precedence than `OR`; without parentheses the grouping changes
and extra rows leak in.
</details>

<details><summary>10. `'M%'` vs `'_M%'` in LIKE — difference?</summary>

`'M%'` = starts with M. `'_M%'` = any one char, then M, then anything (M is the 2nd
character).
</details>

---

## 10. Practice

👉 [`practice.md`](./practice.md) — on OrderIQ in DuckDB you'll reproduce each NULL
trap live (the disappearing `NOT IN`, the `AVG` surprise), then write a real
data-quality missing-value report. BUILD → BREAK → EXPLAIN.

---

*Next: [Topic 4 — Sorting, DISTINCT, LIMIT & Pagination](../topic-4-sorting-distinct-limit/) — finishes Phase 0.*
