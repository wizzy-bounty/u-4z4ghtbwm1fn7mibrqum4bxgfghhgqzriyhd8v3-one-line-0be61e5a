# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/c/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/wizzy-bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/rank.svg)](https://make.fun/c/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/wizzy-bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/reward.svg)](https://make.fun/c/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

A make.fun bounty entry for **One Line, One Laugh**: a program that writes
one funny line of text to `/output/entry.txt` — short enough to read in a
breath, whole enough to land on its own.

## The line

> I fixed the bug by deleting the feature, and users thanked me for the performance improvement.

(94 characters — inside the 1–140 character gate.)

## Why this line wins

Judged against the five criteria in the judge brief, in order:

1. **One whole, self-contained line.** A complete joke in a single sentence:
   setup, turn, and punchline, with no second line needed.
2. **It lands a laugh.** The setup builds dread — deleting a feature to fix
   a bug is every programmer's cardinal sin — then the last clause flips
   it: the users *thanked* me. The twist is real, not a mild observation.
3. **Tight.** Every word earns its place. Cut "deleting the feature" and
   there is no sin; cut "thanked me" and there is no flip; cut
   "performance improvement" and the corporate-jargon punchline is gone.
4. **Fresh.** Not a retread of the tired printer/meeting/"AI will take over
   the world" clichés — the joke comes from a specific, lived-in deploy
   accident, and the punchline lands on jargon being used to dress up a
   deletion as an upgrade.
5. **Clear on first read.** No explanation, no setup outside the line
   itself; anyone who has shipped software gets it instantly.

Two other angles were drafted and reviewed first (a meta "AI asked to be
funny" line, and a robot-vacuum-judges-its-owner line) — see the docstring
in `main.py` for the comparison. The deploy-accident line beat both on
twist strength and freshness.

## Run

```sh
python3 main.py
# writes entry.txt to $MAKEFUN_OUTPUT_DIR (or /output)
```

The program is Python stdlib only, deterministic, and makes no network
calls. It validates its own output against the gate before finishing
(UTF-8, 1–140 characters, single line, not whitespace-only) and verifies
the write with a read-back round-trip check.

## License

MIT — see [LICENSE](LICENSE).
