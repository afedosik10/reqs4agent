---
# R4A vision template (FR-CON-012). The traceability ROOT: epics and roadmaps point here via parent_vision.
# id: pure ID (VIS-<NNN>), repo-global sequence. One vision per product stream; multiple visions per repo allowed.
id: VIS-{NNN}
type: vision
status: draft
version: 0.1
last_updated:
owner:
# see_also: ROADMAP-{NNN} (execution roadmap), VIS-{NNN} (parent vision if this is a sub-stream)
# open_questions: SSOT for unresolved points — each entry carries a local ID (Q-1, Q-2, …),
# unique within this artifact, never reused; the Assumptions/open questions section mirrors this list
# open_questions:
#   - "Q-1: Question that must be answered before approval"
---

# Vision: [Product / stream name]

**Summary:** [One sentence: strategic direction and what success looks like.]

---

## Problem & context

[2–3 sentences: the opportunity, why now. If this is a sub-stream, name the parent vision and how this stream fits.]

---

## Target audience

| Segment | Primary need |
|---------|--------------|
| [Role] | [What they need most] |

**Key pains addressed:** [Pain 1]; [Pain 2].

---

## Vision statement

[One clear sentence or short paragraph: desired end state and primary value.]

---

## Strategic goals

<!-- The section epics bind to. Each goal gets a stable anchor id (G1, G2, …) —
     epics reference "VIS-{NNN} → G2", DoR checks the reference is specific. -->

| # | Goal | Success metric (measurable, with horizon) |
|---|------|-------------------------------------------|
| G1 | [Goal] | [Metric] |
| G2 | [Goal] | [Metric] |

---

## Unique value proposition

- **[Theme]:** [Differentiator vs alternatives.]

---

## Guiding principles

- **[Principle]:** [Short explanation.]

---

## Future state (1–2 years out)

[Present-tense narrative of the achieved vision: "A user opens the product and…"]

---

## Out of scope

- [What this vision deliberately does not pursue]

---

## Assumptions, open questions & risks

<!-- SSOT for open questions is the frontmatter `open_questions` list (Q-<N> entries); mirror them
     here with owner/context — never edit this section independently; validate checks the mirror. -->

| Type | Item | Owner |
|------|------|-------|
| Assumption | [Assumption] | |
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

- **Roadmap:** [ROADMAP-{NNN}](ROADMAP-{NNN}-slug.md)
- **Epics implementing this vision:** use `parent_vision: VIS-{NNN}` (find them by frontmatter search or generated index)
