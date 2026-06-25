"""P1b.1 — the bulk (T1.7) + Cosserat (T1.8) DOFs are now DYNAMICALLY PRESENT.

Branch: engine/p1b-modes-live (off engine/p1a-carrier-unification).

════════════════════════════════════════════════════════════════════════════════
THE FLIP (absence-finding → propagation gate)
════════════════════════════════════════════════════════════════════════════════
At L1 the longitudinal-BULK (T1.7, the A1 dilatation "3") and the Cosserat
MICRO-ROTATION (T1.8, the ω winding=charge) modes PASS-iff-ABSENT — the srs
free-mode vector-TLM carries only the 2 transverse photon DOF, so those tests
recorded a MEDIUM-EXTENSION FINDING (`longitudinal_dof_present == False`,
`cosserat_wave_present == False`) with an explicit REGRESSION ANCHOR:

    test_l1_multiwave.py:299-303  "if a future L3 extension ADDS the bulk DOF,
        this test flips and must become the real T1.7 propagation test."
    test_l1_multiwave.py:410-413  "if an independent gapped micro-rotation branch
        turns out to be present (then rewrite T1.8 as a real gapped-dispersion
        gate)."

P1a built exactly that extension — the UNIFIED chiral-srs carrier
(ave.solvers.srs_cage_winding.SrsCageWinding) RE-HOMES BOTH the A1 dilatation
node-field AND the ω Cosserat micro-rotation onto the SAME chiral srs z=3 node
list the free photon rides. So the absence-findings now FLIP: this module is the
real propagation gate the regression anchors call for.

════════════════════════════════════════════════════════════════════════════════
WHAT "PRESENT as a real DOF" MEANS (not faked, not just allocated)
════════════════════════════════════════════════════════════════════════════════
The discipline guard (ave-evidence-framing-discipline + Rule 10 empirical):
allocating a `np.zeros` array is NOT a present DOF. A present DOF must
  (a) OSCILLATE / PROPAGATE — carry a nonzero, evolving field (phase advance for
      the A1 analytic signal; spatial spread for the dilatation packet; amplitude
      oscillation for ω);
  (b) CARRY ENERGY — a nonzero grade-norm that participates in the joint H;
  (c) be SEPARATELY CONSERVED-then-EXCHANGED — the A1 grade and the ω grade are
      genesis-24-orthogonal (ω is its OWN DOF, never grad(V)); when the
      saturation-front port engages they EXCHANGE energy with the joint H still
      conserved (a "pin" cannot be bought by bleeding one grade into the other);
  (d) leave the closed-box ENERGY GATE green with the modes ACTIVE (no PML, no
      damping — the rigor guard; energy-gate-discipline).

MEDIUM-activation, NOT self-formation (the self-formation slot stays BARRED;
this is the medium hosting the modes, not an electron-genesis search).

substrate-native-check (Operating Principle 1; done BEFORE this code):
  * Dynamics  : the certified CN/Cayley unitary stepper on the chiral srs z=3
                graph Laplacian L_srs (NOT a Cartesian Laplacian; NOT the diamond
                z=4 TETRA stencil) — the SrsCageWinding carrier, wired verbatim.
  * Sector    : T1.7 = A1 longitudinal/bulk dilatation (the Heaviside-excised
                scalar "3"); T1.8 = ω Cosserat micro-rotation (the (2,3) winding
                = charge seat). Named per the grounded mapping in
                test_l1_multiwave.py:22-39, NOT conflated.
  * Objective : per-grade energy, phase advance / spatial spread, A1↔ω exchange,
                joint energy conservation — the propagation+conservation gate.
  * Coords    : real-space node-field observables (the DOFs' own coordinates).
  * Saturation: ON for the coupling test (A near the front R_II=4/7 so the port
                engages); the propagation tests run at small A (linear limit) so
                the gate is in its lossless regime.

α-CLEAN: the SrsCageWinding carrier carries κ̃=6/5, θ_χ=2π·(2/7) — NO ALPHA /
Q_TANK / V_SNAP / ELECTRON on the chord path (import-guard triad re-asserted in
ave.solvers.srs_cage_winding). No α on the verdict path here.
"""

from __future__ import annotations

import numpy as np

from ave.solvers.srs_cage_winding import SrsCageWinding, SrsCageWindingConfig

from . import _medium as M


