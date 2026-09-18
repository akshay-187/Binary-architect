# PatchPilot — Hackathon Build Plan

Five phases for the 48-hour IBM Bob 2.0 Hackathon build, split across a
3-person team: Bob Architect, Product Engineer, QA / Pitch Lead. Each phase
has an exit condition — do not move to the next phase until it is met.

## Timeline overview

| Phase | Duration | Focus |
|-------|----------|-------|
| 1. Setup & Scoping | ~4-5 hrs | Problem statement, access, baseline timing |
| 2. Core Loop (MVP) | ~18 hrs | One bug through the full pipeline, for real |
| 3. Full Pipeline & Evidence | ~12 hrs | Remaining bugs, rollback demo, impact numbers |
| 4. Polish the Demo Path | ~8 hrs | Fix only what's on the demo path |
| 5. Record & Submit | ~6 hrs | Video, slides, submission |

## Phase 1 — Setup & Scoping (~4-5 hrs)

| Role | Tasks |
|------|-------|
| Bob Architect | Confirm Bob 2.0 access; confirm the brain layer (`AGENTS.md`, `.bob/rules*`) is live in the repo |
| Product Engineer | Pin down the target user and one-sentence problem statement with the team; set up `sample_repository/` as a clean base |
| QA / Pitch Lead | Pick 2 bugs to seed later; manually fix one the "old way" now and time it end-to-end — this baseline number drives the whole business case |

**Exit condition:** one agreed problem statement, plus a working Bob connection.

## Phase 2 — Core Loop (MVP) (~18 hrs)

The phase that decides if there is a project.

| Role | Tasks |
|------|-------|
| Bob Architect | Get one seeded bug through the entire pipeline for real: Plan Mode + subagents investigate, human approves, Agent Mode patches and writes the regression test, report generates. Confirm subagents are actually spawning, not just narrated |
| Product Engineer | Seed 3-5 real bugs into `sample_repository/` (logic bug, off-by-one, unhandled input, race condition); wire `app.py` to visualize each stage of that first run |
| QA / Pitch Lead | Watch the first full run closely — confirm the regression test genuinely fails before the patch and passes after; time the run against the Phase 1 baseline |

**Exit condition:** one bug goes in as a raw report and comes out the other
side as an approved, tested patch, reproducibly, on screen. If this does not
work by the end of this phase, cut scope, not corners.

## Phase 3 — Full Pipeline & Evidence (~12 hrs)

| Role | Tasks |
|------|-------|
| Bob Architect | Push the remaining seeded bugs through the pipeline; deliberately fail a patch once and demo Rollback recovering cleanly |
| Product Engineer | Add a document-understanding entry point (raw ticket export or log file instead of typed text); deploy the app to a real URL |
| QA / Pitch Lead | Collect timing and step-count numbers across all seeded bugs; draft the business case: target user, rough market, one revenue model |

**Exit condition:** every seeded bug has a clean, inspected run, the app has
a live URL, and the before/after numbers are real, not estimated.

## Phase 4 — Polish the Demo Path (~8 hrs)

| Role | Tasks |
|------|-------|
| Bob Architect | Clean up the exported Bob session reports for the 1-2 bugs being demoed |
| Product Engineer | Fix bugs only on the path being demoed — resist adding scope |
| QA / Pitch Lead | Finalize slides (8-10 pages); write the video script |

**Exit condition:** the exact demo sequence runs twice in a row without
breaking.

## Phase 5 — Record & Submit (~6 hrs)

| Role | Tasks |
|------|-------|
| Bob Architect | Final push to the public GitHub repo, exported Bob reports included |
| Product Engineer | Final smoke test on the deployed URL right before submission |
| QA / Pitch Lead | Record the video; submit with time to spare; prep for judge Q&A |

**Exit condition:** submitted, with buffer time left over — not spent on new
features.
