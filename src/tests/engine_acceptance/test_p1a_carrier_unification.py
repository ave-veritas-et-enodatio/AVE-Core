"""P1a — the CARRIER UNIFICATION: free modes + A1 + ω on ONE chiral srs z=3 net.

Branch: engine/p1a-carrier-unification. Carrier core: ave.solvers.srs_cage_winding
(the z=3 ADAPTATION of the diamond z=4 coupled_cage_winding). Facade:
ave.facade.unified_engine (Regime.UNIFIED_SRS).

THE MAKE-OR-BREAK (Decision-1 ratified: chiral z=3 srs): collapse the TWO
K4-family carriers P0 left — the srs z=3 free-photon carrier (already srs) + the
diamond z=4 A1/ω carrier — onto ONE literal chiral z=3 srs node list. The A1
cavity + the ω Cosserat-winding are RE-HOMED off the diamond TETRA_OFFSETS (z=4)
stencil onto the chiral srs net (build_srs_net), with the cage/winding Grad/Div
ADAPTED z=4 → z=3 (Rule-14: adapt, don't rebuild).

WHY chiral srs: the soliton's charge IS a handed (2,3) winding; the achiral
diamond (z=4, inversion-symmetric) CANNOT carry handedness (writhe ≡ 0); only the
chiral srs (z=3, no inversion) carries the winding handedness = charge/spin/
parity/OA. So the A1/ω MUST live on chiral srs.

substrate-native-check (walked before the carrier code): the cage/winding operator
is the srs z=3 graph Laplacian Bᵀ·diag(D_bond)·B on build_srs_net's OWN bond graph
(NOT diamond z=4 TETRA, NOT Cartesian-on-parity-mask) — structural-null-stencil-
lens satisfied. MODE=A1-bulk + ω-Cosserat-winding + free-transverse; REGIME=linear
S=1 lossless; PHASE-STATE=cold closed-box (no PML, no damping). The closed-box
energy gate stays LIVE (the GX-style negative control below TRIPS it).
consistency-vs-emergence: CONSISTENCY — the unification re-homes certified
structure; no emergence headline, no α-readout. self-formation slot BARRED.

α-CLEAN: the carrier carries κ̃=6/5, θ_χ=2π·(2/7); the facade re-asserts the
import-guard triad. No α-carrier on the verdict path.
"""

from __future__ import annotations

import numpy as np

from ave.facade import Regime, UnifiedEngine, UnifiedEngineConfig


# ═════════════════════════════════════════════════════════════════════════════
# THE ONE-NODE-LIST IDENTITY — the literal carrier collapse (not two carriers)
# ═════════════════════════════════════════════════════════════════════════════
def test_p1a_one_node_list_identity():
    """[UNIFICATION IDENTITY] — the free-mode carrier and the unified A1/ω carrier
    are the SAME chiral srs net: same node count, z=3 both, byte-identical node
    positions. ONE literal node list, NOT two K4-family carriers."""
    eng = UnifiedEngine(UnifiedEngineConfig(regime=Regime.UNIFIED_SRS))
    idn = eng.one_node_list_identity()
    print("\n--- P1a ONE-node-list identity ---")
    print(f"  n_nodes={idn['n_nodes']}  degree={idn['degree']}  enantiomorph={idn['enantiomorph']}")
    print(f"  same_node_count={idn['same_node_count']}  srs_z3_both={idn['srs_z3_both']}  "
          f"node_lists_identical={idn['node_lists_identical']}")
    assert idn["degree"] == 3, f"FAIL: unified carrier z={idn['degree']} != 3 (do NOT flip 3→4)"
    assert idn["same_node_count"], "FAIL: free-mode and A1/ω carrier node counts differ"
    assert idn["node_lists_identical"], "FAIL: the node lists are not byte-identical (not ONE list)"
    assert idn["ONE_node_list"], "FAIL: the carriers did NOT collapse onto ONE chiral srs node list"


# ═════════════════════════════════════════════════════════════════════════════
# THE DECISION-1 PAYOFF — the unified carrier's net is genuinely CHIRAL
# ═════════════════════════════════════════════════════════════════════════════
def test_p1a_chirality_carried():
    """[DECISION-1 PAYOFF] — the unified carrier's srs net carries HANDEDNESS: the
    ring-writhe pseudoscalar is nonzero, SIGN-FLIPS between enantiomorphs, and is
    IDENTICALLY ZERO on the achiral diamond control. This is exactly what the
    diamond z=4 carrier could NOT carry — the handedness = charge-sign / parity /
    optical-activity, the reason the A1/ω MUST live on chiral srs."""
    eng = UnifiedEngine(UnifiedEngineConfig(regime=Regime.UNIFIED_SRS))
    chir = eng.srs_chirality_carried()
    print("\n--- P1a chirality carried (the Decision-1 payoff) ---")
    print(f"  writhe srs-right={chir['writhe_srs_right']:+.4f}  srs-left={chir['writhe_srs_left']:+.4f}  "
          f"diamond={chir['writhe_diamond']:+.2e}")
    print(f"  srs_chiral={chir['srs_chiral']}  diamond_achiral={chir['diamond_achiral']}  "
          f"carries_handedness={chir['carries_handedness']}")
    assert chir["srs_chiral"], (
        "FAIL: srs writhe not chiral (must be nonzero AND sign-flip between enantiomorphs)"
    )
    assert chir["diamond_achiral"], (
        "FAIL: diamond writhe not ~0 — the achiral control must carry NO handedness"
    )
    assert chir["carries_handedness"], (
        "FAIL: the unified srs carrier does not carry handedness — the chiral payoff is absent"
    )


