"""genesis_24_saturated_seed.py — GAP-1 saturated-seed test (genesis-24).

Prereg (FROZEN — GO, Lane 1):
    research/2026-06-09_genesis-24-saturated-seed_prereg.md
Lineage: direct successor to genesis-23 (reflection_genesis_23_self_assembly.py).
This driver REUSES every genesis-23 extractor / seeder / engine-factory
(_phase_space_winding, _beltrami_helicity_total, _seed_v_partner, _make_engine,
_seed_photon, _localization, _spin_L, _v_sector_state, _hamiltonian, _interior) —
NO new physics machinery. It adds only an ARM HARNESS + the non-circular SEED-AUDIT
+ the frozen HEADLINE (dE_V) + the Smith-Γ reads + the 5 figures.

CANONICAL-AVE-ONLY (prereg §0, Grant directive 2026-06-09):
  Absorb/emit IS the Axiom-4 saturation engage/relax cycle on the bond LC tank.
  The "3" is the REAL Heaviside/Gibbs-excised longitudinal V-sector (physical,
  present in a mass). ZERO QED / Maxwell-vector framing anywhere.

NON-CIRCULAR SEED (prereg §4): direct-write k4.V_inc via _seed_v_partner
  (circularly-polarized in-plane V-vector, amp = frac·V_SNAP, A²_V = frac²),
  Cosserat ω EMPTY (H_bel = 0, charge-neutral), NO θ=2φ+3ψ knot. On the Smith
  chart: an INTERMEDIATE off-center Γ (set by frac), NOT the Γ=−1 rim.
FORBIDDEN (auto-VOID): initialize_electron_2_3_sector /
  initialize_2_3_torus_knot_sector — those PLANT the knot (= seed AT the rim).

HEADLINE (frozen, prereg §6): dE_V = E_V(photon-ON Arm-1) − E_V(no-photon Arm-2),
  PAIRED with the de-novo (V_inc,V_ref) phase-space winding (w_tor,w_pol)→(2,3).
  max|V_inc|≠0 is NOT the headline (trivially true for any legitimate seed — the
  circularity trap).

Run:  PYTHONPATH=src .../python src/scripts/vol_1_foundations/genesis_24_saturated_seed.py
Env:  GEN24_N (24), GEN24_STEPS (40), GEN24_EMIT_STEPS (60), GEN24_SMOKE_ONLY (0/1)
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

# ── geometry env (propagate to the genesis-23 module BEFORE importing it, so its
#    module-level N / CENTER / seeder geometry match genesis-24) ───────────────
GEN24_N = os.environ.get("GEN24_N", "24")
GEN24_STEPS = int(os.environ.get("GEN24_STEPS", "40"))
GEN24_EMIT_STEPS = int(os.environ.get("GEN24_EMIT_STEPS", "60"))
SMOKE_ONLY = os.environ.get("GEN24_SMOKE_ONLY", "0") == "1"
os.environ.setdefault("GEN23_N", GEN24_N)
os.environ.setdefault("GEN23_STEPS", str(GEN24_STEPS))

# ── import the genesis-23 module by path (reuse ALL its machinery) ────────────
_g23_path = os.path.join(HERE, "reflection_genesis_23_self_assembly.py")
_spec = importlib.util.spec_from_file_location("genesis23", _g23_path)
g23 = importlib.util.module_from_spec(_spec)
sys.modules["genesis23"] = g23
_spec.loader.exec_module(g23)

# Canonical constants ONLY (ave-canonical-source) — no hard-coded physics.
from ave.core.constants import ALPHA, R_I, V_SNAP, V_YIELD  # noqa: E402

# ── FORBIDDEN-SEEDER STATIC GUARD (auto-VOID, prereg §4) ──────────────────────
# This module must never reference the knot planters. (Static assertion: the
# only seeder used is g23._seed_v_partner / g23._seed_photon.)
_FORBIDDEN = ("initialize_electron_2_3_sector", "initialize_2_3_torus_knot_sector")

N = g23.N
CENTER = g23.CENTER
SIGMA, LAM = g23.SIGMA, g23.LAM
A_PHOTON = g23.A_LOCK          # verdict-II energize+LOCK |ω| (soft-moderate wall)
FRACS = (0.30, 0.60, 0.85, 0.95)
DEEP_FRACS = (0.85, 0.95)      # deep-saturation reproduction band (prereg §7 B-guard)
EPS_MACHINE = 1e-9             # FROZEN pre-run: dE_V floor (natural V_SNAP² units)
OMEGA_0 = 2.0 * np.pi / LAM    # carrier (matches the photon wavelength) — Arm-5 pump
PUMP_FRAC_AMP = 0.20           # Arm-5 CW free-work drive amplitude (V_SNAP units)


# ──────────────────────────────────────────────────────────────────────────
# Reads (ALL via reused g23 extractors + engine accessors — no new machinery)
# ──────────────────────────────────────────────────────────────────────────
def _E_V(eng) -> float:
    """V-sector energy E_V = Σ_interior V_inc² (the '3' energization). Reuses
    g23._v_sector_state (PML-excluded, active-masked)."""
    return g23._v_sector_state(eng)["V_sq_sum"]


def _gamma_stats(eng) -> dict:
    """Smith-chart Γ = (Z_eff−1)/(Z_eff+1) over interior-alive cells (the Op3
    reflection map / engine-native operating point). Γ<0 = μ-side short (toward
    the Γ=−1 rim = the electron); Γ>0 = ε-side open (the off-center seed side).
    Reuses g23._interior + the engine's _impedance_gamma_shared."""
    g = eng._coupled._impedance_gamma_shared()
    alive = eng.cos.mask_alive & g23._interior(eng)
    gi = g[alive]
    if gi.size == 0:
        return {"gamma_min": 0.0, "gamma_mean": 0.0, "gamma_max": 0.0, "frac_short": 0.0}
    return {
        "gamma_min": float(gi.min()),
        "gamma_mean": float(gi.mean()),
        "gamma_max": float(gi.max()),
        "frac_short": float((gi < -0.05).mean()),
    }


