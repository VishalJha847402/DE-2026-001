# Phase 0 — Revision + Challenge (all 5 topics)

> **Purpose:** fight the forgetting curve and expose hidden holes *before* Phase 1
> builds on top. Do this in one sitting, from memory, no scrolling back to lessons.
>
> **Covers:** Topic 1 How Python Runs · Topic 2 Variables & Mutability · Topic 3
> Data Structures · Topic 4 Control Flow & Comprehensions · Topic 5 Functions.
>
> **How to use the 4 layers:** Layer 1 warms recall (fast). Layer 2 checks you
> understand *why*. Layer 3 mixes topics (interleaving = real retention). Layer 4
> is the Boss Fight — one program that uses **all five topics at once**.

---

## Layer 1 — ⚡ Flash Recall (answer out loud, 60 seconds each)

No code. Just say the answer. If you hesitate > 5 sec, mark it "review."

1. Is Python compiled or interpreted? What is bytecode? (T1)
2. What does the GIL stop, and what does it *not* stop? (T1)
3. `a = [1,2]; b = a; b.append(3)` — what is `a`? Why? (T2)
4. Name 3 immutable types and 3 mutable types. (T2)
5. `x = 256; y = 256; x is y` → `True` or `False`? Why? (T2 — small int cache)
6. When do you pick a **set** over a **list**? (T3)
7. What's the average lookup cost of `key in dict` vs `item in list`? (T3)
8. `[x for x in data if x]` — what values does `if x` silently drop? (T4)
9. `x or "default"` — what's the bug when `x` is `0` or `""`? (T4)
10. A function with no `return` gives back what? (T5)
11. Why is `def f(cart=[])` dangerous? (T5)
12. What does a **closure** remember? (T5)

<details><summary>Flash answers</summary>

1. Interpreted (to bytecode, then run by the CPython VM). Bytecode = the low-level
   instructions Python compiles your source into (`.pyc`).
2. Stops two Python **threads** running Python bytecode *at the same time*. Does
   NOT stop multiprocessing, and doesn't block I/O-bound concurrency.
3. `[1, 2, 3]`. `b = a` copies the *reference*, not the list — both point to the
   same object.
