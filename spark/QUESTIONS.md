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

## Phase 1 — Spark Core Architecture

### Topic 1 — Driver, Executors & Cluster Manager

#### 🟢 Easy

**E1. What is the role of the Driver in a Spark job? Name three things it does.**

<details>
<summary>▶ Answer</summary>

The Driver is the brain of a Spark job. Three things it does:

1. **Runs your application code** — Your Python/Scala/Java code executes inside the Driver process.
2. **Breaks the job into Tasks** — Divides the work into small units (one Task per data partition) and schedules them on Executors.
3. **Monitors Executors** — Receives heartbeats from all Executors. If one dies, the Driver reschedules its Tasks on another healthy Executor.

Other things it does: builds the execution plan, talks to Cluster Manager to request resources, collects final results.

</details>

---

**E2. What is an Executor? If an Executor has 8 cores, how many Tasks can it run at the same time?**

<details>
<summary>▶ Answer</summary>

An Executor is a JVM process that runs on a worker machine in the cluster. It is the actual laborer — it reads data, runs the computation, and returns results.

With 8 cores, an Executor can run **8 Tasks simultaneously** — one Task per core at any given moment.

If a cluster has 20 Executors with 8 cores each → 20 × 8 = **160 Tasks can run in parallel** across the entire cluster at the same time.

</details>

---

**E3. Name the four types of Cluster Managers Spark supports. Which one is most commonly used in Indian enterprise setups?**

<details>
<summary>▶ Answer</summary>

1. **Standalone** — Spark's own built-in manager. Simple, no external dependencies.
2. **YARN** — Hadoop's resource manager. Most common in Indian enterprise setups (banks, telecom, large companies with on-premise Hadoop).
3. **Kubernetes** — Container-based. Modern cloud-native setups. Growing fast.
4. **Mesos** — Legacy, mostly deprecated.

**Most common in Indian enterprise setups: YARN.** Banks like HDFC, SBI, and large companies running on-premise Hadoop clusters all use YARN. Cloud platforms (EMR, HDInsight) also use YARN under the hood.

</details>

---

#### 🟡 Medium

**M1. You work at Flipkart. A Spark job processes a 4 TB orders file. The cluster has 50 Executors, each with 8 cores. Each partition is 128 MB. How many Tasks will be created? How many run in parallel at once?**

<details>
<summary>▶ Answer</summary>

**Number of partitions (= number of Tasks):**
4 TB = 4,000 GB = 4,096,000 MB ÷ 128 MB = **32,000 Tasks**

**Parallel Tasks at one time:**
50 Executors × 8 cores = **400 Tasks running in parallel simultaneously**

**How the job runs:**
Driver sends the first 400 Tasks to Executors. As each Task finishes, Driver sends the next one. The cluster processes Tasks in waves of 400 until all 32,000 are done.

At 400 Tasks/wave: 32,000 ÷ 400 = **80 waves of parallel execution**.

</details>

---

**M2. Your Spark job's Driver crashes mid-way through processing. The 100 Executors are still healthy and have completed 60% of the Tasks. What happens?**

<details>
<summary>▶ Answer</summary>

**The entire job fails.** The Driver is the single point of failure. When it crashes:

- All Executors lose their connection to the Driver
- Cluster Manager detects the Driver is dead
- All Executor processes are terminated (their resources released back to the cluster)
- The 60% completed work is lost — partial results in Executor RAM are gone

**To restart:** You must re-submit the entire job. It starts from scratch.

