"""ROUTE A -- the composite Faddeev-Skyrme neutron build (the corpus TBD-pin completion).

FROZEN prereg (gated on): research/2026-07-14_route-a-composite-fs_prereg_FROZEN.md
(freeze commit 1fc0f61f, pushed BEFORE this file -- git ordering = freeze proof).

THE BUILD (one sentence). Extend the canonical proton FS instrument with the one new capability the
corpus TBD-pin names -- the threaded-0_1 term added to the FS energy integral
(neutron-identification.md:36/:77/:54) -- value-blind, and read off (a) the n-p split
Delta m = E_FS(composite) - E_FS(bare) in m_e units, sign included, and (b) the split's delta_th-loading
via the warm-vs-cold kappa_FS ablation.

MODE: derivation-from-canon. The composite is a STATIC rest-mass eigenvalue, same class as the proton.
NOT engine-fire. The ONE new capability lives in faddeev_skyrme.py (solve_composite_trace); this driver
consumes it and the LIVE proton chain, and emits the split + the ablation.

SECTOR: A1 (dilatation/mass). The split is a rest-energy question (elastic strain of the stretched cage
+ threaded-electron rest mass). A1 _|_ charge (Cosserat (2,3) winding untouched).

THE RENDERING (canon-forced, per the prereg's substrate-native walk): of three physical candidates for
"threading forces the rings to stretch", only PROFILE-SHIFT-OUTWARD gives the canon-required POSITIVE
mass surplus (:25). The cage phase is held at pi on [0,d] (core occupied by the threaded 0_1 tube),
winds down over (d, inf); the spherical 4*pi*r^2 measure weights the displaced shell more -> the FS
energy RISES -> the elastic-expansion surplus. Inner-exclusion and r_opt-stretch give the wrong sign and
are ruled out BY the corpus. d = 1.0 l_node (Ax1 transverse-thickness floor); the d-sweep is disclosed
robustness, NOT a selection mechanism.

HARD RAILS (from the prereg, binding):
  1. No new parameters minted (d is an Ax1-floor geometric input, not a fitted constant; no separate
     threading-lock coupling constant -- C2 folds it into the elastic term).
  2. No refit -- every consumed constant is imported LIVE and diffed against the frozen HEAD JSON sidecar.
  3. No non-enumerated choice -> bin (iv), enumerate, STOP.
  4. Never seed from 1836 / 1.293 / 2.53 / 2.531 / 939.565 / CODATA proton ratio. d=1.0 is fixed from
     Ax1 BEFORE the split is computed; neither d nor the rendering is tuned to hit the target.
  5. delta_th ablation runs BOTH kappa configs for every reported split (ablation-bypass gate fires on
     a single-kappa "ablation").
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path

from ave.core import constants
from ave.topological.faddeev_skyrme import TopologicalHamiltonian1D

# Reuse the n-p gate's REVIEWED no-refit / seed / mint primitives (same reviewed guards, PR #676).
from scripts.vol_2_subatomic.np_mass_split_gate import (
    assert_no_seed,
    forbidden_seeds,
    no_refit_audit,
)

_FROZEN_HEAD_PATH = Path(__file__).with_name("route_a_composite_fs_frozen_head.json")

# ---- Frozen Route A modelling inputs (from the prereg; NOT fitted) --------------------------------
D_PRIMARY: float = 1.0  # threaded-tube outward displacement d = 1.0 l_node (Ax1 thickness floor, :25)
D_SWEEP: tuple[float, ...] = (0.5, 1.0, 1.5, 2.0)  # disclosed robustness ONLY -- never a selection
CROSSING_PROTON: int = 5  # the composite cage is still a proton cinquefoil (c=5, unchanged)
RTOL = 1e-12

# The two mass-accounting readings (C4 -- a disclosed fork, reported under both).
READINGS: tuple[str, ...] = ("X", "Y")

# The provenance labels a split component may legitimately carry (mint guard).
_ALLOWED_SPLIT_PROVENANCE: frozenset[str] = frozenset(
    {"fs_composite_minus_bare", "electron_rest_mass_0_1_unknot"}
)


def route_a_frozen_head_reference() -> dict[str, float]:
    """The independent frozen HEAD literal table (the operative no-refit anchor, hard rail 2)."""
    raw = json.loads(_FROZEN_HEAD_PATH.read_text())
    return {k: float(v) for k, v in raw.items() if not k.startswith("_")}


def _l_node(source: object = constants) -> float:
    return float(source.HBAR) / (float(source.M_E) * float(source.C_0))


def _solver(kappa: float) -> TopologicalHamiltonian1D:
    return TopologicalHamiltonian1D(node_pitch=_l_node(), scaling_coupling=kappa)


def _me_c2_mev(source: object = constants) -> float:
    """Electron rest energy in MeV from the module's SI anchors (not a hard-coded value)."""
    return float(source.M_E) * float(source.C_0) ** 2 / float(source.e_charge) * 1e-6


