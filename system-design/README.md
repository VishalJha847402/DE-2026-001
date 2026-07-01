# Data System Design — Learning Series

> DE-2026 · Depth-first · **Grounded in 2026 DE interview research** (Jul 2026) · **Tier 3 (senior differentiator)**
> The interview round that decides senior offers: *"design a data platform for X."* This is where all your skills combine into **architecture + trade-off reasoning.**

## 🎯 What 2026 roles demand (research-grounded)

- A **framework** to approach open-ended "design a pipeline/platform" questions.
- **Trade-off reasoning** — scale vs cost vs latency vs consistency; batch vs streaming; lake vs warehouse vs lakehouse.
- **Reliability patterns** — failures, retries, dead-letter queues, backpressure, idempotency, exactly-once.
- Real **case studies** you can whiteboard end to end.

**Why Tier 3:** it's the capstone skill — you can't fake it, and it separates "I use tools" from "I architect systems." Do it **after the core pillars** (it assumes them).

**Practice:** whiteboard designs + build them (OrderIQ is your live case study).

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Foundations & the Framework | 🟡 In Progress |
| Phase 1 | Designing Real Systems | ⏳ Pending |

**Progress: 0 of ~10 lessons done.**

---

## Phase 0 — Foundations & the Framework 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | How to Approach a DE System Design Interview (the framework) ⭐ | 🟡 Next |
| 2 | Requirements & Trade-offs — scale · latency · cost · consistency | ⏳ Pending |
| 3 | Storage Choices — OLTP vs OLAP · lake vs warehouse vs lakehouse | ⏳ Pending |
| 4 | Batch vs Streaming — Lambda vs Kappa architecture | ⏳ Pending |

---

## Phase 1 — Designing Real Systems ⏳

| # | Lesson |
|---|--------|
| 1 | Ingestion at Scale — CDC · event-driven · idempotency |
| 2 | Processing — partitioning · shuffles · distributed compute trade-offs |
| 3 | Serving — warehouses · caching · APIs |
| 4 | Reliability — failures · retries · dead-letter · backpressure · exactly-once ⭐ |
| 5 | Case Study — Design an E-Commerce Analytics Platform (ties to OrderIQ) ⭐ |
| 6 | Case Study — Design a Real-Time Recommendation / Fraud Pipeline |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Foundations | 4 |
| Phase 1 · Designing Real Systems | 6 |
| **Total** | **~10 lessons** |

---

*Sister roadmaps: [DataOps (CI/CD+IaC)](../dataops-cicd-iac/) · [Kubernetes](../kubernetes/) · [Governance & Security](../data-governance-security/) · [AI-Era DE](../ai-era-de/) · [Project: OrderIQ](../projects/)*
