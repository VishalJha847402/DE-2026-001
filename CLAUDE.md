# DE-2026 — Teaching Rules (Python · Spark · SQL · Data Modeling · Azure · Airflow+dbt)

> **Single source of truth for how Claude teaches Vishal.** Replaces all previous rules. Follow exactly.
> Last updated: this session.

---

## 🔴 Core Working Rules (READ FIRST — apply every turn)

1. **ALWAYS read `CLAUDE.md` (this file) before writing any content or answering anything.**
2. **ALWAYS read `PENDING.md` before deciding what to do next.**
3. **After writing or changing content, UPDATE this file** (Section 10 progress; add new decisions/rules).
4. **After finishing or adding a task, UPDATE `PENDING.md`.**
5. If this file and reality disagree, fix the file to match reality.
6. **Before writing any roadmap or lesson, research the 2026 India / AI-era market — data-backed, no assumptions — and ask "is this the best?" If not, make it the best.**

> Never skipped. This file + `PENDING.md` are how context survives between sessions.

---

## 0. What This Project Is

Vishal is learning **Data Engineering** for the **2026 India job market**, pillar by pillar, as **markdown (`.md`) lesson files on GitHub** — NOT in chat, NOT in HTML. Vishal studies on GitHub in his own time.

Series so far (roadmaps built):
- 🐍 **Python for DE** — `python/`
- 🔥 **Spark & PySpark** — `spark/`
- 🗄️ **SQL for DE** — `sql/`
- 📐 **Data Modeling for DE** — `data-modeling/`
- ☁️ **Azure Cloud for DE** — `azure-cloud/`
- 🔀 **Airflow + dbt** — `airflow-dbt/`
- 🏗️ **Flagship project (OrderIQ)** — `projects/`

**Repo:** `VishalJha847402/DE-2026-001` · **Work branch:** `claude/new-session-gmnma2`.

### 🧭 Confirmed Skill Sequence
```
✅ Python · ✅ Spark · ✅ SQL · ✅ Data Modeling · ✅ Azure Cloud · ✅ Airflow+dbt (roadmaps done)
→ 🏔️ Warehouses (Snowflake/Delta/Iceberg) + Kafka (streaming)
   (Linux · Git · Docker alongside · Flagship project OrderIQ P1→P2→P3)
```

---

## 1. Where Content Lives — Folder Structure

```
CLAUDE.md      ← teaching rules (this file) — read before every action
PENDING.md     ← all pending / parked tasks — read before deciding next step

python/ · spark/ · sql/ · data-modeling/ · azure-cloud/ · airflow-dbt/   ← one folder per series:
  README.md · QUESTIONS.md · revision/ · phase-X/topic-Y/README.md
projects/      ← flagship project blueprint (OrderIQ)
```

One lesson = one `README.md` in its own topic folder. Pushed to GitHub on the work branch. Never in chat.

---

## 2. Lesson Structure — EVERY Lesson, No Exceptions

1. **Title + one-line hook**
2. **Why This Exists** — WHY first, always.
3. **Deep concept** — full clear sentences, depth-first, teach WHY. Analogies + real Indian DE scenarios (Flipkart, Swiggy, IRCTC, Zomato) + code/examples.
4. **A Mermaid diagram** in the `.md`.
5. **Revision** — short paragraphs, one per key idea.
6. **Practice Questions** — exactly **10** (3 Easy · 4 Medium · 3 Hard), answers hidden behind `<details><summary>▶ Answer</summary>…</details>`.
7. **"Next:"** link.

---

## 3. Plain-Language Standard (the A+ rule)

Simple plain language so **anybody can understand — without lowering depth.**
- **"🗣️ In plain words:"** one-liner under each tricky concept.
- Every hard word gets a **3-word plain meaning inline**, first time.
- Short sentences, especially in Hard answers. Each Hard answer opens with a one-line plain-words summary.
- Never trade technical accuracy for simplicity.

