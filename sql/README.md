# SQL for Data Engineering — Learning Series

> DE-2026 · Depth-first · **Grounded in real 2026 India DE interview + job research** (Jul 2026)
> **Not a generic SQL tutorial — SQL *for Data Engineering*, taught for the AI era.** Every topic earns its place.

## 🎯 What 2026 DE roles actually demand from SQL (research-grounded)

Across every source (interview banks, dbt's State of Analytics Engineering 2026, real rounds at TCS/Infosys/Deloitte):

- **SQL is the #1 tested skill in DE interviews.** Universal, non-negotiable.
- **AI does NOT replace SQL — it raises the bar.** Tools like QueryGPT *generate* SQL, but DEs must **read, verify, and optimize** it. SQL becomes a **judgment skill**: knowing *why* a query is efficient, and *when to trust* AI output. 72% of teams use AI-assisted coding; validation/governance lags — that gap is where the DE adds value.
- **Heavily tested:** JOINs · **window functions** (#1 topic) · **CTEs** (incl. recursive) · aggregations · dedup.
- **The differentiator:** **query optimization** — execution plans, indexes, join strategies, partitioning, materialization. Interviews ask *"why is this efficient?"*
- **Most-missed foundation:** the *logical order of query execution*.

This roadmap is built to cover exactly that — foundations → analytical SQL → performance internals → warehouse & AI-era SQL.

**Teaching dialect:** **PostgreSQL** (the standard, powerful, free base) — with **warehouse-dialect differences** (Snowflake / BigQuery) called out where they matter.
**Practice environment:** PostgreSQL (free cloud tier or local) + **DuckDB** for fast local analytical practice.

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | SQL Foundations Re-grounded | 🟡 In Progress |
| Phase 1 | Core Querying (the daily bread) | ⏳ Pending |
| Phase 2 | Analytical SQL (interview gold) | ⏳ Pending |
| Phase 3 | Data Definition & Modeling in SQL | ⏳ Pending |
| Phase 4 | Performance & Internals (the differentiator) | ⏳ Pending |
| Phase 5 | Modern · Warehouse · AI-Era SQL | ⏳ Pending |

**Progress: 1 of ~26 lessons done.**

> You know SQL at a "functional" level (you write queries to fetch data). Per our teaching rule, we run the **full cycle even on topics you know** — functional SQL hides holes (execution order, why a query is slow, indexes). Speed-read the easy parts; slow down on the WHY, the internals, and optimization.

---

## Phase 0 — SQL Foundations Re-grounded 🟡

> Fix the hidden holes. The mental models that make everything else click.

| # | Lesson | Status |
|---|--------|--------|
| 1 | [What SQL Is + The Relational Model (tables, keys, relationships)](./phase-0-foundations/topic-1-relational-model/) | ✅ Done |
| 2 | How a Query Actually Executes — the logical order of operations ⭐ | 🟡 Next |
| 3 | SELECT · WHERE · filtering · operators · NULL basics | ⏳ Pending |
| 4 | Sorting · DISTINCT · LIMIT · pagination | ⏳ Pending |

---

## Phase 1 — Core Querying ⏳ (the daily bread)

| # | Lesson |
|---|--------|
| 1 | JOINs Deep — inner / left / right / full / cross / self + how they work + semi/anti |
| 2 | Aggregations · GROUP BY · HAVING |
| 3 | Subqueries — scalar · correlated · IN / EXISTS |
| 4 | CTEs — `WITH`, chained, and recursive |
| 5 | Set Operations — UNION / INTERSECT / EXCEPT |
| 6 | CASE · COALESCE · NULL logic deep (the classic gotcha) |

---

## Phase 2 — Analytical SQL ⏳ (interview gold — the #1 tested area)

| # | Lesson |
|---|--------|
| 1 | Window Functions I — ranking (ROW_NUMBER, RANK, DENSE_RANK, NTILE) |
| 2 | Window Functions II — offset & aggregate (LEAD, LAG, running totals, moving averages, frames) |
| 3 | Advanced Patterns — dedup · top-N per group · gaps & islands · pivot / unpivot |
| 4 | Date/Time & String Functions for Analytics |

---

## Phase 3 — Data Definition & Modeling in SQL ⏳

| # | Lesson |
|---|--------|
| 1 | DDL — CREATE, data types, constraints, primary/foreign keys |
| 2 | Normalization vs Denormalization (when & why) |
| 3 | Dimensional Modeling in SQL — star/snowflake, facts & dims, SCD (intro; full depth in future Data Modeling series) |

---

## Phase 4 — Performance & Internals ⏳ (the differentiator)

| # | Lesson |
|---|--------|
| 1 | How the Query Optimizer Works + Reading Execution Plans (`EXPLAIN`) ⭐ |
| 2 | Indexes Deep — B-tree, composite, covering, when they hurt |
| 3 | Query Optimization Techniques — sargable predicates, avoiding full scans, join strategies (hash / merge / nested loop) |
| 4 | Partitioning · Materialized Views · Statistics |
| 5 | Transactions · ACID · Isolation Levels · Locking · MVCC |

---

## Phase 5 — Modern · Warehouse · AI-Era SQL ⏳

| # | Lesson |
|---|--------|
| 1 | Analytical Warehouses — how Snowflake / BigQuery SQL differs (columnar, distribution, clustering, `QUALIFY`) |
| 2 | Semi-Structured Data in SQL — JSON, arrays, nested fields |
| 3 | SQL for DE — Spark SQL, dbt models, ELT patterns, SQL-based data-quality checks |
| 4 | **AI-Era SQL** — reading & verifying AI-generated SQL, judgment, governance, when to trust ⭐ |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Foundations | 4 |
| Phase 1 · Core Querying | 6 |
| Phase 2 · Analytical SQL | 4 |
| Phase 3 · Definition & Modeling | 3 |
| Phase 4 · Performance & Internals | 5 |
| Phase 5 · Modern / Warehouse / AI-Era | 4 |
| **Total** | **~26 lessons** |

⭐ = high-leverage lessons flagged by the 2026 research (execution order, execution plans, AI-era SQL).

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions)*
*Spaced-repetition recall files live in [`revision/`](./revision/)*
*Sister series: [Spark](../spark/) · [Python](../python/)*
