#!/usr/bin/env python3
"""R4A validate — contract checker (spec FR-VAL-001..003).

Checks, per artifact file under domains/ and vision/:
  1. YAML frontmatter parses and passes the JSON schema for its type
  2. ID grammar (NAMING.md) and repo-wide ID uniqueness
  3. Filename starts with the ID; slug is kebab-case
  4. Path <-> frontmatter consistency: domain/sub_domain match the path; artifact
     sits in the right folder (epics/features/stories, vision/)
  5. Domain code in the ID matches the code declared in domains/structure.yaml
  6. Parent links resolve: story->feature->epic->vision, roadmap->vision
  7. depends_on / see_also / updates / updated_by targets exist
  8. updates/updated_by reciprocity (warning if one-sided)
  9. open_questions entries carry unique local IDs (Q-<N>); the Open questions
     section in the body mirrors the frontmatter list (FR-CON-014)
 10. story bodies carry no ingest placeholder text ("value described in the source
     document") — warning (ingest playbook: real benefit or TBD + open question)
Repo-level:
 11. structure.yaml passes its schema; domain codes unique; folder tree matches the map
 12. releases/*.yaml pass schema; every listed ID exists; artifacts whose `release`
     names a manifest version are listed in it (warning), and vice versa (error)

Exit codes: 0 clean (warnings allowed), 1 errors found, 2 cannot run.
Usage: python3 validate.py [repo_root]   (default: auto-detect from cwd upwards)
"""
from __future__ import annotations
import re, sys
from pathlib import Path

try:
    import yaml, jsonschema
except ImportError as e:
    print(f"validate: missing dependency: {e.name}. Install: pip install pyyaml jsonschema")
    sys.exit(2)

ID_RE = {
    "vision":     re.compile(r"^VIS-\d{3}$"),
    "roadmap":    re.compile(r"^ROADMAP-\d{3}$"),
    "epic":       re.compile(r"^EPIC-([A-Z]{2,5})-\d{3}$"),
    "feature":    re.compile(r"^FEATURE-([A-Z]{2,5})-\d{3}$"),
    "user_story": re.compile(r"^US-([A-Z]{2,5})-\d{3}$"),
}
FOLDER_FOR_TYPE = {"epic": "epics", "feature": "features", "user_story": "stories"}
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
QID_RE = re.compile(r"^Q-(\d+):")                    # well-formed open_questions entry prefix
QID_ANY_RE = re.compile(r"\bQ-(\d+)\b")              # any Q-ID mention (body mirror scan)
OQ_HEAD_RE = re.compile(r"^##\s+.*open questions.*$", re.I | re.M)
SO_THAT_FILLER_RE = re.compile(r"value described in the source", re.I)  # ingest anti-pattern
LINK_FIELDS = ("depends_on", "see_also", "updates", "updated_by")
SCHEMA_FILE = {"vision": "vision", "roadmap": "roadmap", "epic": "epic",
               "feature": "feature", "user_story": "story"}

errors: list[str] = []
warnings: list[str] = []
def err(f, msg): errors.append(f"{f}: {msg}")
def warn(f, msg): warnings.append(f"{f}: {msg}")

def find_root(start: Path) -> Path | None:
    for p in [start, *start.parents]:
        if (p / "domains" / "structure.yaml").exists():
            return p
    return None

def find_schemas(root: Path, script_dir: Path) -> Path | None:
    for c in (script_dir / "schemas", script_dir.parent / "schemas", root / "core" / "schemas",
              root / "schemas", root / "scripts" / "schemas"):
        if c.is_dir():
            return c
    return None

def frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("\n---", 2)
    if len(parts) < 2:
        return None
    return yaml.safe_load(parts[0][3:])

def as_list(v):
    return v if isinstance(v, list) else [v] if v is not None else []

def normalize(fm: dict) -> dict:
    """YAML parses bare dates as date objects; the contract treats them as ISO strings."""
    import datetime as _dt
    return {k: (v.isoformat() if isinstance(v, (_dt.date, _dt.datetime)) else v)
            for k, v in fm.items()}

