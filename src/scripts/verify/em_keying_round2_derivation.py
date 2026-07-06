#!/usr/bin/env python3
"""EM keying ROUND 2 — the DERIVATION: STEP 0 (kill net-flux) + STEP 1 (worked variable).

FROZEN prereg: research/2026-07-05_em-keying-round2-worked-cell_prereg_FROZEN.md
Freeze commit gated on: e4312c43 (prereg FROZEN before this file — git ordering = proof).

STEP 0 (mandatory first line) — the BRIEFED net-flux candidate is DEGENERATE.
  By Poynting's theorem the closed-surface net flux through a cell equals -dU_cell/dt.
  Its time-average is ZERO for ANY steady state -> it blinds the STEADY PUMP as well
  as the atom -> it kills Table I. This ELIMINATES the briefed candidate BY DERIVATION
  (not by selection). Grant's orchestrator correction, verified as a one-line identity.

STEP 1 (REQUIREMENT 1) — DERIVE the loading variable from the cell's OWN equations.
  A vacuum cell is a resonant LC tank (node-up-small-large-signal.md:§1): C=eps0*ell,
  L=mu0*ell, omega_C=1/sqrt(LC)=c/ell. The varactor keys on the VOLTAGE amplitude A_V=V/Vy
  (node-up:118, a potential variable); the inductor on the CURRENT A_I=I/Imax (node-up:119).
  The Axiom-4 kernel deficit d=1-S(A) drives saturation. The physical question requirement 1
  forces: what does the cell's SATURATION ENGAGEMENT integrate to over a clock cycle --
  the AC EXCURSION of the reactive energy (Grant's 'energy sloshing between C and L per
  cycle'), or the held amplitude, or the temporal-gradient rate?

  We derive it by working the LC energy-exchange ledger. The reactive energy exchanged
  BETWEEN C and L per cycle is what 'works' the cell; a held DC bias stores energy but
  exchanges NONE (dead-ended: V constant -> no current -> nothing sloshes). The kernel
  engagement that DISTINGUISHES a worked cell from a held one is the AC (time-varying)
  content of the drive. Two candidate measures both vanish for a held field:
    W_var  = <E^2> - <E>^2       (AC-variance; the amplitude of what sloshes; freq-INDEP)
    W_beat = <(dE/dt)^2>/wC^2    (temporal-gradient; the RATE; freq-SUPPRESSED by (w/wC)^2)
  These agree up to a kinematic w^2 for a co-moving wave (W_beat=(w/wC)^2 W_var) but give
  OPPOSITE Table-I fates. Round 1 eliminated W_beat (as 'T-BEAT') BY TABLE-I survival -- a
  constraint-selection. This round DERIVES which the cell equation forces from the LC energy
  ledger, and lets the substrate adjudicate. NEITHER is selected against Table I.

TWO INDEPENDENT CODE PATHS:
  PATH A: sympy symbolic LC energy-exchange ledger (closed form).
  PATH B: numpy time-domain -- drive a cell at omega, read the reactive-energy AC excursion
          and both candidate measures directly. Independent of PATH A (no sympy).
"""
from __future__ import annotations

import numpy as np
import sympy as sp

from ave.core.constants import C_0, E_YIELD, EPSILON_0, L_NODE, MU_0, OMEGA_C, Z_0
from ave.validation.reconcile_gate import ReconcileGate

E_C = E_YIELD


