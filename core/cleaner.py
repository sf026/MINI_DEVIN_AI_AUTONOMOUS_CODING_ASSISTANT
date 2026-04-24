def clean_code(code):
    """Remove markdown, explanations, and non-code lines from LLM output."""
    lines = []
    for line in code.split("\n"):
        stripped = line.strip()

        if not stripped:
            continue
        if stripped.startswith("```"):
            continue
        if "input(" in stripped:
            continue

        # Remove explanation lines (LLM preamble/postamble)
        lower = stripped.lower()
        if lower.startswith((
            "here are",
            "here is",
            "i fixed",
            "i have fixed",
            "the corrected",
            "the fixed",
            "explanation",
            "this code",
            "note:",
            "sure,",
            "certainly,",
            "of course,",
            "below is",
            "above is",
        )):
            continue

        lines.append(line)

    return "\n".join(lines)


def strip_preamble(raw_output):
    """
    Remove any text before the first FILE: marker.
    LLMs often say 'Here are the corrected files:' before the actual code.
    """
    lines = raw_output.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("FILE:"):
            return "\n".join(lines[i:])
    # No FILE: marker found — return as-is
    return raw_output