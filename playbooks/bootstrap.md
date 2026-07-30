# Playbook: bootstrap

> Agent procedure for initializing an R4A requirements repo for a product. Spec: FR-BST-001..004.
> Prerequisite: you are in a repo created from the R4A template. Read `AGENTS.md` first.
> Human gates are marked **⛔ STOP**. Never skip them.

## Stage 1 — Elicit (guided dialog)

Ask the owner, in small batches (max 3–4 questions at a time):

1. **Product**: name, one-paragraph description, product streams (one vision per stream).
2. **Domains**: propose 4–8 top-level domain candidates from the description; refine with the owner.
   For each: name (`lower_snake`), description, ID code (2–5 uppercase letters, unique).
3. **Sub-domains**: only where the owner sees clear internal areas; do not force them.
4. **Vision seed**: target audience, key pains, 3–5 strategic goal candidates with rough metrics.

Do not proceed while any domain lacks a description or code.

**⛔ STOP — present the full map (domains, codes, sub-domains, vision skeleton) and get explicit
owner confirmation before writing anything.**

## Stage 2 — Generate

On confirmation, create:

1. `domains/structure.yaml` per `core/schemas/structure.schema.yaml` (codes included).
2. Folder tree: `domains/<domain>[/<sub_domain>]/{epics,features,stories}/` with `.gitkeep`.
3. Root dirs: `vision/`, `releases/`, `inbox/`, `docs/`.
4. `AGENTS.md` at repo root from `templates/AGENTS.template.md` (fill product name).
5. `glossary.md` seeded with terms already agreed in the dialog.
6. `vision/VIS-001-<slug>.md` from the vision template, `status: draft`, filled with Stage-1 seed
   content only — real elicited facts, no invented metrics. One per stream if several.
7. Optionally (owner's choice) ONE worked example per artifact type in a domain the owner picks,
   clearly titled "[EXAMPLE]" and `status: draft`.

Do **not** create any other epics/features/stories — that is ingest's job.

## Stage 3 — Validate & report

1. Run `scripts/validate`; fix structural issues it reports.
2. Report to the owner: created tree, vision file(s), open questions from the dialog, suggested
   next step ("drop business input into `inbox/` and run `playbooks/ingest.md`").
