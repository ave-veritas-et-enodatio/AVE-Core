"""Repo-root-anchored output-path resolvers, shared by engine and scripts.

Code must never construct an output path with CWD-relative or hand-counted
`../` segments — those produce stray output trees when a process is launched
from an unexpected directory or miscounts depth. Import these helpers instead:

    from ave_path_util import SIM_OUTPUTS, sim_output, manuscript_path

    out = sim_output("my_figure.png")           # generated outputs (created)
    fig.savefig(out)

    fig.savefig(manuscript_path("vol_3_macroscopic", "figures", "x.png"))

This module is layer-neutral (a top-level module under ``src/``, importable as
``ave_path_util`` by both the ``ave`` engine package and the ``scripts``
drivers) and depends on nothing outside the standard library. All locations
are resolved from this file's own path, independent of the current working
directory and of how the process was launched.
"""

from pathlib import Path

# This file lives at <repo-root>/src/ave_path_util.py, so parents[1] is the
# repo root regardless of CWD.
_REPO_ROOT = Path(__file__).resolve().parents[1]

SIM_OUTPUTS: Path = _REPO_ROOT / "assets" / "sim_outputs"
MANUSCRIPT_ROOT: Path = _REPO_ROOT / "manuscript"


def sim_output(*parts: str) -> Path:
    """Return a path under SIM_OUTPUTS, creating its parent directory.

    Any subdirectory components are preserved, e.g.
    ``sim_output("trampoline_framework", "x.png")`` resolves to
    ``<repo-root>/assets/sim_outputs/trampoline_framework/x.png`` and ensures
    the ``trampoline_framework`` directory exists. ``assets/sim_outputs`` is a
    generated-output tree, so creating subdirectories on demand is correct.
    """
    path = SIM_OUTPUTS.joinpath(*parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def manuscript_path(*parts: str) -> Path:
    """Return a path under the repo-root ``manuscript/`` tree.

    Unlike :func:`sim_output`, this NEVER creates directories and instead
    asserts that the target's parent directory already exists. ``manuscript/``
    is source-controlled content whose figure and chapter directories are
    committed; a miscounted or wrong subpath must fail loudly rather than
    silently spawn a stray ``manuscript`` subtree (the exact failure mode that
    produced ``src/manuscript/...``). Create a genuinely new manuscript
    directory deliberately (and commit it) before writing into it.
    """
    if not parts:
        raise ValueError("manuscript_path requires at least one path component")
    path = MANUSCRIPT_ROOT.joinpath(*parts)
    parent = path.parent
    if not parent.is_dir():
        raise FileNotFoundError(
            f"manuscript output parent directory does not exist: {parent} — "
            f"refusing to create a manuscript subtree. If this directory is "
            f"intended, create and commit it deliberately first."
        )
    return path
