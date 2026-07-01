# Orchestration & Transformation (Airflow + dbt) — Learning Series

> DE-2026 · Depth-first · **Grounded in real 2026 India DE market + interview research** (Jul 2026)
> The two paired "modern data stack" tools: **dbt** does the **T** (transform), **Airflow** does the **scheduling/orchestration**.

## 🎯 What 2026 DE roles actually demand (research-grounded)

- **Airflow** (orchestration, now **v3**) is a **non-negotiable** modern-DE skill. Core: **DAGs · Operators · Sensors · XComs** + scheduling, backfills, retries, executors/scaling.
  - **XCom trap** interviewers probe: XComs pass **metadata only** (IDs, paths, counts) — *never* large DataFrames (bloats the metadata DB).
- **dbt** (transformation / analytics engineering) is the standard for the **T in ELT**. Core: **4 materializations** (view/table/incremental/ephemeral) · **incremental models** · **tests** · **snapshots (SCD2)** · **macros/Jinja** · sources/refs/lineage · semantic layer. Has its own certification.
  - **The interview traps:** *"why did your incremental model reprocess the whole table?"* and *"why did a macro silently swallow a NULL and ship bad data?"* — debugging + trade-off reasoning.
- They're **used together:** Airflow schedules and orchestrates; dbt transforms + tests (often wired via **Cosmos**). Interviews probe *"ETL/ELT design + Airflow orchestration + dbt logic + lakehouse fluency"* as one skill.

**Practice environment:** **dbt Core + DuckDB/PostgreSQL** (free, local) · **Airflow via Docker** (Astro CLI / docker-compose). Both plug straight into the **OrderIQ** flagship project (P3).

## 📌 Where this sits in the overall DE sequence

```
✅ Python · ✅ Spark · ✅ SQL · ✅ Data Modeling · ✅ Azure Cloud (roadmaps done)
👉 Airflow + dbt   ← YOU ARE HERE (orchestrate + transform — the modern stack)
   → 🏔️ Warehouses (Snowflake/Delta/Iceberg) + Kafka (streaming)
   (Linux · Git · Docker alongside · Flagship project P3)
```

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | dbt Foundations (Transformation) | 🟡 In Progress |
| Phase 1 | dbt Production Skills | ⏳ Pending |
| Phase 2 | Airflow Foundations (Orchestration) | ⏳ Pending |
| Phase 3 | Airflow Production Skills | ⏳ Pending |
| Phase 4 | The Modern Stack Together | ⏳ Pending |

**Progress: 0 of ~21 lessons done.**

> **dbt first, Airflow second** — dbt builds directly on your SQL + Data Modeling (it's SQL transformation), so it's the natural next step. Airflow then orchestrates it. Phase 4 wires them together.

---

## Phase 0 — dbt Foundations (Transformation) 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | What dbt Is + Why (ELT vs ETL, "analytics engineering", the T in ELT) | 🟡 Next |
| 2 | dbt Project Setup — structure, `profiles.yml`, dbt Core vs Cloud |  ⏳ Pending |
| 3 | Models, `ref()`, `source()` & the Lineage DAG | ⏳ Pending |
| 4 | Materializations — view · table · incremental · ephemeral (when & why each) | ⏳ Pending |

---

## Phase 1 — dbt Production Skills ⏳

| # | Lesson |
|---|--------|
| 1 | **Incremental Models** — `is_incremental()`, MERGE, the "why did it reprocess everything?" trap ⭐ |
| 2 | **Testing** — generic (unique · not_null · relationships · accepted_values) · singular · `dbt_expectations` ⭐ |
| 3 | **Snapshots** — SCD Type 2 in dbt (timestamp / check strategy) |
| 4 | Macros & Jinja + packages (`dbt_utils`) — reusable, DRY SQL |
| 5 | Sources · Seeds · Docs · Exposures · Semantic / Metrics layer |

---

## Phase 2 — Airflow Foundations (Orchestration) ⏳

| # | Lesson |
|---|--------|
| 1 | What Airflow Is + Why (orchestration vs cron, DAGs) |
| 2 | Airflow Architecture — scheduler · executor · workers · metadata DB · webserver |
| 3 | Writing DAGs — TaskFlow API, tasks & dependencies (Airflow 3) |
| 4 | Operators — Bash · Python · provider operators · task groups & branching |

---

## Phase 3 — Airflow Production Skills ⏳

| # | Lesson |
|---|--------|
| 1 | Sensors & Deferrable Operators — waiting for external conditions |
| 2 | **XComs** — passing metadata (never big data) + the trap ⭐ |
| 3 | Scheduling, Backfills, Catchup, Retries, SLAs, Alerting & Data-Aware scheduling (Datasets) |
| 4 | Connections · Hooks · Variables · Dynamic DAGs |
| 5 | Executors & Scaling — Local / Celery / Kubernetes + deployment |

---

## Phase 4 — The Modern Stack Together ⏳

| # | Lesson |
|---|--------|
| 1 | **Airflow Orchestrating dbt** — Cosmos & the real-world pattern ⭐ |
| 2 | End-to-End Pipeline — ingest → dbt transform → test → serve (scheduled, monitored) |
| 3 | Production Practices — CI/CD, idempotency, observability, cost |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · dbt Foundations | 4 |
| Phase 1 · dbt Production | 5 |
| Phase 2 · Airflow Foundations | 4 |
| Phase 3 · Airflow Production | 5 |
| Phase 4 · Together | 3 |
| **Total** | **~21 lessons** |

⭐ = high-leverage lessons flagged by the 2026 research (incremental models, dbt testing, XComs, Airflow-orchestrating-dbt).

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions)*
*Spaced-repetition recall files live in [`revision/`](./revision/)*
*Sister roadmaps: [Python](../python/) · [Spark](../spark/) · [SQL](../sql/) · [Data Modeling](../data-modeling/) · [Azure Cloud](../azure-cloud/) · [Project: OrderIQ](../projects/)*
