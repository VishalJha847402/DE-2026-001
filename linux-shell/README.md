# Linux & Shell for Data Engineering — Learning Series

> DE-2026 · Depth-first · **Grounded in 2026 DE market research** (Jul 2026)
> *"Being comfortable with Linux, permissions, and shell scripting is not optional — it's essential."* Everything a DE runs — servers, containers, Spark, Airflow — runs on Linux.

## 🎯 What DEs actually need from Linux (research-grounded)

- **Filesystem, navigation, permissions (`chmod`/`chown`)** — every server and container is Linux.
- **Text processing** — `grep`, `sed`, `awk`, `cut`, `sort`, `uniq` for quick data wrangling in the shell.
- **Bash scripting** — variables, conditionals, loops, functions → automate repetitive pipeline tasks and build small CLI tools.
- **Scheduling & processes** — `cron`, background jobs, environment variables, SSH.

**Practice environment:** any Linux/macOS terminal, or **WSL** on Windows, or a Docker Linux container.

## 📌 Sequence note
A **supporting-tools** series — learn it *alongside* the core pillars (it makes Spark, Airflow, Docker, and cloud work smoother), not as a blocking prerequisite.

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Linux Foundations | 🟡 In Progress |
| Phase 1 | Shell Scripting & Automation | ⏳ Pending |

**Progress: 0 of ~10 lessons done.**

---

## Phase 0 — Linux Foundations 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | Why Linux for Data Engineering (servers, containers, everything runs on it) | 🟡 Next |
| 2 | The Filesystem & Navigation — paths, `ls` / `cd` / `pwd`, structure | ⏳ Pending |
| 3 | Files & Directories — `cp` / `mv` / `rm` / `mkdir` / `find` / `ln` | ⏳ Pending |
| 4 | Viewing & Searching Text — `cat` / `less` / `head` / `tail` / `grep` / `wc` | ⏳ Pending |
| 5 | Permissions & Ownership — `chmod` / `chown`, users & groups | ⏳ Pending |

---

## Phase 1 — Shell Scripting & Automation ⏳

| # | Lesson |
|---|--------|
| 1 | Pipes, Redirection & Composition — `\|` · `>` · `>>` · `<` |
| 2 | Text Processing for Data — `grep` / `sed` / `awk` / `cut` / `sort` / `uniq` ⭐ |
| 3 | Bash Scripting — variables · conditionals · loops · functions · arguments ⭐ |
| 4 | Building a Data CLI Tool — a real ETL helper script |
| 5 | Scheduling & Processes — `cron` · `ps` / `kill` / `nohup` · env vars · SSH |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Foundations | 5 |
| Phase 1 · Scripting & Automation | 5 |
| **Total** | **~10 lessons** |

⭐ = high-leverage for DEs (shell text processing, Bash scripting).

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions)*
*Sister roadmaps: [Python](../python/) · [Spark](../spark/) · [SQL](../sql/) · [Data Modeling](../data-modeling/) · [Azure Cloud](../azure-cloud/) · [Airflow+dbt](../airflow-dbt/) · [Warehouses+Streaming](../warehouses-streaming/) · [Git](../git/) · [Docker](../docker/) · [Project: OrderIQ](../projects/)*
