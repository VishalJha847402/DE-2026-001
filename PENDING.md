# PENDING — All Parked / Pending Tasks

> Read before deciding what to do next (CLAUDE.md Core Working Rule #2).
> Finish a task → remove it + update CLAUDE.md Section 11. New task → add here.
> Last updated: this session.

---

## 🎉 Status: ALL PLANNING COMPLETE ✅ (15 series + project + practice + dataset + teaching rules — all locked)

Only work now = **build the dataset tooling, then write lessons + practice sets**.

```
Systems locked: Practice §6 · 3-step examples §2B · Dataset (wide+long e-commerce) §9C · Environments §9
```

---

## 🛠️ 1. Dataset Tooling — BUILD FIRST (locked, §9C + §9C-i)
- ⬜ **WIDE + LONG e-commerce generator** — enriched schema (core tables + price_history, shipments, returns, campaigns, clickstream_events) with varied column types (numeric, text/reviews, timestamps, geo, JSON/nested, PII, deliberate messiness, changing attributes for SCD2). Scalable ~100k → 20–100M rows.
- ⬜ **DuckDB seed** — 2-minute load of the ~100k-row dataset for SQL/Python/modeling practice.
- ⬜ (later) NYC Taxi loader — Spark Phase-4 big-data lessons only.

**Why first:** hands-on practice (§6) isn't real until the wide+long data is runnable.

---

## 📚 2. Next Lessons to Write (each ships with `practice.md` on the e-commerce dataset)
- **Python** — Phase 0 T3: Data Structures Deep (first code-heavy lesson, §2A + §2B)
- **Spark** — Phase 1 T4b: DAG → Jobs → Stages → Tasks
- All other 13 series — Phase 0 T1.

---

## 🔧 3. Plain-Language Retrofit (B-lite) — IN PROGRESS
- ✅ The Shuffle (Spark) — DONE
- ⬜ Narrow vs Wide (Spark) · ⬜ RDD (Spark) · ⬜ How Python Runs (Python) · ⬜ Variables & Memory (Python)

**Status: 1 of 5 done. 4 remaining.**

---

## 🔁 4. Revision — Pending Confirm
- **Phase-wise revision** (cumulative, after each phase) instead of every-6-lessons — agreed better, **awaiting Vishal's explicit "update"** to change CLAUDE.md §5 + restructure existing Spark revision.
- Fix Self-Score Tracker → clickable `- [ ]` task-list (not table) + Google Sheet as durable tracker.

---

## 🏗️ 5. Flagship Project — blueprint DONE (`projects/README.md`)
OrderIQ (e-commerce, wide+long), 3 stages: P1 (after SQL Ph0–2 + Data Modeling Ph0–2 + Python) → P2 (after Spark+Azure) → P3 (after Airflow/dbt/Kafka + AI-Era). Same dataset as all practice.

---

## 🗺️ 6. Optional Later Work
- ⬜ Sharper market grounding: paste 20–30 real JDs → precise skill tally.
- ⬜ Master `DE-ROADMAP.md` — top-level map of all 15 series + project.
- ⬜ Cross-series overlap review (Delta/medallion appear in multiple series).

---

## 🧭 7. Open Decisions
- **Pace/signal protocol** — "done / unclear / too easy|too hard / paste-solution".
- **AI-era DE definition** — A/B/C "replace vs assist vs own" framing to lock into a lesson.
