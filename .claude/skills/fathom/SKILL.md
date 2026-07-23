---
name: fathom
description: One-button Fathom sync — pull the newest meeting (summary + action items + transcript) into raw/ and ingest it. Use when the user says "/fathom", "pull my meetings", or just finished a meeting. Requires a Fathom account.
---

# Fathom — one-button meeting sync

Press this at the end of a meeting (or whenever). It replaces the manual flow
of copying from fathom.video, saving a file, and running ingest by hand.
Only useful if the user records meetings with [Fathom](https://fathom.video).

## Step 1 — Pull

Run the fetcher (path is relative to the brain root):

```
python3 scripts/fathom_poll.py
```

It calls the Fathom API (free tier works; key in `~/.fathom-api-key`) and pulls
**only the single most recent meeting** — the expected habit is pressing this at
the end of each meeting. Add `--all` to sweep every unseen meeting from the last
2 days instead. The file lands in `raw/` as `YYYY-MM-DD-<topic>-fathom.txt` —
summary, action items, and full transcript. Pressing twice is safe:
already-pulled meetings are skipped (state in `~/.fathom-poller-state.json`).

**If it errors with "API key file missing":** the user needs a Fathom API key
(fathom.video → Settings → API). Tell them to run, in a regular terminal window
(not pasted into the chat):

```
echo "PASTE_KEY_HERE" > ~/.fathom-api-key && chmod 600 ~/.fathom-api-key
```

## Step 2 — Report

Tell the user exactly which files landed (or "no new meetings since last
pull" — then stop).

## Step 3 — Ingest

Immediately run the full `ingest` skill protocol on the new files — every step,
including connector enrichment if this session has connectors available.
Finish with the standard ingest digest.
