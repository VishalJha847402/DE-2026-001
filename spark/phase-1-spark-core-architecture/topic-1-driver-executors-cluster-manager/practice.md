# Practice — Spark Topic 1: Driver, Executors & Cluster Manager

> **BUILD → BREAK → EXPLAIN.** You'll start a real Spark engine on the OrderIQ
> data, *see* the three roles in the Spark UI, crash the Driver on purpose, and
> reason about Task math. Output ≠ proof — you must explain *why* each thing happens.

---

## 🛠️ One-time setup (local Spark, ~5 min)

Spark runs fine on one laptop — "local mode" makes one machine act as Driver +
Executor so you can learn every concept without a cluster.

```bash
pip install pyspark            # that's it — bundles everything
# make sure the OrderIQ CSVs exist (from datasets/ — see datasets/README.md)
cd datasets && python generate.py --orders 100000 --out ./data
```

Starter code (paste at the top of every problem):

```python
from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .master("local[4]")          # 1 machine acting as 4 cores = 4 Task slots
         .appName("orderiq-t1")
         .getOrCreate())

orders = spark.read.csv("datasets/data/orders.csv", header=True, inferSchema=True)
print("rows:", orders.count())
print("partitions:", orders.rdd.getNumPartitions())
```

> ✅ Ready when `orders.count()` prints a number and you can open the Spark UI at
> the URL Spark prints (usually `http://localhost:4040`). Keep that tab open.

---

## 🟢 Easy 1 — see the three roles

Run the starter, then open the Spark UI.

1. In the **Executors** tab, how many Executors do you see, and how many **cores**
   does each report? (In local mode, Driver and Executor live in one process.)
2. `spark.sparkContext.defaultParallelism` — what number, and why does it equal
   your `local[4]`?
3. Run `orders.filter(orders.status == "delivered").count()`. In the **Jobs → Stages**
   tab, how many **Tasks** did that stage run? Relate it to `getNumPartitions()`.

<details><summary>What you should observe</summary>

1. One Executor (the local one) with 4 cores. Local mode fuses Driver+Executor.
2. `4` — `local[4]` gives 4 slots, so `defaultParallelism` = 4.
3. Number of Tasks = number of partitions of `orders`. One Task per partition —
   the 1:1 rule. Small CSV may be a few partitions; each is one Task.
</details>

---

## 🟢 Easy 2 — Driver holds data only when you TELL it to

Predict which of these send data to the Driver, then run all three:

```python
orders.write.mode("overwrite").parquet("datasets/data/orders_parquet")  # A
orders.show(5)                                                           # B
rows = orders.collect()                                                  # C  (small data OK here)
```

1. Which lines move data **to the Driver**, and which keep it on the Executors?
2. Why is C safe on 100k rows but a disaster on 5 TB?

<details><summary>Answer</summary>

- **A** — Executors write directly to disk; **nothing** goes to the Driver. Safe at any size.
- **B** — only ~5 rows go to the Driver. Safe.
- **C** — **all** rows travel into the Driver's RAM. Fine for 100k tiny rows; on
  5 TB it overflows the Driver → OOM → whole job dies.
</details>

---

## 🟡 Medium 1 — Task / partition / core math

Your OrderIQ orders file is 4 TB in production. Cluster: 50 Executors × 8 cores.
Partition size 128 MB.

1. How many **partitions** (= Tasks)?
2. How many Tasks run **in parallel** at once?
3. How many sequential **waves** of Tasks?

<details><summary>Answer</summary>

1. 4 TB = 4,096,000 MB ÷ 128 MB = **32,000 Tasks**.
2. 50 × 8 = **400 in parallel**.
3. 32,000 ÷ 400 = **80 waves**.
</details>

---

## 🟡 Medium 2 — increase parallelism yourself

On your local machine:

```python
print(orders.rdd.getNumPartitions())          # say it's small, e.g. 1–2
more = orders.repartition(8)
print(more.rdd.getNumPartitions())             # 8
more.filter("status='delivered'").count()
```

1. After `repartition(8)`, how many Tasks does the `count` stage run?
2. On `local[4]`, does 8 partitions run faster than 2? Why / why not — think about
   **slots vs partitions**.
3. **Break-it:** `orders.repartition(5000).count()` on your laptop. Is it faster or
   slower? Why does *too many* tiny partitions hurt?

<details><summary>Answer</summary>

1. 8 Tasks (one per partition).
2. With only 2 partitions, just 2 of your 4 slots work — half idle. 8 partitions
   fill all 4 slots (in 2 waves) → better utilization. More partitions than slots
   is fine; fewer wastes slots.
3. Slower — 5000 partitions on 100k rows means ~20 rows each. Per-Task startup
   (scheduling, serialization) dwarfs the actual work. Overhead > compute. Sweet
   spot ≈ 2–4× cores, ~100–200 MB per partition.
</details>

---

## 🔴 Hard — BREAK the Driver, then FIX it

**Break it (do this on purpose):**

```python
# Simulate the classic production mistake: pull everything to the Driver.
# Lower the Driver heap first so it fails fast on modest data:
#   restart spark with .config("spark.driver.memory", "512m") in the builder
big = orders.crossJoin(orders.select("order_id").limit(20000))   # blow up row count
data = big.collect()     # ❌ pulls millions of rows into the Driver
```

1. What error do you get, and **which role** died? What happened to the Executors?
2. Explain the exact chain: why did `.collect()` cause it, and why does the *whole
   job* fail rather than just one Task?

**Fix it:** rewrite the intent ("materialize delivered orders per city") so the
Driver never holds the big data.

<details><summary>Answers</summary>

1. `OutOfMemoryError` (Java heap) — the **Driver** died. When the Driver dies,
   Spark tears down the Executors too (they have no boss) → job fails entirely.
2. `.collect()` streams *every* row from all Executors into the Driver's JVM heap.
   The heap is small (512m here) and fills long before all rows arrive → OOM. The
   Driver is the single point of failure, so its death kills the job — unlike an
   Executor death, which just reschedules that Executor's Tasks.

**Fix — keep big data on the Executors, write to storage:**
```python
(orders.filter("status='delivered'")
       .groupBy("city").count()
       .write.mode("overwrite").parquet("datasets/data/delivered_by_city"))
# Executors write directly to disk. Driver only coordinates. No OOM at any scale.
# If you must inspect: .show(20) or .limit(1000).collect() — tiny, safe.
```
</details>

---

### ✅ Mastery check for Topic 1

You own it when you can, without notes:

- point to Driver, Cluster Manager, Executor in the Spark UI and say each one's job,
- do the Task = partitions, parallel = Executors × cores math,
- explain why `.collect()` on big data kills the Driver (and thus the job),
- and explain why an *Executor* death is survivable but a *Driver* death is not.

Passed? → **Topic 2 — SparkSession & SparkContext** (the entry point your Driver
creates first).

*Back to the [lesson](./README.md).*
