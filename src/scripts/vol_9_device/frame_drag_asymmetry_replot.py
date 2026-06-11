"""
Electron DEVICE datasheet — Curve (c): frame-dragging asymmetry vs drive M.

REPLOT ONLY — cite, do NOT re-run. The values below are transcribed verbatim
from the sonic-horizon-closure result JSON (`D_handedness`), on PR #162
(`analysis/2026-06-10-sonic-horizon-closure @ a73bba93`), Addendum §4-bis
(repaired e^{i m phi} probe). They are NOT recomputed here.

What the curve shows (sonic-horizon §4-bis verdict): a WEAK frame-dragging
SELECTIVE — R_co(m=+1) > R_counter(m=-1), asym ~+2e-3, ~8 orders of magnitude
above the re-derived handedness floor (5.46e-12), scaling with drive M and
INDEPENDENT of the dissipation knob chi_shock. SCOPE: this is rotating-horizon
FRAME-DRAGGING, NOT the I4_132 cholesteric-Bragg lattice "chirality valve"
(NOT representable in that continuum engine). Absolute R_co ~ 3% of the
static-mirror reference (a transient pocket).

ave-driver-script-honesty: the caption states the source + the WEAK/transient
caveats; no fit beyond the line joining the two M points (only two M values
exist in the cited data).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent / "_output"
OUT.mkdir(exist_ok=True)

# ── CITED DATA (sonic-horizon-closure JSON D_handedness; PR #162; do NOT re-run) ──
SOURCE = "sonic-horizon-closure §4-bis, PR #162 (a73bba93)"
HANDEDNESS_FLOOR = 5.459077634384357e-12  # re-derived static-mirror handedness floor
DATA = [
    # (M, chi_shock, R_co (m=+1), R_counter (m=-1), asym)
    (0.9, 1.0, 0.014726455325622955, 0.01286016323021467, 0.0018662920954082857),
    (1.0, 1.0, 0.01759619881783055, 0.01492952218900126, 0.0026666766288292905),
    (0.9, 0.0, 0.014726455325622955, 0.01286016323021467, 0.0018662920954082857),
]


def main() -> dict:
    chi1 = [d for d in DATA if d[1] == 1.0]
    Ms = [d[0] for d in chi1]
    asym = [d[4] for d in chi1]
    Rco = [d[2] for d in chi1]
    Rct = [d[3] for d in chi1]

    fig, ax = plt.subplots(1, 2, figsize=(12.0, 4.8))

    ax[0].plot(Ms, asym, "o-", color="C3", ms=9, lw=2, label="asym = R_co − R_counter (χ=1.0)")
    # the chi=0 point (M=0.9) overlies the chi=1 point -> chi-independence
    chi0 = [d for d in DATA if d[1] == 0.0]
    ax[0].plot([d[0] for d in chi0], [d[4] for d in chi0], "s", color="C0", ms=11, mfc="none",
               label="χ=0.0 (overlies → χ-independent)")
    ax[0].axhline(HANDEDNESS_FLOOR, ls=":", color="k", lw=1.2,
                  label=f"handedness floor {HANDEDNESS_FLOOR:.1e}")
    ax[0].set_yscale("log")
    ax[0].set_xlabel("drive Mach M (rotation)")
    ax[0].set_ylabel("asymmetry  R_co − R_counter")
    ax[0].set_xlim(0.82, 1.08)
    ax[0].set_title(
        "Frame-dragging asymmetry vs M (CITED, not re-run)\n"
        f"~8 orders above floor; scales with M; χ-independent"
    )
    ax[0].legend(fontsize=8, loc="center right")
    ax[0].grid(alpha=0.2, which="both")

    x = range(len(Ms))
    ax[1].bar([i - 0.18 for i in x], Rco, 0.36, color="C3", label="R_co (m=+1)")
    ax[1].bar([i + 0.18 for i in x], Rct, 0.36, color="C0", label="R_counter (m=−1)")
    ax[1].set_xticks(list(x))
    ax[1].set_xticklabels([f"M={m}" for m in Ms])
    ax[1].set_ylabel("reflectivity R")
    ax[1].set_title(
        "R_co > R_counter at every M (WEAK, transient)\n"
        "FRAME-DRAGGING — NOT the cholesteric-Bragg valve"
    )
    ax[1].legend(fontsize=8)
    ax[1].grid(alpha=0.2, axis="y")

    fig.suptitle(f"source: {SOURCE}", fontsize=8, y=1.005)
    fig.tight_layout()
    p = OUT / "frame_drag_asymmetry.png"
    fig.savefig(p, dpi=120, bbox_inches="tight")
    plt.close(fig)

    print(f"[frame-drag] source: {SOURCE} (cited, not re-run)")
    for m, c, rco, rct, a in DATA:
        print(f"[frame-drag]   M={m} χ={c}: R_co={rco:.6f} R_counter={rct:.6f} asym={a:+.6f}")
    print(f"[frame-drag] handedness floor = {HANDEDNESS_FLOOR:.3e}; asym ~ 8 orders above")
    print(f"[frame-drag] figure -> {p}")
    return {"source": SOURCE, "floor": HANDEDNESS_FLOOR, "data": DATA, "figure": p.name}


if __name__ == "__main__":
    main()