def _vref_over_vinc(eng) -> float:
    """Phase-space Γ = ⟨|V_ref/V_inc|⟩ per cell (A46 native), where V_inc is
    populated. The dynamical realization of the Op3 reflection map."""
    Vi = np.asarray(eng.k4.V_inc)
    Vr = np.asarray(eng.k4.V_ref)
    m = (eng.k4.mask_active[..., None]) & (np.abs(Vi) > 1e-6)
    if not m.any():
        return 0.0
    return float(np.mean(np.abs(Vr[m] / Vi[m])))


# ──────────────────────────────────────────────────────────────────────────
# STEP 3 — t=0 SEED-AUDIT CERTIFICATE (prereg §4 / §9 CP8)
# ──────────────────────────────────────────────────────────────────────────
def _seed_audit(frac: float) -> dict:
    """The BARE V-seed (no photon, Cosserat ω EMPTY) — the exact Arm-2 initial
    condition — must be ADMISSIBLE:
      vinc_closes_23=False AND vref_closes_23=False (no de-novo (2,3) in either
      phase-space sector) AND ω-(2,3) absent (ω field empty) AND |H_bel|~0
      (charge-neutral). A non-admissible seed VOIDS that frac (C2)."""
    eng = g23._make_engine(emf=True)
    g23._seed_v_partner(eng, frac=frac)              # direct-write V_inc; ω stays 0
    ps = g23._phase_space_winding(eng, CENTER)
    hbel = g23._beltrami_helicity_total(eng)
    c_omega = int(eng.cos.extract_crossing_count())  # ω real-space winding
    omega_max = float(np.abs(np.asarray(eng.cos.omega)).max())
    vs = g23._v_sector_state(eng)
    admissible = bool(
        (not ps["vinc_closes_23"])
        and (not ps["vref_closes_23"])
        and (omega_max < 1e-12)                      # ω sector provably empty → ω-(2,3) absent
        and (abs(hbel) < 1e-9)
    )
    return {
        "frac": frac,
        "admissible": admissible,
        "vinc_closes_23": bool(ps["vinc_closes_23"]),
        "vref_closes_23": bool(ps["vref_closes_23"]),
        "vinc_w_tor": ps.get("vinc_w_tor"),
        "vinc_w_pol": ps.get("vinc_w_pol"),
        "vref_amp": ps["vref_amp"],
        "omega_crossing_c": c_omega,
        "omega_max": omega_max,
        "H_bel": hbel,
        "max_V_inc": vs["max_V_inc"],
        "E_V_seed": vs["V_sq_sum"],
    }


