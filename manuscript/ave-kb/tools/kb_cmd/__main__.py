"""Module entry point so ``python -m kb_cmd <args>`` works."""

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