**How production teams handle this:**
- Run Driver in **cluster mode** on a reliable, managed machine (not your laptop)
- Use Databricks or cloud-managed Spark which can auto-restart the Driver
- Design jobs with **checkpointing** — periodic snapshots of intermediate results to disk so a restart can resume from the last checkpoint, not from scratch (you'll learn this in streaming topics)

</details>

---

**M3. An Executor on Worker Node 7 dies mid-job. It was running Tasks 201 through 208 (8 Tasks, one per core). What exactly happens next? Does the job fail?**

<details>
<summary>▶ Answer</summary>

**No — the job does NOT fail.** Only those 8 Tasks are affected.

Here is what happens step by step:

1. Driver stops receiving heartbeats from Executor on Worker Node 7
2. After a timeout (~60 seconds by default), Driver marks Executor 7 as dead
3. Driver marks Tasks 201–208 as "failed" and adds them back to the pending Task queue
4. Driver reschedules all 8 Tasks on other healthy Executors that have free slots
5. Those Executors re-read the data for those 8 partitions from HDFS/S3 and re-process them
6. Job continues — only these 8 Tasks were lost; all others proceed normally

**The cost:** Some slowdown because of the timeout wait and re-execution. If the Executor died because of a systematic issue (bad data partition causing OOM), it may fail repeatedly — and Spark will retry a limited number of times before truly failing the job.

</details>

---

**M4. A junior DE says: "Why do we need the Cluster Manager? Can't the Driver just directly start Executors on machines?" What's the problem with skipping the Cluster Manager?**

<details>
<summary>▶ Answer</summary>

In theory, yes — and Spark Standalone actually does something close to this. But in a real multi-tenant environment, skipping the Cluster Manager causes serious problems:

**Problem 1 — Resource conflicts:** Multiple Spark jobs run on the same cluster simultaneously (your job + your colleague's job + the nightly ETL). Without a Cluster Manager, every Driver would try to use every machine → all jobs starve each other or crash.

**Problem 2 — No resource tracking:** The Cluster Manager knows which machines have 20 free cores vs 0 free cores. Without it, the Driver has no way to know what's available — it would have to guess.

**Problem 3 — No fair sharing:** YARN implements resource queues — "team A gets 40% of the cluster, team B gets 60%". Without a Cluster Manager, no way to enforce this policy.

**Problem 4 — Non-Spark workloads:** In a company, the same machines run Spark jobs, MapReduce jobs, Python scripts, ML training. YARN/Kubernetes manages ALL of them together. If Spark bypassed the Cluster Manager, it would fight with these other workloads.

The Cluster Manager is the referee that makes a multi-tenant cluster work predictably.

</details>

---

#### 🔴 Hard

**H1. You run `.collect()` on a 500 GB DataFrame in production. The Driver has 16 GB RAM. Walk through exactly what happens and why this is dangerous.**

<details>
<summary>▶ Answer</summary>

`.collect()` is an Action that tells Spark: "Bring ALL rows of this DataFrame back to the Driver as a Python list."

Here is what happens step by step:

1. Driver sends Tasks to Executors to process the 500 GB data
2. All Executors produce their results and start streaming them back to the Driver over the network
3. Driver starts receiving rows and accumulating them in its JVM heap memory
4. Driver's 16 GB RAM fills up — it has received maybe 50 GB of the 500 GB
5. JVM heap overflows → **OutOfMemoryError (OOM)** → Driver process crashes
6. **Entire job fails.** All 50 Executors are terminated. 450 GB of data never processed.

**Why this is dangerous in production:**
- The job crashes after running for hours — wasted compute cost
- If it's a scheduled pipeline, downstream jobs waiting for this output also fail
- Recovery requires re-running the entire job

**What to do instead:**
- Write output to storage: `.write.parquet("s3://bucket/output/")` — Executors write directly to S3, nothing goes to Driver
- Take a sample: `.limit(1000).collect()` or `.sample(0.001).collect()` for inspection
- Use `.show(20)` to view a few rows — only sends 20 rows to Driver, safe

**The rule:** The Driver coordinates. It never processes or holds large data. Everything large goes directly to storage.

</details>

---

**H2. On Databricks, you don't configure YARN or Kubernetes directly. Does that mean understanding Cluster Managers is irrelevant for Databricks users? Argue for and against.**

<details>
<summary>▶ Answer</summary>

**For (irrelevant):** In Databricks, you configure a cluster via UI: "I want 8 worker nodes, each Standard_DS3_v2 (4 cores, 14 GB RAM)". Databricks handles the rest — starts Executors, manages node failures, auto-scales. You never write a YARN config file.

**Against (absolutely relevant) — and this wins:**

**1. Resource request tuning:** When your job shows "Executor allocation timeout" or "not enough resources", you need to know what's happening at the Cluster Manager level to fix it. "Add more workers" or "change the cluster config" requires understanding what you're actually changing.

**2. Spark UI interpretation:** Databricks gives you full Spark UI. The Executors tab shows each Executor, its cores, its memory usage, its Tasks completed. If you don't know what an Executor is, you can't diagnose performance issues.

**3. `spark.executor.memory`, `spark.executor.cores`, `spark.driver.memory`:** These are configs you set in Databricks cluster settings or in `SparkConf`. If you don't know what Executor memory does, you can't tune them — and untuned jobs spill, OOM, and run 10x slower than they should.

**4. Understanding job failures:** "Executor killed by YARN for exceeding memory limits" — this error message only makes sense if you know what YARN and Executors are.

**Verdict:** Databricks abstracts the operations. It does not abstract the concepts. You still need to understand Driver/Executor/Cluster Manager to configure clusters correctly, tune performance, and diagnose failures. The abstraction removes configuration work, not conceptual understanding.

</details>

---

**H3. A Spark cluster has 10 Executors with 10 cores each = 100 parallel Tasks. A job has 50 partitions (= 50 Tasks). Only 50 Tasks ever run in parallel even though 100 slots are available. Then someone says "increase partitions to 1000." Will the job run faster? When does more partitions stop helping?**

<details>
<summary>▶ Answer</summary>

**Will 1000 partitions run faster than 50 partitions on this 100-slot cluster?**

Yes, likely — up to a point. Here's why:

With 50 partitions and 100 slots:
- Only 50 Tasks run at the same time (50 partitions = max 50 Tasks)
- 50 slots are always idle — half the cluster is wasted
- Each Task processes `total_data / 50` of data

With 1000 partitions and 100 slots:
- 100 Tasks run in parallel (full cluster utilized)
- 1000 ÷ 100 = 10 waves of Tasks
- Each Task processes `total_data / 1000` = smaller, faster per Task
- Cluster utilization: 100% (100 slots / 100 slots)

**So yes — more partitions → better parallelism → faster.**

**But: when does more partitions stop helping?**

**Too many partitions causes its own problems:**

1. **Task scheduling overhead:** The Driver must schedule, track, and monitor millions of Tasks. The Driver itself becomes a bottleneck — scheduling overhead exceeds processing time.

2. **Too-small partitions:** If each partition is 1 KB, the Task startup overhead (JVM initialization, network comm, serialization) is larger than the actual work. You waste more time on overhead than computation.

3. **Shuffle amplification:** Operations like `groupBy` require shuffling data between Executors. With 1M partitions, the shuffle creates massive network traffic.

**The sweet spot:**
- Target **100–200 MB per partition** for general workloads
- Target **2–4× the number of available cores** as number of partitions for maximum parallelism
- For this 100-slot cluster: 200–400 partitions is a reasonable range

**The formula used in production:**
```
ideal_partitions = max(2 × total_executor_cores, total_data_size_MB / 200)
```

This is called **repartitioning strategy** — one of the most important tuning levers for Spark performance.

</details>

---

*More topics added as we progress.*
