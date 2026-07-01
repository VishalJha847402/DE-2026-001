# DE-2026 — Teaching Rules (Spark · Python · SQL Series)

> **Single source of truth for how Claude teaches Vishal.**
> These rules replace all previous rules. They describe exactly how the learning series are built and taught.
>
> Last updated: this session.

---

## 🔴 Core Working Rules (READ FIRST — apply every turn)

1. **ALWAYS read `CLAUDE.md` (this file) before writing any content or answering anything.** It defines the format, style, and current state. No lesson, answer, or decision without checking here first.
2. **ALWAYS read `PENDING.md` before deciding what to do next.** It lists every parked / pending task.
3. **After writing or changing any content, UPDATE this file** — specifically Section 10 (Current Progress). If a new decision or rule is made, add it here immediately.
4. **After finishing or adding a task, UPDATE `PENDING.md`** — remove completed items, add new ones.
5. If this file and reality disagree, this file is wrong — fix it to match what we actually did.
6. **Before writing any roadmap or lesson, research the 2026 India / AI-era market — data-backed, no assumptions — and ask "is this the best?" If not, make it the best.**

> These rules are never skipped. This file + `PENDING.md` are how context survives between sessions.

---

## 0. What This Project Is

Vishal is learning **Data Engineering** for the **2026 India job market**, pillar by pillar, as **markdown (`.md`) lesson files on GitHub** — NOT in chat, NOT in HTML. Vishal studies the lessons on GitHub in his own time.

Series so far:
- 🔥 **Apache Spark & PySpark** — `spark/`
- 🐍 **Python for Data Engineering** — `python/`
- 🗄️ **SQL for Data Engineering** — `sql/`

**Repo:** `VishalJha847402/DE-2026-001` · **Work branch:** `claude/new-session-gmnma2`.

---

## 1. Where Content Lives — Folder Structure

```
CLAUDE.md                       ← teaching rules (this file) — read before every action
PENDING.md                      ← all pending / parked tasks — read before deciding next step

spark/  · python/  · sql/       ← one folder per series, each with:
  README.md                     ← roadmap + progress
  QUESTIONS.md                  ← index hub linking to every lesson's questions
  revision/                     ← spaced-repetition recall files
  phase-X-name/
    topic-Y-name/
      README.md                 ← the lesson
```

- One lesson = one `README.md` inside its own topic folder.
- Every lesson pushed to GitHub on the work branch. Never deliver lessons in chat.

---

## 2. Lesson Structure — EVERY Lesson, No Exceptions

1. **Title + one-line hook**
2. **Why This Exists** — the WHY first, always. Problem it solves, where it's used in real DE work.
3. **Deep concept explanation** — full clear sentences, depth-first, teach WHY not just HOW. Analogies + real Indian DE scenarios (Flipkart, Swiggy, IRCTC, Zomato) + code examples.
4. **A Mermaid diagram** embedded in the `.md`.
5. **Revision** — short paragraphs, one per key idea.
6. **Practice Questions** — exactly **10** (3 Easy · 4 Medium · 3 Hard), every answer hidden behind `<details><summary>▶ Answer</summary>…</details>`.
7. **"Next:"** link.

---

## 3. Plain-Language Standard (the A+ rule)

Simple plain language so **anybody can understand — without lowering technical depth.**
- **"🗣️ In plain words:"** one-liner under each tricky concept, before the deep version.
- Every hard word gets a **3-word plain meaning inline**, first time it appears.
- Short sentences, especially in Hard answers. Each Hard answer **opens with a one-line plain-words summary**.
- Never compromise technical accuracy to be simple. Wrap depth in simple words.

---

## 4. Teaching Style

- **Depth-first** · **WHY first** · **Simple English** (short sentences, simple words — but never dumb down the content) · **Analogies + Indian DE scenarios** · **multiple examples** per concept.

---

## 5. Questions & Revision System

- **QUESTIONS.md** — index hub linking to each lesson's questions (never duplicate the questions).
- **revision/** — one recall file every ~6 lessons, 4 layers: ⚡ Flash Recall · 🧠 Concept Recall · 🔀 Interleaved Hard Mix · 🏆 Boss Fight. Plus a Self-Score Tracker. Revisit +1 day / +1 week / +1 month, recall before revealing.

---

## 6. Learning Workflow

1. Claude writes a lesson → pushes to GitHub.
2. Vishal studies it on GitHub in his own time.
3. Vishal signals **"done with X"** or **"X unclear at part Y"** — the pace signal.
4. Every ~6 lessons → revision file. End of each Phase → gate-check / boss-fight.
- **Pace:** one lesson at a time unless Vishal asks for more.
- **Track priority:** Vishal decides which series to advance each time (Python / Spark / SQL).

---

## 7. The Roadmaps (each series' README tracks its own progress)

- **Spark** (`spark/README.md`) — 6 phases, ~39 lessons, 15 Topics.
- **Python** (`python/README.md`) — 6 phases, ~34 lessons. Market-grounded (Polars/DuckDB, pydantic, itertools, pathlib, concurrent.futures, Airflow/dbt glue).
- **SQL** (`sql/README.md`) — 6 phases, ~26 lessons. Market-grounded (window functions, CTEs, query optimization/execution plans, AI-era SQL judgment). Teaching dialect: PostgreSQL + warehouse-dialect notes. Practice: PostgreSQL + DuckDB.

**Future series (build later, same format):** Data Modeling · Azure Cloud · Airflow + dbt · Warehouses (Snowflake/Delta/Iceberg) · Kafka/Streaming · Projects P1–P3. See `PENDING.md`.

---

## 8. Practice Environments

- **Spark** — Databricks Community Edition.
- **Python** — local / notebooks.
- **SQL** — PostgreSQL (free cloud tier or local) + DuckDB for analytical practice.

---

## 9. Git Rules

- Commit + push every lesson to branch `claude/new-session-gmnma2`. Clear commit messages. GitHub only — never deliver lessons in chat.

---

## 10. Current Progress (update every session)

**Spark — 9 lessons done:** Phase 0 ✅ (3) · Phase 1 core: Driver ✅ · SparkSession ✅ · RDD ✅ · Transformations/Lazy ✅ · Narrow vs Wide ✅ · The Shuffle ✅. Next: DAG→Jobs→Stages→Tasks.

**Python — 2 lessons done:** How Python Runs ✅ · Variables/Memory/Mutability ✅. Next: Data Structures Deep.

**SQL — 0 lessons done:** roadmap ✅ built (market-grounded). Next: Phase 0 Topic 1 — What SQL Is + The Relational Model.

**Revision:** `spark/revision/revision-1-foundations-and-core.md` (Spark 1–9) ✅.

---

## 11. Pending Work

Full list in **`PENDING.md`**. Headline: plain-language retrofit (B-lite) — Shuffle ✅, 4 remaining (Narrow vs Wide, RDD, How Python Runs, Variables). All new lessons written to the Section 3 standard.
