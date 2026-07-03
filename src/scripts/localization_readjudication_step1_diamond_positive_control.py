"""STEP 1 — NATIVE-DIAMOND POSITIVE CONTROL.

Prereg : research/2026-07-03_localization-readjudication_prereg.md §4.

THE MAKE-OR-BREAK FOR THE DIAMOND INSTRUMENT. Construct a configuration KNOWN to
bind on the diamond TETRA stencil and push it through the ORIGINAL Stage-2/S3
`classify()` pipeline UNMODIFIED. Which bin does it read?

  * reads MODE_I_PERSIST → the instrument CAN see a trap; the original DISPERSE
    verdicts (#403/#404) regain PARTIAL standing (the readout is live, at least
    for this input). Report honestly.
  * after a genuine attempt at ALL THREE routes NO config reads PERSIST → the
    native readout cannot register bound for ANY input → [INSTRUMENT-DEAD] for
    the diamond carrier. Decisive.

CRITICAL: this driver IMPORTS `classify` and `run_native_imex` VERBATIM from the
original make-or-break driver — it NEVER redefines the adjudication. The IDENTICAL
pipeline (same solve, same bins, same thresholds) is the requirement (Step 3.8a).

Every config's nullspace-energy fraction (§5 diagnostic) is reported BEFORE its
verdict is read (Step 3.8: a purely-nullspace 'PERSIST' is DISQUALIFIED as a
bookkeeping-frozen artifact, NOT a bound state — the prereg §4.1 guard).

α-clean. NO ALPHA / Q_TANK / 137 anywhere (imports the α-free operator only).
"""

import json

import numpy as np

from ave.solvers.native_cage_imex import (  # noqa: E402
    NativeCageIMEX,
    NativeCageIMEXConfig,
    assemble_L_D,
    build_grad_div_periodic,
)

# ── the IDENTICAL pipeline, imported VERBATIM (never redefined) ──
# The original Stage-2 make-or-break driver IS a package module (src/scripts is a
# package). classify() + run_native_imex() are imported as-is — the IDENTICAL
# adjudication (same solve, same bins, same thresholds), never redefined here.
from scripts.engine_stage2_native_cage_imex_makeorbreak import (  # noqa: E402
    DX,
    N_STEPS_TOTAL,
    N_STEPS_TRANSIENT,
    SEED_AMP,
    SEED_RADIUS,
    classify,
    run_native_imex,
)

# NOTE: the §5 nullspace-fraction diagnostic (spectral_liveness) is used VERBATIM
# in the tractable-N tests (test_spectral_liveness.py) and in the srs re-run
# (step 3, where n_nodes is small enough for dense eigh). At the diamond's full
# N=24 (1.3e4 DOF) a dense eigh is intractable, so `_nullspace_fraction_N24`
# below computes the SAME quantity (energy fraction in |λ|<tol) via the sparse
# shift-invert near-nullspace — the identical diagnostic, scaled for the heavy
# operator. The frozen kernel is small (16-dim), so σ=0 shift-invert grabs it
# exactly.

N = 24  # v14 canonical (matches the original make-or-break)


def _diamond_L_D(n):
    Grad, Div = build_grad_div_periodic(n)
    return assemble_L_D(Grad, Div, np.ones(n**3))


def _nullspace_fraction_N24(seed_field):
    """The seed's TRUE dead-leg fraction at the FULL N=24 dynamics operator, via
    the sparse near-nullspace (dense eig at 1.3e4 DOF is heavy; the frozen kernel
    is small so shift-invert at σ=0 grabs it exactly). This is the §5 liveness
    number read BEFORE the verdict (Step 3.8a), on the operator the dynamics use."""
    from scipy.sparse.linalg import eigsh
    L = _diamond_L_D(N)
    w, V = eigsh(L, k=64, sigma=0.0, which="LM")
    nmask = np.abs(w) < 1e-8
    s = seed_field.reshape(-1)
    s = s / max(np.linalg.norm(s), 1e-30)
    null_frac = float(np.sum((V[:, nmask].T @ s) ** 2))
    return null_frac, int(nmask.sum())


