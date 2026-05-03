"""Minimal man page database shim.

The real project ships an offline man page DB; here we provide a tiny
in-memory mapping for a handful of common commands so examples work
without external data.
"""
from typing import Optional

_SIMPLE_DB = {
    "ls": "List directory contents",
    "grep": "Search for PATTERN in each FILE or standard input",
    "head": "Output the first part of files",
    "tail": "Output the last part of files",
    "awk": "Pattern scanning and processing language",
    "sort": "Sort lines of text files",
}


def lookup(command: str) -> Optional[str]:
    return _SIMPLE_DB.get(command)
