---
name: lint
description: Run a maintenance pass on the wiki — find orphans, stale pages, superseded claims, contradictions, missing entity pages, index gaps, missing cross-references, format drift, and open data gaps. Use monthly, or whenever the user says "lint" or asks for wiki maintenance.
---

# Lint — the wiki maintenance pass

> Wikis die because the maintenance burden grows faster than the value. This pass keeps the cost of maintenance near zero. Run it monthly, or whenever the user asks.

---

## Step 1 — Orient

Read `WIKI-SCHEMA.md`, then `wiki/index.md`, then skim `wiki/log.md` for recent activity.
Build the full picture: every page that exists, every page the index claims exists.

---

## Step 2 — Run every check

Walk the whole `wiki/` tree and check:

1. **Orphan pages** — no inbound `[[wikilink]]` from anywhere. Every page must be reachable.
2. **Stale pages** — `updated:` more than 30 days ago; likely needs a refresh or an explicit "still current" confirmation.
3. **Superseded claims** — facts that a newer source has overtaken (e.g. a status page still showing a decision that a later meeting reversed). Compare page content against newer log entries and meeting pages.
4. **Contradictions** — conflicting facts across pages. Note the contradiction on both pages; never silently pick a winner.
5. **Missing entity pages** — people, projects, or concepts mentioned on 2+ pages but with no dedicated page.
6. **Index gaps** — pages that exist but aren't listed in `wiki/index.md`, or index rows pointing at pages that don't exist.
7. **Missing cross-references** — a concept/person/project named in prose but not wikilinked.
8. **Format drift** — pages missing frontmatter, wrong category values, filenames off-convention, missing Links section.
9. **Data gaps** — open questions the wiki raises but never answers (an "Uncertain" from an old ingest digest that was never resolved, an action item with no outcome). Many can be imputed directly with a web search or a connector query — do so when the answer is factual and checkable; flag the rest as candidates for investigation.
10. **New page candidates** — interesting connections across existing pages that deserve a page of their own: a theme recurring on 3+ pages, two concepts that keep appearing together, a pattern nobody has named yet. Propose these as new concept/synthesis pages.

---

## Step 3 — Report before fixing

Show the user a findings list grouped by check, each with the proposed fix.

- **Mechanical fixes** (index rows, missing backlinks, frontmatter/format repairs): apply directly, no approval needed.
- **Content fixes** (resolving contradictions, marking claims superseded, refreshing stale pages, answering data gaps): these change compiled knowledge — get the user's confirmation first, or mark the page with the open question if the user isn't available.

---

## Step 4 — Apply and log

Apply the approved fixes. Then append to `wiki/log.md`:

```
## [YYYY-MM-DD] lint | full pass
**Checks run:** 10/10
**Fixed:** [list — orphans linked, index rows added, ...]
**Flagged for user:** [contradictions/gaps awaiting a decision]
**New page candidates:** [proposed, with the pages that suggested them]
**Clean:** [checks that found nothing]
```

---

## Step 5 — Digest

End with a short summary in chat: what was fixed, what needs the user's decision, and **suggested further questions to ask the wiki** — the lint pass is also how the brain tells you what it's curious about (per Karpathy: "The LLMs are quite good at suggesting further questions to ask and look into").
