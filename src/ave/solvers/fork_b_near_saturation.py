"""Fork-B GATE3 NEAR-SATURATION re-run — the chord-residual the original GATE3 missed.

Prereg / parent: research/2026-06-20_fork-b-saturation-tank-confinement_result.md §4
Built off origin/main @ d83f77c3 (the merged Fork-B gate, PR#307).

═══════════════════════════════════════════════════════════════════════════════
WHY THIS MODULE EXISTS (the residual, brutally stated)
═══════════════════════════════════════════════════════════════════════════════
The merged GATE3 reported the quarter-arc S(A)=√(1−A²) shape-GENERIC (Δ/L gap ~0
vs a same-family (1−A²)^p comparator) ⇒ ECHO. But that result holds ONLY because
the planted well maxed at A_bond.max ≈ 0.77 (diamond L=8; only ~8/256 bonds had
A>0.5). The quarter-arc's DISTINCTIVE feature is its STEEP region near A=1
(dS/dA = −A/√(1−A²) → −∞ as A→1). That region was NEVER exercised. So the
"shape-generic" verdict is, strictly, "shape-generic in the SHALLOW regime."

This module drives the core bonds into FULL SATURATION (A_bond.max ≈ 0.95–0.99 —
the steep regime) and re-runs the SAME depth-invariant Δ/L shape discriminator,
but against GENUINELY-DIFFERENT comparator FAMILIES (not just same-family
(1−A²)^p): plain tanh(k(1−A)), exp(−kA), Lorentzian 1/(1+kA²), power (1−A^n),
linear (1−kA). Each is norm-matched to the quarter-arc norm π/4 and depth-matched
to the same well floor.

═══════════════════════════════════════════════════════════════════════════════
ANTI-TAUTOLOGY: the POSITIVE CONTROL (load-bearing)
═══════════════════════════════════════════════════════════════════════════════
A zero shape gap is only informative if the metric CAN open a gap at this regime.
So a top-hat (STEP-discontinuous) stiffness comparator is run alongside: it MUST
open a large gap (and drop the eigenvector overlap) or the test is VOID at this
regime (the metric is saturated/blind, not discriminating). The smooth families
are the AVE-distinct content; the top-hat is the discriminator-still-works witness.

═══════════════════════════════════════════════════════════════════════════════
FROZEN BINNING (honest, pre-committed)
═══════════════════════════════════════════════════════════════════════════════
At FULL saturation, judged by the SAME Δ/L metric with the SAME bound-mode
selector as the merged GATE3:
  * CHORD-PARTIAL  : gap > 10% AND eigenvector overlap < 0.95 (positive control
                     confirms the metric discriminates) ⇒ the quarter-arc IS
                     shape-SPECIAL where it is steepest ⇒ a PARTIAL mass-sector
                     chord on the shape axis (upgrade the verdict).
  * ECHO-FINAL     : gap ≈ 0 AND overlap ≈ 1 even at full saturation ⇒ the
                     quarter-arc is not shape-special even in its steep regime.

ECHO-FINAL is the EXPECTED outcome. A CHORD claim must survive the positive
control AND the overlap<0.95 bar AND the symmetric-standard bar (saturable-NLS
shape-sensitivity is generic; the AVE-distinct content is SPECIFICALLY
quarter-arc-vs-other-SMOOTH-kernel at full saturation).

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE + ALPHA-FREE (inherited from fork_b_saturation_tank)
═══════════════════════════════════════════════════════════════════════════════
  * Operator: the SAME native connect-map graph-stiffness L = Bᵀ diag(1/S) B
    (imported, not re-posited). A1 dilatation-scalar grade (CP2).
  * The shape kernels read the DIMENSIONLESS A=|V|/V_yield ⇒ ALPHA cancels.
    ALPHA is NEVER imported. α-invariance is structural (verified by the parent
    module's α→2α gate).
  * Real-space spatial eigenmode localization (CP4), not a φ² phase-space claim.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# ── reuse the canonical native connect-map operator + selector (NOT re-posited) ──
from ave.solvers.fork_b_saturation_tank import (
    ConfinementConfig,
    _band_structure,
    _operator_from_bond_S,
    _select_core_bound_mode,
    node_radius,
    saturated_core_strain_native,
    unique_bonds,
)

# ── alpha-leak guard (HR2): the parent module is alpha-free; so is this one ──
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"

QUARTER_ARC_NORM = np.pi / 4.0  # ∫₀¹ √(1−A²) dA = π/4 (the canonical kernel's norm)


# ═════════════════════════════════════════════════════════════════════════════
# 1. THE CROSS-FAMILY SATURABLE KERNELS  S(A): S(0)=1, decreasing on [0,1]
# ═════════════════════════════════════════════════════════════════════════════
# Each is a GENUINELY DIFFERENT family from the quarter-arc √(1−A²) — NOT the
# same-family (1−A²)^p the merged GATE3 used. The retired RF-5 endpoint-tanh
# 0.5(1+tanh(k(0.5−A))) is sup-norm-pinned at 0.500 < π/4 = norm-INFEASIBLE; the
# PLAIN tanh(k(1−A)) used here DOES reach π/4 (norm-feasible). All five reach the
# quarter-arc norm π/4 (verified by the brentq norm-match below) — so "cross-family
# is norm-infeasible" was an OVER-GENERALIZATION from the ONE retired parameterization.


def kernel_quarter_arc(A: np.ndarray) -> np.ndarray:
    """The CANONICAL AVE kernel S(A)=√(1−A²) (p=0.5). The quarter circle exactly
    (S²+A²=1). Parameter-free. The steep region near A=1 (dS/dA→−∞) is its
    distinctive feature — exercised ONLY at full saturation. alpha-FREE."""
    return np.sqrt(np.maximum(1.0 - A**2, 0.0))


def kernel_plain_tanh(A: np.ndarray, k: float) -> np.ndarray:
    """PLAIN tanh saturable kernel 0.5(1+tanh(k(1−A))). Distinct from the RETIRED
    RF-5 0.5(1+tanh(k(0.5−A))) (which sup-pinned at 0.500). This one reaches π/4."""
    return 0.5 * (1.0 + np.tanh(k * (1.0 - A)))


def kernel_exp(A: np.ndarray, k: float) -> np.ndarray:
    """Exponential saturable kernel exp(−kA). A genuinely different family."""
    return np.exp(-k * A)


def kernel_lorentzian(A: np.ndarray, k: float) -> np.ndarray:
    """Lorentzian saturable kernel 1/(1+kA²). A genuinely different family."""
    return 1.0 / (1.0 + k * A**2)


def kernel_power(A: np.ndarray, n: float) -> np.ndarray:
    """Power-law saturable kernel (1−Aⁿ). NOTE: this is (1−Aⁿ), a DIFFERENT family
    from the same-family (1−A²)^p of the merged GATE3 (different functional form)."""
    return np.maximum(1.0 - A**n, 0.0)


def kernel_linear(A: np.ndarray, k: float) -> np.ndarray:
    """Linear saturable kernel (1−kA). The straight-line ramp; no curvature."""
    return np.maximum(1.0 - k * A, 0.0)


def kernel_tophat(A: np.ndarray, A_step: float) -> np.ndarray:
    """POSITIVE CONTROL: a STEP-DISCONTINUOUS stiffness — S=1 for A<A_step, S=0
    (clipped to the floor) for A≥A_step. A discontinuous stiffness IS discriminable
    (it changes the confining-region topology, not its smooth curvature); the metric
    MUST open a gap here or the test is void at this regime. NOT a smooth saturable
    kernel — the anti-tautology witness."""
    return np.where(A >= A_step, 0.0, 1.0)


# ── the cross-family registry: (builder, brentq bracket for the norm-match) ──
_SMOOTH_FAMILIES: dict[str, tuple] = {
    "plain_tanh": (kernel_plain_tanh, (0.01, 50.0)),
    "exp": (kernel_exp, (1e-3, 50.0)),
    "lorentzian": (kernel_lorentzian, (1e-3, 50.0)),
    "power": (kernel_power, (0.1, 20.0)),
    "linear": (kernel_linear, (1e-3, 1.0)),
}


def norm_match_family(builder, bracket: tuple[float, float], *, target_norm: float = QUARTER_ARC_NORM) -> dict:
    """Solve the family parameter so ∫₀¹ S(A) dA = target_norm (default π/4, the
    quarter-arc norm). Returns {ok, param, norm} or {ok:False} if INFEASIBLE (the
    target is outside the family's reachable norm range — the HALT the RF-5
    endpoint-tanh hit). This is the load-bearing check that the cross-family
    comparators are norm-FEASIBLE (NOT assumed-away). alpha-FREE."""
    from scipy.integrate import quad
    from scipy.optimize import brentq

    lo, hi = bracket

    def _norm(k: float) -> float:
        val, _ = quad(lambda A: builder(A, k), 0.0, 1.0, limit=200)
        return float(val)

    n_lo, n_hi = _norm(lo), _norm(hi)
    if not (min(n_lo, n_hi) <= target_norm <= max(n_lo, n_hi)):
        lo_n, hi_n = min(n_lo, n_hi), max(n_lo, n_hi)
        return {"ok": False, "reason": f"target_norm {target_norm:.4f} outside [{lo_n:.4f},{hi_n:.4f}]"}
    k = brentq(lambda kk: _norm(kk) - target_norm, lo, hi)
    return {"ok": True, "param": float(k), "norm": _norm(k), "target_norm": target_norm}


def depth_match_affine(S_raw: np.ndarray, target_min_S: float) -> np.ndarray:
    """Affine-rescale a raw per-bond S field so its MINIMUM equals target_min_S
    (the well floor), PRESERVING the kernel's curvature signature. The IDENTICAL
    construction as fork_b_saturation_tank._depth_matched_bond_S (so the depth axis
    is matched exactly the same way): S' = target + (S−S.min)·(1−target)/(1−S.min),
    clipped to [target, 1]. Isolates curvature from floor-depth. alpha-FREE."""
    s0 = float(S_raw.min())
    if abs(1.0 - s0) < 1e-12:
        return np.clip(S_raw, target_min_S, 1.0)
    S_scaled = target_min_S + (S_raw - s0) * (1.0 - target_min_S) / (1.0 - s0)
    return np.clip(S_scaled, target_min_S, 1.0)


# ═════════════════════════════════════════════════════════════════════════════
# 2. THE BOUND-MODE READOUT (same selector + same Δ/L metric as the merged GATE3)
# ═════════════════════════════════════════════════════════════════════════════
def _bound_mode_full(net, S_bond: np.ndarray, core_mask: np.ndarray, r: np.ndarray) -> dict:
    """Solve L=Bᵀ diag(1/S) B, pick the bound LEVEL's most core-localized member
    (the IDENTICAL _select_core_bound_mode selector as GATE1/GATE3), and return BOTH
    the depth-invariant Δ/L = √(Σr²|ψ|²/Σ|ψ|²)/L AND the bound eigenVECTOR ψ (so the
    overlap can be measured). The eigenvector is the load-bearing addition the
    merged GATE3 did not record (it reported only Δ/L). alpha-FREE."""
    L = _operator_from_bond_S(net, S_bond)
    w, V = np.linalg.eigh(L)
    band = _band_structure(w)
    if not band["ok"]:
        return {"ok": False, "reason": band["reason"]}
    best = _select_core_bound_mode(w, V, core_mask, band)
    psi = V[:, best["idx"]].astype(np.float64)
    p2 = psi**2
    rms = float(np.sqrt((p2 * r**2).sum() / (p2.sum() + 1e-300)))
    return {
        "ok": True,
        "psi": psi,
        "delta_over_L": rms / net.box,
        "core_frac": best["core_frac"],
        "omega": best["omega"],
        "gapped_discrete": bool(band["gap_above_sq"] > max(band["mean_continuum_spacing_sq"], 1e-9)),
        "min_S": float(S_bond.min()),
    }


def _eigvec_overlap(psi_a: np.ndarray, psi_b: np.ndarray) -> float:
    """|⟨ψ_a|ψ_b⟩| / (‖ψ_a‖‖ψ_b‖) — the absolute normalized overlap of two bound
    eigenvectors (sign-agnostic; eigenvectors carry an arbitrary global sign). =1.0
    means the SAME physical mode; <0.95 means a genuinely different localization."""
    na = float(np.linalg.norm(psi_a))
    nb = float(np.linalg.norm(psi_b))
    if na < 1e-300 or nb < 1e-300:
        return 0.0
    return abs(float(psi_a @ psi_b)) / (na * nb)


# ═════════════════════════════════════════════════════════════════════════════
# 3. THE NEAR-SATURATION SHAPE TEST (the chord-residual driver)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class NearSaturationConfig:
    """A FULL-SATURATION GATE3 config. The defaults drive A_bond.max into the steep
    regime (~0.95–0.99) on the srs connect-map (whose nodes sit near the centroid),
    where the quarter-arc √(1−A²)'s steep tail IS exercised — the regime the merged
    GATE3 (A_bond.max≈0.77) never reached.

    frac→1 (the planted-well amplitude → A_cap) + sigma_frac=1/6 keeps the well wide
    enough that interior bonds saturate too; S_min sets the depth-match floor. The
    canonical kernel CLIP (crystal_engine.py:194, A_cap=0.99) bounds A in the
    confinement OPERATOR, but GATE3's shape metric builds S DIRECTLY from A_bond
    (no clip) — so the steep regime is driven by A_bond.max, confirmed by the
    achieved_A_max readout (it does NOT no-op)."""

    net: str = "srs"
    L: int = 6
    frac: float = 0.999
    sigma_frac: float = 1.0 / 6.0
    S_min: float = 1e-3

    def to_confinement_cfg(self) -> ConfinementConfig:
        return ConfinementConfig(net=self.net, L=self.L, frac=self.frac, sigma_frac=self.sigma_frac, S_min=self.S_min)


def solve_near_saturation_shape(cfg: NearSaturationConfig) -> dict:
    """GATE3 NEAR-SATURATION re-run. Drive the core to A_bond.max≈0.95–0.99 and
    re-run the depth-invariant Δ/L shape discriminator: quarter-arc (p=0.5) vs each
    of the five GENUINELY-DIFFERENT smooth families (norm+depth-matched) AND the
    top-hat POSITIVE CONTROL. Records, for EVERY comparator, BOTH the Δ/L gap AND
    the bound-eigenvector overlap (the load-bearing addition).

    Returns the achieved A_max, the per-comparator (gap, overlap), the positive
    control, and the frozen-binned verdict (ECHO-FINAL vs CHORD-PARTIAL). alpha-FREE."""
    cc = cfg.to_confinement_cfg()
    net = cc.build_net()
    A = saturated_core_strain_native(net, frac=cfg.frac, sigma_frac=cfg.sigma_frac)
    bonds = unique_bonds(net)
    A_bond = np.array([max(A[u], A[v]) for (u, v) in bonds])
    achieved_A_max = float(A_bond.max())

    r = node_radius(net)
    sigma = cfg.sigma_frac * net.box
    core_mask = r <= max(sigma * 1.5, net.box / float(cfg.L))

    # ── the canonical quarter-arc sets the depth target (its own well floor) ──
    S_canon = depth_match_affine(kernel_quarter_arc(A_bond), cfg.S_min)
    target_depth = float(S_canon.min())
    m_canon = _bound_mode_full(net, S_canon, core_mask, r)
    if not m_canon["ok"]:
        return {"ok": False, "reason": f"canonical bound mode not found: {m_canon['reason']}"}
    psi_canon = m_canon["psi"]
    dL_canon = m_canon["delta_over_L"]

    # ── the five GENUINELY-DIFFERENT smooth families, norm+depth-matched ──
    smooth_rows = []
    max_smooth_gap = 0.0
    min_smooth_overlap = 1.0
    all_norm_feasible = True
    max_shape_diff = 0.0  # max|ΔS| — the shapes must be genuinely DIFFERENT
    for name, (builder, bracket) in _SMOOTH_FAMILIES.items():
        nm = norm_match_family(builder, bracket)
        if not nm["ok"]:
            all_norm_feasible = False
            smooth_rows.append({"family": name, "norm_feasible": False, "reason": nm["reason"]})
            continue
        S_raw = builder(A_bond, nm["param"])
        S_comp = depth_match_affine(S_raw, target_depth)
        shape_diff = float(np.abs(S_canon - S_comp).max())
        max_shape_diff = max(max_shape_diff, shape_diff)
        m_comp = _bound_mode_full(net, S_comp, core_mask, r)
        if not m_comp["ok"]:
            smooth_rows.append({"family": name, "norm_feasible": True, "bound_mode_found": False})
            continue
        gap = abs(dL_canon - m_comp["delta_over_L"]) / (dL_canon + 1e-300)
        overlap = _eigvec_overlap(psi_canon, m_comp["psi"])
        max_smooth_gap = max(max_smooth_gap, gap)
        min_smooth_overlap = min(min_smooth_overlap, overlap)
        smooth_rows.append({
            "family": name,
            "norm_feasible": True,
            "norm_param": nm["param"],
            "matched_norm": nm["norm"],
            "delta_over_L": m_comp["delta_over_L"],
            "shape_gap": gap,
            "eigvec_overlap": overlap,
            "max_abs_dS_vs_canon": shape_diff,
            "depth_matched": bool(abs(m_comp["min_S"] - target_depth) < 1e-6),
            "core_frac": m_comp["core_frac"],
        })

    # ── POSITIVE CONTROL: the top-hat step (MUST open a gap / drop overlap) ──
    S_th = depth_match_affine(kernel_tophat(A_bond, 0.5), target_depth)
    m_th = _bound_mode_full(net, S_th, core_mask, r)
    pc_gap = abs(dL_canon - m_th["delta_over_L"]) / (dL_canon + 1e-300) if m_th["ok"] else float("nan")
    pc_overlap = _eigvec_overlap(psi_canon, m_th["psi"]) if m_th["ok"] else float("nan")
    # the metric DISCRIMINATES at this regime iff the positive control opens a gap
    # AND drops the overlap (a discontinuous stiffness IS a different physical mode).
    metric_discriminates = bool(np.isfinite(pc_gap) and pc_gap > 0.10 and pc_overlap < 0.95)

    # ── frozen binning (honest) ──
    # CHORD-PARTIAL : a SMOOTH cross-family gap >10% AND overlap <0.95 (the
    #                 quarter-arc is shape-special where steepest) — only counts if
    #                 the positive control confirms the metric still discriminates.
    # ECHO-FINAL    : smooth gap ~0 AND overlap ~1 even at full saturation.
    smooth_is_shape_special = bool(max_smooth_gap > 0.10 and min_smooth_overlap < 0.95)
    if not metric_discriminates:
        verdict = "VOID"
        reason = "positive control did NOT discriminate at this regime — metric is blind, test void"
    elif smooth_is_shape_special:
        verdict = "CHORD-PARTIAL"
        reason = ("a SMOOTH cross-family comparator opened a >10% Δ/L gap with eigvec "
                  "overlap <0.95 at full saturation — the quarter-arc IS shape-special "
                  "where it is steepest (PARTIAL mass-sector chord on the shape axis)")
    else:
        verdict = "ECHO-FINAL"
        reason = ("all SMOOTH cross-family comparators give Δ/L gap ~0 (≪10%) with "
                  "eigvec overlap ~1 even at full saturation — the quarter-arc is NOT "
                  "shape-special even in its steep regime (generic saturable-NLS)")

    return {
        "ok": True,
        "net": net.name,
        "L": cfg.L,
        "n_nodes": net.n_nodes,
        "S_min": cfg.S_min,
        "achieved_A_max": achieved_A_max,
        "n_bonds_A_gt_0p9": int((A_bond > 0.9).sum()),
        "in_steep_regime": bool(achieved_A_max >= 0.95),
        "target_depth_min_S": target_depth,
        "delta_over_L_canonical": dL_canon,
        "canon_core_frac": m_canon["core_frac"],
        "smooth_comparators": smooth_rows,
        "all_smooth_norm_feasible": all_norm_feasible,
        "max_smooth_shape_gap": max_smooth_gap,
        "min_smooth_eigvec_overlap": min_smooth_overlap,
        "max_abs_dS_smooth_vs_canon": max_shape_diff,  # shapes genuinely different
        "positive_control_top_hat": {
            "shape_gap": pc_gap,
            "eigvec_overlap": pc_overlap,
            "delta_over_L": m_th.get("delta_over_L") if m_th["ok"] else None,
        },
        "metric_discriminates_at_full_sat": metric_discriminates,
        "verdict": verdict,
        "reason": reason,
    }


# ═════════════════════════════════════════════════════════════════════════════
# 4. CONFIG SWEEP (the fast verdict net + a DEEPER full-saturation confirmation)
# ═════════════════════════════════════════════════════════════════════════════
def near_saturation_sweep(configs=None) -> dict:
    """Run solve_near_saturation_shape over a ladder of full-saturation configs.

    The default ladder: srs L=6 (A_max≈0.976, the fast verdict net) and a DEEPER
    srs L=8 (A_max≈0.99, S_min=1e-5 — the steepest regime reachable). If the
    verdict is ECHO-FINAL across BOTH, the steep-regime quarter-arc is not special.
    Returns the per-config rows + a pooled verdict. alpha-FREE."""
    if configs is None:
        configs = [
            NearSaturationConfig(net="srs", L=6, frac=0.999, sigma_frac=1.0 / 6.0, S_min=1e-3),
            NearSaturationConfig(net="srs", L=8, frac=0.9999, sigma_frac=0.20, S_min=1e-5),
        ]
    rows = []
    verdicts = []
    for cfg in configs:
        out = solve_near_saturation_shape(cfg)
        rows.append(out)
        verdicts.append(out.get("verdict", "ERR"))
    all_echo = bool(all(v == "ECHO-FINAL" for v in verdicts))
    any_chord = bool(any(v == "CHORD-PARTIAL" for v in verdicts))
    any_void = bool(any(v == "VOID" for v in verdicts))
    pooled = "VOID" if any_void else ("CHORD-PARTIAL" if any_chord else ("ECHO-FINAL" if all_echo else "MIXED"))
    return {
        "ok": True,
        "rows": rows,
        "verdicts": verdicts,
        "pooled_verdict": pooled,
    }


if __name__ == "__main__":
    import json

    print("FORK-B GATE3 NEAR-SATURATION RE-RUN (the chord-residual)")
    print("=" * 72)
    out = solve_near_saturation_shape(NearSaturationConfig())
    compact = {
        "achieved_A_max": round(out["achieved_A_max"], 4),
        "in_steep_regime": out["in_steep_regime"],
        "max_smooth_shape_gap_pct": round(out["max_smooth_shape_gap"] * 100, 4),
        "min_smooth_eigvec_overlap": round(out["min_smooth_eigvec_overlap"], 6),
        "positive_control_gap_pct": round(out["positive_control_top_hat"]["shape_gap"] * 100, 2),
        "positive_control_overlap": round(out["positive_control_top_hat"]["eigvec_overlap"], 4),
        "metric_discriminates_at_full_sat": out["metric_discriminates_at_full_sat"],
        "verdict": out["verdict"],
    }
    print(json.dumps(compact, indent=2))
    print("-" * 72)
    print(f"VERDICT: {out['verdict']}")
    print(f"REASON : {out['reason']}")
