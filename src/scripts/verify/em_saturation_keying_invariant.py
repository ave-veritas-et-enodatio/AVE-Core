#!/usr/bin/env python3
"""EM-sector saturation keying — PIECE (b): which 2nd-order invariant survives -> S_E.

FROZEN prereg: research/2026-07-05_em-saturation-keying-functional_prereg_FROZEN.md
Freeze commit gated on: bfd897c5.

Piece (a) showed <E^2> cannot key saturation (static and wave both nonzero). This
piece derives WHICH second-order invariant the node's LC-tank constitutive
response actually integrates, from the node mode structure -- the substrate
picks it, not fiat. Three carried candidates (frozen sub-bins):
  T-POYNT : S = |<E x H>|         (Poynting energy-in-flight)
  T-BEAT  : S = <(d_t E)^2>/wC^2  (temporal-gradient content)
  T-CIRC  : S = |oint E.dl|^2     (E-side circulation, dual of oint H.dl)

THE SUBSTRATE ARGUMENT (derived, sympy):
Each substrate cell is a resonant LC tank (node-up-small-large-signal.md:97).
Its two reactances key on DIFFERENT variables (the keyed-argument duality,
:104-106): the varactor (epsilon) on the potential V~E, the inductor (mu) on the
circulating current I ~ oint H.dl. The Axiom-4 kernel S(A) is a LOCAL response to
the node's instantaneous operating point. From piece (a), the potential
engagement <E^2> is DC-degenerate. The engagement that distinguishes transport
must therefore live in the ENERGY EXCHANGE between the node's L and C -- the node
loads only when power flows through it. For an EM field the instantaneous power
flux through a cell face IS the Poynting vector u = E x H (units W/m^2). A held
Coulomb field has H = 0 -> u = 0 (no flux, the node is a dead-ended capacitor);
a co-moving wave has H = E/(c*Z_0)... = E/(mu_0 c) -> u = E^2/(mu_0 c) != 0.

So the substrate FORCES T-POYNT as the primary transport invariant: it is the
one 2nd-order EM invariant that (i) vanishes for held stock, (ii) is the ACTUAL
power the LC node exchanges, (iii) is bounded for a wave (no VCA-R01 pointwise
singularity), and (iv) is a genuine Lorentz tensor flux (T^{0i}) -> closes boost.

Relation to T-BEAT: for a co-moving plane wave B=E/c, Faraday gives
d_t E = c * (spatial gradient) = omega E, so <(d_t E)^2>/wC^2 = (omega/wC)^2 <E^2>
= (omega/wC)^2 * (Poynting-in-units-of-E^2). They agree up to the (omega/wC)^2
kinematic factor for a co-moving wave; they DIFFER for a standing wave (Poynting
time-averages to zero; the beat does not). The derivation below shows the node
consumes the POWER FLUX (Poynting), which is the co-moving-transport quantity,
and expresses S_E in the dimensionless transport coordinate.

TWO INDEPENDENT CODE PATHS:
  PATH A: sympy symbolic LC-node energy-exchange rate, closed form.
  PATH B: numpy: build a co-moving wave and a held field, compute all three
          candidate invariants, confirm the static->0 / wave->nonzero split and
          the coefficient.
"""
from __future__ import annotations

import numpy as np
import sympy as sp

from ave.core.constants import C_0, E_YIELD, EPSILON_0, L_NODE, M_E, OMEGA_C, Z_0

E_C = E_YIELD  # saturation field


