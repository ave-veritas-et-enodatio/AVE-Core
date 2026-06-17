"""L0 — the medium (LC/TLM lattice) on the chiral srs grid.

Each test is a falsifiable physics CLAIM with a PRE-REGISTERED pass/fail bin in
its docstring (frozen BEFORE running). CONSISTENCY-class (T0.1, T0.3) plus one
Class-A IDENTITY (T0.2 Z₀): the engine MUST pass these to be a valid medium.

Medium: the scalar TLM layer of the v9 chiral-srs grid
(`ave.core.chiral_lattice`) for the unitarity + isotropy checks; the canonical
bond-LC mapping (`bond_lc`) for the impedance identity. These OVERLAP with the
existing Phase-0 smokes (`test_chiral_lattice_smokes.py`) by design — the
acceptance suite re-asserts them as the engine's L0 regression gate with frozen
bins, NOT as new physics.
"""

from __future__ import annotations

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld
from ave.core.constants import EPSILON_0, MU_0, Z_0

from . import _medium as M
from . import _viz as VZ


# ─────────────────────────────────────────────────────────────────────────────
# T0.1 — energy conservation: the TLM scatter is unitary (Γ²+T²=1)
# ─────────────────────────────────────────────────────────────────────────────
def test_t0_1_energy_conservation_unitary_scatter():
    """T0.1 [CONSISTENCY] — a bare-lattice wave conserves total energy.

    The one-step operator M = Connect·blockdiag(S) is orthogonal: the Op5
    degree-3 shunt scatter S = (2/3)J − I satisfies SᵀS = I (Γ²+T²=1 every
    scatter), and Connect is a port permutation. So Σ|V_inc|² is conserved
    exactly and all eigenvalue moduli are 1.

    Two assertions: (1) the scatter is provably unitary (SᵀS=I, |eig|=1) AND the
    connect is a permutation — the ANALYTIC backbone; (2) the dynamical total
    energy H stays flat to integrator floor over a LONG run — the empirical
    confirmation (Rule 10: run the driver, don't trust the algebra alone).

    PRE-REGISTERED BINS:
      * PASS : SᵀS = I (< 1e-12) AND |eig(S)| = 1 (< 1e-12) AND connect is a
               permutation AND max relative energy drift < 1e-10 over >= 2000 steps.
      * FAIL : any unitarity check fails OR energy drift >= 1e-10 (the bare
               medium is lossy / gains energy).
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(8, "right")
    S = cl.scatter_matrix(net.degree)

    # (1) analytic unitarity backbone
    sts_err = float(np.abs(S.T @ S - np.eye(net.degree)).max())
    eig_err = float(np.abs(np.abs(np.linalg.eigvals(S)) - 1.0).max())
    is_perm = cld.connect_is_permutation(net)

    # (2) dynamical confirmation over a long run
    seed = int(np.where(net.interior_mask)[0][0])
    V = np.zeros((net.n_nodes, net.degree))
    V[seed] = 1.0
    E0 = cl.lattice_energy(V)
    conn = net.connect_index()
    drift = 0.0
    for _ in range(2000):
        V = cl.scalar_tlm_step(net, V, S, conn)
        drift = max(drift, abs(cl.lattice_energy(V) - E0) / E0)

    print("\n--- T0.1 energy conservation / unitary scatter (srs, N=8, 2000 steps) ---")
    print(f"  ‖SᵀS − I‖∞        : {sts_err:.3e}  (PASS < 1e-12)")
    print(f"  max ||eig(S)| − 1| : {eig_err:.3e}  (PASS < 1e-12)")
    print(f"  connect is permutation: {is_perm}")
    print(f"  max relative energy drift: {drift:.3e}  (PASS < 1e-10)")

    assert sts_err < 1e-12, f"FAIL: scatter not unitary — ‖SᵀS−I‖={sts_err:.3e}"
    assert eig_err < 1e-12, f"FAIL: scatter eigenvalues off unit circle — {eig_err:.3e}"
    assert is_perm, "FAIL: connect is not a port permutation"
    assert drift < 1e-10, f"FAIL: bare medium not energy-conserving — drift {drift:.3e}"

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        V_seed = np.zeros((net.n_nodes, net.degree))
        V_seed[seed] = 1.0
        e_trace = VZ.record_scalar_energy(net, V_seed, 2000)
        # a final-state field snapshot: energy per z-plane after the run
        Vf = V_seed.copy()
        for _ in range(2000):
            Vf = cl.scalar_tlm_step(net, Vf, S, conn)
        z = net.pos[:, 2]
        planes = np.unique(np.round(z, 6))
        pidx = np.searchsorted(planes, np.round(z, 6))
        prof = np.zeros(len(planes))
        np.add.at(prof, pidx, np.sum(Vf * Vf, axis=1))

        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            VZ._panel_energy(ax1, e_trace,
                             drift_floor_label=f"point-source seed, 2000 steps")
            ax2.plot(planes, prof, color="#1f77b4")
            ax2.set_xlabel("z (cartesian)")
            ax2.set_ylabel("|V|^2 per plane")
            ax2.set_title("field snapshot at t=2000 (spread point source)")

        path = VZ.save_simple_figure(
            "T0.1", "energy conservation / unitary scatter (scalar TLM)", _draw)
        print(f"  [viz] energy figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T0.2 — characteristic impedance Z₀ = √(μ₀/ε₀), uniform
# ─────────────────────────────────────────────────────────────────────────────
def test_t0_2_characteristic_impedance():
    """T0.2 [IDENTITY (Class A)] — Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω, uniform.

    The srs medium's per-bond LC mapping (`chiral_lattice.bond_lc`) derives the
    line L, C from the canonical Z₀, c₀: L = Z₀/c₀, C = 1/(Z₀·c₀), so
    √(L/C) = Z₀. This is a Class-A IDENTITY (Z₀ = √(μ₀/ε₀) is the DEFINITION of
    the characteristic impedance) — not a prediction. The test confirms the
    medium's bond-LC is wired to the canonical constants and is uniform
    (same on every bond — the unstrained Phase-0 lattice), and that the
    round-trip √(L/C) and 1/√(LC) recover Z₀ and c₀.

    consistency-vs-emergence tag: Class A — 0.00% by definition; the value comes
    from CODATA-pinned μ₀, ε₀ through `ave.core.constants`, not an emergence.

    PRE-REGISTERED BINS:
      * PASS : √(L/C) == Z₀ AND Z₀ == √(μ₀/ε₀) to < 1e-9 relative; bond-LC is
               uniform (no per-bond variation — unstrained lattice).
      * FAIL : any relative mismatch >= 1e-9.
    """
    M.assert_canonical_constants()
    lc = cl.bond_lc()
    z_from_lc = np.sqrt(lc["L_per"] / lc["C_per"])
    c_from_lc = 1.0 / np.sqrt(lc["L_per"] * lc["C_per"])
    z_from_mu_eps = np.sqrt(MU_0 / EPSILON_0)

    rel_z_lc = abs(z_from_lc - Z_0) / Z_0
    rel_z_def = abs(z_from_mu_eps - Z_0) / Z_0
    rel_c = abs(c_from_lc - lc["c0"]) / lc["c0"]

    print("\n--- T0.2 characteristic impedance (Class-A identity) ---")
    print(f"  Z₀ (canonical)        : {Z_0:.6f} Ω")
    print(f"  √(L/C) from bond-LC   : {z_from_lc:.6f} Ω   (rel {rel_z_lc:.2e})")
    print(f"  √(μ₀/ε₀)              : {z_from_mu_eps:.6f} Ω   (rel {rel_z_def:.2e})")
    print(f"  1/√(LC) vs c₀         : {c_from_lc:.1f} vs {lc['c0']:.1f}  (rel {rel_c:.2e})")

    assert rel_z_lc < 1e-9, f"FAIL: √(L/C) != Z₀ — rel {rel_z_lc:.2e}"
    assert rel_z_def < 1e-9, f"FAIL: Z₀ != √(μ₀/ε₀) — rel {rel_z_def:.2e}"
    assert rel_c < 1e-9, f"FAIL: 1/√(LC) != c₀ — rel {rel_c:.2e}"

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        labels = ["Z₀ canonical\n(√μ₀/ε₀)", "√(L/C)\nfrom bond-LC", "√(μ₀/ε₀)\nidentity"]
        vals = [Z_0, z_from_lc, z_from_mu_eps]
        rels = [0.0, rel_z_lc, rel_z_def]

        def _draw(fig):
            ax = fig.subplots(1, 1)
            bars = ax.bar(labels, vals, color=["#1f77b4", "#2ca02c", "#9467bd"])
            ax.set_ylabel("characteristic impedance (Ω)")
            ax.set_ylim(0, max(vals) * 1.15)
            ax.set_title(
                "Class-A IDENTITY (consistency-vs-emergence): "
                "value is CODATA-pinned via ave.core.constants, NOT an emergence"
            )
            for b, v, r in zip(bars, vals, rels):
                ax.annotate(f"{v:.4f} Ω\nrel {r:.1e}",
                            xy=(b.get_x() + b.get_width() / 2, v),
                            xytext=(0, 4), textcoords="offset points",
                            ha="center", fontsize=9)

        path = VZ.save_simple_figure(
            "T0.2", "characteristic impedance Z₀ = √(μ₀/ε₀)", _draw)
        print(f"  [viz] impedance-identity figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T0.3 — isotropy: no spurious anisotropy beyond the known lattice factor
# ─────────────────────────────────────────────────────────────────────────────
def test_t0_3_isotropy_no_spurious_anisotropy():
    """T0.3 [CONSISTENCY] — wave speed isotropic up to the known lattice-projection.

    The plan: do NOT re-litigate the √2/√3 convention (already mapped — the srs
    trivalent link-line factor is 1/√3, `ANALYTIC_NETWORK_FACTOR`). Confirm only
    that there is NO SPURIOUS anisotropy beyond it: (1) a point pulse spreads
    axis-isotropically (rms spread ratio min/max near 1), and (2) the k→0
    network-velocity factor matches the analytic 1/√3 (so the measured speed sits
    on the known projection, not a spurious direction-dependent value).

    PRE-REGISTERED BINS:
      * PASS : point-pulse rms-spread isotropy ratio (min/max) > 0.9 AND the k→0
               network factor matches 1/√3 to < 2% (the known projection, no
               spurious offset).
      * FAIL : isotropy ratio <= 0.9 (spurious spatial anisotropy) OR network
               factor off 1/√3 by >= 2% (spurious speed offset).
    """
    M.assert_canonical_constants()
    net = cl.build_srs_net(6, "right")
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()

    # (1) point-pulse spatial isotropy
    i0 = int(np.where(net.interior_mask)[0][0])
    V = np.zeros((net.n_nodes, net.degree))
    V[i0] = 1.0
    for _ in range(120):
        V = cl.scalar_tlm_step(net, V, S, conn)
    E = np.sum(V * V, axis=1)
    d = net.pos - net.pos[i0]
    d -= net.box * np.round(d / net.box)
    rms = np.sqrt(np.sum(E[:, None] * d**2, axis=0) / E.sum())
    iso = float(rms.min() / rms.max())

    # (2) network-velocity factor vs analytic 1/√3
    nf = cld.network_velocity_factor(cl.build_srs_net(8, "right"), axis=2, n_steps=600)
    factor_err = abs(nf["factor"] - cld.ANALYTIC_NETWORK_FACTOR) / cld.ANALYTIC_NETWORK_FACTOR

    print("\n--- T0.3 isotropy / no spurious anisotropy (srs) ---")
    print(f"  point-pulse rms spread (x,y,z): {rms[0]:.3f}, {rms[1]:.3f}, {rms[2]:.3f}")
    print(f"  isotropy ratio (min/max)      : {iso:.4f}  (PASS > 0.9)")
    print(f"  k→0 network factor            : {nf['factor']:.5f}  vs 1/√3={cld.ANALYTIC_NETWORK_FACTOR:.5f}")
    print(f"  factor rel error vs 1/√3      : {factor_err:.4f}  (PASS < 0.02)")

    assert iso > 0.9, f"FAIL: spurious spatial anisotropy — ratio {iso:.4f}"
    assert factor_err < 0.02, (
        f"FAIL: network factor off the known 1/√3 projection — rel {factor_err:.4f}"
    )

    # ── visual-debug layer (additive; never affects pass/fail) ──
    if VZ.viz_enabled():
        # E and d are in scope from the point-pulse spread above
        cks = np.array(nf["c_of_k"])
        kks = np.array(nf["k"])

        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            ax1.bar(["x", "y", "z"], rms, color=["#1f77b4", "#2ca02c", "#9467bd"])
            ax1.set_ylabel("rms spread (cartesian)")
            ax1.set_title(f"point-pulse spread — isotropy ratio {iso:.3f} (PASS>0.9)")
            for i, r in enumerate(rms):
                ax1.annotate(f"{r:.3f}", xy=(i, r), xytext=(0, 3),
                             textcoords="offset points", ha="center", fontsize=9)
            ax2.plot(kks, cks, "o-", color="#2ca02c", label="c(k) measured")
            ax2.axhline(cld.ANALYTIC_NETWORK_FACTOR * nf["c_link"], color="k", ls="--",
                        lw=1.0, label="1/√3 · c_link (analytic)")
            ax2.set_xlabel("k (rad/cartesian)")
            ax2.set_ylabel("c(k) (cartesian/step)")
            ax2.set_title(f"k→0 factor {nf['factor']:.4f} vs 1/√3 (rel {factor_err:.1e})")
            ax2.legend(fontsize=8)

        path = VZ.save_simple_figure(
            "T0.3", "isotropy / no spurious anisotropy (scalar TLM)", _draw)
        print(f"  [viz] isotropy figure -> {path}")
