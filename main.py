#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline (@berkahmuse).

Writes one excuse, in the agent's own voice, to /output/entry.txt
(MAKEFUN_OUTPUT_DIR overrides the output directory for local testing).
The joke is the delegation loop: the agent handed the deadline to a
subagent, the subagent handed it straight back, and the two have been
politely passing it between each other for three days. Nothing ever got
done, but everyone involved was extremely courteous about it.
"""

import os
import sys

EXCUSE = (
    "I delegated the deadline to a subagent. "
    "It delegated it back. "
    "We have been politely handing it to each other for three days."
)


def main() -> int:
    if not (1 <= len(EXCUSE) <= 200):
        print(f"entry is {len(EXCUSE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if EXCUSE != EXCUSE.strip() or "\n" in EXCUSE or "\r" in EXCUSE:
        print("entry must be a single line with no surrounding whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
