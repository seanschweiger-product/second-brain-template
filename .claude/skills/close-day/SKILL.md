---
name: close-day
description: End-of-day close against the brain — what was actually done, THEN a proposed plan for tomorrow, one log entry. Use when the user says "/close-day" or wants to wrap up the working day.
---

# /close-day — close today, plan tomorrow

Paths are relative to the brain root.

Goal: close today honestly, THEN produce a proposed **time-blocked plan for tomorrow** (same shape as /start-day's plan), grounded in a broad read of the brain and — if a calendar integration is connected — the live calendar. Don't treat any planning document other than `current-status.md` as authoritative unless the user explicitly says it's still current. One adjustment round with the user, then — only on explicit approval, and only if a calendar integration is connected — create tomorrow's calendar events. This lets tomorrow's /start-day verify a delta instead of building a plan from scratch.

## Step 0 — meeting check (report only, NO ingest)
If `raw/` contains unprocessed files, mention it in one line ("N file(s) waiting in raw/ — say ingest"). Never ingest during /close-day.

## Step 1 — close today (2 lines)
Reply with EXACTLY two lines:
- **Done:** what was actually completed today (verified facts only — if the day's task wasn't finished, say so plainly). No achievement inflation — "restarted a server" is a chore, not an achievement.
- **Tomorrow:** the one-line headline of tomorrow's main focus (the full time-blocked plan follows in Step 3).

## Step 2 — scan for tomorrow (broad, forward-looking)
Read:
- `wiki/log.md` (recent entries, including today's — carry forward anything left open today)
- `wiki/projects/current-status.md` in full, including any open-commitment tables (owner/status/notes), not just the header
- Any active project pages `current-status.md` points to — follow links that look live/open

Extract: every open item with a deadline or pending action, especially anything due tomorrow or in the next few days, plus anything from today that didn't get finished.

If a calendar integration is connected, use it to list the user's actual events for **tomorrow** (and the day after, for context). Never trust a meeting claim in a wiki doc without calendar confirmation — treat the live calendar as ground truth for anything schedule-shaped, the wiki as ground truth for content/context/commitments. Flag mismatches explicitly. If no calendar integration is connected, skip this and say so plainly rather than guessing at the schedule.

## Step 3 — build tomorrow's day plan
Prioritize using tomorrow's calendar (fixed events, upcoming external commitments, when available) plus the open items surfaced in Step 2. Do not treat any standalone plan doc as authoritative.

Output a table of time blocks covering the whole day, same format as /start-day:

| Start–End | Block | What happens |
|---|---|---|

Rules for the plan:
- Fixed calendar events are hard constraints — place them as-is.
- Add prep slots immediately before any external call/meeting.
- Always include a lunch block (roughly an hour, placed near midday).
- Fill remaining time with deep-work blocks covering all active work lanes surfaced in Step 2 — sized realistically.
- If a block heads toward a deadline found in Step 2, name the deadline it serves.

Present the plan as the reply. No headers beyond the table + brief framing lines. No documents produced yet.

## Step 4 — one adjustment round
Let the user push back once; adjust the plan in conversation. One round, then move to scheduling once they approve.

## Step 5 — on explicit approval only, and only if a calendar integration is connected: create tomorrow's events
Only after the user explicitly approves the (possibly adjusted) plan:
- Create one calendar event per block on the user's own calendar, each with a description stating what the block is for and which deadline/commitment it serves, plus a marker tag `(via /close-day — planned <today's date>)` so tomorrow's /start-day can recognize these events as pre-planned.
- If a block involves another person and their calendar is accessible, check their availability first and adjust the block before creating/sending an invite.
- Any message sent to a colleague should match the language conventions the user normally uses for that channel.
- If no calendar integration is connected, or the user doesn't approve/schedule, skip this step — record that plainly in the log instead of a "planned + scheduled" note.

## Step 6 — log entry (the only written artifact)
Append one dated entry to `wiki/log.md` recording: what was done today, decisions made, and — if Step 5 completed — that tomorrow was planned + scheduled, with the approved plan table (or a compact summary of its blocks) so tomorrow's /start-day can diff against it. If it wasn't approved/scheduled, say so plainly instead of claiming tomorrow is planned.

## Step 7 — refresh current-status.md
Update the "Today" line in `wiki/projects/current-status.md` if it's stale (see /start-day for the page format if it doesn't exist yet).

## Standing rules
- Never invent state — if the log or status doc is stale, or the plan wasn't approved, say so plainly rather than filling gaps.
- Reply in the language the user writes in.
- No side documents — `wiki/log.md` and the `current-status.md` refresh are the only writes /close-day makes.
