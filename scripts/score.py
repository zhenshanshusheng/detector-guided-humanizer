#!/usr/bin/env python3
"""Score text against the Zhuque AI detector API.

Usage:
    python3 score.py <textfile> [--merge]
    cat file.txt | python3 score.py

The API key is read from the ZHUQUE_API_KEY environment variable.
Never hardcode keys. Never commit keys.

Output: Human/AI/Suspected percentages + per-segment labels.
"""
import json
import os
import sys
import urllib.request
import urllib.error

API = "https://ai-gateway.edgeone.link/v1/providers/zhuque-text/classify"
NAMES = {"0": "Human", "1": "AI", "2": "Suspected"}


def detect(text, merge=True):
    key = os.environ.get("ZHUQUE_API_KEY", "")
    if not key:
        sys.exit("error: set ZHUQUE_API_KEY environment variable")
    body = json.dumps({"text": text, "is_merge": merge}).encode()
    req = urllib.request.Request(API, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", "Bearer " + key)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"error: HTTP {e.code}: {e.read().decode()[:200]}")


def main():
    merge = "--merge" in sys.argv
    if sys.stdin.isatty() and len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
        text = open(sys.argv[1], encoding="utf-8").read()
    else:
        text = sys.stdin.read()
    out = detect(text, merge=merge)
    if out.get("status") != "success":
        sys.exit(f"error: {str(out)[:200]}")
    r = out.get("labels_ratio", {})
    print(f"Human {r.get('0', 0)*100:.1f}% / AI {r.get('1', 0)*100:.1f}% / "
          f"Suspected {r.get('2', 0)*100:.1f}% (conf {out.get('softmax_confidence')})")
    for s in out.get("segment_labels", []):
        print(f"  seg{s.get('order')}: {NAMES.get(str(s.get('label')))} "
              f"conf={s.get('conf', 0):.4f}")
    tokens = (out.get("makers_models_usage") or {}).get("total_tokens")
    print(f"  tokens billed: {tokens}")


if __name__ == "__main__":
    main()
