# R4A requirements repo — `<your product>`

> **One repo, two teams — humans and AI agents.**

R4A turns a pile of business documents into a structured, git-native requirements repo that both your team and your AI agents work from — the same files, the same rules.

This repository was created from the [R4A](https://github.com/afedosik10/reqs4agent) template. It is **your product's single source of truth** for requirements: vision → domains → epics → features → stories, every artifact Markdown + YAML with a stable ID, status, parent link, and source reference.

## Get started

1. **Clone** this repo and open it in any agent tool (see "Works with" below).
2. **Bootstrap** — tell the agent: *"execute `playbooks/bootstrap.md`"*. A guided dialog produces your domain map, vision, and glossary. You confirm the map before anything is written.
3. **Ingest** — drop business documents (BRD, notes, transcripts) into `inbox/` and say: *"execute `playbooks/ingest.md`"*. The agent extracts a hierarchy, **stops for your confirmation**, then drafts artifacts. Gaps become open questions — never invented content.
4. **Live** — day-to-day changes via `playbooks/maintain.md`; run `scripts/validate.py` (CI-friendly) on every change; cut releases via `releases/*.yaml`.

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
```

## License

MIT © Anatolii Fedosik
