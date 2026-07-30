---
id: US-ACC-001
type: user_story
status: draft
version: 0.1
last_updated: '2026-07-29'
owner: example.owner
domain: access_control
parent_feature: FEATURE-ACC-001
source: inbox/vision-scope-document.docx (5.2 item 2)
---

# User story: Client can create roles with different access levels for his staff

**Summary:** Client can create roles with different access levels for his staff (extracted from 5.2 item 2).

---

## Story

**As a** Client (bakery owner)
**I want** create roles with different access levels for his staff
**So that** my people get exactly the access their job needs.2 item 2.

---

## Design

No UI designs exist yet — TBD (platform undecided, see VIS-001 open questions).

---

## Acceptance criteria

- [ ] Predefined role templates: Owner, Store Manager, Baker, Viewer
- [ ] Client can create custom roles from a permission set
- [ ] Role scope can be limited to a store or oven group

---

## Decisions

- Decision (agent-recommended, owner-accepted 2026-07-29): v1 = RBAC with templates + custom roles scoped by store/oven group. Cloud roles are independent from panel pin-roles (pin remains for physical access).

---

## For implementers

> **Reference only — not a requirement.** No relevant reference found — nothing to suggest; dev to define implementation.

---

## References

- **Parent feature:** [FEATURE-ACC-001](../features/FEATURE-ACC-001-custom-roles-and-permissions.md)
- **Source:** inbox/vision-scope-document.docx (5.2 item 2)
