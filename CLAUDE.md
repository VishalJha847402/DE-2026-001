# DE-2026 — Teaching Rules (Spark · Python · SQL · Data Modeling)

> **Single source of truth for how Claude teaches Vishal.**
> These rules replace all previous rules. Follow them exactly.
> Last updated: this session.

---

## 🔴 Core Working Rules (READ FIRST — apply every turn)

1. **ALWAYS read `CLAUDE.md` (this file) before writing any content or answering anything.**
2. **ALWAYS read `PENDING.md` before deciding what to do next.**
3. **After writing or changing content, UPDATE this file** (Section 10 progress; add new decisions/rules here).
4. **After finishing or adding a task, UPDATE `PENDING.md`.**
5. If this file and reality disagree, fix the file to match what we actually did.
6. **Before writing any roadmap or lesson, research the 2026 India / AI-era market — data-backed, no assumptions — and ask "is this the best?" If not, make it the best.**

> Never skipped. This file + `PENDING.md` are how context survives between sessions.

---

## 0. What This Project Is

Vishal is learning **Data Engineering** for the **2026 India job market**, pillar by pillar, as **markdown (`.md`) lesson files on GitHub** — NOT in chat, NOT in HTML. Vishal studies on GitHub in his own time.

Series so far:
- 🐍 **Python for DE** — `python/`
- 🔥 **Spark & PySpark** — `spark/`
- 🗄️ **SQL for DE** — `sql/`
- 📐 **Data Modeling for DE** — `data-modeling/`

**Repo:** `VishalJha847402/DE-2026-001` · **Work branch:** `claude/new-session-gmnma2`.

### 🧭 Confirmed Skill Sequence
```
✅ Python · ✅ Spark · ✅ SQL (roadmap) · 👉 Data Modeling (roadmap done, lessons next)
→ ☁️ Azure Cloud → 🔀 Airflow + dbt → 🏔️ Warehouses (Snowflake/Delta/Iceberg) + Kafka
   (Linux · Git · Docker alongside · Projects P1–P3 at phase ends)
```
Rationale: Data Modeling before Cloud — it builds on SQL and is the conceptual foundation Cloud/warehouse/dbt work assumes.

---

## 1. Where Content Lives — Folder Structure

```
CLAUDE.md                       ← teaching rules (this file) — read before every action
PENDING.md                      ← all pending / parked tasks — read before deciding next step

python/ · spark/ · sql/ · data-modeling/   ← one folder per series, each with:
  README.md                     ← roadmap + progress
  QUESTIONS.md                  ← index hub linking to every lesson's questions
  revision/                     ← spaced-repetition recall files
  phase-X-name/topic-Y-name/README.md   ← the lesson
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
- Never trade technical accuracy for simplicity — wrap depth in simple words.

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
3. Vishal signals **"done with X"** / **"X unclear at Y"** — the pace signal.
4. ~Every 6 lessons → revision file. End of Phase → gate-check / boss-fight.
- Pace: one lesson at a time unless asked for more. Vishal chooses which series to advance each turn.

---

## 7. The Roadmaps (each series README tracks its own progress)

- **Python** (`python/README.md`) — ~34 lessons, market-grounded (Polars/DuckDB, pydantic, itertools, pathlib, concurrent.futures, Airflow/dbt glue).
- **Spark** (`spark/README.md`) — ~39 lessons, 15 Topics.
- **SQL** (`sql/README.md`) — ~26 lessons, market-grounded (window functions, CTEs, execution plans/optimization, AI-era SQL). Dialect: PostgreSQL + warehouse notes.
- **Data Modeling** (`data-modeling/README.md`) — ~21 lessons, market-grounded (Kimball/star, grain, SCD Type 2, medallion, Data Vault 2.0, OBT, "design a schema" interview, AI-era). Practice: dbdiagram.io → PostgreSQL/DuckDB → dbt.

**Future series (build later, same format):** Azure Cloud · Airflow + dbt · Warehouses + Kafka · Linux/Git/Docker · Projects P1–P3. See `PENDING.md`.

---

## 8. Practice Environments
- **Python** — local / notebooks.  **Spark** — Databricks Community.  **SQL** — PostgreSQL + DuckDB.  **Data Modeling** — dbdiagram.io / paper → PostgreSQL/DuckDB → dbt.

---

## 9. Git Rules
Commit + push every lesson to `claude/new-session-gmnma2`. Clear messages. GitHub only.

---

## 10. Current Progress (update every session)

**Python — 2 done:** How Python Runs ✅ · Variables/Memory ✅. Next: Data Structures Deep.
**Spark — 9 done:** Phase 0 ✅ (3) · Phase 1: Driver ✅ · SparkSession ✅ · RDD ✅ · Transformations/Lazy ✅ · Narrow vs Wide ✅ · Shuffle ✅. Next: DAG→Stages→Tasks.
**SQL — 0 done:** roadmap ✅. Next: Phase 0 T1 — What SQL Is + Relational Model.
**Data Modeling — 0 done:** roadmap ✅. Next: Phase 0 T1 — What Data Modeling Is + Why It Matters.
**Revision:** `spark/revision/revision-1-foundations-and-core.md` (Spark 1–9) ✅.

---

## 11. Pending Work
Full list in **`PENDING.md`**. Headline: plain-language retrofit (B-lite) — Shuffle ✅, 4 remaining (Narrow vs Wide, RDD, How Python Runs, Variables). All new lessons written to the Section 3 standard.
