# Practice — Control Flow & Comprehensions

> Paste the dataset into a `.ipynb` cell, run it, then solve each problem yourself BEFORE revealing.
> Prove you own it: solve 🟡+🔴 without looking → explain WHY → fix the break-it → paste to Claude for grading.
> Tiers: 🟢 Warm-up · 🟡 Core · 🔴 Stretch.

---

## 📦 The dataset (run first — includes deliberate messiness)

```python
orders = [
    {"id": 1, "customer_id": 101, "city": "Mumbai",    "amount": 1200.0, "status": "delivered"},
    {"id": 2, "customer_id": 102, "city": "Delhi",     "amount": 300.0,  "status": "delivered"},
    {"id": 3, "customer_id": 101, "city": "Mumbai",    "amount": 0.0,     "status": "delivered"},   # free order (real 0)
    {"id": 4, "customer_id": 103, "city": "Bangalore", "amount": 2500.0, "status": "cancelled"},
    {"id": 5, "customer_id": 102, "city": None,        "amount": 1800.0, "status": "delivered"},    # null city
    {"id": 6, "customer_id": 104, "city": "Mumbai",    "amount": None,   "status": "delivered"},    # null amount
    {"id": 7, "customer_id": 101, "city": "Mumbai",    "amount": -50.0,  "status": "returned"},     # bad negative
    {"id": 8, "customer_id": 105, "city": "Bangalore", "amount": 150.0,  "status": "delivered"},
]
vip_customer_ids = {101, 103}
```

---

## 🟢 Warm-up 1 — Delivered order IDs (comprehension)
**Task:** list of `id`s whose `status == "delivered"`, in one comprehension.
**Acceptance:** `[1, 2, 3, 5, 6, 8]`.

<details><summary>▶ Solution + why</summary>

```python
delivered = [o["id"] for o in orders if o["status"] == "delivered"]
print(delivered)   # [1, 2, 3, 5, 6, 8]
```
Anatomy: keep `o["id"]` · loop `for o in orders` · filter `if status == "delivered"`.
**Common mistake:** using `=` instead of `==` in the filter → SyntaxError.
</details>

---

## 🟢 Warm-up 2 — Fill missing cities
**Task:** build a list of cities where any `None`/empty becomes `"UNKNOWN"`.
**Acceptance:** order 5's city → `"UNKNOWN"`, the rest unchanged.

<details><summary>▶ Solution + why</summary>

```python
cities = [(o["city"] or "UNKNOWN") for o in orders]
print(cities)   # ['Mumbai','Delhi','Mumbai','Bangalore','UNKNOWN','Mumbai','Mumbai','Bangalore']
```
`o["city"] or "UNKNOWN"` → falls back when city is `None`/`""`. This is safe here because *any* empty city should become UNKNOWN.
**🧨 Break-it:** this `or` trick is safe for strings but NOT for numbers where 0 is valid — see Core 2.
</details>

---