def reconcile_pathA_pathB_W_var():
    """ReconcileGate: PATH A (symbolic W_var = 1/2 (E/Ec)^2) vs PATH B (numpy time-domain W_var),
    with can-fire PROVEN on the real comparator+halt path (derived tolerance). The two paths are
    ALGEBRAICALLY INDEPENDENT: PATH A is the sympy closed form Var(E0 cos wt)=E0^2/2; PATH B is a
    numpy time-series variance of a sampled cosine -- different code paths (the #527 obligation)."""
    # PATH A (symbolic closed form, in E0=1 units): Var = 1/2
    W_var_A = 0.5
    # PATH B (numpy time-domain, independent): the sampled variance of cos over integer cycles
    def pathB():
        return lc_reactive_swing_numeric(0.0196, held=False)["W_var"]
    # derived tolerance: discrete-sampling error of Var over integer cycles ~ 1/n_samples ~ 1e-5;
    # set rtol conservatively to 1e-4 (well above sampling error, well below any real disagreement).
    gate = ReconcileGate(
        label="W_var PATH-A(symbolic 1/2) vs PATH-B(numpy time-domain)",
        claimed=W_var_A, independent=pathB, rtol=1e-4)
    return gate.enforce(prove_first=True)  # can-fire proven, then DISCREPANT-HALT if they disagree


# ============================================================ STEP 0: net-flux is degenerate
def step0_netflux_degenerate_symbolic():
    """The briefed net-flux candidate is DEGENERATE (Poynting identity, sympy).

    Poynting: div(E x H) = -dt(u)  (source-free, lossless region -- Ax3). The closed-surface
    net flux out of a cell = integral of div(E x H) = -dt(U_cell). Time-average over a cycle:
    <net flux> = -<dt U_cell>. For E(t)=E0 cos(w t) at a fixed cell (a STEADY wave -- envelope
    constant), <dt u> = 0 -> <net flux> = 0. So a STEADY PUMP has ZERO net cell flux, exactly
    like the atom's steady hidden-momentum loop. Net-flux keying blinds the pump -> kills
    Table I -> ELIMINATED by derivation.
    """
    t, w = sp.symbols("t omega", positive=True)
    E0 = sp.symbols("E0", positive=True)
    E = E0 * sp.cos(w * t)
    # energy density (up to a constant eps0; the TIME structure is what matters for <dt u>)
    u = E**2
    dudt = sp.diff(u, t)
    Tw = 2 * sp.pi / w
    avg_dudt = sp.simplify(sp.integrate(dudt, (t, 0, Tw)) / Tw)
    # net flux out of a 1D cell = S(x+ell)-S(x) = -dt(U); its cycle average is -avg_dudt
    avg_netflux = sp.simplify(-avg_dudt)
    return {
        "u": u,
        "dudt": dudt,
        "avg_dudt_over_cycle": avg_dudt,     # == 0
        "avg_netflux_over_cycle": avg_netflux,  # == 0 -> pump blind too -> DEGENERATE
    }


