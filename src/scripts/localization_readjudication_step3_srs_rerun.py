"""STEP 3 — THE srs-z3 RE-RUN (the physics reading).

Prereg : research/2026-07-03_localization-readjudication_prereg.md §6.

Port the Stage-2 bulk-self-trap test to the CHIRAL srs z=3 carrier — the Axiom-1
canonical lattice. Rule-14: ADAPT the certified core (ave.solvers.srs_cage_winding
SrsCageWinding, A1-only mode), do NOT rebuild. The srs-native graph Laplacian
L_srs = Bᵀ·diag(D_bond)·B is canon-derived and has nullspace dim 1 (constant mode
only) — NOT the diamond's 8-16 dim frozen kernel (verified §6.1).

CANON-DERIVED PARAMETERIZATION (no tuning-to-match-diamond):
  * operator      : L_srs (srs_cage_winding.assemble_L_srs) on build_srs_net z=3.
  * saturation    : S(A)=(1−A²)^0.5, D=1/S (graded_vacuum_network, α-free Op14).
  * bond geometry : the srs builder (z=3, girth-10, I4₁32).
ENGINEERING-CHOICE (tagged, prereg §6.2): dt (accuracy-set), L (box size, robust),
seed width (matched to v14 in the shared cube-frame).

THE CLOSED-BOX LOCALIZATION METRIC (KEEP-BOTH, prereg §6.4):
  The srs supercell is FULLY PERIODIC (no PML/absorbing boundary; interior_mask =
  all nodes). The diamond driver's "interior peak" observable (PML-excluded cube
  interior) has NO analog here. So we ADD a closed-system localization metric
  ALONGSIDE the legacy peak: the PARTICIPATION NUMBER PN = 1/Σpᵢ² (pᵢ = energy
  fraction at node i). PN SMALL = localized (energy on few nodes); PN LARGE =
  dispersed (energy spread over the box). This is LOCAL (per-node), satisfying the
  structural-degeneracy guard (NOT a global sum that telescopes to zero). The
  legacy peak-persistence is also reported.

Every seed's nullspace-fraction (§5 diagnostic) is reported BEFORE its verdict.
The srs POSITIVE CONTROL (a localized L_srs eigenmode) is pushed through the
IDENTICAL srs classify FIRST (readout-liveness, Step 3.8a).

α-clean. NO ALPHA / Q_TANK / V_SNAP on any path (imports the α-free carrier only).
"""

import json

import numpy as np

from ave.core.chiral_lattice import build_srs_net
from ave.solvers.graded_vacuum_network import saturation_kernel
from ave.solvers.spectral_liveness import spectral_liveness
from ave.solvers.srs_cage_winding import (
    SrsCageWinding,
    SrsCageWindingConfig,
    assemble_L_srs,
    build_incidence,
)

# ── frozen window (mirrors the diamond driver's v14 window) ──
N_STEPS_TOTAL = 600
N_STEPS_TRANSIENT = 200
SEED_AMP = 0.85
SEED_RADIUS = 2.5  # cube-frame cells (matched to v14 in the shared frame_N)
PROD_DT = 0.066    # ENGINEERING-CHOICE: accuracy-set (CN unconditionally stable)

# legacy Stage-2 §8a bin thresholds (KEEP-BOTH: applied where they still apply).
BIN_PEAK_MIN = 0.2       # I-1
BIN_BREATHE_MIN = 0.05   # I-2
BIN_DIVERGE_MAX = 0.5    # I-3
BIN_NEM_MAX = 0.97       # I-4
BIN_MAXABS = 10.0        # I-6


def _participation_number(field: np.ndarray) -> float:
    """PN = 1/Σpᵢ² with pᵢ = |field_i|²/Σ|field|² — the closed-box localization
    metric (# nodes carrying the energy). SMALL = localized, LARGE = dispersed."""
    e = np.abs(field) ** 2
    tot = float(e.sum())
    if tot < 1e-30:
        return 0.0
    p = e / tot
    return float(1.0 / np.sum(p ** 2))


def _srs_L_cold(L):
    net = build_srs_net(L=L, enantiomorph="right")
    B, bonds = build_incidence(net)
    return assemble_L_srs(B, bonds, np.ones(net.n_nodes)), net, B, bonds


