# Kubernetes for Data Engineering — Learning Series

> DE-2026 · Depth-first · **Grounded in 2026 DevOps/DE research** (Jul 2026) · **Tier 3 (senior differentiator)**
> Orchestrate containers **at scale** — autoscaling, self-healing, running the data stack (Spark, Airflow) on a cluster. Where Docker ends, Kubernetes begins.

## 🎯 What 2026 roles demand (research-grounded)

- **Autoscaling** to handle traffic/load spikes; **modular architecture** where each component scales independently.
- Running **data workloads on K8s** — Spark on Kubernetes, Airflow on Kubernetes.
- Core objects: **Pods · Deployments · Services · ConfigMaps/Secrets · Volumes**, plus **Helm** for packaging.

**Why Tier 3:** most DEs don't operate K8s daily, but knowing *why and how* the platform runs (and reading a failing pod) is a strong senior signal. Learn **after Docker**.

**Practice:** local cluster via **minikube / kind** + Docker Desktop.

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Kubernetes Foundations | 🟡 In Progress |
| Phase 1 | Kubernetes for Data Engineering | ⏳ Pending |

**Progress: 0 of ~9 lessons done.**

---

## Phase 0 — Kubernetes Foundations 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | Why Kubernetes (orchestration at scale · beyond a single Docker host) | 🟡 Next |
| 2 | Architecture — control plane · nodes · kubelet · etcd | ⏳ Pending |
| 3 | Pods, Deployments & ReplicaSets | ⏳ Pending |
| 4 | Services & Networking | ⏳ Pending |
| 5 | ConfigMaps, Secrets & Volumes | ⏳ Pending |

---

## Phase 1 — Kubernetes for Data Engineering ⏳

| # | Lesson |
|---|--------|
| 1 | Scaling & Autoscaling (HPA) — handling load spikes ⭐ |
| 2 | Running Data Workloads — Spark on K8s · Airflow on K8s ⭐ |
| 3 | Helm — packaging & deploying |
| 4 | Production — resource limits · monitoring · when DEs actually need K8s |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Foundations | 5 |
| Phase 1 · K8s for DE | 4 |
| **Total** | **~9 lessons** |

---

*Sister roadmaps: [DataOps (CI/CD+IaC)](../dataops-cicd-iac/) · [Governance & Security](../data-governance-security/) · [System Design](../system-design/) · [AI-Era DE](../ai-era-de/) · [Docker](../docker/) · [Project: OrderIQ](../projects/)*
