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

> Hands-on problems live in a separate `practice.md` (see Section 6), so the lesson stays focused on concept + understanding.

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
- **revision/** — spaced-repetition recall files: ⚡ Flash Recall · 🧠 Concept Recall · 🔀 Interleaved Hard Mix · 🏆 Boss Fight + Self-Score Tracker. Revisit +1 day / +1 week / +1 month, recall before revealing.
  - (Cadence — phase-wise vs every-6-lessons — pending Vishal's final confirm; see `PENDING.md`.)

---

## 6. Practice & Problem-Solving System (application — the real gate) 🔒 LOCKED

The hands-on layer where Vishal actually writes/runs code. Separate from the 10 conceptual questions. This is what proves he can *do* it, not just understand it.

### Two levels
- **Lesson Practice** — `practice.md` next to each lesson. 3–5 hands-on problems using that lesson's concept, on the shared dataset.
- **Phase Challenge** — `phase-X-challenge.md` per phase. ONE realistic "work ticket" (a stakeholder request) combining every lesson in the phase. Integration — can't be faked.

### Difficulty tiers (every set — the "not too easy, not too hard" rule)
- 🟢 **Warm-up** — apply the concept directly (5–10 min)
- 🟡 **Core** — realistic scenario, combine with prior concepts, real thinking (20–30 min) ← main effort zone
- 🔴 **Stretch** — production-grade: optimize / handle the edge case / explain the trade-off (30–60 min)

### Every problem's anatomy (no exceptions)
1. **Realistic scenario** — a real DE ticket with messy data. NEVER toy problems ("reverse a string").
2. **Dataset + context** — runnable, not pseudocode.
3. **Acceptance criteria** — exactly how you know the answer is correct.
4. **Hidden reference solution + WHY it works.**
5. **Common wrong approaches** — the traps.
6. **A "break-it" variant** — nulls / duplicates / 100M rows → what breaks?
7. **Interview tag** — when it mirrors a real 2026 interview ask.
8. **Multiple valid approaches + trade-offs** — not one "right" answer (teaches judgment).

### The 5 locked enhancements (what makes it best)
1. **Spaced re-solving** — hard problems re-surface inside the phase revision file (practice ↔ revision linked).
2. **Runnable data** — every series has `datasets/` with a setup/seed (e.g., OrderIQ/Olist → DuckDB/Postgres in ~2 min) so practice is truly hands-on.
3. **Multiple approaches + trade-offs** shown in every solution.
4. **Adaptive difficulty** — Vishal signals "too easy / too hard" → Claude recalibrates the next set.
5. **Interview-prep track** — timed, company-style problems (TCS/Deloitte-style SQL, system design) assembled near job-hunt.

### Mastery proof (output ≠ proof)
A problem is truly "owned" only when Vishal can:
1. Solve **Core + Stretch without looking**,
2. **Explain WHY** + the trade-offs,
3. **Fix the break-it variant**.
Then: **paste the solution → Claude grades it** (bugs, better approach, honest "do you really get it or did you get lucky?"). This grading loop is the highest-value part — it only pays off if Vishal actually uses it.

---

## 7. Learning Workflow
1. Claude writes a lesson (+ `practice.md`) → pushes to GitHub.
2. Vishal studies + solves on GitHub / locally in his own time.
3. Vishal signals **"done with X"** / **"X unclear at Y"** / pastes a solution for grading / **"too easy / too hard."**
4. End of Phase → phase challenge + revision file.
- Pace: one lesson at a time unless asked. Vishal chooses which series to advance each turn.

---

## 8. The Roadmaps (each series README tracks its own progress + lesson counts)

Core: Python ~34 · Spark ~39 · SQL ~26 · Data Modeling ~21 · Azure ~24 · Airflow+dbt ~21 · Warehouses+Streaming ~20.
Supporting: Linux ~10 · Git ~9 · Docker ~10.
Tier 3: DataOps ~11 · Kubernetes ~9 · Governance & Security ~10 · System Design ~10 · AI-Era DE ~11.
Project: OrderIQ (P1→P2→P3). **Total ≈ 265 lessons across 15 series.**

---

## 9. Practice Environments
Python — notebooks · Spark/Azure — Databricks Community · SQL/Data Modeling — PostgreSQL/DuckDB · Airflow+dbt/Warehouses+Streaming — Docker + Snowflake trial · Linux — terminal/WSL · Git — GitHub · Docker/K8s — Docker Desktop + minikube · DataOps — GitHub Actions + Terraform · Governance — cloud RBAC/Key Vault · AI-Era — LLM API + Chroma. Shared practice dataset: OrderIQ / Olist.

---

## 10. Git Rules
Commit + push every lesson to `claude/new-session-gmnma2`. Clear messages. GitHub only.

---

## 11. Current Progress (update every session)

**Roadmaps: all 15 built ✅ + flagship project ✅. Planning complete — now writing lessons.**

**Python — 2 done:** How Python Runs ✅ · Variables/Memory ✅. Next: Data Structures Deep.
**Spark — 9 done:** Phase 0 ✅ (3) · Phase 1: Driver ✅ · SparkSession ✅ · RDD ✅ · Transformations/Lazy ✅ · Narrow vs Wide ✅ · Shuffle ✅. Next: DAG→Stages→Tasks.
**All other 13 series — 0 lessons done.** Each next = Phase 0 Topic 1 (see each README).
**Practice & Problem-Solving System — 🔒 LOCKED (Section 6), 0 practice sets built yet.**
**Revision:** `spark/revision/revision-1-foundations-and-core.md` (Spark 1–9) ✅.

---

## 12. Pending Work
Full list in **`PENDING.md`**. Headline: plain-language retrofit (B-lite) — Shuffle ✅, 4 remaining. Phase-wise revision cadence + clickable tracker — pending confirm. All new lessons written to the Section 3 standard; every lesson also gets a `practice.md` per Section 6.
