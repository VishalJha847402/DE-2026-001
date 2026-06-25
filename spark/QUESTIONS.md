# Spark Series — Practice Questions (All Topics)

> Use this file for revision. All answers hidden — try each question first, then reveal.
> Organized by Phase → Topic → Easy / Medium / Hard.

---

## Phase 0 — Why Spark Exists

### Topic 1 — Why One Machine Breaks on Big Data

#### 🟢 Easy

**E1. What are the three main parts of a computer that matter for data processing? Describe each in one sentence.**

<details>
<summary>▶ Answer</summary>

**CPU (The Brain):** Does all calculations — filtering, sorting, aggregating — but can only work on data already in RAM.

**RAM (The Desk):** Active working space. All data must come here from disk before the CPU can process it. Fast but small.

**Disk (The Cupboard):** Permanent storage. Holds TBs of data but 100–1000x slower than RAM. Data travels Disk → RAM → CPU.

</details>

---

**E2. What is the Golden Rule of data processing in a computer?**

<details>
<summary>▶ Answer</summary>

Data must always follow: **Disk → RAM → CPU**

CPU cannot read data directly from disk. RAM is the only gateway. If data doesn't fit in RAM, the machine struggles or crashes.

</details>

---

**E3. What is the difference between Scale Up and Scale Out? Give one example of each.**

<details>
<summary>▶ Answer</summary>

**Scale Up (Vertical):** Make one machine bigger — more RAM, faster CPU. Example: upgrading to a ₹50 lakh server with 1 TB RAM.

**Scale Out (Horizontal):** Add more machines, split the work. Example: 100 cloud machines each handling 1/100th of data in parallel. This is Spark.

</details>

---

#### 🟡 Medium

**M1. Zomato has 800 GB of order data. Your machine has 64 GB RAM. You run an aggregation query. What happens? What should you do instead?**

<details>
<summary>▶ Answer</summary>

800 GB doesn't fit in 64 GB RAM. The OS swaps data back to disk — making it 100x slower. Query takes hours or crashes.

**Fix:** Use Spark. It splits 800 GB into chunks, sends each to a different machine (each with its own 64 GB RAM), processes in parallel, combines results. No single machine holds all 800 GB.

</details>

---

**M2. Your company has 500 GB today, 5 TB next year, 50 TB the year after. Why is Scale Up a bad long-term strategy?**

<details>
<summary>▶ Answer</summary>

1. **Cost:** 10x more RAM costs 50–100x more money — specialty hardware is exponentially priced.
2. **Hard ceiling:** Even the biggest servers max out (~6 TB RAM). At 50 TB, no single machine works.
3. **Single point of failure:** One server goes down = 100% outage. Scale Out: one of 100 goes down = 1% impact.

</details>

---

**M3. IRCTC has 10 TB load at 8–10 AM (Tatkal), only 200 GB outside peak. How does Scale Out help? Can Scale Up match this?**

<details>
<summary>▶ Answer</summary>

**Scale Out:** Spin up 100 machines during peak, shut down 90 after peak. Pay only for what you use. This is elastic scaling.

**Scale Up:** Buy one big server for peak load. It sits 2% utilized off-peak. You pay full cost 24/7. You can't "un-buy" hardware.

Cloud platforms (AWS, Azure, GCP) are built on Scale Out for exactly this reason.

</details>

---

**M4. A junior DE says: "Our data is 300 GB, server has 512 GB RAM. We don't need Spark." Right or wrong?**

<details>
<summary>▶ Answer</summary>

**Right — for now.** If 300 GB fits in 512 GB RAM, a single machine works fine. Spark adds unnecessary complexity.

**Wrong long-term** if data is growing. When it hits 1–2 TB, single machine will struggle. Industry rule of thumb: consider Spark when data consistently exceeds ~1 TB or single-machine processing becomes too slow.

</details>

---

#### 🔴 Hard

**H1. "Scale Up has no network overhead — so it's faster than Scale Out." What's fundamentally wrong with this?**

<details>
<summary>▶ Answer</summary>