# ═════════════════════════════════════════════════════════════════════════════
# THE MAKE-OR-BREAK — joint energy conserved + winding integer held on srs
# ═════════════════════════════════════════════════════════════════════════════
def test_p1a_unification_verdict_works():
    """[MAKE-OR-BREAK] — the unified srs carrier (A1 cage + ω (2,3) winding on ONE
    chiral z=3 node list) conserves the JOINT energy |dH/H| < 1e-8 over the coupled
    CN/Cayley evolution AND holds the winding integer (the (2,3) charge survives on
    the srs net). REGIME: linear lossless closed-box (no PML, no damping) — a pin
    cannot be bought by damping (the rigor guard). The verdict is WORKS or WALLED."""
    eng = UnifiedEngine(UnifiedEngineConfig(regime=Regime.UNIFIED_SRS))
    v = eng.unification_verdict(n_steps=60)
    print("\n--- P1a UNIFICATION VERDICT (the make-or-break) ---")
    print(f"  verdict: {v['verdict']}  (ONE_node_list={v['ONE_node_list']}, "
          f"carries_handedness={v['carries_handedness']})")
    print(f"  joint energy |dH/H| over 60 coupled steps = {v['joint_energy_rel_drift']:.3e}  (PASS<1e-8)")
    print(f"  gmres info (0=ok): {v['gmres_info']}")
    print(f"  winding integer Q_link: {v['Q_link_before']} → {v['Q_link_after']} "
          f"(w_tor={v['w_tor_after']}); held={v['winding_integer_held']}")
    print(f"  per-grade: A1 {v['a1_energy'][0]:.3e}→{v['a1_energy'][1]:.3e}  "
          f"ω {v['omega_energy'][0]:.3e}→{v['omega_energy'][1]:.3e}  (genesis-24 BOTH-conserved)")
    assert v["gmres_info"] == 0, "FAIL: coupled GMRES did not converge on the srs carrier"
    assert v["joint_energy_conserved"], (
        f"FAIL: joint energy not conserved on the unified srs carrier — "
        f"|dH/H|={v['joint_energy_rel_drift']:.3e}. The A1+ω re-homing onto chiral srs "
        f"did NOT stay lossless (a WALL)."
    )
    assert v["winding_integer_held"], (
        f"FAIL: winding integer changed ({v['Q_link_before']}→{v['Q_link_after']}) — the "
        f"(2,3) charge did not survive the re-homing onto chiral srs (a WALL)."
    )
    assert v["verdict"] == "WORKS", (
        f"FAIL: unification verdict={v['verdict']} — the carrier unification onto chiral "
        f"srs z=3 hit a WALL."
    )


def test_p1a_winding_seed_reads_canonical_2_3_on_srs():
    """[VALIDATE-ON-KNOWN] — the (2,3) winding seeded on the srs node cloud reads
    back the canonical integer Q_link(poloidal)=3, w_tor(toroidal)=2 via the
    srs-native reader (the z=3 analog of compute_Q_link). The ω≡0 null reads 0.
    'A reader that cannot see a known-imposed (2,3) cannot certify it survives.'"""
    eng = UnifiedEngine(UnifiedEngineConfig(regime=Regime.UNIFIED_SRS))
    carrier = eng.unified_srs()
    carrier.seed_winding(amplitude=0.02)
    w = carrier.winding_integer()
    # null: zero ω must read 0
    from ave.solvers.srs_cage_winding import compute_Q_link_srs
    w0 = compute_Q_link_srs(
        carrier.net, np.zeros((carrier.n, 3)), carrier.cfg.R, carrier.cfg.r,
        frame_N=carrier.cfg.frame_N,
    )
    print("\n--- P1a winding validate-on-known (srs-native reader) ---")
    print(f"  seeded (2,3): Q_link(pol)={w['Q_link']} (raw {w['Q_link_raw']:.3f})  w_tor={w['w_tor']}  "
          f"rel={w['w_pol_rel']:.3f}")
    print(f"  ω≡0 null: Q_link={w0['Q_link']}")
    assert w["Q_link"] == 3, f"FAIL: srs reader does not recover the poloidal q=3 — Q_link={w['Q_link']}"
    assert w["w_tor"] == 2, f"FAIL: srs reader does not recover the toroidal p=2 — w_tor={w['w_tor']}"
    assert w0["Q_link"] == 0, f"FAIL: ω≡0 null does not read 0 — Q_link={w0['Q_link']}"


