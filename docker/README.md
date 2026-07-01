# Docker & Containers for Data Engineering — Learning Series

> DE-2026 · Depth-first · **Grounded in 2026 DE market research** (Jul 2026)
> Docker solves the *"works on my machine"* problem — package an app + all its dependencies into a portable container. The whole modern data stack (Airflow, Kafka, Spark, Postgres) runs in containers.

## 🎯 What DEs actually need from Docker (research-grounded)

- **Containers vs VMs** — why containers give consistency across environments.
- **Images & Dockerfiles** — build a reproducible environment (`FROM` / `RUN` / `COPY` / `CMD`).
- **Volumes & networking** — persist data, connect containers, env vars.
- **Docker Compose** — run a multi-container data stack with one file.
- **CI/CD + registries** — build/push images, deploy; plus a **Kubernetes intro** (orchestration at scale — where DEs meet it).

**Practice environment:** **Docker Desktop** (or Docker Engine on Linux/WSL).

## 📌 Sequence note
A **supporting-tools** series — learn after Linux basics (Docker runs Linux under the hood). It powers the local Airflow/Kafka/Postgres you'll use in **OrderIQ P3**.

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Docker Foundations | 🟡 In Progress |
| Phase 1 | Docker for Data Engineering | ⏳ Pending |

**Progress: 0 of ~10 lessons done.**

---

## Phase 0 — Docker Foundations 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | Why Containers (the "works on my machine" problem · VMs vs containers) | 🟡 Next |
| 2 | Images & Containers — `run` / `ps` / `stop` / `rm`, Docker Hub | ⏳ Pending |
| 3 | Writing a Dockerfile — layers · `FROM` / `RUN` / `COPY` / `CMD` · build | ⏳ Pending |
| 4 | Data & Networking — volumes (persist data) · ports · env vars | ⏳ Pending |
| 5 | Docker Compose — multi-container stacks (e.g., app + Postgres) | ⏳ Pending |

---

## Phase 1 — Docker for Data Engineering ⏳

| # | Lesson |
|---|--------|
| 1 | Containerizing a Python / ETL Job ⭐ |
| 2 | Running the Data Stack in Docker — Airflow · Kafka · Postgres via Compose ⭐ |
| 3 | Image Optimization & Best Practices — small images · multi-stage builds · layer caching |
| 4 | Docker in CI/CD & Registries — GitHub Actions · building & pushing images |
| 5 | Kubernetes Intro — why/what (orchestration at scale) · where DEs meet it |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Foundations | 5 |
| Phase 1 · Docker for DE | 5 |
| **Total** | **~10 lessons** |

⭐ = high-leverage for DEs (containerizing jobs, running the data stack locally).

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions)*
*Sister roadmaps: [Python](../python/) · [Spark](../spark/) · [SQL](../sql/) · [Data Modeling](../data-modeling/) · [Azure Cloud](../azure-cloud/) · [Airflow+dbt](../airflow-dbt/) · [Warehouses+Streaming](../warehouses-streaming/) · [Linux](../linux-shell/) · [Git](../git/) · [Project: OrderIQ](../projects/)*
