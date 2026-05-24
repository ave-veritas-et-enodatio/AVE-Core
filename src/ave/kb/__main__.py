"""Module entry point so ``python -m ave.kb <args>`` works."""

from __future__ import annotations

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