# ──────────────────────────────────────────────────────────────────────────
# Arm construction + per-step reactance-pair recording (A-Rule-10)
# ──────────────────────────────────────────────────────────────────────────
def _build_arm(arm: int, frac: float):
    """Engine + IC per arm. emf=True (the ω→V EMF reciprocal k4_cosserat_coupling
    :703 is the source channel — dead at V=0, live at V≠0). Impedance boundary ON
    (verdict-II self-trap = the Smith-Γ wall). use_asymmetric_saturation=True
    (default; the κ_chiral·h photon ω is the wall, the V-seed biases the EMF)."""
    eng = g23._make_engine(emf=True)
    if arm == 1:        # seed + photon (+h)
        g23._seed_v_partner(eng, frac=frac)
        g23._seed_photon(eng, A_PHOTON, +1.0)
    elif arm == 2:      # SAME seed, NO photon (DECISIVE control)
        g23._seed_v_partner(eng, frac=frac)
    elif arm == 3:      # no seed + photon (= genesis-23 null; frac-independent)
        g23._seed_photon(eng, A_PHOTON, +1.0)
    elif arm == 4:      # seed + OPPOSITE-helicity photon (−h)
        g23._seed_v_partner(eng, frac=frac)
        g23._seed_photon(eng, A_PHOTON, -1.0)
    elif arm == 5:      # CW free-work pump on the V-tank (Class-C discriminator)
        g23._seed_v_partner(eng, frac=frac)
        from ave.topological.vacuum_engine import CWSource
        x0 = int(round(CENTER[0]))
        eng.add_source(
            CWSource(
                x0=x0, direction=(1, 0, 0), amplitude=PUMP_FRAC_AMP, omega=OMEGA_0,
                sigma_yz=SIGMA, t_ramp=4, t_sustain=10**6,
            )
        )
    else:
        raise ValueError(f"unknown arm {arm}")
    return eng


def _run24(eng, nsteps: int) -> list[dict]:
    """Step the coupled engine; record the FULL reactance PAIR EVERY step
    (A-Rule-10): C-state (max|V_inc|, E_V=ΣV_inc², |ω|max) AND L-state
    (max|Φ_link|, |ω̇|max), plus the conservation ledger (H, H_bel, |L|) and the
    Smith-Γ. A single snapshot cannot distinguish a held seed from an oscillator
    caught at peak, nor energize-LOCK from a secular pump — hence every step."""
    tr = []
    for t in range(nsteps):
        eng.step()
        vs = g23._v_sector_state(eng)
        gs = _gamma_stats(eng)
        tr.append({
            "t": t,
            "max_V_inc": vs["max_V_inc"],                                  # C-state
            "E_V": vs["V_sq_sum"],                                         # C-state (energy)
            "max_Phi_link": vs["max_Phi_link"],                            # L-state (reactance pair)
            "omega_C": float(np.abs(np.asarray(eng.cos.omega)).max()),     # C-state (ω)
            "omega_dot_L": float(np.abs(np.asarray(eng.cos.omega_dot)).max()),  # L-state (ω̇)
            "H": g23._hamiltonian(eng),                                    # ledger: energy
            "H_bel": g23._beltrami_helicity_total(eng),                    # ledger: charge
            "L_spin": g23._spin_L(eng),                                    # ledger: spin
            "gamma_min": gs["gamma_min"],
            "gamma_mean": gs["gamma_mean"],
        })
    return tr


def _run_arm(arm: int, frac: float, nsteps: int) -> dict:
    """Build → measure t=0 → evolve → measure peak. Winding measured in
    (V_inc,V_ref) phase-space (A46), sampled around the |ω|² density-peak (CP7)."""
    eng = _build_arm(arm, frac)
    ps0 = g23._phase_space_winding(eng, CENTER)        # t=0 (seed-start) winding
    g0 = _gamma_stats(eng)
    ev0 = _E_V(eng)
    tr = _run24(eng, nsteps)
    _, pk = g23._localization(eng)                     # density-peak (CP7), PML-excluded
    ps1 = g23._phase_space_winding(eng, pk)            # peak winding
    g1 = _gamma_stats(eng)
    ev1 = _E_V(eng)
    return {
        "arm": arm, "frac": frac, "eng": eng, "trace": tr, "peak": [int(x) for x in pk],
        "E_V0": ev0, "E_V": ev1,
        "ps0": ps0, "ps1": ps1, "gamma0": g0, "gamma1": g1,
        "H_bel": g23._beltrami_helicity_total(eng), "L_spin": g23._spin_L(eng),
        "vref_over_vinc": _vref_over_vinc(eng),
        "H_series": [r["H"] for r in tr],
        "EV_series": [r["E_V"] for r in tr],
        "Vinc_series": [r["max_V_inc"] for r in tr],
        "Phi_series": [r["max_Phi_link"] for r in tr],
        "L_series": [r["L_spin"] for r in tr],
        "Hbel_series": [r["H_bel"] for r in tr],
        "gmin_series": [r["gamma_min"] for r in tr],
    }


_CACHE: dict = {}


