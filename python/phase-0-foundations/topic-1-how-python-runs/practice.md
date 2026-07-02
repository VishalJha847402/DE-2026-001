# Practice — Python Topic 1: How Python Actually Runs

> **BUILD → BREAK → EXPLAIN.** You'll look at real bytecode, race the slow path vs
> the fast path on OrderIQ, and prove the GIL's behaviour with your own threads.
> Output ≠ proof — after each problem, explain *why* in one or two plain sentences.
>
> Needs: `pip install numpy` (once) + the OrderIQ CSVs (`datasets/README.md`).

---

## 🟢 Easy 1 — see your own bytecode

```python
import dis

def gst(amount):
    return amount * 1.18

dis.dis(gst)
```

1. How many bytecode instructions did one line of Python become?
2. Point at the instruction that does the multiplication.
3. In one plain sentence: who *executes* these instructions, and one at a time or
   all at once?

<details><summary>Answer</summary>

1. Typically 3–4 (`LOAD_FAST`, `LOAD_CONST`, `BINARY_MULTIPLY`/`BINARY_OP`, `RETURN_VALUE`).
2. `BINARY_MULTIPLY` (or `BINARY_OP 5 (*)` on newer Pythons).
3. The CPython interpreter — a C program — executes them **one at a time** in its
   fetch-decode-execute loop. That per-instruction loop is what "interpreted" means.
</details>

---

## 🟢 Easy 2 — find the bytecode cache

1. Create a tiny module `helper.py` (any function inside). In another file,
   `import helper` and run it.
2. Look at the folder — what appeared? Open `__pycache__/`. What's inside, and why
   does it make the *second* run start faster?
3. Does it make the program *run* faster too? Why not?

<details><summary>Answer</summary>

1–2. A `__pycache__/` folder with `helper.cpython-3XX.pyc` — the **compiled
bytecode**, cached so the next run skips the compile step.
3. No — only *startup* is faster. Execution still goes through the same
interpreter loop either way; caching skips compilation, not interpretation.
</details>

---

## 🟡 Medium 1 — race the slow path vs the fast path on OrderIQ

```python
import csv, time
import numpy as np

with open("datasets/data/orders.csv") as f:
    amounts = [float(r["amount"]) for r in csv.DictReader(f) if r["amount"]]
print(len(amounts), "amounts loaded")

# slow path — per-row Python
start = time.time()
total = 0.0
for a in amounts:
    total += a * 1.18
py = time.time() - start

# fast path — vectorized C
arr = np.array(amounts)
start = time.time()
total_np = (arr * 1.18).sum()
npt = time.time() - start

print(f"loop {py:.4f}s | numpy {npt:.4f}s | {py/npt:.0f}x faster")
```

1. What speedup do you get? Name the **three taxes** the loop pays per row that
   NumPy avoids.
2. Regenerate the dataset bigger (`python generate.py --orders 1000000`) and rerun.
   Does the speedup grow or shrink? Why?

<details><summary>Answer</summary>

1. Usually 20–100x. The three per-row taxes: interpreter overhead
   (fetch/decode/execute per element), dynamic type-checking per operation, and
   heavy Python objects (allocation + pointer-chasing) — NumPy does one C call
   over a contiguous typed block.
2. **Grows** — the per-row taxes scale with row count, while NumPy's one-time call
   overhead stays constant. The bigger the data, the more vectorization wins.
   That's exactly why this matters for DE-scale data.
</details>

---

## 🟡 Medium 2 — BREAK it: threads on CPU-bound work

Predict first: 4 threads on a 4+ core machine — how much faster than 1 thread?

```python
import time
from threading import Thread

def crunch(n):                      # pure-Python CPU work
    total = 0
    for i in range(n):
        total += i * i
    return total

N = 5_000_000

start = time.time()                 # sequential: 4 runs one after another
for _ in range(4):
    crunch(N)
print(f"sequential: {time.time()-start:.2f}s")

start = time.time()                 # "parallel": 4 threads
threads = [Thread(target=crunch, args=(N,)) for _ in range(4)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f"4 threads:  {time.time()-start:.2f}s")
```

1. Compare the two times. Where did your 4x speedup go?
2. Now swap `crunch` for an I/O-style wait (`time.sleep(1)`) and rerun both
   versions. Why do threads suddenly give ~4x?
3. State the rule a DE uses to choose threads vs multiprocessing.

<details><summary>Answer</summary>

1. The thread version is ~the same (or slower) than sequential. The **GIL**: only
   one thread executes Python bytecode at a time, so CPU-bound threads take turns
   on one core — plus switching overhead.
2. `time.sleep` (like network/disk waits) **releases the GIL** while waiting, so
   all 4 waits overlap → ~1s total instead of ~4s. Waiting-heavy work overlaps;
   computing-heavy work serializes.
3. **CPU-bound pure Python → multiprocessing (or push into NumPy/Spark). I/O-bound
   → threads or async.** Match the tool to the bottleneck.
</details>

---

## 🔴 Hard — the disguised loop (interview classic)

A teammate processes OrderIQ with pandas but it's still slow:

```python
import pandas as pd
df = pd.read_csv("datasets/data/orders.csv")

# their code:
df["price_band"] = df.apply(
    lambda row: "high" if (row["amount"] or 0) > 1000 else "low", axis=1
)
```

1. pandas is C under the hood — so why is this still the slow path? Name what
   `.apply(..., axis=1)` really is.
2. Rewrite it vectorized (hint: `np.where` + `fillna`). Time both on your data.
3. **Break-it:** your vectorized version and their apply version may disagree on
   rows where `amount` is missing. Check whether they do, and explain why NULL
   handling must be an *explicit decision* in both versions.
4. Explain-back (say it out loud, plain words): why does "pandas is written in C"
   not save you the moment you hand it a Python lambda per row?

<details><summary>Answer</summary>

1. `.apply(axis=1)` calls a **Python** lambda once per row — it's a disguised
   Python for-loop. The C engine is reduced to invoking slow interpreted code N
   times, paying all three taxes per row.
2. ```python
   import numpy as np
   df["price_band"] = np.where(df["amount"].fillna(0) > 1000, "high", "low")
   ```
   Typically 10–100x faster — the comparison and selection run entirely in C.
3. In the apply version, `row["amount"] or 0` treats NaN *and legitimate 0* as 0
   (the falsy trap from Topic 4 of control flow!). `fillna(0)` treats only missing
   as 0. On a real ₹0 order both give "low" here, but with a different rule (e.g.
   `>= 0`) they'd diverge. Missing-value handling is a business rule — decide it
   explicitly, never let `or` decide silently.
4. Model answer: "C is only fast while the loop stays *inside* C. A per-row Python
   lambda forces control back into the interpreter for every row — so the loop is
   Python again, just wearing a pandas costume."
</details>

---

### ✅ Mastery check for Topic 1

Without notes:

- explain source → bytecode → interpreter loop, and what `__pycache__` caches,
- name the three per-operation taxes that make pure Python slow,
- explain why vectorized NumPy/pandas escapes them (and prove it with a timing),
- state when threads help (I/O-bound) vs don't (CPU-bound, GIL) — and what to use instead.

Passed? → [Topic 2 — Variables, Memory & the Mutable/Immutable Trap](../topic-2-variables-memory-mutability/).

*Back to the [lesson](./README.md).*
