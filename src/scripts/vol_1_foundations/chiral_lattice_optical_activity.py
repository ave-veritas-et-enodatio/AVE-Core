#!/usr/bin/env python
"""
Genesis v9 Phase-0 driver — the two smokes on the chiral trivalent lattice.

Standalone analysis driver (has __main__; NOT a pytest test). Prints the full
Smoke A (consistency gate) and Smoke B (optical-activity source = ring writhe)
batteries on both srs enantiomorphs + the achiral diamond control.

PHASE-0 scaffold. NO genesis run. See
research/2026-06-11_genesis-v9-chiral-lattice_design.md (incl. the §0
adjudication flag: v9 re-opens the 2026-06-07 lattice-net resolution-of-record).

Run:  PYTHONPATH=src python src/scripts/vol_1_foundations/chiral_lattice_optical_activity.py
"""

import numpy as np

from ave.core import chiral_lattice as cl


def smoke_a(L=6, steps=200):
    """Consistency gate: unitarity, eigenvalues, energy conservation, isotropy."""
    S3 = cl.scatter_matrix(3)
    S4 = cl.scatter_matrix(4)
    unit = float(np.abs(S3.T @ S3 - np.eye(3)).max())
    eig = np.abs(np.linalg.eigvals(S3))
    reduces = bool(np.allclose(S4, 0.5 * np.ones((4, 4)) - np.eye(4)))

    net = cl.build_srs_net(L, "right")
    conn = net.connect_index()
    i0 = int(np.where(net.interior_mask)[0][0])
    V = np.zeros((net.n_nodes, 3))
    V[i0] = 1.0
    E0 = cl.lattice_energy(V)
    drift = 0.0
    for _ in range(steps):
        V = cl.scalar_tlm_step(net, V, S3, conn)
        drift = max(drift, abs(cl.lattice_energy(V) - E0) / E0)
    E = np.sum(V * V, axis=1)
    d = net.pos - net.pos[i0]
    d -= net.box * np.round(d / net.box)
    rms = np.sqrt(np.sum(E[:, None] * d**2, axis=0) / E.sum())

    print("=" * 70)
    print("SMOKE A — CONSISTENCY GATE (lattice change must not break the physics)")
    print("=" * 70)
    print("  trivalent scatter S_ij = 2/3 - delta_ij  (derived from Op5, n=3)")
    print(f"  unitarity |SᵀS - I|max         = {unit:.2e}   (canon diamond: 2.2e-16)")
    print(f"  eigenvalue moduli              = {np.round(eig, 6)}   (target all 1.000)")
    print(f"  n=4 reduces to canon ½-δ       = {reduces}")
    print(f"  closed-system energy drift     = {drift:.2e}   (target < 1e-10)")
    print(f"  point-source RMS spread x,y,z  = {np.round(rms, 3)}")
    print(f"  dispersion isotropy ratio      = {rms.min() / rms.max():.3f}   (target > 0.9)")
    passA = unit < 1e-12 and np.allclose(eig, 1.0, atol=1e-12) and reduces and drift < 1e-10 and (
        rms.min() / rms.max() > 0.9
    )
    print(f"  --> SMOKE A: {'PASS' if passA else 'FAIL'}")
    return passA


def smoke_b(L=6):
    """Optical-activity source: writhe (helicity) of the shortest closed circuits."""
    wr_r, sr, nr, ln_r = cl.net_ring_writhe(cl.build_srs_net(L, "right"))
    wr_l, sl, nl, ln_l = cl.net_ring_writhe(cl.build_srs_net(L, "left"))
    wr_d, sd, nd, ln_d = cl.net_ring_writhe(cl.build_diamond_net(L))

    print("=" * 70)
    print("SMOKE B — OPTICAL-ACTIVITY SOURCE (writhe of shortest circuits)")
    print("=" * 70)
    print(f"  srs-right  (I4_1 32) : writhe = {wr_r:+.5e}  (std {sr:.1e}, {nr} rings, len {ln_r})")
    print(f"  srs-left   (I4_3 32) : writhe = {wr_l:+.5e}  (std {sl:.1e}, {nl} rings, len {ln_l})")
    print(f"  diamond    (control) : writhe = {wr_d:+.5e}  (std {sd:.1e}, {nd} rings, len {ln_d})")
    nonzero = abs(wr_r) > 1e-3
    flipped = wr_r * wr_l < 0 and abs(wr_r + wr_l) < 1e-2 * abs(wr_r)
    control0 = abs(wr_d) < 0.05 * abs(wr_r)
    print(f"  chiral net carries helicity    : {nonzero}")
    print(f"  enantiomorphs opposite+equal   : {flipped}")
    print(f"  achiral control ~ zero         : {control0}")
    passB = nonzero and flipped and control0
    verdict_b = (
        "PASS — slats are real, Phase-1 armed (pending §0 + Grant)"
        if passB
        else "FAIL — lattice-chirality hypothesis takes a structural hit (report honestly)"
    )
    print(f"  --> SMOKE B: {verdict_b}")
    return passB


def main():
    print("\nGENESIS v9 — PHASE-0 SCAFFOLD SMOKES (chiral trivalent lattice)\n")
    a = smoke_a()
    print()
    b = smoke_b()
    print("\n" + "=" * 70)
    print("PHASE-0 VERDICT:")
    print(f"  Smoke A (consistency) : {'PASS' if a else 'FAIL'}")
    print(f"  Smoke B (optical act) : {'PASS' if b else 'FAIL'}")
    print("  NOTE: Phase-1 freeze is gated on the §0 adjudication (v9 re-opens the")
    print("  2026-06-07 lattice-net resolution-of-record) AND on Grant's prereg freeze.")
    print("=" * 70)


if __name__ == "__main__":
    main()
