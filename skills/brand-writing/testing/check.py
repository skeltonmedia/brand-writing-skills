#!/usr/bin/env python3
"""Pack self-test: lint fixtures behave, every SKILL.md has frontmatter and
stays under 500 lines, no reference file is missing."""
import json
import re
import sys
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PACK / "detect" / "scripts"))
from lint import lint  # noqa: E402

FIXTURES = PACK / "testing" / "fixtures"
REQUIRED_REFS = [
    "references/ai-patterns.md",
    "references/word-lists.json",
    "references/voice-preservation.md",
    "references/proof-block-format.md",
]


def check_skill_files():
    errors = []
    for skill in PACK.rglob("SKILL.md"):
        text = skill.read_text(encoding="utf-8")
        rel = skill.relative_to(PACK)
        if not text.startswith("---"):
            errors.append(f"{rel}: missing frontmatter")
            continue
        fm = text.split("---", 2)[1]
        for field in ("name:", "description:"):
            if not re.search(rf"^{field}", fm, re.MULTILINE):
                errors.append(f"{rel}: frontmatter lacks {field}")
        if text.count("\n") > 500:
            errors.append(f"{rel}: over 500 lines")
    return errors


def check_refs():
    return [f"missing {r}" for r in REQUIRED_REFS if not (PACK / r).exists()]


def check_fixtures():
    errors = []
    slop = (FIXTURES / "slop-sample.md").read_text(encoding="utf-8")
    expected = json.loads((FIXTURES / "slop-sample.expected.json").read_text(encoding="utf-8"))
    findings = lint(slop)
    kinds = {f["pattern"] for f in findings}
    if len(findings) < expected["min_findings"]:
        errors.append(f"slop-sample: {len(findings)} findings, expected at least {expected['min_findings']}")
    for kind in expected["must_include"]:
        if kind not in kinds:
            errors.append(f"slop-sample: pattern '{kind}' not found")
    clean = (FIXTURES / "clean-sample.md").read_text(encoding="utf-8")
    clean_findings = lint(clean)
    if clean_findings:
        errors.append(f"clean-sample: {len(clean_findings)} false positive(s): {clean_findings}")
    return errors


def check_own_prose():
    """The pack's prose must pass its own lint. Files that quote patterns on
    purpose (detect, ai-patterns, the example) are exempt."""
    exempt = {"detect/SKILL.md", "references/ai-patterns.md", "references/examples/before-after-01.md"}
    errors = []
    readme = PACK.parent.parent / "README.md"
    targets = ([readme] if readme.exists() else []) + sorted(PACK.rglob("*.md"))
    for path in targets:
        rel = path.relative_to(PACK) if path.is_relative_to(PACK) else path.name
        if str(rel) in exempt or "fixtures" in str(rel):
            continue
        hits = lint(path.read_text(encoding="utf-8"))
        for h in hits:
            errors.append(f"{rel}: {h['pattern']} line {h['line']}: {h['excerpt'][:60]}")
    return errors


def main():
    errors = check_skill_files() + check_refs() + check_fixtures() + check_own_prose()
    for e in errors:
        print("FAIL", e)
    print("ok" if not errors else f"{len(errors)} failure(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