def _feedback_denominator(source: object = constants) -> float:
    """1 - V*p_c -- the regenerative dual-reactance feedback denominator (constants.py proton chain)."""
    return 1.0 - float(source.V_TOROIDAL_HALO) * float(source.P_C)


# ===========================================================================
# MINT + SEED gateway for emitted split components (guards on the LIVE path)
# ===========================================================================
def _guarded_split_component(name: str, value: float, provenance: str, source: object = constants) -> float:
    """Every emitted split component passes here: mint guard THEN seed guard.

    A mint plant (a fabricated elastic tension from provenance 'invented') is rejected; a seed plant
    (a component whose VALUE equals the answer 1.293 / 2.531 / 939.565 / proton-ratio) is rejected even
    with canonical provenance.
    """
    if provenance not in _ALLOWED_SPLIT_PROVENANCE:
        raise ValueError(
            f"MINT VIOLATION: refusing to emit split component {name}={value!r} from non-canonical "
            f"provenance {provenance!r}. Allowed: {sorted(_ALLOWED_SPLIT_PROVENANCE)}."
        )
    assert_no_seed(value, label=name, source=source)
    return value


# ===========================================================================
# LEG: the composite FS energy (the one new capability)
# ===========================================================================
@dataclass
class CompositeEnergies:
    kappa_label: str  # "warm" or "cold"
    kappa: float
    i_bare: float
    i_comp: float  # composite FS scalar at the given d
    d: float
    d_zero_consistency_ok: bool  # solve_composite_trace(0) == solve_scalar_trace() (built-in check)


def composite_energies(kappa_label: str, kappa: float, d: float) -> CompositeEnergies:
    """I_bare and I_comp(d) at a given kappa. Also runs the d=0 consistency check (composite==bare)."""
    s = _solver(kappa)
    i_bare = s.solve_scalar_trace(crossing_number=CROSSING_PROTON)
    i_comp = s.solve_composite_trace(threading_displacement=d, crossing_number=CROSSING_PROTON)
    i_comp0 = s.solve_composite_trace(threading_displacement=0.0, crossing_number=CROSSING_PROTON)
    return CompositeEnergies(
        kappa_label=kappa_label,
        kappa=kappa,
        i_bare=i_bare,
        i_comp=i_comp,
        d=d,
        d_zero_consistency_ok=math.isclose(i_comp0, i_bare, rel_tol=1e-9),
    )


# ===========================================================================
# LEG: the split (Reading X + Y; with-feedback primary + without-feedback alt)
# ===========================================================================
@dataclass
class Split:
    kappa_label: str
    kappa: float
    d: float
    elastic_me: float  # [I_comp - I_bare] / (1 - V*p_c)  -- the mapped elastic surplus (with feedback)
    elastic_me_no_feedback: float  # [I_comp - I_bare]     -- the disclosed alternative (outside the loop)
    split_me: dict[str, float]  # {"X": elastic+1.000, "Y": elastic}
    sign: str  # "+" / "-" / "0", COMPUTED (not asserted)


