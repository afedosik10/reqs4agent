---
id: EPIC-FLT-001
type: epic
status: draft
version: 0.1
last_updated: '2026-07-29'
owner: example.owner
domain: fleet_control
parent_vision: VIS-001
source: inbox/vision-scope-document.docx
open_questions:
- "Q-1: Offline/restricted networks: v1 requires internet (owner-accepted decision); VPN
  supported — revisit if offline clients push back"
---

# Epic: Fleet remote control

**Summary:** From 1:1 panel mirror to central control of all client ovens.

---

## Business context

**Why this epic:** From 1:1 panel mirror to central control of all client ovens. Extracted from inbox/vision-scope-document.docx.

**Vision goals served:** VIS-001/G1

**Target users:** see VIS-001 target audience.

---

## Goals & success criteria

| Goal | Success criterion |
|------|-------------------|
| Fleet remote control | - [ ] Design serves both small clients (1-3 ovens) and large clients (100-300 ovens) — source: 5.5 UI Requirements |

---

## Scope

### In scope

- Oven fleet registry and grouping
- Remote panel control of a selected oven
- Bulk oven operations

### Out of scope

- TBD

---

## Features (children)

| ID | Feature | Status |
|----|---------|--------|
| FEATURE-FLT-001 | [Oven fleet registry and grouping](../features/FEATURE-FLT-001-oven-fleet-registry-and-grouping.md) | draft |
| FEATURE-FLT-002 | [Remote panel control of a selected oven](../features/FEATURE-FLT-002-remote-panel-control-of-a-selected-oven.md) | draft |
| FEATURE-FLT-003 | [Bulk oven operations](../features/FEATURE-FLT-003-bulk-oven-operations.md) | draft |

---

## Open questions & risks

| Type | Item | Owner |
|------|------|-------|
| Question | Q-1: Offline/restricted networks — v1 requires internet; VPN supported; revisit if offline clients push back | TBD |

---

## References

- **Vision:** [VIS-001](../../../vision/VIS-001-ovenlink.md)