## 🟡 Core 1 — Safe total revenue (skip missing & negative)
**Scenario:** Finance wants total revenue, ignoring bad rows (missing or negative amounts). A real `0.0` order **counts** (it's valid, just free).
**Task:** sum `amount`, skipping `None` and negatives, keeping `0.0`.
**Acceptance:** `1200 + 300 + 0 + 2500 + 1800 + 150 = 5950.0` (order 6 None skipped, order 7 -50 skipped).

<details><summary>▶ Solution + why + break-it</summary>

```python
total = 0.0
for o in orders:
    amt = o["amount"]
    if amt is None or amt < 0:      # None FIRST (short-circuit avoids None < 0 crash)
        continue
    total += amt
print(total)   # 5950.0
```
**Why order matters:** test `amt is None` before `amt < 0`. `or` short-circuits, so if `amt is None` is True, Python never evaluates `amt < 0` (which would `TypeError`).
**Common mistake:** `if not amt: continue` — this would wrongly skip the valid `0.0` order (0 is falsy!). Must check `is None` explicitly.
**🧨 Break-it:** as a one-liner generator: `sum(o["amount"] for o in orders if o["amount"] is not None and o["amount"] >= 0)` → same 5950.0, memory-light.
</details>

---

## 🟡 Core 2 — Label each order (bucket with a helper)
**Scenario:** tag orders: `amount is None` → "missing", `<= 0` → "invalid", `<= 500` → "low", `<= 2000` → "medium", else "high".
**Task:** produce a list of `(id, label)`. Use a testable helper + a simple comprehension.
**Acceptance:** e.g. `(1,'medium'),(3,'invalid'),(6,'missing'),(7,'invalid'),(4,'high')`.

<details><summary>▶ Solution + why</summary>

```python
def bucket(amount):
    if amount is None:  return "missing"
    if amount <= 0:     return "invalid"
    if amount <= 500:   return "low"
    if amount <= 2000:  return "medium"
    return "high"

labels = [(o["id"], bucket(o["amount"])) for o in orders]
print(labels)
# [(1,'medium'),(2,'low'),(3,'invalid'),(4,'high'),(5,'medium'),(6,'missing'),(7,'invalid'),(8,'low')]
```
**Why a helper, not a nested ternary in the comprehension:** the branching is testable, readable, and easy to extend. Cramming 5-way logic into one comprehension line is "clever" but hurts the next reader. Comprehension holds a *simple* expression (`bucket(...)`).
**Interview tag:** ⭐ categorize/bucket — extracting logic into a function signals production maturity.
</details>

---

## 🔴 Stretch — VIP revenue by city, efficiently
**Scenario:** total **valid** revenue (skip None/negative) from **VIP** customers, broken down by city, on data assumed too large for memory.
**Task:** produce `{city → vip_revenue}`; use a set for VIP lookup, handle nulls, keep it stream-friendly.
**Acceptance:** VIPs are {101,103}. Their valid orders: id1 Mumbai 1200, id3 Mumbai 0.0, id4 Bangalore 2500 (cancelled still counts — we're not filtering status here), id7 -50 skipped. → `{'Mumbai': 1200.0, 'Bangalore': 2500.0}`.

<details><summary>▶ Solution + why + scale</summary>

🗣️ **Plain words:** loop once, skip non-VIP (O(1) set check), skip bad amounts, add to a per-city running total.

```python
from collections import defaultdict

vip_rev = defaultdict(float)
for o in orders:                                  # a stream, one row at a time
    if o["customer_id"] not in vip_customer_ids:  # O(1) set membership
        continue
    amt = o["amount"]
    if amt is None or amt < 0:                     # skip bad
        continue
    city = o["city"] or "UNKNOWN"
    vip_rev[city] += amt

print(dict(vip_rev))   # {'Mumbai': 1200.0, 'Bangalore': 2500.0}
```
**Why each choice:**
- **`set` for `vip_customer_ids`** → O(1) membership (a list would be O(n) per row → slow at scale).
- **`continue` early** → skips non-VIP/bad rows before doing work (clean control flow).
- **`defaultdict(float)`** → per-city accumulation without boilerplate (comprehensions can't accumulate).
- **loop over a stream** → constant memory; never build a big list.

**🧨 Scale note:** for genuinely huge data, the most professional answer is push it to **DuckDB/SQL** (`SELECT city, SUM(amount) ... WHERE customer_id IN (...) AND amount >= 0 GROUP BY city`) or **Spark**. Expressing it cleanly in Python proves you understand *why* those engines work.

**Multiple approaches:** a generator + `Counter`-style sum also works, but per-key accumulation is clearest with `defaultdict`.
</details>

---

### ✅ Done?
Tell Claude **"done with Control Flow practice"**, paste a solution to grade, or **"too easy/too hard"** to recalibrate. Any 🔴 you couldn't crack → we revisit in the Phase-0 revision.
