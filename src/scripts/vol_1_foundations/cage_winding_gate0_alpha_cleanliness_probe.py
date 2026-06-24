"""GATE 0 — cage⊗winding-engine host α-cleanliness probe (the hard STOP de-risk).

Charter: _orchestration/2026-06-23_cage-winding-engine-charter.md
Prereg:  research/2026-06-23_cage-winding-gate0-host-alpha-cleanliness-prereg.md

This is a REFUTE-BY-DEFAULT, validate-on-known probe. It asks the single Gate-0
question: can the Cosserat winding host (`cosserat_field_3d.py`) carry the A1
mass-cage α-CLEANLY, with the Q-slot left EMPTY?

It does NOT mutate the host. It instruments three independent α-contamination
vectors and contrasts them against the existing α-FREE `_bulk.py` cold-Q
known-negative (Q≈30.8 ≠ 137):

  V1 (import guard)  : does the canonical α-leak guard (vacuum_varactor_scatter.py:
                       110-112, "ALPHA"/"Q_TANK"/"ELECTRON" not in globals()) TRIP
                       on the host module globals?
  V2 (Γ-field wiring): does the host's moving-Γ=−1 cage Γ-field route through the
                       α-baked KAPPA_CHIRAL_ELECTRON (= α·κ̃)?
  V3 (Q-slot)        : is the host's extract_quality_factor() an EMPTY-slot cold
                       ring-down, or a closed-form golden-torus α⁻¹ form that
                       algebraically equals 4π³+π²+π = 137.036?

Run:  PYTHONPATH=src python src/scripts/vol_1_foundations/cage_winding_gate0_alpha_cleanliness_probe.py
"""

from __future__ import annotations

import numpy as np

# This is a DIAGNOSTIC (the meter, not the engine): it intentionally references α
# to demonstrate the host's α-contamination. The α references are imported from the
# canonical source (ave-canonical-source), never hard-coded — the engine under test
# is what must be α-free, not this probe.
from ave.core.constants import ALPHA, ALPHA_COLD_INV

ALPHA_INV_COLD = ALPHA_COLD_INV  # = 4π³+π²+π ≈ 137.0363 (golden-torus cold α⁻¹)
ALPHA_INV_CODATA = 1.0 / ALPHA   # CODATA α⁻¹ ≈ 137.0360


def _canonical_alpha_leak_guard(module_globals: dict) -> dict:
    """The verbatim canonical guard (vacuum_varactor_scatter.py:110-112) applied to
    an arbitrary module-globals dict. Returns which forbidden symbols are reachable.
    TRIPS if any of ALPHA / Q_TANK / ELECTRON is in scope."""
    forbidden = ("ALPHA", "Q_TANK", "ELECTRON")
    reachable = {sym: (sym in module_globals) for sym in forbidden}
    return {
        "reachable": reachable,
        "trips": any(reachable.values()),
        "tripped_on": [s for s, v in reachable.items() if v],
    }


def probe_v1_import_guard() -> dict:
    """V1 — apply the canonical α-leak guard to the host module globals."""
    import ave.topological.cosserat_field_3d as host

    res = _canonical_alpha_leak_guard(vars(host))
    res["kappa_chiral_electron_present"] = "KAPPA_CHIRAL_ELECTRON" in vars(host)
    res["kappa_chiral_electron_value"] = vars(host).get("KAPPA_CHIRAL_ELECTRON")
    res["kappa_tilde_electron_value"] = vars(host).get("KAPPA_TILDE_ELECTRON")
    return res


def probe_v2_gamma_field_wiring() -> dict:
    """V2 — does the host's cage Γ-field route through the α-baked κ_chiral default?

    Static cite: cosserat_field_3d.py:1842-1853 — _impedance_gamma_field() calls
    _update_saturation_kernels(..., KAPPA_CHIRAL_ELECTRON) → S_μ,S_ε → Z_eff → Γ.
    The cage clamp weight (relu(−Γ), :1957) is frozen from THIS Γ-field.
    """
    import ave.topological.cosserat_field_3d as host

    kappa_chiral = host.KAPPA_CHIRAL_ELECTRON  # = ALPHA · κ̃ (α-baked default)
    kappa_tilde = host.KAPPA_TILDE_ELECTRON    # = 6/5 (α-free topological factor)
    # The α-baked default is exactly ALPHA × 1.2:
    alpha_baked_ratio = kappa_chiral / kappa_tilde  # == ALPHA if α is the only factor
    return {
        "cage_gamma_default_kappa": kappa_chiral,
        "alpha_free_kappa_tilde": kappa_tilde,
        "kappa_chiral_over_kappa_tilde": alpha_baked_ratio,
        "is_alpha_baked": abs(alpha_baked_ratio - ALPHA) < 1e-9,
    }


