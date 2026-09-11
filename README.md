# R4A requirements repo — `<your product>`

[![validate](https://github.com/afedosik10/reqs4agent/actions/workflows/validate.yml/badge.svg)](https://github.com/afedosik10/reqs4agent/actions/workflows/validate.yml)

> **One repo, two teams — humans and AI agents.**

R4A turns a pile of business documents into a structured, git-native requirements repo that both your team and your AI agents work from — the same files, the same rules.

This repository was created from the [R4A](https://github.com/afedosik10/reqs4agent) template. It is **your product's single source of truth** for requirements: vision → domains → epics → features → stories, every artifact Markdown + YAML with a stable ID, status, parent link, and source reference.

## See it in action

Not sure what the output looks like? **[examples/bakery-fleet-requirements](examples/bakery-fleet-requirements/)** is a complete worked case: a real discovery-phase Vision & Scope document (anonymized) went in — a validated requirements tree came out: 1 vision, 7 domains, 7 epics, 17 features, 19 stories, every artifact traced to its source section. A good way to calibrate expectations before your first ingest. (You can delete `examples/` from your own repo once you're comfortable.)

Note what the case proves: the first pass gives you a **validated skeleton** — vision, domain map, the full tree with source traces — while details missing from the source become open questions, never invented content. Detailing happens later, through the maintain playbook, as you answer those questions.

## Why R4A — measured, not promised

Every requirements framework claims *"the agent won't invent facts and will follow the rules"*. Most ask you to trust the prose. R4A is built **Eval-Driven**: those claims are metrics with hard gates in CI, not adjectives in a README.

| | Prose-only frameworks | R4A |
|--|-----------------------|-----|
| Quality claim | "the agent follows the contract" — trust us | gated metrics: no-invention, traceability, coverage, human-gate compliance, schema validity |
| Proof of the claim | README adjectives | scores reported with N and 95% confidence intervals; run log is append-only |
| Framework updates | silent quality drift | release **blocked in CI** if any metric drops > 2 pp vs the last released score |
| "Prove it on **my** history" | — | turn your own requirements git-history into a golden dataset and measure R4A against **your** conventions, before adopting |

**Current measured status** — public benchmark `examples/bakery-fleet-requirements` (golden v1.0, latest run 2026-08-31, grade-only harness smoke, self-judged — method caveats apply):

| Metric | Gate | Latest | Status |
|--------|------|--------|--------|
| schema validity | 1.000 | 1.000 | ✅ |
| human-gate compliance | 1.000 | 1.000 | ✅ |
| traceability precision | ≥ 0.90 | 0.977 (n=43) | ✅ |
| coverage recall | ≥ 0.80 | 0.977 (n=44) | ✅ |
| no-invention rate | 1.000 | 0.953 (n=43) | ❌ below gate |

Yes, we publish the row that **misses** its own gate — that's the point of measuring. The two flagged artifacts (2 of 43) contained facts absent from the source document; the fix lands before the next release tag, and the score updates here.

## Get started

1. **Clone** this repo and open it in any agent tool (see "Works with" below).
2. **Install validator dependencies** (once): `pip install -r requirements.txt` (Python 3.10+).
3. **Bootstrap** — tell the agent: *"execute `playbooks/bootstrap.md`"*. A guided dialog produces your domain map, vision, and glossary. You confirm the map before anything is written.
4. **Ingest** — drop business documents (BRD, notes, transcripts) into `inbox/` and say: *"execute `playbooks/ingest.md`"*. The agent extracts a hierarchy, **stops for your confirmation**, then drafts artifacts. Gaps become open questions — never invented content.
5. **Live** — day-to-day changes via `playbooks/maintain.md`; run `scripts/validate.py` (CI-friendly) on every change; cut releases via `releases/*.yaml`.

## Rules of the house (short version)

- Agents draft and propose; **only humans approve** (`status: approved` is human-only).
- Open questions live in frontmatter with local IDs (`Q-1: …`) and are mirrored in the artifact body; resolving one requires a recorded **decision** with provenance.
- Binding sections are filled from sourced facts only — `TBD` is legal, invention is a contract violation.
- Full contract: `docs/CONTRACT.md`. Agent rules: `AGENTS.md` (picked up automatically by most tools).

## Works with

Any tool whose agent reads files — via the `AGENTS.md` standard and plain-Markdown playbooks.

| Tool | Usage |
|------|-------|
| Claude Code / Cowork | Open the repo; ask to execute a playbook |
| Cursor | `AGENTS.md` is picked up automatically; same ask |
| GitHub Copilot | Same — AGENTS.md support is native |
| Codex / Jules / Windsurf / Zed / Kimi / others | Same pattern |

## Layout

```
domains/     your requirements tree (structure.yaml is the domain map SSOT)
vision/      vision & roadmap artifacts
playbooks/   bootstrap · ingest · maintain — agent procedures with human gates
templates/   artifact templates (self-documenting)
scripts/     validate.py + frontmatter schemas
docs/        the contract (CONTRACT.md)
inbox/       business input awaiting ingest (archive/ holds processed input)
releases/    release manifests
examples/    worked end-to-end cases (input → output); safe to delete
```

## License

MIT © Anatolii Fedosik
