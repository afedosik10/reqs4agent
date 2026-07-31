---
id: US-FLT-005
type: user_story
status: draft
version: 0.1
last_updated: '2026-07-31'
owner: example.owner
domain: fleet_control
parent_feature: FEATURE-FLT-003
updates: US-FLT-004
depends_on: US-FLT-004
open_questions:
  - "Q-1: Should scheduled ON (preheat at a set time) also be supported, or OFF only? Impacts oven-side scheduler scope."
---

# User story: Bulk OFF warns on active baking and can be scheduled

**Summary:** Change request to US-FLT-004 — turning ovens OFF must warn when a baking program is
active, and OFF can be scheduled for a set time.

---

## Change request

**Updates:** [US-FLT-004](US-FLT-004-user-can-turn-on-off-one-or-many.md) (approved baseline —
not edited; this story carries the delta).

**Reason:** safety review follow-up — operators turning a whole store OFF at closing time must
not silently kill an oven that is still baking; end-of-day OFF is usually known in advance.

---

## Story

**As a** User
**I want** a mid-bake warning before OFF and the ability to schedule OFF for a set time
**So that** I never ruin an active bake, and closing-time shutdown happens without me waiting for it.

---

## Design

No UI designs exist yet — TBD (platform undecided, see VIS-001 open questions).

---

## Acceptance criteria

- [ ] Turning OFF an oven with an active baking program shows a specific warning naming the program and remaining time — in addition to the generic confirmation required by US-FLT-004
- [ ] The user can override the warning per oven or exclude such ovens from the bulk action
- [ ] OFF can be scheduled for a set date/time; a scheduled action is visible in the oven list and cancellable until execution
- [ ] Audit log required by US-FLT-004 also records: warning shown/overridden, and scheduled time for scheduled actions

---

## Open questions

- [Q-1: Should scheduled ON (preheat at a set time) also be supported, or OFF only? Impacts oven-side scheduler scope.]

---

## Decisions

- Decision (owner-decided, 2026-07-31): mid-bake warning and scheduled OFF are in scope for the fleet ON/OFF capability; implemented as a CR to the approved baseline, not by editing it.

---

## For implementers

> **Reference only — not a requirement.** Scheduled OFF likely needs oven-side execution (client may be disconnected at the set time) — dev to confirm against NB-touch panel capabilities.

---

## References

- **Parent feature:** [FEATURE-FLT-003](../features/FEATURE-FLT-003-bulk-oven-operations.md)
- **Updates:** [US-FLT-004](US-FLT-004-user-can-turn-on-off-one-or-many.md)