def probe_v3_q_slot() -> dict:
    """V3 — is the host's extract_quality_factor() an EMPTY slot, or a baked α⁻¹?

    Static cite: cosserat_field_3d.py:2422-2425
        return 16π³·(R·r) + 4π²·(R·r) + π·d
    This is the GOLDEN-TORUS Q form. At R·r = 1/4, d=1 it equals 4π³+π²+π EXACTLY
    = the cold α⁻¹ = 137.036. It is a closed-form geometric formula, NOT a cold
    ring-down measurement: the Q-slot is pre-filled with the 137 echo by construction.
    """
    import ave.topological.cosserat_field_3d as host

    def q_formula(Rr: float, d: float = 1.0) -> float:
        return 16.0 * np.pi**3 * Rr + 4.0 * np.pi**2 * Rr + np.pi * d

    # The exact normalization that makes the host formula == α⁻¹:
    q_at_quarter = q_formula(0.25)

    # And on a real seeded (2,3) state (no ring-down — the formula is geometric):
    solver = host.CosseratField3D(nx=24, ny=24, nz=24)
    solver.initialize_electron_2_3_sector(R_target=6.0, r_target=2.0)
    R, r = solver.extract_shell_radii()
    q_seeded = solver.extract_quality_factor()

    return {
        "q_formula_at_Rr_quarter": q_at_quarter,
        "alpha_inv_cold": ALPHA_INV_COLD,
        "q_quarter_equals_alpha_inv": abs(q_at_quarter - ALPHA_INV_COLD) < 1e-6,
        "seeded_R": float(R),
        "seeded_r": float(r),
        "seeded_Rr": float(R * r),
        "seeded_Q": float(q_seeded),
        "is_ringdown_measurement": False,  # it is a closed-form geometric formula
    }


def probe_v4_alpha_free_baseline() -> dict:
    """V4 — the existing α-FREE _bulk.py cold-Q known-negative for contrast.

    The L3 mass-cage T3.4b cold ring-down on the Master-Equation scalar engine
    (NOT the Cosserat host) is α-free (Z_eff=√S, no κ_chiral, no Q_TANK/ELECTRON)
    and lands at Q_ringdown≈30.75, Q_linewidth≈3.75 — NOT 137. This is the
    KNOWN-NEGATIVE the Gate-0 host is asked to reproduce with the Q-slot empty.
    """
    # Run the α-free bulk cage cold-Q via the _bulk helpers (no Cosserat host).
    # Imported as a proper package module so its relative imports resolve.
    from tests.engine_acceptance import _bulk as B

    # Guard: _bulk imports NO α-bearing symbol.
    bulk_guard = _canonical_alpha_leak_guard(vars(B))

    enga = B.make_cage_engine(N=72, S_min=1e-3, A_cap=0.999, pml_thickness=12)
    probe_idx = B.breathing_kick_cage(
        enga, frac=0.9, core_sigma=8.0, kick_width=2.0, kick_amp=0.01
    )
    dVdt = B.record_breathing_dVdt(enga, probe_idx, 6000)
    ev = B.cutoff_eigenfrequency(enga, dVdt)
    rd = B.ringdown_Q(enga, dVdt, ev["omega_cutoff"])
    return {
        "engine": "MasterEquationFDTD/_bulk (NOT the Cosserat host)",
        "alpha_guard_trips_on_bulk": bulk_guard["trips"],
        "omega_cutoff": float(ev["omega_cutoff"]),
        "Q_ringdown": float(rd["Q_ringdown"]),
        "Q_linewidth": float(ev["q_linewidth"]),
        "matches_137": abs(float(rd["Q_ringdown"]) - ALPHA_INV_COLD) < 20.0,
    }


