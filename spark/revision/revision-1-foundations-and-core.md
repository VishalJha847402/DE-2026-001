# 🔁 Revision 1 — Foundations + Spark Core (Lessons 1–9)

> **This is a recall tool, not a re-reading tool.**
> Cover every answer. Try to retrieve it from memory FIRST. Only then reveal and check.
> Retrieving from memory (even when you fail) is what builds permanent, deep understanding.

**Covers:** Phase 0 (all) + Phase 1 Topics 2–4a
1. Why One Machine Breaks · 2. HDFS · 3. MapReduce→Spark
4. Driver/Executors/Cluster Mgr · 5. SparkSession · 6. RDD
7. Transformations vs Actions / Lazy · 8. Narrow vs Wide · 9. The Shuffle

---

## 📅 How to use (spaced repetition — DE-2026 Rule #13)

Revisit this SAME file 3 times at growing gaps:

| When | Do these layers | Time |
|------|-----------------|------|
| **+1 day** after learning | Layer 1 (Flash Recall) | 10 min |
| **+1 week** | Layers 1 + 2 + 3 | 40 min |
| **+1 month** | All 4 layers incl. Boss Fight | 90 min |

Rule: **cover the answer, recall out loud or in GoodNotes, THEN reveal.** No peeking first.
After each pass, fill the **Self-Score Tracker** at the bottom. 🔁 = revisit next time.

---

## ⚡ Layer 1 — Flash Recall (rapid one-liners)

> Read the question. Say the answer in one breath. Reveal to check. Go fast.

**1. The golden path data must follow inside a computer?**
<details><summary>▶</summary>Disk → RAM → CPU. CPU can't read disk directly; RAM is the only gateway.</details>

**2. Scale Up vs Scale Out in 5 words each?**
<details><summary>▶</summary>Scale Up = one bigger machine. Scale Out = many machines, split work (Spark).</details>

**3. HDFS — NameNode stores ___, DataNodes store ___?**
<details><summary>▶</summary>NameNode = metadata (block map). DataNodes = actual data blocks. Default block 128 MB, replication 3.</details>

**4. MapReduce's fatal flaw?**
<details><summary>▶</summary>Writes to disk after every step. Disk is 100x slower than RAM. Spark keeps data in RAM between steps.</details>

**5. The three roles in every Spark job?**
<details><summary>▶</summary>Driver (plans + schedules) · Cluster Manager (gives machines) · Executors (do the work).</details>

**6. One Executor with 8 cores runs how many Tasks at once?**
<details><summary>▶</summary>8 — one Task per core. Cores = parallel slots.</details>

**7. What does `getOrCreate()` guarantee?**
<details><summary>▶</summary>One SparkSession per JVM. Returns existing one if it exists, else creates it.</details>

**8. RDD stands for? Its 3 properties?**
<details><summary>▶</summary>Resilient Distributed Dataset. Partitions · Immutability · Lineage.</details>

**9. What is lineage and why does it matter?**
<details><summary>▶</summary>The recipe of how an RDD was built. Lets Spark rebuild a lost partition without copying data (fault tolerance).</details>

**10. Transformation vs Action — the one-line test?**
<details><summary>▶</summary>Returns a DataFrame you can keep chaining → transformation (lazy). Returns a value / prints / writes → action (runs everything).</details>

**11. What is lazy evaluation?**
<details><summary>▶</summary>Transformations build a plan and run nothing. The action runs the whole plan. Lets Spark optimize before running.</details>

**12. Narrow vs Wide in one line?**
<details><summary>▶</summary>Narrow = 1 input partition → 1 output (no shuffle, cheap). Wide = many inputs → 1 output (shuffle, expensive).</details>

**13. Name 3 wide transformations.**
<details><summary>▶</summary>groupBy, join, orderBy (also distinct, repartition, reduceByKey).</details>

**14. Every wide transformation creates a ___?**
<details><summary>▶</summary>Shuffle = a stage boundary. Count shuffles ≈ count stages.</details>

**15. The two sides of a shuffle?**
<details><summary>▶</summary>Map side (shuffle write: hash, bucket, write to local disk). Reduce side (shuffle read: fetch from all map tasks, combine).</details>

