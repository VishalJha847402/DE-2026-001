# PENDING — All Parked / Pending Tasks

> Read this before deciding what to do next (per CLAUDE.md Core Working Rule #2).
> When a task is finished, remove it and update CLAUDE.md Section 10. When a new task is agreed, add it here.
>
> Last updated: this session.

---

## 🔧 1. Plain-Language Retrofit (B-lite) — IN PROGRESS

Apply the CLAUDE.md Section 3 plain-language standard to the 5 densest existing lessons:

- ✅ The Shuffle (Spark) — DONE
- ⬜ Narrow vs Wide (Spark)
- ⬜ RDD (Spark)
- ⬜ How Python Runs (Python)
- ⬜ Variables & Memory (Python)

**Status: 1 of 5 done. 4 remaining.**

---

## 📚 2. Next Lessons to Write

**SQL (roadmap ✅ done, market-grounded):**
- 🟡 Phase 0 Topic 1 — What SQL Is + The Relational Model
- Phase 0 Topic 2 — How a Query Actually Executes (logical order)
- … then Phases 0→5 (see `sql/README.md`)

**Python:**
- 🟡 Phase 0 Topic 3 — Data Structures Deep (list/dict/set/tuple + collections)
- … then Phase 0 Topic 4 (Control Flow), Topic 5 (Functions) → Phase 1 onward (see `python/README.md`)

**Spark:**
- 🟡 Phase 1 Topic 4b — DAG → Jobs → Stages → Tasks
- … then 4c (Fault Tolerance), Topic 5 (Partitioning/Memory/Cache) → Phase 2 onward (see `spark/README.md`)

---

## 🔁 3. Revision Files (spaced repetition)

- ✅ `spark/revision/revision-1-foundations-and-core.md` (Spark 1–9)
- ⬜ Python revision #1 — due after ~6 Python lessons (have 2)
- ⬜ SQL revision #1 — due after ~6 SQL lessons (have 0)
- ⬜ Spark revision #2 — due after Phase 1 completes

---

## 📊 4. Optional — Sharper Market Grounding

- Roadmaps grounded in 2026 India research (blogs + job-board titles/counts + interview banks).
- Could not scrape raw Naukri/LinkedIn JD text (they block bots, 403).
- **If Vishal wants exact numbers:** he pastes 20–30 real JDs → Claude does a precise skill-frequency tally. Parked until requested.

---

## 🏗️ 5. Future Series (after Python + Spark + SQL mature)

Depth-first — build as their own `.md` series later, same format:
- Data Modeling (star/snowflake, SCD, dimensional) — deeper than the SQL Phase 3 intro
- Azure Cloud (ADF, Databricks, Synapse, Fabric)
- Airflow + dbt (orchestration)
- Snowflake / Delta / Iceberg (warehouses) + Kafka (streaming)
- Linux · Git · Docker (supporting tools, picked up alongside)
- Projects P1 (SQL analytics), P2 (end-to-end pipeline), P3 (AI-era pipeline)

Do NOT start these until the core pillars are well underway.

---

## 🧭 6. Open Decisions (not yet locked)

- **Pace/signal protocol** — current signal = "done with X" / "X unclear at Y". Could formalize later.
- **AI-era DE definition** — which DE tasks AI replaces vs assists vs Vishal owns deeply. Drafted in chat, not locked.
- **Master `DE-ROADMAP.md`** — a top-level file mapping all pillars (offered, not yet created).
