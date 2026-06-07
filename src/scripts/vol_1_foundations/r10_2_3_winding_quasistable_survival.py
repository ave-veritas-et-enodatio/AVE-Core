#!/usr/bin/env python3
"""
Phase 0.5 (NO new engine code): does a QUASI-STABLE (sub-saturation) (2,3)
regime exist, and does the winding SURVIVE there?

Prereg (FROZEN):  research/2026-06-06_cosserat-geometric-integrator-prereg.md
Brief  (§1.5):    _orchestration/2026-06-06_cosserat-geometric-integrator.md
Reuses (UNMODIFIED) the validated coordinate-correct extractor + the Arm-C
imposed control from r10_2_3_winding_extractor_coordinate.py.

────────────────────────────────────────────────────────────────────────────
WHY (Phase-0 verdict (B))
────────────────────────────────────────────────────────────────────────────
Phase-0 showed the Arm-C control OVER-SATURATES: A²max = 1.69 at the SEED
(amp 0.40, already >1) → ~6 under the pumping SpatialDipoleCPSource sources.
The (2,3) is DETONATED by over-amplitude in BOTH sectors at once — V0 never had
a clean conservation regime. So the original "12/12→5/12 fail" was a bad-test-
regime (over-saturation) artifact, not winding loss. Phase 0.5 finds a regime
where A²max(t) ≈ const (sub-saturation) and re-tests survival there.

────────────────────────────────────────────────────────────────────────────
KEY VARIABLE — sources-OFF free evolution
────────────────────────────────────────────────────────────────────────────
Build the SAME imposed-(2,3) seed (initialize_2_3_voltage_ansatz on the golden-
torus shell) but evolve WITHOUT the pumping SpatialDipoleCPSource sources, so
A²max cannot be pumped past saturation — it should settle/decay, not blow up.

The PairNucleationGate observer is ALSO dropped in the sources-off variant: it
is an observer-WITH-SIDE-EFFECT (vacuum_engine.py:1172) that INJECTS a Beltrami
vortex pair once a bond reaches Meissner saturation (A²≥0.95). "Free evolution,
no pumping" means no injection of any kind. In the sub-saturation Goldilocks
band the gate would be dormant anyway (A²<0.95 ⇒ never fires), so dropping it
changes nothing load-bearing; at the over-amplitude end it removes exactly the
saturation-triggered injection the test is trying to avoid. Flagged, not buried.

  SEED SCALING (forward, not fit): the ansatz envelope is LINEAR in `amplitude`
  (tlm_…_eigenmode.py:78,121) ⇒ A²max(seed) ∝ amplitude². Phase-0 measured
  A²max(0.40 seed)=1.69 ⇒ A²max(amp) ≈ 1.69·(amp/0.40)²; A²max=1 ≈ amp 0.31.
  So the sub-saturation band is amp < ~0.31.

────────────────────────────────────────────────────────────────────────────
DISCRIMINATORS (read from the numbers — NOT fit; ave-driver-script-honesty)
────────────────────────────────────────────────────────────────────────────
  (I)   quasi-stable band exists (A²max(t)<1, no blow-up) AND the (2,3)
        SURVIVES (w1=2/w2=3 hold over evolution) → physically conserved; the
        V0 "fail" was purely over-saturation → V0 FORK RESOLVED (the (2,3) is
        innocent; vindicates topological protection).
  (II)  band exists AND the (2,3) DEGRADES → genuine physics degradation,
        independent of amplitude.
  (III) NO quasi-stable band — the (2,3) only forms/survives WITH saturation
        (sub-saturation = no surviving (2,3)) → the imposed-(2,3) ansatz can't
        be both formed and stable (a seed/ansatz finding).

HONEST SCOPE (substrate-native-check CP8): sources-off free evolution is closer
to seed-the-precursor than the pumped Arm-C, BUT the (2,3) is still an IMPOSED
PLANT — a (2,3) that survives free evolution shows conservation-of-an-imposed-
plant, NOT autonomous hosting. This is a CONSISTENCY/conservation test, not an
emergence claim (consistency-vs-emergence).

DISCIPLINE WALK — see module footer.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve()
sys.path.insert(0, str(_HERE.parents[3] / "src"))
sys.path.insert(0, str(_HERE.parent))

from ave.core.constants import ALPHA  # noqa: E402  (ave-canonical-source)

import r10_2_3_winding_extractor_coordinate as ext  # noqa: E402  (reuse; no new engine code)

# Substrate-derived constants — reuse the extractor's canonical values (no fresh
# literals; ave-canonical-source). A²=1 is the rupture/wall scale; √(2α) is Op14.
PHI = ext.PHI
DT = ext.DT
COMPTON_PERIOD = ext.COMPTON_PERIOD
A2_OP14 = ext.A2_OP14
A2_WALL = 1.0  # Op14 rupture / wall scale (A²→1 = boundary forms). NOT a literal
#              physics constant — the saturation kernel's own normalization.


# ══════════════════════════════════════════════════════════════════════════════
# sources-OFF free-evolution engine: impose (2,3), NO sources, NO nucleation gate
# ══════════════════════════════════════════════════════════════════════════════
def _build_free_engine(N, PML, amplitude):
    """Build the EXACT Arm-C engine config (vacuum_engine flags identical to
    ext._run_armC_full_field) and impose the SAME (2,3) ansatz on the SAME
    golden-torus shell — but add NO SpatialDipoleCPSource sources and NO
    PairNucleationGate. Pure free evolution from the planted seed."""
    from ave.topological.vacuum_engine import VacuumEngine3D
    from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz

    engine = VacuumEngine3D.from_args(
        N=N, pml=PML, temperature=0.0, amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True, enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True, axiom_4_enabled=True,
    )
    # IMPOSED (2,3): identical placement to Arm-C (legacy R_shell=0.22N).
    R_shell = 0.22 * N
    r_shell = R_shell / (PHI**2)
    initialize_2_3_voltage_ansatz(engine.k4, R=R_shell, r=r_shell,
                                  amplitude=amplitude)
    return engine, {"R_shell": R_shell, "r_shell": r_shell}


def _a2_phi2_max(engine):
    """Reactance PAIR snapshot (substrate-native-check CP6): C-state A²max from
    V_inc AND L-state Φ²max from Phi_link, both over interior+all sites. A²max is
    the saturation driver; Φ²max confirms the quasi-stability is genuine (not
    C settling while L grows). Returns (a2_max, phi2_max)."""
    V_inc = engine.k4.V_inc
    Phi = engine.k4.Phi_link
    a2 = float(np.sum(np.asarray(V_inc) ** 2, axis=-1).max())
    phi2 = float(np.sum(np.asarray(Phi) ** 2, axis=-1).max())
    return a2, phi2


def run_free_evolution(N, PML, amplitude, snapshot_periods, a2_log_stride=2):
    """Single sources-OFF trajectory: impose the (2,3), step to max(snapshot),
    log the reactance pair (A²max, Φ²max) every `a2_log_stride` steps (the fine
    quasi-stability curve), and run the UNMODIFIED extractor at each snapshot.

    Returns (snapshots[list of extractor records], a2_trace[(t,a2,phi2)],
    meta). DETERMINISTic single trajectory (temperature=0.0), so the snapshot
    sequence is one self-consistent evolution (not stitched truncated re-runs)."""
    eng, geo = _build_free_engine(N, PML, amplitude)
    snap_steps = {int(round(k * COMPTON_PERIOD / DT)): k for k in snapshot_periods}
    n_steps = max(snap_steps) if snap_steps else 0

    records, a2_trace = [], []
    t0 = time.time()

    def _snap(step_i, k, a2, phi2):
        rec = ext._extract_on_engine(eng, N, PML, f"off_amp{amplitude}_t{k}")
        rec.update(n_periods=float(k), n_steps=int(step_i),
                   phi2_max=float(phi2), amplitude=float(amplitude),
                   with_sources=False)
        cf1, c1, n1 = _coherence(rec, "w1")
        cf2, c2, n2 = _coherence(rec, "w2")
        rec["w1_coherence_frac"], rec["w2_coherence_frac"] = cf1, cf2
        records.append(rec)
        print(f"    [off amp={amplitude:.2f}] t={k:>5.1f}T  "
              f"w1={rec['w1_base']}(coh {c1}/{n1})  w2={rec['w2_fibre']}(coh {c2}/{n2})  "
              f"c={rec['crossing_count_c']}  A²max={rec['a2_max']:.3f}  "
              f"Φ²max={phi2:.3g}  sites={rec.get('n_shell_sites', 0)}", flush=True)

    # t=0 seed snapshot
    a2, phi2 = _a2_phi2_max(eng)
    a2_trace.append((0.0, a2, phi2))
    if 0 in snap_steps:
        _snap(0, 0.0, a2, phi2)

    # Blow-up guard (Rule 10 empirical-driver discipline): A² is saturation-
    # clamped (~O(1)) but the L-store Φ_link can run away near the wall (the
    # smoke saw Φ²max 0→251 sources-OFF at amp 0.30). If A²/Φ² goes non-finite
    # or past a sane bound, record the detonation t + a final snapshot and STOP —
    # honest blow-up record, not a nan crash + not wasted evolution.
    blew_up = False
    for step_i in range(1, n_steps + 1):
        eng.step()
        a2, phi2 = _a2_phi2_max(eng)
        if step_i % a2_log_stride == 0 or step_i in snap_steps:
            a2_trace.append((step_i * DT / COMPTON_PERIOD, a2, phi2))
        if step_i in snap_steps:
            _snap(step_i, float(snap_steps[step_i]), a2, phi2)
        bad = (not np.isfinite(a2)) or (not np.isfinite(phi2)) or a2 > 1e3 or phi2 > 1e8
        if bad:
            blew_up = True
            t_blow = round(step_i * DT / COMPTON_PERIOD, 2)
            geo["blew_up_t"] = t_blow
            if step_i not in snap_steps:   # capture the blow-up state
                _snap(step_i, t_blow, a2, phi2)
            print(f"    [off amp={amplitude:.2f}] BLEW UP at t={t_blow}T "
                  f"(A²max={a2:.3g}, Φ²max={phi2:.3g}) — sources-OFF self-amplification",
                  flush=True)
            break

    geo["blew_up"] = bool(blew_up)
    geo["wall_s"] = round(time.time() - t0, 1)
    geo["n_steps"] = int(n_steps)
    return records, a2_trace, geo


def run_sources_on_snapshots(N, PML, amplitude, snapshot_periods):
    """sources-ON comparison: REUSE ext._run_armC_full_field (the EXACT Phase-0
    Arm-C: counter-propagating sources + PairNucleationGate) via deterministic
    truncated re-runs at each snapshot. Records (A²max, Φ²max) + extractor at
    each. This faithfully reproduces the Phase-0 over-driven curve."""
    records, a2_trace = [], []
    for k in snapshot_periods:
        t0 = time.time()
        eng, meta = ext._run_armC_full_field(N=N, PML=PML, n_periods=k,
                                              amplitude=amplitude)
        rec = ext._extract_on_engine(eng, N, PML, f"on_amp{amplitude}_t{k}")
        a2, phi2 = _a2_phi2_max(eng)
        rec.update(n_periods=int(k), n_steps=int(meta.get("n_steps", 0)),
                   phi2_max=float(phi2), amplitude=float(amplitude),
                   with_sources=True, wall_s=round(time.time() - t0, 1))
        cf1, c1, n1 = _coherence(rec, "w1")
        cf2, c2, n2 = _coherence(rec, "w2")
        rec["w1_coherence_frac"], rec["w2_coherence_frac"] = cf1, cf2
        records.append(rec)
        a2_trace.append((float(k), float(a2), float(phi2)))
        print(f"    [ON  amp={amplitude:.2f}] t={k:>3}T  "
              f"w1={rec['w1_base']}(coh {c1}/{n1})  w2={rec['w2_fibre']}(coh {c2}/{n2})  "
              f"c={rec['crossing_count_c']}  A²max={rec['a2_max']:.3f}  "
              f"Φ²max={phi2:.3f}  [{rec['wall_s']}s]", flush=True)
    return records, a2_trace


def _coherence(rec, half):
    """Per-half modal-coherence fraction (count/n_walks) — the 12/12→5/12 metric.
    half ∈ {'w1','w2'}. (Same definition as the Phase-0 driver.)"""
    if half == "w1":
        c, n = rec.get("w1_base_modal_count", 0), rec.get("w1_base_n_walks", 0)
    else:
        c, n = rec.get("w2_fibre_modal_count", 0), rec.get("w2_fibre_n_walks", 0)
    return (float(c) / float(n)) if n else float("nan"), int(c), int(n)


# ══════════════════════════════════════════════════════════════════════════════
# Per-amplitude band membership + survival (transparent rule, NO fit)
# ══════════════════════════════════════════════════════════════════════════════
def classify_amplitude(records, a2_trace):
    """Forward read of ONE sources-off amplitude's snapshots → band membership
    + survival. NO optimizer, NO target-match — every field is a printed delta.

      seed_formed   = the extractor recovers a (2,3) at t=0 (is_2_3).
      quasi_stable  = A²max(t) NEVER reaches the wall A²→1 over the whole
                      evolution (sub-saturation throughout) — the Goldilocks
                      saturation gate. (Settling/decay below 1 counts; only a
                      blow-up THROUGH the wall fails.)
      persisted     = a (2,3) is still read at SOME evolved snapshot (t>0) — the
                      winding lived past the planted instant.
      survived      = the winding INTEGERS hold (w1=2 AND w2=3) at the LAST TWO
                      evolved snapshots — SUSTAINED topological survival, robust
                      to a single-frame LC-equilibration transient (the all-C
                      seed spins up Φ_link over the first ~few T; a one-snapshot
                      dip-then-recover must NOT count as survival).
      survived_final = is_2_3 at the last snapshot only (accepts (3,2)/c=3) —
                      reported alongside so a sustained-vs-final divergence shows.
    """
    seed, evolved = records[0], records[-1]
    a2_all = [r["a2_max"] for r in records] + [p[1] for p in a2_trace]
    phi2_all = [r.get("phi2_max", 0.0) for r in records] + [p[2] for p in a2_trace]
    late = records[-2:] if len(records) >= 2 else records
    survived_sustained = all(r["w1_base"] == 2 and r["w2_fibre"] == 3 for r in late)
    t_first_loss = next((r["n_periods"] for r in records[1:]
                         if not ext.is_2_3(r)), None)
    return {
        "amplitude": float(seed.get("amplitude", float("nan"))),
        "seed_formed": bool(ext.is_2_3(seed)),
        "a2_seed": float(seed["a2_max"]),
        "a2_peak": float(max(a2_all)),
        "a2_evolved": float(evolved["a2_max"]),
        "phi2_seed": float(seed.get("phi2_max", 0.0)),
        "phi2_peak": float(max(phi2_all)),
        "quasi_stable": bool(max(a2_all) < A2_WALL),
        "persisted_past_seed": bool(any(ext.is_2_3(r) for r in records[1:])),
        "survived": bool(survived_sustained),
        "survived_final": bool(ext.is_2_3(evolved)),
        "w1_seed": seed["w1_base"], "w2_seed": seed["w2_fibre"],
        "w1_evolved": evolved["w1_base"], "w2_evolved": evolved["w2_fibre"],
        "coh_w1_seed": seed["w1_coherence_frac"], "coh_w2_seed": seed["w2_coherence_frac"],
        "coh_w1_evolved": evolved["w1_coherence_frac"],
        "coh_w2_evolved": evolved["w2_coherence_frac"],
        "coh_w1_late_min": float(min(r["w1_coherence_frac"] for r in late)),
        "coh_w2_late_min": float(min(r["w2_coherence_frac"] for r in late)),
        "t_first_loss": t_first_loss,
        "n_periods_evolved": evolved["n_periods"],
    }


def classify_verdict(per_amp):
    """Band-level I/II/III from the per-amplitude reads (transparent rule).

      (I)   ∃ amp: quasi_stable & seed_formed & SURVIVED → the (2,3) is
            physically conserved in a sub-saturation regime → V0 fork RESOLVED.
      (II)  not (I), but ∃ amp: quasi_stable & seed_formed & persisted_past_seed
            → a quasi-stable (2,3) regime exists, the winding lives for a while
            then DEGRADES → genuine physics degradation, amplitude-independent.
      (III) not (I)/(II): every quasi-stable+formed amp loses the (2,3) by the
            FIRST evolved snapshot → sub-saturation = no persisting (2,3); the
            imposed plant can't be both formed and stable (a seed/ansatz finding).
    """
    band = [a for a in per_amp if a["quasi_stable"] and a["seed_formed"]]
    goldilocks = [a for a in band if a["survived"]]
    persisted = [a for a in band if a["persisted_past_seed"]]
    if goldilocks:
        verdict, why = "I", (
            "a sub-saturation (quasi-stable) regime exists AND the (2,3) SURVIVES "
            "there (winding integers hold under free evolution) — the (2,3) is "
            "physically conserved; the V0 'fail' was purely over-saturation → "
            "V0 FORK RESOLVED.")
    elif persisted:
        verdict, why = "II", (
            "a quasi-stable (sub-saturation) regime exists and the (2,3) forms + "
            "lives for a while, but DEGRADES under free evolution at EVERY "
            "amplitude — genuine physics degradation, independent of amplitude "
            "(NOT an over-saturation artifact).")
    elif band:
        verdict, why = "III", (
            "the (2,3) forms at the seed but is GONE by the first evolved "
            "snapshot at every sub-saturation amplitude — the imposed (2,3) plant "
            "cannot be both formed AND stable sub-saturation; it only appears "
            "transiently. A seed/ansatz finding, not a conservation result.")
    else:
        verdict, why = "III", (
            "no amplitude is simultaneously sub-saturation AND (2,3)-formed — no "
            "quasi-stable (2,3) regime exists at all.")
    return {
        "verdict": verdict, "why": why,
        "band_amps": [a["amplitude"] for a in band],
        "goldilocks_amps": [a["amplitude"] for a in goldilocks],
        "persisted_amps": [a["amplitude"] for a in persisted],
        "a2_wall": A2_WALL,
    }


# ══════════════════════════════════════════════════════════════════════════════
# Dark-aesthetic figure (repo convention: #0d1117 / #161b22 / #00ffcc)
# ══════════════════════════════════════════════════════════════════════════════
def plot_quasistable(off_traces, off_amps, on_traces, on_amps, per_amp,
                     verdict, survival_amps, survival_records, out_path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    BG, PANEL, GRID = "#0d1117", "#161b22", "#30363d"
    C_OFF, C_ON, C2, C3 = "#00ffcc", "#f85149", "#00ffcc", "#ff7ad9"
    WALL, OP14 = "#f0a04b", "#8b949e"

    fig, axes = plt.subplots(3, 1, figsize=(9.5, 12))
    fig.patch.set_facecolor(BG)

    # ── Panel 1 — A²max(t): sources-ON (blow-up) vs sources-OFF (settles) ──
    ax = axes[0]
    ax.set_facecolor(PANEL)
    ax.axhline(A2_WALL, color=WALL, lw=1.0, ls="--", alpha=0.8)
    ax.axhline(A2_OP14, color=OP14, lw=0.8, ls=":", alpha=0.6)
    ax.text(0.5, A2_WALL, " A²=1 wall (rupture/detonation)", color=WALL,
            fontsize=8, va="bottom")
    ax.text(0.5, A2_OP14, " √(2α) Op14 onset", color=OP14, fontsize=8, va="bottom")
    greens = plt.cm.winter(np.linspace(0.15, 0.95, len(off_amps)))
    for amp, tr, col in zip(off_amps, off_traces, greens):
        t = [p[0] for p in tr]; a2 = [p[1] for p in tr]
        ax.plot(t, a2, "-", color=col, lw=1.8, label=f"OFF amp={amp:.2f}")
    for amp, tr in zip(on_amps, on_traces):
        t = [p[0] for p in tr]; a2 = [p[1] for p in tr]
        ax.plot(t, a2, "s--", color=C_ON, lw=2.0, ms=6, alpha=0.9,
                label=f"ON amp={amp:.2f} (Arm-C)")
    ax.set_ylabel("A²max  (saturation driver)", color="#c9d1d9")
    ax.set_xlabel("evolution time  (Compton periods)", color="#c9d1d9")
    ax.set_title(f"Phase 0.5 — sources-OFF free evolution vs Arm-C pumping     "
                 f"VERDICT = ({verdict['verdict']})",
                 color="#e6edf3", fontsize=12, pad=10)
    ax.legend(facecolor=PANEL, edgecolor=GRID, labelcolor="#c9d1d9",
              fontsize=7.5, ncol=2, loc="upper right")

    # ── Panel 2 — Goldilocks band map: a2_peak vs amplitude, survival-colored ──
    ax = axes[1]
    ax.set_facecolor(PANEL)
    ax.axhline(A2_WALL, color=WALL, lw=1.0, ls="--", alpha=0.8)
    amps = [a["amplitude"] for a in per_amp]
    a2_seed = [a["a2_seed"] for a in per_amp]
    a2_peak = [a["a2_peak"] for a in per_amp]
    ax.plot(amps, a2_seed, "o--", color="#79c0ff", lw=1.4, ms=7, alpha=0.8,
            label="A²max(seed)")
    ax.plot(amps, a2_peak, "D-", color=WALL, lw=1.4, ms=6, alpha=0.7,
            label="A²max(peak over evolution)")
    for a in per_amp:
        ok = a["survived"]
        ax.scatter([a["amplitude"]], [a["a2_peak"]], s=170, zorder=5,
                   marker=("*" if ok else "X"),
                   color=("#3fb950" if ok else C_ON),
                   edgecolor="#0d1117", linewidth=0.6)
    ax.scatter([], [], marker="*", color="#3fb950", s=120, label="(2,3) survived")
    ax.scatter([], [], marker="X", color=C_ON, s=100, label="(2,3) degraded")
    ax.set_ylabel("A²max", color="#c9d1d9")
    ax.set_xlabel("imposed amplitude  (sources-off)", color="#c9d1d9")
    ax.set_title("Goldilocks-band map: sub-saturation AND surviving?",
                 color="#e6edf3", fontsize=11, pad=8)
    ax.legend(facecolor=PANEL, edgecolor=GRID, labelcolor="#c9d1d9", fontsize=8)

    # ── Panel 3 — survival: w1/w2 vs t for representative band amplitudes ──
    ax = axes[2]
    ax.set_facecolor(PANEL)
    ax.axhline(2, color=C2, lw=0.8, ls=":", alpha=0.5)
    ax.axhline(3, color=C3, lw=0.8, ls=":", alpha=0.5)
    styles = ["-", "--", "-."]
    for idx, (amp, recs) in enumerate(zip(survival_amps, survival_records)):
        t = [r["n_periods"] for r in recs]
        w1 = [r["w1_base"] for r in recs]
        w2 = [r["w2_fibre"] for r in recs]
        ls = styles[idx % len(styles)]
        ax.plot(t, w1, "o" + ls, color=C2, lw=2.0, ms=7,
                label=f'w1 "2" amp={amp:.2f}')
        ax.plot(t, w2, "s" + ls, color=C3, lw=2.0, ms=7,
                label=f'w2 "3" amp={amp:.2f}')
    ax.text(0.3, 2, " imposed w1=2", color=C2, fontsize=8, va="bottom")
    ax.text(0.3, 3, " imposed w2=3", color=C3, fontsize=8, va="bottom")
    ax.set_ylabel("winding integer", color="#c9d1d9")
    ax.set_xlabel("evolution time  (Compton periods)", color="#c9d1d9")
    ax.set_title("(2,3) survival under sub-saturation free evolution",
                 color="#e6edf3", fontsize=11, pad=8)
    ax.legend(facecolor=PANEL, edgecolor=GRID, labelcolor="#c9d1d9",
              fontsize=7.5, ncol=2, loc="best")

    for a in axes:
        for sp in a.spines.values():
            sp.set_color(GRID)
        a.tick_params(colors="#8b949e")
        a.grid(True, color=GRID, lw=0.5, alpha=0.4)

    fig.tight_layout()
    fig.savefig(out_path, facecolor=BG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
def main(smoke=False):
    print("=" * 80, flush=True)
    print("  Phase 0.5 — quasi-stable (2,3) survival  (sources-OFF free evolution")
    print("              vs Arm-C pumping; amplitude sweep)")
    print("  Reuses UNMODIFIED r10_2_3_winding_extractor_coordinate (no new engine code)")
    print("=" * 80, flush=True)
    print(f"  ALPHA={ALPHA} (ave-canonical-source)   √(2α)={A2_OP14:.4f}   "
          f"A²=1 wall ≈ amp 0.31 (seed ∝ amp²)\n", flush=True)

    N, PML = 48, 4
    if smoke:
        off_amps = [0.20, 0.30]
        on_amps = [0.40]
        snaps, on_snaps = [0, 2, 5], [0, 2, 5]
    else:
        off_amps = [0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
        on_amps = [0.40, 0.20]
        # sources-OFF to t=40 for a definitive LATE survival read; sources-ON
        # only to t=10 (the blow-up is fully evident by t=2-5; Phase-0 already
        # carried Arm-C to t=40 sustained ~5-6) — saves the expensive t=20/40
        # truncated re-runs without losing the head-to-head A²max story.
        snaps, on_snaps = [0, 2, 5, 10, 20, 40], [0, 2, 5, 10]
    print(f"  config: N={N} PML={PML}   off_amps={off_amps} snaps={snaps}\n"
          f"          on_amps={on_amps} on_snaps={on_snaps}\n", flush=True)

    t_start = time.time()

    # ── sources-OFF free-evolution amplitude sweep ──
    print("  ── sources-OFF free evolution (the key variable) ──", flush=True)
    off_records, off_traces = [], []
    for amp in off_amps:
        recs, tr, geo = run_free_evolution(N, PML, amp, snaps)
        off_records.append(recs)
        off_traces.append(tr)

    # ── sources-ON comparison (EXACT Phase-0 Arm-C, reused) ──
    print("\n  ── sources-ON (Arm-C: sources + nucleation gate; Phase-0 reuse) ──",
          flush=True)
    on_records, on_traces = [], []
    for amp in on_amps:
        recs, tr = run_sources_on_snapshots(N, PML, amp, on_snaps)
        on_records.append(recs)
        on_traces.append(tr)

    # ── classify ──
    per_amp = [classify_amplitude(recs, tr)
               for recs, tr in zip(off_records, off_traces)]
    verdict = classify_verdict(per_amp)

    print("\n" + "=" * 80)
    print("  GOLDILOCKS-BAND MAP  (sources-off)")
    print("=" * 80)
    print(f"  {'amp':>5} {'seed':>5} {'A²seed':>7} {'A²peak':>7} {'quasi':>6} "
          f"{'persist':>7} {'surv':>5}  seed→evolved (w1,w2)")
    for a in per_amp:
        print(f"  {a['amplitude']:>5.2f} {str(a['seed_formed']):>5} "
              f"{a['a2_seed']:>7.3f} {a['a2_peak']:>7.3f} "
              f"{str(a['quasi_stable']):>6} {str(a['persisted_past_seed']):>7} "
              f"{str(a['survived']):>5}  "
              f"({a['w1_seed']},{a['w2_seed']})→({a['w1_evolved']},{a['w2_evolved']})"
              f"  t_first_loss={a['t_first_loss']}")

    print("\n" + "=" * 80)
    print("  VERDICT")
    print("=" * 80)
    print(f"  >> VERDICT = ({verdict['verdict']})")
    print(f"     {verdict['why']}")
    print(f"  quasi-stable+formed band amps: {verdict['band_amps']}")
    print(f"  persisted-past-seed amps:      {verdict['persisted_amps']}")
    print(f"  goldilocks (survived) amps:    {verdict['goldilocks_amps']}")

    # survival curves for panel 3: the GENUINELY quasi-stable+formed band (the
    # honest sub-saturation set, NOT an amplitude cutoff — a near-wall seed can
    # self-detonate sources-off, e.g. amp 0.30). Fall back to the lowest amps if
    # the band is empty so the panel is never blank.
    survival_amps, survival_records = [], []
    for a, amp, recs in zip(per_amp, off_amps, off_records):
        if a["quasi_stable"] and a["seed_formed"]:
            survival_amps.append(amp); survival_records.append(recs)
    if not survival_amps:
        survival_amps, survival_records = off_amps[:3], off_records[:3]

    out = {
        "config": {"N": N, "PML": PML, "off_amps": off_amps, "on_amps": on_amps,
                   "snapshot_periods": snaps, "ALPHA": ALPHA, "A2_op14": A2_OP14,
                   "A2_wall": A2_WALL, "dt": DT,
                   "total_wall_s": round(time.time() - t_start, 1)},
        "sources_off": [[{k: v for k, v in r.items() if k != "_curve"} for r in recs]
                        for recs in off_records],
        "sources_off_a2_traces": [[list(p) for p in tr] for tr in off_traces],
        "sources_on": [[{k: v for k, v in r.items() if k != "_curve"} for r in recs]
                       for recs in on_records],
        "sources_on_a2_traces": [[list(p) for p in tr] for tr in on_traces],
        "per_amplitude": per_amp,
        "verdict": verdict,
        "phase0_anchor": {"armC_amp0.40_seed_A2max": 1.69,
                          "armC_amp0.40_pumped_A2max": "~6",
                          "note": "Phase-0 verdict (B): Arm-C over-saturates; "
                                  "Phase 0.5 re-tests survival sub-saturation."},
    }
    op = _HERE.parent / "r10_2_3_winding_quasistable_survival_results.json"
    op.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {op.name}", flush=True)

    fig_path = _HERE.parent / "r10_2_3_winding_quasistable_survival.png"
    plot_quasistable(off_traces, off_amps, on_traces, on_amps, per_amp,
                     verdict, survival_amps, survival_records, fig_path)
    print(f"  Saved {fig_path.name}", flush=True)
    return out


if __name__ == "__main__":
    main(smoke=("--smoke" in sys.argv))


# ══════════════════════════════════════════════════════════════════════════════
# DISCIPLINE WALK (which skills fired — ave-driver-script-honesty bookkeeping)
# ══════════════════════════════════════════════════════════════════════════════
# substrate-native-check:
#   CP1 (dynamics): writes NO solver — controls SNAPSHOT cadence on the engine's
#        own velocity-Verlet wave-propagation step. No gradient-descent / energy-
#        min construct introduced.
#   CP5 (saturation-modulated local clock): the engine's step() applies the
#        local clock ω_local(r)=ω_global·√(1−A²(r)) natively; A²max(t) is reported
#        as the saturation driver. No uniform-global-σ eigsolve is done (which
#        would miss local modes) — this is a forward time-domain read.
#   CP6 (reactance pair): BOTH stores tracked over the window — C-state A²max
#        (V_inc) AND L-state Φ²max (Phi_link) at every logged step (_a2_phi2_max).
#        A one-store snapshot can't tell quasi-static from oscillator-at-peak; the
#        pair shows whether "A²max≈const" is genuine or C-settles-while-L-grows.
#   CP7 (sampling): the extractor PML-excludes every ring point + locates the
#        shell by density crest (reused unchanged).
#   CP8 (emergence/hosting): the (2,3) is an IMPOSED PLANT — sources-off free
#        evolution is CLOSER to seed-the-precursor (no external pumping) but is
#        still a plant, NOT a grown-from-precursor hosting test. A surviving (2,3)
#        shows conservation-of-an-imposed-plant, not autonomous hosting. Flagged.
# phase-space-coordinate-check: the load-bearing winding is read in phase-space
#   Θ=2φ+3ψ (the extractor's internal U(1) phase, matching the corpus (2,3) claim
#   on the Clifford torus); A²max/Φ²max are scalars (saturation magnitude, frame-
#   free); the real-space shell (R,r) is diagnostic-only (where to walk). MATCH.
# ave-canonical-source: ALPHA from ave.core.constants; PHI/DT/COMPTON/A2_OP14
#   reused from the extractor module. A2_WALL=1.0 is the saturation kernel's own
#   rupture normalization (tagged, NOT a fresh physics literal). N/PML/amplitudes/
#   snapshot cadence are honestly-tagged ENGINEERING/config choices.
# ave-driver-script-honesty: forward READ of a KNOWN-imposed signal — NO
#   minimize/curve_fit, NO parameter tuned toward (2,3). The seed A²max∝amp²
#   scaling is a forward PREDICTION (verified, not fit). The I/II/III verdict is
#   computed from seed→evolved deltas via a TRANSPARENT printed rule.
# consistency-vs-emergence: CONSERVATION-under-free-evolution of an IMPOSED
#   control + a regime/tool characterization (does a quasi-stable band exist) —
#   CONSISTENCY class, NOT emergence; no α / hosting / CODATA claim.
# ave-evidence-framing-discipline: a (II) or (III) is a VALID, expected outcome
#   stated honestly from the data; survival is NOT pre-claimed.
