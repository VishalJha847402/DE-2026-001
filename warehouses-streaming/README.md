# Warehouses & Streaming (Snowflake · Table Formats · Kafka) — Learning Series

> DE-2026 · Depth-first · **Grounded in real 2026 India DE market + interview research** (Jul 2026)
> The **storage/serving** layer (Snowflake + open table formats) and the **real-time** layer (Kafka + Spark Structured Streaming). The last core pillar.

## 🎯 What 2026 DE roles actually demand (research-grounded)

**Warehousing (Snowflake — huge in India, ~13k live DE jobs):**
- **Separation of storage & compute** · **micro-partitions** (core storage unit) · virtual warehouses · pruning/zone maps · caching.
- Must-know features: **Snowpipe** (auto-ingest) · **Streams & Tasks** (CDC/incremental) · **Time Travel** + **Zero-Copy Cloning** · masking/row-access policies · **resource monitors** (credit/cost control).
- **Open table formats** — **Delta · Iceberg · Hudi** — bring ACID, schema evolution, and time travel to object storage. This is the **lakehouse** (Snowflake now supports Iceberg; Databricks uses Delta).

**Streaming (Kafka + Spark Structured Streaming):**
- Core: **topics · partitions** (unit of parallelism) · brokers · replication · **consumer groups + offsets** · **schema registry** (Avro, schema evolution).
- **Kafka + Spark**: checkpoints (not consumer groups), micro-batch, **exactly-once via idempotent sinks + WAL**, **watermarks** for late data.
- Production: CDC pipelines, tuning for millions of events/sec, high availability.

**Practice environment:** **Snowflake free trial** (30-day, $400 credit) · **Kafka via Docker** (Confluent/Redpanda) · **Spark Structured Streaming** on Databricks Community · DuckDB/Iceberg local. Feeds **OrderIQ P2 (lakehouse) + P3 (streaming)**.

## 📌 Where this sits in the overall DE sequence

```
✅ Python · ✅ Spark · ✅ SQL · ✅ Data Modeling · ✅ Azure Cloud · ✅ Airflow+dbt (roadmaps done)
👉 Warehouses + Streaming   ← YOU ARE HERE (the last core pillar)
   (Linux · Git · Docker alongside · Flagship project OrderIQ)
```

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Data Warehousing & Snowflake Foundations | 🟡 In Progress |
| Phase 1 | Snowflake Advanced + Open Table Formats | ⏳ Pending |
| Phase 2 | Kafka Foundations (Streaming) | ⏳ Pending |
| Phase 3 | Stream Processing & Production | ⏳ Pending |
| Phase 4 | The Real-Time Lakehouse (capstone) | ⏳ Pending |

**Progress: 0 of ~20 lessons done.**

> **Warehouse first, streaming second.** Snowflake + table formats build on your SQL + Data Modeling + Spark. Kafka + Structured Streaming then add the real-time layer (your Spark skills carry straight over).

---

## Phase 0 — Data Warehousing & Snowflake Foundations 🟡

| # | Lesson | Status |
|---|--------|--------|
| 1 | Why a Cloud Data Warehouse (warehouse vs lake vs lakehouse · storage/compute separation) | 🟡 Next |
| 2 | Snowflake Architecture — micro-partitions · virtual warehouses · the 3 layers · caching | ⏳ Pending |
| 3 | Loading Data — stages · `COPY` · **Snowpipe** auto-ingest | ⏳ Pending |
| 4 | Querying & Performance — pruning / zone maps · clustering keys · warehouse sizing · caches | ⏳ Pending |

---

## Phase 1 — Snowflake Advanced + Open Table Formats ⏳

| # | Lesson |
|---|--------|
| 1 | **Streams & Tasks** — CDC / incremental processing in Snowflake |
| 2 | **Time Travel & Zero-Copy Cloning** — recovery & dev workflows |
| 3 | Security & Cost Control — masking · row-access policies · resource monitors · credits |
| 4 | **Open Table Formats** — Delta vs Iceberg vs Hudi (ACID · schema evolution · time travel) ⭐ |
| 5 | The Lakehouse — table formats unifying lake + warehouse (Snowflake Iceberg, Databricks Delta) |

---

## Phase 2 — Kafka Foundations (Streaming) ⏳

| # | Lesson |
|---|--------|
| 1 | Why Streaming (batch vs stream · real-time use cases) |
| 2 | Kafka Architecture — brokers · topics · **partitions** · replication |
| 3 | Producers, Consumers, **Consumer Groups & Offsets** ⭐ |
| 4 | Schemas & the Schema Registry — Avro · schema evolution |

---

## Phase 3 — Stream Processing & Production ⏳

| # | Lesson |
|---|--------|
| 1 | Spark Structured Streaming — micro-batch · streaming DataFrames · triggers · output modes |
| 2 | Kafka + Spark Integration — checkpoints · offset tracking |
| 3 | **Delivery Semantics** — at-least-once vs exactly-once · idempotent sinks · WAL ⭐ |
| 4 | Windowing & Watermarks — event time · late data · aggregations |
| 5 | Production Streaming — CDC · tuning · high availability · monitoring |

---

## Phase 4 — The Real-Time Lakehouse (capstone) ⏳

| # | Lesson |
|---|--------|
| 1 | Streaming into the Lakehouse — Kafka → Structured Streaming → Delta/Iceberg medallion ⭐ |
| 2 | Batch + Streaming Together — Lambda vs Kappa architecture · unified serving |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Warehousing / Snowflake | 4 |
| Phase 1 · Snowflake Adv + Table Formats | 5 |
| Phase 2 · Kafka Foundations | 4 |
| Phase 3 · Stream Processing | 5 |
| Phase 4 · Real-Time Lakehouse | 2 |
| **Total** | **~20 lessons** |

⭐ = high-leverage lessons from the 2026 research (table formats/lakehouse, consumer groups & offsets, exactly-once semantics, streaming into the lakehouse).

**Note:** Alternatives are called out where relevant — **BigQuery/Redshift** vs Snowflake; **Flink** vs Spark Structured Streaming; **Kinesis** vs Kafka — but we teach the dominant India-2026 combo (Snowflake + Kafka + Spark).

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions)*
*Spaced-repetition recall files live in [`revision/`](./revision/)*
*Sister roadmaps: [Python](../python/) · [Spark](../spark/) · [SQL](../sql/) · [Data Modeling](../data-modeling/) · [Azure Cloud](../azure-cloud/) · [Airflow+dbt](../airflow-dbt/) · [Project: OrderIQ](../projects/)*
