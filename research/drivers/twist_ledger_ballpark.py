"""Twist-ledger ballpark — the gamma_c couple-stress energy of the ground-state
(2,3) winding at electron scale, from CANON-SUPPLIED inputs only.

Companion to research/2026-08-02_twist-ledger-audit.md sec.6.

CLASS: paper arithmetic, ORDER-OF-MAGNITUDE ONLY. NOT a simulation, NOT a
prediction, mints no clm-/def-/exp-/sup-. No solver, no lattice, no field.
Every input is imported from ave.core.constants (ave-canonical-source: never
hard-code a constant) or is a geometry quoted from a cited canon leaf.

Run:  PYTHONPATH=src .venv/bin/python research/drivers/twist_ledger_ballpark.py

What it shows, in order:
  (1) T4's U_AVE = T_EM * l_node is EXACTLY 1.0 m_e c^2 -- a Class-A definitional
      identity (T_EM is DEFINED as m_e c^2 / l_node at constants.py:493), so it
      cannot be read as evidence that the budget is physically exhausted.
  (1b) T5 -- the l3-electron-soliton-synthesis.md Virial sum (audit sec.2.2b):
      substituting canon's own closed forms (:98-105) gives 0.5 + 0.5 = 1.0
      EXACTLY, with xi_topo cancelling identically. clm-ka5zdx's open
      strengthen-by is therefore trivially satisfiable, hence vacuous.
  (2) The dimensional defect in the canonical xi_K relations (audit FLAG-2). The
      stress reading is forced by DIMENSIONAL ANALYSIS ALONE; the l_c = sqrt(6)
      cross-check is a T_EM-INVARIANT null check (both readings degenerate) and
      is printed only to show that degeneracy explicitly.
  (3) E_twist under the two 6-OOM-separated gamma_c normalizations canon carries
      (audit FLAG-3 / constants.py:331-337), spanning 12 orders.
  (4) The generation rung for comparison -- recorded, explicitly NOT claimed as a
      match (audit sec.6.4 discrimination note).
"""

import numpy as np

from ave.core.constants import (
    ALPHA,
    C_0,
    ELL_C,
    G_VAC,
    L_NODE,
    M_E,
    M_MUON,
    RHO_BULK,
    T_EM,
    e_charge,
)

# --- canon geometry (each line carries its cite) ---------------------------
XI_K1, XI_K2 = 8.0 / 3.0, 32.0  # q-g47-substrate-scale-cosserat-closure.md:58
TW_TURNS = 3.0 / 2.0  # Tw = q/p, 540 deg/rev: 2026-06-07_vacuum-characterization-program.md:59
L_C_WEAK = 1.0e-18  # weak-force range: gauge-boson-masses.md:39

MEC2 = M_E * C_0**2
C_LOOP = L_NODE  # electron-unknot.md:28
R_0 = L_NODE / (2.0 * np.pi)  # electron-unknot.md:11 ; weak-coupling.md:18
V_TUBE = np.pi * R_0**2 * C_LOOP  # = l_node^3 / (4 pi)
KAPPA = 2.0 * np.pi * TW_TURNS / C_LOOP  # |grad omega| along the loop [rad/m]


