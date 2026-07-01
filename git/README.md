# Git & Version Control for Data Engineering — Learning Series

> DE-2026 · Depth-first · **Grounded in 2026 DE market research** (Jul 2026)
> *"In 2026, knowing Git is a baseline skill."* Every data project — pipelines, dbt models, Airflow DAGs — lives in Git.

## 🎯 What DEs actually need from Git (research-grounded)

- **The essentials:** clone, commit, branch, merge, resolve conflicts.
- **Collaboration:** pull requests, code review, branching strategies — how teams ship without breaking each other's work.
- **DE-specific:** repo structure for pipelines/dbt/Airflow, keeping secrets out (`.gitignore`, `.env`), large files (Git LFS), and Git as the trigger for **CI/CD**.

**Practice environment:** Git locally + **GitHub** (you're already using it for this whole learning repo).

## 📌 Sequence note
A **supporting-tools** series — learn alongside the core pillars. You're already committing lessons to Git; this makes that fluent and professional.

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Git Foundations | 🟡 In Progress |
| Phase 1 | Collaboration & DE Workflows | ⏳ Pending |

**Progress: 0 of ~9 lessons done.**

---

## Phase 0 — Git Foundations 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | Why Version Control (the problem it solves, snapshots vs backups) | 🟡 Next |
| 2 | Git Basics — `init` / `clone` / `add` / `commit` / `status` / `log` + the 3 areas (working · staging · repo) | ⏳ Pending |
| 3 | Branching & Merging — branches, `merge`, fast-forward | ⏳ Pending |
| 4 | Remotes — `push` / `pull` / `fetch`, GitHub, `origin` | ⏳ Pending |
| 5 | Undoing Things — `reset` / `revert` / `checkout` / `restore`, `.gitignore` | ⏳ Pending |

---

## Phase 1 — Collaboration & DE Workflows ⏳

| # | Lesson |
|---|--------|
| 1 | Merge Conflicts — how they happen, resolving them cleanly ⭐ |
| 2 | Pull Requests & Code Review — the team workflow |
| 3 | Branching Strategies — feature branches · trunk-based · git flow |
| 4 | Git for Data Projects — repo structure · secrets (`.env`) · Git LFS · CI/CD triggers ⭐ |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Foundations | 5 |
| Phase 1 · Collaboration & DE Workflows | 4 |
| **Total** | **~9 lessons** |

⭐ = high-leverage for DEs (conflict resolution, Git for data projects/CI).

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions)*
*Sister roadmaps: [Python](../python/) · [Spark](../spark/) · [SQL](../sql/) · [Data Modeling](../data-modeling/) · [Azure Cloud](../azure-cloud/) · [Airflow+dbt](../airflow-dbt/) · [Warehouses+Streaming](../warehouses-streaming/) · [Linux](../linux-shell/) · [Docker](../docker/) · [Project: OrderIQ](../projects/)*