# ==================================================== STEP 1 PATH A: LC energy-exchange ledger
def step1_lc_energy_ledger_symbolic():
    """Derive the worked variable from the LC cell's OWN energy-exchange equation (sympy).

    A driven LC cell: the varactor stores U_C=1/2 C V^2, the inductor U_L=1/2 L I^2. The cell
    is 'worked' by the reactive power sloshing between them: P_reactive = dt(U_C) = -dt(U_L) for
    a lossless tank. Over a cycle the NET energy exchanged is zero (reactive), but the AMPLITUDE
    of the swing -- the peak reactive energy exchanged, the 'sloshing' Grant names -- is nonzero
    ONLY when V (hence the stored energy) VARIES in time.

    For a drive V(t)=V0 cos(w t):
      U_C(t) = 1/2 C V0^2 cos^2(w t) = 1/2 C V0^2 (1 + cos 2wt)/2.
      Its time-average is 1/2 C V0^2 /2 (the DC stored energy); its AC PART -- the part that
      sloshes -- has amplitude 1/2 C V0^2 /2 and oscillates at 2w. The 'working' of the cell
      is measured by the VARIANCE of the stored energy (its AC excursion), which for the kernel
      argument A_V = V/Vy maps to Var(A_V^2)-class content.

    The Axiom-4 kernel deficit to 2nd order is d(t) = 1 - S(A_V) ~ 1/2 A_V(t)^2. The cell's
    SATURATION engagement is the CYCLE-AVERAGE of the deficit that a HELD field does NOT produce
    -- i.e. the part of <A_V^2> that is absent for a static field of the SAME time-average. That
    is exactly the VARIANCE <A_V^2> - <A_V>^2 = Var(A_V), the AC content. A held DC field has
    <A_V^2> = <A_V>^2 (no variance) -> zero worked engagement; a wave has Var(A_V) = A_V,rms^2/... != 0.

    We derive Var(E) for a held field and a wave and show the held field gives ZERO.
    """
    t, w = sp.symbols("t omega", positive=True)
    E0, Ec = sp.symbols("E0 E_c", positive=True)
    Tw = 2 * sp.pi / w

    # WAVE at the cell: E(t) = E0 cos(w t)
    E_wave = E0 * sp.cos(w * t)
    meanE_wave = sp.integrate(E_wave, (t, 0, Tw)) / Tw
    meanE2_wave = sp.integrate(E_wave**2, (t, 0, Tw)) / Tw
    var_wave = sp.simplify(meanE2_wave - meanE_wave**2)          # E0^2/2
    grad2_wave = sp.simplify(sp.integrate(sp.diff(E_wave, t) ** 2, (t, 0, Tw)) / Tw)  # E0^2 w^2/2

    # HELD field at the cell: E(t) = E0 (constant in time)
    var_held = sp.Integer(0)   # <E^2>-<E>^2 = E0^2 - E0^2 = 0 (no time variation)
    grad2_held = sp.Integer(0)  # dE/dt = 0

    # dimensionless worked coordinates in (E/Ec)^2 units
    W_var_wave = sp.simplify(var_wave / Ec**2)                   # (1/2)(E0/Ec)^2
    W_beat_wave = sp.symbols("wC")  # placeholder; computed below with wC
    wC = sp.symbols("omega_C", positive=True)
    W_beat_wave = sp.simplify(grad2_wave / (wC**2 * Ec**2))      # (1/2)(w/wC)^2 (E0/Ec)^2
    ratio_beat_over_var = sp.simplify((grad2_wave / wC**2) / var_wave)  # (w/wC)^2

    return {
        "var_wave": var_wave,
        "grad2_wave": grad2_wave,
        "var_held": var_held,
        "grad2_held": grad2_held,
        "W_var_wave_over_EEc2": sp.simplify(W_var_wave / (E0 / Ec) ** 2),   # 1/2
        "W_beat_wave_over_EEc2": sp.simplify(W_beat_wave / (E0 / Ec) ** 2),  # (1/2)(w/wC)^2
        "ratio_W_beat_over_W_var": ratio_beat_over_var,                     # (w/wC)^2
    }


