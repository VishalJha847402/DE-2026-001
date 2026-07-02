# Practice — Data Structures Deep (list · dict · set · tuple + collections)

> **How to use:** paste the dataset below into a `.ipynb` cell and run it. Solve each problem yourself FIRST, then open the ▶ solution.
> **Prove you own it:** solve 🟡 + 🔴 without looking → explain WHY → fix the break-it → paste your solution to Claude for grading.
> Tiers: 🟢 Warm-up (5–10 min) · 🟡 Core (20–30 min) · 🔴 Stretch (30–60 min).

---

## 📦 The dataset (run this first — small e-commerce data, no DuckDB needed)

```python
orders = [
    {"id": 1, "customer_id": 101, "city": "Mumbai",    "category": "Electronics", "amount": 1200.0, "product_id": "P1"},
    {"id": 2, "customer_id": 102, "city": "Delhi",     "category": "Books",       "amount": 300.0,  "product_id": "P2"},
    {"id": 3, "customer_id": 101, "city": "Mumbai",    "category": "Books",       "amount": 450.0,  "product_id": "P3"},
    {"id": 4, "customer_id": 103, "city": "Bangalore", "category": "Electronics", "amount": 2500.0, "product_id": "P1"},
    {"id": 5, "customer_id": 102, "city": "Delhi",     "category": "Electronics", "amount": 1800.0, "product_id": "P4"},
    {"id": 6, "customer_id": 104, "city": "Mumbai",    "category": "Books",       "amount": 200.0,  "product_id": "P2"},
    {"id": 7, "customer_id": 101, "city": "Mumbai",    "category": "Electronics", "amount": 999.0,  "product_id": "P1"},
    {"id": 8, "customer_id": 105, "city": "Bangalore", "category": "Books",       "amount": 150.0,  "product_id": "P3"},
]
valid_product_ids = ["P1", "P2", "P3", "P4", "P5"]   # the catalog
```

---

## 🟢 Warm-up 1 — Orders per city

**Scenario:** The city ops team asks: *"How many orders did each city get?"*
**Task:** Produce a dict/Counter of `city → order count`.
**Acceptance criteria:** output equals `{'Mumbai': 4, 'Delhi': 2, 'Bangalore': 2}` (any order).
**Interview tag:** ⭐ classic "count by group".

<details>
<summary>▶ Solution + why</summary>

```python
from collections import Counter
city_counts = Counter(o["city"] for o in orders)
print(city_counts)   # Counter({'Mumbai': 4, 'Delhi': 2, 'Bangalore': 2})
```

**Why:** `Counter` counts occurrences in one line. **Alternative** (no import):
```python
counts = {}
for o in orders:
    counts[o["city"]] = counts.get(o["city"], 0) + 1
```
**Common mistake:** using `counts[o["city"]] += 1` without a default → `KeyError` on the first time a city appears. Use `.get(k, 0)` or `defaultdict(int)`.

**🧨 Break-it:** what if some orders have `"city": None` or `"city": "mumbai"` (lowercase)? → `None` becomes its own bucket, and `"mumbai"` ≠ `"Mumbai"` (case-sensitive) → split counts. Fix: clean/normalize (`(o["city"] or "UNKNOWN").title()`) before counting. This is a real data-quality trap.

</details>

---

## 🟢 Warm-up 2 — Unique customers

**Scenario:** *"How many distinct customers do we have?"*
**Task:** Return the set of unique `customer_id`s and its size.
**Acceptance criteria:** 5 unique customers → `{101, 102, 103, 104, 105}`, count `5`.

<details>
<summary>▶ Solution + why</summary>

```python
unique_customers = {o["customer_id"] for o in orders}   # set comprehension
print(unique_customers, len(unique_customers))          # {101,102,103,104,105} 5
```

**Why:** a `set` auto-dedupes; `len()` gives the distinct count. **Common mistake:** building a list then eyeballing duplicates — `len([...])` would give **8** (total orders), not 5 (distinct customers). The structure choice *is* the answer.

</details>

---

## 🟡 Core 1 — Revenue per city, then the top city

**Scenario:** Finance wants *total revenue per city* and *the single highest-revenue city*.
**Task:** Build `city → total revenue` with `defaultdict`, then find the top city.
**Acceptance criteria:** Mumbai `2849.0`, Delhi `2100.0`, Bangalore `2650.0`; top = **Mumbai**.
**Interview tag:** ⭐ "aggregate by group + find max".

<details>
<summary>▶ Solution + why + alternatives</summary>

```python
from collections import defaultdict

revenue = defaultdict(float)
for o in orders:
    revenue[o["city"]] += o["amount"]

print(dict(revenue))                        # {'Mumbai': 2849.0, 'Delhi': 2100.0, 'Bangalore': 2650.0}

top_city = max(revenue, key=revenue.get)    # key with the largest value
print(top_city, revenue[top_city])          # Mumbai 2849.0
```

**Why `defaultdict(float)`:** the first `+=` on a new city starts at 0.0 — no boilerplate, no `KeyError`.

**Alternative approaches (know the trade-offs):**
- Plain dict: `revenue[c] = revenue.get(c, 0) + amt` — same result, one extra call per row.
- `Counter`: `Counter()` can sum too — `c = Counter(); for o in orders: c[o["city"]] += o["amount"]` then `c.most_common(1)` gives the top directly.

