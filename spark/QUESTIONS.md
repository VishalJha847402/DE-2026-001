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

*More topics will be added here as we progress through the series.*
