# DE-2026 — Teaching Rules (15 series + flagship project)

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

## 7. The Roadmaps (each series README tracks its own progress + lesson counts)

Core: Python ~34 · Spark ~39 · SQL ~26 · Data Modeling ~21 · Azure ~24 · Airflow+dbt ~21 · Warehouses+Streaming ~20.
Supporting: Linux ~10 · Git ~9 · Docker ~10.
Tier 3: DataOps(CI/CD+IaC) ~11 · Kubernetes ~9 · Governance & Security ~10 · System Design ~10 · AI-Era DE ~11.
Project: OrderIQ (P1→P2→P3). **Total ≈ 265 lessons across 15 series.**

---

## 8. Practice Environments
Per series README. Python — notebooks · Spark/Azure — Databricks Community · SQL/Data Modeling — PostgreSQL/DuckDB · Airflow+dbt/Warehouses+Streaming — Docker + Snowflake trial · Linux — terminal/WSL · Git — GitHub · Docker/K8s — Docker Desktop + minikube · DataOps — GitHub Actions + Terraform · Governance — cloud RBAC/Key Vault · AI-Era — LLM API + Chroma.

---

## 9. Git Rules
Commit + push every lesson to `claude/new-session-gmnma2`. Clear messages. GitHub only.

---

## 10. Current Progress (update every session)

**Roadmaps: all 15 built ✅ + flagship project ✅. Planning complete — now writing lessons.**

**Python — 2 done:** How Python Runs ✅ · Variables/Memory ✅. Next: Data Structures Deep.
**Spark — 9 done:** Phase 0 ✅ (3) · Phase 1: Driver ✅ · SparkSession ✅ · RDD ✅ · Transformations/Lazy ✅ · Narrow vs Wide ✅ · Shuffle ✅. Next: DAG→Stages→Tasks.
**All other 13 series — 0 lessons done.** Each next = Phase 0 Topic 1 (see each README).
**Revision:** `spark/revision/revision-1-foundations-and-core.md` (Spark 1–9) ✅.

---

## 11. Pending Work
Full list in **`PENDING.md`**. Headline: plain-language retrofit (B-lite) — Shuffle ✅, 4 remaining. All new lessons written to the Section 3 standard.
