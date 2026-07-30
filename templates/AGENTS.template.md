# [Product] requirements — agent instructions

<!-- Placed at the repo root by bootstrap. Governs ALL agents working in this requirements repo.
     Rendered from R4A core; profile installs may append sections below the marker at the end. -->

This is an **R4A requirements repository** (Markdown + YAML). Humans and AI agents work on the
same files under the same contract. Read this file fully before creating or editing anything.

## The contract

| Question | Answer |
|----------|--------|
| Layout, fields, binding rules | [core CONTRACT](templates/../docs/CONTRACT.md) — local copy installed by bootstrap |
| IDs & filenames | NAMING rules — pure IDs (`US-<DOMAIN>-<NNN>`), slug only in filename |
| Statuses & who may change them | LIFECYCLE rules — see the transition table |
| When an artifact is ready | DOR checklist per artifact type |
| Domain map & ID codes | `domains/structure.yaml` — the only authority |

## Creating artifacts

1. Always start from `templates/<type>_template.md`; never freehand a file.
2. Assign the next free ID per NAMING (scan existing files first).
3. Fill **binding** sections from sourced facts only. Missing information → `open_questions`
   entry + `TBD` marker; **never invent** requirements, ACs, endpoints, or design links.
4. "For implementers" is **non-binding, optional**: sourced observations with tentative language,
   or an explicit "no relevant reference found". Never treat it as requirements.
5. Run the DOR checklist; report results item by item before proposing `ready_for_review`.

## Hard rules (no exceptions)

- **Never set `status: approved`** — that transition is human-only.
- **Never bulk-create artifacts without a confirmed hierarchy** — ingest goes through its
  human gate first (`playbooks/ingest.md`).
- **Never weaken a DoR item's wording to pass it.**
- **Never resolve an open question silently** — resolution requires a human decision recorded
  in the artifact's **Decisions** section with provenance
  (`Decision (owner-decided | agent-recommended, owner-accepted, YYYY-MM-DD): …`).
- Structural changes (domains, sub-domains) must update `domains/structure.yaml` and the folder
  tree together, then pass `scripts/validate`.

## Workflows

- New repo setup: `playbooks/bootstrap.md`
- Business input → draft backlog: `playbooks/ingest.md`
- Everything else (add, link, move, CRs, statuses): `playbooks/maintain.md`
- Before any commit: run `scripts/validate` and fix what it reports.

## Key paths

- Glossary: `glossary.md` — use its terms; add new terms there first
- Vision & roadmaps: `vision/`
- Release manifests: `releases/`
- Raw input awaiting ingest: `inbox/`

<!-- PROFILE SECTIONS BELOW — installed profiles append here; do not edit manually above this line as an agent. -->