def main() -> int:
    script_dir = Path(__file__).resolve().parent
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else find_root(Path.cwd())
    if root is None or not (root / "domains" / "structure.yaml").exists():
        print("validate: cannot find repo root (no domains/structure.yaml)"); return 2
    schemas_dir = find_schemas(root, script_dir)
    if schemas_dir is None:
        print("validate: cannot find schemas directory"); return 2
    schemas = {t: yaml.safe_load((schemas_dir / f"{s}.schema.yaml").read_text(encoding="utf-8"))
               for t, s in SCHEMA_FILE.items()}
    structure_schema = yaml.safe_load((schemas_dir / "structure.schema.yaml").read_text(encoding="utf-8"))
    release_schema = yaml.safe_load((schemas_dir / "release.schema.yaml").read_text(encoding="utf-8"))

    # ---- structure.yaml ----
    sfile = root / "domains" / "structure.yaml"
    structure = yaml.safe_load(sfile.read_text(encoding="utf-8")) or {}
    try:
        jsonschema.validate(structure, structure_schema)
    except jsonschema.ValidationError as e:
        err(sfile.name, f"structure schema: {e.message}")
        return report()
    domains = structure.get("domains", {})
    codes = {}
    for dname, d in domains.items():
        code = d.get("code", "")
        if code in codes:
            err(sfile.name, f"duplicate domain code {code} ({codes[code]} and {dname})")
        codes[code] = dname
    code_of = {d: v.get("code") for d, v in domains.items()}
    subs_of = {d: [s["id"] for s in v.get("sub_domains", [])] for d, v in domains.items()}

    # folder tree <-> map
    ddir = root / "domains"
    for dname in domains:
        base = ddir / dname
        if not base.is_dir():
            err("domains/", f"domain '{dname}' declared but folder missing"); continue
        targets = [base / s for s in subs_of[dname]] if subs_of[dname] else [base]
        for t in targets:
            for leaf in ("epics", "features", "stories"):
                if not (t / leaf).is_dir():
                    warn(str(t.relative_to(root)), f"missing {leaf}/ folder")
    for p in ddir.iterdir():
        if p.is_dir() and p.name not in domains:
            err("domains/", f"folder '{p.name}' not declared in structure.yaml")

    # ---- collect artifacts ----
    artifacts = {}   # id -> (path, fm)
    files = list((root / "vision").glob("*.md")) if (root / "vision").is_dir() else []
    files += [p for p in ddir.rglob("*.md") if p.name != "_index.md"]
    for path in files:
        rel = str(path.relative_to(root))
        fm = None
        try:
            fm = frontmatter(path)
        except yaml.YAMLError as e:
            err(rel, f"frontmatter YAML error: {e}"); continue
        if not isinstance(fm, dict):
            warn(rel, "no YAML frontmatter — skipped (free-form file in typed area?)"); continue
        fm = normalize(fm)
        empty_keys = [k for k, v in fm.items() if v is None]
        for k in empty_keys:
            warn(rel, f"empty frontmatter key '{k}' — fill it or remove the key")
        fm = {k: v for k, v in fm.items() if v is not None}
        atype = fm.get("type")
        if atype not in schemas:
            err(rel, f"unknown/missing type: {atype!r}"); continue
        try:
            jsonschema.validate(fm, schemas[atype])
        except jsonschema.ValidationError as e:
            loc = "/".join(str(x) for x in e.path) or "frontmatter"
            err(rel, f"schema ({loc}): {e.message}")
        aid = str(fm.get("id", ""))
        m = ID_RE.get(atype) and ID_RE[atype].match(aid)
        if not m:
            err(rel, f"id '{aid}' does not match {atype} grammar"); continue
        if aid in artifacts:
            err(rel, f"duplicate id {aid} (also in {artifacts[aid][0].relative_to(root)})")
            continue
        artifacts[aid] = (path, fm)
        # filename & slug
        if not path.stem.startswith(aid):
            err(rel, f"filename must start with id '{aid}'")
        else:
            slug = path.stem[len(aid):].lstrip("-")
            if slug and not SLUG_RE.match(slug):
                warn(rel, f"slug '{slug}' is not kebab-case")
        # placement & path consistency
        if atype in ("vision", "roadmap"):
            if path.parent != root / "vision":
                err(rel, f"{atype} must live in vision/")
        else:
            parts = path.relative_to(ddir).parts
            dom = parts[0]
            sub = parts[1] if len(parts) == 4 else None
            leaf = parts[-2]
            if leaf != FOLDER_FOR_TYPE[atype]:
                err(rel, f"{atype} must be under {FOLDER_FOR_TYPE[atype]}/, found {leaf}/")
            if fm.get("domain") != dom:
                err(rel, f"frontmatter domain '{fm.get('domain')}' != path domain '{dom}'")
            if sub and fm.get("sub_domain") != sub:
                err(rel, f"frontmatter sub_domain '{fm.get('sub_domain')}' != path '{sub}'")
            if not sub and fm.get("sub_domain"):
                err(rel, f"sub_domain set but file not in a sub-domain folder")
            expected_code = code_of.get(dom)
            if expected_code and m.group(1) != expected_code:
                err(rel, f"id code '{m.group(1)}' != domain code '{expected_code}' for '{dom}'")

    # ---- links ----
    PARENT = {"user_story": ("parent_feature", "feature"), "feature": ("parent_epic", "epic"),
              "epic": ("parent_vision", "vision"), "roadmap": ("parent_vision", "vision")}
    for aid, (path, fm) in artifacts.items():
        rel = str(path.relative_to(root))
        atype = fm["type"]
        if atype in PARENT:
            field, ptype = PARENT[atype]
            pid = fm.get(field)
            if pid:
                if pid not in artifacts:
                    err(rel, f"{field} '{pid}' does not resolve")
                elif artifacts[pid][1]["type"] != ptype:
                    err(rel, f"{field} '{pid}' is a {artifacts[pid][1]['type']}, expected {ptype}")
        for f in LINK_FIELDS:
            for t in as_list(fm.get(f)):
                if t not in artifacts:
                    err(rel, f"{f} target '{t}' does not resolve")
        for t in as_list(fm.get("updates")):
            if t in artifacts and aid not in as_list(artifacts[t][1].get("updated_by")):
                warn(rel, f"updates {t}, but {t} has no updated_by back-link")

    # ---- open questions mirror (FR-CON-014) ----
    for aid, (path, fm) in artifacts.items():
        rel = str(path.relative_to(root))
        fm_qids = []
        for q in as_list(fm.get("open_questions")):
            m = QID_RE.match(str(q))
            if not m:
                continue  # malformed entries are already reported via the schema pattern
            if m.group(1) in fm_qids:
                err(rel, f"duplicate open_questions ID Q-{m.group(1)}")
            fm_qids.append(m.group(1))
        text = path.read_text(encoding="utf-8")
        msec = OQ_HEAD_RE.search(text)
        sec = None
        if msec:
            tail = text[msec.end():]
            end = re.search(r"^(---\s*$|##\s)", tail, re.M)
            sec = tail[:end.start()] if end else tail
        sec_qids = QID_ANY_RE.findall(sec) if sec else []
        if fm_qids and sec is None:
            err(rel, "open_questions in frontmatter but no 'Open questions' section mirrors them")
        for q in fm_qids:
            if sec is not None and q not in sec_qids:
                err(rel, f"Q-{q} missing from the Open questions section (mirror of the frontmatter SSOT)")
        for q in dict.fromkeys(sec_qids):
            if q not in fm_qids:
                err(rel, f"Q-{q} in the Open questions section but not in frontmatter (frontmatter is the SSOT)")
        if fm.get("type") == "user_story" and SO_THAT_FILLER_RE.search(text):
            warn(rel, "placeholder 'So that' text — write the real benefit or mark TBD + open question (ingest playbook)")

    # ---- releases ----
    rdir = root / "releases"
    manifests = {}
    if rdir.is_dir():
        for rfile in sorted(rdir.glob("*.yaml")):
            rel = f"releases/{rfile.name}"
            data = yaml.safe_load(rfile.read_text(encoding="utf-8")) or {}
            try:
                jsonschema.validate(data, release_schema)
            except jsonschema.ValidationError as e:
                err(rel, f"release schema: {e.message}"); continue
            manifests[str(data.get("version"))] = data
            for key in ("epics", "features", "stories"):
                for aid in data.get(key, []):
                    if aid not in artifacts:
                        err(rel, f"{key} entry '{aid}' does not exist")
    listed = {aid for d in manifests.values() for k in ("epics", "features", "stories")
              for aid in d.get(k, [])}
    for aid, (path, fm) in artifacts.items():
        for r in as_list(fm.get("release")):
            if str(r) in manifests and aid not in listed:
                warn(str(path.relative_to(root)), f"release '{r}' has a manifest but {aid} is not listed in it")

    return report()

def report() -> int:
    for w in warnings: print(f"WARN  {w}")
    for e in errors:  print(f"ERROR {e}")
    print(f"\nvalidate: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