True but irrelevant at scale. When data is 5 TB and RAM is 16 GB, Scale Up isn't "faster" — it's crashing or 100x slow from disk swapping. Two things network speed cannot fix:

1. **RAM ceiling:** No single machine holds petabyte-scale data. RAM is the bottleneck, not network.
2. **Parallelism:** 100 machines do 100x work simultaneously. One machine does 1x regardless of speed. Modern data center networks (~10 Gbps) make network overhead negligible compared to parallelism gains.

</details>

---

**H2. A 1,000-machine Spark cluster is processing 5 TB of data. One machine crashes mid-job. What happens? Does the job fail completely?**

<details>
<summary>▶ Answer</summary>

**No — the job does NOT fail.** Spark tracks exactly what each machine was doing. When a machine crashes, Spark detects it and re-runs only that machine's chunk on a different healthy machine. The other 999 machines continue uninterrupted.

This is **fault tolerance** via lineage — one of Spark's core design principles. You'll learn the exact mechanism in Phase 1.

Compare: Scale Up machine crashes = 100% failure. Scale Out machine crashes = 0.1% setback, auto-recovered.

</details>

---

**H3. If Scale Out is better, why not use Spark for everything — even 10 GB datasets?**

<details>
<summary>▶ Answer</summary>

Because Scale Out has real costs that hurt small data:

1. **Startup overhead:** Cluster setup takes 30+ seconds before processing even starts. Single machine does 10 GB in 2 seconds.
2. **Complexity:** Distributed debugging is much harder. One error message vs. logs across 100 machines.
3. **Network shuffling:** Machines sharing data (for joins, aggregations) adds overhead. For small data, it's pure cost with no benefit.
4. **Price:** 100 machines for 1 min costs more than 1 machine for 5 min — and single machine is faster for small data.

**Rule:** Use pandas/SQL/DuckDB under ~1 TB. Use Spark when single-machine tools run out of memory or become too slow.

</details>

---

### Topic 2 — HDFS: How Files Are Stored Across Many Machines

#### 🟢 Easy

**E1. What are the two types of nodes in HDFS? What does each one do?**

<details>
<summary>▶ Answer</summary>

**NameNode (1 machine):** Stores the metadata — the map of which file is split into which blocks and which DataNode holds each block. Does NOT store actual data.

**DataNodes (many machines):** Actually store the data blocks on their local disks. Send heartbeats to the NameNode every few seconds to confirm they’re alive.

</details>

---

**E2. What is a block in HDFS? What is the default block size?**

<details>
<summary>▶ Answer</summary>

A block is a fixed-size chunk of a file. HDFS cuts every file into blocks before storing them. Default block size = **128 MB**.

A 5 TB file becomes ~39,000 blocks of 128 MB each, distributed across many DataNodes.

</details>

---

**E3. What is replication in HDFS and why does it exist?**

<details>
<summary>▶ Answer</summary>

Replication means every block is copied and stored on multiple DataNodes. Default replication factor = **3** — each block exists on 3 different machines.

It exists for **fault tolerance** — if a DataNode crashes, the data is not lost because 2 more copies exist. HDFS automatically detects the lost copy and creates a new replica on a healthy DataNode.

</details>

---

#### 🟡 Medium

**M1. A Spark job needs to process a 1 TB log file in HDFS. Walk through exactly what happens step by step.**

<details>
<summary>▶ Answer</summary>

1. Spark asks the **NameNode**: “Where are all the blocks of /logs/app.log?”
2. NameNode returns the **block map**: Block 001 → DataNode 3, Block 002 → DataNode 7 … (~8,000 blocks total).
3. Spark assigns each **Executor** to read specific blocks from the DataNodes holding them.
4. Each Executor reads its blocks **locally** (data locality — code goes to data, not data to code).
5. Each Executor processes its blocks **in parallel**.
6. Results are **combined** and returned.

No single machine ever holds the full 1 TB.

</details>

---

**M2. Your HDFS cluster has 10 DataNodes. One crashes. Replication factor = 3. What happens to your data?**