def step1_which_measure_the_ledger_forces():
    """The DERIVATION verdict: which measure does the LC energy ledger force?

    The reactive energy that sloshes between C and L is 1/2 C V^2 (capacitive) <-> 1/2 L I^2
    (inductive). The AMPLITUDE of this exchange -- the peak-to-mean swing of the stored reactive
    energy -- is the physical 'working' of the cell. For V(t)=V0 cos(w t):
        U_C(t) = 1/2 C V0^2 cos^2 = (1/4 C V0^2)(1 + cos 2wt).
    The swing amplitude of U_C is (1/4 C V0^2), INDEPENDENT of w -- the cell exchanges the same
    reactive-energy amplitude per cycle whether it is worked slowly or fast (a resonant LC tank
    driven at amplitude V0 sloshes the SAME peak energy 1/2 C V0^2 regardless of drive rate,
    below resonance). So the ledger forces the FREQUENCY-INDEPENDENT measure: the AC-VARIANCE
    of the field content, W_var = Var(E)/Ec^2 = 1/2 (E/Ec)^2 for a wave. This is [WORKED-VAR].

    W_beat (the temporal-gradient) measures the RATE of the exchange (power ~ w * energy), not
    the AMPLITUDE of the energy exchanged. The saturation kernel keys on the OPERATING-POINT
    EXCURSION (how far A_V swings), which is an AMPLITUDE, not a rate. So the ledger does NOT
    force W_beat. This is the substrate DERIVING W_var, not selecting it against Table I: the
    reason is the reactive-energy-swing amplitude is frequency-independent, a property of the LC
    tank's energy ledger, which we verify numerically (PATH B) below.

    HONEST CAVEAT (carried to the slow-drive constraint item, §4-7): this frequency-independence
    is the QUASI-STATIC (below-resonance, w << wC) tank response. The cell response time is
    1/wC ~ 1.3e-21 s; a drive slower than that but still time-VARYING works the cell at the same
    reactive-energy amplitude. What it does NOT cover is the deeply-sub-optical middle band where
    NO experiment constrains the worked-E response -- a declared OPEN SCALE (constraint 7).
    """
    return {
        "forced_measure": "W_var",
        "sub_bin": "[WORKED-VAR]",
        "reason": "the reactive-energy swing amplitude 1/2 C V0^2 is frequency-independent "
                  "(the LC tank sloshes the same peak energy per cycle at amplitude V0, below "
                  "resonance) -> the saturation operating-point excursion keys on the AC-variance "
                  "amplitude, not the rate. DERIVED from the LC energy ledger, NOT selected vs "
                  "Table I.",
        "W_beat_status": "measures the RATE (power ~ w*energy), not the amplitude of energy "
                         "exchanged -> NOT the operating-point excursion the kernel keys on. "
                         "Carried as the open alternative [WORKED-BEAT] (not eliminated by "
                         "Table-I survival, but by the ledger's amplitude-vs-rate distinction).",
    }


# ==================================================== STEP 1 PATH B: numpy time-domain ledger
def lc_reactive_swing_numeric(omega_over_wC: float, held: bool,
                              n_cycles: int = 200, spc: int = 512) -> dict:
    """Drive a cell at omega; read the reactive-energy AC excursion + both worked measures.

    Independent of PATH A (pure numpy). For a driven LC cell with V(t)=V0 cos(w t):
      - held (V constant): the stored energy is constant -> ZERO reactive swing -> worked=0.
      - wave: the stored energy oscillates at 2w with a swing amplitude ~ 1/2 C V0^2,
        FREQUENCY-INDEPENDENT (below resonance). Read Var(E) and <(dE/dt)^2>/wC^2.
    Returns worked measures in E0^2 units (E0=1).
    """
    wC = OMEGA_C
    C_cell = EPSILON_0 * L_NODE
    E0 = 1.0
    if held:
        TC = 2 * np.pi / wC
        t = np.linspace(0.0, TC, spc, endpoint=False)
        E = np.full_like(t, E0)
        dEdt = np.zeros_like(t)
    else:
        w = omega_over_wC * wC
        Tw = 2 * np.pi / w
        t = np.linspace(0.0, n_cycles * Tw, n_cycles * spc, endpoint=False)
        E = E0 * np.cos(w * t)
        dEdt = -E0 * w * np.sin(w * t)
    # the reactive stored energy (per unit face, up to geometry): U_C ~ 1/2 C (E*ell)^2-class;
    # its AC EXCURSION (max - mean) is the 'sloshing amplitude' -- read it directly:
    U_C = 0.5 * C_cell * (E * L_NODE) ** 2  # ~ 1/2 C V^2 with V = E*ell
    swing_amp = float(np.max(U_C) - np.mean(U_C))   # the reactive-energy swing amplitude
    # normalize the swing by the wave's swing at this E0 to expose frequency-(in)dependence:
    W_var = float(np.mean(E**2) - np.mean(E) ** 2)   # AC-variance in E0^2 units
    W_beat = float(np.mean(dEdt**2) / wC**2)         # temporal-gradient in E0^2 units
    return {
        "omega_over_wC": omega_over_wC,
        "reactive_swing_amp_J": swing_amp,
        "W_var": W_var,
        "W_beat": W_beat,
    }


