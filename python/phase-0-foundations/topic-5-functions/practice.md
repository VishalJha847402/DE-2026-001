# Practice — Topic 5: Functions

> Rule: **output ≠ proof.** After each problem, run the **Break-it** variant and
> explain *why* the output changed. If you can't explain it, you don't own it yet.

Paste this dataset at the top of a new cell/file. It has real traps: a `None`
city, a `None` amount, a genuine `0` free order, a negative amount, and a messy
comma-string amount.

```python
orders = [
    {"id": 1, "city": " Pune ",  "amount": "1,299", "status": "delivered"},
    {"id": 2, "city": None,       "amount": None,    "status": "cancelled"},
    {"id": 3, "city": "mumbai",   "amount": 0,       "status": "delivered"},  # real free order
    {"id": 4, "city": "Delhi",    "amount": -50,     "status": "delivered"},  # bad data
    {"id": 5, "city": "bengaluru","amount": "899",   "status": "delivered"},
    {"id": 6, "city": "Pune",     "amount": "2500",  "status": "returned"},
]
```

---

## 🟢 Easy 1 — `clean_amount(raw) -> float`

Write a function that turns any `amount` above into a clean, **non-negative**
float. `None`, empty, unparseable, or negative → `0.0`. `"1,299"` → `1299.0`.

**Break-it:** call `clean_amount("₹899")`. Does it return `0.0` or crash? Explain,
then make it survive (strip non-digit currency symbols).

<details><summary>Solution</summary>

```python
def clean_amount(raw) -> float:
    if raw is None:
        return 0.0
    try:
        v = float(str(raw).replace(",", "").replace("₹", "").strip())
    except ValueError:
        return 0.0
    return v if v >= 0 else 0.0

print([clean_amount(o["amount"]) for o in orders])
# [1299.0, 0.0, 0.0, 0.0, 899.0, 2500.0]
```
Note `id=3` (real 0) and `id=4` (negative) both become `0.0` here — same output,
different reason. That's the trap the next problem separates.
</details>

---

## 🟢 Easy 2 — default argument done right

Write `normalize_city(city, fallback="UNKNOWN")` that trims + title-cases the
city, and returns `fallback` when the city is `None` or blank.

**Break-it:** now write a *wrong* version `def tag(city, seen=[])` that appends
each city to `seen` and returns it. Call it 3 times. Explain why old cities
persist, then fix it with `None`.

<details><summary>Solution</summary>

```python
def normalize_city(city, fallback="UNKNOWN"):
    if city is None or not city.strip():
        return fallback
    return city.strip().title()

print([normalize_city(o["city"]) for o in orders])
# ['Pune', 'UNKNOWN', 'Mumbai', 'Delhi', 'Bengaluru', 'Pune']
```
The mutable-default fix:
```python
def tag(city, seen=None):
    if seen is None:
        seen = []
    seen.append(city)
    return seen
```
</details>

---

## 🟡 Medium 1 — `*args` aggregator

Write `total_revenue(*amounts)` that accepts **any number** of already-cleaned
amounts and returns their sum. Then call it two ways: (a) pass 3 numbers directly,
(b) unpack the cleaned list from Easy 1 with `*`.

**Break-it:** what happens if you call `total_revenue()` with nothing? Should it
crash or return `0`? Make sure it returns `0`.

<details><summary>Solution</summary>

```python
def total_revenue(*amounts):
    return sum(amounts)          # sum(()) == 0, so empty call is safe

cleaned = [clean_amount(o["amount"]) for o in orders]
print(total_revenue(100, 200, 50))   # 350
print(total_revenue(*cleaned))       # 4698.0
print(total_revenue())               # 0
```
</details>

---

## 🟡 Medium 2 — closure factory

Write `min_amount_filter(threshold)` that **returns a function**. The returned
function takes the `orders` list and returns only orders whose cleaned amount is
`>= threshold`. Build two filters: `big = min_amount_filter(1000)` and
`any_paid = min_amount_filter(1)`.

**Break-it:** after creating `big`, reassign `threshold = 0` in the outer scope
(new variable). Does `big` change its behaviour? Explain what it actually
remembers.

<details><summary>Solution</summary>

