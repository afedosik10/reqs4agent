---
# R4A user story template. Contract: core/contract/CONTRACT.md · IDs: NAMING.md · statuses: LIFECYCLE.md · ready bar: DOR.md
# id: pure ID, no slug (US-<DOMAIN>-<NNN>). Slug goes in the filename only.
id: US-{DOMAIN}-{NNN}
type: user_story
status: draft
version: 0.1
last_updated:
owner:
domain:
# sub_domain:
# parent_feature: REQUIRED — every story belongs to a feature
parent_feature: FEATURE-{DOMAIN}-{NNN}
# release: "1.0"
# external_id: Jira/ADO id, e.g. PROJ-12345
# depends_on: US-... (story this one relies on: workflow, spec)
# see_also: US-... (same UX/spec/context — implementers should read it)
# updates: US-... (if this story is a change request to an implemented story)
# updated_by: US-... (filled on the original when a CR exists)
# source: path/ref to the ingested business input (set by ingest playbook)
# open_questions: SSOT for unresolved points — each entry carries a local ID (Q-1, Q-2, …),
# unique within this artifact, never reused; the Open questions section mirrors this list
# open_questions:
#   - "Q-1: Unresolved point — never silently resolved by an agent"
# verified_by: []     # RESERVED v2 — test case refs
# documented_in: []   # RESERVED v2 — user doc refs
---

# User story: [Story title in sentence case]

**Summary:** [One sentence: the user action and outcome.]

---

## Story

<!-- BINDING -->

**As a** [role from the product]
**I want** [capability or action]
**So that** [benefit or goal].

---

## Design

<!-- BINDING where the story has UI. One link per screen/state. If no UI, write "No UI — not applicable". -->

| Description | Link |
|-------------|------|
| [Screen / state / variant] | [Design link] |

---

## Acceptance criteria

<!-- BINDING. Testable, specific to this story; cover happy path and key error paths.
     Use Gherkin scenarios where behavior is stateful. -->

- [ ] [Criterion 1]
- [ ] [Criterion 2]

---

## Open questions

<!-- SSOT is frontmatter `open_questions` (Q-<N> entries); mirror them here with context — never edit
     this section independently; validate checks the mirror. Blocking ones keep the story in draft. -->

- [Q-1: Question — what's needed to resolve it]

---

## Decisions

<!-- Optional. Every resolved open question lands here as a decision record with provenance:
     "Decision (owner-decided | agent-recommended, owner-accepted, YYYY-MM-DD): Q-<N> — <what was decided>".
     An open question may only leave `open_questions` when a record referencing its Q-ID appears here. -->

- [Decision record — or remove this section if no decisions yet]

---

## For implementers

> **Reference only — not a requirement.**
> Optional context for developers, QA automation, and AI tools. Content here is a **best-effort pointer**
> to existing code or systems — **not** a technical design, API contract, or implementation mandate.
>
> **What is binding:** [Story](#story), [Acceptance criteria](#acceptance-criteria), [Design](#design),
> and **Out of scope** on the parent feature.
> **Who owns implementation:** the development team. Errors or omissions in this section are **not**
> acceptance defects against the author.
> **If nothing useful was found:** say so explicitly — e.g. *No relevant reference found — nothing to
> suggest; dev to define implementation.* That is a valid outcome; **never invent paths or APIs.**

**Observations (non-binding):**

- [Sourced observation with tentative language ("likely", "dev to confirm") — or the explicit "nothing found" statement above]

---

## References

- **Parent feature:** [FEATURE-{DOMAIN}-{NNN} title](../features/FEATURE-{DOMAIN}-{NNN}-slug.md)
- **Glossary:** [glossary.md](../../../glossary.md)
