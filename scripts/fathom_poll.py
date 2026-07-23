#!/usr/bin/env python3
"""Poll the Fathom API for new meetings and drop formatted source files into raw/.

Each new meeting becomes one file in <brain>/raw/, named
YYYY-MM-DD-<topic>-fathom.txt, ready for the /ingest skill. The brain root is
resolved from this script's location (it lives in <brain>/scripts/). State
(seen recording ids) lives in ~/.fathom-poller-state.json; the API key in
~/.fathom-api-key. Neither is inside the repo, so no secrets can be committed.
"""

import json
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API_BASE = "https://api.fathom.ai/external/v1"
KEY_FILE = Path.home() / ".fathom-api-key"
STATE_FILE = Path.home() / ".fathom-poller-state.json"
RAW_DIR = Path(__file__).resolve().parent.parent / "raw"
LOG_FILE = Path.home() / ".fathom-poller.log"
LOOKBACK_DAYS = 2  # bounds the query; only the single newest meeting is taken
MAX_SEEN_IDS = 1000


def log(msg: str) -> None:
    line = f"{datetime.now().isoformat(timespec='seconds')} {msg}"
    print(line)
    with LOG_FILE.open("a") as f:
        f.write(line + "\n")


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"seen_ids": []}


def save_state(state: dict) -> None:
    state["seen_ids"] = state["seen_ids"][-MAX_SEEN_IDS:]
    STATE_FILE.write_text(json.dumps(state, indent=2))


def api_get(path: str, params: dict) -> dict:
    query = urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(
        f"{API_BASE}{path}?{query}",
        headers={"X-Api-Key": KEY_FILE.read_text().strip()},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


def fetch_new_meetings(since: str) -> list:
    meetings, cursor = [], None
    while True:
        params = {
            "created_after": since,
            "include_summary": "true",
            "include_transcript": "true",
            "include_action_items": "true",
        }
        if cursor:
            params["cursor"] = cursor
        page = api_get("/meetings", params)
        meetings.extend(page.get("items", []))
        cursor = page.get("next_cursor")
        if not cursor:
            return meetings


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (title or "untitled").lower()).strip("-")
    return slug[:50].rstrip("-") or "untitled"


def local_date(iso_ts: str) -> str:
    dt = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
    return dt.astimezone().strftime("%Y-%m-%d")


def duration_minutes(m: dict) -> str:
    try:
        start = datetime.fromisoformat(m["recording_start_time"].replace("Z", "+00:00"))
        end = datetime.fromisoformat(m["recording_end_time"].replace("Z", "+00:00"))
        return f"{round((end - start).total_seconds() / 60)} mins"
    except (KeyError, TypeError, ValueError):
        return "unknown length"


def format_meeting(m: dict) -> str:
    lines = [
        f"# {m.get('title') or m.get('meeting_title') or 'Untitled meeting'}",
        f"Date: {local_date(m['created_at'])} ({duration_minutes(m)})",
    ]
    rec = m.get("recorded_by") or {}
    if rec:
        lines.append(f"Recorded by: {rec.get('name', '?')} <{rec.get('email', '?')}>")
    invitees = m.get("calendar_invitees") or []
    if invitees:
        people = ", ".join(
            f"{p.get('name') or '?'} <{p.get('email') or '?'}>"
            + (" [external]" if p.get("is_external") else "")
            for p in invitees
        )
        lines.append(f"Invitees: {people}")
    lines.append(f"Fathom link: {m.get('share_url') or m.get('url') or '?'}")
    lines.append("Source: Fathom API auto-pull (scripts/fathom_poll.py)")

    summary = (m.get("default_summary") or {}).get("markdown_formatted")
    lines += ["", "## Summary", "", summary.strip() if summary else "(no summary returned)"]

    lines += ["", "## Action items", ""]
    items = m.get("action_items") or []
    if items:
        for it in items:
            assignee = (it.get("assignee") or {}).get("name") or "unassigned"
            ts = it.get("recording_timestamp") or "?"
            lines.append(f"- [ ] {it.get('description', '?')} — {assignee} ({ts})")
    else:
        lines.append("(none)")

    lines += ["", "## Transcript", ""]
    transcript = m.get("transcript") or []
    if transcript:
        for t in transcript:
            speaker = (t.get("speaker") or {}).get("display_name") or "?"
            lines.append(f"[{t.get('timestamp', '?')}] {speaker}: {t.get('text', '')}")
    else:
        lines.append("(no transcript returned)")

    return "\n".join(lines) + "\n"


def target_path(m: dict) -> Path:
    base = f"{local_date(m['created_at'])}-{slugify(m.get('title') or m.get('meeting_title'))}-fathom"
    path = RAW_DIR / f"{base}.txt"
    if path.exists():
        path = RAW_DIR / f"{base}-{m['recording_id']}.txt"
    return path


def main() -> int:
    if not KEY_FILE.exists():
        log("ERROR: API key file missing at ~/.fathom-api-key")
        return 1
    state = load_state()
    since = (datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    try:
        meetings = fetch_new_meetings(since)
    except Exception as e:
        log(f"ERROR: Fathom API call failed: {e}")
        return 1

    if not meetings:
        log(f"done: no meetings found in the last {LOOKBACK_DAYS} days")
        return 0

    # Default (end-of-meeting button): only the single newest meeting.
    # --all (safety net for daily rituals): every unseen meeting in the window.
    if "--all" in sys.argv:
        targets = sorted(meetings, key=lambda m: m.get("created_at", ""))
    else:
        targets = [max(meetings, key=lambda m: m.get("created_at", ""))]

    written = 0
    for m in targets:
        if m.get("recording_id") in state["seen_ids"]:
            continue
        path = target_path(m)
        path.write_text(format_meeting(m))
        state["seen_ids"].append(m.get("recording_id"))
        written += 1
        log(f"wrote {path.name}")

    save_state(state)
    if written == 0:
        log("done: nothing new — already pulled")
    else:
        log(f"done: {written} file(s) written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
