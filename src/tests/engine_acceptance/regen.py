"""Regenerate ALL L0-L1 acceptance debug figures with one command.

    PYTHONPATH=<worktree>/src KF_VIZ=1 \\
        <repo>/.venv/bin/python -m tests.engine_acceptance.regen

This runs the full acceptance suite with figure emission ON (KF_VIZ=1), writing
every `<test_id>_debug.png` into research/figures/engine_acceptance/. It is a thin
pytest wrapper — it does NOT re-implement any physics; the figures are recorded
off the same stepper the functional tests run. Exit code mirrors pytest's
(non-zero if any acceptance test fails — figures are additive, the physics gate
is unchanged).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path


def main() -> int:
    os.environ["KF_VIZ"] = "1"
    import pytest

    suite = str(Path(__file__).resolve().parent)
    # -s so the per-test "[viz] ... -> <path>" lines surface
    return pytest.main([suite, "-s", "-q"])


if __name__ == "__main__":
    sys.exit(main())
