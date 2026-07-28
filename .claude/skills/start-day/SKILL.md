---
name: start-day
description: Morning standup against the brain — broad scan, calendar-verified day plan, optional scheduling. Use when the user says "/start-day", "good morning", or asks what today's plan is.
---

# /start-day — morning standup → verified day plan

Paths are relative to the brain root.

Goal: produce a proposed **day plan** (time-blocked schedule), grounded in a broad read of the brain AND — if a calendar integration is connected — the live calendar. Don't treat any planning document other than `current-status.md` as authoritative unless the user explicitly says it's still current; standalone plan docs go stale fast.

## Step 0 — meeting-file check (report only, never ingest)
If `raw/` contains unprocessed files, mention it in one line ("N file(s) waiting in raw/ — say ingest"). Never ingest during /start-day.

## Step 0.5 — check for an evening plan (delta-mode gate)
Before doing any broad scan or building a plan from scratch, check whether last night's `/close-day` already planned + scheduled today:
- Read the most recent `/close-day` entry in `wiki/log.md` (should be dated yesterday) — look for a "planned + scheduled" note covering today's date and a plan table/summary.
- If a calendar integration is connected, cross-check it: list today's events and look for ones whose description carries the marker `(via /close-day — planned <yesterday's date>)`.

If both signals agree an evening plan exists (or the log note is confirmed and no calendar integration is connected to cross-check) → go to **Delta mode** below and skip Steps 1–3. If either signal is missing or unclear (close-day was skipped, the plan wasn't approved, or events weren't actually created) → say so plainly and fall back to the **Full build** (Steps 1–3 unchanged, exactly as before).

## Delta mode (only when Step 0.5 finds an evening plan)
1. Retrieve last night's plan from the `/close-day` log entry (the table or block summary it recorded).
2. If a calendar integration is connected, re-list today's actual events — ground truth.
3. Compare block by block: still present as planned? moved? cancelled? Also flag any new event that appeared overnight and wasn't in last night's plan, any overnight meeting files that landed in `raw/` (report only, per Step 0), and any other new signal that's trivially visible — don't go hunting, just don't ignore what's already in view.
4. Report **only the delta** — lead with "what changed since last night" and list adds/moves/removals. Do not restate unchanged blocks in full.
5. Propose changes only for the affected blocks (move/add/remove) — one adjustment round, same as Step 4 below.
6. On explicit approval, and only if a calendar integration is connected, apply only the delta to the calendar (create/update/delete the affected events) — leave unaffected events untouched.
7. No separate log entry is required for /start-day itself; a one-line note in the reply that the delta was applied is enough.

## Full build (fallback — no evening plan found, or Step 0.5 was inconclusive)

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
