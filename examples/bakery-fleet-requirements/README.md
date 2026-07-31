# Example: OvenLink — fleet control & statistics

A complete worked R4A example, from raw input to a validated requirements repo.

**OvenLink** is a fictional fleet control & statistics product by **Northbake AB**, a fictional
bakery-oven manufacturer. It was produced by actually running `playbooks/bootstrap.md` and
`playbooks/ingest.md` on a real (2014) discovery-phase Vision & Scope document, then **fully
anonymized** — all company, product, partner, and person names are fictional.

## Input → Output

| | |
|---|---|
| **Input** | `input/vision-scope-document.docx` — the actual Vision & Scope document (2014, v0.1), fully anonymized (fictional company/product/supplier/person names; embedded figures blanked — they showed real branding). Exactly what a user would drop into `inbox/`. |
| **Output** | `output/` — a validated R4A requirements tree: 1 vision, 7 domains, 7 epics, 17 features, 19 stories + glossary. |

## What to look at

- `output/vision/VIS-001-ovenlink.md` — typed vision with goals G1–G4, honest `TBD` metrics, and
  open questions in the `Q-<N>` format (frontmatter list = SSOT, mirrored in the body section)
- `output/domains/` — every artifact carries a `source:` trace back to a section of the input
- `output/domains/fleet_control/stories/US-FLT-004-*` — decision-record pattern: safety gating
  for remote oven ON/OFF
- `output/domains/fleet_control/stories/US-FLT-005-*` — **change request pattern**: the approved
  baseline (US-FLT-004) is never edited; the delta arrives as a new story linked both ways
  (`updates` / `updated_by`). The "current spec" = baseline + CR chain

## Verify it yourself

From the repository root:

```bash
python scripts/validate.py examples/bakery-fleet-requirements/output
# → validate: 0 error(s), 0 warning(s)
```

## The first deliverable is a skeleton — and that is the point

One ingest pass does not produce "finished requirements". It produces a **validated skeleton**:
a typed vision with goals, a 7-domain map, and a complete epic/feature/story tree with stable
IDs and source traces. Building that by hand takes days; here it is one agent run plus a human
review gate. The tree then grows through the maintain playbook as open questions get answered.

Many fields are `TBD` — the source was scope-level. That is the contract working as designed:
gaps become open questions, never invented content. Open the input docx next to the vision and
check for yourself: every gap the source left open shows up as an open question, not as invented
detail.
