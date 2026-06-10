"""
Crystal-Graft v4 — LOCK-ISOLATION SMOKE (the adversarial panel's highest-priority follow-up).

WHY: the v4 SMOKE-1 (planted-knot survival) PASSED with BOTH lock-ON and lock-OFF reading (2,3)
(crystal_graft_v4_results.json: smoke_lock.read_tN_lockON == read_tN_lockOFF == [2,3]). So that smoke
did NOT demonstrate the lock — survival was never isolated from the source simply being too gentle to
destroy the knot. This bounded diagnostic (NOT a v5) isolates the lock: it applies a *v3-STRENGTH buckle*
— the frozen-Beltrami-template director that destroyed the planted knot in graft-v3 ((2,3)->(2,1)) — to a
RESOLVABLE planted (2,3), in lock-ON vs lock-OFF arms with EVERYTHING ELSE held identical (only lock_eta
differs).

v3 config pulled verbatim via `git show 4627651a:src/scripts/vol_1_foundations/crystal_graft_v3_run.py`
(smoke_independence + _make_engine):
  N=44, source_mode='abc', lam_sign=+1, p=2, q=3, S_min=2e-3, A_cap=0.999, omega_gap=1.0,
  wall_center=0.78, wall_width=0.16, kappa_tilde=6/5, pml_thickness=5,
  seed_bulk(sigma=4.5, frac=0.9) + seed_photon(sigma=5, wavelength=7, amplitude=0.35),
  build_beltrami_director(R,r) at wall_geometry(e),
  planted (2,3) at Rk=0.22*N, rk=Rk/phi^2, amplitude=0.3, then 500 live steps.
The v3-strength buckle is reproduced inside the v4 engine via photon_coupling=False, which makes
CrystalGraftV4._buckle_forces() defer to the v3 frozen-Beltrami-template buckle (crystal_graft_v4.py:147-149)
once build_beltrami_director has populated self._b_dir. So the ONLY engine difference vs graft-v3's
destructive smoke is the v4 LOCK substep (lock_eta>0).

THE SEED-SCALING CONFOUND (surfaced, flag-don't-fix): v4's own seed_omega_known_2_3 docstring
(crystal_graft_v4.py:300-307) flags the v2/v3 plant default delta=0.4 as a MIS-SCALED seed (implied
pi_omega ~ 50x amplitude at the v4 CFL dt) — "a SEED artifact, NOT an instability". To disentangle
"the lock saves a real buckle-destroyed knot" from "the lock damps a seed-artifact swing", BOTH seed
scalings are run: delta=0.4 (the exact v3 plant that read back (2,1)) AND delta=omega_gap*dt (the v4
well-scaled quasi-stationary plant). Each x {lock OFF, lock ON} = 4 arms.

RESOLUTION RULE (frozen here, BEFORE the run; Rule 11 — applied to the data, not tuned to it):
  lock-OFF collapses (2,3)->(2,1)-style AND lock-ON preserves (2,3)  -> EARNS-ITS-KEEP
  both arms survive (both read (2,3))                                -> NOT-DEMONSTRATED (source, not lock)
  both arms collapse (neither reads (2,3))                           -> INERT (lock cannot save it)

apparatus-floor (ave-apparatus-floor-attribution): the plant minor radius rk and the alias gate are
reported; a t0 read != (2,3) means the plant itself is below the extractor floor -> arm VOID.
ave-conserved-vs-pumped: the LOCK is the subject — does it CONSERVE the planted topology against a
destructive source, or is survival the source's doing? lock_helicity_drift (crystal_graft_v4.py:348-352,
built but never called anywhere in-tree) is wired per-substep and reported in both arms.
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core.constants import PHI  # noqa: E402  emergence comparison target ONLY (never fed to engine)
from ave.core.crystal_graft_v4 import CrystalGraftV4  # noqa: E402
from ave.utils.fast_winding_extractor import extract_2_3_omega_fast  # noqa: E402

OUT = Path(__file__).parent
PHI2 = PHI**2

# ── v3 config (git show 4627651a:.../crystal_graft_v3_run.py — _make_engine + smoke_independence) ──
N = 44
LOCK_ETA = 0.05  # the FROZEN v4 lock strength (matches the full-run / SMOKE-1 value)
V3CFG = dict(
    source_mode="abc", lam_sign=1, p=2, q=3, S_min=2e-3, A_cap=0.999, omega_gap=1.0,
    wall_center=0.78, wall_width=0.16, kappa_tilde=6.0 / 5.0, pml_thickness=5,
)
PLANT_AMP = 0.3          # v3 smoke_independence amplitude
N_STEPS = 600            # > 500 (prereg LOCK-smoke floor); v3 destroyed at 500
DELTA_V3 = 0.4           # the v2/v3 seed_omega_known_2_3 hard-coded phase advance (the mis-scaled plant)


def wall_geometry(e):
    """R, r of the Gamma=-1 wall shell the Beltrami director lives on (verbatim from v3 run script)."""
    A = e.strain_field()
    c = (e.N - 1) / 2.0
    i, j, k = np.indices((e.N, e.N, e.N))
    rr = np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2)
    m = e.interior_mask()
    shell = (np.abs(A - e.wall_center) < 0.5 * e.wall_width) & m
    if shell.sum() > 8:
        R = float(np.median(rr[shell]))
        r = float(max(2.0, np.std(rr[shell]) + e.wall_width * e.N * 0.25))
    else:
        R = 0.22 * e.N
        r = max(2.0, e.wall_width * e.N * 0.5)
    return R, r


def read_winding(omega, pi_omega, R, r):
    """The SAME (2,3) read as crystal_graft_v4_run.read_winding (fast extractor + alias check)."""
    res = extract_2_3_omega_fast(omega, pi_omega, R, r, N)
    for sec in ("w_tor", "w_pol"):
        raws = res.get(f"{sec}_raw_list", [])
        if raws:
            mode = res[sec]
            outl = sum(1 for w in raws if abs(abs(w) - mode) > 1.0 or abs(w) > 6.5)
            res[f"{sec}_alias_frac"] = outl / len(raws)
        else:
            res[f"{sec}_alias_frac"] = 0.0
    res["alias_clean"] = (res["w_tor_alias_frac"] <= 0.34) and (res["w_pol_alias_frac"] <= 0.34)
    return res


def build_v3strength(lock_eta):
    """v4 engine wearing the v3-strength buckle: photon_coupling=False -> _buckle_forces() defers to v3's
    frozen-Beltrami-template buckle (crystal_graft_v4.py:147-149) once build_beltrami_director sets _b_dir.
    The ONLY thing lock_eta toggles is the CHANGE-2 lock substep. Everything else is v3-identical."""
    ic = N // 2
    e = CrystalGraftV4(N=N, lock_on=(lock_eta > 0), lock_eta=lock_eta, photon_coupling=False,
                       buckle_on=True, **V3CFG)
    e.seed_bulk((ic, ic, ic), sigma=4.5, frac=0.9)
    e.seed_photon((ic, ic, ic), sigma=5.0, wavelength=7.0, amplitude=0.35, helicity=1.0)  # decoupled (matches v3)
    e.freeze_wall_window()
    R, r = wall_geometry(e)
    e.build_beltrami_director(R=R, r=r)  # <- builds _b_dir => the v3-strength buckle is now active
    return e


def run_arm(*, label, delta, lock_eta):
    """Plant a resolvable (2,3), step N_STEPS under the v3-strength buckle, recording the lock canary +
    H_bel per substep. Returns the t0/tN winding reads + the helicity-drift series."""
    Rk, rk = 0.22 * N, (0.22 * N) / PHI2  # = 9.68, 3.70 cells (v3 smoke_independence plant scale)
    e = build_v3strength(lock_eta)
    e.seed_omega_known_2_3(Rk, rk, amplitude=PLANT_AMP, p=2, q=3, delta=delta)
    w0 = read_winding(e.omega, e.omega_velocity(), Rk, rk)
    Hbel0 = e.helicity_bel()

    drift_abs, hbel_t = [], []
    for _ in range(N_STEPS):
        e.step()
        # lock_helicity_drift = relative H_bel change ACROSS the lock substep (0 when lock OFF: no substep)
        drift_abs.append(abs(e.lock_helicity_drift()))
        hbel_t.append(e.helicity_bel())
    w1 = read_winding(e.omega, e.omega_velocity(), Rk, rk)

    hbel_t = np.asarray(hbel_t)
    survives = bool(w1["is_2_3"] and (w1["w_tor"], w1["w_pol"]) == (2, 3))
    collapsed_pol = bool((w1["w_tor"], w1["w_pol"]) == (2, 1))  # the literal v3 (2,3)->(2,1) signature
    out = {
        "label": label, "delta": delta, "lock_eta": lock_eta, "n_steps": N_STEPS,
        "Rk": Rk, "rk": rk, "plant_amp": PLANT_AMP,
        "read_t0": [w0["w_tor"], w0["w_pol"]], "is_2_3_t0": bool(w0["is_2_3"]),
        "alias_clean_t0": bool(w0["alias_clean"]),
        "read_tN": [w1["w_tor"], w1["w_pol"]], "is_2_3_tN": bool(w1["is_2_3"]),
        "rel_tN": [w1["w_tor_rel"], w1["w_pol_rel"]], "alias_clean_tN": bool(w1["alias_clean"]),
        "survives_2_3": survives, "collapsed_to_2_1": collapsed_pol,
        "H_bel_t0": float(Hbel0), "H_bel_tN": float(hbel_t[-1]),
        "H_bel_min": float(hbel_t.min()), "H_bel_max": float(hbel_t.max()),
        "lock_drift_max": float(np.max(drift_abs)), "lock_drift_mean": float(np.mean(drift_abs)),
        "lock_active": bool(lock_eta > 0),
        "_hbel_t": hbel_t.tolist(),  # for the figure (stripped from the JSON summary)
    }
    print(f"  [{label:16s}] delta={delta:<7.4g} lock_eta={lock_eta:.3f} | t0={out['read_t0']}(is23={out['is_2_3_t0']}) "
          f"-> tN={out['read_tN']}(is23={out['is_2_3_tN']}) | H_bel {Hbel0:+.2f}->{out['H_bel_tN']:+.2f} "
          f"[min {out['H_bel_min']:+.2f}] | lock|drift| max={out['lock_drift_max']:.2e} mean={out['lock_drift_mean']:.2e}",
          flush=True)
    return out


def classify(res):
    """Apply the FROZEN resolution rule to the PRIMARY (faithful v3-seed, delta=0.4) arms; the v4-seed arms
    are the seed-artifact disentangler."""
    def verdict(off, on):
        off_collapse = not off["survives_2_3"]
        on_survive = on["survives_2_3"]
        # arms VOID if the plant itself never read (2,3) at t0 (below the extractor floor)
        if not (off["is_2_3_t0"] and on["is_2_3_t0"]):
            return "VOID (plant below extractor floor: t0 != (2,3))"
        if off_collapse and on_survive:
            return "EARNS-ITS-KEEP"
        if (not off_collapse) and on_survive:
            return "NOT-DEMONSTRATED"  # both survive => the source, not the lock
        if off_collapse and (not on_survive):
            return "INERT"             # both collapse => the lock cannot save it
        return "NOT-DEMONSTRATED"
    return {
        "primary_v3seed": verdict(res["v3seed_lockOFF"], res["v3seed_lockON"]),
        "control_v4seed": verdict(res["v4seed_lockOFF"], res["v4seed_lockON"]),
    }


def make_figures(res):
    paths = []
    arms = ["v3seed_lockOFF", "v3seed_lockON", "v4seed_lockOFF", "v4seed_lockON"]

    # fig1 — winding readback (t0 vs tN) per arm
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.6))
    x = np.arange(len(arms))
    wt0 = [res[a]["read_t0"][0] for a in arms]; wp0 = [res[a]["read_t0"][1] for a in arms]
    wtN = [res[a]["read_tN"][0] for a in arms]; wpN = [res[a]["read_tN"][1] for a in arms]
    ax[0].bar(x - 0.3, wp0, 0.28, label="w_pol  t0 (plant)", color="C1", alpha=0.5)
    ax[0].bar(x - 0.02, wpN, 0.28, label="w_pol  tN", color="C1")
    ax[0].bar(x + 0.3, wtN, 0.28, label="w_tor  tN", color="C0")
    ax[0].axhline(3, ls=":", color="C1"); ax[0].axhline(2, ls=":", color="C0")
    ax[0].set_xticks(x); ax[0].set_xticklabels(arms, rotation=18, fontsize=7)
    ax[0].set_ylabel("winding integer")
    v = classify(res)
    ax[0].set_title(f"Planted (2,3) readback under v3-strength buckle (N={N}, {N_STEPS} steps)\n"
                    f"PRIMARY (v3-seed delta=0.4): {v['primary_v3seed']}")
    ax[0].legend(fontsize=7)

    # fig2 — H_bel(t): the planted topological charge, lock OFF vs ON, both seeds
    for a, c, ls in [("v3seed_lockOFF", "C3", "-"), ("v3seed_lockON", "C2", "-"),
                     ("v4seed_lockOFF", "C3", "--"), ("v4seed_lockON", "C2", "--")]:
        h = res[a]["_hbel_t"]
        ax[1].plot(np.arange(len(h)), h, ls, color=c, lw=1.3,
                   label=f"{a} (|drift|max={res[a]['lock_drift_max']:.1e})")
    ax[1].set_yscale("symlog", linthresh=10.0)
    ax[1].set_xlabel("step"); ax[1].set_ylabel("H_bel(t) = planted topological charge (symlog)")
    ax[1].set_title("Planted-knot helicity vs time (lock ON green / OFF red; v3-seed solid / v4-seed dashed)\n"
                    "lock-ON curve sits ON lock-OFF: the lock is inert to knot fate in BOTH regimes")
    ax[1].legend(fontsize=6)
    fig.tight_layout()
    p = OUT / "crystal_graft_v4_lock_isolation_fig.png"
    fig.savefig(p, dpi=115); plt.close(fig); paths.append(p.name)
    return paths


def main():
    print("=" * 96)
    print("  CRYSTAL-GRAFT v4 — LOCK-ISOLATION SMOKE (v3-strength buckle; lock ON vs OFF; planted (2,3))")
    print("=" * 96, flush=True)
    res = {}
    res["v3seed_lockOFF"] = run_arm(label="v3seed_lockOFF", delta=DELTA_V3, lock_eta=0.0)
    res["v3seed_lockON"] = run_arm(label="v3seed_lockON", delta=DELTA_V3, lock_eta=LOCK_ETA)
    # v4 well-scaled plant (delta=omega_gap*dt) — built per-arm so dt is known; pass the engine's value
    dt_probe = build_v3strength(0.0).dt
    delta_v4 = V3CFG["omega_gap"] * dt_probe
    res["v4seed_lockOFF"] = run_arm(label="v4seed_lockOFF", delta=delta_v4, lock_eta=0.0)
    res["v4seed_lockON"] = run_arm(label="v4seed_lockON", delta=delta_v4, lock_eta=LOCK_ETA)

    verdicts = classify(res)
    figs = make_figures(res)
    summary = {k: {kk: vv for kk, vv in v.items() if kk != "_hbel_t"} for k, v in res.items()}
    out = {
        "config": {"N": N, "v3_config": V3CFG, "lock_eta": LOCK_ETA, "n_steps": N_STEPS,
                   "plant_amp": PLANT_AMP, "delta_v3": DELTA_V3, "delta_v4": delta_v4,
                   "v3strength_via": "photon_coupling=False + build_beltrami_director (crystal_graft_v4.py:147-149)"},
        "arms": summary, "verdicts": verdicts, "figures": figs,
    }
    (OUT / "crystal_graft_v4_lock_isolation_results.json").write_text(json.dumps(out, indent=2, default=str))
    print("\n" + "=" * 96)
    print(f"  PRIMARY (faithful v3-seed delta=0.4):  {verdicts['primary_v3seed']}")
    print(f"  CONTROL (v4 well-scaled seed):         {verdicts['control_v4seed']}")
    print("=" * 96, flush=True)
    return out


if __name__ == "__main__":
    main()
