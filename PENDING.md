# PENDING — Parked Items

All items here are agreed in principle but execution is deferred. Do not pick these up unless Vishal explicitly says "let's do this."

---

## 1. Cross-Device Sync Setup (CONFIRMED — Option D)
**Goal:** Same project, same progress on both Macs (MacBook + Mac mini). Nothing ever vanishes.

**Approach:**
- **Code** lives on private GitHub repo (`DE-2026`).
- **Progress** (gate ticks, topic %, completion dates) lives in a Google Sheet inside Vishal's Drive.
- Each HTML page reads from Sheet on load → shows real progress.
- Claude updates Sheet via Drive MCP.

**Steps to do later:**
1. Confirm GitHub username + repo name (`DE-2026`).
2. Create private GitHub repo.
3. `git init` + first commit + push.
4. Clone repo on Mac mini.
5. Create Google Sheet `DE-2026 Progress` via Drive MCP.
6. Add Sheet-sync JS to every HTML page (read on load, write on gate tick).
7. Add session backup button (downloads JSON of full state).

**Why parked:** Setup is ~15 minutes. Vishal wants to focus on learning right now. Will do this once Topic 1 + Topic 2 are deep underway.

---

## 2. Plan Items Still Not Finalized
From CLAUDE.md Rule #16, still open:

### a. AI Era DE Definition
Define which DE tasks AI replaces, which AI assists, which Vishal owns deeply.
Three buckets (A/B/C) drafted in chat — not yet locked into CLAUDE.md.

### b. Pace/Signal System
How Vishal signals "too fast" or "too slow" mid-session. Need a clear protocol.
Not designed yet.

---

## 3. Projects (Already Locked, Execution Deferred)
From CLAUDE.md Rule #14:
- **P1** — SQL Analytics Project (end of Phase 1)
- **P2** — End-to-End Pipeline (end of Phase 2)
- **P3** — AI-Era Pipeline (end of Phase 3)

Do not start any project until that phase's skills are complete.

---

## 4. Topic Pages Not Yet Built
Only `index.html` and `python.html` (Topic 1 only) exist.
Other pending HTML files referenced from index.html:
- linux.html, git.html, sql.html
- data-modeling.html, cloud.html, docker.html, etl.html
- spark-basics.html, airflow.html, dbt.html, warehouse.html
- spark-advanced.html, kafka.html, ai-de.html

Build each only when we reach that skill.

---

## 5. Python Topics — Build Status
Build inside `python.html` as separate sections when each topic begins:
- ✅ 1. Data Types & Variables — DONE (+ 15-question practice bank)
- ✅ 2. Control Flow — DONE (+ 15-question practice bank)
- ✅ 3. Data Structures — DONE (+ 15-question practice bank)
- ✅ 4. Functions — DONE (+ 15-question practice bank)
- ✅ 5. OOP — Classes — DONE (+ 15-question practice bank)
- ✅ 6. OOP Advanced — Inheritance, ABC, Context Managers — DONE (+ 15-question practice bank)
- ✅ 7. Pydantic & Modern Validation — DONE (+ 15-question practice bank)
- ✅ 8. Async OOP & Testing — DONE (+ 15-question practice bank)
- 9. Error Handling
- 10. Files & Serialization
- 8. Files & Serialization
- 9. Modules & Virtual Envs
- 10. Testing (pytest)
- 11. APIs & HTTP
- 12. Iterators & Decorators
- 13. Pandas
- 14. NumPy

**Note on skipped topics 3 & 4:** Must come back before Topic 7 (Error Handling) at the latest. OOP will work but Vishal may need quick refreshers on dict/list internals and function basics during OOP teaching.

---

## 6. Misc Improvements (When We Have Time)
- Session backup / restore (download JSON of all progress + typed code, re-upload anytime)
- Search bar in sidebar (jump to any topic across all skills)
- Print-friendly version of each topic (for handwritten notes in GoodNotes)
- Mobile responsive polish (current works, but could be smoother)

---

**Last updated:** by Claude during initial planning session.
