# Practice — SQL Topic 1: The Relational Model

> Topic 1 is about **thinking** in the relational model, not heavy querying (that
> starts Topic 3). So this practice = set up your SQL environment once, then reason
> about **schema, keys, and relationships** on the real OrderIQ tables.

---

## 🛠️ One-time setup (do this now — you'll use it for the whole SQL series)

You have two easy options. **Pick DuckDB** if you want zero-install and speed.

### Option A — DuckDB (recommended to start, ~3 min)

DuckDB is a database *inside* a single file — no server, no cloud.

```bash
# from the repo root
pip install duckdb
cd datasets
python generate.py --orders 100000 --out ./data   # builds the OrderIQ CSVs
python seed_duckdb.py                              # loads them into orderiq.duckdb
```

Then query it:

```bash
python -c "import duckdb; con=duckdb.connect('datasets/orderiq.duckdb'); print(con.sql('SHOW TABLES'))"
```

Or in a notebook cell:

```python
import duckdb
con = duckdb.connect("datasets/orderiq.duckdb")
con.sql("SELECT * FROM orders LIMIT 5").show()
```

### Option B — PostgreSQL (closer to interview reality, set up later)

A free cloud tier (Supabase/Neon) or local Postgres. We'll switch to this in a
later phase for indexes/`EXPLAIN`. **DuckDB is enough for now** — same SQL.

> ✅ You're ready when `SELECT count(*) FROM orders;` returns a number.

---

## Part 1 — 🟢 Read the schema (no query needed, just inspect)

Run this to see each table's columns and types:

```python
for t in ["customers", "products", "sellers", "orders", "order_items", "payments"]:
    print(f"\n=== {t} ===")
    con.sql(f"DESCRIBE {t}").show()
```

**Answer in your own words (write it down):**

1. Which column is the **primary key** of `orders`? How do you know it's a good PK?
2. `order_items` has no single unique column. What is its **composite key**?
3. List every **foreign key** you can find across the 6 tables and say which table
   each points to.
4. Which columns are **nullable** (can hold NULL) and why might that be realistic
   for e-commerce data?

<details><summary>Guidance</summary>

1. `order_id` — one row per order, never blank, never reused.
2. `(order_id, product_id)` — the pair is unique; each product appears once per order.
3. Expect: `orders.customer_id → customers`, `order_items.order_id → orders`,
   `order_items.product_id → products`, `payments.order_id → orders`,
   `products.seller_id → sellers` (check your actual generated schema and confirm).
4. `city`, `email`, `status` etc. — real source systems have missing values; the
   generator injects ~1% nulls on purpose so you learn to handle them.
</details>

---

## Part 2 — 🟡 Prove the relationships with counts

Run these and interpret — you're *seeing* 1:N in the data.

```python
con.sql("SELECT COUNT(*) AS n_orders FROM orders").show()
con.sql("SELECT COUNT(*) AS n_items  FROM order_items").show()
con.sql("""
    SELECT order_id, COUNT(*) AS items_in_order
    FROM order_items
    GROUP BY order_id
    ORDER BY items_in_order DESC
    LIMIT 5
""").show()
```

**Questions:**

1. Is `n_items` greater than, equal to, or less than `n_orders`? What relationship
   does that confirm between `orders` and `order_items`?
2. Find one `customer_id` with more than one order (below). What relationship does
   *that* confirm?

```python
con.sql("""
    SELECT customer_id, COUNT(*) AS orders_placed
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(*) > 1
    ORDER BY orders_placed DESC
    LIMIT 5
""").show()
```

<details><summary>Answers</summary>

1. `n_items > n_orders` because **one order has many items** — the classic 1:N.
2. A customer with several orders confirms **customers 1 ──< N orders** (1:N).
   Together these two 1:N links are what let `order_items` bridge orders↔products.
</details>

---

## Part 3 — 🔴 See the fan-out trap with your own eyes (the important one)

This is the whole reason Topic 1 matters. Run **both** and compare.

```python
# WRONG — sum order amount AFTER joining to items (fans out)
con.sql("""
    SELECT SUM(o.amount) AS revenue_WRONG
    FROM orders o
    JOIN order_items i ON i.order_id = o.order_id
    WHERE o.status = 'delivered'
""").show()

# RIGHT — sum order amount on orders alone (one row per order)
con.sql("""
    SELECT SUM(amount) AS revenue_RIGHT
    FROM orders
    WHERE status = 'delivered'
""").show()
```

**Tasks:**

1. Are the two numbers different? By roughly how much?
2. **Explain in one sentence** *why* the first is inflated. (Name the relationship
   and the word "fan-out.")
3. **Break-it / fix-it:** suppose you genuinely need per-item detail *and* a correct
   order total in one result. Write a query that avoids the double-count. Hint:
   aggregate `order_items` in a subquery/CTE first, then join.

<details><summary>Answers</summary>

1. `revenue_WRONG` is larger — each order's `amount` is repeated once per line
   item, so orders with more items are counted more times.
2. Joining across the **1:N** `orders → order_items` relationship **fans out** the
   order rows, so `SUM(o.amount)` counts each amount multiple times.
3. Aggregate first, then join:

```sql
WITH item_counts AS (
    SELECT order_id, COUNT(*) AS n_items, SUM(quantity) AS total_qty
    FROM order_items
    GROUP BY order_id
)
SELECT o.order_id, o.amount, ic.n_items, ic.total_qty
FROM orders o
JOIN item_counts ic ON ic.order_id = o.order_id
WHERE o.status = 'delivered';
-- Now o.amount appears exactly ONCE per order. SUM(o.amount) here is correct.
```
This "aggregate at the right grain, *then* join" pattern is one of the most
important habits in all of data engineering. You just met it on day one.
</details>

---

### ✅ Mastery check for Topic 1

You own this topic when you can, without looking:

- point to the PK / composite key / FKs in the OrderIQ schema and say *why*,
- state which side of a 1:N holds the FK,
- explain why M:N needs a bridge table and name OrderIQ's bridge,
- and **explain + fix the fan-out double-count** from Part 3.

Do all 4? → Topic 1 gate passed. **Next: Topic 2 — the logical order of query
execution** (why `WHERE` runs before `SELECT`, and why you can't filter on a
`SELECT` alias).

*Back to the [lesson](./README.md).*
