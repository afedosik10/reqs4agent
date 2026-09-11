# R4A · Reqs4Agent

> **One repo, two teams — humans and AI agents.**

R4A turns messy business documents into a clean, git-based requirements repository — one that your team **and** your AI agents can both work from. Same files, same rules, no translation layer in between.

**Status:** pre-release · **License:** MIT · **Works with:** Claude Code, Cursor, Copilot, Kimi, Codex, and any agent that can read files.

---

## The problem we solve

Your product knowledge lives in BRDs, call notes, and chat threads. Your AI coding agent knows none of it — so every session starts with re-explaining your product. Wiki pages go stale. Specs drift away from reality.

R4A fixes the missing step *before* coding: it turns business chaos into a living requirements repo — vision → domains → epics → features → user stories — that stays true because both humans and agents follow the same written contract.

```
messy docs  →  R4A  →  structured requirements repo  →  your agents finally understand your product
```

## Easy to start. Seriously.

**1.** Create your repo from this template (one click).
**2.** Drop your documents into `inbox/`.
**3.** Tell your agent: *"execute `playbooks/ingest.md`"*.

That's it. The agent reads your docs, proposes a requirements hierarchy, and **stops to ask for your confirmation** before writing anything. Missing details become open questions — never invented facts. No new tool to learn, no UI, no SaaS account. If your agent can read files, it can run R4A.

## See the result before you start

**[examples/bakery-fleet-requirements](examples/bakery-fleet-requirements/)** is a complete real case: one Vision & Scope document in — a validated requirements tree out (1 vision, 7 domains, 7 epics, 17 features, 19 stories), every artifact linked back to its source section. Two minutes of reading tells you exactly what to expect.

## Why R4A is different

**1. It feeds your coding agents.** Tools like Spec Kit or OpenSpec turn specs into code — but they need a good spec first. R4A creates that spec from your messy business documents. It covers the step *before* them, the one nobody else does.

**2. Humans stay in charge.** Agents draft and propose; only humans approve. Every change goes through a visible gate. `status: approved` is human-only — by contract, enforced in CI.

**3. Measured, not promised.** Every framework claims *"the agent won't invent facts"*. We turned that claim into numbers with hard CI gates — and we publish them, including the misses:

| Metric | Gate | Latest run (2026-08-31)* | Status |
|--------|------|--------------------------|--------|
| schema validity | 100% | 100% | ✅ |
| human-gate compliance | 100% | 100% | ✅ |
| traceability precision | ≥ 90% | 97.7% (n=43) | ✅ |
| coverage recall | ≥ 80% | 97.7% (n=44) | ✅ |
| no-invention rate | 100% | 95.3% (n=43) | ❌ below gate |

*Harness smoke run, self-judged — method notes apply. We show the failing row on purpose: that's what "measured" means. The two flagged artifacts (of 43) contained facts absent from the source document; the fix ships before the next release tag.

Framework updates are regression-gated: if any metric drops more than 2 points, the release is blocked. Quality can't silently degrade.

**4. Prove it on *your* history.** Skeptical? If you already have a requirements repo, its git history can be turned into a test set — so you measure R4A against *your* conventions before you adopt it. No other prose-based framework can offer that, because they have nothing to measure with.

## What's inside

```
domains/     your requirements tree (the source of truth)
vision/      vision & roadmap
playbooks/   bootstrap · ingest · maintain — agent procedures with human gates
templates/   self-documenting artifact templates
scripts/     validate.py — CI-friendly checks of the whole tree
docs/        the contract both teams follow
inbox/       business input waiting for ingest
examples/    worked end-to-end cases (safe to delete)
```

## Principles

1. **One repo, two teams** — no drift between "docs for people" and "context for AI".
2. **Contract in files, not in prompts** — rules survive tool changes.
3. **Gated, not generated** — agents never bulk-write; humans hold the gate.
4. **Gaps become questions, never inventions.**
5. **Quality is a number with a gate** — not an adjective.

## What R4A is not

Not a code generator. Not a project-management tool. Not another prompt collection. It is the structured requirements layer your agentic workflow is missing.

## License

MIT © Anatolii Fedosik
