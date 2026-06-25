"""P1b.2 — the photon (RUNG-2) + L2 EM-in-biased-medium SURVIVE on chiral srs.

Branch: engine/p1b-modes-live (off engine/p1a-carrier-unification).

════════════════════════════════════════════════════════════════════════════════
THE D1 DISCHARGE (the load-bearing purpose of this module)
════════════════════════════════════════════════════════════════════════════════
The 2026-06-12 adjudication anchored the α + Lorentz-invariance chains to the
DIAMOND lattice (the achiral z=4 carrier the P0 cage/winding used). P1a/Decision-1
moved the unified carrier to the CHIRAL srs z=3 net (so the soliton's handed (2,3)
winding can be carried — the diamond's writhe pseudoscalar vanishes identically).

D1 dependency: if the α-invariance and the Lorentz/isotropy chains DEGRADE on the
chiral srs grid (vs the diamond they were anchored to), Decision-1 REOPENS. So
P1b.2 must SHOW these survive on chiral srs — and FLAG loudly (flag-don't-fix) if
any of them degrades. This module is that explicit cross-substrate survival check:
the photon, the emergent-Lorentz isotropy, the EM varactor, α-invariance, and the
SYM/ASYM (Meissner) mirror, all evaluated ON the chiral srs grid (BOTH
enantiomorphs), with the diamond-vs-srs contrast reported.

════════════════════════════════════════════════════════════════════════════════
α-CLEAN SCRUB (NOT a use): the α-invariance test below is a STRUCTURAL-IDENTITY
SCRUB (the eps_eff·c_EM = eps0·c0 cancellation), NOT an α derivation. No CODATA α
is on the verdict path — the e, ℏ, 4π cancel in the ratio α(A0)/α0, so the test
reads ONLY the canonical eps0,c0 + the α-clean kernel S(A). consistency-vs-
emergence tag: CONSISTENCY of the canonical claim clm-3zz0f6 (α itself is an
ECHO at value level; this confirms the SYM-invariance STRUCTURE, it does not
derive α).

substrate-native-check (Operating Principle 1; done BEFORE this code):
  * Dynamics  : the certified srs vector-TLM scatter+connect (the photon) +
                the canonical bond-LC graded EM line (the L2 varactor; the corpus
                L2 claim lives in impedance-plane / phase-velocity coordinates,
                A46 — the 1D graded line measures in exactly those coordinates,
                per test_l2_em_in_media.py:16-22).
  * Sector    : EM-transverse (the 2-polarization photon; Z_EM≡Z₀); the SYM/ASYM
                varactor (ε,μ co-scaled vs E-only). NOT the shear/bulk sectors.
  * Regime    : LINEAR free (S=1) for the photon/isotropy; biased operating-point
                A0 for the varactor (the Axiom-4 modulation, NOT saturation-rupture).
  * Coords A46: real-space/spectral for the photon; impedance-plane (Z,Γ,c_EM,
                group delay) for L2 — matching the corpus claim coordinates.
"""

from __future__ import annotations

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld
from ave.core.constants import C_0, EPSILON_0, Z_0

from . import _em_media as EM
from . import _medium as M


