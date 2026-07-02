# PENDING — All Parked / Pending Tasks

> Read before deciding what to do next (CLAUDE.md Core Working Rule #2).
> Finish a task → remove it + update CLAUDE.md §11. New task → add here.
> Last updated: this session.

---

## 🎉 Status: BUILDING PHASE — dataset v1 ✅, lessons shipping

Locked systems: Practice §6 · 3-step examples §2B · Dataset (wide+long e-commerce) §9C · Environments §9 · **Build-in-Public Content System → `content-system.md`** (authoritative).

```
Progress: Python Phase 0 ✅ (5/5) · SQL Phase 0 ✅ (4/26) · Azure 3/24 · Spark retrofit 2/6
```

---

## ⚡ 0. Token / Efficiency Convention
- **Big new rules go in their OWN small file** (like `content-system.md`), NOT crammed into CLAUDE.md — keeps CLAUDE.md lean and updates cheap.
- **Batch CLAUDE.md updates** — don't rewrite it for every micro-decision.
- **Use a FRESH session for lesson-writing** — a new session reads CLAUDE.md + PENDING.md (+ referenced rule files) and has full context cheaply. Long sessions re-process everything = token drain.
- Authoritative files chain: **CLAUDE.md + PENDING.md + referenced rule files** (`content-system.md`, future `/rules/*`).

---

## 🔧 1. FORMAT RETROFIT QUEUE (active — do in order)
Bring pre-format lessons to the locked standard (🎯 first-principle banner · 🗣️ plain-words · 3-step example · separate `practice.md` on OrderIQ):
- ⬜ **Python T1 — How Python Runs** (no practice.md, no plain-words) ← NEXT
- ⬜ **Python T2 — Variables/Memory** (same)
- ⬜ Spark P1-T3 RDD/Lineage · ⬜ P1-T3b Lazy Eval · ⬜ P1-T3c Narrow/Wide · ⬜ P1-T4a Shuffle
- ⬜ SQL T1 + T2 — add 🎯 first-principle banner only (cosmetic)
- ✅ Spark P1-T1 Driver/Executors · ✅ Spark P1-T2 SparkSession
- ℹ️ Spark Phase 0 (3 lessons) — stays old format per Vishal ("start from phase 1"). Revisit only if he asks.

## 🛠️ 2. Dataset Tooling
- ✅ v1 generator (`datasets/generate.py`) + DuckDB seed (`seed_duckdb.py`) + README.
- ⬜ v2 enrichments (build when a lesson needs them): reviews · geolocation · categories · price_history (SCD2) · shipments · returns · campaigns · clickstream JSON.
- ⬜ (later) NYC Taxi loader — Spark Phase-4 only.

## 📚 3. Next Lessons (each ships with `practice.md` on OrderIQ)
- Python Phase 1 T1: Iterators & Generators · SQL Phase 1 T1: JOINs Deep · Azure T4: Data Stack Map (finishes its Phase 0) · Spark (after retrofit): DAG→Stages→Tasks.
- Vishal has pending self-work: Python Phase-0 Boss Fight (paste solution → grade) · SQL Phase-0 gate · Azure account setup + rg-orderiq-dev + budget alert.

## 📣 4. Content — build a "Content Pack" per lesson (`content-system.md`)
- Start LinkedIn + X. Claude drafts pack; Vishal adds real touch + posts. (Not started.)

## 🔁 5. Revision — Pending Confirm
- Phase-wise revision (cumulative) instead of every-N-lessons — awaiting Vishal's "update". Fix Self-Score Tracker → clickable `- [ ]` + Google Sheet.
- ✅ python/revision/phase-0-revision.md shipped (4-layer). SQL Phase-0 gate lives in SQL T4 practice.

## 🏗️ 6. Flagship Project — blueprint done (`projects/README.md`)
OrderIQ P1 (after SQL Ph0–2 + Data Modeling Ph0–2 + Python) → P2 (Spark+Azure) → P3 (Airflow/dbt/Kafka+AI). Same dataset as practice.

## 🗺️ 7. Optional Later
- Master `DE-ROADMAP.md` · cross-series overlap dedupe · sharper JD grounding (paste 20–30 JDs) · (optional) refactor CLAUDE.md into lean index + `/rules/*` modules.

## 🧭 8. Open Decisions
- Pace/signal protocol · AI-era DE A/B/C framing to lock into a lesson.