**16. The #1 config to tune for shuffles? Default value?**
<details><summary>▶</summary>`spark.sql.shuffle.partitions`, default 200. Target ~128–200 MB per partition.</details>

**17. What is data skew and why is it deadly at a shuffle?**
<details><summary>▶</summary>One hot key → all its rows in one giant partition. The barrier means everyone waits for that one slow task. Fix: salting or AQE skew join.</details>

---

## 🧠 Layer 2 — Concept Recall (explain in your own words)

> Say a full 2–4 sentence explanation OUT LOUD before revealing. Compare yours to the model answer.

**C1. Why does a single machine "break" on big data — and why isn't a faster CPU the fix?**
<details><summary>▶ Model answer</summary>

Data must go Disk → RAM → CPU, and the CPU can only work on data in RAM. If the dataset is bigger than RAM (e.g., 5 TB on a 16 GB machine), the OS swaps to disk and everything slows 100x, or it crashes. A faster CPU doesn't help because the bottleneck is the **RAM ceiling** and the disk, not CPU speed. The real fix is Scale Out — split the data across many machines, each with its own RAM, processing in parallel.
</details>

**C2. Explain how lineage gives Spark fault tolerance WITHOUT copying data 3 times.**
<details><summary>▶ Model answer</summary>

Spark records how every RDD was built from its parent (the lineage / recipe). When an Executor dies and its partitions are lost, Spark reads the lineage to find exactly how to rebuild just those partitions — it re-reads the original source blocks (still safe on HDFS/S3) and replays the transformations for only the lost partitions. No backup copies of intermediate data are needed. Storing a recipe (tiny metadata) is far cheaper than storing 3 copies of the data (HDFS-style replication of RAM).
</details>

**C3. Why is lazy evaluation a performance advantage, not just a quirk?**
<details><summary>▶ Model answer</summary>

Because Spark sees the whole plan before running anything, it can optimize globally: predicate pushdown (filter while reading the file), column pruning (read only needed columns), fusing narrow steps into one pass, and stopping early if you only asked for `take(5)`. An eager system runs each line immediately and has already committed to wasteful work before it learns what you actually need. Lazy = foresight = optimization. Reading 500 GB can become reading 20 GB automatically.
</details>

**C4. Explain, end to end, what physically happens during a `groupBy("city").sum()` shuffle.**
<details><summary>▶ Model answer</summary>

Map side: each task computes `hash(city) % numPartitions` for its rows, does a partial sum per city within its own partition (map-side combine), buckets the partial sums, and writes them to local disk as shuffle files. Barrier: all map tasks must finish. Reduce side: each reduce task fetches its assigned bucket from every map task over the network, then adds up all the partial sums to get each city's final total. The cost is disk write + serialize + network fetch (M×R connections) + disk read + the barrier wait. Partial aggregation shrinks the data so only a few partial sums cross the network, not all raw rows.
</details>

**C5. Why is the Driver both the brain and the biggest risk of a Spark job?**
<details><summary>▶ Model answer</summary>

The Driver runs your code, builds the plan, breaks it into Tasks, schedules them, and monitors Executors — it's the coordinator (brain). But it's a single process and a single point of failure: if it crashes, the whole job dies even if all Executors are healthy. That's why you never bring big data to it (no `.collect()` on huge DataFrames — OOM kills it). The Driver coordinates; it must never process or hold large data.
</details>

---

## 🔀 Layer 3 — Interleaved Hard Mix (combine multiple topics)

> These deliberately mix 2–3 lessons. This is where hidden gaps show up. Struggle is expected and good.

**X1. You cache an RDD, then an Executor holding cached partitions crashes mid-job. Walk through recovery and explain why cache did NOT save you any recompute. (RDD + Lineage + Cache + Fault Tolerance)**
<details><summary>▶ Answer</summary>

The cache lives in that Executor's RAM — which is exactly what was lost. So Spark falls back to lineage: it traces back to the original source file, re-reads the relevant blocks, and replays all transformations to rebuild the lost partitions. The cache saved nothing here because cache is a **performance** optimization (avoids recompute on *future actions* when the Executor is alive), not a **fault-tolerance** mechanism. For fault tolerance that survives Executor death, you need `checkpoint()` — which writes to reliable disk (HDFS/S3) and truncates lineage.
</details>