def arm_result(arm: int, frac: float, nsteps: int) -> dict:
    key = (arm, frac if arm != 3 else "noseed", nsteps)  # arm-3 is frac-independent
    if key not in _CACHE:
        _CACHE[key] = _run_arm(arm, frac, nsteps)
    return _CACHE[key]


def _ledger_closes(res: dict) -> dict:
    """ENERGY (H ~conserved, no H_drift), CHARGE (H_bel bounded), SPIN (|L|
    bounded precession, NOT |L|~t). Energize-LOCK, not secular pump."""
    H = np.asarray(res["H_series"], dtype=float)
    L = np.asarray(res["L_series"], dtype=float)
    Vi = np.asarray(res["Vinc_series"], dtype=float)
    H0 = abs(H[0]) if H.size and abs(H[0]) > 1e-30 else 1.0
    H_drift = float((H[-1] - H[0]) / H0) if H.size else 0.0
    H_span = float((H.max() - H.min()) / H0) if H.size else 0.0
    # secular V growth tell: last-quarter mean / first-quarter mean
    q = max(1, len(Vi) // 4)
    v_secular = float(Vi[-q:].mean() / max(Vi[:q].mean(), 1e-30)) if Vi.size else 1.0
    L_bounded = bool(L.max() < 5.0 * max(L[0], 1e-30)) if L.size else True
    return {
        "H_drift": H_drift, "H_span": H_span, "v_secular_ratio": v_secular,
        "L_bounded": L_bounded,
        "closes": bool(abs(H_drift) < 0.05 and L_bounded and v_secular < 3.0),
    }


# ──────────────────────────────────────────────────────────────────────────
# Figures (prereg §8) — savefig genesis24_fig{1..5}_*.png
# ──────────────────────────────────────────────────────────────────────────
def _make_figures(out, matrix, emit) -> dict:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    paths = {}
    cols = {0.30: "C0", 0.60: "C1", 0.85: "C2", 0.95: "C3"}

    # FIG 1 — dE_V(t) per frac: E_V(Arm-1) − E_V(Arm-2) over the absorb window
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.8))
    for f in FRACS:
        a1 = matrix[(1, f)]; a2 = matrix[(2, f)]
        ev1 = np.asarray(a1["EV_series"]); ev2 = np.asarray(a2["EV_series"])
        ts = np.arange(len(ev1))
        ax[0].plot(ts, ev1, "-", color=cols[f], label=f"frac={f} Arm-1 (photon)")
        ax[0].plot(ts, ev2, "--", color=cols[f], alpha=0.6, label=f"frac={f} Arm-2 (control)")
        ax[1].plot(ts, ev1 - ev2, "-", color=cols[f], label=f"frac={f}")
    ax[0].set_xlabel("step"); ax[0].set_ylabel("E_V = Σ V_inc²")
    ax[0].set_title("V-sector energy: photon-ON vs no-photon control"); ax[0].legend(fontsize=7)
    ax[1].axhline(0, color="k", lw=0.8); ax[1].axhline(EPS_MACHINE, color="r", ls=":", lw=0.8, label="eps_machine")
    ax[1].set_xlabel("step"); ax[1].set_ylabel("dE_V = E_V(ON) − E_V(ctrl)")
    ax[1].set_title("HEADLINE: photon-attributable dE_V(t)"); ax[1].legend(fontsize=7)
    fig.suptitle("FIG 1 — dE_V headline (photon-attributable V-sector energization)")
    fig.tight_layout()
    p = os.path.join(HERE, "genesis24_fig1_dEV_headline.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig1"] = p

    # FIG 2 — SMITH CHART: Γ operating point, seed-start vs Arm-1 peak vs Arm-2 end
    fig, ax = plt.subplots(figsize=(7.2, 7.0))
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(th), np.sin(th), "k-", lw=1.0)
    ax.plot(0, 0, "k+", ms=12); ax.annotate("Γ=0 (photon / matched)", (0.02, 0.02), fontsize=8)
    ax.plot(-1, 0, "rs", ms=10); ax.annotate("Γ=−1 (electron rim)", (-0.98, -0.10), fontsize=8, color="r")
    for f in FRACS:
        a1 = matrix[(1, f)]; a2 = matrix[(2, f)]
        gs = a1["gamma0"]["gamma_min"]   # seed-start (off-center, t=0)
        g1 = a1["gamma1"]["gamma_min"]   # Arm-1 photon-driven end
        g2 = a2["gamma1"]["gamma_min"]   # Arm-2 control end
        ax.plot(gs, 0, "o", color=cols[f], ms=9)
        ax.annotate(f"seed {f}", (gs, 0.04 + 0.05 * list(FRACS).index(f)), fontsize=7, color=cols[f])
        ax.annotate("", xy=(g1, -0.06), xytext=(gs, 0),
                    arrowprops=dict(arrowstyle="->", color=cols[f], lw=1.6))
        ax.plot(g1, -0.06, "*", color=cols[f], ms=13)
        ax.plot(g2, 0.06, "x", color=cols[f], ms=9)
    ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15); ax.set_aspect("equal")
    ax.set_xlabel("Re Γ  (Γ_min over interior)"); ax.set_ylabel("(plotting offset only)")
    ax.set_title("FIG 2 — Smith chart: does the PHOTON drive seed→Γ=−1 rim?\n"
                 "o=seed t=0  ✷=Arm-1 photon-end  ✕=Arm-2 control-end")
    fig.tight_layout()
    p = os.path.join(HERE, "genesis24_fig2_smith_chart.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig2"] = p

    # FIG 3 — reactance-pair trajectory: C-state (max|V_inc|) vs L-state (max|Φ_link|)
    fig, ax = plt.subplots(1, 2, figsize=(13, 4.8))
    for f in FRACS:
        a1 = matrix[(1, f)]
        ax[0].plot(a1["Vinc_series"], a1["Phi_series"], "-", color=cols[f], label=f"frac={f}")
        ax[0].plot(a1["Vinc_series"][0], a1["Phi_series"][0], "o", color=cols[f])
    ax[0].set_xlabel("C-state  max|V_inc|"); ax[0].set_ylabel("L-state  max|Φ_link|")
    ax[0].set_title("Arm-1 reactance pair (energize-LOCK = closed loop;\nsecular pump = open spiral)")
    ax[0].legend(fontsize=7)
    # Arm-1 vs Arm-5 (pump) secular-V tell at deepest frac
    f = 0.95
    a1 = matrix[(1, f)]; a5 = matrix[(5, f)]
    ax[1].plot(a1["Vinc_series"], "-", color="C2", label="Arm-1 (finite photon)")
    ax[1].plot(a5["Vinc_series"], "--", color="C3", label="Arm-5 (CW free-work pump)")
    ax[1].set_xlabel("step"); ax[1].set_ylabel("max|V_inc|")
    ax[1].set_title(f"frac={f}: LOCK (bounded) vs PUMP (secular |V|~t → Class C)")
    ax[1].legend(fontsize=8)
    fig.suptitle("FIG 3 — reactance-pair (A-Rule-10): energize-LOCK vs secular pump")
    fig.tight_layout()
    p = os.path.join(HERE, "genesis24_fig3_reactance_pair.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig3"] = p

    # FIG 4 — conservation ledger H, H_bel, |L| over the (Arm-1) window
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.4))
    for f in FRACS:
        a1 = matrix[(1, f)]; ts = np.arange(len(a1["H_series"]))
        ax[0].plot(ts, a1["H_series"], "-", color=cols[f], label=f"frac={f}")
        ax[1].plot(ts, a1["Hbel_series"], "-", color=cols[f])
        ax[2].plot(ts, a1["L_series"], "-", color=cols[f])
    ax[0].set_title("H (energy) — flat = no H_drift"); ax[0].set_xlabel("step"); ax[0].legend(fontsize=7)
    ax[1].set_title("H_bel (charge) — bounded = energized+LOCKED"); ax[1].set_xlabel("step")
    ax[2].set_title("|L| (spin) — bounded precession, not |L|~t"); ax[2].set_xlabel("step")
    fig.suptitle("FIG 4 — conservation ledger (Arm-1): energize-LOCK, not pump")
    fig.tight_layout()
    p = os.path.join(HERE, "genesis24_fig4_ledger.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig4"] = p

    # FIG 5 — Arm-4 charge sign: final H_bel (+h photon) vs (−h photon) per frac
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    xs = np.arange(len(FRACS)); w = 0.36
    hp = [matrix[(1, f)]["H_bel"] for f in FRACS]
    hm = [matrix[(4, f)]["H_bel"] for f in FRACS]
    ax.bar(xs - w / 2, hp, w, color="C0", label="Arm-1  +h photon")
    ax.bar(xs + w / 2, hm, w, color="C3", label="Arm-4  −h photon")
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xticks(xs); ax.set_xticklabels([str(f) for f in FRACS]); ax.set_xlabel("seed frac")
    ax.set_ylabel("final integrated Beltrami H_bel")
    ax.set_title("FIG 5 — Arm-4 charge sign-flip (provenance certificate)")
    ax.legend()
    fig.tight_layout()
    p = os.path.join(HERE, "genesis24_fig5_arm4_charge_flip.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig5"] = p
    return paths


