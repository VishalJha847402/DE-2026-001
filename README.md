# DE-2026 — Data Engineering Learning Platform

A premium, browser-based learning platform for becoming a Data Engineer in 2026 India.

## What's Inside

**8 Python topics deep**, each with main content + 15-question practice bank:

- **T1** Data Types & Variables — types, mutability, datetime, pathlib, Decimal
- **T2** Control Flow — if/elif/else, loops, comprehensions, walrus, match/case
- **T3** Data Structures — list/dict/set/tuple, Counter, defaultdict, heapq, bisect
- **T4** Functions — decorators, closures, generators, itertools, functools
- **T5** OOP Classes — classes, dataclass, classmethod, staticmethod, property, slots
- **T6** OOP Advanced — inheritance, ABC, MRO, context managers, contextlib
- **T7** Pydantic — BaseModel, validators, nested models, BaseSettings, special types
- **T8** Async OOP & Testing — asyncio, async ctx managers, pytest, fixtures, mocks

**120 real-world DE practice problems** across Indian e-commerce, fintech, stock market, logistics, banking scenarios.

## Features

- Premium dark/light theme UI
- VS Code-style code blocks with syntax highlighting
- Line-by-line walkthroughs
- Live Python in browser (Pyodide — no install)
- SPA navigation, topic isolation
- Progress tracking via localStorage
- 4-Gates accountability per topic
- India-grounded (Naukri / LinkedIn India 2026 market data)

## How to Use

1. Open `index.html` in any modern browser
2. Click any topic card → study at depth
3. Click "Open Practice Bank" → solve 15 real-world problems
4. Tick 4 Gates per topic to mark complete

## Local Development

No build step. Just open the HTML files in browser.

```bash
# Optional: serve via local HTTP for cleaner URL handling
python -m http.server 8000
# Then open http://localhost:8000
```

## Deploy

Drop the folder to Netlify (netlify.com/drop) or connect via GitHub for auto-deploy.

## Project Files

- `index.html` — roadmap dashboard
- `python.html` — all 8 topics (SPA)
- `python-t1-practice.html` ... `python-t8-practice.html` — practice banks
- `CLAUDE.md` — teaching rules + project guidelines
- `PENDING.md` — backlog status

---

Built with Claude. Designed for the 2026 India DE job market.