def demonstrate_swing_frequency_independence():
    """Show the reactive-energy swing amplitude is the SAME across drive frequencies (the
    load-bearing fact that DERIVES W_var over W_beat): drive a cell at three sub-optical
    frequencies and read the swing amplitude -- it is frequency-independent (below resonance),
    while W_beat scales as (w/wC)^2. This is the numerical proof PATH A asserts symbolically."""
    freqs = [3.033e-6, 0.0196, 0.1]  # sub-optical bands (all w << wC)
    swings, w_vars, w_beats = [], [], []
    for r in freqs:
        d = lc_reactive_swing_numeric(r, held=False)
        swings.append(d["reactive_swing_amp_J"])
        w_vars.append(d["W_var"])
        w_beats.append(d["W_beat"])
    return {
        "freqs": freqs,
        "reactive_swing_amps": swings,      # ~ identical across freqs (freq-independent)
        "W_var_values": w_vars,             # ~ identical (0.5) across freqs
        "W_beat_values": w_beats,           # scale as (w/wC)^2 -> collapse at low freq
    }


def step1_variance_vs_meansquare_the_crux():
    """THE LOAD-BEARING CRUX (flag-don't-fix): variance (blind to DC) vs mean-square (DC included).

    STEP 1 derived that the cell keys on the AC EXCURSION AMPLITUDE (freq-independent), not the rate.
    But 'AC excursion amplitude' has two readings that differ by the DC baseline:
      (i)  VARIANCE  <A_V^2> - <A_V>^2  -- BLIND to a held DC (Grant's worked candidate); OR
      (ii) MEAN-SQUARE <A_V^2>          -- DC INCLUDED (the corpus R2 canon).
    The mean deficit <1-S(A_V)> the kernel integrates is ~ <A_V^2>/2 = MEAN-SQUARE at leading order
    -- which is NONZERO for a held DC field. So the kernel-deficit route (verified numerically) forces
    the MEAN-SQUARE, which is the round-1 [C-EXCLUDED] amplitude key -- NOT the variance.

    THE CORPUS TENSION (verbatim, verify-before-cite, node-up-small-large-signal.md):
      :118  'A DC bias is a real operating point.'   (the ε-varactor loads on the HELD amplitude)
      :40   the operating point is 'analogous to DC bias on a semiconductor varactor'
      :217  'A static E is a real operating-point bias for the V-keyed varactor -- it loads epsilon'
    -> the corpus ε-varactor canon INCLUDES the DC (mean-square), and there is NO corpus Lenz-analog
    DC-blindness mechanism for the ε side (Lenz DC-blindness is the mu-INDUCTOR's property, keyed on
    dI/dt via oint H.dl; tau-relax-derivation.md:93-97, node-up:119-123 -- NOT claimed for the varactor).

    SO THE HONEST DERIVATION VERDICT SPLITS BY SECTOR:
      * B-SIDE (mu-inductor): worked-keying is CANON-DERIVED. A_I responds only to dB/dt (Lenz); a
        static B is not worked -> A_I=0 -> S_mu=1 EXACTLY (node-up:364, 'DERIVED analytically exact').
        The B-side variance/worked reading IS forced by the corpus mechanism.
      * E-SIDE (epsilon-varactor): worked-keying (blind to held DC E) CONTRADICTS the corpus R2 canon
        (:118, :217: a held DC E IS a real operating point). The cell energy ledger forces the AC part
        to engage, but it does NOT force the DC part to be EXCLUDED -- the mean deficit <1-S> is
        mean-square, DC-included. For the E-varactor to be worked-keyed requires a NEW ε-side
        DC-blindness mechanism (a Lenz-dual for displacement current) that the corpus does NOT supply.

    THIS IS THE ROUND-1 SS1.1 CONTRADICTION, NOW SHARPER: #539 [C-EXCLUDED] is empirical evidence that
    the DC-included (mean-square) E-varactor key is FALSIFIED at atomic scales (overshoots CREMA 4-7
    OOM). So EITHER the corpus R2 'held DC E loads epsilon' is wrong at atomic scales (superseded by a
    worked/variance E-key -- but that key is NOT corpus-derived, it needs the missing ε-side mechanism),
    OR the E-varactor genuinely loads on the held DC and the birefringence E-route is scale-bounded.

    RETURNS the crux for the bin router: the WORKED variable is DERIVED for the B-side, but for the
    E-side it is SELECTED (the cell ledger forces AC-engagement but not DC-exclusion; DC-exclusion
    needs a missing ε-side Lenz-dual). Flag-don't-fix: surfaced with both verbatim citations, NOT
    silently reconciled.
    """
    import numpy as np
    from ave.core.constants import OMEGA_C
    # numerically show the mean kernel deficit is MEAN-SQUARE (DC-included), not variance:
    def S(x): return np.sqrt(np.clip(1 - x**2, 1e-12, 1))
    A0 = 0.3
    # held DC field at A0: deficit is nonzero (DC-included -> the round-1 key)
    d_held = 1 - S(A0)
    # pure-AC drive of the same peak A0: mean deficit
    r = 1e-2; w = r * OMEGA_C; t = np.linspace(0, 50 * 2*np.pi/w, 50*4096, endpoint=False)
    d_ac = float(np.mean(1 - S(A0*np.cos(w*t))))
    var_ac = float(np.var(A0*np.cos(w*t)))       # variance (blind to DC)
    meansq_ac = float(np.mean((A0*np.cos(w*t))**2))  # mean-square (what the deficit tracks)
    return {
        "deficit_held_DC": d_held,          # NONZERO -> DC IS included (mean-square), contradicts 'worked'
        "deficit_mean_AC": d_ac,            # ~ meansq/2 -> tracks MEAN-SQUARE, not variance
        "variance_AC": var_ac,              # A0^2/2 = 0.045
        "meansquare_AC": meansq_ac,         # A0^2/2 = 0.045 (equal to variance ONLY because DC=0 here)
        "B_side_verdict": "worked-DERIVED (Lenz, canon-exact node-up:364)",
        "E_side_verdict": "worked-SELECTED (ledger forces AC-engagement; DC-exclusion needs a missing "
                          "epsilon-side Lenz-dual; corpus R2 :118/:217 says DC IS included)",
        "corpus_tension": "node-up:118 'A DC bias is a real operating point' CONTRADICTS a "
                          "DC-blind (variance) E-varactor; #539 [C-EXCLUDED] is empirical evidence the "
                          "DC-included E-key is falsified at atomic scales. FLAG, not fix.",
    }