def _run_srs(cfg: SrsCageWindingConfig, seed_field, *, label,
             n_total=N_STEPS_TOTAL, n_transient=N_STEPS_TRANSIENT):
    """Evolve an A1-only srs core; record peak, participation-number, energy, and
    the saturation gauge every step. A1-only (winding_on=False) — the bulk
    self-trap question is A1-sector (mass=A1 scope-lock; ω not evolved here)."""
    eng = SrsCageWinding(cfg)
    eng.winding_on = False
    eng.seed_A1_field(seed_field)
    eng.dt = PROD_DT

    # nullspace fraction FIRST (liveness before verdict, §5 / Step 3.8a).
    L_cold, net, _, _ = _srs_L_cold(cfg.L)
    live = spectral_liveness(np.abs(seed_field), L_cold)

    H0 = eng.a1_energy()
    peak_hist, pn_hist, energy_hist, nem_hist, maxabs_hist = [], [], [], [], []
    for _ in range(n_total):
        eng.step()
        a = np.abs(eng.a_A1)
        peak_hist.append(float(a.max()))
        pn_hist.append(_participation_number(eng.a_A1))
        energy_hist.append(eng.a1_energy())
        # saturation gauge n_EM = √S(A) (min over nodes — is saturation engaged?)
        A = np.minimum(a / cfg.V_yield, cfg.A_cap)
        S = saturation_kernel(A, exponent=cfg.exponent, S_min=cfg.S_min)
        nem_hist.append(float(np.sqrt(S).min()))
        maxabs_hist.append(float(a.max()))
    peak = np.array(peak_hist)
    pn = np.array(pn_hist)
    post = peak[n_transient:]
    pn_post = pn[n_transient:]
    H1 = eng.a1_energy()
    return {
        "label": label,
        "n_nodes": net.n_nodes,
        "nullspace_fraction": live.nullspace_energy_fraction,
        "live_fraction": live.live_energy_fraction,
        "nullspace_dim": live.nullspace_dim,
        # legacy peak-persistence observables (KEEP-BOTH):
        "peak0": float(peak[0]),
        "v_peak_mean_post": float(post.mean()),
        "v_peak_std_over_mean_post": float(post.std() / max(post.mean(), 1e-9)),
        "n_em_min_over_window": float(np.min(nem_hist)),
        "max_abs_over_run": float(np.max(maxabs_hist)),
        # closed-box localization metric (the ADDED srs-native bin):
        "participation_number_0": float(pn[0]),
        "participation_number_post_mean": float(pn_post.mean()),
        "participation_ratio_grew": float(pn_post.mean() / max(pn[0], 1e-9)),
        # rigor guard: A1-energy conservation (unitary Cayley ⇒ no damping fakes a pin)
        "a1_energy_rel_drift": float(abs(H1 - H0) / max(H0, 1e-30)),
    }


def classify_srs(res, radiation_floor_pn):
    """FROZEN Stage-2 §8a bins where they apply (KEEP-BOTH) + the ADDED srs-native
    closed-box localization bin. Returns (legacy_verdict, srs_verdict, bins).

    Legacy peak bins (I-1..I-6): applied verbatim on the srs peak history. The
    I-5 'above radiation floor' compares the srs core's LOCALIZATION against a
    delocalized null control's participation number (the srs-native radiation
    floor — a dispersed field has PN ≈ n_nodes).

    ADDED srs-native LOCALIZATION bin (LOC): the core is LOCALIZED iff its post-
    transient participation number stays a SMALL fraction of the box AND did not
    grow toward the delocalized floor. This is the closed-box analog of the
    diamond's 'interior peak persists' — LOCAL (per-node), degeneracy-safe."""
    mean_post = res["v_peak_mean_post"]
    som = res["v_peak_std_over_mean_post"]
    nem = res["n_em_min_over_window"]
    maxabs = res["max_abs_over_run"]
    pn_post = res["participation_number_post_mean"]
    n_nodes = res["n_nodes"]

    legacy_bins = {
        "I-1 mean V_peak > 0.2": mean_post > BIN_PEAK_MIN,
        "I-2 breathing std/mean > 0.05": som > BIN_BREATHE_MIN,
        "I-3 not diverging std/mean < 0.5": som < BIN_DIVERGE_MAX,
        "I-4 saturation engaged n_EM < 0.97": nem < BIN_NEM_MAX,
        "I-6 bounded max|V| < 10": maxabs < BIN_MAXABS,
    }
    legacy_verdict = "MODE_I_PERSIST" if all(legacy_bins.values()) else "MODE_III_DISPERSE"

    # ADDED srs-native localization bin (the closed-box analog):
    localized_frac = pn_post / max(n_nodes, 1)
    grew_toward_floor = pn_post > 0.5 * radiation_floor_pn  # spread ≥ half the delocalized floor
    loc_bins = {
        "LOC-1 stays localized (PN_post < 25% of box)": localized_frac < 0.25,
        "LOC-2 did not disperse to floor (PN_post < 50% of delocalized PN)": not grew_toward_floor,
        "LOC-3 bounded (max|V| < 10)": maxabs < BIN_MAXABS,
    }
    srs_verdict = "LOCALIZED_PERSIST" if all(loc_bins.values()) else "DISPERSED"

    return legacy_verdict, srs_verdict, {**legacy_bins, **loc_bins}


