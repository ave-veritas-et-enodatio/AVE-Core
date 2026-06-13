#!/usr/bin/env python3
"""Render the engine x DOF capability matrix from engine_capability_matrix.yaml.

CLASS-TAG (load-bearing): the matrix is VERIFIED-STATE (audit-grounded); the
substrate-complete engine described in engine-capability-map.md is a DESIGN
PROPOSAL, not a built engine.

This figure is a LIVING TRACKER: update a cell's `status` in
engine_capability_matrix.yaml and re-run this script -> the PNG (and thus the
leaf) updates. A cage-test PASS or a loop that stops being imposed is a
one-line YAML edit + re-render.

Usage:
    python engine_capability_map.py [--out engine_capability_map.png]
"""
from __future__ import annotations

import argparse
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import yaml  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent

STATUS_COLOR = {
    "have": "#2e7d32",     # green
    "partial": "#f9a825",  # amber
    "absent": "#c62828",   # red
    "na": "#bdbdbd",       # grey
}
STATUS_GLYPH = {"have": "●", "partial": "◐", "absent": "○", "na": "–"}


def load() -> dict:
    with open(HERE / "engine_capability_matrix.yaml") as f:
        return yaml.safe_load(f)


def render(data: dict, out: str) -> None:
    dof = data["dof"]
    engines = data["engines"]
    ncol, nrow = len(dof), len(engines)

    fig, ax = plt.subplots(figsize=(2.0 + 1.25 * ncol, 1.4 + 0.62 * nrow))

    for r, eng in enumerate(engines):
        y = nrow - 1 - r
        for c, d in enumerate(dof):
            cell = eng["cells"].get(d["key"], {})
            st = cell.get("status", "na")
            ax.add_patch(
                plt.Rectangle((c, y), 1, 1, facecolor=STATUS_COLOR[st], edgecolor="white", lw=2)
            )
            ax.text(
                c + 0.5, y + 0.5, STATUS_GLYPH[st],
                ha="center", va="center", color="white", fontsize=15, fontweight="bold",
            )

    ax.set_xlim(0, ncol)
    ax.set_ylim(0, nrow)
    ax.set_xticks([c + 0.5 for c in range(ncol)])
    ax.set_xticklabels([d["name"] for d in dof], rotation=32, ha="right", fontsize=8)
    ax.set_yticks([nrow - 1 - r + 0.5 for r in range(nrow)])
    ax.set_yticklabels([e["name"] for e in engines], fontsize=8)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_title(
        "AVE engine × DOF capability map\n"
        "(matrix = verified-state; substrate-complete engine = design proposal)",
        fontsize=9, pad=12,
    )
    legend = [Patch(facecolor=STATUS_COLOR[k], label=f"{STATUS_GLYPH[k]} {k}")
              for k in ("have", "partial", "absent", "na")]
    ax.legend(handles=legend, loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=8, frameon=False)

    fig.tight_layout()
    fig.savefig(out, dpi=150, bbox_inches="tight")
    print(f"wrote {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "engine_capability_map.png"))
    args = ap.parse_args()
    render(load(), args.out)
