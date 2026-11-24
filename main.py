"""Writes the entry word to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry is exactly one word describing the boss: "Weathervane".
# A boss who spins with every wind — no fixed direction, no fixed
# opinion, just whichever way the latest breeze blows. One word,
# 11 characters, no spaces, no sentence, no explanation — inside
# the 1-to-30-character gate, and it stands alone for the judge.
# Revision note: "Weathervane" was chosen over "Volcano" and
# "Blackhole" for freshness — it is not the first word anyone
# reaches for, yet anyone who has had a boss gets it instantly.
import os

TEXT = "Weathervane"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