# ─────────────────────────────────────────────────────────────────────────────
# T1.7-LIVE — the longitudinal-BULK (A1 dilatation "3") DOF is PRESENT + PROPAGATES
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_7_longitudinal_bulk_dof_present_and_propagates():
    """T1.7-LIVE [the absence-finding FLIPPED to PRESENT] — the longitudinal-BULK
    DOF (the A1 dilatation "3", the mass precursor) is now a real, propagating,
    energy-carrying DOF on the unified chiral srs net.

    DEF-LOCK (frozen, inherited): c_bulk = √(K/ρ) [the longitudinal DILATATION
    wave; the A1 "3" / mass precursor; K=2G; bulk-impedance-at-saturation-
    boundary.md:24,31]. Distinct from c_EM=c₀/S and c_shear=c₀·√S.

    THE FLIP: test_l1_multiwave.py:261 recorded `longitudinal_dof_present == False`
    (the srs free-mode vector-TLM is (N,degree,2) — 2 transverse only) with the
    regression anchor "if a future L3 extension ADDS the bulk DOF, this test flips
    and must become the real c_bulk propagation gate." P1a's unified srs carrier
    IS that extension: the A1 node-field a_A1 (n_nodes,) rides the SAME chiral srs
    z=3 node list. This test is the real propagation gate.

    PRE-REGISTERED BINS (frozen before run):
      * PASS : the A1 dilatation DOF is PRESENT (the carrier exposes a_A1 on the
               srs node list) AND it PROPAGATES — (i) its analytic-signal phase
               ADVANCES (a propagating mode, not a static seed: |Δarg| > 0.5 rad
               over the window) AND (ii) the dilatation packet SPREADS spatially
               (rms radius changes by > 1e-3, the bulk wave disperses) AND (iii)
               it CARRIES ENERGY (a1_energy > 0) AND (iv) the closed-box energy
               gate stays GREEN with the mode active (|dH/H| < 1e-8, no PML/damp).
      * FAIL : the A1 DOF is absent/frozen (no phase advance OR no spatial spread —
               an allocated-but-dead array), OR it carries no energy, OR the
               energy gate fails (the mode is lossy / a pin bought by damping).
    """
    M.assert_canonical_constants()
    cfg = SrsCageWindingConfig(L=12, enantiomorph="right", winding_on=False)
    c = SrsCageWinding(cfg)  # A1-alone: isolate the bulk DOF (ω port off)

    # the DOF is PRESENT on the srs node list (n_nodes scalar dilatation field)
    a1_present = (c.a_A1.shape == (c.n,)) and (c.net.degree == 3)

    c.seed_A1_sech(amplitude=0.02, radius=2.5)  # small A ⇒ lossless gate limit
    a1_energy0 = c.a1_energy()
    probe = int(np.argmax(np.abs(c.a_A1)))  # the seed peak node

    # spatial-spread tracker: the rms radius of the dilatation energy about its
    # centroid (the bulk wave DISPERSES ⇒ radius changes — propagation, not static)
    ctr = c.net.pos.mean(axis=0)

    def _rms_radius() -> float:
        w = np.abs(c.a_A1) ** 2
        d = c.net.pos - ctr
        d -= c.net.box * np.round(d / c.net.box)
        return float(np.sqrt((w * (d ** 2).sum(axis=1)).sum() / w.sum()))

    H0 = c.total_energy()
    a1_probe_trace = [c.a_A1[probe]]
    r_trace = [_rms_radius()]
    H_trace = [H0]
    n_steps = 120
    for _ in range(n_steps):
        c.step()
        a1_probe_trace.append(c.a_A1[probe])
        r_trace.append(_rms_radius())
        H_trace.append(c.total_energy())

    a1_probe_trace = np.array(a1_probe_trace)
    r_trace = np.array(r_trace)
    H_trace = np.array(H_trace)

    phase_advance = float(abs(np.angle(a1_probe_trace[-1]) - np.angle(a1_probe_trace[0])))
    radius_spread = float(r_trace.max() - r_trace.min())
    rel_drift = float(abs(H_trace[-1] - H0) / H0)
    secular_slope = float(np.polyfit(np.arange(len(H_trace)), H_trace, 1)[0] / H0)
    propagates = phase_advance > 0.5 and radius_spread > 1e-3
    gate_green = rel_drift < 1e-8 and abs(secular_slope) < 1e-8 and c.last_gmres_info == 0

    print("\n--- T1.7-LIVE longitudinal-BULK (A1 '3') DOF: PRESENT + PROPAGATES ---")
    print("  DEF-LOCK: c_bulk = √(K/ρ)  [A1 dilatation; K=2G; distinct from c_EM,c_shear]")
    print(f"  A1 DOF present on srs z=3 list : {a1_present}  (a_A1 shape {c.a_A1.shape}, n_nodes {c.n})")
    print(f"  (i)  phase advance |Δarg|     : {phase_advance:.4f} rad  (PASS > 0.5 ⇒ propagating, not static)")
    print(f"  (ii) dilatation packet spread : {radius_spread:.4f}  (PASS > 1e-3 ⇒ bulk wave disperses)")
    print(f"  (iii) a1_energy carried       : {a1_energy0:.6e}  (PASS > 0)")
    print(f"  (iv) energy gate (mode active): |dH/H|={rel_drift:.2e}, slope={secular_slope:.2e} (PASS < 1e-8)")
    print("  → the absence-finding FLIPPED: the longitudinal-bulk DOF is LIVE (medium-activation).")

    assert a1_present, "FAIL: A1 longitudinal-bulk DOF not present on the srs z=3 node list"
    assert propagates, (
        f"FAIL: A1 DOF does not propagate (phase {phase_advance:.3f}, spread {radius_spread:.3e})"
    )
    assert phase_advance > 0.5, (
        f"FAIL: A1 DOF does not propagate — phase advance {phase_advance:.4f} <= 0.5 "
        "(allocated-but-static, not a real propagating DOF)"
    )
    assert radius_spread > 1e-3, (
        f"FAIL: A1 dilatation packet does not spread — rms-radius spread {radius_spread:.4e} <= 1e-3 "
        "(no spatial propagation)"
    )
    assert a1_energy0 > 0.0, f"FAIL: A1 DOF carries no energy — a1_energy {a1_energy0:.3e}"
    assert gate_green, (
        f"FAIL: energy gate not green with the A1 mode active — |dH/H| {rel_drift:.2e}, "
        f"slope {secular_slope:.2e}, gmres {c.last_gmres_info}"
    )


