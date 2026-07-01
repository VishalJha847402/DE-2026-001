# DataOps — CI/CD + Infrastructure as Code (Terraform) — Learning Series

> DE-2026 · Depth-first · **Grounded in 2026 DE/DevOps research** (Jul 2026) · **Tier 3 (senior differentiator)**
> Bring **software-engineering rigor** to data: auto-test & deploy pipelines (CI/CD) and provision infrastructure from code (IaC). *"Now core competencies for modern data engineers."*

## 🎯 What 2026 roles demand (research-grounded)

- **CI/CD** for data — **GitHub Actions / GitLab CI**: automatically test (dbt/Spark/SQL + data-quality gates) and deploy pipelines across dev → staging → prod with approvals.
- **Infrastructure as Code** — **Terraform** (most-adopted; ~90% of cloud users use IaC): provision ADLS/Databricks/Snowflake declaratively, no manual clicking, reproducible.
- **Production patterns:** remote state, drift detection, policy-as-code, Terratest, ephemeral environments.

**Why Tier 3:** most juniors skip this; it's what makes you *"manage infra with the same rigor as application engineers"* — a senior signal.

**Practice:** GitHub Actions (free) + Terraform CLI against a cloud free tier. Wraps **OrderIQ** for production credibility.

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | CI/CD for Data | 🟡 In Progress |
| Phase 1 | Infrastructure as Code (Terraform) | ⏳ Pending |

**Progress: 0 of ~11 lessons done.**

---

## Phase 0 — CI/CD for Data 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | Why DataOps (software rigor for data pipelines) | 🟡 Next |
| 2 | CI/CD Concepts — pipelines · stages · dev/staging/prod environments | ⏳ Pending |
| 3 | GitHub Actions — workflows · jobs · triggers · secrets | ⏳ Pending |
| 4 | CI for Data — test dbt/Spark/SQL · lint · **data-quality gates** ⭐ | ⏳ Pending |
| 5 | CD for Data — deploy pipelines · environment promotion · approvals | ⏳ Pending |

---

## Phase 1 — Infrastructure as Code (Terraform) ⏳

| # | Lesson |
|---|--------|
| 1 | Why IaC (declarative infra · no manual clicking · reproducible) |
| 2 | Terraform Basics — providers · resources · **state** · `plan` / `apply` ⭐ |
| 3 | Variables, Modules & Reuse |
| 4 | Terraform for Data Infra — provision ADLS / Databricks / Snowflake |
| 5 | Production IaC — remote state · drift detection · policy-as-code · Terratest |
| 6 | Terraform + CI/CD — the full automated pipeline ⭐ |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · CI/CD | 5 |
| Phase 1 · Terraform / IaC | 6 |
| **Total** | **~11 lessons** |

---

*Sister roadmaps: [Kubernetes](../kubernetes/) · [Governance & Security](../data-governance-security/) · [System Design](../system-design/) · [AI-Era DE](../ai-era-de/) · [Docker](../docker/) · [Project: OrderIQ](../projects/)*