4. Immutable: `int, str, tuple, float, bool, frozenset`. Mutable: `list, dict, set`.
5. `True` — CPython caches small ints (−5 to 256), so both names point to the same
   cached object. (Don't rely on this; use `==`.)
6. Membership tests / dedup / set math (union/intersection) — O(1) lookup, no dupes.
7. dict/set: **O(1)** average. list: **O(n)**. Huge at scale.
8. Falsy values: `0`, `0.0`, `""`, `None`, `[]`, `{}`, `False`.
9. `0` and `""` are falsy → `or` replaces a *real* value with the default. Use
   `x if x is not None else "default"`.
10. `None`.
11. The default list is made once at definition and shared across all default
    calls — state leaks. Use `None` + create inside.
12. Variables captured from its enclosing function, kept alive after that function
    returned.
</details>

---

## Layer 2 — 🧠 Concept Gate (explain WHY in 2–3 plain sentences)

Write/say these in your own words. If you can't, that topic isn't owned yet.

- **Why** does `b = a` on a list surprise beginners but not on an int? (Tie T2
  mutability to references.)
- **Why** is a dict lookup O(1)? (Say the word *hashing*.)
- **Why** does a generator expression `(x for x in big)` save memory vs a list
  comprehension `[x for x in big]`? (T4 → previews Phase 1.)
- **Why** do DEs avoid `global` and prefer pass-in / return-out? (T5, idempotency.)

<details><summary>Model answers</summary>

- A list is mutable and passed by reference, so two names can point to the *same*
  changeable object — mutating through one is visible through the other. Ints are
  immutable: `b = b + 1` makes a *new* int, so `a` never changes.
- A dict stores keys in a hash table: it computes a hash of the key and jumps
  straight to the slot, instead of scanning every entry. That's why size barely
  affects lookup speed.
- The list comp builds **all** results in memory at once. The generator yields
  **one at a time**, holding a single item — so it handles data far bigger than RAM.
- `global` hides shared mutable state, so a task that reruns (Airflow retries!)
  can behave differently the second time. Pure functions that take inputs and
  return outputs are repeatable and testable.
</details>

---

## Layer 3 — 🔀 Interleaved Drills (mix topics — this is where retention is built)

Paste this dataset, then solve each drill. Each drill deliberately combines
2+ topics.

```python
orders = [
    {"id": 1, "city": " Pune ",   "amount": "1,299", "status": "delivered"},
    {"id": 2, "city": None,        "amount": None,    "status": "cancelled"},
    {"id": 3, "city": "mumbai",    "amount": 0,       "status": "delivered"},  # real free order
    {"id": 4, "city": "Delhi",     "amount": -50,     "status": "delivered"},  # bad data
    {"id": 5, "city": "bengaluru", "amount": "899",   "status": "delivered"},
    {"id": 6, "city": "Pune",      "amount": "2500",  "status": "returned"},
    {"id": 7, "city": "MUMBAI",    "amount": "1500",  "status": "delivered"},
]
```

**Drill A** *(T3 set + T4 comprehension)* — get the **distinct** cities that have
at least one *delivered* order, normalized to Title case. Expected:
`{'Pune', 'Mumbai', 'Bengaluru', 'Delhi'}`.

**Drill B** *(T4 truthiness trap + T5 function)* — write `safe_amount(raw)` that
returns a non-negative float; `None`/blank/negative/unparseable → `0.0`, but a
real `0` stays `0.0`. Then build a list of `(id, safe_amount)` for all rows.

**Drill C** *(T3 dict-as-accumulator + T4 loop)* — count how many orders each
`status` has. Expected: `{'delivered': 4, 'cancelled': 1, 'returned': 1}`... wait,
recount from the data yourself — that's the point.

**Drill D** *(T5 closure + T4 filter)* — write `status_filter(status)` that
returns a function selecting rows of that status. Use it to get delivered rows.

<details><summary>Solutions</summary>

```python
# A
cities = {o["city"].strip().title()
          for o in orders
          if o["status"] == "delivered" and o["city"]}
print(cities)   # {'Pune', 'Mumbai', 'Bengaluru', 'Delhi'}

# B
def safe_amount(raw):
    if raw is None:
        return 0.0
    try:
        v = float(str(raw).replace(",", "").strip())
    except ValueError:
        return 0.0
    return v if v >= 0 else 0.0

print([(o["id"], safe_amount(o["amount"])) for o in orders])
# [(1,1299.0),(2,0.0),(3,0.0),(4,0.0),(5,899.0),(6,2500.0),(7,1500.0)]

# C
counts = {}
for o in orders:
    counts[o["status"]] = counts.get(o["status"], 0) + 1
print(counts)   # {'delivered': 4, 'cancelled': 1, 'returned': 2}
# ^ note: id=6 returned AND... recount: delivered = 1,3,4,5,7 = 5; returned = 6 = 1
# Correct: {'delivered': 5, 'cancelled': 1, 'returned': 1}. Did you trust the prompt
# or the data? Always trust the data.

# D
def status_filter(status):
    def apply(rows):
        return [r for r in rows if r["status"] == status]
    return apply

delivered = status_filter("delivered")
print([o["id"] for o in delivered(orders)])   # [1, 3, 4, 5, 7]
```
**Drill C is a trap on purpose** — the prompt's expected answer was wrong. A DE
verifies against the data, never against a claimed number. That instinct is worth
more than the syntax.
</details>

---

## Layer 4 — 🐉 Boss Fight (all 5 topics in one program)

**Scenario.** You're the DE. Raw orders arrive as messy dicts (above). Build a
single clean report. Requirements — each maps to a Phase-0 topic:

1. **(T5 functions)** Structure the whole thing as composed functions:
   `clean → keep → summarize`. No giant blob.
2. **(T2 mutability)** `clean` must **not mutate** the caller's original `orders`
   list/dicts. Prove it (print original after running).
3. **(T4 control flow / truthiness)** Revenue counts an order only if it's
   `delivered` **and** `amount > 0`. The real `0` free order counts as a *delivered
   order* but adds `0` revenue. Handle `None`/negative/comma-string safely.
4. **(T3 data structures)** Return a summary with: `distinct_cities` (a set),
   `orders_by_status` (a dict), and `revenue_by_city` (a dict, delivered+paid only).
5. **(T5 `**kwargs`)** `summarize(rows, **opts)` supports `opts["min_amount"]`
   (default `0`) to drop orders below a floor before computing revenue.

**Target output** (no `min_amount`):

```python
{
  'distinct_cities': {'Pune', 'Mumbai', 'Bengaluru', 'Delhi'},
  'orders_by_status': {'delivered': 5, 'cancelled': 1, 'returned': 1},
  'revenue_by_city': {'Pune': 1299.0, 'Bengaluru': 899.0, 'Mumbai': 1500.0}
}
```

Try it fully yourself before opening the solution. Then run the **Break-its**.

<details><summary>Reference solution</summary>

```python
from collections import defaultdict

def safe_amount(raw):
    if raw is None:
        return 0.0
    try:
        v = float(str(raw).replace(",", "").strip())
    except ValueError:
        return 0.0
    return v if v >= 0 else 0.0

def clean(row):
    row = dict(row)                       # T2: copy — never mutate caller's dict
    row["city"] = (row.get("city") or "UNKNOWN").strip().title()
    row["amt"]  = safe_amount(row.get("amount"))
    return row

def is_paid_delivered(row):
    return row["status"] == "delivered" and row["amt"] > 0

def summarize(rows, **opts):
    floor = opts.get("min_amount", 0)
    cleaned = [clean(r) for r in rows]                     # T4 comprehension
    distinct_cities = {r["city"] for r in cleaned          # T3 set
                       if r["status"] == "delivered" and r["city"] != "UNKNOWN"}
    by_status = defaultdict(int)                            # T3 dict accumulator
    for r in cleaned:
        by_status[r["status"]] += 1
    revenue = defaultdict(float)
    for r in cleaned:
        if is_paid_delivered(r) and r["amt"] >= floor:
            revenue[r["city"]] += r["amt"]
    return {
        "distinct_cities": distinct_cities,
        "orders_by_status": dict(by_status),
        "revenue_by_city": dict(revenue),
    }

report = summarize(orders)
from pprint import pprint
pprint(report)
print("original untouched:", orders[0]["city"] == " Pune ")   # True → not mutated
```
</details>

**Break-its (do all three, explain each):**

- **(a)** Call `summarize(orders, min_amount=1000)`. Which city vanishes? Why?
- **(b)** In `clean`, change `dict(row)` to just `row`. Now run `summarize` twice
  and print `orders[0]`. What broke, and how does this connect to Topic 2?
- **(c)** Change `is_paid_delivered` to use `>=` instead of `>`. Does `Mumbai`'s
  `id=3` free order appear in `revenue_by_city`? Is counting a ₹0 order as
  "revenue" correct? (This is a *business-rules* judgment, not a syntax one — say
  why count-metrics and revenue-metrics filter differently.)

<details><summary>Break-it answers</summary>

- (a) Bengaluru (`899 < 1000`) drops. The floor removes it before summing.
- (b) Without the copy, `clean` mutates the original dicts — `orders[0]["city"]`
  becomes `'Pune'` (trimmed/titled), and `"amount"` gains an `"amt"` sibling. On
  the second run you're cleaning already-cleaned data. This is the **mutable
  reference** trap from Topic 2: functions that mutate their inputs cause
  spooky-action-at-a-distance bugs. Always copy at the boundary.
- (c) With `>=`, `id=3` (`0.0`) passes → `revenue_by_city` gains `'Mumbai': 0.0`
  from it (on top of the 1500). Counting a ₹0 order as revenue is *wrong* — it
  inflates the "cities with revenue" set with zero-value entries. **Count metrics**
  (how many delivered orders?) include the free order; **revenue metrics** must
  filter `amount > 0`. Same data, different denominator — always pin the
  definition first.
</details>

---

## ✅ Phase-0 Gate — you pass when you can, from memory:

- [ ] Explain interpreted vs bytecode + what the GIL blocks (T1)
- [ ] Predict aliasing/mutability behaviour and copy safely (T2)
- [ ] Pick list vs dict vs set by cost, and count with a dict/`defaultdict` (T3)
- [ ] Write comprehensions, avoid the falsy/`or` trap, know when a loop is clearer (T4)
- [ ] Write clean functions, dodge the mutable-default trap, use `*args/**kwargs`,
      explain a closure (T5)
- [ ] **Compose functions into a small pipeline and reason about mutation + business
      definitions** (Boss Fight)

Missed any? Redo that topic's `practice.md` Hard problem, then re-run the Boss Fight.

**All green → you're ready for Phase 1: Iterators & Generators (lazy data).**

---

*Spaced repetition: revisit this file's Layer 1 flash cards in 3 days, then 7 days,
then 21 days. Re-run the Boss Fight from scratch at the end of Phase 1.*
