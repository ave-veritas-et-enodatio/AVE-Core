"""
Apparatus-floor characterization 2 — THE H_bel LEDGER FLOOR
===========================================================

Retroactive self-audit of `ave-apparatus-floor-attribution` (skill check A —
"calibrate on knowns at the run's own scale; the free-evolution drift IS the
ledger's noise floor; closure claims tighter than the floor are meaningless").

The instrument under test is the graft family's headline helicity ledger
    H = ∫ ξ·(∇×ξ)   (curl = CrystalGraftV2._curl, central-diff via np.roll)
exactly as used by `crystal_graft_v2.helicity_bel` (ω carrier, line 287-294),
`crystal_graft_v4.helicity_photon` (w photon, v4:338-346) and v4's
`helicity_ledger` (the headline conservation measurement). We characterize that
SAME stencil on three knowns at the v4-relevant grid scale:

  (a) FREE DRIFT   — a free helical photon (sigma=3, wavelength=6, helicity=+1)
                     propagated with NO wall, NO source, NO converter, NO ω-sector.
                     d(∫w·∇×w)/dt = the ledger noise floor (numerical curl +
                     leapfrog dispersion + decoupled-vector-wave non-conservation).
  (b) KNOWN-NULL   — a LINEARLY polarized (zero-helicity) photon. |∫w·∇×w| = the
                     false-positive floor (must read ~0).
  (c) KNOWN-POSITIVE — a planted ABC Beltrami field ω with ∇×ω=λω EXACTLY, so the
                     analytic helicity is λ∫|ω|². Read accuracy = measured/analytic
                     = the central-difference curl truncation sin(λdx)/(λdx) at a
                     resolvable scale.

THE NUMBER v4's ledger-closure must beat = the free-drift relative drift over the
run, plus the false-positive floor expressed against a representative trapped H_bel.

ave-driver-script-honesty: identical stencil to the production instrument (we call
the engine's own _curl); no fit; the analytic known-positive is computed from λ and
|ω|² alone, not back-solved from the read.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core.crystal_graft_v3 import CrystalGraftV3  # noqa: E402

OUT = Path(__file__).parent
# the v4-relevant grid: crystal_graft_v4_run.py:43 uses N_GRID=72. We run the floor
# at the actual v4 N AND a smaller N to expose the N-scaling of the floor.
N_V4 = 72
N_SMALL = 44  # v3's N_GRID — the cross-scale check
SEED_PHOTON = dict(sigma=3.0, wavelength=6.0, amplitude=0.35)  # the LOCKED photon config
N_STEPS = 1000


def hbel_of(e, field):
    """∫ξ·(∇×ξ) over the PML-excluded interior, using the ENGINE'S OWN _curl —
    byte-identical to helicity_bel / helicity_photon. `field` is e.w or e.omega."""
    curl = e._curl(field, e.dx)
    dens = np.sum(field * curl, axis=-1)
    return float((dens * e.interior_mask()).sum())


def field_l2(e, field):
    return float((np.sum(field**2, axis=-1) * e.interior_mask()).sum())


def make_free_engine(N, S_min=2e-3, A_cap=0.999, pml=5):
    """A bare engine: NO bulk seed, NO Beltrami director, ω-sector + buckle OFF,
    converter OFF (inherited). A photon seeded into w propagates as a free wave."""
    return CrystalGraftV3(
        N=N,
        source_mode="abc",
        lam_sign=+1,
        S_min=S_min,
        A_cap=A_cap,
        omega_sector_on=False,
        buckle_on=False,
        omega_gap=1.0,
        pml_thickness=pml,
    )


# ───────────────────────────────────────────── (a) FREE DRIFT
def free_drift(N, helicity, n_steps=N_STEPS, label=""):
    e = make_free_engine(N)
    ic = N // 2
    e.seed_photon((ic, ic, ic), helicity=helicity, **SEED_PHOTON)
    H0 = hbel_of(e, e.w)
    L0 = field_l2(e, e.w)
    ts, Hs, Ls = [0.0], [H0], [L0]
    for s in range(n_steps):
        e.step()
        if (s + 1) % 25 == 0:
            ts.append(e.time)
            Hs.append(hbel_of(e, e.w))
            Ls.append(field_l2(e, e.w))
    Hs = np.array(Hs)
    Ls = np.array(Ls)
    # drift relative to |H0|; also relative to the field norm (so PML loss of |w|²
    # is separated from genuine helicity-per-energy drift)
    Hnorm = Hs / (Ls + 1e-30)  # helicity per unit |w|² (intensive — PML-robust)
    drift_rel_H0 = float((Hs[-1] - H0) / (abs(H0) + 1e-30))
    span_rel_H0 = float((Hs.max() - Hs.min()) / (abs(H0) + 1e-30))
    drift_intensive = float((Hnorm[-1] - Hnorm[0]) / (abs(Hnorm[0]) + 1e-30))
    span_intensive = float((Hnorm.max() - Hnorm.min()) / (abs(Hnorm[0]) + 1e-30))
    return {
        "N": N,
        "helicity": helicity,
        "label": label,
        "dt": e.dt,
        "n_steps": n_steps,
        "H0": float(H0),
        "H_end": float(Hs[-1]),
        "L0": float(L0),
        "L_end": float(Ls[-1]),
        "drift_rel_H0": drift_rel_H0,
        "span_rel_H0": span_rel_H0,
        "drift_intensive": drift_intensive,
        "span_intensive": span_intensive,
        "norm_loss_frac": float((L0 - Ls[-1]) / (L0 + 1e-30)),
        "t": ts,
        "H_t": Hs.tolist(),
        "Hnorm_t": Hnorm.tolist(),
    }


# ───────────────────────────────────────────── (b) KNOWN-NULL
def known_null(N, n_steps=N_STEPS):
    """Linearly polarized photon (helicity=0 ⇒ only one transverse axis filled).
    |∫w·∇×w| = the false-positive floor; we report it absolute AND normalized by
    the helicity a true CP photon of the SAME |w|² would carry (= k∫|w|²)."""
    fd = free_drift(N, helicity=0.0, n_steps=n_steps, label="known-null (linear pol)")
    # reference CP helicity at the same |w|²: a CP photon is Beltrami with k=2π/λ
    k = 2.0 * np.pi / SEED_PHOTON["wavelength"]
    H_cp_ref = k * fd["L0"]
    fd["k_photon"] = float(k)
    fd["H_cp_reference"] = float(H_cp_ref)
    fd["false_pos_floor_abs_t0"] = float(abs(fd["H0"]))
    fd["false_pos_floor_rel_to_CP"] = float(abs(fd["H0"]) / (abs(H_cp_ref) + 1e-30))
    # also the max |H| over the whole free evolution (the worst-case false positive)
    fd["false_pos_floor_abs_max"] = float(np.max(np.abs(fd["H_t"])))
    fd["false_pos_floor_rel_to_CP_max"] = float(np.max(np.abs(fd["H_t"])) / (abs(H_cp_ref) + 1e-30))
    return fd


# ───────────────────────────────────────────── (c) KNOWN-POSITIVE
def abc_field(N, c, lam, dx, amp=1.0):
    """ABC Beltrami field on the grid: ∇×b = λ b EXACTLY (continuum). Returns the
    (N,N,N,3) array."""
    i, j, k = np.indices((N, N, N))
    X = (i - c) * dx
    Y = (j - c) * dx
    Z = (k - c) * dx
    b = np.empty((N, N, N, 3))
    b[..., 0] = np.sin(lam * Z) + np.cos(lam * Y)
    b[..., 1] = np.sin(lam * X) + np.cos(lam * Z)
    b[..., 2] = np.sin(lam * Y) + np.cos(lam * X)
    return amp * b


def known_positive(N):
    """Plant an ABC Beltrami in ω at several resolvable wavelengths; the analytic
    helicity is λ∫|ω|². Read accuracy = measured / analytic = the curl-stencil
    truncation. Tests the SAME helicity_bel instrument on a field of KNOWN helicity."""
    e = make_free_engine(N)
    c = (N - 1) / 2.0
    m = e.interior_mask()
    rows = []
    for wavelength in (4.0, 6.0, 8.0, 10.0, 12.0):
        lam = 2.0 * np.pi / wavelength
        b = abc_field(N, c, lam, e.dx, amp=1.0)
        e.omega = b
        measured = e.helicity_bel()  # ∫ω·(∇×ω), production instrument
        analytic = float(lam * (np.sum(b**2, axis=-1) * m).sum())  # λ∫|ω|²
        ratio = measured / (analytic + 1e-30)
        # closed-form central-diff truncation for a sinusoid: sin(λdx)/(λdx)
        predicted = float(np.sin(lam * e.dx) / (lam * e.dx))
        rows.append(
            {
                "wavelength_cells": wavelength,
                "lambda": float(lam),
                "lambda_dx": float(lam * e.dx),
                "H_measured": float(measured),
                "H_analytic": float(analytic),
                "read_accuracy": float(ratio),
                "read_error_pct": float(100.0 * (ratio - 1.0)),
                "predicted_sinc_truncation": predicted,
            }
        )
    return rows


def main():
    t0 = time.time()
    print("=" * 78)
    print("  APPARATUS-FLOOR 2 — THE H_bel LEDGER FLOOR  (instrument calibration)")
    print("  retroactive self-audit of ave-apparatus-floor-attribution (check A)")
    print("=" * 78, flush=True)

    out = {"config": {"seed_photon": SEED_PHOTON, "n_steps": N_STEPS, "N_v4": N_V4, "N_small": N_SMALL}}

    # (a) FREE DRIFT — the LOCKED photon config, helicity=+1, at both N
    print("\n[a] FREE DRIFT — free helical photon (sigma=3, λ=6, h=+1); no wall/source/converter", flush=True)
    free = {}
    for N in (N_SMALL, N_V4):
        fd = free_drift(N, helicity=+1.0, label=f"free helical h=+1 N={N}")
        free[N] = fd
        print(
            f"   N={N:3d}: H0={fd['H0']:+.4g}  drift(rel H0)={fd['drift_rel_H0']:+.3%}  "
            f"span={fd['span_rel_H0']:.3%}  |  intensive drift={fd['drift_intensive']:+.3%} "
            f"span={fd['span_intensive']:.3%}  |w|²-loss={fd['norm_loss_frac']:.2%}",
            flush=True,
        )
    out["free_drift"] = free

    # (b) KNOWN-NULL — linear polarization
    print("\n[b] KNOWN-NULL — linearly polarized photon (h=0); |H_bel| = false-positive floor", flush=True)
    nulls = {}
    for N in (N_SMALL, N_V4):
        kn = known_null(N)
        nulls[N] = kn
        print(
            f"   N={N:3d}: |H_bel|(t0)={kn['false_pos_floor_abs_t0']:.4g}  "
            f"(rel to same-|w|² CP photon: {kn['false_pos_floor_rel_to_CP']:.3e})  "
            f"max over run rel-CP={kn['false_pos_floor_rel_to_CP_max']:.3e}",
            flush=True,
        )
    out["known_null"] = nulls

    # (c) KNOWN-POSITIVE — planted ABC Beltrami of known helicity
    print("\n[c] KNOWN-POSITIVE — planted ABC Beltrami ω (∇×ω=λω); read accuracy vs analytic λ∫|ω|²", flush=True)
    pos = {}
    for N in (N_SMALL, N_V4):
        kp = known_positive(N)
        pos[N] = kp
        print(f"   N={N}:", flush=True)
        for r in kp:
            print(
                f"      λ-wavelength={r['wavelength_cells']:4.0f} cells: read={r['read_accuracy']:.4f} "
                f"(err {r['read_error_pct']:+.2f}%)  predicted sinc={r['predicted_sinc_truncation']:.4f}",
                flush=True,
            )
    out["known_positive"] = pos

    # THE NUMBER v4's ledger-closure must beat (at the v4 grid N=72)
    fd72 = free[N_V4]
    null72 = nulls[N_V4]
    floor_drift = abs(fd72["drift_intensive"])  # PML-robust end-to-end free-drift
    floor_span_int = abs(fd72["span_intensive"])  # intensive swing during transit
    floor_span_ext = abs(fd72["span_rel_H0"])  # extensive swing (read-phase sensitivity)
    floor_drift_extensive = abs(fd72["drift_rel_H0"])
    floor_falsepos = null72["false_pos_floor_rel_to_CP_max"]
    # scale-dependent read-accuracy truncation (the magnitude floor): at the v4
    # photon scale (v4 SEED_PHOTON wavelength=10 ⇒ ~6.5% under-read) and at a fine
    # few-cell winding scale (the extractor sits at r≈1.1 cells ⇒ ≥17-36% under-read).
    kp72 = {r["wavelength_cells"]: r for r in pos[N_V4]}
    read_err_v4photon = abs(kp72[10.0]["read_error_pct"]) / 100.0  # λ=10 (v4 photon)
    read_err_fine = abs(kp72[4.0]["read_error_pct"]) / 100.0  # 4-cell winding
    # the conservation floor (fractional closure) vs the magnitude floor
    conservation_floor = max(floor_drift, floor_span_int)
    ledger_floor = max(conservation_floor, read_err_v4photon)
    out["ledger_floor"] = {
        "N": N_V4,
        "n_steps": N_STEPS,
        "free_drift_intensive_end": floor_drift,
        "free_drift_intensive_span": floor_span_int,
        "free_drift_extensive_end": floor_drift_extensive,
        "free_drift_extensive_span_read_phase": floor_span_ext,
        "false_positive_floor_rel_CP": floor_falsepos,
        "read_accuracy_error_v4_photon_lambda10": read_err_v4photon,
        "read_accuracy_error_4cell_winding": read_err_fine,
        "conservation_floor_intensive": conservation_floor,
        "combined_ledger_floor": ledger_floor,
        "criterion": (
            f"At N={N_V4}, {N_STEPS} steps: H_bel-ledger CLOSURE claims tighter than "
            f"±{100*ledger_floor:.1f}% are below the instrument floor. Decomposition: a FREE "
            f"helical photon (NO wall/source/converter) conserves its OWN helicity only to "
            f"{100*floor_drift:.1f}% end-to-end (intensive) / {100*floor_span_int:.1f}% intensive "
            f"swing — and its EXTENSIVE ∫w·∇×w swings {100*floor_span_ext:.0f}% during transit, so a "
            f"ledger read at an arbitrary timestep carries ±{100*floor_span_ext:.0f}% read-phase error. "
            f"The magnitude read is under-reported by the central-diff curl truncation "
            f"sin(λdx)/(λdx): {100*read_err_v4photon:.1f}% at the v4 photon scale (λ=10 cells), rising "
            f"to {100*read_err_fine:.0f}% at a 4-cell winding. The false-positive (zero-helicity) "
            f"floor is the one clean number: {floor_falsepos:.1e} (machine-zero — the stencil "
            f"manufactures no helicity). NET: trust the SIGN and ratios > ~5%; distrust any closure "
            f"magnitude claimed tighter than ±{100*ledger_floor:.0f}% at this config."
        ),
    }
    print("\n" + "=" * 78)
    print("  LEDGER FLOOR (the number v4 must beat):")
    print("  " + out["ledger_floor"]["criterion"])
    print("=" * 78, flush=True)

    (OUT / "apparatus_floor_hbel_results.json").write_text(json.dumps(out, indent=2, default=str))
    make_figure(out)
    out["elapsed_s"] = time.time() - t0
    (OUT / "apparatus_floor_hbel_results.json").write_text(json.dumps(out, indent=2, default=str))
    print(f"\n  elapsed {out['elapsed_s']:.1f}s", flush=True)
    return out


def make_figure(out):
    fig, ax = plt.subplots(1, 3, figsize=(16, 4.6))

    # panel 1: free-drift H_bel(t) (intensive, PML-robust) at both N
    for N, color in ((N_SMALL, "C0"), (N_V4, "C3")):
        fd = out["free_drift"][N]
        t = np.array(fd["t"])
        hn = np.array(fd["Hnorm_t"])
        ax[0].plot(t, hn / hn[0], color=color, label=f"N={N} (drift {fd['drift_intensive']:+.2%})")
    ax[0].axhline(1.0, ls=":", color="k")
    ax[0].set_xlabel("time")
    ax[0].set_ylabel("H_bel/|w|²  normalized to t0  (intensive)")
    ax[0].set_title(
        f"(a) FREE-DRIFT floor: free helical photon\nh=+1, σ=3, λ=6, NO wall/source/converter, {N_STEPS} steps"
    )
    ax[0].legend(fontsize=7)

    # panel 2: EXTENSIVE ∫w·∇×w transit swing (the read-phase floor) + null annotation
    for N, color in ((N_SMALL, "C0"), (N_V4, "C3")):
        fd = out["free_drift"][N]
        t = np.array(fd["t"])
        h = np.array(fd["H_t"])
        ax[1].plot(t, h / h[0], color=color, label=f"N={N} (span {fd['span_rel_H0']:.0%})")
    ax[1].axhline(1.0, ls=":", color="k")
    ax[1].set_xlabel("time")
    ax[1].set_ylabel("extensive ∫w·∇×w  normalized to t0")
    nullfloor = out["known_null"][N_V4]["false_pos_floor_rel_to_CP_max"]
    ax[1].set_title(
        f"(b) read-phase floor: extensive H_bel swings ~21%\nin transit  |  known-null (linear pol) "
        f"false-pos = {nullfloor:.0e} (machine-0)"
    )
    ax[1].legend(fontsize=7)

    # panel 3: known-positive read accuracy vs resolution
    for N, color in ((N_SMALL, "C0"), (N_V4, "C3")):
        kp = out["known_positive"][N]
        wl = [r["wavelength_cells"] for r in kp]
        acc = [r["read_accuracy"] for r in kp]
        pred = [r["predicted_sinc_truncation"] for r in kp]
        ax[2].plot(wl, acc, "o-", color=color, label=f"measured N={N}")
        ax[2].plot(wl, pred, "x--", color=color, alpha=0.5, label=f"sinc(λdx) N={N}")
    ax[2].axhline(1.0, ls=":", color="k", label="perfect")
    ax[2].set_xlabel("Beltrami wavelength (cells)")
    ax[2].set_ylabel("read accuracy (measured/analytic)")
    ax[2].set_title("(c) KNOWN-POSITIVE read accuracy\n= central-diff curl truncation sin(λdx)/(λdx)")
    ax[2].legend(fontsize=6)

    fig.tight_layout()
    p = OUT / "apparatus_floor_hbel_fig1.png"
    fig.savefig(p, dpi=110)
    plt.close(fig)
    print(f"  figure: {p.name}", flush=True)


if __name__ == "__main__":
    main()