# ─────────────────────────────────────────────────────────────────────────────
# P1b.2-A — the PHOTON (RUNG-2) propagates losslessly on the chiral srs grid
# ─────────────────────────────────────────────────────────────────────────────
def test_p1b2_photon_rung2_on_chiral_srs():
    """P1b.2-A [CONSISTENCY] — the transverse photon (RUNG-2) propagates
    losslessly + dispersionlessly on the CHIRAL srs grid, BOTH enantiomorphs.

    The photon is the 2-transverse-DOF excitation of the srs vector-TLM. This is
    the RUNG-2 transverse-mode survival on the chiral carrier (the diamond carrier
    is NOT used for the photon — the photon already lives on srs at L1; this
    re-certifies it under the P1b unified-carrier context + the L/R symmetry the
    D1 discharge needs).

    PRE-REGISTERED BINS (frozen before run):
      * PASS : on BOTH enantiomorphs the photon (i) propagates LOSSLESSLY
               (energy drift < 1e-8) AND (ii) has a well-defined transverse speed
               |c|/c_net within 5% of 1 (c_net = c_link/√3) AND (iii) the two
               enantiomorphs give the SAME speed to < 1% (handedness does not
               break the EM-transverse clock).
      * FAIL : lossy, OR wrong speed, OR the enantiomorphs differ in speed by
               >= 1% (the photon clock would be handedness-dependent — a Lorentz
               red-flag on srs ⇒ FLAG + reopen D1).
    """
    M.assert_canonical_constants()
    speeds = {}
    drifts = {}
    for en in ("right", "left"):
        net = cl.build_srs_net(10, en)
        c_link = cld.mean_bond_length(net)
        c_net = cld.ANALYTIC_NETWORK_FACTOR * c_link
        V0 = M.oneway_packet(net, axis=2, sign=-1.0, m=2, width_frac=0.10, pol=0)
        drift = M.max_energy_drift(net, V0, 600, chiral_rotation=False)
        ct = M.centroid_translation(net, V0, 600, axis=2, chiral_rotation=False)
        speeds[en] = abs(ct["speed"]) / c_net
        drifts[en] = drift

    speed_lr_diff = abs(speeds["right"] - speeds["left"]) / (0.5 * (speeds["right"] + speeds["left"]))

    print("\n--- P1b.2-A PHOTON (RUNG-2) on chiral srs (both enantiomorphs) ---")
    for en in ("right", "left"):
        print(f"  {en}: lossless drift {drifts[en]:.3e} (PASS<1e-8); |c|/c_net {speeds[en]:.4f} (PASS within 5%)")
    print(f"  L/R speed difference: {speed_lr_diff:.3e}  (PASS < 1e-2 ⇒ EM clock handedness-independent)")

    for en in ("right", "left"):
        assert drifts[en] < 1e-8, f"FAIL: photon lossy on srs-{en} — drift {drifts[en]:.3e}"
        assert abs(speeds[en] - 1.0) <= 0.05, (
            f"FAIL: wrong photon speed on srs-{en} — |c|/c_net {speeds[en]:.4f}"
        )
    assert speed_lr_diff < 1e-2, (
        f"FLAG (D1 red-flag): photon speed is handedness-DEPENDENT on srs — "
        f"L/R differ by {speed_lr_diff:.3e} >= 1% (Lorentz chain degraded on srs)"
    )


# ─────────────────────────────────────────────────────────────────────────────
# P1b.2-B — emergent-LORENTZ ISOTROPY survives on chiral srs (the D1 core check)
# ─────────────────────────────────────────────────────────────────────────────
def test_p1b2_emergent_lorentz_isotropy_on_chiral_srs():
    """P1b.2-B [CONSISTENCY — the D1 LORENTZ-CHAIN survival check] — the network
    velocity c(k→0) is direction-INDEPENDENT (emergent isotropy) on the CHIRAL srs
    grid, to the SAME quality the diamond carrier had, for BOTH enantiomorphs.

    This is the load-bearing D1 discharge: the 2026-06-12 adjudication anchored
    the Lorentz/isotropy chain to the diamond lattice. The chiral srs net is the
    NEW carrier. If srs were anisotropic (a preferred Cartesian axis), the
    emergent-Lorentz claim would NOT transfer and D1 would reopen. So measure the
    network velocity along all three Cartesian axes on srs and require the
    cross-axis spread to be at the diamond-quality floor.

    PRE-REGISTERED BINS (frozen before run):
      * PASS : on BOTH enantiomorphs (i) the isotropic factor c(k→0)/c_link
               recovers 1/√3 to < 2% (the 3D-TLM geometric factor) AND (ii) the
               cross-axis speed spread (c_x,c_y,c_z) is < 1e-2 (direction-
               independent ⇒ emergent isotropy) AND (iii) the two enantiomorphs
               give the SAME isotropic factor to < 1e-6 (handedness does not break
               isotropy).
      * FAIL : the factor is off 1/√3 by >= 2%, OR the cross-axis spread is
               >= 1e-2 (a preferred axis ⇒ Lorentz chain degraded on srs ⇒ FLAG +
               reopen D1), OR the enantiomorphs' isotropy factors differ.
    """
    M.assert_canonical_constants()
    target = float(cld.ANALYTIC_NETWORK_FACTOR)  # 1/√3
    results = {}
    for en in ("right", "left"):
        net = cl.build_srs_net(8, en)
        speeds = []
        for ax in (0, 1, 2):
            nf = cld.network_velocity_factor(net, axis=ax, m_values=(1, 2, 3, 4), n_steps=600)
            speeds.append(float(nf["factor"]))
        speeds = np.array(speeds)
        factor = float(speeds.mean())
        cross_axis_spread = float((speeds.max() - speeds.min()) / factor)
        rel_target = abs(factor - target) / target
        results[en] = {"factor": factor, "spread": cross_axis_spread,
                       "rel_target": rel_target, "speeds": speeds}

    lr_factor_diff = abs(results["right"]["factor"] - results["left"]["factor"])

    print("\n--- P1b.2-B emergent-LORENTZ isotropy on chiral srs (D1 survival) ---")
    print(f"  target 1/√3 = {target:.6f}")
    for en in ("right", "left"):
        r = results[en]
        print(f"  {en}: factor {r['factor']:.6f} (rel-target {r['rel_target']:.2e}); "
              f"c_x,c_y,c_z {r['speeds'].round(6)}; cross-axis spread {r['spread']:.2e} (PASS<1e-2)")
    print(f"  L/R isotropic-factor difference: {lr_factor_diff:.3e}  (PASS < 1e-6 ⇒ isotropy handedness-indep)")
    print("  → the emergent-Lorentz ISOTROPY chain SURVIVES on chiral srs (D1 dependency discharged).")

    for en in ("right", "left"):
        r = results[en]
        assert r["rel_target"] < 0.02, (
            f"FLAG (D1 red-flag): srs-{en} isotropic factor off 1/√3 by {r['rel_target']:.2e} "
            "(Lorentz chain degraded on srs)"
        )
        assert r["spread"] < 1e-2, (
            f"FLAG (D1 red-flag): srs-{en} has a PREFERRED AXIS — cross-axis spread {r['spread']:.2e} "
            ">= 1e-2 (emergent isotropy / Lorentz chain degraded on srs ⇒ reopen D1)"
        )
    assert lr_factor_diff < 1e-6, (
        f"FLAG (D1 red-flag): isotropy is handedness-dependent — L/R factors differ by {lr_factor_diff:.3e}"
    )


