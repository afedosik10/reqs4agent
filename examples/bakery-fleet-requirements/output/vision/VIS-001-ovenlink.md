---
id: VIS-001
type: vision
status: draft
version: 0.1
last_updated: 2026-07-29
owner: example.owner
open_questions:
  - "Q-1: Success metrics: stakeholders said 'as soon as possible' and 'attractive to customer' — no measurable targets defined. Owner to define per-goal metrics."
  - "Q-2: Liability for remote oven ON/OFF is uninvestigated (safety concern) — who is responsible?"
  - "Q-3: Software licensing model undefined."
  - "Q-4: Clients with offline/restricted networks (no internet, firewalls, VPN): is offline mode in scope?"
  - "Q-5: Voltware AB (fictional supplier) dependency: source code and documentation access is restricted — impact on delivery unknown."
  - "Q-6: Technical platform undecided (web service, iPad, Android tablet) — usability approach depends on it."
---

# Vision: OvenLink — Remote Control & Statistics

**Summary:** Turn single-oven remote control into fleet-wide control and statistics, so Northbake can serve big customers (up to 300 ovens) and stay competitive — selling more ovens on the strength of the software.

---

## Problem & context

Northbake manufactures bakery equipment; every modern oven ships with the NB-touch panel whose legacy Remote Control mirrors one panel to one PC. Big clients run up to 300 ovens across stores: they cannot control them centrally and must update panel software manually via USB on each oven, while competitors already offer multi-oven control. This gap blocks Northbake from serving its largest customers and from market leadership.

---

## Target audience

| Segment | Primary need |
|---------|--------------|
| Customers (bakery/store owners) | Control all their ovens centrally; see production and cost statistics |
| Distributors | Demonstrate and sell Northbake equipment with a modern software story |
| Northbake (service, support, stakeholders) | Service statistics; centralized support of installed base |

**Key pains addressed:** 1:1-only remote control; manual per-oven USB software updates; no fleet statistics.

---

## Vision statement

For customers who need to control their ovens and understand their operations, OvenLink controls the whole fleet remotely and presents statistics per oven and across the fleet — for clients from a single pizzeria to a 300-oven chain.

---

## Strategic goals

| # | Goal | Success metric (measurable, with horizon) |
|---|------|-------------------------------------------|
| G1 | Fleet control: from 1:1 to N ovens per client | TBD (see open questions) |
| G2 | Fleet statistics per oven and aggregated | TBD (see open questions) |
| G3 | Sell more ovens via the product (self-financing: product is free, ovens pay) | TBD (see open questions) |
| G4 | Retain existing clients and attract new ones | TBD (see open questions) |

---

## Unique value proposition

- **Fleet-first:** competitors offer multi-oven control; OvenLink pairs it with statistics across the installed Northbake base.
- **Zero-touch maintenance:** panel software updates delivered centrally instead of USB per oven.

---

## Guiding principles

- **Usability first:** stakeholder-stated focus; platform choice must serve it.
- **Ship small, grow fast:** first version may have a minimal feature list; frequent updates are a stakeholder success criterion.
- **Scales down and up:** same product for 1-oven and 300-oven clients.

---

## Future state (1–2 years out)

A bakery chain owner opens OvenLink and sees every oven in every store: what is baking, energy consumed, which store's production lags and why. She pushes a recipe update to 300 ovens at once; the service department sees failing ovens before the client calls.

---

## Out of scope

- Replacing the NB-touch panel itself or its on-oven UI
- Oven hardware changes (VW-600 board is a given)

---

## Assumptions, open questions & risks

| Type | Item | Owner |
|------|------|-------|
| Assumption | Remote Control base feature (mirror, recipes) keeps working as the foundation | |
| Question | Q-1: No measurable success metrics — owner to define per-goal targets | TBD |
| Question | Q-2: Remote ON/OFF liability (safety) | TBD |
| Question | Q-3: Licensing model | TBD |
| Question | Q-4: Offline/restricted-network clients | TBD |
| Question | Q-6: Technical platform undecided — usability approach depends on it | TBD |
| Risk | Q-5: Voltware source/doc access restriction may block panel-side changes | TBD |
| Risk | Release cadence coupled to Voltware (2×/year) and CEO decision | TBD |

---

## References

- **Source:** `../../input/vision-scope-document.docx` — anonymized Vision & Scope (v0.1, 2014-05-26); the Stage-2 ingest gate artifact is `../../input/vision-scope-document.proposal.yaml`
- **Roadmap:** none yet — create via maintain playbook when planning starts