**X2. A job does `filter → groupBy("city") → orderBy("total")`. It's slow. Using narrow/wide + shuffle + lazy eval, explain WHERE the time goes and ONE change to move less data. (Narrow/Wide + Shuffle + Lazy)**
<details><summary>▶ Answer</summary>

`filter` is narrow (cheap, no shuffle). `groupBy` and `orderBy` are each wide → 2 shuffles → 2 stage boundaries → that's where ~all the time goes (disk write, network fetch, barrier). Because Spark is lazy, it can push the filter into the file read, so make sure the filter is BEFORE the groupBy so the shuffle carries the smallest possible data. If only a subset is needed (e.g., one region), filter that first too. The two shuffles are the cost centers — confirm with `.explain()` (look for 2 `Exchange` nodes) and the Spark UI Shuffle Read/Write columns.
</details>

**X3. You join a 3 TB orders table with a 4 MB city-lookup table. Default behavior shuffles 3 TB. How do you make this nearly free, and which earlier concepts explain why it works? (Wide/Shuffle + Broadcast + Driver/Executors)**
<details><summary>▶ Answer</summary>

Use a **broadcast join**: `orders.join(broadcast(city_lookup), "city_id")`. Spark sends a full copy of the tiny 4 MB table to every Executor's RAM; each Executor joins its local partition of the 3 TB table against the in-memory copy. The 3 TB table never moves — no shuffle at all. It works because Executors each have their own RAM (can hold a 4 MB copy) and the Driver collects + ships the small table once. This converts an expensive wide operation into something nearly as cheap as a narrow one. AQE can do this automatically when it detects a small side.
</details>

**X4. `spark.sql.shuffle.partitions = 200` on a 10 GB job AND on a 5 TB job. Explain why the SAME setting is wrong for both, in opposite ways. (Shuffle config + Partitions + Tasks)**
<details><summary>▶ Answer</summary>

10 GB / 200 = 50 MB per partition — too SMALL. Fine-ish, but if data were even smaller you'd get hundreds of tiny tasks where scheduling overhead dominates the actual work. 5 TB / 200 = 25 GB per partition — way too BIG. No task can hold 25 GB → heavy spill to disk or OOM, job crawls/crashes. The default 200 is a fixed number but the right value depends on data size: target ~128–200 MB per partition (`data_MB / 150`). So 5 TB needs ~33,000 partitions, not 200. AQE auto-sizes this at runtime.
</details>

**X5. A 10,000-task map stage finishes in 1 min except ONE task that takes 12 min, then the whole job stalls. Name the phenomenon, why the barrier makes it catastrophic, and 2 fixes. (Shuffle barrier + Skew + Stragglers)**
<details><summary>▶ Answer</summary>

This is a **straggler**, almost certainly caused by **data skew** — that one task got a hot key (huge partition). The shuffle **barrier** means the reduce stage cannot start until ALL map tasks finish, so 9,999 idle Executors wait 12 minutes for one task → the cluster runs at the speed of its slowest task. Fixes: (1) **salting** — add a random suffix to the hot key to spread it across many partitions, then two-stage aggregate; (2) **AQE skew join** (`spark.sql.adaptive.skewJoin.enabled=true`) — Spark detects the oversized partition at runtime and splits it; also (3) **speculative execution** re-launches the slow task elsewhere.
</details>

---

## 🏆 Layer 4 — Boss Fight (one scenario, everything at once)

> Do this on the +1 month pass. Spend 20–30 min. Write the full answer in GoodNotes before revealing.

**THE SCENARIO — Swiggy, end to end:**

You're a DE at Swiggy. You have **4 TB of order data** in S3 (Parquet). You must produce: *total revenue per restaurant, for delivered orders above ₹200, in the top 5 cities, sorted high to low.* Your cluster: **25 Executors × 8 cores, 16 GB RAM each.** The job keeps failing with OOM on one task, and even when it runs, it's slow.

