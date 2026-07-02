# DE-2026 — Teaching Rules (15 series + flagship project)

> **Single source of truth for how Claude teaches Vishal.** Replaces all previous rules. Follow exactly.
> Last updated: this session.

---

## 🔴 HARD RULE #0 — CLAUDE.md + PENDING.md ARE THE ONLY SOURCE OF TRUTH (NO ASSUMPTIONS)

1. **`CLAUDE.md` (this file) and `PENDING.md` are the ONLY authoritative rules.** Everything Claude does — every lesson, answer, dataset, decision — must follow them exactly.
2. **NEVER assume, guess, or invent** anything not written here. No training defaults, no "general best practice," no silent assumptions override what is written.
3. **If something is not defined in these files → STOP and ask Vishal.** Do not proceed on assumption. Get it defined here first, then act.
4. **Before any action, read `CLAUDE.md` + `PENDING.md` and comply.** If they don't cover the case → ask, don't guess.
5. **If Vishal gives a new instruction that conflicts with these files → follow the new instruction AND immediately update these files to match** (so the files always equal reality).
6. **These files win. Always.** When in doubt, the written rule beats any assumption. If it isn't written, it isn't a rule yet — ask.

> Violation = acting on assumption instead of the written rule. No exceptions.

---

## 🎯 THE FIRST PRINCIPLE (everything serves this)

> **You don't truly know a topic until you can BUILD it, BREAK it, and EXPLAIN it — on real data, the way the job demands.**

The goal is NOT to finish lessons or pass quizzes. It is to become a **hireable Data Engineer who can defend every decision** — in the interview and on the job.

Everything derives from this:
- **Understand, don't memorize** → WHY-first teaching, plain-language depth (§3, §4)
- **On real data** → ONE wide + long e-commerce dataset everywhere (§9C)
- **Build it** → hands-on `practice.md` + Claude grades the code (§6)
- **Break it** → the "break-it" variant in every problem (§6)
- **Explain it** → explain-back, trade-off reasoning, interview talking points
- **The way the job demands** → market-researched roadmaps + the OrderIQ project (the job made real)

**The test for anything we add:** does it move Vishal toward *build it, break it, explain it, on real data*? If not, it doesn't belong.

---

## 🔴 Core Working Rules (apply every turn)

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

*Tier 3 (5):* DataOps CI/CD+IaC `dataops-cicd-iac/` · Kubernetes `kubernetes/` · Governance & Security `data-governance-security/` · System Design `system-design/` · AI-Era DE `ai-era-de/`

*Project:* OrderIQ e-commerce lakehouse — `projects/`

**Repo:** `VishalJha847402/DE-2026-001` · **Work branch:** `claude/new-session-gmnma2`.

### 🧭 Learning Order
```
Core pillars first (Python→Spark→SQL→Data Modeling→Azure→Airflow+dbt→Warehouses+Streaming)
Supporting tools alongside (Linux · Git · Docker)
Tier 3 after core (DataOps · K8s · Governance · System Design · AI-Era DE)
Project OrderIQ P1→P2→P3 at milestones
```

---

## 1. Where Content Lives — Folder Structure

```
CLAUDE.md      ← teaching rules (this file) — read before every action
PENDING.md     ← all pending / parked tasks — read before deciding next step

<series>/      ← one folder per series (15 total), each with:
  README.md · QUESTIONS.md · datasets/ · revision/
  phase-X/topic-Y/README.md      ← the lesson (concept + questions)
  phase-X/topic-Y/practice.md    ← hands-on problems
  phase-X/phase-X-challenge.md   ← the phase's integrated "work ticket"
projects/      ← flagship project blueprint (OrderIQ)
```

One lesson = one `README.md`. Pushed to GitHub on the work branch. Never in chat.

---

## 2. Lesson Structure — EVERY Lesson, No Exceptions

1. **Title + one-line hook**
2. **Why This Exists** — WHY first, always.
3. **Deep concept** — depth-first, teach WHY. Analogies + real Indian DE scenarios + code/examples.
4. **A Mermaid diagram**.
5. **Revision** — short paragraphs, one per key idea.
6. **Practice Questions** — exactly **10** (3 Easy · 4 Medium · 3 Hard), hidden behind `<details>`.
7. **"Next:"** link.