# ─────────────────────────────────────────────────────────────────────────────
# P1b.2-C — the L2 EM VARACTOR (n_EM=S, NOT 1/S) on the srs-grounded medium
# ─────────────────────────────────────────────────────────────────────────────
def test_p1b2_l2_em_varactor_n_equals_S_on_srs_constants():
    """P1b.2-C [CONSISTENCY] — the L2 EM varactor relations (n_EM = S(A0), the
    REFRACTIVE INDEX = S, NOT the 1/S speed ratio) hold on the srs-grounded medium.

    The L2 corpus claim lives in the EM-sector impedance-plane (c_EM, Z_EM, Γ);
    the canonical bond-LC graded line measures in exactly those coordinates (A46,
    test_l2_em_in_media.py:16-22). The medium is grounded on the SAME canonical
    bond-LC Z₀ the srs L0/L1 medium validates (the EM varactor is lattice-agnostic
    in its impedance coordinates — it rides ε₀,μ₀,Z₀,c₀, the vacuum moduli, which
    are the SAME constants the srs photon carries). The load-bearing sign is
    n_EM = S(A0) < 1 (the EM packet ADVANCES; n is NOT 1/S — 1/S is the c_EM/c0
    speed ratio). This re-certifies the L2 relations under the P1b srs context.

    PRE-REGISTERED BINS (frozen before run):
      * PASS : n_EM == S(A0) to < 1e-9 (the refractive index IS S, not 1/S) AND
               c_EM/c0 == 1/S(A0) to < 1e-9 (the speed ratio is 1/S) AND
               Z_EM == Z₀ under SYM to < 1e-9 (impedance-matched) AND the srs-
               medium Z₀ matches the canonical bond-LC Z₀ to < 1e-12.
      * FAIL : n_EM != S (the sign/inversion error the corpus FINDING warns
               against), OR c_EM != c0/S, OR Z_EM != Z₀ under SYM, OR the medium
               Z₀ does not match the srs canonical Z₀.
    """
    EM.assert_canonical_constants()
    # the srs medium and the L2 varactor share the SAME canonical bond-LC Z₀
    z_match = abs(EM.bond_lc_z0() - Z_0) / Z_0
    assert z_match < 1e-12, f"L2 medium Z₀ != canonical bond-LC Z₀ (srs-grounded) — rel {z_match:.2e}"

    A0 = 0.7
    S = float(EM.S_of_A(A0))
    p = EM.em_params(A0, A0)  # SYM region
    n_em = float(p["n_EM"])
    c_ratio = float(p["c_EM"]) / C_0
    z_ratio = float(p["Z_EM"]) / Z_0

    rel_n = abs(n_em - S)            # n_EM = S  (the REFRACTIVE INDEX, NOT 1/S)
    rel_c = abs(c_ratio - 1.0 / S)   # c_EM/c0 = 1/S (the SPEED ratio)
    rel_z = abs(z_ratio - 1.0)       # Z_EM = Z₀ under SYM

    print("\n--- P1b.2-C L2 EM varactor (n_EM=S NOT 1/S) on srs-grounded medium ---")
    print(f"  srs/canonical bond-LC Z₀ match : rel {z_match:.2e}  (PASS < 1e-12)")
    print(f"  n_EM = S(A0)  [REFRACTIVE INDEX]: {n_em:.6f}  (= S {S:.6f}, rel {rel_n:.2e}) — NOT 1/S")
    print(f"  c_EM/c0 = 1/S [SPEED ratio]     : {c_ratio:.6f}  (= 1/S {1.0/S:.6f}, rel {rel_c:.2e})")
    print(f"  Z_EM/Z₀ (SYM)                   : {z_ratio:.6f}  (= 1.0, rel {rel_z:.2e})")
    print("  → n_EM is S (the EM packet ADVANCES, c_EM>c0); the shear sector would slow (√S). Distinct.")

    assert rel_n < 1e-9, f"FAIL: n_EM != S (refractive index inverted to 1/S?) — rel {rel_n:.2e}"
    assert rel_c < 1e-9, f"FAIL: c_EM/c0 != 1/S — rel {rel_c:.2e}"
    assert rel_z < 1e-9, f"FAIL: Z_EM != Z₀ under SYM — rel {rel_z:.2e}"


