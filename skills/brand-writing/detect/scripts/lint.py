#!/usr/bin/env python3
"""Flag the regex-catchable AI patterns in a text file. Word lists come from
references/word-lists.json so the script carries no content of its own."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORD_LISTS = HERE.parent.parent / "references" / "word-lists.json"

BINARY_CONTRAST = re.compile(
    r"\b(?:it|this|that|the (?:question|point|issue|problem))(?:'s|\s+(?:is|was))?\s*n[o']t\s+(?:just\s+|only\s+|about\s+)?[^.?!]{1,80}[.,;]\s*(?:it'?s|but)\b",
    re.IGNORECASE,
)
COLON_REVEAL = re.compile(r"(?:^|[.!?]\s+)([A-Z][^.:!?,\n]{2,40}):\s+([a-z][^.,:;!?\n]{3,70})\.")
EM_DASH = "—"


def colon_reveal(line):
    """Short lead, short lowercase reveal, no commas on either side: the dramatic
    shape, not a colon introducing a list or an explanation."""
    for m in COLON_REVEAL.finditer(line):
        lead, reveal = m.group(1), m.group(2)
        if len(lead.split()) <= 6 and len(reveal.split()) <= 10:
            return True
    return False


def load_lists(path=WORD_LISTS):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _phrase_re(phrase):
    return re.compile(r"\b" + re.escape(phrase).replace(r"\ ", r"\s+") + r"\b", re.IGNORECASE)


def lint(text, lists=None):
    lists = lists or load_lists()
    findings = []
    lines = text.splitlines()

    def add(kind, lineno, excerpt, fix):
        findings.append({"pattern": kind, "line": lineno, "excerpt": excerpt.strip(), "fix": fix})

    for kind, key, fix in (
        ("banned word", "banned", "cut it or say the plain thing"),
        ("empty phrase", "empty_phrases", "cut it; start at the point"),
    ):
        for phrase in lists[key]:
            rx = _phrase_re(phrase)
            for i, line in enumerate(lines, 1):
                for m in rx.finditer(line):
                    add(kind, i, m.group(0), fix)

    for i, line in enumerate(lines, 1):
        if BINARY_CONTRAST.search(line):
            add("binary contrast", i, line[:120], "state the second half directly")
        if not line.lstrip().startswith(("-", "*", "|", "#", ">")) and colon_reveal(line):
            add("colon reveal", i, line[:120], "rewrite as a plain sentence")

    dash_count = text.count(EM_DASH)
    words = max(len(text.split()), 1)
    if dash_count >= 3 and dash_count / words > 0.004:
        add("em dash cluster", 0, f"{dash_count} em dashes in {words} words", "recast as periods, commas, or colons")

    return findings


def main(argv):
    if len(argv) < 2:
        print("usage: lint.py <file.md> [--json]", file=sys.stderr)
        return 2
    text = Path(argv[1]).read_text(encoding="utf-8")
    findings = lint(text)
    if "--json" in argv:
        print(json.dumps(findings, indent=2))
    else:
        for f in findings:
            loc = f"line {f['line']}" if f["line"] else "whole text"
            print(f"{f['pattern']} ({loc}): \"{f['excerpt']}\" -> {f['fix']}")
        print(f"{len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