**Common mistake:** `max(revenue)` *without* `key=revenue.get` returns the city with the largest **name** alphabetically (`'Mumbai'` by string), not the largest revenue. Always pass `key=`.

**🧨 Break-it:** two cities tie for top revenue — `max` returns just the *first* one it finds. If you need *all* top cities, compute `mx = max(revenue.values())` then `[c for c,v in revenue.items() if v == mx]`.

</details>

---

## 🟡 Core 2 — Revenue by (city, category) using a tuple key

**Scenario:** *"Break revenue down by city AND category together."*
**Task:** Use a **tuple** `(city, category)` as the dict key to sum revenue for each combination.
**Acceptance criteria:** includes `('Mumbai','Electronics'): 2199.0`, `('Mumbai','Books'): 650.0`, `('Delhi','Electronics'): 1800.0`, etc.
**Interview tag:** ⭐ composite-key grouping (mirrors SQL `GROUP BY city, category`).

<details>
<summary>▶ Solution + why</summary>

```python
from collections import defaultdict

rev = defaultdict(float)
for o in orders:
    rev[(o["city"], o["category"])] += o["amount"]     # tuple key = group by 2 fields

for key, total in rev.items():
    print(key, total)
# ('Mumbai', 'Electronics') 2199.0
# ('Delhi', 'Books') 300.0
# ('Mumbai', 'Books') 650.0
# ('Bangalore', 'Electronics') 2500.0
# ('Delhi', 'Electronics') 1800.0
# ('Bangalore', 'Books') 150.0
```

**Why the tuple:** you want to group by *two* fields at once — a tuple `(city, category)` is a single hashable key that captures both. This is the Python version of SQL's `GROUP BY city, category`.

**Common mistake:** using a **list** `[city, category]` as the key → `TypeError: unhashable type: 'list'`. Keys must be immutable → use a tuple.

**🧨 Break-it:** what if you later want "revenue per city" from this? You'd sum across categories: `defaultdict` again keyed on `key[0]`. Point: the grain of your key decides what you can answer — pick it deliberately (a Data Modeling idea you'll meet again).

</details>

---

## 🔴 Stretch — Flag invalid orders at scale (the O(1) lesson)

**Scenario:** Before loading, you must flag any order whose `product_id` is **not** in the catalog. Today it's 8 orders; in production it's **50M orders** against a **2M-product** catalog, and the naive version is too slow.
**Task:**
1. Return the list of order IDs with an invalid `product_id` (here: none are invalid — all P1–P4 exist; add a bad one to test).
2. Make it **efficient at 50M scale** and explain the structure choice.
3. Handle the break-it cases.
**Acceptance criteria:** with the given data, 0 invalid. Add `{"id": 9, ..., "product_id": "P99"}` → returns `[9]`.
**Interview tag:** ⭐⭐ membership-at-scale + O(1) vs O(n) (a very common senior filter).

<details>
<summary>▶ Solution + why + scale reasoning</summary>

🗣️ **In plain words first:** turn the catalog into a **set** once, then each "is this product valid?" check is instant. Never check membership against a list in a big loop.

```python
catalog = set(valid_product_ids)          # O(1) membership from here on

invalid = [o["id"] for o in orders if o["product_id"] not in catalog]
print(invalid)                            # []  (all P1–P4 are valid)

# test it:
orders_test = orders + [{"id": 9, "customer_id": 106, "city": "Pune",
                         "category": "Books", "amount": 100.0, "product_id": "P99"}]
invalid = [o["id"] for o in orders_test if o["product_id"] not in catalog]
print(invalid)                            # [9]
```

**Why a `set`, not the `list`:**
- `"P99" not in valid_product_ids` (a **list**) scans up to 2M items **every time** → O(n). Over 50M orders that's up to 10¹⁴ comparisons → minutes/hours.
- `"P99" not in catalog` (a **set**) is one hash jump → **O(1)**. 50M checks finish in seconds. **Same result, ~1000x faster.**

**Multiple approaches / trade-offs:**
- `set` membership (above) — best for "valid or not".
- If you also need the product's *details*, use a **dict** `product_id → product` and check `.get(pid)` (slightly more memory).
- `pandas`/Spark later: `df[~df.product_id.isin(catalog)]` / `df.join(...)` — same idea, distributed.

**🧨 Break-it (what breaks at 50M):**
1. **Type mismatch** — catalog has `"P1"` (str) but an order has `1` (int) or `" P1 "` (whitespace) → falsely flagged invalid. Fix: normalize types/trim before comparing (data quality).
2. **Memory** — the 2M-id set is fine (~tens of MB); but if orders don't fit in RAM, **stream/chunk** them or push to Spark/SQL — you never need all 50M orders in memory at once for this check.
3. **Nulls** — `product_id` is `None` → not in catalog → flagged. Decide: is null "invalid" or "route to dead-letter"? (ties to the practice-system "break-it" + dead-letter idea.)

</details>

---

### ✅ When you've done this set
Tell Claude: **"done with Data Structures practice"** (and paste any solution you want graded), or **"too easy / too hard"** so the next set is recalibrated. Any 🔴 you couldn't crack → we revisit it in the Phase-0 revision.
