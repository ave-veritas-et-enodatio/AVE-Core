#!/usr/bin/env python
"""
Genesis v9 Phase-0 — the two smokes as REAL DYNAMICS on the chiral lattice.

Companion to chiral_lattice_optical_activity.py. That driver reported the static
geometry batteries; THIS driver runs the *dynamical* observers (scatter+connect
dispersion + transverse Bishop transport) and emits two figures.

  Smoke A (CONSISTENCY GATE): small-k scalar dispersion + energy conservation on
    the chiral srs net vs the cubic diamond reference vs the analytic c0. The gate
    is the dimensionless 3D-TLM network-velocity invariant c0/c_link = 1/sqrt(3),
    which the lattice change must NOT break, identically between enantiomorphs.

  Smoke B (OPTICAL ACTIVITY): a transverse polarization frame transported along
    the exact 4_1 screw orbit (the available transverse channel) + the reflection-
    odd ring-writhe pseudoscalar (the load-bearing signed channel). Honest scope:
    the converged *dynamical* polarization-rotation of a propagating packet needs
    the full vector-TLM = Phase-1 (design doc §3); Phase-0 reports the signed
    geometric source + the mirror-odd transverse rotation, with the limitation.

PHASE-0 scaffold. NO genesis run. See
research/2026-06-11_genesis-v9-chiral-lattice_design.md (incl. the §0 adjudication
flag: v9 re-opens the 2026-06-07 lattice-net resolution-of-record).

Run:  PYTHONPATH=src python src/scripts/vol_1_foundations/chiral_lattice_smoke_dynamics.py
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core import chiral_lattice as cl  # noqa: E402
from ave.core import chiral_lattice_dynamics as cld  # noqa: E402

OUT = Path(__file__).parent / "genesis_v9_figs"
OUT.mkdir(exist_ok=True)


def smoke_a(L=8):
    print("=" * 74)
    print("SMOKE A — CONSISTENCY GATE (dynamical: dispersion + energy conservation)")
    print("=" * 74)
    target = cld.ANALYTIC_NETWORK_FACTOR
    nets = {
        "srs-R": cl.build_srs_net(L, "right"),
        "srs-L": cl.build_srs_net(L, "left"),
        "diamond": cl.build_diamond_net(L),
    }
    disp = {}
    rows = {}
    for nm, net in nets.items():
        perm = cld.connect_is_permutation(net)
        drift = cld.energy_drift(net, steps=200)
        nf = cld.network_velocity_factor(net, n_steps=600)
        disp[nm] = nf
        rows[nm] = (perm, drift, nf)
        print(f"  {nm:8s} CONNECT-perm={perm!s:5s}  E-drift={drift:.1e}  "
              f"c0={nf['c0']:.4f}  c_link={nf['c_link']:.4f}  "
              f"factor c0/c_link={nf['factor']:.4f}  (analytic 1/sqrt3={target:.4f})")
    fR, fL = disp["srs-R"]["factor"], disp["srs-L"]["factor"]
    print("  analytic c0          : c_link / sqrt(3)  (3D link-line TLM network velocity)")
    print(f"  enantiomorph match   : |f_R - f_L| = {abs(fR - fL):.2e}  (achiral observable, want ~0)")
    print(f"  chiral-vs-analytic   : |f_srs - 1/sqrt3| = {abs(fR - target):.2e} ({abs(fR-target)/target*100:.2f}%)")
    print(f"  cubic-vs-analytic    : |f_dia - 1/sqrt3| = {abs(disp['diamond']['factor'] - target):.2e}")
    ok = all(
        perm and drift < 1e-10 and abs(nf["factor"] - target) / target < 0.02
        and nf["linearity_spread"] < 0.02
        for (perm, drift, nf) in rows.values()
    ) and abs(fR - fL) < 1e-3
    print(f"  --> SMOKE A: {'PASS' if ok else 'FAIL'}  "
          f"(energy conserved + dispersion reproduces 1/sqrt3 on chiral AND cubic, enantiomorph-invariant)")
    _fig_dispersion(disp, target)
    return ok, disp


def _fig_dispersion(disp, target):
    fig, ax = plt.subplots(figsize=(7, 4.5))
    colors = {"srs-R": "#c0392b", "srs-L": "#2980b9", "diamond": "#27ae60"}
    for nm, nf in disp.items():
        ks = np.array(nf["k"])
        cs = np.array(nf["c_of_k"]) / nf["c_link"]  # dimensionless factor vs k
        ax.plot(ks, cs, "o-", color=colors[nm], label=f"{nm}  (c0/c_link={nf['factor']:.4f})")
    ax.axhline(target, ls="--", color="k", lw=1, label=f"analytic 1/√3 = {target:.4f}")
    ax.set_xlabel("wavevector k along screw/cubic axis (rad / length)")
    ax.set_ylabel("network-velocity factor  c(k) / c_link")
    ax.set_title("Genesis v9 Smoke A — scalar dispersion vs analytic c₀ (3D-TLM 1/√3)")
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(alpha=0.3)
    p = OUT / "smoke_a_dispersion.png"
    fig.savefig(p, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {p}")


def smoke_b(L=6):
    print("=" * 74)
    print("SMOKE B — OPTICAL ACTIVITY (dynamical: transverse transport + writhe source)")
    print("=" * 74)
    # (B1) reflection-odd writhe pseudoscalar — the load-bearing signed channel
    wr_r, sr, nr, lr = cl.net_ring_writhe(cl.build_srs_net(L, "right"))
    wr_l, sl, nl, ll = cl.net_ring_writhe(cl.build_srs_net(L, "left"))
    wr_d, sd, nd, ld = cl.net_ring_writhe(cl.build_diamond_net(L))
    print("  (B1) ring-writhe pseudoscalar  [signed, reflection-odd, box-independent]")
    print(f"       srs-R (I4_1 32) : {wr_r:+.5e}  (std {sr:.1e}, {nr} rings, len {lr})")
    print(f"       srs-L (I4_3 32) : {wr_l:+.5e}  (std {sl:.1e}, {nl} rings, len {ll})")
    print(f"       diamond control : {wr_d:+.5e}  (std {sd:.1e}, {nd} rings, len {ld})")

    # (B2) transverse Bishop transport along the exact screw orbit
    cR = cld.screw_orbit_helix("right", n_turns=3)
    cM = cR.copy()
    cM[:, 0] = -cM[:, 0]  # explicit mirror = true left enantiomorph helix
    cL = cld.screw_orbit_helix("left", n_turns=3)  # INDEPENDENTLY-found left screw (4_3)
    _, _, rR = cld.bishop_transport_rotation(cR)
    _, _, rM = cld.bishop_transport_rotation(cM)
    _, _, rL = cld.bishop_transport_rotation(cL)
    tR, tM = cld.helix_signed_torsion(cR), cld.helix_signed_torsion(cM)
    print("  (B2) transverse Bishop-transport rotation along the exact 4_1 screw orbit")
    print(f"       srs-R screw helix         : Δθ/L = {np.degrees(rR):+8.3f} deg/unit  τ={tR:+.4f}")
    print(f"       mirror(srs-R) = true srs-L: Δθ/L = {np.degrees(rM):+8.3f} deg/unit  τ={tM:+.4f}")
    print(f"       --> MIRROR-ODD exact: Δθ/L sign flips, |sum|={abs(rR + rM):.1e}, magnitudes match")
    print(f"       srs-L INDEPENDENT 4_3 axis : Δθ/L = {np.degrees(rL):+8.3f} deg/unit  "
          "(same sign as srs-R: single-screw-ray is handedness-AMBIGUOUS)")

    # honest verdicts
    nonzero = abs(wr_r) > 1e-3 and abs(rR) > 1e-3
    flipped_writhe = wr_r * wr_l < 0 and abs(wr_r + wr_l) < 1e-2 * abs(wr_r)
    flipped_transport = rR * rM < 0 and abs(rR + rM) < 1e-9 * abs(rR)
    control0 = abs(wr_d) < 0.05 * abs(wr_r)
    print("  verdicts:")
    print(f"       chiral lattice carries signed handedness (writhe & transport nonzero) : {nonzero}")
    print(f"       writhe enantiomorph-odd + zero control (LOAD-BEARING channel)  : {flipped_writhe and control0}")
    print(f"       transverse transport mirror-odd (exact flip under x->-x)  : {flipped_transport}")
    print("  LIMITATION (honest, design §3 + A46):")
    print("       * per-length transport RATE is NOT cleanly converged at Phase-0")
    print("         (discrete 4-gon-per-turn orbit, ~9% wobble) — converged dynamical")
    print("         rotation needs the full vector-TLM = Phase-1.")
    print("       * a single independently-found screw axis is handedness-ambiguous")
    print("         (srs-R 4_1 and srs-L 4_3 helices share sign); the clean SIGNED")
    print("         discriminator is the reflection-odd writhe / the mirror operation.")
    passB = nonzero and flipped_writhe and control0 and flipped_transport
    bin_ = "ROTATES-ENANTIOMORPH-ODD" if passB else "AMBIGUOUS"
    detail = "signed source + mirror-odd transverse rotation, zero on control" if passB else "see limitation"
    print(f"  --> SMOKE B: {bin_}  ({detail})")
    _fig_smoke_b(wr_r, wr_l, wr_d, rR, rM, rL, cR, cM)
    return passB, bin_, dict(wr_r=wr_r, wr_l=wr_l, wr_d=wr_d, rR=rR, rM=rM, rL=rL, tR=tR, tM=tM)


def _fig_smoke_b(wr_r, wr_l, wr_d, rR, rM, rL, cR, cM):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.4))
    # left: writhe pseudoscalar bars (the load-bearing signed channel)
    labels = ["srs-R\n(I4₁32)", "srs-L\n(I4₃32)", "diamond\n(control)"]
    vals = [wr_r, wr_l, wr_d]
    a1.bar(labels, vals, color=["#c0392b", "#2980b9", "#27ae60"])
    a1.axhline(0, color="k", lw=0.8)
    a1.set_ylabel("mean ring-writhe (reflection-odd pseudoscalar)")
    a1.set_title("Smoke B (B1) — signed handedness source\n(opposite sign, zero on control)")
    for i, v in enumerate(vals):
        a1.text(i, v + (0.003 if v >= 0 else -0.004), f"{v:+.4f}", ha="center", fontsize=8)
    a1.grid(alpha=0.3, axis="y")
    # right: transverse transport helices (right vs its mirror) — mirror-odd rotation
    a2.plot(cR[:, 0], cR[:, 2], "o-", color="#c0392b", ms=3, label=f"srs-R helix  Δθ/L={np.degrees(rR):+.1f}°/u")
    a2.plot(cM[:, 0], cM[:, 2], "s-", color="#2980b9", ms=3, label=f"mirror=srs-L  Δθ/L={np.degrees(rM):+.1f}°/u")
    a2.set_xlabel("x (Cartesian)")
    a2.set_ylabel("z along screw axis")
    a2.set_title("Smoke B (B2) — transverse transport\n(exact mirror-odd; rate not converged @P0)")
    a2.legend(fontsize=8)
    a2.grid(alpha=0.3)
    p = OUT / "smoke_b_optical_activity.png"
    fig.savefig(p, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  [figure] {p}")


def main():
    print("\nGENESIS v9 — PHASE-0 SMOKES AS REAL DYNAMICS (chiral trivalent lattice)\n")
    a, _ = smoke_a()
    print()
    b, bin_b, _ = smoke_b()
    print("\n" + "=" * 74)
    print("PHASE-0 DYNAMICAL-SMOKE VERDICT:")
    print(f"  Smoke A (consistency gate) : {'PASS' if a else 'FAIL'}")
    print(f"  Smoke B (optical activity) : {bin_b}")
    print("  NOTE: Phase-1 freeze is gated on the §0 adjudication (v9 re-opens the")
    print("  2026-06-07 lattice-net resolution-of-record) AND on Grant's prereg freeze.")
    print("=" * 74)


if __name__ == "__main__":
    main()