# ─────────────────────────────────────────────────────────────────────────────
# SEEDS (prereg §6.3) — every one gets its §5 nullspace-fraction BEFORE verdict
# ─────────────────────────────────────────────────────────────────────────────
def seed_smooth_core(cfg):
    """(1) the equivalent smooth core (v14 sech re-homed onto srs nodes)."""
    eng = SrsCageWinding(cfg)
    eng.seed_A1_sech(amplitude=SEED_AMP, radius=SEED_RADIUS)
    return np.real(eng.a_A1).copy()


def seed_srs_positive_control(cfg):
    """(2) the srs POSITIVE CONTROL — the most-localized nonzero L_srs eigenmode
    (constructed the SAME way as the diamond route-1 positive control). KNOWN to
    stay localized (it is an operator eigenmode ⇒ oscillates in place, does not
    disperse under energy-conserving CN). Expected reading: LOCALIZED_PERSIST."""
    L_cold, net, _, _ = _srs_L_cold(cfg.L)
    Ls = L_cold.toarray()
    w, V = np.linalg.eigh(Ls)
    best = None
    for j in range(net.n_nodes):
        if abs(w[j]) < 1e-9:
            continue
        u = V[:, j]
        pn = 1.0 / float(np.sum((u ** 2) ** 2))
        if best is None or pn < best[1]:
            best = (j, pn)
    j = best[0]
    u = V[:, j]
    return (SEED_AMP * u / np.max(np.abs(u))).astype(float), float(w[j])


def seed_delocalized_null(cfg):
    """(3a) delocalized null control — a broad random field (NOT a localized core).
    Its post participation number is the srs-native RADIATION FLOOR (a dispersed
    field spreads over the whole box). Should read DISPERSED."""
    L_cold, net, _, _ = _srs_L_cold(cfg.L)
    rng = np.random.default_rng(0)
    f = rng.standard_normal(net.n_nodes)
    return (SEED_AMP * f / np.max(np.abs(f))).astype(float)


def seed_constant_mode_null(cfg):
    """(3b) the constant mode (srs nullspace) — the degenerate frozen case. Should
    read as the DISQUALIFIED bookkeeping case (uniform field, PN = n_nodes)."""
    L_cold, net, _, _ = _srs_L_cold(cfg.L)
    return (SEED_AMP * np.ones(net.n_nodes)).astype(float)


