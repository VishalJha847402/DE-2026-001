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

**DataNodes (many machines):** Actually store the data blocks on their local disks. Send heartbeats to the NameNode every few seconds to confirm they're alive.

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

1. Spark asks the **NameNode**: "Where are all the blocks of /logs/app.log?"
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

### Topic 3 — MapReduce & Why It Was Slow → Spark Born

#### 🟢 Easy

**E1. What are the two steps in MapReduce? Describe what each step does in simple words.**

<details>
<summary>▶ Answer</summary>

**Map step:** Each machine takes its chunk of data and produces (key, value) pairs. Example: for word count, each machine scans its lines and emits `("hello", 1)` for every word it sees.

**Reduce step:** All values with the same key are grouped together and combined. Example: all `("hello", 1)` entries from all machines are summed → `("hello", 47)`.

Map = split and label. Reduce = group and combine.

</details>

---

**E2. What is the fatal flaw in MapReduce that makes it slow for multi-step jobs?**

<details>
<summary>▶ Answer</summary>

After every single step (Map or Reduce), MapReduce writes all results to disk. Then the next step reads from disk again.

Disk is 100–1000x slower than RAM. A 5-step job = 10 disk reads + 10 disk writes (5 reads + 5 writes = 10 trips to disk). Every trip is slow.

**In short:** MapReduce is slow because it treats disk as its working memory instead of RAM.

</details>

---

**E3. What was Spark's key insight that made it 10–100x faster than MapReduce?**

<details>
<summary>▶ Answer</summary>

Keep data **in RAM** across all steps. Read from disk once at the start, write to disk once at the end. Everything in between stays in memory.

No intermediate disk writes = no disk round-trips = 10–100x faster, especially for jobs with multiple steps.

</details>

---

#### 🟡 Medium

**M1. A Flipkart pipeline has 7 steps: ingest → clean → join → aggregate → filter → rank → export. How many disk operations does MapReduce need? How many does Spark need?**

<details>
<summary>▶ Answer</summary>

**MapReduce:** Each of the 7 steps = 1 read + 1 write = 2 disk ops per step.
7 steps × 2 = **14 disk operations** (minimum — some steps chain multiple MR jobs).

**Spark:** 1 disk read (load data) + 1 disk write (save output) = **2 disk operations**.
All 7 steps run in RAM. No intermediate disk I/O.

At 1 TB data, MapReduce reads+writes ~14 TB total. Spark reads+writes ~2 TB. This is why Spark is 7x+ faster here, not counting the raw speed difference between RAM and disk.

</details>

---

**M2. Walk through how MapReduce would count the number of orders per city from a 500 GB Swiggy orders file.**

<details>
<summary>▶ Answer</summary>

**Map step:** Each machine reads its portion of the file. For every order row, it emits `(city_name, 1)`.
Example: Machine 3 processes 10,000 rows → emits `("Mumbai", 1)` × 3,200, `("Delhi", 1)` × 2,800, etc.

**Shuffle:** All `("Mumbai", 1)` pairs from ALL machines are collected and sent to the same Reducer machine. Same for Delhi, Bangalore, etc.

**Reduce step:** Each Reducer machine receives all counts for its assigned cities. It sums them: `("Mumbai", 47,382)`, `("Delhi", 38,901)`, etc.

**Write to disk:** Final results written. If you need more analysis, next MapReduce job reads these results from disk.

</details>

---

**M3. A Machine Learning model needs 100 training iterations. Each iteration reads the same dataset. Compare MapReduce vs Spark for this use case.**

<details>
<summary>▶ Answer</summary>

**MapReduce:** Each iteration is a full MapReduce job. 100 iterations = 100 disk reads of the full dataset + 100 disk writes. If dataset is 50 GB, that's 5 TB of disk reads alone. Extremely slow. This is why ML on Hadoop was essentially impractical.

**Spark:** Load the dataset into RAM once. Cache it. Run 100 iterations in memory. 1 disk read total. 100x faster.

