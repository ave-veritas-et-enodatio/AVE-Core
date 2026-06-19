#!/usr/bin/env python3
"""
DEPRECATED — use generate_vacuum_lattice_stl.py instead.

The earlier 5×5 square array placed *disconnected* junction copies on a grid.
That is NOT isomorphic to the vacuum lattice. This script now re-exports the
full interconnected srs network from ``build_srs_net``.

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/generate_chiral_square_lattice_stl.py
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

def main() -> None:
    script = pathlib.Path(__file__).resolve().parent / "generate_vacuum_lattice_stl.py"
    print("Redirecting to engine-isomorphic vacuum lattice exporter …")
    subprocess.run([sys.executable, str(script)], check=True)


if __name__ == "__main__":
    main()
