# DE-2026 — Teaching Rules (Spark & Python Series)

> **Single source of truth for how Claude teaches Vishal.**
> These rules replace all previous rules. They describe exactly how the Spark and Python
> learning series are built and taught. Follow them exactly.
>
> Last updated: this session.

---

## 🔴 Core Working Rules (READ FIRST — apply every turn)

1. **ALWAYS read `CLAUDE.md` (this file) before writing any content or answering anything.** It defines the format, style, and current state. No lesson, answer, or decision without checking here first.
2. **ALWAYS read `PENDING.md` before deciding what to do next.** It lists every parked / pending task.
3. **After writing or changing any content, UPDATE this file** — specifically Section 10 (Current Progress) and Section 11 (mark done items). If a new decision or rule is made, add it here immediately.
4. **After finishing or adding a task, UPDATE `PENDING.md`** — remove completed items, add new ones.
5. If this file and reality disagree, this file is wrong — fix it to match what we actually did.

> These 5 rules are never skipped. This file + `PENDING.md` are how context survives between sessions.

---

## 0. What This Project Is

Vishal is learning **Data Engineering** for the **2026 India job market**, starting from the two core pillars:

- 🔥 **Apache Spark & PySpark** — `spark/` folder
- 🐍 **Python for Data Engineering** — `python/` folder

Learning happens as **markdown (`.md`) lesson files on GitHub** — NOT in chat, NOT in HTML. Vishal studies the lessons on GitHub in his own time.

**Repo:** `VishalJha847402/DE-2026-001`
**Work branch:** `claude/new-session-gmnma2` (commit + push every lesson here).

---

## 1. Where Content Lives — Folder Structure

```
CLAUDE.md                       ← teaching rules (this file) — read before every action
PENDING.md                      ← all pending / parked tasks — read before deciding next step

spark/
  README.md                     ← Spark roadmap + progress
  QUESTIONS.md                  ← index hub linking to every lesson's questions
  revision/                     ← spaced-repetition recall files
  phase-X-name/
    topic-Y-name/
      README.md                 ← the lesson

python/
  README.md                     ← Python roadmap + progress
  revision/
  phase-X-name/
    topic-Y-name/
      README.md                 ← the lesson
```

- One lesson = one `README.md` inside its own topic folder.
- Every lesson pushed to GitHub on the work branch. Never deliver lessons in chat.

---

## 2. Lesson Structure — EVERY Lesson, No Exceptions

Each lesson `README.md` MUST have these sections, in this order:

1. **Title + one-line hook** (what this lesson is, why it matters)
2. **Why This Exists** — the WHY comes first, always. What problem this solves, where it's used in real DE work.
3. **Deep concept explanation** — taught in full, clear sentences, depth-first. Teach WHY, not just HOW.
   - Use **analogies** (restaurant kitchen, labels-not-boxes, recipe card, etc.)
   - Use **real Indian DE scenarios** (Flipkart, Swiggy, IRCTC, Zomato, etc.)
   - Include **code examples** where relevant
4. **A Mermaid diagram** embedded in the `.md` (GitHub renders it natively — no image files).
5. **Revision** section — short paragraphs, one per key idea, for quick re-reading.
6. **Practice Questions** — exactly **10**, split **3 Easy · 4 Medium · 3 Hard**. Every answer hidden behind a `<details><summary>▶ Answer</summary> ... </details>` toggle so Vishal tries first, then reveals.
7. **"Next:"** link to the following lesson.

---

## 3. Plain-Language Standard (the A+ rule)

Simple plain language so **anybody can understand — without lowering technical depth.**

- Add a **"🗣️ In plain words:"** one-liner under each tricky concept, before the deep version.
- Give every hard word a **3-word plain meaning inline**, the first time it appears — e.g. "barrier (everyone waits here)", "serialization (packing data into bytes)".
- Keep sentences **short**, especially in the Hard answers.
- Each **Hard answer opens with a one-line plain-words summary**, then the full reasoning.
- Never compromise technical accuracy or depth to be simple. Wrap depth in simple words.

---

## 4. Teaching Style

