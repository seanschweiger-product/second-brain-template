---
name: start-day
description: Morning standup against the brain — broad scan, calendar-verified day plan, optional scheduling. Use when the user says "/start-day", "good morning", or asks what today's plan is.
---

# /start-day — morning standup → verified day plan

Paths are relative to the brain root.

Goal: produce a proposed **day plan** (time-blocked schedule), grounded in a broad read of the brain AND — if a calendar integration is connected — the live calendar. Don't treat any planning document other than `current-status.md` as authoritative unless the user explicitly says it's still current; standalone plan docs go stale fast.

## Step 0 — meeting-file check (report only, never ingest)
If `raw/` contains unprocessed files, mention it in one line ("N file(s) waiting in raw/ — say ingest"). Never ingest during /start-day.

## Step 1 — broad scan (not just two files)
Read:
- `wiki/log.md` (recent entries, enough to cover since the last working day)
- `wiki/projects/current-status.md` in full — including any open-commitment tables from recent meetings (owner/status/notes rows), not just the header
  - **If `current-status.md` doesn't exist yet** (first run): ask the user for their current objective — ONE sentence describing the outcome their work is driving toward right now — and create the page:

    ```markdown
    # Current status

    **Objective:** <their sentence>
    **Today:** <date> — <task, filled by this skill>
    ```
- Any active project pages `current-status.md` points to — follow links that look live/open, skip ones clearly closed or superseded

From this, extract: what changed since last session, and every open item with a deadline or pending owner action — especially ones due today or in the next few days.

## Step 2 — calendar verification (if a calendar integration is connected)
If a calendar tool/integration is available, use it to list the user's actual events for **today + the next 2–3 days**. Never trust a meeting claim in a wiki doc without calendar confirmation — wiki docs go stale (a doc can list a meeting that was never booked, or omit one that's actually on the calendar). Treat the live calendar as ground truth for anything schedule-shaped; treat the wiki as ground truth for content/context/commitments.

Cross-check: for every meeting or deadline claimed in Step 1, confirm it against the calendar. Flag mismatches explicitly (e.g. "wiki says X at 09:30 — not on the calendar, dropping it" / "calendar shows Y tomorrow 14:00 that the wiki didn't mention — this is real").

If no calendar integration is connected, skip this step and say so plainly rather than guessing at the schedule.

## Step 3 — build the day plan
Prioritize using calendar deadlines (fixed events, upcoming external commitments, when available) plus `current-status.md`'s open items.

Output a table of time blocks covering the whole day:

| Start–End | Block | What happens |
|---|---|---|

Rules for the plan:
- Fixed calendar events are hard constraints — place them as-is.
- Add prep slots immediately before any external call/meeting (review notes, prep talking points).
- Always include a lunch block (roughly an hour, placed near midday).
- Fill remaining time with deep-work blocks covering all active work lanes surfaced in Step 1 (not just one task) — sized realistically against what's actually open.
- If a block heads toward a deadline found in Step 1/2, name the deadline it serves.

Present the plan as the reply. No headers beyond the table + brief framing lines. No documents produced.

## Step 4 — one adjustment round
Let the user push back once; adjust the plan in conversation. Do not re-litigate endlessly — one round, then move to execution once they approve.

## Step 5 — on explicit approval only: schedule it
Only after the user explicitly approves the (possibly adjusted) plan, and only if a calendar integration is connected:
- Create one calendar event per block on the user's own calendar, each with a description (what the block is for, which deadline/commitment it serves).
- If a block involves another person and their calendar is accessible, check their availability first and adjust the block before creating/sending an invite to them.
- Any message sent to a colleague as part of this should match the language conventions the user normally uses for that channel.

If no calendar integration is connected, skip this step — the plan stands as a conversation artifact only.

## Standing rules
- Never invent state — if the log or status doc is stale, say so plainly rather than filling gaps.
- Reply in the language the user writes in.
- No documents are produced by /start-day — the day plan lives in the conversation (and, once approved, on the calendar if one is connected).