This is why Spark became the standard for large-scale ML pipelines (via MLlib and Spark's integration with ML frameworks).

</details>

---

**M4. MapReduce was created at Google in 2004 and worked well for years. If disk writes are slow, why did Google use this approach?**

<details>
<summary>▶ Answer</summary>

In 2004, the context was different:

1. **RAM was expensive:** 1 GB of RAM cost ~₹8,000 in 2004. Servers had 2–4 GB RAM max. Keeping TBs in memory was physically impossible and unaffordable.

2. **Jobs ran overnight:** Google's initial use cases were batch indexing of the web — a job running 6 hours vs 30 hours didn't matter much. Nobody was waiting on it.

3. **Fault tolerance via disk:** Writing to disk after every step meant if any machine crashed, you only lost one step — resume from the last write. With in-memory processing, a crash loses everything in RAM.

By 2010–2012, RAM costs had dropped 10–20x, jobs became business-critical (no overnight wait), and better fault tolerance was possible — making Spark's in-memory approach viable and obviously superior.

</details>

---

#### 🔴 Hard

**H1. Spark keeps data in RAM. What happens when the total dataset is larger than the combined RAM of all Executors? Does Spark crash?**

<details>
<summary>▶ Answer</summary>

**No, Spark does not crash.** It has a fallback mechanism called **spilling to disk**.

When an Executor runs out of RAM during a shuffle or sort operation:
1. Spark detects memory pressure
2. It serializes the least-recently-used data partitions and writes them to local disk (a "spill file")
3. Processing continues with freed-up RAM
4. Spark reads spill files back when needed

**The cost:** Performance degrades — you lose the RAM speed advantage for those partitions. A job that should run in 5 minutes might take 30 minutes if heavily spilling.

**How to detect it:** Spark UI shows "Spill (Memory)" and "Spill (Disk)" columns in the Stages tab. Non-zero values mean you're spilling.

**Fix:** Add more Executors, increase Executor memory, or repartition data into smaller chunks. You'll learn this in Phase 4 (Performance & Production).

</details>

---

**H2. "Spark is just MapReduce in memory." A senior engineer says this is wrong. Explain exactly why.**

<details>
<summary>▶ Answer</summary>

This is wrong for three fundamental reasons:

**1. Execution model is different:**
MapReduce is strictly Map → Shuffle → Reduce — two phases, rigid. Spark has a DAG (Directed Acyclic Graph) — it can express any graph of operations: filter → join → groupBy → window → filter again. Not locked to Map+Reduce.

**2. Spark has lazy evaluation:**
When you write Spark code, nothing runs. Spark collects all operations and builds an execution plan. Then it optimizes the entire plan before running anything (push filters down, reorder joins, combine steps). MapReduce has no optimizer — each job runs immediately.

**3. Spark has a unified engine:**
MapReduce only did batch processing. Spark runs batch, streaming, SQL, machine learning, and graph processing — same engine, same API. MapReduce needed separate systems for each (Pig for ETL, Hive for SQL, Storm for streaming).

So Spark is not MapReduce in RAM — it's a fundamentally different execution model that happens to also avoid disk I/O.

</details>

---

**H3. Google built MapReduce, then built Dremel (BigQuery) and Flume internally — and largely stopped using MapReduce. Yahoo, Facebook, Cloudera all ran massive Hadoop clusters but have mostly moved to Spark or cloud warehouses. What does this pattern tell you about how distributed systems evolve?**

<details>
<summary>▶ Answer</summary>

This pattern reveals three fundamental truths about distributed systems evolution:

**1. Hardware economics drive architecture:**
MapReduce was born when RAM cost ₹8,000/GB. Spark was born when RAM cost ₹80/GB. Dremel/BigQuery was born when columnar SSDs became cheap. The "right" architecture depends heavily on what hardware costs at the time. Always evaluate tools in context of current hardware economics — not when they were designed.

**2. Use case complexity outgrows simple models:**
MapReduce's two-step model was elegant for 2004's use cases (web indexing, log processing). By 2012, companies needed: multi-step ETL, iterative ML, SQL, real-time — none of which Map+Reduce expresses cleanly. Systems that are too rigid eventually lose to flexible ones.

**3. Operational cost matters as much as technical performance:**
Hadoop clusters required large teams to manage. Cloud warehouses (BigQuery, Snowflake, Databricks) eliminate most operational overhead. In 2026 India, most companies don't run on-premise Hadoop — they use Databricks on Azure or AWS EMR with S3. The "best" system is often the one you can actually maintain, not the theoretically fastest one.

**For your career:** Understand the history so you know WHY things work the way they do. But spend your time mastering the tools companies actually use today: Spark + Delta Lake + Databricks + cloud storage. That's the 2026 stack.

</details>

---

*More topics added as we progress.*
