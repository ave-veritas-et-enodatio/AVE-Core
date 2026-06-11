"""
Electron DEVICE datasheet — Curve (a): Safe Operating Area (SOA).

Bound-state existence vs atomic number Z, from the cavitation number
    C = Z * alpha / n          (de-broglie-standing-wave.md:248)
The n=1 line crosses C = 1 at Z = 1/alpha, where no bound state exists — the
AVE derivation of the maximum atomic number (de-broglie-standing-wave.md:248).

Canonical-source discipline (ave-canonical-source): alpha is taken from the
canonical cold-lattice value alpha^-1 = 4*pi^3 + pi^2 + pi (ALPHA_COLD_INV,
constants.py:204) — NOT a CODATA substitution. This is therefore a
consistency-class curve on a canonical constant, not an emergence claim.

ave-driver-script-honesty: the figure caption states the actual crossing Z
computed from the constant; nothing is fit.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core.constants import ALPHA_COLD_INV  # noqa: E402

OUT = Path(__file__).parent / "_output"
OUT.mkdir(exist_ok=True)

ALPHA = 1.0 / ALPHA_COLD_INV  # canonical cold-lattice alpha (NOT CODATA)


def cavitation_number(Z: np.ndarray, n: int) -> np.ndarray:
    """C = Z*alpha/n — the wake/cavitation number (de-broglie:248)."""
    return Z * ALPHA / n


def main() -> dict:
    Z = np.linspace(1.0, 200.0, 400)
    Z_soa = ALPHA_COLD_INV  # Z = 1/alpha, the n=1 crossing of C=1
    Z_derate = 0.4 * ALPHA_COLD_INV  # C ~ 0.4 onset of relativistic wake (Z~50)

    fig, ax = plt.subplots(1, 1, figsize=(8.0, 5.2))
    for n, color in ((1, "C3"), (2, "C0"), (3, "C2")):
        C = cavitation_number(Z, n)
        ax.plot(Z, C, color=color, lw=2, label=f"n={n}: C = Z·α/{n}")
    ax.axhline(1.0, ls=":", color="k", lw=1.5, label="C = 1 (no bound state)")
    ax.axvline(Z_soa, ls="--", color="C3", lw=1.2)
    ax.axvline(Z_derate, ls="--", color="gray", lw=1.0)
    ax.fill_betweenx([0, 1], 1.0, Z_soa, color="C2", alpha=0.07)
    ax.annotate(
        f"Z = 1/α = {Z_soa:.2f}\n(n=1 SOA edge)",
        xy=(Z_soa, 1.0),
        xytext=(Z_soa - 65, 1.35),
        fontsize=9,
        color="C3",
        arrowprops=dict(arrowstyle="->", color="C3"),
    )
    ax.annotate(
        f"Z ≈ {Z_derate:.0f} (C≈0.4)\nrelativistic-wake derate",
        xy=(Z_derate, 0.4),
        xytext=(Z_derate - 35, 0.62),
        fontsize=8,
        color="gray",
        arrowprops=dict(arrowstyle="->", color="gray"),
    )
    ax.set_xlabel("atomic number Z")
    ax.set_ylabel("cavitation number  C = Z·α/n")
    ax.set_ylim(0, 1.8)
    ax.set_xlim(0, 200)
    ax.set_title(
        "Electron SOA — bound-state existence vs Z\n"
        f"n=1 crosses C=1 at Z=1/α={Z_soa:.2f} "
        f"(canonical α⁻¹=4π³+π²+π; de-broglie:248)"
    )
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    p = OUT / "electron_soa_cavitation.png"
    fig.savefig(p, dpi=120)
    plt.close(fig)

    res = {
        "alpha_inv_canonical": float(ALPHA_COLD_INV),
        "Z_soa_n1": float(Z_soa),
        "Z_derate_onset": float(Z_derate),
        "figure": p.name,
    }
    print(f"[SOA] α⁻¹ (canonical) = {ALPHA_COLD_INV:.4f}")
    print(f"[SOA] n=1 SOA edge Z = 1/α = {Z_soa:.4f}  (C=1, no bound state)")
    print(f"[SOA] relativistic-wake derate onset Z ≈ {Z_derate:.1f} (C≈0.4)")
    print(f"[SOA] figure -> {p}")
    return res


if __name__ == "__main__":
    main()