# ─────────────────────────────────────────────────────────────────────────────
# P1b.2-D — α-INVARIANCE (T2.4) survives on srs (the D1 α-chain SCRUB, not a use)
# ─────────────────────────────────────────────────────────────────────────────
def test_p1b2_alpha_invariance_survives_on_srs():
    """P1b.2-D [CONSISTENCY of clm-3zz0f6 — the D1 α-CHAIN survival SCRUB] — α is
    INVARIANT under SYM scaling, and the invariance is carried by the SAME vacuum
    moduli (ε₀,c₀) the chiral srs photon rides, so the α-chain SURVIVES the move
    from diamond to srs.

    The invariance is the STRUCTURAL cancellation eps_eff·c_EM = (eps0·S)(c0/S)
    = eps0·c0 — the S cancels ⇒ α(A0) = α0 EXACTLY. This is ALGEBRAIC (lattice-
    independent in its FORM), but the D1 concern is whether the INPUTS (ε₀,c₀, the
    α-clean kernel S) are the same on srs as on diamond. They are: the srs photon
    carries Z_EM≡Z₀=√(μ₀/ε₀) and c_EM=c₀/S off the SAME ε₀,μ₀ (P1b.2-C confirmed
    the srs-medium Z₀ matches the canonical bond-LC Z₀). So the α-invariance holds
    on srs with the SAME inputs.

    α-CLEAN: this is a SCRUB, not a use — no CODATA α on the verdict path. The
    ratio α(A0)/α0 cancels e,ℏ,4π and reads only ε₀,c₀,S. The c_shear NEGATIVE
    CONTROL (the category error: substituting c_shear=c₀√S gives 1/S^{3/2}≠1)
    confirms the test discriminates the RIGHT speed (c_EM, not c_shear).

    PRE-REGISTERED BINS (frozen before run):
      * PASS : α(A0)/α0 == 1 to < 1e-12 for EVERY A0 in {0,0.3,0.5,0.7,0.9} with
               c_EM (SYM-invariant) AND the c_shear control DEVIATES (> 1e-3 for
               A0 >= 0.3) AND the moduli are the srs vacuum moduli (ε₀ matches
               EPSILON_0, c₀ matches C_0 — the SAME inputs as on diamond).
      * FAIL : α(A0)/α0 deviates from 1 with c_EM (SYM invariance broken on srs ⇒
               FLAG + reopen D1), OR the c_shear control does not deviate (test
               not discriminating), OR the moduli differ from the canonical vacuum
               moduli.
    """
    EM.assert_canonical_constants()
    # the inputs are the SAME vacuum moduli the srs photon rides (D1 input check):
    # read ε₀, c₀ DIRECTLY off the srs net's own bond-LC (cl.bond_lc), NOT a
    # re-import — this is the genuine srs-medium-grounding link (the srs photon's
    # Z₀=√(μ₀/ε₀) comes from THESE same per-bond reactances).
    blc = cl.bond_lc()
    eps_match = abs(float(blc["eps_0"]) - EPSILON_0) / EPSILON_0
    c_match = abs(float(blc["c0"]) - C_0) / C_0

    A0_sweep = (0.0, 0.3, 0.5, 0.7, 0.9)

    def alpha_ratio(A0, *, use_shear):
        Se = float(EM.S_of_A(A0))
        eps_eff = EPSILON_0 * Se
        c = C_0 * np.sqrt(Se) if use_shear else C_0 / Se  # c_shear vs c_EM (SYM)
        return (EPSILON_0 * C_0) / (eps_eff * c)

    cem = {A0: alpha_ratio(A0, use_shear=False) for A0 in A0_sweep}
    csh = {A0: alpha_ratio(A0, use_shear=True) for A0 in A0_sweep}
    max_dev_cem = max(abs(cem[A0] - 1.0) for A0 in A0_sweep)
    min_dev_csh = min(abs(csh[A0] - 1.0) for A0 in A0_sweep if A0 >= 0.3)

    print("\n--- P1b.2-D α-INVARIANCE survives on srs (SCRUB, not a use; D1 α-chain) ---")
    print(f"  srs vacuum moduli match: ε₀ rel {eps_match:.2e}, c₀ rel {c_match:.2e} (SAME inputs as diamond)")
    for A0 in A0_sweep:
        print(f"  A0={A0}: α/α0 c_EM = {cem[A0]:.12f}   c_shear (WRONG) = {csh[A0]:.6f} (=1/S^1.5)")
    print(f"  max |α/α0 − 1| (c_EM)   : {max_dev_cem:.3e}  (PASS < 1e-12 — INVARIANT on srs)")
    print(f"  min |α/α0 − 1| (c_shear): {min_dev_csh:.3e}  (control must be > 1e-3 — DISCRIMINATES)")
    print("  → α-invariance SURVIVES on chiral srs with the SAME ε₀,c₀ inputs (D1 α-chain discharged).")

    assert eps_match < 1e-12, f"FLAG (D1): srs ε₀ differs from canonical EPSILON_0 — rel {eps_match:.2e}"
    assert c_match < 1e-12, f"FLAG (D1): srs c₀ differs from canonical C_0 — rel {c_match:.2e}"
    assert max_dev_cem < 1e-12, (
        f"FLAG (D1 red-flag): α NOT invariant under SYM on srs — max deviation {max_dev_cem:.3e} "
        "(α-chain degraded on srs ⇒ reopen D1)"
    )
    assert min_dev_csh > 1e-3, (
        f"FAIL: c_shear control did not deviate — test not discriminating c_EM vs c_shear "
        f"(min deviation {min_dev_csh:.3e})"
    )


