# DE-2026 — Teaching Rules (15 series + flagship project)

> **Single source of truth for how Claude teaches Vishal.** Replaces all previous rules. Follow exactly.
> Last updated: this session.

---

## 🔴 Core Working Rules (READ FIRST — apply every turn)

1. **ALWAYS read `CLAUDE.md` (this file) before writing any content or answering anything.**
2. **ALWAYS read `PENDING.md` before deciding what to do next.**
3. **After writing or changing content, UPDATE this file** (Section 11 progress; add new decisions/rules).
4. **After finishing or adding a task, UPDATE `PENDING.md`.**
5. If this file and reality disagree, fix the file to match reality.
6. **Before writing any roadmap or lesson, research the 2026 India / AI-era market — data-backed, no assumptions — and ask "is this the best?" If not, make it the best.**

> Never skipped. This file + `PENDING.md` are how context survives between sessions.

---

## 0. What This Project Is

Vishal is learning **Data Engineering** for the **2026 India job market**, pillar by pillar, as **markdown (`.md`) lesson files on GitHub** — NOT in chat, NOT in HTML. Vishal studies on GitHub in his own time.

**ALL roadmaps built — planning complete. 15 series + flagship project:**

*Core pillars (7):* Python `python/` · Spark `spark/` · SQL `sql/` · Data Modeling `data-modeling/` · Azure Cloud `azure-cloud/` · Airflow+dbt `airflow-dbt/` · Warehouses+Streaming `warehouses-streaming/`

*Supporting tools (3):* Linux `linux-shell/` · Git `git/` · Docker `docker/`

*Tier 3 — senior differentiators (5):* DataOps CI/CD+IaC `dataops-cicd-iac/` · Kubernetes `kubernetes/` · Governance & Security `data-governance-security/` · System Design `system-design/` · AI-Era DE `ai-era-de/`

*Project:* OrderIQ e-commerce lakehouse — `projects/`

**Repo:** `VishalJha847402/DE-2026-001` · **Work branch:** `claude/new-session-gmnma2`.

### 🧭 Learning Order
```
Core pillars first (Python→Spark→SQL→Data Modeling→Azure→Airflow+dbt→Warehouses+Streaming)
Supporting tools alongside (Linux · Git · Docker)
Tier 3 senior differentiators after core (DataOps · K8s · Governance · System Design · AI-Era DE)
Project OrderIQ P1→P2→P3 at milestones
```
All roadmaps done. **Phase now = writing the actual lessons.**

---

## 1. Where Content Lives — Folder Structure