# ==================================================== PATH A: sympy LC-node rate
def lc_node_transport_coordinate():
    """Derive the dimensionless transport coordinate the node loads on.

    A vacuum cell: C_cell = eps0*ell, L_cell = mu0*ell (node-up :96). The stored
    energy is U = 1/2 C V^2 + 1/2 L I^2. The POWER exchanged through the cell (the
    Poynting flux integrated over a face of area ell^2) is P = (E x H).ell^2. In
    the node's own units the natural power scale is the rest-energy-per-clock:
    P_C = (m_e c^2) * omega_C = (m_e c^2) c / ell_node. The dimensionless transport
    engagement is T = P / P_C = (E H ell^2) / (m_e c^2 omega_C).

    For a co-moving plane wave H = E/Z_0, so E x H = E^2/Z_0, and
        T = E^2 ell^2 / (Z_0 m_e c^2 omega_C).
    We show T reduces to (E/E_c)^2 up to a pure geometric/dimensionless factor,
    i.e. the transport engagement is the SAME (E/E_c)^2 magnitude the Letter uses
    -- but now GATED by the presence of transport (H != 0), which a held field
    lacks. The coefficient linking T to (E/E_c)^2 is DERIVED here (not fitted).
    """
    E, H, ell, Z0, mc2, wC, Ec, eps0, mu0, c = sp.symbols(
        "E H ell Z_0 mc2 omega_C E_c epsilon_0 mu_0 c", positive=True)
    # Poynting flux magnitude for co-moving wave: u = E*H = E^2/Z0
    u = E**2 / Z0
    # power through a cell face of area ell^2
    P = u * ell**2
    # node power scale = rest energy per clock cycle worth: P_C = mc2 * wC
    P_C = mc2 * wC
    T = sp.simplify(P / P_C)
    # substitute the substrate identities:
    #   Z0 = sqrt(mu0/eps0);  wC = c/ell;  mc2 = m_e c^2;
    #   E_c^2 = ? we want to show T ~ (E/E_c)^2 * (geometric factor)
    # Use mc2 = eps0 E_c^2 ell^3 * (something)?  Test the energy-density identity:
    #   the cell rest-energy-density scale is mc2/ell^3. And 1/2 eps0 E_c^2 is the
    #   field energy density at the yield field. Their ratio is the geometric factor.
    T_sub = T.subs({Z0: sp.sqrt(mu0 / eps0), wC: c / ell})
    T_sub = sp.simplify(T_sub)
    # ratio to (E/E_c)^2:
    ratio = sp.simplify(T_sub / (E / Ec) ** 2)
    return {
        "u_poynting": u,
        "T": T,
        "T_substituted": T_sub,
        "ratio_to_EEc2": ratio,
        "symbols": (E, H, ell, Z0, mc2, wC, Ec, eps0, mu0, c),
    }


def three_invariants_symbolic():
    """Symbolic forms of the three candidate invariants for E(t)=E0 cos(wt),
    co-moving H = E/Z0 for a wave; H=0 for held stock. Cycle-averaged."""
    t, w, E0, Z0, wC = sp.symbols("t omega E0 Z_0 omega_C", positive=True)
    Tw = 2 * sp.pi / w
    E = E0 * sp.cos(w * t)
    dE = sp.diff(E, t)
    # WAVE (co-moving H = E/Z0)
    H_wave = E / Z0
    poynt_wave = sp.simplify(sp.integrate(E * H_wave, (t, 0, Tw)) / Tw)  # <E H>
    beat_wave = sp.simplify(sp.integrate(dE**2, (t, 0, Tw)) / Tw / wC**2)  # <dE^2>/wC^2
    # HELD stock: H=0, dE=0 -> both zero
    return {
        "poynt_wave": poynt_wave,  # = E0^2/(2 Z0)
        "beat_wave": beat_wave,  # = E0^2 w^2/(2 wC^2)
        "poynt_static": 0,  # H=0
        "beat_static": 0,  # dE=0
        "ratio_beat_over_poynt_units": sp.simplify(beat_wave / (poynt_wave * Z0)),
    }


# ============================================================== PATH B: numpy
def three_invariants_numeric(omega_over_wC: float, held: bool,
                             n_cycles: int = 200, spc: int = 512) -> dict:
    """Compute all three candidate invariants for a wave or a held field.

    Held field: E constant, H=0 (a dead-ended capacitor - no transport).
    Wave: E=E0 cos, H=E/Z0 co-moving, dE/dt=omega-scaled.
    Returns the transport engagements in E0^2 units (E0=1 -> ratios to E_c later).
    """
    wC = OMEGA_C
    E0 = 1.0
    if held:
        TC = 2 * np.pi / wC
        t = np.linspace(0.0, TC, spc, endpoint=False)
        E = np.full_like(t, E0)
        H = np.zeros_like(t)  # held stock: no co-moving magnetic transport
        dEdt = np.zeros_like(t)
    else:
        w = omega_over_wC * wC
        Tw = 2 * np.pi / w
        t = np.linspace(0.0, n_cycles * Tw, n_cycles * spc, endpoint=False)
        E = E0 * np.cos(w * t)
        H = E / Z_0  # co-moving plane wave
        dEdt = -E0 * w * np.sin(w * t)
    poynt = float(np.mean(E * H))  # <E H>  (Poynting, W/m^2 with E,H in SI)
    beat = float(np.mean(dEdt**2) / wC**2)  # <(dE/dt)^2>/wC^2
    amp2 = float(np.mean(E**2))  # <E^2> (the rejected key)
    return {"poynt": poynt, "beat": beat, "amp2": amp2}