def main():
    out = {
        "prereg": "research/2026-07-03_localization-readjudication_prereg.md",
        "step": "3 — srs-z3 re-run (the physics reading)",
        "carrier": "chiral srs z=3 (Axiom-1 canonical); A1-only (mass=A1 scope-lock)",
        "operator": "L_srs = Bᵀ·diag(D_bond)·B (canon srs_cage_winding, nullspace dim 1)",
        "scheme": "Crank–Nicolson/Cayley unitary (energy-conserving; no damping fakes a pin)",
        "engineering_choices": {
            "dt": f"{PROD_DT} (accuracy-set; CN unconditionally stable)",
            "L": "L∈{4,6} robustness (finite-size cross-check)",
            "seed_width": f"radius={SEED_RADIUS} cube-frame cells (matched to v14)",
        },
        "localization_metric": (
            "closed-box participation number PN=1/Σpᵢ² (LOCAL, degeneracy-safe); "
            "legacy peak-persistence reported alongside (KEEP-BOTH)"
        ),
    }
    results = {}
    for L in (4, 6):
        cfg = SrsCageWindingConfig(L=L, winding_on=False)

        # radiation floor (delocalized null) FIRST — sets the srs-native floor.
        deloc_seed = seed_delocalized_null(cfg)
        deloc = _run_srs(cfg, deloc_seed, label=f"delocalized_null_L{L}")
        floor_pn = deloc["participation_number_post_mean"]

        # POSITIVE CONTROL — pushed through the IDENTICAL classify FIRST (Step 3.8a).
        pc_seed, pc_lambda = seed_srs_positive_control(cfg)
        pc = _run_srs(cfg, pc_seed, label=f"positive_control_eigenmode_L{L}")
        pc["eigenmode_lambda"] = pc_lambda
        pc_legacy, pc_srs, pc_bins = classify_srs(pc, floor_pn)
        pc["legacy_verdict"] = pc_legacy
        pc["srs_verdict"] = pc_srs
        pc["bins"] = {k: bool(v) for k, v in pc_bins.items()}
        pc["readout_live"] = bool(pc_srs == "LOCALIZED_PERSIST")

        # the SMOOTH CORE (the primary test seed) — verdict read only AFTER the
        # positive control certified the readout live.
        core_seed = seed_smooth_core(cfg)
        core = _run_srs(cfg, core_seed, label=f"smooth_core_L{L}")
        core_legacy, core_srs, core_bins = classify_srs(core, floor_pn)
        core["legacy_verdict"] = core_legacy
        core["srs_verdict"] = core_srs
        core["bins"] = {k: bool(v) for k, v in core_bins.items()}

        # constant-mode null (the degenerate frozen case, DISQUALIFIED reference).
        const_seed = seed_constant_mode_null(cfg)
        const = _run_srs(cfg, const_seed, label=f"constant_mode_null_L{L}")
        const_legacy, const_srs, const_bins = classify_srs(const, floor_pn)
        const["srs_verdict"] = const_srs

        # the delocalized null's own srs verdict (should be DISPERSED — it IS the floor).
        deloc_legacy, deloc_srs, _ = classify_srs(deloc, floor_pn)

        results[f"L{L}"] = {
            "radiation_floor_pn": floor_pn,
            "positive_control": pc,
            "smooth_core": core,
            "delocalized_null": {
                "srs_verdict": deloc_srs,
                "participation_number_post_mean": floor_pn,
                "participation_number_0": deloc["participation_number_0"],
            },
            "constant_mode_null": {
                "srs_verdict": const_srs,
                "participation_number_post_mean": const["participation_number_post_mean"],
            },
        }
    out["results"] = results

    # ── STEP-3 VERDICT (open-goal; the physics reading) ──
    # readout-liveness gate: the positive control MUST read LOCALIZED_PERSIST.
    Lkeys = list(results.keys())
    live_L = [L for L in Lkeys if results[L]["positive_control"]["readout_live"]]
    core_verdicts = {L: results[L]["smooth_core"]["srs_verdict"] for L in Lkeys}
    if not live_L:
        out["STEP3_VERDICT"] = "SRS_INSTRUMENT_DEAD"
        out["STEP3_REASON"] = (
            "the srs positive-control eigenmode did NOT read LOCALIZED_PERSIST at "
            "any L — the srs readout could not register bound for a known-bound "
            "input. No physics verdict on the smooth core (→ [INSTRUMENT-DEAD])."
        )
    elif all(v == "DISPERSED" for v in core_verdicts.values()):
        out["STEP3_VERDICT"] = "DISPERSES_ON_SRS_LIVE"
        out["STEP3_REASON"] = (
            f"the srs readout is PROVEN LIVE (positive control reads "
            f"LOCALIZED_PERSIST at L={live_L}), and the smooth A1 core DISPERSES "
            f"at every L ({core_verdicts}). The bulk self-trap falsification "
            "RE-BOOKS with solid evidence on the Axiom-1 canonical carrier; the "
            "boundary/topological reroute (#403/#404) stands, now grounded."
        )
    elif all(v == "LOCALIZED_PERSIST" for v in core_verdicts.values()):
        out["STEP3_VERDICT"] = "BINDS_ON_SRS"
        out["STEP3_REASON"] = (
            f"the srs readout is PROVEN LIVE, and the smooth A1 core PERSISTS "
            f"localized at every L ({core_verdicts}). MEDIUM-scaffold finding — "
            "requires its OWN adversarial panel before ANY canon change (the "
            "seduction-trap is named in the prereg §1.1; this does NOT by itself "
            "revert #403/#404)."
        )
    else:
        out["STEP3_VERDICT"] = "L_DEPENDENT_SURFACE_TO_GRANT"
        out["STEP3_REASON"] = (
            f"the smooth-core verdict is L-dependent ({core_verdicts}) — a finite-"
            "size framing fork. Surface to Grant (trigger 8/9); do NOT self-resolve."
        )

    print(json.dumps(out, indent=2, default=float))
    return out


if __name__ == "__main__":
    main()