<details>
<summary>▶ Answer</summary>

**Data is safe.** Every block on the crashed DataNode has 2 more copies on other DataNodes.

NameNode detects the death (missed heartbeats), identifies blocks now at only 2 copies, instructs healthy DataNodes to re-replicate them back to 3. Fully automatic, zero data loss.

</details>

---

**M3. Why does HDFS use 128 MB blocks instead of 1 MB blocks? What breaks with tiny blocks?**

<details>
<summary>▶ Answer</summary>

A 5 TB file at 1 MB blocks = **5,000,000 blocks** vs 39,000 at 128 MB.

Problems with tiny blocks:
1. **NameNode RAM overload:** Metadata for 5M blocks fills NameNode memory — it becomes the bottleneck.
2. **Too many disk seeks:** Millions of tiny reads are far slower than thousands of large reads.
3. **Coordination overhead:** 5M block assignments between Spark and NameNode vs 39,000 — massive extra work.

128 MB balances metadata size, disk efficiency, and parallelism.

</details>

---

**M4. Spark has 50 Executors. HDFS file has 200 blocks. How many blocks per Executor? What if only 10 Executors?**

<details>
<summary>▶ Answer</summary>

**50 Executors:** 200 ÷ 50 = **4 blocks each**. All 50 run in parallel. Total time ≈ time to process 4 blocks.

**10 Executors:** 200 ÷ 10 = **20 blocks each**. Each processes 20 sequentially. Total time ≈ 5x longer.

More Executors = more parallelism = faster. This is why cluster sizing matters.

</details>

---

#### 🔴 Hard

**H1. HDFS has only ONE NameNode — a single point of failure. If it crashes, the whole cluster is inaccessible even if all DataNodes are healthy. How does modern HDFS solve this?**

<details>
<summary>▶ Answer</summary>

HDFS 2.x+ solves this with **NameNode High Availability (HA)**:

- Two NameNodes run simultaneously: one **Active**, one **Standby**.
- Both share the same metadata via a **shared edit log** (stored on separate JournalNodes).
- DataNodes send heartbeats to **both** NameNodes.
- If Active crashes, Standby automatically promotes itself in seconds. Zero downtime for users.

Cloud storage (S3, Azure Blob) solves it differently — metadata is fully managed by the cloud provider with built-in redundancy. No NameNode HA to manage.

</details>

---

**H2. The machine holding Block 001 is busy with 5 other tasks. Spark can't achieve data locality. What does Spark do? What's the cost?**

<details>
<summary>▶ Answer</summary>

Spark falls through a **locality preference hierarchy**:

1. **PROCESS_LOCAL** — data in same JVM (best, in-memory)
2. **NODE_LOCAL** — same machine, different process (fast, local disk)
3. **RACK_LOCAL** — different machine, same network rack (fast, short hop)
4. **ANY** — anywhere in cluster (slowest, full network transfer)

Spark **waits briefly** (~3 seconds by default) for the ideal machine to free up. If it doesn't, it fetches the block from a replica on another machine via network.

**Cost:** Full 128 MB network transfer adds latency. In undersized clusters with frequent locality misses, this is a major performance bottleneck.

</details>

---

**H3. Most Spark jobs on Databricks use S3 / Azure Blob / GCS instead of HDFS. Does data locality still apply? Is cloud storage Spark slower?**

<details>
<summary>▶ Answer</summary>

**Data locality mostly does NOT apply.** With cloud storage, data lives in a separate service (S3, Blob) independent of the compute cluster. Every block read is a network call.

**Is it slower?** It depends:
- Cloud network bandwidth is very high (10–25 Gbps within same region) — 128 MB reads are fast.
- Databricks/EMR use **local SSD caching layers** (Delta Cache) to bring hot data close to Executors.
- **Decoupling compute and storage is actually an advantage** — scale each independently, pay for what you use.

**Verdict:** Slightly slower on raw read throughput vs perfect HDFS data locality, but the operational simplicity and cost efficiency make cloud storage the dominant pattern in 2026.

</details>

---

*More topics added as we progress.*
