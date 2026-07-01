# PENDING — All Parked / Pending Tasks

> Read before deciding what to do next (CLAUDE.md Core Working Rule #2).
> Finish a task → remove it + update CLAUDE.md Section 11. New task → add here.
> Last updated: this session.

---

## 🎉 Status: ALL PLANNING COMPLETE ✅ (15 series + project + practice system + dataset — all locked)

Only work now = **build the dataset tooling, then write lessons + practice sets**.

```
Core (7):  Python · Spark · SQL · Data Modeling · Azure · Airflow+dbt · Warehouses+Streaming
Support(3):Linux · Git · Docker
Tier 3 (5):DataOps(CI/CD+IaC) · Kubernetes · Governance & Security · System Design · AI-Era DE
Project:   OrderIQ blueprint
Systems:   Practice & Problem-Solving 🔒 · Dataset Strategy 🔒 (CLAUDE.md §6, §9C)
```

---

## 🛠️ 1. Dataset Tooling — BUILD FIRST (locked, §9C)
- ⬜ **E-commerce data generator** — produces the OrderIQ (Olist-style) schema at any size: ~100k rows (laptop) → 20–100M rows (Spark/cloud).
- ⬜ **DuckDB seed** — 2-minute setup that loads the ~100k-row dataset into DuckDB for SQL/Python/modeling practice.
- ⬜ (later) NYC Taxi loader — for the 1–2 Spark Phase-4 big-data performance lessons only.

**Why first:** hands-on practice (§6) isn't real until the data is runnable.

---

## 📚 2. Next Lessons to Write (each ships with a `practice.md` on the e-commerce dataset)
- **Python** — Phase 0 T3: Data Structures Deep (first code-heavy lesson)
- **Spark** — Phase 1 T4b: DAG → Jobs → Stages → Tasks
- All other 13 series — Phase 0 T1.

---

## 🔧 3. Plain-Language Retrofit (B-lite) — IN PROGRESS
- ✅ The Shuffle (Spark) — DONE
- ⬜ Narrow vs Wide (Spark) · ⬜ RDD (Spark) · ⬜ How Python Runs (Python) · ⬜ Variables & Memory (Python)

**Status: 1 of 5 done. 4 remaining.**

---

## 🔁 4. Revision — Pending Confirm
- **Phase-wise revision** (revise after each phase, cumulative) instead of every-6-lessons — agreed better, **awaiting Vishal's explicit "update"** to change CLAUDE.md §5 + restructure existing Spark revision.
- Fix Self-Score Tracker → clickable `- [ ]` task-list (not table) + note Google Sheet as durable tracker.

---

## 🏗️ 5. Flagship Project — blueprint DONE (`projects/README.md`)
OrderIQ (e-commerce), 3 stages: P1 (after SQL Ph0–2 + Data Modeling Ph0–2 + Python) → P2 (after Spark+Azure) → P3 (after Airflow/dbt/Kafka + AI-Era). Same dataset as all practice. Grow ONE project.

---

## 🗺️ 6. Optional Later Work
- ⬜ Sharper market grounding: paste 20–30 real JDs → precise skill tally (Naukri/LinkedIn scraping blocked, 403).
- ⬜ Master `DE-ROADMAP.md` — one top-level file linking all 15 series + project.
- ⬜ Cross-series overlap review (Delta/medallion appear in multiple series).

---

## 🧭 7. Open Decisions
- **Pace/signal protocol** — current = "done with X" / "X unclear at Y" / "too easy|too hard" / paste-solution-for-grading.
- **AI-era DE definition** — has its own roadmap (`ai-era-de/`); A/B/C "replace vs assist vs own" framing to lock into a lesson.
