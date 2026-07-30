---
# R4A epic template. Contract: core/contract/CONTRACT.md · IDs: NAMING.md · statuses: LIFECYCLE.md · ready bar: DOR.md
# id: pure ID, no slug (EPIC-<DOMAIN>-<NNN>). <DOMAIN> = code from domains/structure.yaml. Slug goes in the filename only.
id: EPIC-{DOMAIN}-{NNN}
type: epic
# status: draft | ready_for_review | approved | in_progress | implemented | postponed | deprecated (LIFECYCLE.md)
status: draft
version: 0.1
# last_updated: ISO date, bump on every content change
last_updated:
# owner: accountable human (not an agent)
owner:
# domain / sub_domain: must match the file path under domains/
domain:
# sub_domain:            # only for domains with sub-domains
# parent_vision: REQUIRED — the vision this epic implements (VIS-<NNN>)
parent_vision: VIS-{NNN}
# release: target release(s), string or list; synced with releases/<version>.yaml
# release: "1.0"
# external_id: Jira/ADO/etc. reference(s)
# depends_on / see_also: related artifact IDs (single or list)
# open_questions: SSOT for unresolved points — each entry carries a local ID (Q-1, Q-2, …),
# unique within this artifact, never reused; the Open questions section mirrors this list
# open_questions:
#   - "Q-1: Question that must be answered before approval"
---

# Epic: [Epic title in sentence case]

<!-- One-line summary used whenever this epic is referenced. -->
**Summary:** [One sentence: what this epic delivers and for whom.]

---

## Business context

**Why this epic:** [2–3 sentences: the problem/opportunity.]

**Vision goals served:** [Reference SPECIFIC goals from the parent vision, e.g. "VIS-001 → goal 'Unified platform'". Not just a link to the vision file — DoR requires named goals.]

**Target users:** [Roles from the vision's target audience.]

---

## Goals & success criteria

| Goal | Success criterion (measurable at epic level) |
|------|-----------------------------------------------|
| [Goal 1] | [Measurable outcome — not a copy of story ACs] |

---

## Scope

### In scope

- [Capability or outcome]

### Out of scope

- [Explicit exclusion — child features/stories inherit this as binding]

---

## Features (children)

<!-- Maintained as features are created; generated indexes may automate this. -->

| ID | Feature | Status |
|----|---------|--------|
| FEATURE-{DOMAIN}-{NNN} | [Feature name](../features/FEATURE-{DOMAIN}-{NNN}-slug.md) | draft |

---

## Open questions & risks

<!-- SSOT for open questions is the frontmatter `open_questions` list (Q-<N> entries); mirror them
     here with owner/context — never edit this section independently; validate checks the mirror. -->

| Type | Item | Owner |
|------|------|-------|
| Question | [Q-1: Open question] | |
| Risk | [Risk and mitigation] | |

---

## Decisions

<!-- Optional. Every resolved open question lands here as a decision record with provenance:
     "Decision (owner-decided | agent-recommended, owner-accepted, YYYY-MM-DD): Q-<N> — <what was decided>".
     An open question may only leave `open_questions` when a record referencing its Q-ID appears here. -->

- [Decision record — or remove this section if no decisions yet]

---

## References

- **Vision:** [VIS-{NNN} title](../../../vision/VIS-{NNN}-slug.md)
- **Glossary:** [glossary.md](../../../glossary.md)