# ──────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────
def main():
    g23._canonical_source_gate()
    # forbidden-seeder static guard (auto-VOID if violated). Detects an actual
    # CALL (name immediately followed by "("), NOT the docstring/tuple mention.
    _src = open(os.path.abspath(__file__)).read()
    used_forbidden = [f for f in _FORBIDDEN if f"{f}(" in _src]
    out = {
        "config": {"N": N, "steps": GEN24_STEPS, "emit_steps": GEN24_EMIT_STEPS,
                   "A_photon": A_PHOTON, "fracs": list(FRACS), "eps_machine": EPS_MACHINE,
                   "omega_0": OMEGA_0, "pump_amp": PUMP_FRAC_AMP,
                   "V_SNAP": V_SNAP, "V_YIELD": V_YIELD, "R_I": R_I, "alpha": ALPHA},
        "forbidden_seeder_used": used_forbidden,
    }
    print("=" * 84)
    print("GENESIS-24 — saturated-seed test of GAP-1 (non-circular V-seed + photon)")
    print(f"  N={N} steps={GEN24_STEPS} | A_photon={A_PHOTON} | eps_machine={EPS_MACHINE:.0e}")
    print(f"  canonical: V_SNAP(SI)={V_SNAP:.0f}  V_YIELD={V_YIELD:.0f}  R_I={R_I:.4f}  α={ALPHA:.6e}")
    print(f"  FORBIDDEN seeders referenced: {used_forbidden} (must be [])")
    print("=" * 84)

    # ── STEP 3: SEED-AUDIT CERTIFICATE (all fracs, t=0, BEFORE evolving) ──
    print("\n[STEP 3 — SEED-AUDIT CERTIFICATE] (bare V-seed, ω EMPTY; admissible iff no t=0 (2,3))")
    audits = {f: _seed_audit(f) for f in FRACS}
    out["seed_audit"] = audits
    all_admissible = all(a["admissible"] for a in audits.values())
    for f, a in audits.items():
        print(f"  frac={f}: admissible={a['admissible']}  vinc_closes_23={a['vinc_closes_23']} "
              f"vref_closes_23={a['vref_closes_23']}  ω_c={a['omega_crossing_c']} ω_max={a['omega_max']:.1e} "
              f"|H_bel|={abs(a['H_bel']):.1e}  E_V_seed={a['E_V_seed']:.3e}")
    out["seed_audit_all_admissible"] = bool(all_admissible)
    print(f"  ALL seeds admissible: {all_admissible}")

    # ── STEP 4: SMOKE (frac=0.85, Arm-1 vs Arm-2) — Rule 10 early validation ──
    print("\n[STEP 4 — SMOKE] frac=0.85  Arm-1 (seed+photon) vs Arm-2 (seed, no photon)")
    a1s = arm_result(1, 0.85, GEN24_STEPS)
    a2s = arm_result(2, 0.85, GEN24_STEPS)
    dEV_smoke = a1s["E_V"] - a2s["E_V"]
    smoke_C1 = dEV_smoke <= EPS_MACHINE
    out["smoke"] = {"frac": 0.85, "E_V_arm1": a1s["E_V"], "E_V_arm2": a2s["E_V"],
                    "dE_V": dEV_smoke, "is_C1": bool(smoke_C1)}
    print(f"  E_V(Arm-1)={a1s['E_V']:.4e}  E_V(Arm-2)={a2s['E_V']:.4e}  dE_V={dEV_smoke:.4e}")
    print(f"  smoke C1 (dE_V<=eps_machine)?  {smoke_C1}")
    if smoke_C1:
        print("  >>> SMOKE indicates C1 (source-level dead even at deep saturation). "
              "Proceeding to full matrix for complete diagnostics (per structured-output needs).")

    if SMOKE_ONLY:
        out["mode"] = "SMOKE_ONLY"
        jpath = os.path.join(HERE, "genesis_24_saturated_seed_results.json")
        with open(jpath, "w") as fh:
            json.dump(out, fh, indent=2, default=float)
        print(f"\n[SMOKE_ONLY] results: {jpath}")
        return out

    # ── STEP 5: FULL MATRIX  arms {1,2,3,4,5} × fracs ──
    print("\n[STEP 5 — FULL MATRIX] arms {1,2,3,4,5} × fracs {0.30,0.60,0.85,0.95}")
    matrix = {}
    for f in FRACS:
        for arm in (1, 2, 3, 4, 5):
            res = arm_result(arm, f, GEN24_STEPS)
            matrix[(arm, f)] = res
        dEV = matrix[(1, f)]["E_V"] - matrix[(2, f)]["E_V"]
        p1 = matrix[(1, f)]["ps1"]; p2 = matrix[(2, f)]["ps1"]
        print(f"  frac={f}: dE_V={dEV:.4e}  | Arm-1 (w_tor,w_pol)=("
              f"{p1.get('vinc_w_tor')},{p1.get('vinc_w_pol')}) closes23={p1['vinc_closes_23'] or p1['vref_closes_23']}"
              f"  | Arm-2 closes23={p2['vinc_closes_23'] or p2['vref_closes_23']}  "
              f"Γ: seed={matrix[(1,f)]['gamma0']['gamma_min']:+.3f}→Arm1={matrix[(1,f)]['gamma1']['gamma_min']:+.3f} "
              f"Arm2={matrix[(2,f)]['gamma1']['gamma_min']:+.3f}")

    # ── headline dE_V per frac + monotonicity ──
    dEV = {f: matrix[(1, f)]["E_V"] - matrix[(2, f)]["E_V"] for f in FRACS}
    vals = [dEV[f] for f in FRACS]
    monotone = all(vals[i] <= vals[i + 1] + 1e-12 for i in range(len(vals) - 1))
    deep_pos = all(dEV[f] > EPS_MACHINE for f in DEEP_FRACS)
    out["headline_dEV"] = {str(f): dEV[f] for f in FRACS}
    out["headline_monotone"] = bool(monotone)
    out["headline_deep_positive"] = bool(deep_pos)

    # ── winding per frac (t=0 vs peak), Arm-1 ──
    out["winding"] = {}
    three_closes_deep = False
    for f in FRACS:
        p0 = matrix[(1, f)]["ps0"]; p1 = matrix[(1, f)]["ps1"]
        closes = bool(p1["vinc_closes_23"] or p1["vref_closes_23"])
        if f in DEEP_FRACS and closes:
            three_closes_deep = True
        out["winding"][str(f)] = {
            "t0": {"w_tor": p0.get("vinc_w_tor"), "w_pol": p0.get("vinc_w_pol"),
                   "closes23": bool(p0["vinc_closes_23"] or p0["vref_closes_23"])},
            "peak": {"w_tor": p1.get("vinc_w_tor"), "w_pol": p1.get("vinc_w_pol"),
                     "vinc_rel_pol": p1.get("vinc_rel_pol"), "closes23": closes},
        }

    # ── Arm-2 decisive control: must be null in BOTH source and topology ──
    arm2_topology_null = all(
        not (matrix[(2, f)]["ps1"]["vinc_closes_23"] or matrix[(2, f)]["ps1"]["vref_closes_23"])
        for f in FRACS
    )
    out["arm2_topology_null"] = bool(arm2_topology_null)
    out["arm2_EV_growth"] = {
        str(f): (matrix[(2, f)]["E_V"] / max(audits[f]["E_V_seed"], 1e-30)) for f in FRACS
    }

    # ── Arm-3 (= genesis-23 null): no-seed photon stays at center ──
    a3 = matrix[(3, 0.30)]
    out["arm3_null"] = {
        "E_V": a3["E_V"], "max_V_inc": float(np.asarray(a3["Vinc_series"]).max()),
        "closes23": bool(a3["ps1"]["vinc_closes_23"] or a3["ps1"]["vref_closes_23"]),
        "gamma_min": a3["gamma1"]["gamma_min"],
    }

    # ── Arm-4 charge flip (provenance certificate) ──
    flips = []
    for f in FRACS:
        hp = matrix[(1, f)]["H_bel"]; hm = matrix[(4, f)]["H_bel"]
        flips.append(np.sign(hp) != np.sign(hm) and abs(hp) > 1e-6 and abs(hm) > 1e-6)
    out["arm4_charge_flip"] = {
        "per_frac": {str(f): {"H_bel_plus": matrix[(1, f)]["H_bel"],
                              "H_bel_minus": matrix[(4, f)]["H_bel"], "flips": bool(flips[i])}
                     for i, f in enumerate(FRACS)},
        "any_flip": bool(any(flips)),
    }

    # ── Arm-5 (Class-C discriminator): structure ONLY under CW free-work pump? ──
    out["arm5_pump"] = {}
    pump_only_structure = False
    for f in FRACS:
        a5 = matrix[(5, f)]
        led5 = _ledger_closes(a5)
        closes5 = bool(a5["ps1"]["vinc_closes_23"] or a5["ps1"]["vref_closes_23"])
        closes1 = bool(matrix[(1, f)]["ps1"]["vinc_closes_23"] or matrix[(1, f)]["ps1"]["vref_closes_23"])
        if closes5 and not closes1:
            pump_only_structure = True
        out["arm5_pump"][str(f)] = {
            "H_drift": led5["H_drift"], "v_secular_ratio": led5["v_secular_ratio"],
            "closes23": closes5, "ledger_closes": led5["closes"],
        }
    out["arm5_pump_only_structure"] = bool(pump_only_structure)

    # ── conservation ledger (Arm-1, deepest frac) ──
    led1 = _ledger_closes(matrix[(1, 0.95)])
    out["ledger"] = led1

    # ── emission reverses? (frac=0.85 Arm-1 extended; photon disperses → V relax) ──
    print("\n[emission-reverse] frac=0.85 Arm-1 extended (absorb → relax): does V_inc unwind toward Arm-2?")
    e_emit = _build_arm(1, 0.85)
    tr_emit = _run24(e_emit, GEN24_STEPS + GEN24_EMIT_STEPS)
    ev_emit = np.asarray([r["E_V"] for r in tr_emit])
    vi_emit = np.asarray([r["max_V_inc"] for r in tr_emit])
    pk_t = int(np.argmax(ev_emit)); ev_peak = float(ev_emit.max()); ev_final = float(ev_emit[-1])
    base2 = matrix[(2, 0.85)]["E_V"]
    # peak strictly before the end AND final decays toward the control baseline
    reverses = bool(pk_t < len(ev_emit) - 2 and ev_final < ev_peak and (ev_peak - base2) > EPS_MACHINE)
    out["emission_reverse"] = {
        "E_V_peak": ev_peak, "E_V_peak_step": pk_t, "E_V_final": ev_final,
        "E_V_arm2_baseline": base2, "max_V_inc_peak": float(vi_emit.max()),
        "max_V_inc_final": float(vi_emit[-1]), "reverses": reverses,
        "emit_trace_EV": ev_emit.tolist(), "emit_trace_Vinc": vi_emit.tolist(),
    }
    print(f"  E_V peak={ev_peak:.4e}@step{pk_t}  final={ev_final:.4e}  Arm-2 baseline={base2:.4e}  reverses={reverses}")

    # ── VERDICT (prereg §7; honest closure, no debug-toward-A) ──
    if used_forbidden or (not all_admissible) or (not arm2_topology_null):
        verdict = "C2"
        msg = "VOID — forbidden seeder / non-admissible seed / non-null Arm-2 topology (circular)"
    elif not deep_pos:
        verdict = "C1"
        msg = "FALSIFIER — dE_V<=eps_machine at deep saturation: GAP-1 STRUCTURAL (missing primitive)"
    elif three_closes_deep and out["arm4_charge_flip"]["any_flip"] and led1["closes"] and reverses:
        verdict = "A"
        msg = "STRONG POSITIVE — dE_V>0, de-novo (2,3) closes, Arm-2 null, Arm-4 flips, ledger closes, emission reverses"
    else:
        verdict = "B"
        msg = "LOCALIZES (expected/honest WIN) — dE_V>0 (source reversed) but (2,3) does NOT wind: missing winder primitive"
    out["verdict"] = verdict
    out["verdict_msg"] = msg

    print("\n" + "=" * 84)
    print(f"VERDICT {verdict}: {msg}")
    print(f"  dE_V per frac: " + "  ".join(f"{f}:{dEV[f]:+.3e}" for f in FRACS) +
          f"  | monotone={monotone} deep_positive={deep_pos}")
    print(f"  three_closes_deep={three_closes_deep}  arm2_topology_null={arm2_topology_null}  "
          f"arm4_flip={out['arm4_charge_flip']['any_flip']}  ledger_closes={led1['closes']}  "
          f"emission_reverses={reverses}  arm5_pump_only={pump_only_structure}")
    print("=" * 84)

    # ── figures + json ──
    try:
        out["figures"] = _make_figures(out, matrix, out["emission_reverse"])
        print("\nFigures:")
        for k, v in out["figures"].items():
            print(f"  {k}: {v}")
    except Exception as exc:  # never let plotting sink the data
        print(f"\n[figures FAILED: {exc}]")
        out["figures"] = {}

    jpath = os.path.join(HERE, "genesis_24_saturated_seed_results.json")
    with open(jpath, "w") as fh:
        json.dump(out, fh, indent=2, default=float)
    print(f"\nResults JSON: {jpath}")
    return out


if __name__ == "__main__":
    main()
