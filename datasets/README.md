# OrderIQ Dataset — the shared spine for ALL practice + the project

> ONE wide+long e-commerce dataset used across Python, SQL, DuckDB, Data Modeling, dbt, Spark, and the OrderIQ P1→P2→P3 project. See `CLAUDE.md §9C`.
> **This is v1 (core tables).** Enrichments (reviews, clickstream JSON, price_history/SCD2, geo) get added as we reach the lessons that need them.

## Get runnable data in ~3 minutes

```bash
# 1. generate the CSVs (no installs needed — stdlib only)
python generate.py --orders 100000        # or --orders 1000 for a quick test

# 2. load into DuckDB
pip install duckdb
python seed_duckdb.py                      # creates orderiq.duckdb
```

That's it. You now have `orderiq.duckdb` you can query from Python or SQL.

**Verify it worked:**
```python
import duckdb
con = duckdb.connect("orderiq.duckdb")
con.sql("SELECT city, COUNT(*) AS orders FROM customers GROUP BY 1 ORDER BY 2 DESC").show()
```

## Tables (v1) — with referential integrity

| Table | Grain | Key columns | Links to |
|-------|-------|-------------|----------|
| `customers` | one per customer | customer_id (PK), name, email, city, state, signup_date | — |
| `products` | one per product | product_id (PK), category, price, weight_g | — |
| `sellers` | one per seller | seller_id (PK), city, state | — |
| `orders` | one per order | order_id (PK), customer_id, order_date, status | customers |
| `order_items` | one per line item | order_item_id (PK), order_id, product_id, seller_id, quantity, unit_price, freight | orders · products · sellers |
| `payments` | one per order | payment_id, order_id, payment_type, installments, amount | orders |

## Deliberate messiness (so data-quality practice is real)
- ~1% null `email`, `city`, `status`
- ~0.5% null `freight` (a numeric column contaminated by blanks — intentional)
- ~50 **exact duplicate** rows in `orders` (for dedup practice + a "broken primary key")

Don't "fix" the generator to remove these — cleaning them **is** the practice.

## Scaling
- Laptop / SQL / Python / modeling: `--orders 100000` (default) → runs fine in DuckDB.
- Spark / big-data lessons: `--orders 20000000`+ → generate on Databricks / a bigger box.

## Roadmap for this dataset
- **v1 (now):** the 6 core tables above.
- **v2 (later):** reviews (text → AI/embeddings) · clickstream_events (JSON → streaming) · price_history (SCD2) · geolocation (geo) · returns · marketing_campaigns.
