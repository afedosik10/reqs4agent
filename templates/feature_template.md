---
# R4A feature template. Contract: core/contract/CONTRACT.md · IDs: NAMING.md · statuses: LIFECYCLE.md · ready bar: DOR.md
# id: pure ID, no slug (FEATURE-<DOMAIN>-<NNN>). Slug goes in the filename only.
id: FEATURE-{DOMAIN}-{NNN}
type: feature
status: draft
version: 0.1
last_updated:
owner:
domain:
# sub_domain:
# parent_epic: REQUIRED — every feature belongs to an epic
parent_epic: EPIC-{DOMAIN}-{NNN}
# release: "1.0"
# external_id:
# depends_on / see_also / updates / updated_by: artifact IDs
# open_questions: SSOT for unresolved points — each entry carries a local ID (Q-1, Q-2, …),
# unique within this artifact, never reused; the Open questions section mirrors this list
# open_questions:
#   - "Q-1: Question that must be answered before approval"
---

# Feature: [Feature title in sentence case]

**Summary:** [One sentence: what this feature delivers and the main user value.]

---

## Description

[What the feature does and why — user-visible behavior and business rationale.
No implementation prescriptions: the how belongs to the dev team.]

---

## Acceptance criteria

<!-- BINDING. Feature-level: complete, testable, no overlap with child stories' ACs. -->

- [ ] [Criterion 1]
- [ ] [Criterion 2]

---

## Out of scope

<!-- BINDING for this feature AND for its child stories ("parent Out of scope"). -->

- [Explicit exclusion]

---

## Stories (children)

| ID | Story | Status |
|----|-------|--------|
| US-{DOMAIN}-{NNN} | [Story name](../stories/US-{DOMAIN}-{NNN}-slug.md) | draft |

---

## Open questions

<!-- SSOT is frontmatter `open_questions` (Q-<N> entries); mirror them here with context — never edit
     this section independently; validate checks the mirror. Blocking ones keep the feature in draft. -->

- [Q-1: Question — what's needed to resolve it]

---

## Decisions

<!-- Optional. Every resolved open question lands here as a decision record with provenance:
     "Decision (owner-decided | agent-recommended, owner-accepted, YYYY-MM-DD): Q-<N> — <what was decided>".
     An open question may only leave `open_questions` when a record referencing its Q-ID appears here. -->

- [Decision record — or remove this section if no decisions yet]

---

## References

- **Parent epic:** [EPIC-{DOMAIN}-{NNN} title](../epics/EPIC-{DOMAIN}-{NNN}-slug.md)
- **Glossary:** [glossary.md](../../../glossary.md)
