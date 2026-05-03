"""Very small extractor placeholder.

In the full project this would use NLTK to select relevant paragraphs
from man pages. For the minimal runnable version we just return the
man_db.lookup result (if any).
"""
from typing import Optional
from .man_db import lookup


def extract_description(command: str) -> Optional[str]:
    return lookup(command)