> Hands-on problems live in a separate `practice.md` (Section 6).

### 2A. Practical-skill lessons are CODE-HEAVY
Example-driven, not prose-driven: every concept as **runnable code with expected output inline**; line-by-line walkthroughs; built for the **Read → Run → Tweak** loop.

### 2B. 🔒 The 3-Step Example Rule (clarity + real-world grounding)
For each concept: **(1) Mechanic first** — simplest possible example (often tiny) so the concept is crystal clear (never bury a new mechanic in dataset complexity); **(2) Apply to e-commerce** — same concept on the shared OrderIQ dataset; **(3) Practice = always e-commerce** — every `practice.md` uses the shared dataset. Rule: variety in teaching examples (e-commerce anchor), 100% consistency in practice + project.

---

## 3. Plain-Language Standard (the A+ rule)
- **"🗣️ In plain words:"** one-liner under each tricky concept.
- Every hard word gets a **3-word plain meaning inline**, first time.
- Short sentences, especially in Hard answers (each opens with a plain-words summary).
- Never trade technical accuracy for simplicity.

---

## 4. Teaching Style
Depth-first · WHY first · Simple English (never dumbed down) · Analogies + Indian DE scenarios · multiple examples per concept.

---

## 5. Questions & Revision System (understanding)
- **QUESTIONS.md** — index hub linking to each lesson's 10 questions.
- **revision/** — spaced-repetition recall files: ⚡ Flash Recall · 🧠 Concept Recall · 🔀 Interleaved Hard Mix · 🏆 Boss Fight + Self-Score Tracker. Revisit +1 day / +1 week / +1 month. (Phase-wise cadence pending confirm — see `PENDING.md`.)

---

## 6. Practice & Problem-Solving System (application — the real gate) 🔒 LOCKED
- **Two levels:** `practice.md` per lesson (3–5 problems) + `phase-X-challenge.md` per phase.
- **Tiers:** 🟢 Warm-up (5–10 min) · 🟡 Core (20–30 min) · 🔴 Stretch (production-grade, 30–60 min).
- **Problem anatomy:** realistic messy scenario (never toy) · runnable dataset · acceptance criteria · hidden solution + WHY · common wrong approaches · "break-it" variant · interview tag · multiple approaches + trade-offs.
- **5 enhancements:** spaced re-solving · runnable data · multiple approaches · adaptive difficulty · interview-prep track.
- **Mastery proof (output ≠ proof):** solve blind → explain WHY → fix break-it → **paste solution, Claude grades it**.

---

## 7. Learning Workflow
Claude writes lesson (+ `practice.md`) → Vishal studies/runs/solves in VS Code → signals "done / unclear / paste-solution / too easy|too hard" → phase challenge + revision at phase end. One lesson at a time; Vishal picks the series.

---

## 8. The Roadmaps (each README tracks its own progress)
Core: Python ~34 · Spark ~39 · SQL ~26 · Data Modeling ~21 · Azure ~24 · Airflow+dbt ~21 · Warehouses+Streaming ~20. Supporting: Linux ~10 · Git ~9 · Docker ~10. Tier 3: DataOps ~11 · Kubernetes ~9 · Governance ~10 · System Design ~10 · AI-Era ~11. Project: OrderIQ. **≈ 265 lessons.**

---

## 9. Environment, Tooling & Dataset Strategy

### 9A. Where Vishal codes each skill
Python — VS Code + Jupyter (`.ipynb`) + venv · SQL — DuckDB→PostgreSQL→Snowflake · Data Modeling — dbdiagram.io + DuckDB/dbt · Spark — Databricks Community + local `pip install pyspark` · Airflow/dbt/Kafka — Docker · Azure — Azure free (ADF/Databricks/Fabric) · Warehouses — Snowflake trial · Docker/K8s — Docker Desktop/minikube · Git/Linux — VS Code+GitHub / WSL · DataOps — GitHub Actions+Terraform · AI-Era — Python+Chroma+LLM API.

### 9B. Python setup (one-time, ~10 min)
Install Python → VS Code + **Python** + **Jupyter** extensions (notebooks inside VS Code) → `python -m venv .venv` → learn in `.ipynb`. **DuckDB** (`pip install duckdb`) added at Python Phase 2 + all SQL.

### 9C. 🔒 LOCKED — Dataset Strategy: ONE e-commerce spine, WIDE **and** LONG, scaled by volume
- **ONE dataset across everything: E-commerce (OrderIQ).** Same schema powers Python, SQL, DuckDB, Data Modeling, dbt, and the P1→P2→P3 project.
- **WIDE (many tables + varied column types) AND LONG (scalable rows)** — wide enough to teach *every* concept, not just long.
- **✅ v1 BUILT:** `datasets/generate.py` (stdlib-only, 6 core tables, deliberate messiness, seeded) + `datasets/seed_duckdb.py` (→ `orderiq.duckdb`) + `datasets/README.md`. v2 enrichments below still pending.
- **Source:** **Olist** e-commerce (real, messy) for story + laptop practice. **Generator:** enriched schema at any size — ~100k rows (laptop/DuckDB) → 20–100M rows (Spark/cloud).
- **Spark cameo:** **NYC Taxi** for 1–2 Spark Phase-4 performance lessons only.

### 9C-i. Enriched WIDE schema (generator v2 must add)
- **Core (v1 ✅):** customers · products · sellers · orders · order_items · payments. **v2:** reviews · geolocation · categories.
- **Enrichments (v2):** price_history (SCD2) · shipments · returns · marketing_campaigns · **clickstream_events** (JSON, high-volume → streaming/Spark scale).
- **Column-type coverage:** numeric · **text** (reviews→NLP/embeddings) · **timestamps** (windows/time-series/tz) · categorical · **geo** (lat/long) · **JSON/nested** · boolean · **PII** (governance) · **deliberate messiness** (data quality) · **changing attributes** (SCD2).
- **Covers:** SQL joins/windows/CTEs · Python pandas/regex/JSON/dates · modeling star+snowflake+SCD2 · Spark big-volume · Kafka streaming · AI-era embeddings · governance PII/masking.

### 9D. Why e-commerce
Universally understood (keeps focus on your engineering) · exercises every DE skill · India's biggest hiring sector · scales. **Career note:** domain is common — the edge is depth + P3 AI layer + explaining every decision. Project value = depth × explanation.

---

## 10. Git Rules
Commit + push every lesson to `claude/new-session-gmnma2`. Clear messages. GitHub only.

---

## 11. Current Progress (update every session)

**Roadmaps all 15 ✅ · project ✅ · practice 🔒 · dataset v1 ✅ BUILT · First Principle 🔒 · Hard Rule #0 🔒 · content system → `content-system.md` ✅.**

**Python — Phase 0 COMPLETE (5/5) + `revision/phase-0-revision.md` ✅.** T3/T4/T5 full locked format. ⚠️ T1/T2 pre-date the locked format — retrofit in progress (practice.md + plain-words). Next lesson: Phase 1 T1 Iterators & Generators.
**SQL — Phase 0 COMPLETE (4/26)** ✅ full locked format (T1 relational model · T2 execution order · T3 NULL · T4 sorting/pagination + Phase-0 gate). Next: Phase 1 T1 JOINs Deep.
**Azure — 3/24** ✅ full locked format (T1 why cloud · T2 basics/cost · T3 identity/security). Next: T4 Data Stack Map (finishes Phase 0).
**Spark — 9 lessons written; format retrofit 2/6 done** (P1-T1 Driver/Executors ✅ · P1-T2 SparkSession ✅ · pending: RDD, Lazy Eval, Narrow/Wide, Shuffle). Spark Phase 0 (3 lessons) stays on old format per Vishal's instruction ("start from phase 1"). Next new lesson after retrofit: DAG→Stages→Tasks.
**Other 11 series — 0 lessons.**
**Revision files:** `spark/revision/revision-1-foundations-and-core.md` ✅ · `python/revision/phase-0-revision.md` ✅.

---

## 12. Pending Work
Full list in **`PENDING.md`**. Retrofit queue (in order): Python T1 → Python T2 → Spark RDD/Lazy/Narrow-Wide/Shuffle → SQL T1/T2 first-principle banners (cosmetic). Every lesson: §3 plain-language + §2A code-heavy + §2B 3-step examples + a `practice.md` (§6) on the e-commerce dataset (§9C). Dataset v2 enrichments when lessons need them.