```
CLAUDE.md      ← teaching rules (this file) — read before every action
PENDING.md     ← all pending / parked tasks — read before deciding next step

<series>/      ← one folder per series (15 total), each with:
  README.md                         ← roadmap + progress
  QUESTIONS.md                      ← index hub linking to every lesson's questions
  datasets/                         ← runnable seed/setup for hands-on practice
  revision/                         ← spaced-repetition recall files (phase-wise)
  phase-X/topic-Y/README.md         ← the lesson (concept + questions)
  phase-X/topic-Y/practice.md       ← hands-on problems for that lesson
  phase-X/phase-X-challenge.md      ← the phase's integrated "work ticket"
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

> Hands-on problems live in a separate `practice.md` (see Section 6).

### 2A. Practical-skill lessons are CODE-HEAVY (Python, SQL, pandas, etc.)
For hands-on skills, the lesson is **example-driven, not prose-driven**: every concept shown as **runnable code with expected output inline**; **line-by-line walkthroughs**; designed for the **Read → Run → Tweak** loop. Then `practice.md` = Solve; then paste for grading (Section 6).

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

## 5. Questions & Revision System (understanding)
- **QUESTIONS.md** — index hub linking to each lesson's 10 questions (never duplicate).
- **revision/** — spaced-repetition recall files: ⚡ Flash Recall · 🧠 Concept Recall · 🔀 Interleaved Hard Mix · 🏆 Boss Fight + Self-Score Tracker. Revisit +1 day / +1 week / +1 month, recall before revealing. (Cadence phase-wise vs every-6-lessons — pending confirm; see `PENDING.md`.)

---

## 6. Practice & Problem-Solving System (application — the real gate) 🔒 LOCKED

Hands-on layer where Vishal writes/runs code. Separate from the 10 conceptual questions.

- **Two levels:** `practice.md` per lesson (3–5 problems) + `phase-X-challenge.md` per phase (integrated work ticket).
- **Difficulty tiers:** 🟢 Warm-up (5–10 min) · 🟡 Core (20–30 min, main effort zone) · 🔴 Stretch (production-grade, 30–60 min).
- **Every problem's anatomy:** realistic scenario (messy data, never toy) · runnable dataset · acceptance criteria · hidden solution + WHY · common wrong approaches · a "break-it" variant · interview tag · multiple approaches + trade-offs.
- **5 locked enhancements:** spaced re-solving (into phase revision) · runnable data (`datasets/` seed) · multiple approaches shown · adaptive difficulty ("too easy/too hard" → recalibrate) · interview-prep track near job-hunt.
- **Mastery proof (output ≠ proof):** solve Core+Stretch blind → explain WHY + trade-offs → fix the break-it → **paste solution, Claude grades it**. Only pays off if used.

---

## 7. Learning Workflow
1. Claude writes a lesson (+ `practice.md`) → pushes to GitHub.
2. Vishal studies + runs + solves in VS Code (his own time).
3. Vishal signals **"done with X"** / **"X unclear at Y"** / pastes a solution / **"too easy / too hard."**
4. End of Phase → phase challenge + revision file.
- Pace: one lesson at a time unless asked. Vishal chooses which series to advance each turn.

---

## 8. The Roadmaps (each series README tracks its own progress + lesson counts)

Core: Python ~34 · Spark ~39 · SQL ~26 · Data Modeling ~21 · Azure ~24 · Airflow+dbt ~21 · Warehouses+Streaming ~20.
Supporting: Linux ~10 · Git ~9 · Docker ~10.
Tier 3: DataOps ~11 · Kubernetes ~9 · Governance & Security ~10 · System Design ~10 · AI-Era DE ~11.
Project: OrderIQ (P1→P2→P3). **Total ≈ 265 lessons across 15 series.**

---

## 9. Environment, Tooling & Dataset Strategy

### 9A. Where Vishal codes each skill
| Skill | Where you code |
|-------|----------------|
| Python | VS Code + Jupyter (`.ipynb`) + venv |
| SQL | DuckDB → PostgreSQL → Snowflake |
| Data Modeling | dbdiagram.io + DuckDB/Postgres + dbt |
| Spark / PySpark | Databricks Community (free cloud notebooks) |
| Airflow · dbt · Kafka | Docker Desktop (local) |
| Azure | Azure free account (ADF · Databricks · Fabric) |
| Warehouses | Snowflake free trial |
| Docker · K8s | Docker Desktop · minikube |
| Git · Linux | VS Code + GitHub · terminal/WSL |
| DataOps | GitHub Actions + Terraform CLI |
| AI-Era | Python + Chroma + LLM API |

### 9B. Python setup (one-time, ~10 min)
1. Install Python (python.org). 2. VS Code + extensions **Python** + **Jupyter** (notebooks run inside VS Code — no separate Jupyter install). 3. `python -m venv .venv` (activate). 4. Learn in `.ipynb` notebooks — Read → Run → Tweak.

### 9C. 🔒 LOCKED — Dataset Strategy: ONE e-commerce spine, scaled by volume
- **ONE dataset across everything: E-commerce (OrderIQ).** Same schema powers Python, SQL, DuckDB, Data Modeling, dbt, AND the P1→P2→P3 project. One mental model; the same data flows through the whole stack (this IS real DE).
- **Source:** **Olist** e-commerce dataset (real, messy, ~100k orders) for the story + laptop practice.
- **Scaled by a generator** (to build): produces the same schema at any size — ~100k rows (laptop/DuckDB) for SQL/Python/modeling; **20–100M rows** for Spark/cloud (enough to trigger shuffles/skew/partitioning on Databricks Community; real-TB is a paid-job thing, not needed to *learn*).
- **DuckDB** is the runnable-data backbone (`pip install duckdb`) — added at Python Phase 2 + all SQL. Pure-Python Phase-0 lessons need only VS Code + Python.
- **Spark big-data cameo:** **NYC Taxi** bolted on for 1–2 Spark Phase-4 performance lessons only (real massive dataset). Spine stays e-commerce.

### 9D. Why e-commerce (locked rationale)
Universally understood by interviewers (keeps focus on *your engineering*, not the domain) · exercises **every** DE skill (joins, facts/dims, **SCD2**, streaming order events, clear metrics) · matches India's biggest hiring sector (Flipkart/Amazon/Meesho/Swiggy/Zomato) · scales small→huge.
**Career note:** the domain is *common* — the edge is **engineering depth + the P3 AI-era layer + being able to explain every decision.** Project value = depth × explanation.

---

## 10. Git Rules
Commit + push every lesson to `claude/new-session-gmnma2`. Clear messages. GitHub only.

---

## 11. Current Progress (update every session)

**Roadmaps: all 15 built ✅ + flagship project ✅ + dataset strategy 🔒 locked. Now writing lessons.**

**Python — 2 done:** How Python Runs ✅ · Variables/Memory ✅. Next: Data Structures Deep (first code-heavy lesson + first `practice.md`).
**Spark — 9 done:** Phase 0 ✅ (3) · Phase 1: Driver ✅ · SparkSession ✅ · RDD ✅ · Transformations/Lazy ✅ · Narrow vs Wide ✅ · Shuffle ✅. Next: DAG→Stages→Tasks.
**All other 13 series — 0 lessons done.**
**Practice system — 🔒 locked (§6), 0 sets built. Dataset — 🔒 locked (§9C), generator + DuckDB seed to build.**
**Revision:** `spark/revision/revision-1-foundations-and-core.md` (Spark 1–9) ✅.

---

## 12. Pending Work
Full list in **`PENDING.md`**. Headline: build the e-commerce generator + DuckDB seed; plain-language retrofit (B-lite, 4 left); phase-wise revision + clickable tracker (pending confirm). All new lessons: Section 3 standard + code-heavy (§2A) + a `practice.md` (§6) on the e-commerce dataset (§9C).
