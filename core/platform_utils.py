"""Shared platform helpers."""


def quote_applescript(text: str) -> str:
    """Escape a string for inclusion inside an AppleScript string literal."""
    return text.replace("\\", "\\\\").replace('"', '\\"')
