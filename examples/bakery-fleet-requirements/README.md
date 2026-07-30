# Example: OvenLink — fleet control & statistics

A complete worked R4A example, from raw input to a validated requirements repo.

**OvenLink** is a fictional fleet control & statistics product by **Northbake AB**, a fictional
bakery-oven manufacturer. It was produced by actually running `playbooks/bootstrap.md` and
`playbooks/ingest.md` on a real (2014) discovery-phase Vision & Scope document, then **fully
anonymized** — all company, product, partner, and person names are fictional.

## Input → Output

| | |
|---|---|
| **Input** | `input/vision-scope-document.docx` — the actual Vision & Scope document (2014, v0.1), fully anonymized (fictional company/product/supplier/person names; embedded figures removed). Exactly what a user would drop into `inbox/`. |
| **Output** | `output/` — a validated R4A requirements tree: 1 vision, 7 domains, 7 epics, 17 features, 18 stories + glossary. |

## What to look at

- `output/vision/VIS-001-ovenlink.md` — typed vision with goals G1–G4, honest `TBD` metrics, and
  open questions in the `Q-<N>` format (frontmatter list = SSOT, mirrored in the body section)
- `output/domains/` — every artifact carries a `source:` trace back to a section of the input
- `output/domains/fleet_control/stories/US-FLT-004-*` — decision-record pattern: safety gating
  for remote oven ON/OFF

## Verify it yourself

From the repository root:

```bash
python scripts/validate.py examples/bakery-fleet-requirements/output
# → validate: 0 error(s), 0 warning(s)
```

## Why the drafts are thin

Many fields are `TBD` — the source was scope-level. That is the contract working as designed:
gaps become open questions, never invented content. Open the input docx next to the vision and
check for yourself: every gap the source left open shows up as an open question, not as invented
detail.