def main() -> None:
    print("=" * 78)
    print("(1) T4 -- the closure identity is ALGEBRAICALLY FORCED (Class A)")
    print("=" * 78)
    print(f"  T_EM              = {T_EM:.6e} N      [constants.py:493, = M_E*C_0**2/L_NODE]")
    print(f"  l_node            = {L_NODE:.6e} m")
    print(f"  m_e c^2           = {MEC2:.6e} J = {MEC2 / e_charge / 1e6:.5f} MeV")
    print(
        f"  U_AVE = T_EM*l_node = {T_EM * L_NODE:.6e} J"
        f"  ->  {T_EM * L_NODE / MEC2:.6f} m_e c^2   [electron-unknot.md:48]"
    )
    print("  => the '1.0' is a tautology, not an exhausted physical budget.\n")

    print("=" * 78)
    print("(1b) T5 -- the l3 Virial sum closes at 1.0 BY CONSTRUCTION (Class A)")
    print("=" * 78)
    # Closed forms quoted from l3-electron-soliton-synthesis.md:98-105 (parameter table);
    # the boxed sum is at :90, the per-half split at :114-116, the closure claim at :118.
    xi_topo = e_charge / L_NODE  # :101  (identical to constants.py:356 XI_TOPO)
    l_0 = M_E / xi_topo**2  # :102  L_0 = xi_topo^-2 * m_e
    i_max = xi_topo * C_0  # :103  I_max = xi_topo * c
    v_snap = MEC2 / e_charge  # :105  V_SNAP = m_e c^2 / e
    c_e = e_charge**2 / MEC2  # :104  C_e = e/V_SNAP = e^2/(m_e c^2)
    e_l = 0.5 * l_0 * i_max**2
    e_c = 0.5 * c_e * v_snap**2
    print(f"  xi_topo = e/l_node        = {xi_topo:.6e} C/m   (= constants.py:356 XI_TOPO)")
    print(f"  L_0     = xi_topo^-2 * m_e = {l_0:.6e} H")
    print(f"  I_max   = xi_topo * c      = {i_max:.6e} A")
    print(f"  C_e     = e^2/(m_e c^2)    = {c_e:.6e} F")
    print(f"  V_SNAP  = m_e c^2 / e      = {v_snap:.6e} V")
    print(f"  1/2 L_0 I_max^2 / (m_e c^2) = {e_l / MEC2:.6f}")
    print(f"  1/2 C_e V_peak^2 / (m_e c^2) = {e_c / MEC2:.6f}")
    print(f"  SUM                          = {(e_l + e_c) / MEC2:.6f}")
    # xi_topo-independence: rescale xi_topo by an arbitrary factor; the inductive half
    # is unchanged, because L_0 ~ xi_topo^-2 and I_max^2 ~ xi_topo^2 cancel identically.
    for scale in (1.0, 7.0, 1.0e6):
        xt = xi_topo * scale
        e_l_s = 0.5 * (M_E / xt**2) * (xt * C_0) ** 2
        print(f"  xi_topo scaled by {scale:>9.1e} -> 1/2 L_0 I_max^2/(m_e c^2) = {e_l_s / MEC2:.6f}")
    print("  => xi_topo CANCELS IDENTICALLY; the sum is 1.0 before any number is chosen.")
    print("     clm-ka5zdx's open strengthen-by (vol2/claim-quality.md:1258) is therefore")
    print("     TRIVIALLY SATISFIABLE and carries no information. See audit sec.2.2b;")
    print("     canon's own longhand cancellation: relativistic-inductor.md:28.\n")

    print("=" * 78)
    print("(2) FLAG-2 -- dimensional defect in the canonical xi_K relations")
    print("=" * 78)
    print("  canon: 'mu+kappa = xi_K1 * T_EM  [Pa]' and")
    print("         'beta+gamma = xi_K2 * T_EM * l_node^2  [N]'")
    print("         (cosserat_field_3d.py:28 / k4_cosserat_coupling.py:34 /")
    print("          q-g47-substrate-scale-cosserat-closure.md:58)")
    print(f"  literal reading, T_EM = {T_EM:.4e} N:")
    print(f"     xi_K1*T_EM              = {XI_K1 * T_EM:.4e} N     -- bracket says [Pa]  MISMATCH")
    print(f"     xi_K2*T_EM*l_node^2     = {XI_K2 * T_EM * L_NODE**2:.4e} N*m^2 -- bracket says [N]   MISMATCH")
    sigma_0 = MEC2 / L_NODE**3
    mu_k = XI_K1 * sigma_0
    b_g = XI_K2 * sigma_0 * L_NODE**2
    print(f"  stress reading, T_EM -> sigma_0 = m_e c^2 / l_node^3 = {sigma_0:.4e} Pa:")
    print(f"     mu+kappa                = {mu_k:.4e} Pa    [Pa] OK")
    print(f"     beta+gamma              = {b_g:.6e} N     [N]  OK")
    # l_c = sqrt((beta+gamma)/(2(mu+kappa))) is T_EM-INVARIANT: T_EM cancels between
    # numerator and denominator, so it CANNOT discriminate the tension reading from the
    # stress reading. Canon states the invariance itself at
    # q-g47-substrate-scale-cosserat-closure.md:56 ("independent of T_EM") and
    # constants.py:326. Both readings are evaluated below to show the degeneracy.
    lc_stress = np.sqrt(b_g / (2.0 * mu_k))
    lc_tension = np.sqrt((XI_K2 * T_EM * L_NODE**2) / (2.0 * XI_K1 * T_EM))
    print(f"     l_c | stress reading  = {lc_stress / L_NODE:.5f} * l_node")
    print(f"     l_c | tension reading = {lc_tension / L_NODE:.5f} * l_node")
    print(f"     canon sqrt(6)         = {np.sqrt(6.0):.5f}")
    print("     -> T_EM-INVARIANT CONSISTENCY CHECK, NOT A DISCRIMINATOR.")
    print("        T_EM cancels in (beta+gamma)/(2(mu+kappa)); BOTH readings are")
    print("        DEGENERATE here. Confirms only xi_K2/(2*xi_K1) = 6.")
    print("        The STRESS reading is forced by DIMENSIONAL ANALYSIS ALONE (above).\n")

    print("=" * 78)
    print("(3) FLAG-3 -- E_twist under the two 6-OOM-separated gamma_c readings")
    print("=" * 78)
    print(f"  G_vac    = {G_VAC:.4e} Pa   (= RHO_BULK*C_0**2, rho_bulk = {RHO_BULK:.4e} kg/m^3)")
    print(f"  ELL_C    = {ELL_C:.4e} m  (= sqrt(6)*l_node, constants.py:338)")
    print(f"  V_tube   = {V_TUBE:.4e} m^3 (= l_node^3/4pi)")
    print(f"  Tw       = {TW_TURNS} turns/rev = {TW_TURNS * 360:.0f} deg/rev -> kappa = {KAPPA:.4e} 1/m")
    print("  E_twist  = gamma_c * kappa^2 * V_tube    [cosserat_field_3d.py:713 'gamma kappa.kappa']\n")
    rows = (
        ("R1a  lattice-scale  gamma_c = G_vac*ELL_C^2       ", G_VAC * ELL_C**2),
        ("R1b  lattice-scale  gamma_c = xi_K2*sigma_0*l^2   ", b_g),
        ("R2   weak-scale     gamma_c = G_vac*(1e-18 m)^2   ", G_VAC * L_C_WEAK**2),
    )
    for lab, gam in rows:
        e = gam * KAPPA**2 * V_TUBE
        print(f"  {lab} gamma_c = {gam:.4e} N -> E = {e:.4e} J = {e / MEC2:.4e} m_e c^2")
    print(f"\n  R1b/R1a = {(b_g) / (G_VAC * ELL_C**2):.4f}  (internal lattice-scale slop: 32/3)")
    print(f"  R1a/R2  = {(G_VAC * ELL_C**2) / (G_VAC * L_C_WEAK**2):.4e}  (the 12-OOM gate)\n")

    print("=" * 78)
    print("(4) the generation rung -- recorded, NOT claimed as a match")
    print("=" * 78)
    # rung from the canonical CODATA anchors (constants.py:131 M_MUON, :159 M_E) --
    # ave-canonical-source: no hard-coded masses.
    rung = (M_MUON - M_E) / M_E
    print(f"  (m_mu - m_e)/m_e  (CODATA anchors)   = {rung:8.2f} m_e c^2")
    print(
        f"  1/(alpha*sqrt(3/7)) - 1  (canon)     = {1.0 / (ALPHA * np.sqrt(3.0 / 7.0)) - 1.0:8.2f}"
        " m_e c^2   [lepton-spectrum.md:39]"
    )
    closed = XI_K2 * (2.0 * np.pi * TW_TURNS) ** 2 / (4.0 * np.pi)
    print(f"  R1b closed form xi_K2*(2 pi Tw)^2/(4 pi) = 72 pi = {closed:8.2f} m_e c^2")
    print("  => SAME ORDER, 8% apart. NOT a match. Any term of this shape is FORCED")
    print("     into the 1e1-1e3 band because T_EM*l_node == m_e c^2 identically;")
    print("     see audit sec.6.4 discrimination note.")


if __name__ == "__main__":
    main()
