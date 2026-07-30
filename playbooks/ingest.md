# Playbook: ingest

> Agent procedure: business input → reviewable draft backlog. Spec: FR-ING-001..006.
> Read `AGENTS.md` first. Human gates are marked **⛔ STOP**. Never skip them.
>
> **The prime directive: no artifact files before the gate; no invented content ever.**
> Whatever the input does not say becomes an `open_questions` entry — not your guess.

## Stage 0 — Accept input

- Supported: `.md`, `.txt`, `.docx`, `.pdf` (text layer). Anything else: reject explicitly,
  tell the owner what to convert; never silently mangle.
- Input location: `inbox/` or explicit paths from the owner.

## Stage 1 — Extract

1. Read the full input. Build an inventory of candidate scope items: capabilities, user roles,
   business rules, constraints, explicit exclusions, stated goals.
2. Tag every item with its source location (file + section/heading).
3. Collect contradictions and gaps as candidate open questions.
4. Check terms against `glossary.md`; new terms → glossary candidates.

## Stage 2 — Propose hierarchy (NO artifact files)

1. Map items onto the existing domain map (`domains/structure.yaml`). If items do not fit,
   propose new domains/sub-domains explicitly — do not shoehorn.
2. Build the proposed tree: domain → epic → feature → story (titles + one-line summaries only),
   respecting the mandatory chain and vision linkage (which vision goal each epic serves).
3. Write the proposal to `inbox/<input-name>.proposal.yaml`:
   ```yaml
   source: <input file>
   unmapped: [...]          # items you could not place — never drop them
   open_questions: [...]
   new_domains: [...]       # if any
   tree:
     - domain: authentication
       epics:
         - title: ...
           vision_goal: VIS-001/G2
           features:
             - title: ...
               stories: [ {title: ..., source: "brd.md#section-3"} ]
   ```
4. Present a readable summary tree in chat: counts, new-domain proposals, open questions, unmapped items.
   Compute the counts (epics/features/stories/total) **from `*.proposal.yaml`** — never hand-count;
   the chat summary and the gate file must come from the same source.

**⛔ STOP — the owner reviews (and may edit `*.proposal.yaml` directly). Proceed only on explicit
confirmation. If the owner edits the file, re-read it and use the edited version. Owner may ask
for per-domain gating — then repeat this gate per domain.**

## Stage 3 — Draft artifacts

For each confirmed node, in hierarchy order (epics → features → stories):

1. Create from `templates/<type>_template.md`; assign IDs per NAMING; `status: draft`.
   Slug: a meaningful kebab-case phrase (≤ 8 words) — drop filler words; never truncate
   mid-phrase into fragments like `...-e-g`. Rephrase, don't chop.
2. Fill binding sections ONLY from the input. `source` = input **filename + section anchor**
   (e.g. `brd.docx (§4.2)`) — filename, not path, so archiving doesn't break provenance.
   Story statement (As a / I want / So that) must be **rephrased in natural language** —
   never a copy of the artifact title. If the input gives no real user value, write
   `So that: TBD` + an `open_questions` entry — never filler like "to get the value
   described in the source document" (a pointer is not a value).
   Missing info → `TBD` marker + `open_questions` entry. Empty ACs are legal in draft;
   invented ACs are a contract violation.
3. Leave "For implementers" empty unless the owner asked for codebase review.
4. Add new agreed terms to `glossary.md`.

## Stage 4 — Validate & report

1. Run `scripts/validate`; fix what it reports.
2. Report: tree of created files (with counts per type), all open questions grouped by artifact,
   unmapped leftovers, glossary additions, DoR snapshot (what blocks `ready_for_review`).
3. Archive: move the processed input document and its `*.proposal.yaml` to `inbox/archive/`.
   `inbox/` root holds only unprocessed input.
4. Suggested next step: owner reviews drafts; statuses move per LIFECYCLE (agent may propose
   `ready_for_review` for artifacts passing DoR — report per-item results).