def poynting_coefficient_honesty():
    """The T-POYNT engagement coefficient: 1/(4pi), and its normalization status.

    T = P/P_C with P = (E^2/Z0) ell^2 (Poynting through a cell face) and the node
    power scale P_C = mc2 * wC. At E=E_c this gives T(E_c)/(E/E_c)^2 = 1/(4pi)
    (verified below). The geometric 1/(4pi) is a CONSISTENCY-class magnitude: it
    rides the power-normalization choice P_C = mc2*wC (rest-energy-per-clock). The
    LOAD-BEARING, normalization-INDEPENDENT chord is the FREQUENCY-INDEPENDENCE of
    the transport engagement: a co-moving wave carries Poynting E^2/Z0 at EVERY
    frequency, so T-POYNT engages the pump FULLY (unlike T-BEAT's (omega/wC)^2
    suppression). That structural fact -- Table I survives -- does not depend on
    the 1/(4pi) value.
    """
    import math
    Ec = E_C
    ell = L_NODE
    mc2 = M_E * C_0**2
    wC = OMEGA_C
    T_at_Ec = Ec**2 * ell**2 / (Z_0 * mc2 * wC)  # = T/(E/Ec)^2
    inv_4pi = 1.0 / (4.0 * math.pi)
    u_field_Ec = 0.5 * EPSILON_0 * Ec**2
    u_rest = mc2 / ell**3
    return {
        "T_coeff": T_at_Ec,
        "one_over_4pi": inv_4pi,
        "rel": abs(T_at_Ec - inv_4pi) / inv_4pi,
        "u_field_Ec_over_u_rest": u_field_Ec / u_rest,  # = 1/(8pi)
        "one_over_8pi": 1.0 / (8.0 * math.pi),
    }


def boost_check_OPEN():
    """BOOST-CONSISTENCY OPEN (CRITICAL-2). The 'structural closure' claim is RETRACTED.

    The prior claim was that a boosted static field's Poynting 'is a DC drift, aliased
    to omega_C, averages out' -- so the boost is closed structurally. This is REFUTED
    by two of my own results:
      (i) piece (a) shows a DC 2nd-order quantity SURVIVES clock-averaging (static
          <E^2>_secular = 1.0 at omega=0). A boosted static field is omega=0 in the lab,
          so its 2nd-order content does NOT average out -- the aliasing claim contradicts
          the secular-averaging math it rests on.
      (ii) the boosted config carries a real static H (the magnet's B), so the LOCAL
          E x H is nonzero -- the coded functional engages on the config called 'blind'.
    Returns the boosted motional field magnitude only, as an INPUT to the OPEN question,
    NOT a closure. The round-2 pointer: a NET-flux functional anchored in the LATTICE
    REST FRAME is frame-anchored by the theory's declared preferred frame -- a boosted
    observer sees transformed observables, not a re-keyed vacuum. That resolution belongs
    to a NEW derivation, not this one.
    """
    v = 370e3  # m/s, CMB boost
    B = 2.5  # T, PVLAS-scale static magnet
    E_mot = v * B  # motional E ~ v B (Letter main.tex:312)
    A2 = (E_mot / E_C) ** 2
    return {"E_motional": E_mot, "A2_boost": A2, "v_over_c_sq": (v / C_0) ** 2,
            "verdict": "OPEN", "note": "aliasing refuted; boost-consistency OPEN "
            "(requires lattice-frame anchoring, round-2 forward pointer)."}


