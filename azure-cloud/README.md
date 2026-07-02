# Azure Cloud for Data Engineering — Learning Series

> DE-2026 · Depth-first · **Grounded in real 2026 India Azure DE market research** (Jul 2026)
> The cloud where you actually **run** pipelines. Your SQL + Python + Spark + Data Modeling all come together here.

## 🎯 What 2026 India Azure DE roles actually demand (research-grounded)

- **Core = SQL + Python + Spark**, plus hands-on **Azure Data Factory · Azure Databricks · Synapse · Microsoft Fabric · ADLS Gen2 · Power BI**.
- **Cert shift:** DP-203 **retired** (Mar 2025). **DP-700 (Fabric Data Engineer Associate)** is the current credential. New **DP-750 (Azure Databricks Data Engineer)** in beta.
- **Microsoft Fabric** = Microsoft's new unified SaaS platform (OneLake + Lakehouse + Warehouse + Data Factory + Real-Time Intelligence + Power BI). Rising fast, premium pay.
- **Databricks** = deep engineering (Spark, clusters, Delta Lake, Unity Catalog) — **your Spark skills transfer directly.** **Synapse** = legacy but thousands of live deployments still hiring.
- Must-knows: **Medallion on ADLS/OneLake**, **Delta Lake**, **Unity Catalog**, security (Entra ID/RBAC/Key Vault), CI/CD, cost.
- **Projects beat certificates** — a real end-to-end pipeline portfolio is the #1 differentiator. Salary ₹6 LPA → ₹17–30 LPA.

**Practice environment:** Azure free account ($200 credit) + **Microsoft Fabric free trial** + **Databricks Community** (already using for Spark). Real hands-on needs an Azure account.

## 📌 Where this sits in the overall DE sequence

```
✅ Python · ✅ Spark · ✅ SQL · ✅ Data Modeling (roadmaps done)
👉 Azure Cloud   ← YOU ARE HERE (where SQL + Python + Spark + Modeling run for real)
   → 🔀 Airflow + dbt → 🏔️ Warehouses + Kafka
   (Linux · Git · Docker alongside · Projects P1–P3 at phase ends)
```

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Cloud & Azure Fundamentals | 🟡 In Progress |
| Phase 1 | Storage — The Data Lake (ADLS Gen2) | ⏳ Pending |
| Phase 2 | Compute — Azure Databricks ★ | ⏳ Pending |
| Phase 3 | Ingestion & Orchestration — Azure Data Factory | ⏳ Pending |
| Phase 4 | Warehouse & Serving — Synapse + Microsoft Fabric | ⏳ Pending |
| Phase 5 | Production · Security · Cost · Certification | ⏳ Pending |

**Progress: 2 of ~24 lessons done.**

> This is a **hands-on** skill (unlike Data Modeling). Lessons teach the concept + the WHY + the click-path, but real mastery needs you running it in an Azure account. Portfolio project is built across the phases.

---

## Phase 0 — Cloud & Azure Fundamentals 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | [Why Cloud for Data Engineering (compute/storage separation, elasticity, on-prem vs cloud)](./phase-0-fundamentals/topic-1-why-cloud/) | ✅ Done |
| 2 | [Azure Basics — subscriptions, resource groups, regions, portal, the cost model](./phase-0-fundamentals/topic-2-azure-basics/) | ✅ Done |
| 3 | Identity & Security — Entra ID (Azure AD), RBAC, Managed Identities, Key Vault | 🟡 Next |
| 4 | The Azure Data Stack Map — how ADLS / ADF / Databricks / Synapse / Fabric fit together | ⏳ Pending |

---

## Phase 1 — Storage: The Data Lake ⏳

| # | Lesson |
|---|--------|
| 1 | Azure Data Lake Storage Gen2 — hierarchical namespace, containers, access |
| 2 | File Formats & Partitioning in the Lake — Parquet, Delta, folder partitioning |
| 3 | Medallion on Azure — Bronze / Silver / Gold on ADLS & OneLake (ties to Data Modeling) |

---

## Phase 2 — Compute: Azure Databricks ⏳ ★ (your Spark skills land here)

| # | Lesson |
|---|--------|
| 1 | Databricks on Azure — workspace, clusters, notebooks |
| 2 | Delta Lake Deep — ACID, time travel, MERGE/upsert, OPTIMIZE / Z-ORDER |
| 3 | Building ELT Pipelines in Databricks (PySpark + SQL) |
| 4 | Unity Catalog — governance, lineage, access control |
| 5 | Databricks Workflows / Jobs — scheduling & orchestration |

---

## Phase 3 — Ingestion & Orchestration: Azure Data Factory ⏳

| # | Lesson |
|---|--------|
| 1 | ADF Core — pipelines, activities, linked services, datasets, integration runtime |
| 2 | Ingestion Patterns — Copy activity, batch vs incremental / CDC |
| 3 | Mapping Data Flows vs Orchestrating Databricks notebooks |
| 4 | Triggers, Parameters, Monitoring & Error Handling |

---

## Phase 4 — Warehouse & Serving: Synapse + Microsoft Fabric ⏳

| # | Lesson |
|---|--------|
| 1 | Azure Synapse — dedicated vs serverless SQL pools, Spark pools (legacy but live) |
| 2 | **Microsoft Fabric** — OneLake, Lakehouse, Warehouse, the one-SaaS model ⭐ |
| 3 | Fabric Data Factory + Real-Time Intelligence + Power BI serving |
| 4 | Fabric vs Synapse vs Databricks — choosing the right tool |

---

## Phase 5 — Production · Security · Cost · Certification ⏳

| # | Lesson |
|---|--------|
| 1 | CI/CD for Azure Data — Git integration, Azure DevOps, deployment (+ IaC intro) |
| 2 | Security & Governance — RBAC, Key Vault, Private Endpoints, Microsoft Purview |
| 3 | Cost Optimization & Monitoring — Azure Monitor, cost management, cluster sizing |
| 4 | Certification Path & Portfolio — **DP-700 (Fabric)** · DP-750 (Databricks) · end-to-end project ⭐ |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Fundamentals | 4 |
| Phase 1 · Storage (ADLS) | 3 |
| Phase 2 · Compute (Databricks) | 5 |
| Phase 3 · Ingestion (ADF) | 4 |
| Phase 4 · Warehouse (Synapse/Fabric) | 4 |
| Phase 5 · Production / Certs | 4 |
| **Total** | **~24 lessons** |

⭐ = high-leverage lessons from the 2026 research (Microsoft Fabric, the DP-700 cert path + portfolio project).

**Note:** Azure-native streaming (Event Hubs / Stream Analytics / Fabric Real-Time Intelligence) is touched in Phase 4; deep streaming (Kafka + Spark Structured Streaming) gets its own series later.

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions) + `practice.md` (setup + reasoning drills)*
*Spaced-repetition recall files live in [`revision/`](./revision/)*
*Sister series: [Spark](../spark/) · [Python](../python/) · [SQL](../sql/) · [Data Modeling](../data-modeling/)*
