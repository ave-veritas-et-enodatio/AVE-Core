"""Repo-root-anchored sim-outputs directory resolver for driver scripts.

Drivers must never construct the sim-outputs path with CWD-relative or
hand-counted `../` segments — those produce stray output trees when the
driver is launched from an unexpected directory or miscounts depth. Import
this helper instead:

    from scripts._output import SIM_OUTPUTS, sim_output

    out = sim_output("my_figure.png")
    fig.savefig(out)

The location is resolved from this file's own path, so it is independent of
the current working directory and of how the driver is launched.
"""

from pathlib import Path

# This file lives at <repo-root>/src/scripts/_output.py, so parents[2] is the
# repo root regardless of CWD.
_REPO_ROOT = Path(__file__).resolve().parents[2]

SIM_OUTPUTS: Path = _REPO_ROOT / "assets" / "sim_outputs"


def sim_output(*parts: str) -> Path:
    """Return a path under SIM_OUTPUTS, creating its parent directory.

    Any subdirectory components are preserved, e.g.
    ``sim_output("trampoline_framework", "x.png")`` resolves to
    ``<repo-root>/assets/sim_outputs/trampoline_framework/x.png`` and ensures
    the ``trampoline_framework`` directory exists.
    """
    path = SIM_OUTPUTS.joinpath(*parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