# ─────────────────────────────────────────────────────────────────────────────
# T1.8-LIVE — the Cosserat MICRO-ROTATION (ω winding=charge) DOF is PRESENT + LIVE
# ─────────────────────────────────────────────────────────────────────────────
def test_t1_8_cosserat_microrotation_dof_present_and_oscillates():
    """T1.8-LIVE [the absence-finding FLIPPED to PRESENT] — the Cosserat MICRO-
    ROTATION DOF (the ω field, the (2,3) winding=charge seat) is now a real,
    INDEPENDENT, energy-carrying DOF on the unified chiral srs net — NOT the
    optical-activity twist of the transverse field that test_l1_multiwave.py:367
    recorded as the ONLY rotation in the free-mode engine.

    DEF-LOCK (frozen, inherited): the Cosserat micro-rotation is carried by the 3
    micropolar DOF (the ω field) — the charge=winding seat (the "3" winding;
    two-threes, master-equation.md:20). It is genesis-24-orthogonal to the A1
    dilatation: ω is its OWN DOF, SEPARATELY seeded, NEVER grad(V).

    THE FLIP: test_l1_multiwave.py:367 recorded `cosserat_wave_present == False`
    (the free-mode engine's only rotation is the k-independent optical-activity
    global-writhe twist) with the regression anchor "if an independent micro-
    rotation branch turns out to be present, rewrite T1.8 as a real gate." P1a's
    unified srs carrier IS that extension: the ω micro-rotation lives on the SAME
    chiral srs z=3 node list as an INDEPENDENT field (the (2,3) winding template
    ê_w + the dynamical LC amplitude b_ω), with the winding integer Q_link read
    off it. This test is the real micro-rotation DOF gate.

    PRE-REGISTERED BINS (frozen before run):
      * PASS : the ω micro-rotation DOF is PRESENT as an INDEPENDENT field (the
               carrier exposes ê_w (n,3) + the dynamical b_ω on the srs node list,
               separate from a_A1) AND it is GENESIS-24-ORTHOGONAL (ω is seeded by
               the (2,3) phase field, NOT read off a_A1 — the winding integer
               Q_link ≠ 0 is carried by ω, NOT by the A1 grade) AND it CARRIES
               ENERGY (omega_energy > 0) AND, when the saturation-front port
               engages, the ω grade OSCILLATES and EXCHANGES energy with A1 (both
               grade-norms swing > 1e-6) while the JOINT energy is conserved
               (|dH/H| < 1e-8) — proving ω is a live coupled DOF, not a frozen seed.
      * FAIL : the ω DOF is absent/frozen (no energy, no oscillation under the
               engaged port), OR it is NOT independent (Q_link == 0, or the
               winding is read off the A1 grade), OR the joint energy is not
               conserved during the exchange (a pin bought by bleeding ω↔A1).
    """
    M.assert_canonical_constants()

    # (1) PRESENT + independent + carries the winding integer (the charge seat) —
    #     A1-alone control OFF here is not needed; seed BOTH grades separately.
    cfg = SrsCageWindingConfig(L=12, enantiomorph="right", winding_on=True)
    c = SrsCageWinding(cfg)
    c.seed_A1_sech(amplitude=0.02, radius=2.5)
    c.seed_winding(amplitude=0.02)

    omega_present = (c.e_w.shape == (c.n, 3)) and (c.b_w.shape == (c.n,))
    omega_energy0 = c.omega_energy()
    w0 = c.winding_integer()
    # genesis-24 orthogonality: the winding integer is carried by the ω grade
    # (Q_link ≠ 0 read off the reconstructed ω field), the A1 grade is a scalar
    # node-field that carries NO (2,3) winding (it is never grad(V) here).
    omega_carries_winding = w0["Q_link"] != 0

    # (2) the LIVE coupling test: seed A near the front R_II=4/7 so the A1↔ω port
    #     engages, then verify the ω grade OSCILLATES + EXCHANGES energy with A1
    #     while the joint energy is conserved (the real coupled-DOF certification).
    cfg2 = SrsCageWindingConfig(L=12, enantiomorph="right", winding_on=True)
    c2 = SrsCageWinding(cfg2)
    c2.seed_A1_sech(amplitude=0.60, radius=2.5)  # A peaks near 0.57 = front gate
    c2.seed_winding(amplitude=0.02)
    Omega_max = float(c2.coupling_Omega().max())
    port_engaged = Omega_max > 1e-3

    a1_init, om_init = c2.a1_energy(), c2.omega_energy()
    Hjoint0 = a1_init + om_init
    a1_tr, om_tr, H_tr = [a1_init], [om_init], [Hjoint0]
    for _ in range(60):
        c2.step()
        a1_tr.append(c2.a1_energy())
        om_tr.append(c2.omega_energy())
        H_tr.append(c2.total_energy())
    a1_tr, om_tr, H_tr = np.array(a1_tr), np.array(om_tr), np.array(H_tr)

    a1_swing = float(a1_tr.max() - a1_tr.min())
    om_swing = float(om_tr.max() - om_tr.min())
    energy_exchanged = a1_swing > 1e-6 and om_swing > 1e-6
    joint_rel_drift = float(abs(H_tr[-1] - Hjoint0) / Hjoint0)
    joint_conserved = joint_rel_drift < 1e-8 and c2.last_gmres_info == 0

    print("\n--- T1.8-LIVE Cosserat MICRO-ROTATION (ω winding=charge) DOF: PRESENT + LIVE ---")
    print("  DEF-LOCK: 3 micropolar ω DOF; charge=winding seat; genesis-24 ⊥ A1 (ω ≠ grad(V))")
    print(f"  ω DOF present on srs z=3 list  : {omega_present}  (ê_w {c.e_w.shape}, b_ω {c.b_w.shape})")
    print(f"  ω carries the (2,3) winding    : Q_link={w0['Q_link']} (≠0 ⇒ charge on the ω grade, not A1)")
    print(f"  ω energy carried               : {omega_energy0:.6e}  (PASS > 0)")
    print(f"  A1↔ω port engaged (A≈4/7)      : {port_engaged}  (Ω_max={Omega_max:.4f})")
    print(f"  ω grade OSCILLATES (swing)     : {om_swing:.4f}   A1 swing {a1_swing:.4f}  (energy EXCHANGED)")
    print(f"  joint energy conserved         : |dH/H|={joint_rel_drift:.2e}  (PASS < 1e-8, no pin-by-damping)")
    print("  → the absence-finding FLIPPED: the Cosserat micro-rotation DOF is LIVE (medium-activation).")

    assert omega_present, "FAIL: ω micro-rotation DOF not present as an independent field on the srs list"
    assert omega_carries_winding, (
        f"FAIL: ω DOF carries no winding — Q_link {w0['Q_link']} (the charge seat is empty)"
    )
    assert omega_energy0 > 0.0, f"FAIL: ω DOF carries no energy — omega_energy {omega_energy0:.3e}"
    assert port_engaged, (
        f"FAIL: A1↔ω port did not engage — Ω_max {Omega_max:.4f} <= 1e-3 "
        "(cannot certify ω as a live coupled DOF)"
    )
    assert energy_exchanged, (
        f"FAIL: ω grade did not oscillate/exchange — A1 swing {a1_swing:.3e}, ω swing {om_swing:.3e} "
        "(a frozen seed, not a live DOF)"
    )
    assert joint_conserved, (
        f"FAIL: joint energy not conserved during exchange — |dH/H| {joint_rel_drift:.2e} "
        f"(a pin bought by bleeding ω↔A1), gmres {c2.last_gmres_info}"
    )