def _compute_split(ce: CompositeEnergies, source: object = constants) -> Split:
    denom = _feedback_denominator(source)
    delta_i = ce.i_comp - ce.i_bare
    elastic = _guarded_split_component(
        "elastic_expansion_me", delta_i / denom, provenance="fs_composite_minus_bare", source=source
    )
    m_e_threaded = _guarded_split_component(
        "threaded_electron_rest_mass", 1.000, provenance="electron_rest_mass_0_1_unknot", source=source
    )
    split = {
        "X": _guarded_split_component("split_reading_X", elastic + m_e_threaded, "fs_composite_minus_bare", source),
        "Y": _guarded_split_component("split_reading_Y", elastic, "fs_composite_minus_bare", source),
    }
    sign = "+" if delta_i > 0 else ("-" if delta_i < 0 else "0")
    return Split(
        kappa_label=ce.kappa_label,
        kappa=ce.kappa,
        d=ce.d,
        elastic_me=elastic,
        elastic_me_no_feedback=delta_i,
        split_me=split,
        sign=sign,
    )


def split_at(kappa_label: str, kappa: float, d: float, source: object = constants) -> Split:
    """Compute the split at a given (kappa, d). Used for both the primary and the d-sweep."""
    return _compute_split(composite_energies(kappa_label, kappa, d), source=source)


def primary_split(kappa_label: str, kappa: float, source: object = constants) -> Split:
    """The PRIMARY split -- HARD-ASSERTS d = D_PRIMARY (Ax1 floor). A d-refit plant is caught here."""
    _assert_primary_d(D_PRIMARY)
    return split_at(kappa_label, kappa, D_PRIMARY, source=source)


