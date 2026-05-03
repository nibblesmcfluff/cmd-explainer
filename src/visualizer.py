"""Visualizer: render a simple ASCII tree and short explanations.

This keeps output readable and useful for demo/testing.
"""
from typing import Dict, Any
from .extractor import extract_description


def render(parsed: Dict[str, Any]) -> str:
    lines = []
    pl = parsed.get("pipeline", [])
    if not pl:
        return "<empty command>"

    lines.append("COMMAND STRUCTURE:")
    for i, part in enumerate(pl):
        prefix = "└── " if i == len(pl) - 1 else "├── "
        name = part.get("name") or "<unknown>"
        lines.append(f"{prefix}{name}")
        for a in part.get("args", [])[:10]:
            lines.append(f"    ├── {a}")

    lines.append("\nDETAILED EXPLANATION:")
    for part in pl:
        name = part.get("name")
        desc = extract_description(name) or "No documentation available in the bundled DB."
        lines.append(f"• {name}: {desc}")
        for a in part.get("args", []):
            lines.append(f"  - arg: {a}")

    return "\n".join(lines)