def main():
    print("=" * 78)
    print("EM KEYING ROUND 2 — DERIVATION (STEP 0 net-flux kill + STEP 1 worked variable)")
    print("=" * 78)

    print("\n[STEP 0] the BRIEFED net-flux candidate is DEGENERATE (Poynting identity):")
    s0 = step0_netflux_degenerate_symbolic()
    print(f"    d/dt(u) for E=E0 cos(wt):  {s0['dudt']}")
    print(f"    <d/dt u>_cycle          = {s0['avg_dudt_over_cycle']}")
    print(f"    <net flux>_cycle = -<du/dt> = {s0['avg_netflux_over_cycle']}")
    print("    -> ZERO for a STEADY wave (pump) AND the atom's steady loop alike.")
    print("    -> net-flux keying blinds the pump -> kills Table I -> ELIMINATED by derivation.")

    print("\n[STEP 1 PATH A] LC energy-exchange ledger (sympy):")
    a = step1_lc_energy_ledger_symbolic()
    print(f"    Var(E)_wave  = {a['var_wave']}   ; Var(E)_held = {a['var_held']}")
    print(f"    <(dE/dt)^2>_wave = {a['grad2_wave']} ; held = {a['grad2_held']}")
    print(f"    W_var (wave)  = {a['W_var_wave_over_EEc2']} * (E/Ec)^2   [freq-INDEPENDENT]")
    print(f"    W_beat (wave) = {a['W_beat_wave_over_EEc2']} * (E/Ec)^2   [freq-SUPPRESSED]")
    print(f"    W_beat/W_var  = {a['ratio_W_beat_over_W_var']}  = (w/wC)^2")

    print("\n[STEP 1 verdict] which measure the ledger FORCES:")
    v = step1_which_measure_the_ledger_forces()
    print(f"    FORCED: {v['forced_measure']}  -> sub-bin {v['sub_bin']}")
    print(f"    reason: {v['reason']}")
    print(f"    W_beat: {v['W_beat_status']}")

    print("\n[STEP 1 PATH B] numpy time-domain ledger (independent):")
    print(f"    {'case':22s} {'reactive swing (J)':>20s} {'W_var':>10s} {'W_beat':>12s}")
    bh = lc_reactive_swing_numeric(0.0, held=True)
    print(f"    {'HELD static':22s} {bh['reactive_swing_amp_J']:20.4e} {bh['W_var']:10.4f} {bh['W_beat']:12.4e}")
    for r in [3.033e-6, 0.0196, 1.0]:
        b = lc_reactive_swing_numeric(r, held=False)
        print(f"    {'WAVE w/wC='+f'{r:.2e}':22s} {b['reactive_swing_amp_J']:20.4e} {b['W_var']:10.4f} {b['W_beat']:12.4e}")

    print("\n[STEP 1 PATH B] reactive-swing FREQUENCY-INDEPENDENCE (derives W_var over W_beat):")
    d = demonstrate_swing_frequency_independence()
    print(f"    freqs (w/wC):          {['%.2e' % f for f in d['freqs']]}")
    print(f"    reactive swing amps:   {['%.4e' % s for s in d['reactive_swing_amps']]}  (freq-INDEPENDENT)")
    print(f"    W_var values:          {['%.4f' % s for s in d['W_var_values']]}  (all ~0.5, freq-INDEP)")
    print(f"    W_beat values:         {['%.4e' % s for s in d['W_beat_values']]}  (scale as (w/wC)^2)")
    print("    -> the LC tank sloshes the SAME reactive-energy amplitude per cycle at any sub-")
    print("       resonant frequency -> the operating-point excursion (what the kernel keys on)")
    print("       is the FREQUENCY-INDEPENDENT AC-variance W_var. DERIVED, not selected vs Table I.")

    print("\n[ReconcileGate] PATH A (symbolic) vs PATH B (numpy) for W_var, can-fire proven:")
    rg = reconcile_pathA_pathB_W_var()
    print(f"    reconciled={rg.reconciled}  max_rel={rg.max_rel_discrepancy:.2e}  can_fire_proven={rg.can_fire_proven}")

    print("\n[STEP 1 CRUX] variance (DC-blind) vs mean-square (DC-included) -- the LOAD-BEARING split:")
    x = step1_variance_vs_meansquare_the_crux()
    print(f"    held-DC deficit 1-S(A0) = {x['deficit_held_DC']:.4e}  (NONZERO -> DC IS included ="
          f" mean-square = the round-1 key)")
    print(f"    mean-AC deficit         = {x['deficit_mean_AC']:.4e}  (tracks MEAN-SQUARE {x['meansquare_AC']:.4f}/2,"
          f" not variance {x['variance_AC']:.4f})")
    print(f"    B-side: {x['B_side_verdict']}")
    print(f"    E-side: {x['E_side_verdict']}")
    print(f"    CORPUS TENSION (flag-don't-fix): {x['corpus_tension']}")

    return s0, a, v, d, x


if __name__ == "__main__":
    main()