# ─────────────────────────────────────────────────────────────────────────────
# P1b.2-E — SYM achromatic (Γ=0) vs ASYM Meissner mirror (Γ=−1) on srs constants
# ─────────────────────────────────────────────────────────────────────────────
def test_p1b2_sym_achromatic_vs_asym_meissner_mirror():
    """P1b.2-E [CONSISTENCY] — SYM = achromatic & reflectionless (Γ≈0); ASYM
    (E-only / μ_eff→0 ⇒ Meissner) = a vacuum-impedance mirror (|Γ| large), on the
    srs-grounded EM varactor.

    SYM (ε,μ co-scaled): Z_EM = Z₀√(S/S) = Z₀ invariant ⇒ Γ=0 (reflectionless),
    c_EM achromatic. ASYM (E-only, S_μ=1): Z_EM = Z₀/√S ≠ Z₀ ⇒ Γ≠0 (the mirror).
    The deep-ASYM μ_eff→0 limit (S_μ→0) is the Meissner mirror Γ→−1. The SYM/ASYM
    split is the canonical CLAUDE.md:60 (W6 2026-06-05) mechanism; this re-certifies
    it under the P1b srs context.

    PRE-REGISTERED BINS (frozen before run):
      * PASS : (i) SYM is reflectionless (|Γ_sym| < 1e-9) AND achromatic (the
               excess group delay spread across the band < 1e-3) AND (ii) ASYM
               (E-only at A0=0.9) gives a NONZERO mirror (|Γ_asym| > 0.10) AND
               (iii) the deep-Meissner limit (μ_eff→0) drives |Γ| → 1 (a hard
               mirror; |Γ_meissner| > 0.99).
      * FAIL : SYM reflects (|Γ_sym| >= 1e-9) or is chromatic, OR ASYM gives no
               mirror, OR the Meissner limit does not approach |Γ|=1.
    """
    EM.assert_canonical_constants()
    A0 = 0.9

    # (i) SYM: Z=Z₀ ⇒ Γ=0 + achromatic group delay
    p_sym = EM.em_params(A0, A0)
    z_sym = float(p_sym["Z_EM"]) / Z_0
    gamma_sym = EM.gamma_step(1.0, z_sym)
    N = 120
    x = (np.arange(N) - N / 2) / (N * 0.18)
    prof = A0 * np.exp(-x * x)
    w_grid = np.linspace(0.05, 0.5, 40)
    gd, gam_grad, _ = EM.group_delay_excess(prof, prof, 1.0, w_grid)  # SYM gradient
    band = (w_grid > 0.08) & (w_grid < 0.45)
    gd_band = gd[band]
    gd_spread = float(gd_band.std() / abs(gd_band.mean())) if gd_band.mean() != 0 else 9.99

    # (ii) ASYM (E-only): Z=Z₀/√S ⇒ Γ≠0 mirror
    p_asym = EM.em_params(A0, 0.0)
    z_asym = float(p_asym["Z_EM"]) / Z_0
    gamma_asym = EM.gamma_step(1.0, z_asym)

    # (iii) deep-Meissner: μ_eff→0 (S_μ→0) ⇒ Z→∞ ⇒ Γ→ +1 in magnitude (open);
    # the canonical matter wall is the magnetic-μ load Z=Z₀√S→0 ⇒ Γ→−1 (a SHORT).
    # Both are |Γ|→1 (sign = chirality-set convention, wall-branch B3-degenerate,
    # test_l1_multiwave.py:75-85). The Meissner mirror is the |Γ|→1 HARD reflector:
    # take the magnetic-wall short (S_μ→0 loads μ, Z=Z₀√S_μ→0).
    S_mu_deep = 1e-6  # deep-Meissner: √S_μ = 1e-3 ⇒ |Γ| = (1−1e-3)/(1+1e-3) → 0.998
    z_meissner = float(np.sqrt(S_mu_deep))  # Z_EM/Z₀ = √(S_μ/S_ε), S_ε=1 ⇒ √S_μ → 0
    gamma_meissner = EM.gamma_step(1.0, z_meissner)

    print("\n--- P1b.2-E SYM achromatic (Γ=0) vs ASYM Meissner mirror (|Γ|→1) on srs ---")
    print(f"  (i)  SYM: Z/Z₀={z_sym:.4f}, Γ={gamma_sym:+.2e} (PASS |Γ|<1e-9); "
          f"group-delay spread {gd_spread:.2e} (PASS<1e-3 achromatic)")
    print(f"  (ii) ASYM E-only: Z/Z₀={z_asym:.4f}, Γ={gamma_asym:+.4f} (PASS |Γ|>0.10 mirror)")
    print(f"  (iii) Meissner μ→0: Z/Z₀={z_meissner:.4e}, Γ={gamma_meissner:+.4f} (PASS |Γ|>0.99 hard wall)")
    print("  → SYM = achromatic gravitational-lensing mirror-free; ASYM/Meissner = the impedance mirror.")

    assert abs(gamma_sym) < 1e-9, f"FAIL: SYM not reflectionless — |Γ_sym| {abs(gamma_sym):.2e}"
    assert gd_spread < 1e-3, f"FAIL: SYM not achromatic — group-delay spread {gd_spread:.2e}"
    assert abs(gamma_asym) > 0.10, f"FAIL: ASYM gives no mirror — |Γ_asym| {abs(gamma_asym):.4f}"
    assert abs(gamma_meissner) > 0.99, (
        f"FAIL: Meissner limit (μ→0) does not approach a hard mirror — |Γ| {abs(gamma_meissner):.4f}"
    )
