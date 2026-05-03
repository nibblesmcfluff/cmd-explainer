"""Simple parser wrapper around bashlex/shlex.

The goal here is not to be a perfect shell parser but to provide a small,
well-typed structure that downstream components (visualizer, shell) can
use for demonstration and testing.
"""
from typing import List, Dict, Any
import shlex

try:
    import bashlex
except Exception:
    bashlex = None


def parse_command(cmd: str) -> Dict[str, Any]:
    """Parse a shell command into a simple structure.

    Returns a dict with keys:
      - pipeline: list of command-parts (each a dict with name, args, raw)

    This function prefers bashlex when available to get a slightly better
    parse; otherwise falls back to splitting on pipes + shlex.
    """
    if not cmd:
        return {"pipeline": []}

    parts = [p.strip() for p in cmd.split("|")]
    pipeline = []

    for part in parts:
        entry = {"raw": part, "name": None, "args": []}
        # try bashlex to get the command name if available
        if bashlex:
            try:
                nodes = bashlex.parse(part)
                # find first word token
                for node in nodes:
                    for word in getattr(node, "words", []) or []:
                        text = getattr(word, "word", None)
                        if text:
                            # split using shlex to respect quotes
                            toks = shlex.split(text)
                            if toks:
                                entry["name"] = toks[0]
                                entry["args"] = toks[1:]
                                break
                    if entry["name"]:
                        break
            except Exception:
                pass

        if entry["name"] is None:
            try:
                toks = shlex.split(part)
                if toks:
                    entry["name"] = toks[0]
                    entry["args"] = toks[1:]
            except Exception:
                # fallback naive split
                toks = part.split()
                if toks:
                    entry["name"] = toks[0]
                    entry["args"] = toks[1:]

        pipeline.append(entry)

    return {"pipeline": pipeline}
