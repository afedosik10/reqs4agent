# R4A Core Contract

> The single entry point to the R4A filesystem contract. If a rule here conflicts with another doc, the framework spec (maintainer-local, not published) wins, then this file, then the detail docs it links.
> Binding for humans and agents. Machine-checked by `core/scripts/validate.py`.

## 1. What the contract is

R4A defines **how a requirements repo is laid out and what every file must contain**, so that humans and AI agents read and maintain the same files under the same rules. The contract is the framework; playbooks and skills are just ways to execute it.

## 2. Repo layout

```
<product>-requirements/
├── AGENTS.md                  # agent rules for THIS repo (from core/templates/AGENTS.template.md)
├── glossary.md                # product terms; single source for naming things
├── _index.md                  # generated navigation (script-maintained)
├── vision/
│   ├── VIS-*.md               # one or more visions (per product stream)
│   └── ROADMAP-*.md           # roadmaps, each linked to its vision
├── domains/
│   ├── structure.yaml         # machine-readable SSOT of the domain map
│   └── <domain>[/<sub_domain>]/
│       ├── epics/
│       ├── features/
│       └── stories/
├── releases/<version>.yaml    # release manifests (script-syncable)
├── inbox/                     # raw business input awaiting ingest (not part of the tree)
├── templates/                 # artifact templates (copied from core at bootstrap)
├── playbooks/                 # bootstrap / ingest / maintain procedures
├── scripts/                   # validate + repo utilities
└── docs/                      # free-form supporting material (non-contractual)
```

- `domains/structure.yaml` is the **only authority** on which domains and sub-domains exist and which ID `code` each domain owns. Human-readable overviews may summarize it, never override it.
- `inbox/` and `docs/` are the two deliberately free-form zones; everything else is typed.

## 3. Hierarchy & traceability

```
VIS-*  ←  ROADMAP-*
  ↑
EPIC-*  ←  FEATURE-*  ←  US-*
```

- Mandatory chain: every **story** has `parent_feature`; every **feature** has `parent_epic`; every **epic** has `parent_vision` and belongs to a domain (or sub-domain). Every **roadmap** has `parent_vision`.
- Single-epic domains are valid — never split an epic artificially to satisfy structure.
- Cross-links: `depends_on`, `see_also`; change requests: `updates` / `updated_by` (see LIFECYCLE.md §3).
- Reserved for v2 downstream traceability: `verified_by` (test cases), `documented_in` (user docs). Schema-valid now, resolved by tooling later.

## 4. Frontmatter

Every artifact is a Markdown file with YAML frontmatter. Full schemas: `core/schemas/`.

| Field | Req? | Applies to | Notes |
|-------|:----:|-----------|-------|
| `id` | ✔ | all | See NAMING.md; identity, never changes |
| `type` | ✔ | all | `vision from roadmap epic feature user_story` |
| `status` | ✔ | all | See LIFECYCLE.md |
| `version` | ✔ | all | Bumped on content change |
| `last_updated` | ✔ | all | ISO date |
| `owner` | ✔ | all | Accountable human |
| `domain` / `sub_domain` | ✔/opt | epic, feature, story | Must match path |
| `parent_vision` | ✔ | epic, roadmap | Must resolve |
| `parent_epic` | ✔ | feature | Must resolve |
| `parent_feature` | ✔ | story | Must resolve |
| `release` | opt | epic, feature, story | Synced with `releases/*.yaml` |
| `external_id` | opt | all | Jira/ADO/etc. reference |
| `depends_on`, `see_also` | opt | all | ID or list of IDs; must resolve |
| `updates`, `updated_by` | opt | all | Change-request links; must resolve |
| `open_questions` | opt | all | SSOT for unresolved points; each entry `"Q-<N>: …"` (unique, never reused); mirrored by the Open questions section — `validate` checks the mirror |
| `source` | opt | ingest-created | Input **filename + section** (e.g. `brd.docx (§4.2)`) — filename, not path: survives archiving |
| `verified_by`, `documented_in` | opt | story | **Reserved (v2)** |

## 5. Binding vs non-binding (the accountability rule)

| Binding — acceptance-relevant | Non-binding — reference only |
|------------------------------|------------------------------|
| Story statement, Acceptance criteria, Design references, Out of scope (own + parent's) | "For implementers" notes: codebase observations, hints |

- Errors in non-binding sections are **not defects** against the author (BA). Implementers own implementation decisions.
- Templates carry this disclaimer verbatim; agents MUST NOT treat implementer notes as requirements, and MUST NOT invent content to fill them ("no relevant reference found" is a valid entry).

## 5.1 Decision records

Resolving an open question is a governed act, not an edit:

- Every resolution is recorded in the artifact's **Decisions** section with provenance:
  `Decision (owner-decided | agent-recommended, owner-accepted, YYYY-MM-DD): Q-<N> — <decision>`.
- Decision records reference the question's local ID (`Q-<N>`) — the ID is never reused, so the
  link survives renumbering-free edits of the question text.
- An entry may leave `open_questions` only when its decision record exists; binding sections are updated in the same commit.
- Agents may recommend; acceptance is always the owner's. Bulk acceptance ("answer them all as you recommend") is legal but each record still names the provenance.

## 6. The gates (who decides what)

- Agents draft, link, check, and propose (`ready_for_review`). **Only humans approve.** Full transition rules: LIFECYCLE.md §2.
- Ingest never writes artifact files before the human confirms the proposed hierarchy (playbooks/ingest.md).
- DoR (DOR.md) is the shared bar for "ready": same checklist for the human reviewer and the validate script.

## 7. Detail docs

| Doc | Covers |
|-----|--------|
| [NAMING.md](NAMING.md) | ID grammar, filenames, paths, stability rules |
| [LIFECYCLE.md](LIFECYCLE.md) | Statuses, transition permissions, change requests |
| [DOR.md](DOR.md) | Definition of Ready per artifact type |
| [`core/schemas/`](../schemas/) | Machine-checkable frontmatter schemas |