def _run_seed_through_pipeline(seed_field, *, label):
    """Push an arbitrary at-rest seed through the IDENTICAL native IMEX +
    classify() pipeline. Returns the verdict, bins, and the reactance history —
    plus the §5 nullspace fraction read BEFORE the verdict (Step 3.8)."""
    # nullspace-fraction diagnostic FIRST (liveness before verdict), on the FULL
    # N=24 dynamics operator (the seed's TRUE dead-leg).
    null_frac, null_dim = _nullspace_fraction_N24(seed_field)
    live_frac = 1.0 - null_frac

    # DYNAMICS: full N=24 native IMEX, IDENTICAL config the original driver used.
    cfg = NativeCageIMEXConfig(N=N, dx=DX, port_sigma=0.03)
    eng = NativeCageIMEX(cfg)
    eng.seed_field(seed_field)
    eng.set_dt_accuracy()
    eng.dt = 0.066  # PROD_DT (the original driver's production dt)
    res = eng.run_record(N_STEPS_TOTAL, N_STEPS_TRANSIENT)
    res["dt_info"] = {"dt": 0.066}
    res["N"] = N
    res["max_strain_over_run"] = float(min(res["max_abs_over_run"] / 1.0, 1.0))

    # the matched Gaussian control (the original driver's radiation floor).
    gauss = run_native_imex(N, profile="gaussian")
    verdict, bins, gauss_disperses, gauss_late = classify(res, gauss)

    return {
        "label": label,
        "nullspace_fraction_N24": null_frac,
        "live_fraction_N24": live_frac,
        "nullspace_dim_N24": null_dim,
        "verdict": verdict,
        "bins": {k: bool(v) for k, v in bins.items()},
        "v_peak_mean_post": res["v_peak_mean_post"],
        "v_peak_std_over_mean_post": res["v_peak_std_over_mean_post"],
        "max_abs_over_run": res["max_abs_over_run"],
        # STEP 3.8 DISQUALIFIER: a 'PERSIST' with ~all-nullspace live fraction is
        # a bookkeeping-frozen artifact, NOT a bound state.
        "persist_is_frozen_artifact": bool(
            verdict == "MODE_I_PERSIST" and live_frac < 0.10
        ),
    }


# ─────────────────────────────────────────────────────────────────────────────
# THE THREE CANDIDATE ROUTES (prereg §4)
# ─────────────────────────────────────────────────────────────────────────────
def route1_low_lambda_localized_eigenmode():
    """ROUTE 1 — an explicit LOW-nonzero-λ localized eigenmode of L_D (the
    operator's own bound-like mode). Built at N=24 directly (sparse eig)."""
    # sparse: get the smallest nonzero eigenpairs of L_D at N=24.
    from scipy.sparse.linalg import eigsh
    L = _diamond_L_D(N)
    # shift-invert near a small positive value to grab low-λ modes; ask for many
    # and pick the most localized nonzero one.
    try:
        w, V = eigsh(L, k=40, sigma=1e-4, which="LM")
    except Exception:
        w, V = eigsh(L, k=40, which="SM")
    nonzero = np.abs(w) > 1e-8
    if not np.any(nonzero):
        return None, {"route1_note": "no nonzero low-λ modes found"}
    idxs = np.where(nonzero)[0]
    best = None
    for j in idxs:
        u = V[:, j]
        p = u**2
        pr = 1.0 / float(np.sum(p**2))
        frac = pr / (N**3)
        if best is None or frac < best[2]:
            best = (u, float(w[j]), frac)
    u, lam, frac = best
    seed = (SEED_AMP * u / np.max(np.abs(u))).reshape(N, N, N)
    return seed, {"route1_lambda": lam, "route1_participation_frac": frac}