```python
def min_amount_filter(threshold):
    def apply(rows):
        return [r for r in rows if clean_amount(r["amount"]) >= threshold]
    return apply

big = min_amount_filter(1000)
any_paid = min_amount_filter(1)

print([o["id"] for o in big(orders)])       # [1, 6]
print([o["id"] for o in any_paid(orders)])  # [1, 5, 6]
```
`big` captured the value `1000` at creation. A later, unrelated `threshold = 0`
doesn't touch it — the closure holds its own captured binding.
</details>

---

## 🔴 Hard — build the mini-pipeline from functions

Wire everything into one pipeline. Write **four** functions and compose them:

1. `clean(row) -> dict` — normalize `city` (Easy 2 rule) and add a
   `clean_amount` float field.
2. `is_countable(row) -> bool` — keep a row only if `status == "delivered"`
   **and** cleaned amount `> 0`. (So the real free order `id=3` is delivered but
   `0` → excluded from revenue; `id=4` negative → excluded; `id=6` returned →
   excluded.)
3. `revenue_by_city(rows) -> dict` — sum cleaned amounts per city, **only** for
   countable rows. Use a plain dict with `.get(...)` or `defaultdict`.
4. `run(rows, **opts) -> dict` — the orchestrator. Accept `**opts` and support
   `opts["min_amount"]` (default `0`) to additionally drop rows below a floor.

Expected (with no `min_amount`):

```python
print(run(orders))
# {'Pune': 1299.0, 'Bengaluru': 899.0}
```

**Break-it (do all three):**
- (a) Call `run(orders, min_amount=1000)`. Which city disappears and why?
- (b) Temporarily make `is_countable` use `>=` instead of `>`. Does `Mumbai`
  (the real `0` order) appear? Is that correct business logic? (Tie it back to
  BUSINESS_RULES thinking: a `0` "free" order is real but contributes `0` revenue.)
- (c) Break `clean` by removing its `return`. Now `run` crashes or gives wrong
  output — explain exactly where the `None` propagates.

<details><summary>Solution</summary>

```python
from collections import defaultdict

def clean(row):
    row = dict(row)                      # copy — don't mutate caller's data
    row["city"] = normalize_city(row["city"])
    row["amt"] = clean_amount(row["amount"])
    return row

def is_countable(row):
    return row["status"] == "delivered" and row["amt"] > 0

def revenue_by_city(rows):
    out = defaultdict(float)
    for r in rows:
        if is_countable(r):
            out[r["city"]] += r["amt"]
    return dict(out)

def run(rows, **opts):
    floor = opts.get("min_amount", 0)
    cleaned = [clean(r) for r in rows]
    kept = [r for r in cleaned if r["amt"] >= floor]
    return revenue_by_city(kept)

print(run(orders))                    # {'Pune': 1299.0, 'Bengaluru': 899.0}
print(run(orders, min_amount=1000))   # {'Pune': 1299.0}
```

**Break-it answers:**
- (a) `min_amount=1000` drops the `899` Bengaluru order → only Pune remains.
- (b) With `>=`, `id=3` Mumbai (delivered, `0`) becomes countable and shows
  `{'Mumbai': 0.0}`. It's *not wrong* to count it as a placed/free order, but it
  adds `0` revenue — this is exactly why revenue metrics filter `amount > 0`
  while *count* metrics might not. Definitions matter.
- (c) Remove `return` from `clean` → the list comp `[clean(r) ...]` becomes
  `[None, None, ...]`. Then `r["amt"]` in `run` raises
  `TypeError: 'NoneType' object is not subscriptable`. The bug's *symptom* is far
  from its *cause* — the classic "forgot to return" failure.
</details>

---

### ✅ Mastery gate for Phase 0

You're ready for the Phase-0 revision + challenge when you can, without looking:

- explain `return` vs `print` and why "no return → `None`" bites,
- spot and fix a mutable default argument,
- read `*args`/`**kwargs` and unpack with `*`/`**`,
- trace an LEGB lookup and say why `global` is a smell,
- describe what a closure "remembers,"
- and **compose 3–4 small functions into a pipeline** — because that is the job.

*Back to the [lesson](./README.md) · Next: Phase-0 Revision + Challenge.*
