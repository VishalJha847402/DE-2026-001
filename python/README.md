# Python for Data Engineering — Learning Series

> DE-2026 · Depth-first · **Grounded in real 2026 India DE job postings** (Jun 2026 research)
> **Not a generic Python tutorial — Python *for Data Engineering*.** Every topic earns its place by making you a better DE.

## 🎯 What 2026 India DE jobs actually ask (research-grounded)

Across ALL profile names — Data Engineer · Big Data Engineer · Azure Data Engineer · Snowflake DE — the constant is **Python + SQL in ~100% of postings.**

**Python libraries they actually use:** pandas **+ the rising Polars + DuckDB hybrid** · PySpark · **pydantic** (now the validation standard) · requests/httpx · SQLAlchemy · PyArrow · boto3/cloud SDKs.
**Python concepts interviews probe:** generators · decorators · dataclasses · asyncio · comprehensions · error handling · PySpark UDFs.

This roadmap is built to cover exactly that. (Spark, Airflow, dbt, cloud, warehouses = their own series — this one is the **Python** pillar + its DE glue.)

## Roadmap

| Phase | Topic | Status |
|-------|-------|--------|
| **Phase 0** | Foundations Re-grounded | 🟡 In Progress |
| Phase 1 | Pythonic & Intermediate | ⏳ Pending |
| Phase 2 | Python for Data Engineering (the DE core) | ⏳ Pending |
| Phase 3 | Production-Grade Python | ⏳ Pending |
| Phase 4 | Performance & Concurrency | ⏳ Pending |
| Phase 5 | AI-Era & Orchestration Glue | ⏳ Pending |

**Progress: 1 of ~35 lessons done.**

> You know Python at a "moderate" level. Per DE-2026 Rule #15, we run the **full cycle even on topics you know** — functional knowledge hides holes. Speed-read the easy parts; slow down on the WHY and the traps.

---

## Phase 0 — Foundations Re-grounded 🟡

> Fix the hidden holes in what you already "know." This is where DA→DE engineers leak.

| # | Lesson | Status |
|---|--------|--------|
| 1 | [How Python Actually Runs (interpreter, bytecode, the GIL)](./phase-0-foundations/topic-1-how-python-runs/) | ✅ Done |
| 2 | Variables, Memory & the Mutable/Immutable Trap | 🟡 Next |
| 3 | Data Structures Deep — list / dict / set / tuple + `collections` | ⏳ Pending |
| 4 | Control Flow & Comprehensions (the Pythonic way) | ⏳ Pending |
| 5 | Functions — args, *args/**kwargs, scope, closures | ⏳ Pending |

---

## Phase 1 — Pythonic & Intermediate ⏳

| # | Lesson |
|---|--------|
| 1 | Iterators & Generators (lazy data — critical for DE) |
| 2 | `itertools` & `functools` (memory-efficient iteration) ⭐ *added from research* |
| 3 | Decorators |
| 4 | Context Managers (`with` — files, DB connections) |
| 5 | Error Handling & Exceptions (+ retries/backoff for pipelines) |
| 6 | OOP + dataclasses + dunder methods |

---

## Phase 2 — Python for Data Engineering ⏳ (the DE core)

| # | Lesson |
|---|--------|
| 1 | Files & the Filesystem — `pathlib`, `os`, `subprocess`, env vars ⭐ *added* |
| 2 | File Formats & I/O — CSV, JSON, Parquet, **PyArrow** (the Arrow backbone) |
| 3 | Regex + Nested / Semi-structured JSON parsing ⭐ *added* |
| 4 | **NumPy** Essentials *(now before pandas — pandas is built on it)* |
| 5 | **pandas** Deep — the DA→DE bridge |
| 6 | **Polars & DuckDB** — the 2026 modern stack ⭐⭐ *heavily demanded in research* |
| 7 | APIs — `requests`/`httpx`, REST, pagination, auth, retries |
| 8 | Databases from Python — SQLAlchemy, connection pooling |
| 9 | Dates, Times & Timezones (the silent data killer) |

---

## Phase 3 — Production-Grade Python ⏳

| # | Lesson |
|---|--------|
| 1 | Type Hints & mypy |
| 2 | **Pydantic** — Data Validation *(now the industry standard)* |
| 3 | Testing with pytest + **data-quality testing** ⭐ *added* |
| 4 | Logging (not `print`) |
| 5 | Packaging, virtualenvs, dependency management (uv/poetry) |
| 6 | Project Structure & Config/Secrets |

---

## Phase 4 — Performance & Concurrency ⏳

| # | Lesson |
|---|--------|
| 1 | Profiling & Memory |
| 2 | The GIL Deep · threading vs multiprocessing · `concurrent.futures` ⭐ *made explicit* |
| 3 | async / asyncio + httpx (I/O-bound DE — thousands of API calls) |
| 4 | Memory-Efficient Processing (chunking, generators, streaming) |

---

## Phase 5 — AI-Era & Orchestration Glue ⏳

| # | Lesson |
|---|--------|
| 1 | Working with LLM APIs / SDKs |
| 2 | Pydantic for Structured LLM Outputs |
| 3 | Python in **Airflow & dbt** — how Python glues orchestration ⭐ *added* |
| 4 | FastAPI for Data Services |

---

## Full Roadmap Summary

| Phase | Lessons |
|-------|---------|
| Phase 0 · Foundations | 5 |
| Phase 1 · Pythonic & Intermediate | 6 |
| Phase 2 · Python for DE | 9 |
| Phase 3 · Production-Grade | 6 |
| Phase 4 · Performance & Concurrency | 4 |
| Phase 5 · AI-Era & Glue | 4 |
| **Total** | **~34 lessons** |

⭐ = added/reordered after Jun 2026 India job-market research (Polars/DuckDB, itertools/functools, pathlib, regex/JSON, concurrent.futures, data-quality testing, Airflow/dbt glue).

---

*Each lesson folder has: `README.md` (full lesson + diagram + revision + 10 practice questions)*
*Spaced-repetition recall files live in [`revision/`](./revision/)*
*Sister series: [Apache Spark & PySpark](../spark/)*
