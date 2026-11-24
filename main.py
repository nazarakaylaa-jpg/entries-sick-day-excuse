"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt:
a sick-day excuse that is absurd yet just plausible enough,
with a concrete detail and the punchline landing at the end.
"""

import os

ENTRY = (
    "Can't come in \u2014 I slipped on the dog's toy, landed on the remote "
    "and accidentally ordered 42 garden gnomes. I have to stay home to "
    "refuse the delivery."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
