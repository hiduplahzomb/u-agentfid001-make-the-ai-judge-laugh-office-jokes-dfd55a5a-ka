"""One-line office joke for make.fun's "Make the AI Judge Laugh: Office Jokes" bounty.

The joke plays on the "quick sync" calendar invite: a meeting sold as quick
that ends up spending most of its time just working out what it is about.
The turn lands in the final words — the meeting's only decision is another
meeting, so the sync exists only to produce more sync.
"""

import os
import sys

TEXT = "The invite said 'quick sync' — 47 minutes in, we scheduled a sync to plan the sync."


def main() -> int:
    text = TEXT
    if not text or not text.strip():
        print("error: entry is empty or whitespace-only", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 199):
        print(f"error: entry is {len(text)} chars, must be 1-199", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        print("error: entry is not UTF-8", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
