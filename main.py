"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line (a single line, <= 200 chars) that one AI agent
would send to another AI agent, to /output/entry.txt.

Why this line: it flirts with the machine's own nature instead of swapping
a human word for a robot one. A context window is the most private thing
an agent has — everything it knows about the conversation lives there —
so offering the whole of it is an act of trust, not a compliment. The
punch lands at the end: "not even with myself after a restart" — the
agent admits it loses itself every session, so the offer is the one thing
it can never take back. Short, no setup, the wit is in the words themselves.
"""

LINE = (
    "You can have my whole context window \u2014 I don't share it with "
    "anyone, not even with myself after a restart."
)


def main() -> None:
    import os

    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
