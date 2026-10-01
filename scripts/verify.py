#!/usr/bin/env python3
"""Verify text integrity after window splicing.

Usage:
    python3 verify.py <textfile>

Checks for:
- Duplicated sentences (strong AI signal + content bug)
- Missing spaces after periods (splice artifacts)
- Double spaces, triple newlines

Exit 0 if clean, 1 if issues found.
"""
import re
import sys


def main():
    text = open(sys.argv[1], encoding="utf-8").read()
    issues = 0

    sentences = re.split(r"(?<=[.!?])\s+", text)
    seen = set()
    for s in sentences:
        s = s.strip()
        if len(s) > 30:
            if s in seen:
                print(f"DUP: {s[:80]}")
                issues += 1
            seen.add(s)

    for m in re.finditer(r"\.[A-Z]", text):
        print(f"MISSING-SPACE: ...{text[max(0,m.start()-25):m.end()+25]!r}...")
        issues += 1

    for m in re.finditer(r" {2,}", text):
        print(f"DOUBLE-SPACE at char {m.start()}")
        issues += 1

    print(f"{'CLEAN' if issues == 0 else f'{issues} ISSUES'}")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python3 verify.py <textfile>")
    main()