def main() -> None:
    print("=" * 78)
    print("GATE 0 — cage⊗winding-engine host α-cleanliness probe (REFUTE-BY-DEFAULT)")
    print("=" * 78)

    v1 = probe_v1_import_guard()
    print("\n[V1] α-leak import-guard on the Cosserat host module globals")
    print(f"     reachable: {v1['reachable']}")
    print(f"     GUARD TRIPS? {v1['trips']}  (tripped on: {v1['tripped_on']})")
    print(f"     KAPPA_CHIRAL_ELECTRON present={v1['kappa_chiral_electron_present']} "
          f"value={v1['kappa_chiral_electron_value']}  (= α·κ̃, α-baked)")

    v2 = probe_v2_gamma_field_wiring()
    print("\n[V2] host cage Γ-field κ default (cosserat_field_3d.py:1850)")
    print(f"     cage Γ default κ_chiral = {v2['cage_gamma_default_kappa']:.10g} (α-baked)")
    print(f"     α-free κ̃               = {v2['alpha_free_kappa_tilde']:.10g}")
    print(f"     κ_chiral / κ̃ = {v2['kappa_chiral_over_kappa_tilde']:.10g}  "
          f"is exactly α? {v2['is_alpha_baked']}")

    v3 = probe_v3_q_slot()
    print("\n[V3] host extract_quality_factor() — the Q-slot (cosserat_field_3d.py:2422)")
    print(f"     formula 16π³(R·r)+4π²(R·r)+π  at R·r=1/4  = {v3['q_formula_at_Rr_quarter']:.6f}")
    print(f"     cold α⁻¹ = 4π³+π²+π                       = {v3['alpha_inv_cold']:.6f}")
    print(f"     Q(R·r=1/4) == α⁻¹ EXACTLY? {v3['q_quarter_equals_alpha_inv']}  <-- 137 LEAK")
    print(f"     on a seeded (2,3) state: R={v3['seeded_R']:.3f} r={v3['seeded_r']:.3f} "
          f"R·r={v3['seeded_Rr']:.3f}  Q={v3['seeded_Q']:.2f}")
    print(f"     is a cold ring-down measurement? {v3['is_ringdown_measurement']} "
          f"(it is a closed-form golden-torus α⁻¹ form)")

    v4 = probe_v4_alpha_free_baseline()
    print("\n[V4] α-FREE _bulk.py cold-Q known-negative (the Q-slot-EMPTY contrast)")
    print(f"     engine: {v4['engine']}")
    print(f"     α-guard trips on _bulk? {v4['alpha_guard_trips_on_bulk']}  (False = α-clean)")
    print(f"     ω_cutoff={v4['omega_cutoff']:.4f}  Q_ringdown={v4['Q_ringdown']:.3f}  "
          f"Q_linewidth={v4['Q_linewidth']:.3f}")
    print(f"     Q ≈ 137? {v4['matches_137']}  → Q≈30.8 ≠ 137 (clean α-free negative)")

    print("\n" + "=" * 78)
    stop = v1["trips"] or v3["q_quarter_equals_alpha_inv"]
    print(f"GATE-0 VERDICT: {'HARD STOP' if stop else 'PASS'}")
    print("=" * 78)
    if stop:
        print("The Cosserat host is α-CONTAMINATED on the Q-readout path:")
        if v1["trips"]:
            print(f"  - V1: the α-leak guard TRIPS (ALPHA in host globals).")
        if v2["is_alpha_baked"]:
            print(f"  - V2: the cage Γ-field default routes through κ_chiral = α·κ̃.")
        if v3["q_quarter_equals_alpha_inv"]:
            print(f"  - V3: extract_quality_factor() is a closed-form golden-torus α⁻¹ "
                  f"(Q-slot NOT empty; 137 baked).")
        print("The α-FREE cold-Q≈30.8 known-negative lives on the _bulk.py "
              "MasterEquationFDTD route (V4), NOT this host's geometric Q form.")


if __name__ == "__main__":
    main()