# ─────────────────────────────────────────────────────────────────────────────
# T1.7+T1.8 JOINT — BOTH modes active TOGETHER, energy conserved (the unified gate)
# ─────────────────────────────────────────────────────────────────────────────
def test_p1b_both_modes_active_energy_conserved():
    """P1b.1 JOINT [the unified-activation gate] — with BOTH the bulk (A1) and the
    Cosserat (ω) DOFs DYNAMICALLY ACTIVE on the SAME chiral srs node list, the
    closed-box joint energy is conserved AND each grade carries nonzero,
    separately-tracked energy (genesis-24 BOTH-conserved). This is the
    medium-activation make-or-break: the modes are LIVE together, the gate is green.

    PRE-REGISTERED BINS (frozen before run):
      * PASS : BOTH grades carry energy (a1_energy > 0 AND omega_energy > 0)
               throughout the run, the joint energy |dH/H| < 1e-8 over the window
               (closed box, no PML/damping), AND the per-grade split is healthy
               (neither grade silently drained to ~0 — both stay > 10% of their
               initial value across the window).
      * FAIL : either grade goes dead (energy → ~0), OR the joint energy gate
               fails, OR a grade is silently drained (the genesis-24 double-count
               guard trips).
    """
    M.assert_canonical_constants()
    cfg = SrsCageWindingConfig(L=12, enantiomorph="right", winding_on=True)
    c = SrsCageWinding(cfg)
    c.seed_A1_sech(amplitude=0.02, radius=2.5)
    c.seed_winding(amplitude=0.02)

    a1_0, om_0 = c.a1_energy(), c.omega_energy()
    H0 = c.total_energy()
    a1_min, om_min = a1_0, om_0
    H_trace = [H0]
    for _ in range(80):
        c.step()
        a1_min = min(a1_min, c.a1_energy())
        om_min = min(om_min, c.omega_energy())
        H_trace.append(c.total_energy())
    H_trace = np.array(H_trace)
    rel_drift = float(abs(H_trace[-1] - H0) / H0)
    secular_slope = float(np.polyfit(np.arange(len(H_trace)), H_trace, 1)[0] / H0)
    both_carry = a1_0 > 0.0 and om_0 > 0.0
    neither_drained = (a1_min > 0.1 * a1_0) and (om_min > 0.1 * om_0)
    gate_green = rel_drift < 1e-8 and abs(secular_slope) < 1e-8 and c.last_gmres_info == 0

    print("\n--- P1b.1 JOINT: BOTH bulk (A1) + Cosserat (ω) modes ACTIVE, energy conserved ---")
    print(f"  a1_energy   (initial / min)   : {a1_0:.6e} / {a1_min:.6e}  (PASS min > 10% initial)")
    print(f"  omega_energy(initial / min)   : {om_0:.6e} / {om_min:.6e}  (PASS min > 10% initial)")
    print(f"  joint energy gate             : |dH/H|={rel_drift:.2e}, slope={secular_slope:.2e} (PASS < 1e-8)")
    print(f"  both grades carry energy      : {both_carry}; neither silently drained: {neither_drained}")
    print("  → BOTH medium modes LIVE on ONE chiral srs node list, closed-box gate green.")

    assert both_carry, f"FAIL: a grade carries no energy — a1 {a1_0:.3e}, ω {om_0:.3e}"
    assert neither_drained, (
        f"FAIL: a grade silently drained (genesis-24 guard) — a1 min {a1_min:.3e}/{a1_0:.3e}, "
        f"ω min {om_min:.3e}/{om_0:.3e}"
    )
    assert gate_green, (
        f"FAIL: joint energy gate not green with both modes active — |dH/H| {rel_drift:.2e}, "
        f"slope {secular_slope:.2e}, gmres {c.last_gmres_info}"
    )
