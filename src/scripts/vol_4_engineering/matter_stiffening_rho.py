"""
THE MATTER-STIFFENING DERIVATION
================================
Does matter's asymmetric channel loading drive the local bond-stiffness ratio
ρ_eff = k_a,eff / k_s,eff from the Ax3 cold point (ρ=1, PR #516) toward the
stiff-matter point (ρ*≈9.77, the K=2G / ν=2/7 locus, PR #506)?

GRANT'S HYPOTHESIS (test-blind): matter = standing/self-trapped waves = DC bias
= per-channel saturation = local stiffening; radiation = pure AC = zero
time-averaged bias (the pump-nulls) = no stiffening.

Prereg (FROZEN): research/2026-07-04_matter-stiffening-rho_prereg_FROZEN.md

CANON-FORCED COMPOSITION (derived in the prereg, NOT guessed):

    axial spring:  C_eff = C_0 / S_axial   (nonlinear-vacuum-capacitance.md:27, Q1=(B))
                   C = ξ²/k  (TKI identity, natural-units-cheatsheet.md:86)
                   ⟹ k_a = ξ²/C_eff = k_{a,0} · S_axial

    shear spring:  G/G_0 = S_shear  (scale_invariant.shear_modulus_ratio, verbatim)
                   c_shear = c_0·√S_shear, c²∝k_s  ⟹ k_s = k_{s,0} · S_shear

    ⟹  ρ_eff = k_a,eff / k_s,eff = ρ_cold · (S_axial / S_shear)

ρ_cold = 1 (Ax3-forced, PR #516). The ratio moves ONLY under ASYMMETRIC loading
(S_axial ≠ S_shear). Symmetric loading (S_axial = S_shear) ⟹ ρ_eff = ρ_cold
IDENTICALLY — the radiation control / R1 INVARIANT-S2 null.

ANTI-TUNE GUARD (prereg §5.6): this driver takes NO free ρ*-target parameter.
The number 9.77 enters ONLY as a read-off comparison constant (RHO_STAR_IMPORTED
below), never as an input the sweep is fit to. It is GR-imported (PR #506).

The kernel S(A) and the operating-point amplitudes are imported from canon
(ave.axioms.scale_invariant, ave.core.constants) — nothing is hand-set.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.axioms.scale_invariant import saturation_factor, shear_modulus_ratio
from ave.core.constants import ALPHA, V_SNAP

# ────────────────────────────────────────────────────────────────────
# Canon anchors (imported / read-off — NOT tuned)
# ────────────────────────────────────────────────────────────────────

# Cold point: Ax3-forced knob-free (PR #516). ρ_bond = k_a/k_s = 1.
RHO_COLD = 1.0

# Stiff-matter point: the ν=2/7 ⟺ K=2G locus, GR-IMPORTED (PR #506,
# research/2026-07-04_srs-elastic-tensor_result.md:94). This is a READ-OFF
# comparison constant, NEVER an input to the sweep (anti-tune guard).
RHO_STAR_IMPORTED = 9.7734

# A1 mass-core operating point: A = V_yield/V_snap = √α (def-vyvsn1,
# Grant-ratified 2026-06-30, nonlinear-vacuum-capacitance.md:18,36). The core
# operates DEEPLY SUB-SATURATED — that is WHY it binds.
A_CORE_SQRT_ALPHA = np.sqrt(ALPHA)  # ≈ 0.08542


# ────────────────────────────────────────────────────────────────────
# The canon-forced per-channel saturation → stiffness maps
# ────────────────────────────────────────────────────────────────────


def k_axial_over_k0(A_axial: np.ndarray) -> np.ndarray:
    r"""
    Axial (longitudinal-A1) stiffness ratio k_a/k_{a,0} under saturation.

    Chain (canon, prereg Step 1):
      C_eff = C_0 / S(A_axial)   [nonlinear-vacuum-capacitance.md:27, Q1=(B)]
      k     = ξ²/C               [TKI identity, natural-units-cheatsheet.md:86]
      ⟹ k_a/k_{a,0} = C_0/C_eff = S(A_axial)

    We compute it VIA the compliance inversion (not by directly returning S) so
    the validation harness can cross-check the sign — the one place a sign error
    hides (prereg §5.5).
    """
    S = saturation_factor(A_axial, yield_limit=1.0)  # A already normalized to yield
    C_eff_over_C0 = 1.0 / S  # C_eff = C_0/S
    return 1.0 / C_eff_over_C0  # k_a/k_{a,0} = C_0/C_eff = S


def k_shear_over_k0(A_shear: np.ndarray) -> np.ndarray:
    r"""
    Shear (deviatoric-G) stiffness ratio k_s/k_{s,0} under saturation.

    Chain (canon, prereg Step 1):
      G/G_0 = S(A_shear)         [scale_invariant.shear_modulus_ratio, verbatim]
      c_shear = c_0·√S, c²∝k_s   [port map, CLAUDE.md:75]
      ⟹ k_s/k_{s,0} = S(A_shear)

    Computed via shear_modulus_ratio (the canon alias) so the two derivations
    (modulus ratio vs c²) are cross-checked to agree.
    """
    return shear_modulus_ratio(A_shear, yield_strain=1.0)


def rho_eff(A_axial: np.ndarray, A_shear: np.ndarray) -> np.ndarray:
    r"""
    ρ_eff = k_a,eff / k_s,eff = ρ_cold · (S_axial / S_shear).

    The canon-forced composition. ρ_cold = 1 (Ax3-forced, PR #516).
    """
    return RHO_COLD * (k_axial_over_k0(A_axial) / k_shear_over_k0(A_shear))


# ────────────────────────────────────────────────────────────────────
# Validation harness (Rule 10 — run BEFORE reading the verdict)
# ────────────────────────────────────────────────────────────────────


def run_validation() -> dict:
    """All validate-on-known checks. HALT (raise) if any fails."""
    checks = {}

    # V1 — cold recovery: A=0 ⟹ ρ_eff = 1
    r_cold = float(rho_eff(np.array(0.0), np.array(0.0)))
    checks["V1_cold_recovery"] = {
        "rho_eff": r_cold,
        "target": 1.0,
        "pass": bool(abs(r_cold - 1.0) < 1e-12),
    }

    # V2 — symmetric-loading null: S_axial = S_shear ⟹ ρ_eff = ρ_cold identically
    #      (the R1/INVARIANT-S2 / radiation-control check)
    A_sym = np.array([0.1, 0.5, 0.9, 0.99])
    r_sym = rho_eff(A_sym, A_sym)  # same amplitude both channels
    checks["V2_symmetric_null"] = {
        "A_sym": A_sym.tolist(),
        "rho_eff": r_sym.tolist(),
        "max_dev_from_cold": float(np.max(np.abs(r_sym - RHO_COLD))),
        "pass": bool(np.max(np.abs(r_sym - RHO_COLD)) < 1e-12),
    }

    # V3 — kernel identity: S(√α) = √(1−α)
    S_core = float(saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=1.0))
    S_core_expected = float(np.sqrt(1.0 - ALPHA))
    checks["V3_kernel_identity"] = {
        "S_sqrt_alpha": S_core,
        "sqrt_1_minus_alpha": S_core_expected,
        "pass": bool(abs(S_core - S_core_expected) < 1e-12),
    }

    # V4 — monotonicity: ρ_eff(A_wall) monotone in A_wall for each assignment
    A_wall = np.linspace(0.0, 0.999, 200)
    S_core_fixed = saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=1.0)
    # SHEAR-LOADS: axial sub-saturated (√α), shear = A_wall → ρ_eff rises
    r_shear_loads = S_core_fixed / saturation_factor(A_wall, yield_limit=1.0)
    # AXIAL-LOADS: shear sub-saturated (√α), axial = A_wall → ρ_eff falls
    r_axial_loads = saturation_factor(A_wall, yield_limit=1.0) / S_core_fixed
    checks["V4_monotonicity"] = {
        "shear_loads_monotone_increasing": bool(np.all(np.diff(r_shear_loads) >= -1e-12)),
        "axial_loads_monotone_decreasing": bool(np.all(np.diff(r_axial_loads) <= 1e-12)),
        "pass": bool(
            np.all(np.diff(r_shear_loads) >= -1e-12)
            and np.all(np.diff(r_axial_loads) <= 1e-12)
        ),
    }

    # V5 — composition sign cross-check: k_a = ξ²/C_eff with C_eff=C_0/S must
    #      reproduce k_a/k_0 = S independently (guards the compliance inversion)
    A_test = np.array([0.1, 0.5, 0.9])
    S_direct = saturation_factor(A_test, yield_limit=1.0)
    k_via_compliance = k_axial_over_k0(A_test)
    checks["V5_compliance_inversion_sign"] = {
        "S_direct": S_direct.tolist(),
        "k_a_over_k0_via_compliance": np.asarray(k_via_compliance).tolist(),
        "max_dev": float(np.max(np.abs(np.asarray(k_via_compliance) - S_direct))),
        "pass": bool(np.max(np.abs(np.asarray(k_via_compliance) - S_direct)) < 1e-12),
    }

    all_pass = all(c["pass"] for c in checks.values())
    checks["ALL_PASS"] = all_pass
    if not all_pass:
        raise RuntimeError(f"VALIDATION HALT — a validate-on-known check failed:\n{json.dumps(checks, indent=2)}")
    return checks


# ────────────────────────────────────────────────────────────────────
# The derivation: both channel-assignments, blind
# ────────────────────────────────────────────────────────────────────


def _crossing_amplitude(A_wall: np.ndarray, rho_profile: np.ndarray, target: float) -> float | None:
    """Linear-interpolated A_wall where rho_profile crosses target, or None."""
    r = np.asarray(rho_profile)
    # find first bracketing pair
    for i in range(len(r) - 1):
        lo, hi = r[i], r[i + 1]
        if (lo - target) * (hi - target) <= 0 and lo != hi:
            frac = (target - lo) / (hi - lo)
            return float(A_wall[i] + frac * (A_wall[i + 1] - A_wall[i]))
    return None


def run_derivation() -> dict:
    """Both channel-assignments (SHEAR-LOADS, AXIAL-LOADS), reported blind."""
    # The near-yield wall ladder the corpus uses (nonlinear-vacuum-capacitance
    # table rungs) plus a dense sweep for the profile + crossing.
    canon_rungs = np.array([np.sqrt(ALPHA), 0.5, 0.9, 0.99, 0.999])  # def-vyvsn1 / table rungs
    dense = np.linspace(0.0, 0.99999, 5000)

    S_core = float(saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=1.0))  # ≈ 0.9963

    out = {}
    for name, is_shear_loads in [("SHEAR_LOADS", True), ("AXIAL_LOADS", False)]:
        # SHEAR_LOADS: axial fixed sub-saturated (√α), shear swept to yield.
        # AXIAL_LOADS: shear fixed sub-saturated (√α), axial swept to yield.
        def rho_of_wall(A_wall):
            if is_shear_loads:
                return rho_eff(np.full_like(A_wall, A_CORE_SQRT_ALPHA), A_wall)
            return rho_eff(A_wall, np.full_like(A_wall, A_CORE_SQRT_ALPHA))

        r_rungs = rho_of_wall(canon_rungs)
        r_dense = rho_of_wall(dense)
        cross = _crossing_amplitude(dense, r_dense, RHO_STAR_IMPORTED)

        # Direction: does ρ_eff rise or fall as the wall approaches yield?
        direction = "STIFFENING" if r_dense[-1] > RHO_COLD else "SOFTENING"

        # Is the crossing amplitude canon-distinguished? Test against √α and the
        # def-vyvsn1 rungs (√α, and the wall-at-yield A→1). "Arbitrary" otherwise.
        crossing_canon_status = None
        if cross is not None:
            near_sqrt_alpha = abs(cross - np.sqrt(ALPHA)) < 1e-3
            near_one_minus_alpha = abs(cross - (1.0 - ALPHA)) < 1e-3
            near_yield_wall = cross > 0.999  # the def-vyvsn1 A→1 wall
            crossing_canon_status = {
                "A_wall_at_crossing": cross,
                "near_sqrt_alpha": bool(near_sqrt_alpha),
                "near_1_minus_alpha": bool(near_one_minus_alpha),
                "near_yield_wall_Ato1": bool(near_yield_wall),
                "S_shear_at_crossing": float(saturation_factor(cross, yield_limit=1.0))
                if is_shear_loads
                else S_core,
                "canon_distinguished": bool(
                    near_sqrt_alpha or near_one_minus_alpha or near_yield_wall
                ),
            }

        out[name] = {
            "fixed_channel": "axial@√α (sub-saturated)" if is_shear_loads else "shear@√α (sub-saturated)",
            "swept_channel": "shear→yield" if is_shear_loads else "axial→yield",
            "S_core_fixed": S_core,
            "canon_rungs_A_wall": canon_rungs.tolist(),
            "rho_eff_at_rungs": np.asarray(r_rungs).tolist(),
            "rho_eff_at_yield_limit": float(r_dense[-1]),
            "direction": direction,
            "crosses_rho_star_9.77": cross is not None,
            "crossing": crossing_canon_status,
        }
    return out


def run_radiation_control() -> dict:
    """
    Pure-AC traveling wave: zero time-averaged amplitude ⟨A⟩=0 on the loading
    channel. Two independent reasons ρ_eff = ρ_cold identically:
      (1) symmetric-internal (R1, node-up §2): both grades see the SAME ⟨A²⟩,
          so S_axial = S_shear ⟹ ρ_eff = ρ_cold.
      (2) the DC-bias operating point is the time-average; a pure AC drive pumps
          zero net displacement charge (clm-clvchn NULL-CONFIRMED-FINAL) ⟹ no
          net operating-point shift on either channel.
    We confirm (1) numerically: a symmetric time-averaged ⟨A²⟩ over a sinusoid.
    """
    # Pure AC: A(t) = A0·sin(ωt). Time-averaged bias ⟨A⟩ = 0. If BOTH channels
    # are driven by the same AC field (symmetric-internal), they share ⟨A²⟩,
    # so S_axial = S_shear regardless of A0.
    A0 = np.array([0.1, 0.3, 0.6])
    t = np.linspace(0, 2 * np.pi, 10_000)
    results = []
    for a0 in A0:
        A_of_t = a0 * np.sin(t)
        mean_A = float(np.mean(A_of_t))  # ⟨A⟩ = 0
        rms_A = float(np.sqrt(np.mean(A_of_t**2)))  # the effective ⟨A²⟩^½ bias
        # Symmetric-internal: BOTH channels see rms_A ⟹ ρ_eff = ρ_cold
        r = float(rho_eff(np.array(rms_A), np.array(rms_A)))
        results.append(
            {
                "A0": float(a0),
                "mean_A_time_averaged": mean_A,
                "rms_A_effective_bias": rms_A,
                "rho_eff_symmetric": r,
                "equals_rho_cold": bool(abs(r - RHO_COLD) < 1e-12),
            }
        )
    all_null = all(r["equals_rho_cold"] for r in results)
    return {
        "results": results,
        "rho_eff_equals_rho_cold_for_all_AC": all_null,
        "mechanism": "symmetric-internal R1 (S_axial=S_shear) + clm-clvchn displacement-pump null",
        "provenance": "clm-clvchn NULL-CONFIRMED-FINAL 2026-07-02 (project-cleave-01.md:40-59)",
    }


def main():
    validation = run_validation()  # HALT-gated — raises on any failure
    derivation = run_derivation()
    radiation = run_radiation_control()

    out = {
        "title": "THE MATTER-STIFFENING DERIVATION",
        "composition": "rho_eff = rho_cold * (S_axial / S_shear); rho_cold=1 (Ax3, PR#516)",
        "rho_star_imported_readoff_only": RHO_STAR_IMPORTED,
        "A_core_sqrt_alpha": float(A_CORE_SQRT_ALPHA),
        "validation": validation,
        "derivation_both_assignments": derivation,
        "radiation_control": radiation,
    }

    out_dir = Path(__file__).resolve().parent / "_output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "matter_stiffening_rho.json").write_text(json.dumps(out, indent=2))

    # Console summary
    print("=" * 72)
    print("MATTER-STIFFENING DERIVATION — ρ_eff = ρ_cold·(S_axial/S_shear)")
    print("=" * 72)
    print(f"Validation ALL_PASS: {validation['ALL_PASS']}")
    print(f"A1-core operating point A=√α = {A_CORE_SQRT_ALPHA:.5f}, S_core = {np.sqrt(1-ALPHA):.5f}")
    print(f"ρ*_imported (read-off only) = {RHO_STAR_IMPORTED}")
    print()
    for name, d in derivation.items():
        print(f"--- {name} (fixed {d['fixed_channel']}, sweep {d['swept_channel']}) ---")
        print(f"    direction: {d['direction']}")
        print(f"    ρ_eff at yield limit: {d['rho_eff_at_yield_limit']:.4g}")
        print(f"    crosses 9.77: {d['crosses_rho_star_9.77']}")
        if d["crossing"]:
            c = d["crossing"]
            print(f"    crossing A_wall = {c['A_wall_at_crossing']:.5f}  "
                  f"canon-distinguished={c['canon_distinguished']}")
        print(f"    ρ_eff at rungs {[round(x,3) for x in d['canon_rungs_A_wall']]}:")
        print(f"                   {[round(x,4) for x in d['rho_eff_at_rungs']]}")
        print()
    print(f"Radiation control: ρ_eff=ρ_cold for all pure-AC drives: "
          f"{radiation['rho_eff_equals_rho_cold_for_all_AC']}")
    print(f"Output → {out_dir / 'matter_stiffening_rho.json'}")


if __name__ == "__main__":
    main()
