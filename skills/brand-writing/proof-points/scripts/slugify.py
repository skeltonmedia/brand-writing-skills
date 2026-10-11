#!/usr/bin/env python3
import re
import sys


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:96].strip("-")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: slugify.py 'Proof title'", file=sys.stderr)
        sys.exit(2)
    print(slugify(" ".join(sys.argv[1:])))
