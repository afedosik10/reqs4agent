---
id: US-FLT-004
type: user_story
status: draft
version: 0.1
last_updated: '2026-07-29'
owner: example.owner
domain: fleet_control
parent_feature: FEATURE-FLT-003
source: inbox/vision-scope-document.docx (4.2 Users Goals)
---

# User story: User can turn ON/OFF one or many ovens remotely

**Summary:** User can turn ON/OFF one or many ovens remotely (extracted from 4.2 Users Goals).

---

## Story

**As a** User
**I want** turn ON/OFF one or many ovens remotely
**So that** I can power-manage my whole fleet from one place, without walking oven to oven.

---

## Design

No UI designs exist yet — TBD (platform undecided, see VIS-001 open questions).

---

## Acceptance criteria

- [ ] Remote ON/OFF works only for ovens with oven-side 'remote enabled' mode active
- [ ] Every ON/OFF action requires an explicit confirmation dialog naming the affected ovens
- [ ] Every ON/OFF action is written to an audit log (who, which ovens, when, result)

---

## Decisions

- Decision (agent-recommended, owner-accepted 2026-07-29): liability addressed via oven-side enable + confirmation + audit log; client responsibility fixed in license agreement.

---

## For implementers

> **Reference only — not a requirement.** No relevant reference found — nothing to suggest; dev to define implementation.

---

## References

- **Parent feature:** [FEATURE-FLT-003](../features/FEATURE-FLT-003-bulk-oven-operations.md)
- **Source:** inbox/vision-scope-document.docx (4.2 Users Goals)
