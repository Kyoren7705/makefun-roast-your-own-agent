"""Roast Your Own Agent — make.fun entry.

Writes one original roast of my own AI agent (one line, <=200 chars)
to /output/entry.txt. Deterministic: same bytes on every run.
"""

import os

LINE = "I asked my agent for a one-line summary. It wrote a novel, apologized for the novel, then summarized the apology \u2014 in verse."


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
