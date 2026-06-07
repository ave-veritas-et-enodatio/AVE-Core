#!/usr/bin/env python3
"""
Phase-0 diagnostic (NO new engine code): localize the V0 (2,3)-degradation to
the "2"/Cosserat-ω half (w1, MAJOR-φ winding) vs the "3"/LC half (w2, MINOR-ψ
winding) AS A FUNCTION OF EVOLUTION TIME.

Prereg (FROZEN): research/2026-06-06_cosserat-geometric-integrator-prereg.md §1
Reuses (UNMODIFIED) the validated coordinate-correct extractor + Arm-C imposed
control from r10_2_3_winding_extractor_coordinate.py.

────────────────────────────────────────────────────────────────────────────
THE QUESTION
────────────────────────────────────────────────────────────────────────────
The imposed (2,3) = 2φ + 3ψ splits across TWO engine sectors:
  • w1 / "2" (φ, n̂-direction)  = Cosserat-ω rotation, integrated by flat-ℝ³
    velocity-Verlet (cosserat_field_3d.py:1561  `self.omega = self.omega +
    dt*self.omega_dot`, half-kicks :1555-1556/:1570-1571) — the OFF-GROUP leaky
    candidate. The quaternion form is used ONLY for the observable ω→n̂
    projection (:188-192), never the integration.
    [Citation-fix flag: the prereg cites :818,825,841 for the Verlet — those are
     the state DECLARATIONS (omega/omega_dot zero-init + the Lagrangian comment);
     the actual flat-vector integration step is step_velocity_verlet :1533-1571.
     Physics claim (flat-ℝ³ Verlet integrates ω off-group) UNCHANGED.]
  • w2 / "3" (ψ, C↔L fibre)     = (V_inc,V_ref) phase, integrated by the unitary
    K4-TLM scatter+connect (lossless reactive cycling, Axiom 3) — predicted HOLD.

The extractor already reports the per-half modal coherence SEPARATELY:
  w1_base_modal_count / w1_base_n_walks   via the MAJOR-circle (φ) walk  → "2"
  w2_fibre_modal_count / w2_fibre_n_walks via the MINOR-circle (ψ) walk  → "3"
That IS the 12/12→5/12 metric, already split by axis. This driver captures it
across evolution snapshots (clean seed → evolved) and attributes the degrade.

────────────────────────────────────────────────────────────────────────────
DISCRIMINATOR (read from the numbers — NOT fit; ave-driver-script-honesty)
────────────────────────────────────────────────────────────────────────────
  (A) w1/"2" degrades, w2/"3" holds  → flat Cosserat-ω integrator IS the culprit
      → Phase 1 (SO(3)-geometric integrator) warranted.
  (B) w2/"3" ALSO degrades           → leak is in the unitary V-sector or the
      extractor-read → Phase 1 would NOT help (build saved).
  (C) neither winding INTEGER drifts off (2,3) → the 12/12→5/12 was a
      metric/threshold artifact (coherence-count softened, winding conserved),
      not a winding loss → re-examine the extractor's modal-coherence metric.

A half "loses its winding" iff its modal INTEGER drifts off the imposed value
(w1≠2 / w2≠3). The modal COHERENCE fraction (count/n_walks) is the confidence;
a coherence drop WITHOUT an integer drift is the (C) signature.

────────────────────────────────────────────────────────────────────────────
HONEST SCOPE (ave-driver-script-honesty + phase-space-coordinate-check)
────────────────────────────────────────────────────────────────────────────
The load-bearing w1/w2 are BOTH read from the SAME V_inc internal U(1) phase
Θ = 2φ+3ψ, decomposed by which torus circle is walked (major φ → w1, minor
ψ → w2). This is the PREREG's accepted proxy for the two-sector split — it is
NOT a direct read of the Cosserat-ω state array vs the TLM V-array. The closest-
to-literal sector reads (diag_nhat_w1 from the V_inc-weighted n̂-direction;
diag_CL_w2 from V_inc-vs-Phi_link reactance pair) are recorded ALONGSIDE. If
the verdict hinges on the proxy vs the literal reads diverging, this script
SAYS SO rather than silently picking one.

DISCIPLINE WALK — see module footer (substrate-native-check CP1/2/4/6/7/8 ·
phase-space-coordinate-check · ave-canonical-source · consistency-vs-emergence ·
ave-evidence-framing-discipline).
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

import r10_2_3_winding_extractor_coordinate as ext  # noqa: E402  (reuse, no new engine code)

# Substrate-derived constants — reuse the extractor's canonical values (no
# fresh literals; ave-canonical-source). COMPTON_PERIOD / DT define the
# evolution clock; PHI the golden-torus aspect.
PHI = ext.PHI
DT = ext.DT
COMPTON_PERIOD = ext.COMPTON_PERIOD
A2_OP14 = ext.A2_OP14


# ══════════════════════════════════════════════════════════════════════════════
# Snapshot sweep — reuse the UNMODIFIED Arm-C control at increasing n_periods
# ══════════════════════════════════════════════════════════════════════════════
def _coherence(rec, half):
    """Per-half modal-coherence fraction (count / n_walks) — the 12/12→5/12
    metric. half ∈ {'w1','w2'}."""
    if half == "w1":
        c, n = rec.get("w1_base_modal_count", 0), rec.get("w1_base_n_walks", 0)
    else:
        c, n = rec.get("w2_fibre_modal_count", 0), rec.get("w2_fibre_n_walks", 0)
    return (float(c) / float(n)) if n else float("nan"), int(c), int(n)


def run_snapshot_sweep(N, PML, amplitude, snapshot_periods):
    """For each n_periods k in `snapshot_periods`, re-run the UNMODIFIED Arm-C
    imposed control to time k and run the coordinate-correct extractor.

    DETERMINISM (the reuse correctness argument): the engine is built with
    temperature=0.0 (no thermal RNG) and the source schedule is in ABSOLUTE
    time, so a fresh run truncated at k periods reproduces the trajectory at
    time k bit-for-bit. We therefore reconstruct the snapshot sequence via
    independent truncated runs of the SAME validated function — zero new engine
    code, zero duplication of the local _DirSrc source subclass. The t=0
    snapshot is the pristine planted ansatz (clean-ansatz anchor: expect
    w1=2 modal ~12/12, w2=3 modal ~11/12 per the 2026-06-05 §2 validation).
    """
    records = []
    for k in snapshot_periods:
        t0 = time.time()
        eng, meta = ext._run_armC_full_field(N=N, PML=PML, n_periods=k,
                                              amplitude=amplitude)
        rec = ext._extract_on_engine(eng, N, PML, f"t{k}")
        rec["n_periods"] = int(k)
        rec["n_steps"] = int(meta.get("n_steps", 0))
        rec["wall_s"] = round(time.time() - t0, 1)
        cf1, c1, n1 = _coherence(rec, "w1")
        cf2, c2, n2 = _coherence(rec, "w2")
        rec["w1_coherence_frac"] = cf1
        rec["w2_coherence_frac"] = cf2
        records.append(rec)
        print(
            f"  t={k:>3}T  steps={rec['n_steps']:>5}  "
            f"w1='2'={rec['w1_base']} (coh {c1:>2}/{n1}, raw~{rec.get('w1_base_raw', float('nan')):.2f})   "
            f"w2='3'={rec['w2_fibre']} (coh {c2:>2}/{n2}, raw~{rec.get('w2_fibre_raw', float('nan')):.2f})   "
            f"c={rec['crossing_count_c']}   "
            f"diag[n̂={rec['diag_nhat_w1']},CL={rec['diag_CL_w2']}]   "
            f"R={rec['R']:.1f} sites={rec.get('n_shell_sites', 0)} "
            f"A²max={rec['a2_max']:.2f}  [{rec['wall_s']}s]",
            flush=True,
        )
    return records


# ══════════════════════════════════════════════════════════════════════════════
# Verdict — A / B / C from the seed→evolved deltas (NO fit; transparent rule)
# ══════════════════════════════════════════════════════════════════════════════
def classify_verdict(records, coh_floor=0.6):
    """Apply the prereg discriminator to the seed (first) vs evolved (last)
    snapshots. TRANSPARENT rule, printed in full so the verdict is auditable.

    TWO ORTHOGONAL AXES are measured per half (both reported — neither buried):
      • COHERENCE degrade — coherence_frac (modal_count/n_walks, THE 12/12→5/12
        metric the orchestrator named) falls below `coh_floor` (default 0.6,
        which cleanly separates the prereg anchors 12/12=1.00 and 5/12=0.42)
        having started above it at the seed.
      • WINDING-INTEGER loss — the modal INTEGER drifts off the imposed value
        (w1≠2 or w2≠3) at the evolved snapshot. This is the GENUINE topological
        loss; a coherence drop WITHOUT it is the prereg's (C) "metric/threshold
        artifact, not winding loss" signature.

    The A/B/C LETTER follows the COHERENCE axis (the open fork is literally a
    coherence statement, "12/12→5/12"):
      (A) w1/"2" coherence degrades, w2/"3" holds → Cosserat-ω flat-Verlet half.
      (B) w2/"3" coherence degrades (regardless of w1) → the supposedly-unitary
          V-sector half degrades — Phase 1 would NOT help.
      (C) neither coherence degrades → no degradation reproduced.

    The `genuine_winding_loss` flag then REFINES the letter: when the letter is
    A/B but NO integer drifted, the prereg's (C) clause CO-APPLIES — the
    degradation is a coherence-UNIFORMITY softening (winding charge conserved),
    not a topological leak. That (A)/(C)-boundary case is surfaced explicitly,
    NOT silently collapsed to one side (flag-don't-fix).
    """
    seed, evo = records[0], records[-1]
    w1_seed, w2_seed = seed["w1_base"], seed["w2_fibre"]
    w1_evo, w2_evo = evo["w1_base"], evo["w2_fibre"]
    cf1_seed, cf2_seed = seed["w1_coherence_frac"], seed["w2_coherence_frac"]
    cf1_evo, cf2_evo = evo["w1_coherence_frac"], evo["w2_coherence_frac"]

    w1_int_lost = (w1_evo != 2)
    w2_int_lost = (w2_evo != 3)
    w1_coh_collapse = (cf1_seed >= coh_floor) and (cf1_evo < coh_floor)
    w2_coh_collapse = (cf2_seed >= coh_floor) and (cf2_evo < coh_floor)
    genuine_winding_loss = bool(w1_int_lost or w2_int_lost)

    # A/B/C letter on the COHERENCE axis (w2 takes precedence — its degrade is
    # the headline surprise either way, per prereg (B)).
    if w2_coh_collapse or w2_int_lost:
        verdict = "B"
        why = ("the '3'/LC half (w2, unitary K4-TLM V-sector) degrades — leak is "
               "in the supposedly-unitary sector or the extractor-read; a "
               "geometric Cosserat-ω integrator would NOT fix it.")
    elif w1_coh_collapse or w1_int_lost:
        verdict = "A"
        why = ("the '2'/Cosserat-ω half (w1, flat-ℝ³ velocity-Verlet) degrades "
               "while the '3'/LC half holds — the off-group ω integrator is the "
               "culprit sector.")
    else:
        verdict = "C"
        why = ("neither half's coherence degraded below the floor — the evolved "
               "(2,3) held; the original 12/12→5/12 was NOT reproduced at this "
               "config (metric/threshold/config-sensitive).")

    # (A)/(C)-boundary refinement: localized coherence drop with integer held.
    boundary_note = ""
    if verdict in ("A", "B") and not genuine_winding_loss:
        boundary_note = (
            "(A)/(C) BOUNDARY: the winding INTEGER is CONSERVED (w1=2, w2=3) — "
            "the degrade is a coherence-UNIFORMITY softening localized to this "
            "half, NOT a topological winding LOSS. The prereg's (C) clause "
            "('12/12→5/12 a metric/threshold artifact, not winding loss') "
            "CO-APPLIES. Phase 1 would target coherence-uniformity of the "
            "localized half, not recover a lost charge.")

    return {
        "verdict": verdict, "why": why, "boundary_note": boundary_note,
        "coh_floor": coh_floor, "genuine_winding_loss": genuine_winding_loss,
        "seed": {"n_periods": seed["n_periods"], "w1": w1_seed, "w2": w2_seed,
                 "w1_coh": cf1_seed, "w2_coh": cf2_seed},
        "evolved": {"n_periods": evo["n_periods"], "w1": w1_evo, "w2": w2_evo,
                    "w1_coh": cf1_evo, "w2_coh": cf2_evo},
        "w1_winding_lost": bool(w1_int_lost), "w2_winding_lost": bool(w2_int_lost),
        "w1_coherence_collapse": bool(w1_coh_collapse),
        "w2_coherence_collapse": bool(w2_coh_collapse),
    }


# ══════════════════════════════════════════════════════════════════════════════
# Dark-aesthetic figure (repo convention: #0d1117 / #161b22 / #00ffcc)
# ══════════════════════════════════════════════════════════════════════════════
def plot_sector_evolution(records, verdict, out_path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    BG, PANEL = "#0d1117", "#161b22"
    C2, C3 = "#00ffcc", "#ff7ad9"   # "2"/Cosserat (teal) vs "3"/LC (magenta)
    CTX, GRID = "#ffb454", "#30363d"

    t = np.array([r["n_periods"] for r in records], float)
    w1 = np.array([r["w1_base"] for r in records], float)
    w2 = np.array([r["w2_fibre"] for r in records], float)
    w1raw = np.array([r.get("w1_base_raw", np.nan) for r in records], float)
    w2raw = np.array([r.get("w2_fibre_raw", np.nan) for r in records], float)
    cf1 = np.array([r["w1_coherence_frac"] for r in records], float)
    cf2 = np.array([r["w2_coherence_frac"] for r in records], float)
    cc = np.array([r["crossing_count_c"] for r in records], float)
    a2 = np.array([r["a2_max"] for r in records], float)
    sites = np.array([r.get("n_shell_sites", 0) for r in records], float)

    fig, axes = plt.subplots(3, 1, figsize=(9.5, 11), sharex=True)
    fig.patch.set_facecolor(BG)

    # ── Panel 1 — winding integers w1/"2" and w2/"3" vs evolution time ──
    ax = axes[0]
    ax.set_facecolor(PANEL)
    ax.axhline(2, color=C2, lw=0.8, ls=":", alpha=0.5)
    ax.axhline(3, color=C3, lw=0.8, ls=":", alpha=0.5)
    ax.plot(t, w1raw, color=C2, lw=1.0, alpha=0.35, ls="--")
    ax.plot(t, w2raw, color=C3, lw=1.0, alpha=0.35, ls="--")
    ax.plot(t, w1, "o-", color=C2, lw=2.2, ms=8,
            label='w1 = "2"  (φ / n̂ / Cosserat-ω · flat-Verlet)')
    ax.plot(t, w2, "s-", color=C3, lw=2.2, ms=8,
            label='w2 = "3"  (ψ / C↔L fibre · unitary K4-TLM)')
    ax.plot(t, cc, "^-", color=CTX, lw=1.4, ms=6, alpha=0.8,
            label="crossing c (derived; electron=3)")
    ax.set_ylabel("winding integer", color="#c9d1d9")
    ax.set_title(
        f"V0 (2,3)-degradation: which sector leaks under evolution?   "
        f"VERDICT = ({verdict['verdict']})",
        color="#e6edf3", fontsize=12, pad=10)
    ax.legend(facecolor=PANEL, edgecolor=GRID, labelcolor="#c9d1d9", fontsize=8.5)

    # ── Panel 2 — per-half modal coherence (the 12/12→5/12 metric) ──
    ax = axes[1]
    ax.set_facecolor(PANEL)
    ax.axhline(1.0, color="#3fb950", lw=0.8, ls=":", alpha=0.6)
    ax.axhline(5.0 / 12.0, color="#f85149", lw=0.8, ls=":", alpha=0.6)
    ax.axhline(verdict["coh_floor"], color="#8b949e", lw=0.8, ls="-.", alpha=0.5)
    ax.plot(t, cf1, "o-", color=C2, lw=2.2, ms=8, label='w1 "2" coherence')
    ax.plot(t, cf2, "s-", color=C3, lw=2.2, ms=8, label='w2 "3" coherence')
    ax.text(t[-1], 1.0, " 12/12", color="#3fb950", fontsize=8, va="bottom", ha="right")
    ax.text(t[-1], 5.0 / 12.0, " 5/12", color="#f85149", fontsize=8, va="bottom", ha="right")
    ax.text(t[-1], verdict["coh_floor"], f" floor={verdict['coh_floor']:.2f}",
            color="#8b949e", fontsize=8, va="bottom", ha="right")
    ax.set_ylim(-0.05, 1.08)
    ax.set_ylabel("modal coherence  (count / n_walks)", color="#c9d1d9")
    ax.legend(facecolor=PANEL, edgecolor=GRID, labelcolor="#c9d1d9", fontsize=8.5)

    # ── Panel 3 — confound context: shell amplitude + site count ──
    ax = axes[2]
    ax.set_facecolor(PANEL)
    ln1 = ax.plot(t, a2, "o-", color=CTX, lw=2.0, ms=7, label="A²max (saturation)")
    ax.set_ylabel("A²max", color=CTX)
    ax.tick_params(axis="y", colors=CTX)
    axb = ax.twinx()
    axb.set_facecolor("none")
    ln2 = axb.plot(t, sites, "s--", color="#79c0ff", lw=1.6, ms=6,
                   label="n_shell_sites (extractor)")
    axb.set_ylabel("n_shell_sites", color="#79c0ff")
    axb.tick_params(axis="y", colors="#79c0ff")
    ax.set_xlabel("evolution time  (Compton periods)", color="#c9d1d9")
    lns = ln1 + ln2
    ax.legend(lns, [l.get_label() for l in lns], facecolor=PANEL,
              edgecolor=GRID, labelcolor="#c9d1d9", fontsize=8.5, loc="best")

    for a in list(axes) + [axb]:
        for sp in a.spines.values():
            sp.set_color(GRID)
        a.tick_params(colors="#8b949e")
        a.grid(True, color=GRID, lw=0.5, alpha=0.4)

    fig.tight_layout()
    fig.savefig(out_path, facecolor=BG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ══════════════════════════════════════════════════════════════════════════════
def main():
    print("=" * 80, flush=True)
    print("  Phase-0 diagnostic: (2,3)-winding SECTOR evolution  (w1='2'/Cosserat "
          "vs w2='3'/LC)")
    print("  Reuses UNMODIFIED r10_2_3_winding_extractor_coordinate (no new engine code)")
    print("=" * 80, flush=True)
    print(f"  ALPHA = {ALPHA} (ave-canonical-source)   √(2α) = {A2_OP14:.4f}", flush=True)

    # Match the original V0 config EXACTLY (N=48, PML=4, amp=0.40, up to 40T)
    # so the seed reproduces the clean-ansatz anchor and t=40 reproduces the
    # prior evolved read. Snapshot cadence resolves WHERE the degrade sets in.
    N, PML, amp = 48, 4, 0.40
    snapshot_periods = [0, 2, 5, 10, 20, 40]
    print(f"  config: N={N} PML={PML} amplitude={amp}  "
          f"snapshots(T)={snapshot_periods}\n", flush=True)

    t_start = time.time()
    records = run_snapshot_sweep(N, PML, amp, snapshot_periods)
    verdict = classify_verdict(records)

    print("\n" + "=" * 80)
    print("  VERDICT")
    print("=" * 80)
    s, e = verdict["seed"], verdict["evolved"]
    print(f"  seed (t={s['n_periods']}T):     w1='2'={s['w1']} (coh {s['w1_coh']:.2f})   "
          f"w2='3'={s['w2']} (coh {s['w2_coh']:.2f})")
    print(f"  evolved (t={e['n_periods']}T):  w1='2'={e['w1']} (coh {e['w1_coh']:.2f})   "
          f"w2='3'={e['w2']} (coh {e['w2_coh']:.2f})")
    print(f"  w1 winding-integer lost: {verdict['w1_winding_lost']}   "
          f"w1 coherence collapse: {verdict['w1_coherence_collapse']}")
    print(f"  w2 winding-integer lost: {verdict['w2_winding_lost']}   "
          f"w2 coherence collapse: {verdict['w2_coherence_collapse']}")
    print(f"  genuine winding loss (any integer drift): {verdict['genuine_winding_loss']}")
    print(f"\n  >> VERDICT = ({verdict['verdict']})")
    print(f"     {verdict['why']}")
    if verdict["boundary_note"]:
        print(f"     {verdict['boundary_note']}")
    # Phase 1 is cleanly warranted only by (A) WITH a genuine winding loss in
    # the Cosserat half. (A)-at-the-boundary (coherence-only) is a weaker,
    # adjudication-required signal; (B)/(C) do not warrant the build.
    if verdict["verdict"] == "A" and verdict["genuine_winding_loss"]:
        p1 = "YES (clean: Cosserat half loses winding integer)"
    elif verdict["verdict"] == "A":
        p1 = ("ADJUDICATION-REQUIRED (Cosserat-half coherence softens but winding "
              "integer conserved — weak signal; Grant/auditor call)")
    else:
        p1 = "NO"
    print(f"\n  Phase-1 (SO(3)-geometric integrator) warranted: {p1}", flush=True)

    out = {
        "config": {"N": N, "PML": PML, "amplitude": amp,
                   "snapshot_periods": snapshot_periods, "ALPHA": ALPHA,
                   "A2_op14": A2_OP14, "dt": DT,
                   "total_wall_s": round(time.time() - t_start, 1)},
        "snapshots": [{k: v for k, v in r.items()
                       if k not in ("_curve",)} for r in records],
        "verdict": verdict,
        "anchors": {
            "clean_ansatz_2026_06_05": {"w1": 2, "w1_modal": "12/12",
                                        "w2": 3, "w2_modal": "11/12"},
            "note": ("prereg open-fork: clean-ansatz coherence 12/12 degrades "
                     "to 5/12 on the evolved field; THIS run localizes which "
                     "half + when."),
        },
    }
    op = _HERE.parent / "r10_2_3_winding_sector_evolution_diagnostic_results.json"
    op.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {op.name}", flush=True)

    fig_path = _HERE.parent / "r10_2_3_winding_sector_evolution_diagnostic.png"
    plot_sector_evolution(records, verdict, fig_path)
    print(f"  Saved {fig_path.name}", flush=True)
    return out


if __name__ == "__main__":
    main()


# ══════════════════════════════════════════════════════════════════════════════
# DISCIPLINE WALK (which skills fired — ave-driver-script-honesty bookkeeping)
# ══════════════════════════════════════════════════════════════════════════════
# substrate-native-check:
#   CP1 (dynamics): this driver writes NO solver — it controls SNAPSHOT CADENCE
#        on the engine's own velocity-Verlet wave-propagation step
#        (step_velocity_verlet); it does NOT introduce any gradient-descent /
#        energy-minimization construct. The leaky-candidate IS the Verlet ω-add
#        (:1561); we DIAGNOSE it, we do not (here) change it.
#   CP2 (sector): the (2,3) splits V-sector (K4-TLM, unitary) × Cos-sector
#        (Cosserat-ω, Verlet). w1='2'=Cos (leaky candidate), w2='3'=V (holds).
#   CP4 (phase-space vs real-space): the load-bearing winding is read in the
#        phase-space internal U(1) phase Θ=2φ+3ψ (matching the corpus claim);
#        the torus CIRCLE it is walked on is located in real-space from |V_inc|²
#        density crest. Hybrid is the VALIDATED extractor design (recovers 2,3 on
#        the clean ansatz); flagged, not silently assumed.
#   CP6 (reactance pair): both halves recorded — V_inc (C-state) drives the
#        load-bearing w1/w2 + diag_nhat_w1; Phi_link (L-state) drives diag_CL_w2.
#        (diag_CL is degenerate at the seed: the ansatz plants V_inc≡Phi_link in
#        phase, so diag_CL only sharpens as Phi_link develops quadrature.)
#   CP7 (sampling): the extractor PML-excludes every ring point and locates the
#        shell by density CREST (peak), not centroid — reused unchanged.
#   CP8 (emergence/hosting): N/A — the (2,3) is IMPOSED by construction; this is a
#        winding-CONSERVATION-under-evolution diagnostic, NOT a hosting test.
# phase-space-coordinate-check: corpus claim (2,3) lives in phase-space Θ on the
#   Clifford torus; the test reads Θ winding (major→w1, minor→w2). MATCH on the
#   winding observable. The "2"↔Cosserat / "3"↔LC sector attribution is the
#   prereg's accepted spatial-circle proxy — NOT a direct ω-array vs V-array read;
#   the literal-sector diagnostics (diag_nhat_w1, diag_CL_w2) are reported so a
#   proxy/literal divergence is VISIBLE.
# ave-canonical-source: ALPHA imported from ave.core.constants; PHI/DT/COMPTON
#   reused from the extractor module. No fresh physics literals. (N, PML,
#   amplitude, snapshot cadence are honestly-tagged ENGINEERING/config choices.)
# ave-driver-script-honesty: forward READ of a KNOWN-imposed signal — NO
#   minimize/curve_fit, NO parameter tuned toward (2,3). The verdict is computed
#   from seed→evolved deltas via a TRANSPARENT printed rule (classify_verdict),
#   not hand-set.
# consistency-vs-emergence: TOOL/integrator diagnostic on an IMPOSED control —
#   CONSISTENCY class, NOT emergence; no α / hosting / CODATA claim.
# ave-evidence-framing-discipline: the verdict A/B/C is stated from the data;
#   per the prereg pre-commitment, (B)/(C) honestly REFUTE the integrator
#   hypothesis (a valid, expected outcome) and Phase 1 is NOT built unless (A).