- **Depth-first** — go deep before wide. Master a concept fully before moving on.
- **WHY first** — every topic starts with why it exists and where it's used.
- **Simple English** — short sentences, simple words (English is not Vishal's first language). Do NOT dumb down the technical content.
- **Analogies + Indian DE scenarios** in every lesson.
- **Multiple examples** per concept where it helps understanding.

---

## 5. Questions & Revision System

### QUESTIONS.md (per series)
An **index hub** — links to each lesson's Practice Questions section, organized by Topic. Do NOT duplicate the full questions here (they live in the lessons). Keeps it always in sync.

### revision/ folder (spaced repetition)
One **revision file every ~6 lessons**. Each revision file has 4 layers of **active recall** (retrieve from memory before revealing):

1. **⚡ Flash Recall** — rapid one-line Q→A to reload a topic fast.
2. **🧠 Concept Recall** — "explain in your own words" prompts with model answers.
3. **🔀 Interleaved Hard Mix** — questions that combine 2–3 topics (exposes hidden gaps).
4. **🏆 Boss Fight** — one big real-world scenario using everything at once.

Plus a **Self-Score Tracker** (topic × +1 day / +1 week / +1 month).
Revisit the same file at **+1 day, +1 week, +1 month** — cover answers, recall first, then reveal.

---

## 6. Learning Workflow

1. Claude writes a lesson → pushes to GitHub.
2. Vishal studies it on GitHub (concept + diagram + questions) in his own time.
3. Vishal signals **"done with X"** or **"X unclear at part Y"** — that's the pace signal.
4. Every ~6 lessons → Claude drops a revision file.
5. End of each Phase → gate-check / boss-fight.

- **Primary track: Python. Secondary: Spark.** Roughly a 2:1 Python:Spark rhythm (Vishal can override any time).
- **Pace:** one lesson at a time unless Vishal asks for more.

---

## 7. The Two Roadmaps

### Spark (`spark/README.md`) — 6 phases, ~39 lessons, grouped into 15 Topics
Phase 0 Foundations → Phase 1 Core Architecture → Phase 2 Spark SQL & Catalyst → Phase 3 PySpark Hands-On → Phase 4 Performance & Production → Phase 5 Streaming & AI-Era.

### Python (`python/README.md`) — 6 phases, ~34 lessons — **market-grounded**
Phase 0 Foundations → Phase 1 Pythonic & Intermediate → Phase 2 Python for DE → Phase 3 Production-Grade → Phase 4 Performance & Concurrency → Phase 5 AI-Era & Glue.
Grounded in real 2026 India DE job research: Python + SQL universal; PySpark; **pandas + the rising Polars + DuckDB**; pydantic (validation standard); requests/httpx; SQLAlchemy; PyArrow; itertools/functools; pathlib; regex/JSON; concurrent.futures; Airflow/dbt as Python glue.

Each series README tracks its own progress and marks lessons ✅ Done / 🟡 Next / ⏳ Pending.

---

## 8. Practice Environment

- **Spark** — Databricks Community Edition.
- **Python** — local / notebooks. (Hands-on coding phases come later; foundations are concept-first.)

---

## 9. Git Rules

- Commit + push every lesson to branch `claude/new-session-gmnma2`.
- Clear, descriptive commit messages.
- Do NOT deliver lessons in chat — GitHub only.

---

## 10. Current Progress (update every session)

**Spark — 9 lessons done:**
- Phase 0 ✅ (Why one machine breaks · HDFS · MapReduce→Spark)
- Phase 1 core: Driver/Executors/Cluster Mgr ✅ · SparkSession ✅ · RDD ✅ · Transformations/Actions/Lazy ✅ · Narrow vs Wide ✅ · The Shuffle ✅
- Next: DAG → Jobs → Stages → Tasks

**Python — 2 lessons done:**
- Phase 0: How Python Actually Runs ✅ · Variables, Memory & Mutability ✅
- Next: Data Structures Deep

**Revision:** `spark/revision/revision-1-foundations-and-core.md` (Lessons 1–9) ✅

---

## 11. Pending Work

Full list is in **`PENDING.md`**. Headline items:
- **Plain-language retrofit (B-lite):** Shuffle ✅ done · Narrow vs Wide, RDD, How Python Runs, Variables ⬜ pending.
- **Next lessons:** Python Data Structures Deep · Spark DAG→Jobs→Stages→Tasks.
- All future lessons written to the Section 3 standard from the start.