---

## 4. Teaching Style
Depth-first · WHY first · Simple English (short sentences, simple words, never dumbed down) · Analogies + Indian DE scenarios · multiple examples per concept.

---

## 5. Questions & Revision System
- **QUESTIONS.md** — index hub linking to each lesson's questions (never duplicate).
- **revision/** — one recall file every ~6 lessons: ⚡ Flash Recall · 🧠 Concept Recall · 🔀 Interleaved Hard Mix · 🏆 Boss Fight + Self-Score Tracker. Revisit +1 day / +1 week / +1 month, recall before revealing.

---

## 6. Learning Workflow
1. Claude writes a lesson → pushes to GitHub.
2. Vishal studies on GitHub in his own time.
3. Vishal signals **"done with X"** / **"X unclear at Y"**.
4. ~Every 6 lessons → revision file. End of Phase → gate-check / boss-fight.
- Pace: one lesson at a time unless asked. Vishal chooses which series to advance each turn.

---

## 7. The Roadmaps (each series README tracks its own progress)

- **Python** (`python/`) — ~34 lessons.
- **Spark** (`spark/`) — ~39 lessons, 15 Topics.
- **SQL** (`sql/`) — ~26 lessons. PostgreSQL + warehouse notes.
- **Data Modeling** (`data-modeling/`) — ~21 lessons (Kimball, grain, SCD, medallion, Data Vault, OBT).
- **Azure Cloud** (`azure-cloud/`) — ~24 lessons (ADLS, Databricks, ADF, Synapse, Fabric, DP-700).
- **Airflow + dbt** (`airflow-dbt/`) — ~21 lessons (dbt materializations/incremental/tests/snapshots/macros; Airflow DAGs/operators/sensors/XComs/scheduling; Cosmos integration). Practice: dbt Core+DuckDB, Airflow via Docker.
- **Flagship project** (`projects/`) — OrderIQ e-commerce lakehouse, staged P1→P2→P3.

**Future series (build later, same format):** Warehouses (Snowflake/Delta/Iceberg) + Kafka · Linux/Git/Docker. See `PENDING.md`.

---

## 8. Practice Environments
Python — local/notebooks · Spark — Databricks Community · SQL — PostgreSQL + DuckDB · Data Modeling — dbdiagram.io → PostgreSQL/DuckDB → dbt · Azure — Azure free account + Fabric trial + Databricks Community · Airflow+dbt — dbt Core+DuckDB, Airflow via Docker (Astro CLI).

---

## 9. Git Rules
Commit + push every lesson to `claude/new-session-gmnma2`. Clear messages. GitHub only.

---

## 10. Current Progress (update every session)

**Python — 2 done:** How Python Runs ✅ · Variables/Memory ✅. Next: Data Structures Deep.
**Spark — 9 done:** Phase 0 ✅ (3) · Phase 1: Driver ✅ · SparkSession ✅ · RDD ✅ · Transformations/Lazy ✅ · Narrow vs Wide ✅ · Shuffle ✅. Next: DAG→Stages→Tasks.
**SQL — 0 done:** roadmap ✅. Next: Phase 0 T1.
**Data Modeling — 0 done:** roadmap ✅. Next: Phase 0 T1.
**Azure Cloud — 0 done:** roadmap ✅. Next: Phase 0 T1.
**Airflow + dbt — 0 done:** roadmap ✅. Next: Phase 0 T1 — What dbt Is + Why.
**Project OrderIQ:** in-depth blueprint ✅ (build P1 after SQL+DataModeling foundations).
**Revision:** `spark/revision/revision-1-foundations-and-core.md` (Spark 1–9) ✅.

---

## 11. Pending Work
Full list in **`PENDING.md`**. Headline: plain-language retrofit (B-lite) — Shuffle ✅, 4 remaining (Narrow vs Wide, RDD, How Python Runs, Variables). All new lessons written to the Section 3 standard.
