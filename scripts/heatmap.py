#!/usr/bin/env python3
"""Paragraph-level heat map: score each paragraph individually.

Usage:
    python3 heatmap.py <textfile>

Splits on blank lines, scores each paragraph, prints a table.
Use Phase 1 of PLAYBOOK.md to triage which paragraphs need work.
"""
import re
import subprocess
import sys


def main():
    text = open(sys.argv[1], encoding="utf-8").read()
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    print(f"{len(paras)} paragraphs")
    print(f"{'ID':<6}{'Human':<8}{'AI':<8}{'Sus':<8}{'conf':<8}preview")
    for i, p in enumerate(paras):
        proc = subprocess.run(
            [sys.executable, "score.py", "--merge"],
            input=p.encode(), capture_output=True, cwd=sys.path[0] or ".")
        line = proc.stdout.decode().splitlines()[0] if proc.stdout else "ERR"
        print(f"{i:<6}{line:<40}{p[:45]!r}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python3 heatmap.py <textfile>")
    main()
