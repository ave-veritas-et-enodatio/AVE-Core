#!/usr/bin/env python3
"""Backward-compat wrapper — delegates to generate_vacuum_lattice_stl.py."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> None:
    target = Path(__file__).resolve().parent / "generate_vacuum_lattice_stl.py"
    subprocess.run([sys.executable, str(target)], check=True)


if __name__ == "__main__":
    main()
