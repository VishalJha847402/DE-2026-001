# Practice — Spark Topic 2: SparkSession & SparkContext

> **BUILD → BREAK → EXPLAIN.** Turn the key, use one session for DataFrames *and*
> SQL, prove the singleton, and feel what a bad config does. Output ≠ proof —
> explain *why*.

Setup: `pip install pyspark` and the OrderIQ CSVs from `datasets/`. Reuse this
starter (note: **no `spark` is pre-made outside Databricks — you create it**):

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").appName("orderiq-t2").getOrCreate()
```

---

## 🟢 Easy 1 — turn the key, then look inside

1. Print `spark.version` and `spark.sparkContext` — what does the second show, and
   why does a *SparkSession* contain a *SparkContext*?
2. Open the Spark UI (URL Spark prints). In the **Environment** tab, find
   `spark.master` and `spark.app.name`. Do they match what you set?

<details><summary>Answer</summary>

1. `spark.sparkContext` is the underlying `SparkContext` — the actual cluster
   connection. SparkSession is the modern wrapper; the engine still runs on `sc`.
2. Yes — `spark.master = local[*]`, `spark.app.name = orderiq-t2`. The UI reflects
   your builder config.
</details>

---

## 🟢 Easy 2 — one session, two APIs

Prove the "unified entry point" claim on OrderIQ:

```python
orders = spark.read.csv("datasets/data/orders.csv", header=True, inferSchema=True)
orders.createOrReplaceTempView("orders")

a = orders.filter("status='delivered'").groupBy("city").count()   # DataFrame API
b = spark.sql("SELECT city, COUNT(*) AS count FROM orders WHERE status='delivered' GROUP BY city")  # SQL
```

1. Do `a` and `b` produce the same result? (`a.show()`, `b.show()`.)
2. What single object gave you *both* the DataFrame API and SQL?

<details><summary>Answer</summary>

1. Identical results — same data, same logic, two syntaxes.
2. The one `spark` SparkSession. Pre-2.0 you'd have needed SparkContext *and*
   SQLContext; SparkSession unifies them.
</details>

---

## 🟡 Medium 1 — prove the singleton

```python
s1 = SparkSession.builder.appName("Alpha").getOrCreate()
s2 = SparkSession.builder.appName("Beta").getOrCreate()
print(s1 is s2)
print(s2.conf.get("spark.app.name"))
```

1. What prints for `s1 is s2`?
2. What app name comes back — "Alpha" or "Beta"? Why is the second `appName`
   silently ignored?

<details><summary>Answer</summary>

1. `True` — same object.
2. The **first** app name that actually created the session wins ("Alpha" if this
   is the first session in the JVM). `getOrCreate()` sees an existing session and
   returns it without applying the new builder settings.
</details>

---

## 🟡 Medium 2 — config priority + right-sizing

1. Set shuffle partitions two ways and check which wins:
```python
spark.conf.set("spark.sql.shuffle.partitions", "8")
print(spark.conf.get("spark.sql.shuffle.partitions"))
```
2. Run a groupBy and check the **Stages** tab: how many Tasks does the post-shuffle
   stage have? Relate it to the `8` you set.

<details><summary>Answer</summary>

1. Prints `8` — a runtime `spark.conf.set` overrides the default 200.
2. The aggregation stage runs **8 Tasks** — `spark.sql.shuffle.partitions`
   controls the number of partitions (and thus Tasks) produced by a shuffle.
</details>

---

## 🔴 Hard — BREAK with a bad config, then FIX

**Break it:** restart Spark leaving the default shuffle partitions, on the tiny
OrderIQ file:

```python
spark.stop()
spark = (SparkSession.builder.master("local[*]").appName("badcfg")
         .config("spark.sql.shuffle.partitions", "200")   # default, wrong for tiny data
         .getOrCreate())
orders = spark.read.csv("datasets/data/orders.csv", header=True, inferSchema=True)
orders.groupBy("city").count().collect()
```

1. Open **Stages** → how many Tasks in the groupBy stage? How many rows does each
   partition actually hold (roughly)?
2. Why is this *slower* than using 8 partitions, even though nothing crashes?
   (Think: work per Task vs overhead per Task.)
3. **Fix it** for tiny local data, and state the rule of thumb for choosing this
   number in production on a 5 TB file.

<details><summary>Answers</summary>

1. 200 Tasks — but the file has, say, a few thousand rows, so most partitions hold
   ~a handful of rows, and many are **empty**.
2. Each Task has fixed overhead (scheduling, serialization, JVM bookkeeping). With
   200 near-empty partitions, you pay 200× overhead to do almost no real work —
   overhead dominates. Fewer, fuller partitions finish faster.
3. Fix: `spark.conf.set("spark.sql.shuffle.partitions", "8")` (≈ your core count
   for tiny data). Production rule: target **~100–200 MB per post-shuffle
   partition** → for 5 TB, ~30,000–50,000 partitions; also keep it ≥ 2–4× total
   cores so no slot sits idle.
</details>

---

### ✅ Mastery check for Topic 2

Without notes:

- create a SparkSession and explain the 4 things `getOrCreate()` does,
- use one `spark` for both DataFrame and SQL,
- explain the singleton (why a 2nd `getOrCreate()` returns the same object),
- and right-size `spark.sql.shuffle.partitions` for both tiny and 5 TB data.

Passed? → **Topic 3 — RDD: Partitions, Immutability & Lineage** (what Spark's data
actually *is* underneath the DataFrame).

*Back to the [lesson](./README.md).*