def route2_single_sublattice_localized():
    """ROUTE 2 — an analytically bound state on ONE parity sublattice (respecting
    the decoupling). A centred sech, then ZERO out the odd-parity sublattice — the
    seed lives only on the even sublattice L_D actually couples within."""
    c = N // 2
    coords = np.arange(N) - c
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * DX
    seed = SEED_AMP / np.cosh(r / SEED_RADIUS)
    i, j, k = np.indices((N, N, N))
    even = (i + j + k) % 2 == 0
    seed = np.where(even, seed, 0.0)
    return seed, {"route2_note": "even-sublattice-only sech"}


def route3_nullspace_orthogonal():
    """ROUTE 3 — the v14 sech PROJECTED OUT of the L_D nullspace: evolve only the
    ~6.5% live part (the operator-governed complement). Uses the §5 helper.
    Built/projected at N=12 then re-embedded — but the honest route projects at
    the FULL N=24 (dense eig at 1.3e4 DOF is heavy but the frozen kernel is small,
    so we project via the sparse near-nullspace)."""
    from scipy.sparse.linalg import eigsh
    c = N // 2
    coords = np.arange(N) - c
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * DX
    sech = (SEED_AMP / np.cosh(r / SEED_RADIUS)).reshape(-1)
    L = _diamond_L_D(N)
    # grab the near-nullspace (smallest-magnitude eigenpairs) and project it out.
    w, V = eigsh(L, k=64, sigma=0.0, which="LM")
    null_mask = np.abs(w) < 1e-8
    Vn = V[:, null_mask]
    sech_live = sech - Vn @ (Vn.T @ sech)
    # renormalize to the original peak so the amplitude is comparable.
    if np.max(np.abs(sech_live)) > 1e-12:
        sech_live = sech_live * (SEED_AMP / np.max(np.abs(sech_live)))
    return sech_live.reshape(N, N, N), {
        "route3_null_modes_removed": int(null_mask.sum()),
        "route3_note": "v14 sech projected out of L_D near-nullspace",
    }


def main():
    out = {
        "prereg": "research/2026-07-03_localization-readjudication_prereg.md",
        "step": "1 — native-diamond positive control",
        "pipeline": "IDENTICAL classify()+run_native_imex imported verbatim",
        "N": N,
    }
    routes = {}

    for name, builder in (
        ("route1_low_lambda_localized_eigenmode", route1_low_lambda_localized_eigenmode),
        ("route2_single_sublattice_localized", route2_single_sublattice_localized),
        ("route3_nullspace_orthogonal", route3_nullspace_orthogonal),
    ):
        seed, meta = builder()
        if seed is None:
            routes[name] = {"constructed": False, **meta}
            continue
        res = _run_seed_through_pipeline(seed, label=name)
        routes[name] = {"constructed": True, **meta, **res}

    out["routes"] = routes

    # ── VERDICT for step 1 ──
    persist_routes = [
        r for r, d in routes.items()
        if d.get("constructed") and d.get("verdict") == "MODE_I_PERSIST"
        and not d.get("persist_is_frozen_artifact", False)
    ]
    frozen_only = [
        r for r, d in routes.items()
        if d.get("constructed") and d.get("persist_is_frozen_artifact", False)
    ]
    if persist_routes:
        out["STEP1_VERDICT"] = "INSTRUMENT_CAN_SEE_TRAP"
        out["STEP1_REASON"] = (
            f"routes {persist_routes} read MODE_I_PERSIST with a GENUINE live "
            "fraction (not a frozen-nullspace artifact) → the diamond readout CAN "
            "register bound; the original DISPERSE verdicts regain partial standing."
        )
    else:
        out["STEP1_VERDICT"] = "DIAMOND_INSTRUMENT_DEAD"
        out["STEP1_REASON"] = (
            "after a genuine attempt at all three routes, NO configuration reads "
            "MODE_I_PERSIST with a genuine live fraction. "
            + (f"(routes {frozen_only} read PERSIST but were DISQUALIFIED as "
               "bookkeeping-frozen nullspace artifacts, live-fraction<0.10.) "
               if frozen_only else "")
            + "The native TETRA readout cannot register bound for any input → "
            "[INSTRUMENT-DEAD] for the diamond carrier."
        )

    print(json.dumps(out, indent=2, default=float))
    return out


if __name__ == "__main__":
    main()