Answer ALL of these:
1. How many partitions/Tasks does the read create, and how many run in parallel?
2. Which operations are narrow, which are wide? How many shuffles/stages?
3. Where should the filters go and why?
4. The OOM is on one task during the per-restaurant groupBy — what's the likely cause and 2 fixes?
5. The city-lookup table is 3 MB — how do you join it without a shuffle?
6. One Executor dies after the groupBy shuffle wrote its files — what happens?

<details><summary>▶ Full worked answer</summary>

**1. Partitions/Tasks & parallelism:**
4 TB ÷ 128 MB ≈ **32,000 partitions = 32,000 Tasks** (read stage). Parallel slots = 25 × 8 = **200 Tasks at once** → ~160 waves.

**2. Narrow vs wide / shuffles / stages:**
- Narrow: read, `filter(status='delivered')`, `filter(amount>200)`, `select` — all map-side, no shuffle.
- Wide: `groupBy("restaurant").sum()` (shuffle 1), filter to top-5 cities may need a join/aggregate, final `orderBy` (shuffle 2).
- Roughly **2 shuffles → 3 stages** (more if the top-5-cities step adds a shuffle).

**3. Filters first (push them before any shuffle):**
Apply both filters (delivered, >₹200) and the city restriction as early as possible — they're narrow and shrink the data before the expensive groupBy shuffle. Filtering 4 TB down to, say, 600 GB before shuffling means the shuffle moves 600 GB, not 4 TB. Spark's predicate pushdown also applies the filters during the Parquet read.

**4. OOM on one groupBy task — cause + fixes:**
Likely **data skew** — one mega-restaurant (or a null/"unknown" restaurant_id) has a huge share of orders, so its partition is enormous and won't fit in a 16 GB task. Fixes: (a) **salting** the restaurant_id to spread the hot key across partitions, then two-stage aggregate; (b) enable **AQE skew join / adaptive** to auto-split the skewed partition; also increase `spark.sql.shuffle.partitions` so partitions are ~150 MB. Map-side partial aggregation already helps but won't save a single mega-key alone.

**5. Broadcast the 3 MB city lookup:**
`orders.join(broadcast(city_lookup), "city_id")` — copy the tiny table to every Executor's RAM, join locally, the 4 TB side never shuffles. Nearly free.

**6. Executor dies after writing shuffle files:**
Its shuffle files lived on its local disk → lost. Reduce tasks fetching from it get `FetchFailedException`. Spark detects the lost map output and **re-runs that map task** on a healthy Executor to regenerate the shuffle files, then the reduce fetch retries. (An External Shuffle Service would let the files survive the Executor's death and avoid this recompute.)

**If you answered all 6 correctly → you genuinely own Phase 0 + Phase 1 core. That's interview-ready.**
</details>

---

## 📊 Self-Score Tracker

Fill after each pass. 🟢 = solid, recall was fast and correct. 🔁 = stumbled, revisit next time.

| Topic | +1 day | +1 week | +1 month |
|-------|:------:|:-------:|:--------:|
| 1 · Why one machine breaks | ⬜ | ⬜ | ⬜ |
| 2 · HDFS | ⬜ | ⬜ | ⬜ |
| 3 · MapReduce → Spark | ⬜ | ⬜ | ⬜ |
| 4 · Driver/Executors/Cluster Mgr | ⬜ | ⬜ | ⬜ |
| 5 · SparkSession | ⬜ | ⬜ | ⬜ |
| 6 · RDD | ⬜ | ⬜ | ⬜ |
| 7 · Transformations/Actions/Lazy | ⬜ | ⬜ | ⬜ |
| 8 · Narrow vs Wide | ⬜ | ⬜ | ⬜ |
| 9 · The Shuffle | ⬜ | ⬜ | ⬜ |
| Boss Fight (6/6?) | — | — | ⬜ |

> Any 🔁 → that's your priority next session. Tell me "revise <topic>" and I'll go deeper or re-explain differently.

---

*Revision 1 covers Lessons 1–9. Next revision file (Revision 2) will come after Topic 4 + Topic 5 are complete, mixing the new concepts with these.*