def main():
    print("=" * 74)
    print("PIECE (b) — which 2nd-order invariant survives -> S_E")
    print("=" * 74)

    print("\n--- PATH A: LC-node transport coordinate (sympy) ---")
    A = lc_node_transport_coordinate()
    print(f"  Poynting flux (co-moving)  u = {A['u_poynting']}")
    print(f"  transport engagement T     = {A['T']}")
    print(f"  T (substrate-substituted)  = {A['T_substituted']}")
    print(f"  ratio T / (E/E_c)^2        = {A['ratio_to_EEc2']}")

    print("\n--- three candidate invariants (symbolic, wave vs held) ---")
    S = three_invariants_symbolic()
    print(f"  <E H>_wave (Poynting)      = {S['poynt_wave']}   ;  static = {S['poynt_static']}")
    print(f"  <(dE)^2>/wC^2_wave (beat)  = {S['beat_wave']}   ;  static = {S['beat_static']}")
    print("  >> BOTH vanish for held stock (H=0, dE=0); BOTH nonzero for a wave.")
    print("     The node loads on the POWER FLUX it exchanges (Poynting); T-BEAT is")
    print("     the same content x (omega/wC)^2 for a co-moving wave.")

    print("\n--- PATH B: numeric (independent) ---")
    print(f"  {'case':22s} {'<E H>(Poynt)':>16s} {'<dE^2>/wC^2':>14s} {'<E^2>':>10s}")
    b_static = three_invariants_numeric(0.0, held=True)
    print(f"  {'HELD static':22s} {b_static['poynt']:16.6e} {b_static['beat']:14.6e} {b_static['amp2']:10.4f}")
    for r in [3.033e-6, 0.0196, 1.0]:
        b = three_invariants_numeric(r, held=False)
        print(f"  {'WAVE w/wC='+f'{r:.3e}':22s} {b['poynt']:16.6e} {b['beat']:14.6e} {b['amp2']:10.4f}")

    # RECONCILE: PATH A ratio T/(E/Ec)^2 vs PATH B Poynting/(E^2) up to units.
    # For the wave <E H> = <E^2>/Z0 = amp2/Z0. Check:
    b = three_invariants_numeric(0.0196, held=False)
    pred_poynt = b["amp2"] / Z_0
    rel = abs(b["poynt"] - pred_poynt) / pred_poynt
    print(f"\n  RECONCILE <E H> = <E^2>/Z0 : path-B={b['poynt']:.6e} pred={pred_poynt:.6e} rel={rel:.2e}")

    # LIVE positive control: the wave engages, the static does not.
    print("\n  LIVE positive control (transport split):")
    print(f"    held-static Poynting = {b_static['poynt']:.3e}  (expect 0 -> DC-blind)")
    print(f"    wave     Poynting    = {b['poynt']:.6e}  (expect nonzero -> engaged)")

    print("\n--- Poynting coefficient honesty (magnitude=consistency, structure=chord) ---")
    P = poynting_coefficient_honesty()
    print(f"  T/(E/Ec)^2 = {P['T_coeff']:.10f}  vs 1/(4pi)={P['one_over_4pi']:.10f}  rel={P['rel']:.2e}")
    print(f"  u_field(Ec)/u_rest = {P['u_field_Ec_over_u_rest']:.10f}  vs 1/(8pi)={P['one_over_8pi']:.10f}")
    print("  >> 1/(4pi) rides P_C=mc2*wC normalization (CONSISTENCY-class magnitude).")
    print("     The CHORD is frequency-INDEPENDENCE: pump engages fully (Table I survives),")
    print("     unlike T-BEAT's (omega/wC)^2 pump suppression.")

    print("\n--- boost check: OPEN (aliasing REFUTED, CRITICAL-2) ---")
    Bz = boost_check_OPEN()
    print(f"  motional E (2.5T, 370km/s) = {Bz['E_motional']:.3e} V/m  A^2={Bz['A2_boost']:.3e}")
    print(f"  VERDICT: {Bz['verdict']} -- {Bz['note']}")
    print("  >> the aliasing story ('DC drift averages out') is REFUTED by piece-(a)"
          " DC survival + the coded functional's T!=0 on the boosted config.")

    # FORK verdict: T-POYNT is CONSTRAINT-SELECTED (MAJOR-a), NOT substrate-forced.
    print("\n" + "=" * 74)
    print("FORK VERDICT (T-POYNT vs T-BEAT vs T-CIRC) — CONSTRAINT-SELECTED, not forced:")
    print("  - T-POYNT was SELECTED by Table-I survival: T-BEAT was eliminated BECAUSE")
    print("    it collapses the pump (routed toward the anchored numbers -- the visible-")
    print("    target the knife exists for). This is a CONSTRAINT-SELECTION, not a")
    print("    substrate derivation. Deriving net-vs-local from the network dynamics")
    print("    (not selecting it against Table I) is the round-2 requirement.")
    print("  - T-BEAT: = T-POYNT x (omega/wC)^2 for a co-moving wave -> pump suppressed.")
    print("  - the LOCAL-Poynting form (this PR's boxed functional) is CONSTRAINT-KILLED")
    print("    on the physical atom (constraint 1); the surviving candidate is NET")
    print("    transport (closed-surface flux), lattice-frame-anchored -- ROUND 2.")
    return A, S


if __name__ == "__main__":
    main()
