# Data Modeling for Data Engineering — Learning Series

> DE-2026 · Depth-first · **Grounded in real 2026 India DE interview + market research** (Jul 2026)
> **The skill that decides the "design a schema" interview.** Concept-first — the last foundation before Cloud.

## 🎯 What 2026 DE roles actually demand from data modeling (research-grounded)

- **~1 in 3 DE interviews includes data modeling**, and the signature format is *"design a schema for X."*
- **Candidates fail on WHY, not SQL** — they can't explain *why* a star schema, or the trade-offs. **Explaining trade-offs IS the skill.** This series teaches the WHY at every step.
- **Heavily tested:** normalization (1NF–3NF) · **Kimball dimensional modeling** (fact & dimension tables, star schema) · **grain** (the #1 concept) · **SCD types** (Type 2 is the one that matters) · fact/dimension types.
- **Modern 2026 must-knows:** **Medallion architecture** (Bronze/Silver/Gold — the lakehouse/Databricks pattern) · **Data Vault 2.0** (hubs/links/satellites, schema-drift) · **One Big Table (OBT)**. Kimball is NOT dead — it still powers ~90% of enterprise warehouses.
- Real stacks **combine** approaches: lakehouse + Data Vault (silver) + Kimball marts (gold), built with dbt + Airflow.

**Practice environment:** design on paper / dbdiagram.io → implement in **PostgreSQL / DuckDB** → (later) express as **dbt** models.

## 📌 Where this sits in the overall DE sequence

```
✅ Python   ✅ Spark   ✅ SQL (roadmap done)
👉 Data Modeling   ← YOU ARE HERE (builds on SQL; foundation for Cloud, warehouses, dbt)
   ☁️ Azure Cloud → 🔀 Airflow + dbt → 🏔️ Warehouses + Kafka
   (Linux · Git · Docker alongside · Projects P1–P3 at phase ends)
```

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Foundations of Data Modeling | 🟡 In Progress |
| Phase 1 | Normalization & Denormalization | ⏳ Pending |
| Phase 2 | Dimensional Modeling (Kimball) ★ the core | ⏳ Pending |
| Phase 3 | Modern Warehouse & Lakehouse Modeling | ⏳ Pending |
| Phase 4 | Applied · dbt · AI-Era | ⏳ Pending |

**Progress: 0 of ~21 lessons done.**

> Concept-first skill. Almost no tooling needed to *learn* it — the value is the WHY and the trade-offs. Every lesson drills "why this design, and what would break with a different one."

---

## Phase 0 — Foundations of Data Modeling 🟡

> What modeling is, why bad models are expensive, and the mental models everything builds on.

| # | Lesson | Status |
|---|--------|--------|
| 1 | What Data Modeling Is + Why It Matters (OLTP vs OLAP, cost of a bad model) | 🟡 Next |
| 2 | The 3 Levels — Conceptual → Logical → Physical | ⏳ Pending |
| 3 | Entities, Attributes, Relationships & ER Diagrams | ⏳ Pending |
| 4 | Keys & Cardinality — PK / FK / surrogate / natural · 1:1 / 1:N / M:N | ⏳ Pending |

---

## Phase 1 — Normalization & Denormalization ⏳

| # | Lesson |
|---|--------|
| 1 | Normalization I — 1NF · 2NF · 3NF (fixing a messy table step by step) |
| 2 | Normalization II — BCNF + **denormalization** (when & why to break the rules) |
| 3 | OLTP vs OLAP — why transactional and analytical models are different |

---

## Phase 2 — Dimensional Modeling (Kimball) ⏳ ★ the core

| # | Lesson |
|---|--------|
| 1 | Facts & Dimensions + the **Star Schema** |
| 2 | **Grain** — the single most important modeling decision ⭐ |
| 3 | Fact Table Types — transaction · periodic snapshot · accumulating snapshot |
| 4 | Dimension Types — conformed · degenerate · junk · role-playing |
| 5 | Star vs Snowflake Schema (and when to normalize a dimension) |
| 6 | **Slowly Changing Dimensions (SCD)** — Type 1 · 2 · 3 (+4/6), deep on Type 2 ⭐ |

---

## Phase 3 — Modern Warehouse & Lakehouse Modeling ⏳

| # | Lesson |
|---|--------|
| 1 | Kimball vs Inmon vs Data Vault — how to choose |
| 2 | **Data Vault 2.0** — hubs · links · satellites · handling schema drift |
| 3 | **Medallion Architecture** — Bronze / Silver / Gold (the lakehouse pattern) ⭐ |
| 4 | One Big Table (OBT) & full denormalization for query speed |

---

## Phase 4 — Applied · dbt · AI-Era ⏳

| # | Lesson |
|---|--------|
| 1 | The **"Design a Schema" Interview** — method, trade-offs, rubric ⭐ |
| 2 | Modeling with **dbt** — staging → marts, tests, docs, semantic/metrics layer |
| 3 | Modeling for Data Quality & Streaming / Real-time |
| 4 | **AI-Era Data Modeling** — AI-assisted design, why judgment & governance win ⭐ |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Foundations | 4 |
| Phase 1 · Normalization | 3 |
| Phase 2 · Dimensional (Kimball) | 6 |
| Phase 3 · Modern / Lakehouse | 4 |
| Phase 4 · Applied / dbt / AI-Era | 4 |
| **Total** | **~21 lessons** |

⭐ = high-leverage lessons flagged by the 2026 research (grain, SCD Type 2, medallion, the "design a schema" interview, AI-era modeling).

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions)*
*Spaced-repetition recall files live in [`revision/`](./revision/)*
*Sister series: [Spark](../spark/) · [Python](../python/) · [SQL](../sql/)*
