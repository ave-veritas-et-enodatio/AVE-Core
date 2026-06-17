#!/usr/bin/env python
"""
K4/srs Zone-Edge Nyquist sweep — empirical settle of the two-k_max contradiction.

Prereg (FROZEN): research/2026-06-16_k4-zone-edge-nyquist-settle_prereg_FROZEN.md

The corpus carries TWO values both labeled "K4 Nyquist limit / k_max", ~5.4x apart:
  * 0.577 / ell_node  (= 1/sqrt(3), the 3D-TLM network-velocity factor)
      boundary-observables-m-q-j.md:87 ; chiral_lattice_dynamics.py:48 ANALYTIC_NETWORK_FACTOR
  * pi / ell_node     (the idealized simple-cubic Brillouin/Nyquist zone edge)
      paley-wiener-hilbert.md:10 ; ave-analytical-toolkit-index.md:179 ;
      spectral_gap.brillouin_zone_edge()

This driver does NOT rebuild any solver. It exercises the EXISTING extractor
`ave.core.chiral_lattice_dynamics.measure_dispersion` (docstring: "small-k scalar
dispersion") across the FULL commensurate-m range to the axis Nyquist, reads off
where the band tops out (omega maximal, group velocity dw/dk -> 0), and compares
the measured band-top k_max against BOTH 0.577/ell_node and pi/ell_node.

UNITS (load-bearing, prereg §2): measure_dispersion returns k in rad/a_cell. One
NN bond == one ell_node by construction (build_srs_net a_cell=2*sqrt(2) => c_link=1).
So k_in_ell_node_units = k[rad/a_cell] * c_link[a_cell/bond] = rad per NN-bond = rad/ell_node.

substrate-native-check: discrete scatter+connect TLM (NOT Lagrangian/continuum);
scalar V-sector; A46 coords match (lattice wavevector vs lattice wavevector);
CLOSED (no PML); saturation OFF. consistency-vs-emergence: CONSISTENCY-class.

Run:  PYTHONPATH=src python src/scripts/vol_1_foundations/k4_zone_edge_nyquist_sweep.py
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core import chiral_lattice as cl  # noqa: E402
from ave.core import chiral_lattice_dynamics as cld  # noqa: E402
from ave.core.constants import C_0, L_NODE  # noqa: E402 — canonical constants, never hard-coded

OUT_FIG = Path(__file__).parent / "genesis_v9_figs"
OUT_FIG.mkdir(exist_ok=True)
RESULT_JSON = (
    Path(__file__).resolve().parents[3]
    / "research"
    / "2026-06-16_k4-zone-edge-nyquist-settle_result.json"
)

# Corpus reference values (rad / ell_node)
K_NETWORK_FACTOR = cld.ANALYTIC_NETWORK_FACTOR  # 0.577 = 1/sqrt(3) (a VELOCITY, mislabeled as k_max)
K_BRILLOUIN_PI = np.pi  # pi/ell_node, the idealized cubic Brillouin edge

# Bin tolerances (FROZEN in prereg §4)
TOL_0577 = 0.10
TOL_PI = 0.30


def axis_nyquist_m(net: cl.LatticeNet, axis: int = 2) -> int:
    """Commensurate Nyquist mode integer along `axis`: (#distinct planes)/2."""
    planes = np.unique(np.round(net.pos[:, axis], 6))
    return max(1, len(planes) // 2)


def sweep_to_zone_edge(net: cl.LatticeNet, axis: int = 2, n_steps: int = 2500) -> dict:
    """Sweep measure_dispersion over m=1..m_nyq; return k(rad/ell_node), omega, band-top."""
    c_link = cld.mean_bond_length(net)  # a_cell-lengths per NN bond == ell_node (by construction)
    m_nyq = axis_nyquist_m(net, axis)
    ms = tuple(range(1, m_nyq + 1))
    disp = cld.measure_dispersion(net, axis=axis, m_values=ms, n_steps=n_steps)

    k_acell = np.array([k for k, _, _ in disp])
    omega = np.array([w for _, w, _ in disp])
    c_of_k = np.array([c for _, _, c in disp])
    k_ell = k_acell * c_link  # -> rad / ell_node
    cf = c_of_k / c_link  # dimensionless phase-velocity factor c(k)/c_link

    # band-top = max omega; group velocity from finite differences
    i_top = int(np.argmax(omega))
    dwdk = np.gradient(omega, k_ell)
    k_top = float(k_ell[i_top])
    w_top = float(omega[i_top])

    # low-k phase-velocity factor (the thing 0.577 actually IS): c(k->0)/c_link
    c0_factor = float(cf[0])

    return {
        "name": net.name,
        "handedness": net.handedness,
        "degree": net.degree,
        "n_nodes": net.n_nodes,
        "axis": axis,
        "m_nyq": m_nyq,
        "c_link_acell_per_bond": float(c_link),
        "plane_spacing_acell": float(
            np.min(np.diff(np.unique(np.round(net.pos[:, axis], 6))))
        ),
        "m": list(ms),
        "k_rad_per_ell_node": k_ell.tolist(),
        "omega_rad_per_step": omega.tolist(),
        "phase_velocity_factor_c_of_k_over_c_link": cf.tolist(),
        "group_velocity_dwdk": dwdk.tolist(),
        "band_top_m": int(ms[i_top]),
        "band_top_k_rad_per_ell_node": k_top,
        "band_top_omega_rad_per_step": w_top,
        "band_top_group_velocity": float(dwdk[i_top]),
        "low_k_phase_velocity_factor_c0_over_c_link": c0_factor,
    }


def classify_bin(band_top_k: float) -> tuple[str, dict]:
    """Apply the FROZEN bins (prereg §4) to a band-top k (rad/ell_node)."""
    d_0577 = abs(band_top_k - K_NETWORK_FACTOR)
    d_pi = abs(band_top_k - K_BRILLOUIN_PI)
    # geometry-rescaled image of pi: srs axis-2 plane spacing is ell/sqrt2 => axis edge ~ sqrt2*pi.
    # The pi-bin admits "at pi OR its geometry-rescaled image AND decisively far from 0.577".
    detail = {
        "dist_to_0.577": d_0577,
        "dist_to_pi": d_pi,
        "ratio_to_pi": band_top_k / K_BRILLOUIN_PI,
        "ratio_to_0.577": band_top_k / K_NETWORK_FACTOR,
    }
    if d_0577 <= TOL_0577:
        return "K4-CUTS-AT-~0.577/ell_node", detail
    far_from_0577 = d_0577 > 1.0  # decisively not 0.577
    at_pi = d_pi <= TOL_PI
    geom_image_of_pi = abs(band_top_k - np.sqrt(2.0) * np.pi) <= TOL_PI
    if (at_pi or geom_image_of_pi) and far_from_0577:
        return "K4-CUTS-AT-~pi/ell_node", detail
    return "NEITHER (report measured value)", detail


def main() -> None:
    print("\n" + "=" * 78)
    print("K4/srs ZONE-EDGE NYQUIST SWEEP — settle 0.577/ell_node vs pi/ell_node")
    print("=" * 78)
    print(f"  canonical ell_node = {L_NODE:.6e} m   c = {C_0:.6e} m/s")
    print(f"  corpus value A: 0.577/ell_node = 1/sqrt(3) = {K_NETWORK_FACTOR:.5f}  rad/ell_node")
    print(f"  corpus value B: pi/ell_node    = {K_BRILLOUIN_PI:.5f}  rad/ell_node")
    print("  (A = chiral_lattice_dynamics.ANALYTIC_NETWORK_FACTOR = the 3D-TLM network VELOCITY;")
    print("   B = spectral_gap.brillouin_zone_edge() = idealized simple-cubic Brillouin edge)")
    print("-" * 78)

    L = 8
    nets = {
        "srs-R": cl.build_srs_net(L, "right"),
        "srs-L": cl.build_srs_net(L, "left"),
        "diamond": cl.build_diamond_net(L),
    }

    results = {}
    for nm, net in nets.items():
        r = sweep_to_zone_edge(net, axis=2)
        bin_, detail = classify_bin(r["band_top_k_rad_per_ell_node"])
        r["verdict_bin"] = bin_
        r["bin_detail"] = detail
        results[nm] = r
        print(
            f"  {nm:8s} deg={net.degree}  m_nyq={r['m_nyq']:>2}  "
            f"plane-spacing={r['plane_spacing_acell']:.4f} a_cell  "
            f"c_link={r['c_link_acell_per_bond']:.4f}"
        )
        print(
            f"           band-top: m={r['band_top_m']:>2}  "
            f"k_max={r['band_top_k_rad_per_ell_node']:.4f} rad/ell_node  "
            f"w_max={r['band_top_omega_rad_per_step']:.4f}  "
            f"dw/dk@top={r['band_top_group_velocity']:+.4f}"
        )
        print(
            f"           low-k velocity factor c(k->0)/c_link = "
            f"{r['low_k_phase_velocity_factor_c0_over_c_link']:.5f}   "
            f"(== 0.577? {abs(r['low_k_phase_velocity_factor_c0_over_c_link']-K_NETWORK_FACTOR)<0.01})"
        )
        print(
            f"           -> BIN: {bin_}   "
            f"(d_0.577={detail['dist_to_0.577']:.3f}, d_pi={detail['dist_to_pi']:.3f}, "
            f"k/pi={detail['ratio_to_pi']:.3f})"
        )

    # L-stability of the srs-R band-top
    print("-" * 78)
    print("  L-stability of srs-R band-top k_max (rad/ell_node):")
    l_stab = {}
    for Lx in (6, 8, 10):
        rr = sweep_to_zone_edge(cl.build_srs_net(Lx, "right"), axis=2)
        l_stab[str(Lx)] = {
            "band_top_m": rr["band_top_m"],
            "band_top_k": rr["band_top_k_rad_per_ell_node"],
            "band_top_omega": rr["band_top_omega_rad_per_step"],
        }
        print(
            f"    L={Lx:>2}: m={rr['band_top_m']:>2}  "
            f"k_max={rr['band_top_k_rad_per_ell_node']:.4f}  "
            f"w_max={rr['band_top_omega_rad_per_step']:.4f}"
        )

    # Overall verdict (srs is the load-bearing chiral net; diamond is the cubic control)
    srs_bin = results["srs-R"]["verdict_bin"]
    enantiomorph_agree = results["srs-R"]["verdict_bin"] == results["srs-L"]["verdict_bin"]
    print("=" * 78)
    print(f"  VERDICT (chiral srs net): {srs_bin}")
    print(f"  enantiomorph agreement  : {enantiomorph_agree}")
    print(f"  diamond (cubic control) : band-top k={results['diamond']['band_top_k_rad_per_ell_node']:.4f}"
          f" rad/ell_node, w_max={results['diamond']['band_top_omega_rad_per_step']:.4f}")
    print("=" * 78)

    payload = {
        "prereg": "research/2026-06-16_k4-zone-edge-nyquist-settle_prereg_FROZEN.md",
        "class": "CONSISTENCY",
        "canonical_constants": {"L_NODE_m": L_NODE, "C_0_m_per_s": C_0},
        "corpus_values_rad_per_ell_node": {
            "value_A_0.577_network_factor": K_NETWORK_FACTOR,
            "value_B_pi_brillouin_edge": K_BRILLOUIN_PI,
        },
        "L_used": L,
        "axis": 2,
        "verdict_bin_srs": srs_bin,
        "enantiomorph_agreement": enantiomorph_agree,
        "L_stability_srs_R": l_stab,
        "per_net": results,
    }
    RESULT_JSON.write_text(json.dumps(payload, indent=2))
    print(f"  [json] {RESULT_JSON}")

    _fig(results)


def _fig(results: dict) -> None:
    fig, ax = plt.subplots(figsize=(8.5, 5.0))
    colors = {"srs-R": "#c0392b", "srs-L": "#2980b9", "diamond": "#27ae60"}
    for nm, r in results.items():
        k = np.array(r["k_rad_per_ell_node"])
        w = np.array(r["omega_rad_per_step"])
        ax.plot(k, w, "o-", color=colors[nm], ms=4,
                label=f"{nm}  band-top k={r['band_top_k_rad_per_ell_node']:.2f}/ℓ")
    ax.axvline(K_NETWORK_FACTOR, ls=":", color="k", lw=1.2,
               label=f"corpus 0.577/ℓ (=1/√3, a VELOCITY)")
    ax.axvline(K_BRILLOUIN_PI, ls="--", color="gray", lw=1.2,
               label=f"corpus π/ℓ = {K_BRILLOUIN_PI:.2f} (cubic Brillouin edge)")
    ax.set_xlabel("wavevector k along axis  [rad / ℓ_node]")
    ax.set_ylabel("ω(k)  [rad / step]")
    ax.set_title("K4/srs full-range dispersion — where does the band top out?\n"
                 "(band saturates dω/dk→0; 0.577 is the low-k SLOPE, not the cutoff)")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)
    p = OUT_FIG / "k4_zone_edge_nyquist.png"
    fig.savefig(p, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {p}")


if __name__ == "__main__":
    main()