# ═════════════════════════════════════════════════════════════════════════════
# GATE-LIVENESS CONTROLS — the closed-box energy gate is a LIVE discriminator on
# the srs carrier (a passing gate that always passes is vacuous; these TRIP it).
# Rule-14: the backward-Euler dissipative-control logic mirrors the certified
# GX3 control (test_facade_p0_validate_on_known.py), re-pointed at the srs carrier.
# ═════════════════════════════════════════════════════════════════════════════
def test_p1a_a1_alone_control_conserves_on_srs():
    """[CONTROL — uncoupled arm] — with the winding coupling OFF (Ω≡0, the A1-alone
    arm) the A1 cage STILL conserves joint energy on the srs net. This proves the
    coupling is NOT what fakes conservation (the conservation is the srs operator's,
    not the coupling's)."""
    from ave.solvers.srs_cage_winding import SrsCageWinding, SrsCageWindingConfig

    eng = SrsCageWinding(SrsCageWindingConfig(L=12, winding_on=False))
    eng.seed_A1_sech(amplitude=0.02, radius=2.5)
    eng.seed_winding(amplitude=0.02)
    H0 = eng.total_energy()
    for _ in range(30):
        eng.step()
    rel = abs(eng.total_energy() - H0) / H0
    print("\n--- P1a A1-alone (Ω=0) control on srs ---")
    print(f"  |dH/H| over 30 uncoupled steps = {rel:.3e}  (PASS<1e-8)  gmres={eng.last_gmres_info}")
    assert eng.last_gmres_info == 0, "FAIL: A1-alone GMRES did not converge"
    assert rel < 1e-8, f"FAIL: A1-alone arm does not conserve on srs — |dH/H|={rel:.3e}"


def test_p1a_gate_liveness_dissipative_step_trips_the_srs_gate():
    """[GATE-LIVENESS, reachable-FAIL that TRIPS] — drive the srs carrier with a
    REJECTED backward-Euler-style dissipative step (the non-unitary form, NO
    LHS-average) and assert it BLEEDS energy WELL ABOVE the 1e-8 gate. This proves
    the closed-box energy gate on the srs carrier WOULD CATCH a dissipative
    integrator — i.e. the PASSING |dH/H|=1e-10 verdict is NOT vacuous.

    The dissipative step solves (I + i·dt·H) x^{n+1} = x^n (backward-Euler on the
    unitary generator) which is strictly NORM-DECREASING (|1/(1+iλdt)| < 1 for the
    real-spectrum part) — the analog of the GX3 backward-Euler cage bleed."""
    from scipy.sparse import identity
    from scipy.sparse.linalg import gmres

    from ave.solvers.srs_cage_winding import SrsCageWinding, SrsCageWindingConfig

    eng = SrsCageWinding(SrsCageWindingConfig(L=12))
    eng.seed_A1_sech(amplitude=0.02, radius=2.5)
    eng.seed_winding(amplitude=0.02)
    H0 = eng.total_energy()
    nd = 2 * eng.n
    for _ in range(60):
        H = eng._assemble_H()
        I = identity(nd, format="csr", dtype=complex)
        A_sys = (I + 1j * eng.dt * H).tocsr()   # backward-Euler (NO ½, NO LHS-average)
        x = eng._stack()
        x_new, _ = gmres(A_sys, x, rtol=1e-10, maxiter=2000, x0=x)
        eng._unstack(x_new)
    bleed = (H0 - eng.total_energy()) / H0
    print("\n--- P1a GATE-LIVENESS: backward-Euler TRIPS the srs energy gate ---")
    print(f"  backward-Euler bleed (H0−H_end)/H0 = {bleed:.3e}  (TRIPS at > 1e-3)")
    print(f"  ⇒ |dH/H| = {abs(bleed):.3e} ≫ the 1e-8 gate ⇒ the srs gate WOULD CATCH it")
    assert bleed > 1e-3, (
        f"GATE-LIVENESS FAIL: backward-Euler did NOT bleed on the srs carrier "
        f"(bleed={bleed:.3e} ≤ 1e-3) — if it doesn't trip, the closed-box energy gate "
        f"is not discriminating and the verdict's |dH/H| pass is vacuous."
    )
    assert abs(bleed) > 1e-8, "control must trip well above the 1e-8 gate"