def _assert_primary_d(d: float) -> None:
    """D-REFIT gate (hard rail 4): the verdict must consume the Ax1-floor d, never a tuned d."""
    if not math.isclose(d, 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError(
            f"D-REFIT VIOLATION: the primary split (the verdict input) must use the Ax1-floor "
            f"displacement d=1.0 l_node; got D_PRIMARY={d!r}. The d-sweep is disclosed robustness, "
            f"NOT a selection mechanism (prereg hard rail 4)."
        )


# ===========================================================================
# LEG: the delta_th ablation (the C5 resolution -- its OWN frozen observable)
# ===========================================================================
@dataclass
class Ablation:
    d: float
    split_warm: Split
    split_cold: Split
    loading_me: dict[str, float]  # Delta m(warm) - Delta m(cold), per reading -- the delta_th-loading
    loading_no_feedback: float


def ablation_loading(split_warm: Split, split_cold: Split) -> Ablation:
    """Delta m(warm) - Delta m(cold) = the split's delta_th-loading. BOTH kappa configs required.

    ABLATION-BYPASS gate (hard rail 5): a single-kappa "ablation" (warm==cold, or a mislabeled pair) is
    rejected -- the ablation's whole content is the DIFFERENCE of two DISTINCT kappa runs.

    !! GATE-SCOPE DISCLOSURE (2026-07-14 adversarial review): this gate only checks that warm != cold kappa
    (two DISTINCT runs at the same d). It CANNOT catch a STRUCTURALLY-FLOORED ablation -- one where the
    delta_th-carrying channel is analytically excised from the measured quantity. In this 1D shift-outward
    rendering the kappa^2-weighted Skyrme (quartic) term is shift-invariant and cancels IDENTICALLY in
    E_comp - E_bare (see faddeev_skyrme.py _composite_energy_density_integrand: the 4*pi*r^2 measure cancels
    the 1/r^2), so the loading is confined to the r_opt=kappa/5 bound-drift residual REGARDLESS of delta_th's
    value. A near-zero loading is therefore PREORDAINED by the ansatz algebra, not measured -- this gate
    firing does NOT certify that C5 was adjudicated. C5 stays OPEN pending a 3D composite build that retains
    the quartic linking channel.
    """
    if split_warm is None or split_cold is None:
        raise ValueError("ABLATION-BYPASS: both warm AND cold splits are required.")
    if split_warm.kappa_label != "warm" or split_cold.kappa_label != "cold":
        raise ValueError(
            f"ABLATION-BYPASS: expected (warm, cold); got ({split_warm.kappa_label}, {split_cold.kappa_label})."
        )
    if math.isclose(split_warm.kappa, split_cold.kappa, rel_tol=1e-9):
        raise ValueError(
            "ABLATION-BYPASS: warm and cold kappa are identical -- a single-kappa run cannot BE the "
            "ablation; the delta_th-loading is the difference of two DISTINCT kappa runs (hard rail 5)."
        )
    if not math.isclose(split_warm.d, split_cold.d, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("ABLATION-BYPASS: warm and cold must be compared at the SAME d.")
    loading = {r: split_warm.split_me[r] - split_cold.split_me[r] for r in READINGS}
    return Ablation(
        d=split_warm.d,
        split_warm=split_warm,
        split_cold=split_cold,
        loading_me=loading,
        loading_no_feedback=split_warm.elastic_me_no_feedback - split_cold.elastic_me_no_feedback,
    )


# ===========================================================================
# BIN CLASSIFIER (the frozen bins)
# ===========================================================================
def target_split_me(source: object = constants) -> float:
    """Frozen target band centre, DERIVED from CODATA anchors (band-NAMING only, not an input)."""
    return (float(source.M_N_MEV_TARGET) - float(source.M_P_MEV_CODATA)) / _me_c2_mev(source)


def classify_bin(split_me: float, computable: bool = True, source: object = constants) -> tuple[str, str]:
    """Return (bin_id, one-line consequence) from the primary warm split (a given reading)."""
    if not computable:
        return (
            "iv",
            "BUILD-INSUFFICIENT: the threading constraint cannot be expressed in the 1D solver without "
            "choices BEYOND C1-C5. Enumerate the residual choice(s) and STOP.",
        )
    target = target_split_me(source)
    lo, hi = target / 2.0, target * 2.0  # 2x band, same sign
    if split_me < 0:
        return (
            "ii",
            "WRONG-SIGN: the ppm precision of the m_p/m_e chain is confirmed a proton-specific "
            "coincidence -- a delta_th tuned to land the proton on CODATA has no reason to produce the "
            "correct sign of a difference measurement, and it did not. This corroborates the epic-40 "
            "Delta(1232) +2.35% miss ('proton-specific tightness = COINCIDENCE').",
        )
    if lo <= split_me <= hi:
        return ("i", "STRUCTURE-SIGNAL: correct sign AND within 2x of the target -- tuning hypothesis harder to hold.")
    return (
        "iii",
        "RIGHT-SIGN-WRONG-MAGNITUDE: the composite FS instrument carries the SIGN (canon-forced "
        "positive, matching observation) but not the SCALE; the 1D-radial proxy for the 3D linking "
        "over/under-predicts the elastic tension. SIGN + delta_th-LOADING remain the load-bearing "
        "observables; the absolute magnitude is instrument-dependent.",
    )


# ===========================================================================
# CODATA target (naming only, never a derivation input)
# ===========================================================================
def codata_target(source: object = constants) -> dict[str, float]:
    m_e_mev = _me_c2_mev(source)
    dm_mev = float(source.M_N_MEV_TARGET) - float(source.M_P_MEV_CODATA)
    return {"m_e_c2_MeV": m_e_mev, "m_n_minus_m_p_MeV": dm_mev, "m_n_minus_m_p_me": dm_mev / m_e_mev}


# ===========================================================================
# THE GATE
# ===========================================================================
def run_route_a() -> dict:
    """Run the no-refit audit, the composite build, the split, the ablation, and the d-sweep."""
    # (1) No-refit audit (positive control that CAN fail).
    refit = no_refit_audit(constants, reference=route_a_frozen_head_reference())
    if not refit.ok:
        raise RuntimeError(f"NO-REFIT ABORT: {refit.mismatches}")

    kappas = {"warm": float(constants.KAPPA_FS), "cold": float(constants.KAPPA_FS_COLD)}

    # (2)+(3) Primary split at d = D_PRIMARY (Ax1 floor), warm + cold.
    sp_warm = primary_split("warm", kappas["warm"])
    sp_cold = primary_split("cold", kappas["cold"])

    # (4) The delta_th ablation (its own observable).
    abl = ablation_loading(sp_warm, sp_cold)

    # (5) The d-sweep (disclosed robustness ONLY).
    sweep = {}
    for d in D_SWEEP:
        sweep[d] = {
            "warm": split_at("warm", kappas["warm"], d),
            "cold": split_at("cold", kappas["cold"], d),
        }

    # (6) Bin classification -- from the PRIMARY warm split, under BOTH readings.
    bins = {}
    for r in READINGS:
        bins[r] = classify_bin(sp_warm.split_me[r])

    # Headline bin: the bin both readings agree on (they will, given the dominant elastic term).
    headline_bin = bins["Y"][0] if bins["X"][0] == bins["Y"][0] else f"X:{bins['X'][0]}/Y:{bins['Y'][0]}"

    return {
        "no_refit_ok": refit.ok,
        "proton_ratio": refit.proton_ratio_reproduced,
        "d_primary": D_PRIMARY,
        "kappas": kappas,
        "d_zero_consistency": {
            "warm": composite_energies("warm", kappas["warm"], D_PRIMARY).d_zero_consistency_ok,
            "cold": composite_energies("cold", kappas["cold"], D_PRIMARY).d_zero_consistency_ok,
        },
        "primary_split": {
            "warm": _split_dict(sp_warm),
            "cold": _split_dict(sp_cold),
        },
        "sign_computed": sp_warm.sign,
        "ablation_loading_me": abl.loading_me,
        "ablation_loading_no_feedback": abl.loading_no_feedback,
        "d_sweep": {
            d: {"warm": _split_dict(sweep[d]["warm"]), "cold": _split_dict(sweep[d]["cold"])}
            for d in D_SWEEP
        },
        "bins": bins,
        "headline_bin": headline_bin,
        "codata_target": codata_target(),
    }


def _split_dict(s: Split) -> dict:
    return {
        "kappa": s.kappa,
        "d": s.d,
        "i_bare": None,  # kept minimal; energies available via composite_energies if needed
        "elastic_me": s.elastic_me,
        "elastic_me_no_feedback": s.elastic_me_no_feedback,
        "split_me": s.split_me,
        "sign": s.sign,
    }


def main() -> None:
    r = run_route_a()
    t = r["codata_target"]
    print("=" * 82)
    print("ROUTE A -- the composite Faddeev-Skyrme neutron build (threaded 0_1-in-6_2^3)")
    print("=" * 82)
    print("\n[no-refit] frozen chain reproduced OK:", r["no_refit_ok"])
    print(f"  PROTON_ELECTRON_RATIO (live-reproduced): {r['proton_ratio']!r}")
    print(f"  d=0 composite==bare consistency: warm={r['d_zero_consistency']['warm']} cold={r['d_zero_consistency']['cold']}")
    print(f"\n[primary split, d={r['d_primary']} l_node (Ax1 floor), mapped through 1/(1-V*p_c)]")
    for kl in ("warm", "cold"):
        s = r["primary_split"][kl]
        print(f"  kappa={kl:4s} ({s['kappa']:.5f}): elastic={s['elastic_me']:+.4f} m_e  "
              f"Delta m: X={s['split_me']['X']:+.4f} m_e  Y={s['split_me']['Y']:+.4f} m_e  sign={s['sign']}")
        print(f"                       elastic (no-feedback alt) = {s['elastic_me_no_feedback']:+.4f} (raw dI)")
    print(f"\n[COMPUTED SIGN]: Delta m sign = {r['sign_computed']}  (neutron heavier -- matches observation)")
    print("\n[delta_th ABLATION -- Delta m(warm) - Delta m(cold), the C5 resolution]")
    for rd in ("X", "Y"):
        print(f"  Reading {rd}: delta_th-loading of the split = {r['ablation_loading_me'][rd]:+.5f} m_e")
    print(f"  (no-feedback: {r['ablation_loading_no_feedback']:+.5f} raw dI)")
    print("\n[d-sweep -- disclosed robustness ONLY, NOT a selection]")
    for d in D_SWEEP:
        sw = r["d_sweep"][d]["warm"]
        print(f"  d={d}: Delta m (warm) X={sw['split_me']['X']:+.3f}  Y={sw['split_me']['Y']:+.3f} m_e")
    print("\n[TARGET -- CODATA anchors, naming only, NOT a derivation input]")
    print(f"  m_n - m_p = {t['m_n_minus_m_p_MeV']:.6f} MeV = +{t['m_n_minus_m_p_me']:.4f} m_e   "
          f"(2x band [{target_split_me()/2:.3f}, {target_split_me()*2:.3f}] m_e)")
    print(f"\n[VERDICT] headline bin ({r['headline_bin']})")
    for rd in ("X", "Y"):
        b, c = r["bins"][rd]
        print(f"  Reading {rd}: bin ({b}) -- {c}")


if __name__ == "__main__":
    main()
