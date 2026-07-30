# Playbook: maintain

> Agent procedure for day-to-day work in an R4A repo. Spec: FR-MNT-001..003.
> Read `AGENTS.md` first. Statuses: LIFECYCLE.md. Ready bar: DOR.md.
> After ANY operation below: run `scripts/validate` before committing.

## Add an artifact

1. Confirm the parent exists (story→feature→epic→vision chain) — create parents first if missing,
   each through its own template.
2. Copy from `templates/<type>_template.md`, assign next free ID (NAMING §5), `status: draft`.
3. Fill binding sections from sourced facts; gaps → `open_questions`.
4. Update the parent's children table.

## Propose ready_for_review

1. Run the DOR checklist for the type; report item-by-item.
2. All pass → set `status: ready_for_review`, bump `version`, set `last_updated`.
3. Any fail → stay `draft`; report what is missing. Never weaken a checklist item.

## Change request (CR) to an approved/implemented artifact

1. Never edit binding content of an `approved`/`implemented` artifact directly (typos/links are OK).
2. Create a new story from the template with `updates: <original-id>`; describe the delta.
3. Add `updated_by: <cr-id>` to the original.
4. The CR walks the normal lifecycle from `draft`.

## Resolve an open question

1. Resolution requires a human decision — the owner decides, or accepts your recommendation.
2. Record it in the artifact's **Decisions** section with provenance:
   `Decision (owner-decided | agent-recommended, owner-accepted, YYYY-MM-DD): Q-<N> — <decision>`.
3. Only then remove the entry from `open_questions`; reflect the decision in binding sections
   (ACs etc.) in the same commit.
4. Sweep the body for other mentions of the Q-ID (risk tables, goals, cross-references):
   rephrase them without the Q-token or point to the Decisions section. Once the entry leaves
   frontmatter, `validate` fails on that Q-ID anywhere in the Open questions section — sweep
   first, don't let CI catch it.

## Link / relink

- `depends_on` — this artifact relies on another (workflow, spec). `see_also` — helpful context.
- Both must resolve; prefer linking stories within the same feature scope; cross-domain links are
  fine but check the domain map first — frequent cross-domain dependencies may signal a wrong split.

## Move an artifact

- **Within a domain (sub-domain change):** move the file, update `sub_domain`, fix the parent's
  children table and inbound links. ID unchanged.
- **Across domains:** requires owner confirmation. Reissue the ID under the new domain code
  (NAMING §4), retire the old one via `updates`, fix all inbound references.

## Structural changes (domains / sub-domains)

1. Owner confirmation required.
2. Update `domains/structure.yaml` AND the folder tree in the same commit; new domains need a code.
3. Run validate; fix the report.

## Status sync from a release

- Only on explicit owner instruction, with the release manifest as evidence:
  set listed stories/features/epics to the instructed status, bump `version`/`last_updated`.
- Report every change made; never touch artifacts outside the manifest.

## Renames

- Title change → slug may change: rename file, fix ALL inbound links in the same commit. ID never changes.
