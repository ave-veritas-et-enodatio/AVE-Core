#!/usr/bin/env python3
"""
Stick-slip / Bingham-yield LATCHING rectification — dark-wake thrust, Phase 3.

Phase 2 (rrad_l_acoustic_rectification.py) found NO rectification: the engine's
Axiom-4 saturation kernel S(A)=√(1−(A/A_yield)²) is INSTANTANEOUS and EVEN in A,
so the asymmetric (slow-charge/fast-quench) duty cycle produced no directed DC the
symmetric control lacked (the ⟨A²⟩-triangle identity is asymmetry-blind).  Single
named mechanism; clean negative (Rule 11).

Phase 3 adds the CANONICAL rate-dependent yield-freeze LATCHING that Phase 2 named
as the missing piece — dark-wake-bemf-foc-synthesis.md §1.2 (the Op14/Lenz
back-EMF freeze):

  "When V(t) drops through V_yield in the Cosserat sector at a rate ‖dV/dt‖ such
   that the crossing takes ≥ τ_relax, any topologically non-trivial ω
   configuration ... FREEZES — the diverging L_eff (Op14 near S=0) generates a
   diverging Lenz back-EMF that blocks dω/dt during the τ_relax window.  Residues
   persist for ≥100 Compton periods in the post-heal solid regime."

This is RATE-DEPENDENT (‖dV/dt‖ vs τ_relax) + HYSTERETIC (memory) — the stick-slip
/ Bingham latching Phase 2 found missing.  It is the §1.2 STATED mechanism, NOT an
invented rescue (Rule 12).

=== SUBSTRATE-NATIVE KERNEL (substrate-native-check applied) ===

A per-cell dynamical GRIP state g(r,t) ∈ [0,1] on the COSSERAT ω dynamics — NOT a
phenomenological friction model:
  g=1  gripped/FROZEN  (dω/dt blocked — the diverging-L_eff Lenz freeze; couples)
  g=0  slipped         (Γ=−1, decoupled; ω evolves freely)

Rate-dependent crossing rule (§1.2, exact):
  the crossing of A through A_yield takes t_cross = A_yield/‖dA/dt‖; it FREEZES iff
  t_cross ≥ τ_relax  ⟺  ‖dA/dt‖ ≤ A_yield/τ_relax  (SLOW → grip; FAST → slip).
Memory: g relaxes toward its rate-determined target via the engine's OWN doc-59 §9
backward-Euler form  g ← (g·τ + dt·g_eq)/(τ + dt)  at the CANONICAL τ_relax.

WHY THIS SECTOR (architectural — flag-don't-fix).  The engine already ships a
canonical memristive latch (use_memristive_saturation, doc-59 §9) — but it lives in
the K4 PHOTON sector (S_field on V_inc/V_ref) and is DECOUPLED from the measured
momentum under this driver's disable_cosserat_lc_force=True (the V→ω coupling force
is zeroed at k4_cosserat_coupling.py:427).  The measured 2nd-order momentum is a
pure COSSERAT-ω object, and §1.2 is literally a Cosserat-ω freeze ("blocks dω/dt").
So the latch is applied to the Cosserat ω here, using the SAME canonical τ_relax +
backward-Euler form.  The K4-sector flag is run as a CONTROL (§ "K4-latch control")
to confirm it does nothing to the measured momentum.

=== LOCKED CANONICAL PARAMETERS (rescue-fill guard, prereg §3) ===

  τ_relax  = TAU_RELAX_NATIVE = ℓ_node/c = 1.0  (constants.py:335; Ax1+Ax3, doc-59
             §1; engine k4.tau_relax = dx/c).  PINNED — a single canonical number,
             NOT a bound.  (The §1.2 "≥100 Compton periods" is the residue
             PERSISTENCE — a separate, longer bound ≈ 628 native ≫ sim window.)
  A_yield  = 1  (Cosserat epsilon_yield = 1; the kernel zero S=√(1−A²)=0 at A=1;
             the Γ=−1 saturation/TIR boundary, Axiom 4).
The kernel has ZERO tunable knobs — every factor is the engine's own canonical
quantity (τ_relax, A_yield, S=√(1−A²), backward-Euler).  The τ_relax SWEEP below is
a DIAGNOSTIC to CLASSIFY the outcome (A vs C), NOT a search for a working value: the
headline is at canonical τ_relax; if rectification appears ONLY at non-canonical
τ_relax that is a rescue-fill → NEGATIVE (outcome C, prereg §5C).

Prereg : research/2026-06-08_rrad-l-stickslip-phase3_prereg.md
Phase 2: research/2026-06-08_rrad-l-rectification_result.md
"""

import argparse
import json
import os
import sys

import numpy as np

# Canonical-source imports (ave-canonical-source: never hard-code constants):
from ave.core.constants import (
    ALPHA, C_0, L_NODE, N_NU, TAU_RELAX_NATIVE, TAU_RELAX_SI, Z_0,
)
import ave.core.constants as _avc

from ave.topological.cosserat_field_3d import _compute_curvature, _compute_strain
from ave.topological.vacuum_engine import EngineConfig, VacuumEngine3D

# Reuse the Phase-2 machinery as the single source of truth for the drive
# waveform, the constitutive stress, the momentum-flux tensor, and the K4-native
# bulk-vs-shear extractor (no constitutive-form drift).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rrad_l_acoustic_rectification import (  # noqa: E402
    DutyCycleBeltramiSource,
    momentum_flux_axial,
    source_saturation_max,
    strain_bulk_shear_split,
)
from rrad_l_darkwake_impedance import elastic_energy_density  # noqa: E402

PI = np.pi


# ------------------------------------------------------------------ canonical-source verify
def verify_constants() -> None:
    """ave-canonical-source Step 4 — fail loudly on drift of the LOCKED params."""
    assert _avc.__file__.endswith("ave/core/constants.py"), \
        "ave.core.constants is not the AVE-Core canonical source"
    assert abs(N_NU - 2.0 / 7.0) < 1e-12, f"N_NU drifted: {N_NU}"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA drift from CODATA"
    # τ_relax is canonically PINNED, not tuned (constants.py:335; doc-59 §1).
    assert TAU_RELAX_NATIVE == 1.0, f"TAU_RELAX_NATIVE drifted: {TAU_RELAX_NATIVE}"
    assert abs(TAU_RELAX_SI - L_NODE / C_0) < 1e-30, "TAU_RELAX_SI != ℓ_node/c"
    print(f"[verify_constants] OK  τ_relax(native)={TAU_RELAX_NATIVE}  "
          f"(=ℓ_node/c; SI={TAU_RELAX_SI:.3e} s)  A_yield=1 (ε_yield)  "
          f"Z_0={Z_0:.2f}  ν_vac={N_NU:.4f}")


# ============================================================ stick-slip latch
class StickSlipLatch:
    """Per-cell §1.2 Op14/Lenz Cosserat-ω grip/FREEZE state g(r,t) ∈ [0,1].

    g=1: gripped/frozen — dω/dt blocked (the diverging-L_eff Lenz back-EMF that
         "blocks dω/dt during the τ_relax window", §1.2); the config couples.
    g=0: slipped — Γ=−1, ω evolves freely (decoupled).

    Rate-dependent target (§1.2):  the freeze requires DWELL near the yield
    boundary (S→0, diverging L_eff) for ≥ τ_relax — i.e. a SLOW crossing of the
    *saturation operating point* A₀ through A_yield.  The operating point A₀ is the
    τ_relax-lagged field amplitude (INVARIANT-S2: each LC tank's slow saturation
    state, distinct from the small-signal CARRIER which it cannot follow when
    ω·τ_relax ≳ 1; doc-59 §9 form on the Cosserat A):
        A₀  ← (A₀·τ_relax + dt·A) / (τ_relax + dt)        (operating-point lag)
        rate_slow = clip(1 − |dA₀/dt|·τ_relax/A_yield, 0, 1)   (1 slow → 0 fast)
        sat       = 1 − S(A₀) = 1 − √(1−min(A₀²,1))       (Op14 engagement →1 near S→0)
        g_eq      = sat · rate_slow
    Memory: backward-Euler relaxation at canonical τ_relax (engine doc-59 §9 form):
        g ← (g·τ_relax + dt·g_eq) / (τ_relax + dt)

    ZERO tunable knobs: τ_relax, A_yield, S=√(1−A²), backward-Euler are all the
    engine's own canonical quantities (τ_relax is used identically for the
    operating-point lag, the rate threshold, AND the grip memory — one physical
    relaxation time).  tau_mult is for the CLASSIFY-only sweep (headline runs at
    tau_mult=1.0 = canonical).  The carrier-INSTANTANEOUS rate is also tracked as a
    diagnostic (g_inst): in the ω·τ_relax≳1 regime the carrier always reads "fast",
    so the operating-point A₀ reading is the §1.2-faithful one (FLAG: §1.2 reading
    (a) instantaneous-V vs (b) operating-point-A₀ — surfaced for Grant, not silently
    resolved).
    """

    A_YIELD = 1.0  # canonical Γ=−1 boundary (ε_yield); kernel zero S=0 at A=1

    def __init__(self, cos, outer_dt: float, src_x: int, pml: int, N: int,
                 tau_mult: float = 1.0):
        self.cos = cos
        self.dt = float(outer_dt)
        self.tau = float(TAU_RELAX_NATIVE) * float(tau_mult)  # native time units
        self.g = np.zeros((N, N, N), dtype=np.float64)
        self.A0 = None        # τ_relax-lagged saturation operating point
        self.A0_prev = None
        self.g_inst_sum = 0.0  # diagnostic: carrier-instantaneous-rate grip
        self.A_inst_prev = None
        # grip region: alive interior, PML-excluded (Rule 10), source-slab-excluded
        # (the source overwrites its slab each step; freezing it would fight the
        #  injection).  This is the propagating WAKE where the §1.2 freeze acts.
        ii, jj, kk = np.indices((N, N, N))
        interior = (ii >= pml) & (ii < N - pml) & \
                   (jj >= pml) & (jj < N - pml) & \
                   (kk >= pml) & (kk < N - pml)
        wake = ii >= (src_x + 2)
        self.region = (interior & wake & cos.mask_alive)
        # running diagnostics (charge/quench grip split, hysteresis)
        self.g_charge_sum = 0.0
        self.g_quench_sum = 0.0
        self.n_charge = 0
        self.n_quench = 0
        self.g_max_seen = 0.0       # peak grip anywhere in the wake (engagement)
        self.g_frac_sum = 0.0       # fraction of wake cells with g > 0.1
        self.n_apply = 0

    def _amplitude(self) -> np.ndarray:
        """Per-cell saturation amplitude A = √(A²), A² = ε²/ε_y² + κ²/ω_y²."""
        eps = np.asarray(_compute_strain(self.cos.u, self.cos.omega, self.cos.dx))
        kappa = np.asarray(_compute_curvature(self.cos.omega, self.cos.dx))
        eps_sq = np.sum(eps ** 2, axis=(-1, -2))
        kappa_sq = np.sum(kappa ** 2, axis=(-1, -2))
        A2 = (eps_sq / (self.cos.epsilon_yield ** 2)
              + kappa_sq / (self.cos.omega_yield ** 2))
        return np.sqrt(np.maximum(A2, 0.0)), A2

    def apply(self, omega_prev: np.ndarray, on_charge_edge: bool) -> dict:
        """Advance g one step from the post-engine.step() state, then BLOCK dω/dt
        by the gripped fraction g (revert the fraction-g of this step's Δω and damp
        ω_dot).  Returns per-step grip diagnostics.
        """
        A, A2 = self._amplitude()
        # operating point A₀ = τ_relax-lagged field amplitude (doc-59 §9 form on
        # the Cosserat A; the slow saturation state, INVARIANT-S2)
        if self.A0 is None:
            self.A0 = A.copy()
            self.A0_prev = A.copy()
            self.A_inst_prev = A.copy()
        self.A0 = (self.A0 * self.tau + self.dt * A) / (self.tau + self.dt)
        dA0dt = (self.A0 - self.A0_prev) / self.dt
        self.A0_prev = self.A0.copy()

        # §1.2 rate rule on the OPERATING POINT (canonical threshold A_yield/τ_relax)
        rate_slow = np.clip(1.0 - np.abs(dA0dt) * self.tau / self.A_YIELD, 0.0, 1.0)
        A0_sq = self.A0 ** 2
        S0 = np.sqrt(np.clip(1.0 - np.minimum(A0_sq, 1.0), 0.0, 1.0))
        sat = 1.0 - S0  # Op14 engagement near S→0 (diverging-L_eff regime)
        g_eq = sat * rate_slow

        # diagnostic: carrier-INSTANTANEOUS-rate grip (reading (a)) — expected ~0
        # when ω·τ_relax≳1 because the carrier always reads "fast"
        dAdt_inst = (A - self.A_inst_prev) / self.dt
        self.A_inst_prev = A
        rate_slow_inst = np.clip(1.0 - np.abs(dAdt_inst) * self.tau / self.A_YIELD, 0.0, 1.0)
        Sinst = np.sqrt(np.clip(1.0 - np.minimum(A2, 1.0), 0.0, 1.0))
        g_eq_inst = (1.0 - Sinst) * rate_slow_inst
        if np.any(self.region):
            self.g_inst_sum += float(np.mean(g_eq_inst[self.region]))

        # backward-Euler relaxation at canonical τ_relax (doc-59 §9 form)
        self.g = (self.g * self.tau + self.dt * g_eq) / (self.tau + self.dt)

        # apply: block dω/dt by fraction g, ONLY in the wake region
        g_r = self.g[..., None]
        region = self.region[..., None]
        d_omega = self.cos.omega - omega_prev
        self.cos.omega = np.where(region, omega_prev + (1.0 - g_r) * d_omega,
                                  self.cos.omega)
        self.cos.omega_dot = np.where(region, (1.0 - g_r) * self.cos.omega_dot,
                                      self.cos.omega_dot)

        # diagnostics: mean grip in the wake, split by drive edge
        if np.any(self.region):
            g_in = self.g[self.region]
            gw = float(np.mean(g_in))
            self.g_max_seen = max(self.g_max_seen, float(np.max(g_in)))
            self.g_frac_sum += float(np.mean(g_in > 0.1))
            self.n_apply += 1
        else:
            gw = 0.0
        if on_charge_edge:
            self.g_charge_sum += gw
            self.n_charge += 1
        else:
            self.g_quench_sum += gw
            self.n_quench += 1
        return {"g_wake_mean": gw}

    def edge_grip(self) -> tuple[float, float]:
        """(mean grip on charge edges, mean grip on quench edges) over the window."""
        gc = self.g_charge_sum / self.n_charge if self.n_charge else 0.0
        gq = self.g_quench_sum / self.n_quench if self.n_quench else 0.0
        return gc, gq

    def inst_grip(self) -> float:
        """Mean carrier-INSTANTANEOUS-rate grip target (diagnostic, reading (a))."""
        n = self.n_charge + self.n_quench
        return self.g_inst_sum / n if n else 0.0

    def engagement(self) -> tuple[float, float]:
        """(peak grip anywhere in the wake, mean fraction of wake cells gripped>0.1).

        Distinguishes 'latch engaged but didn't rectify' (clean B) from 'latch
        never engaged' (inconclusive)."""
        frac = self.g_frac_sum / self.n_apply if self.n_apply else 0.0
        return self.g_max_seen, frac


# ============================================================ one condition run
def run_condition(label: str, handedness: str, charge_frac: float,
                  non_chiral: bool, N: int, pml: int, amp: float, lam: float,
                  duty_period: float, n_cycles: float, rec_cycles: float,
                  drive_mode: str = "triangle", latch_on: bool = True,
                  tau_mult: float = 1.0, k4_memristive: bool = False) -> dict:
    cfg = EngineConfig(
        N=N, pml=pml, temperature=0.0,
        use_asymmetric_saturation=True,     # chiral S_mu != S_eps path
        disable_cosserat_lc_force=True,     # A28-corrected bounded |omega|
        enable_cosserat_self_terms=True,
        use_memristive_saturation=k4_memristive,  # K4-sector latch CONTROL
    )
    engine = VacuumEngine3D(cfg)
    prop_axis = 0
    src_x = pml + 2
    omega_drive = 2.0 * PI / lam
    n_steps = int((2.0 + n_cycles) * duty_period)

    src = DutyCycleBeltramiSource(
        x0=src_x, propagation_axis=prop_axis, amplitude=amp,
        omega=omega_drive, handedness=handedness, sigma_yz=max(2.0, N / 8.0),
        duty_period=duty_period, charge_frac=charge_frac,
        ramp_cycles=2.0, non_chiral=non_chiral, drive_mode=drive_mode,
    )
    engine.add_source(src)

    cos = engine.cos
    interior = slice(pml, N - pml)
    far_slab = slice(N - pml - 6, N - pml - 2)
    src_slab = (src_x, interior, interior)

    latch = StickSlipLatch(cos, engine.outer_dt, src_x, pml, N,
                           tau_mult=tau_mult) if latch_on else None

    rec_steps = int(rec_cycles * duty_period)
    record_start = n_steps - rec_steps

    Tpp_series, sig_series, conv_series = [], [], []
    Px_series, Unear_series, A2max_series = [], [], []
    # reactance-pair tracking (Rule 10): C-state ⟨ω²⟩ + L-state ⟨ω_dot²⟩ each step
    omega_store_series, omegadot_store_series = [], []
    near_lo, near_hi = src_x + 1, min(src_x + 7, N - pml - 1)
    f_eff = charge_frac if drive_mode != "triangle" or not non_chiral else charge_frac

    for step in range(n_steps):
        omega_prev = cos.omega.copy() if latch_on else None
        engine.step()
        if latch_on:
            # which drive edge is this step on? (charge vs quench of the duty cycle)
            t_now = engine.step_count * engine.outer_dt
            phase = (t_now % duty_period) / duty_period if duty_period > 0 else 0.0
            on_charge = phase < charge_frac
            latch.apply(omega_prev, on_charge)

        if step >= record_start:
            alive = cos.mask_alive
            Tpp, neg_sig, conv = momentum_flux_axial(cos, prop_axis)
            sl = (far_slab, interior, interior)
            nplanes = far_slab.stop - far_slab.start
            Tpp_series.append(float(np.sum((Tpp * alive)[sl]) / nplanes))
            sig_series.append(float(np.sum((neg_sig * alive)[sl]) / nplanes))
            conv_series.append(float(np.sum((conv * alive)[sl]) / nplanes))
            ux_dot = cos.u_dot[..., prop_axis]
            Px_series.append(float(cos.rho * np.sum((ux_dot * alive)[(interior, interior, interior)])))
            U = elastic_energy_density(cos)
            near_slab = (slice(near_lo, near_hi), interior, interior)
            Unear_series.append(float(np.sum((U * alive)[near_slab])))
            A2max_series.append(source_saturation_max(cos, src_slab))
            wsl = (interior, interior, interior)
            omega_store_series.append(float(np.sum((np.sum(cos.omega ** 2, axis=-1) * alive)[wsl])))
            omegadot_store_series.append(float(np.sum((np.sum(cos.omega_dot ** 2, axis=-1) * alive)[wsl])))

    Tpp = np.array(Tpp_series)
    Px = np.array(Px_series)
    Tpp_dc = float(np.mean(Tpp))
    steps_axis = np.arange(len(Px), dtype=float)
    Px_drift = float(np.polyfit(steps_axis, Px, 1)[0]) if len(Px) > 2 else float("nan")

    strain_split = strain_bulk_shear_split(cos, far_slab, interior)
    g_charge, g_quench = latch.edge_grip() if latch_on else (0.0, 0.0)
    g_inst = latch.inst_grip() if latch_on else 0.0
    g_max, g_frac = latch.engagement() if latch_on else (0.0, 0.0)

    # local-clock modulation (Rule 10): ω_local = ω_drive·√(1−A²) at top-A² sites
    eps = np.asarray(_compute_strain(cos.u, cos.omega, cos.dx))
    kappa = np.asarray(_compute_curvature(cos.omega, cos.dx))
    A2_field = (np.sum(eps ** 2, axis=(-1, -2)) / (cos.epsilon_yield ** 2)
                + np.sum(kappa ** 2, axis=(-1, -2)) / (cos.omega_yield ** 2))
    msk = np.zeros_like(A2_field, dtype=bool)
    msk[interior, interior, interior] = True
    A2_int = np.where(msk & cos.mask_alive, A2_field, 0.0)
    flat = A2_int.ravel()
    topk = np.argpartition(flat, -8)[-8:] if flat.size > 8 else np.arange(flat.size)
    A2_peak = float(np.mean(flat[topk]))
    omega_local_frac = float(np.sqrt(max(0.0, 1.0 - min(A2_peak, 1.0))))  # √(1−A²) factor

    return {
        "label": label, "handedness": handedness, "charge_frac": charge_frac,
        "non_chiral": non_chiral, "latch_on": latch_on, "tau_mult": tau_mult,
        "Tpp_far_dc": Tpp_dc,
        "Px_drift": Px_drift,
        "U_near_mean": float(np.mean(Unear_series)),
        "A2_src_max": float(np.max(A2max_series)),
        "A2_src_mean": float(np.mean(A2max_series)),
        "omega_max": float(np.abs(cos.omega).max()),
        "strain_bulk_fraction": strain_split["strain_bulk_fraction"],
        "g_charge": g_charge, "g_quench": g_quench, "g_inst": g_inst,
        "g_max": g_max, "g_frac": g_frac,
        "omega_store_mean": float(np.mean(omega_store_series)),
        "omegadot_store_mean": float(np.mean(omegadot_store_series)),
        "A2_peak_interior": A2_peak,
        "omega_local_frac": omega_local_frac,
        "n_rec": int(len(Px)),
    }


def _jdir(results, sym_lh, sym_rh, asym_lh, asym_rh):
    def tpp(lbl):
        return results[lbl]["Tpp_far_dc"]
    jd_sym = 0.5 * (tpp(sym_rh) - tpp(sym_lh))
    jd_asym = 0.5 * (tpp(asym_rh) - tpp(asym_lh))
    jc_sym = 0.5 * (tpp(sym_rh) + tpp(sym_lh))
    jc_asym = 0.5 * (tpp(asym_rh) + tpp(asym_lh))
    ratio = abs(jd_asym) / abs(jd_sym) if abs(jd_sym) > 1e-300 else float("inf")
    return jd_sym, jd_asym, jc_sym, jc_asym, ratio


# ====================================================================== main
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=24)
    ap.add_argument("--pml", type=int, default=4)
    ap.add_argument("--amp", type=float, default=1.4)
    ap.add_argument("--lam", type=float, default=4.0)
    ap.add_argument("--duty-period", type=float, default=16.0)
    ap.add_argument("--charge-frac", type=float, default=0.85)
    ap.add_argument("--n-cycles", type=float, default=8.0)
    ap.add_argument("--rec-cycles", type=float, default=4.0)
    ap.add_argument("--sweep", action="store_true", help="run τ_relax classify sweep")
    ap.add_argument("--amp-robust", action="store_true", help="run amplitude robustness")
    ap.add_argument("--k4-control", action="store_true", help="run K4-latch decoupling control")
    ap.add_argument("--json", type=str, default="")
    args = ap.parse_args()

    verify_constants()
    print(f"\n=== stick-slip LATCHING rectification (Phase 3, SMOKE) ===")
    print(f"N={args.N} pml={args.pml} amp={args.amp} lam={args.lam} "
          f"duty={args.duty_period} charge_frac(ASYM)={args.charge_frac}")
    print(f"τ_relax = ℓ_node/c = {TAU_RELAX_NATIVE} native (canonical, PINNED)  "
          f"outer_dt=1/√2≈{1/np.sqrt(2):.3f}  → τ_relax≈{np.sqrt(2):.2f} steps  "
          f"A_yield=1\n")

    base_conditions = [
        ("SYM_LH",  "LH", 0.5,               False, "triangle"),
        ("SYM_RH",  "RH", 0.5,               False, "triangle"),
        ("ASYM_LH", "LH", args.charge_frac,  False, "triangle"),
        ("ASYM_RH", "RH", args.charge_frac,  False, "triangle"),
        ("ASYM_NC", "LH", args.charge_frac,  True,  "triangle"),
        ("FB_LH",   "LH", args.charge_frac,  False, "flyback"),
        ("FB_RH",   "RH", args.charge_frac,  False, "flyback"),
    ]

    def run_set(latch_on, tau_mult=1.0, k4_memristive=False):
        out = {}
        for label, hand, cf, nc, dm in base_conditions:
            out[label] = run_condition(
                label, hand, cf, nc, args.N, args.pml, args.amp, args.lam,
                args.duty_period, args.n_cycles, args.rec_cycles, drive_mode=dm,
                latch_on=latch_on, tau_mult=tau_mult, k4_memristive=k4_memristive)
        return out

    # ---- (A) latch OFF — reproduce Phase 2 baseline (sanity: ratios < 1) ----
    print("--- latch OFF (Phase-2 reproduction) ---")
    res_off = run_set(latch_on=False)
    jd_sym0, jd_asym0, jc_sym0, jc_asym0, ratio0 = _jdir(
        res_off, "SYM_LH", "SYM_RH", "ASYM_LH", "ASYM_RH")
    for lbl in ("SYM_LH", "ASYM_LH", "FB_LH"):
        r = res_off[lbl]
        print(f"  [{lbl:8s}] Tpp_dc={r['Tpp_far_dc']:+.3e}  A2max={r['A2_src_max']:.2f}  "
              f"bulk_frac={r['strain_bulk_fraction']:.3f}")
    print(f"  J_dir: SYM={jd_sym0:+.3e} ASYM={jd_asym0:+.3e}  ratio={ratio0:.2f}  "
          f"(expect <1 ~ Phase 2 null)")

    # ---- (B) latch ON at CANONICAL τ_relax — the Phase 3 result ----
    print("\n--- latch ON @ CANONICAL τ_relax (Phase 3) ---")
    res_on = run_set(latch_on=True, tau_mult=1.0)
    jd_sym, jd_asym, jc_sym, jc_asym, ratio = _jdir(
        res_on, "SYM_LH", "SYM_RH", "ASYM_LH", "ASYM_RH")
    jd_sym_fb, jd_fb, _, jc_fb, ratio_fb = _jdir(
        res_on, "SYM_LH", "SYM_RH", "FB_LH", "FB_RH")
    for lbl in ("SYM_LH", "SYM_RH", "ASYM_LH", "ASYM_RH", "FB_LH", "FB_RH"):
        r = res_on[lbl]
        dt_pp = r["Tpp_far_dc"] - res_off[lbl]["Tpp_far_dc"]
        print(f"  [{lbl:8s}] Tpp_dc={r['Tpp_far_dc']:+.3e} (Δvs_off={dt_pp:+.2e})  "
              f"g_chg={r['g_charge']:.3f} g_qnch={r['g_quench']:.3f}  "
              f"g_max={r['g_max']:.3f} g_frac={r['g_frac']:.3f}  "
              f"g_inst={r['g_inst']:.4f}  |w|max={r['omega_max']:.2e}")
    nc_tpp = res_on["ASYM_NC"]["Tpp_far_dc"]

    print(f"\n  J_dir(directed) = (Tpp_RH − Tpp_LH)/2:")
    print(f"    SYM ={jd_sym:+.3e}   ASYM={jd_asym:+.3e}   FB={jd_fb:+.3e}")
    print(f"    rectification ratio |J_dir_ASYM|/|J_dir_SYM| = {ratio:.2f}  "
          f"|J_dir_FB|/|J_dir_SYM| = {ratio_fb:.2f}")
    print(f"    common-mode  : SYM={jc_sym:+.3e}  ASYM={jc_asym:+.3e}  FB={jc_fb:+.3e}  "
          f"non-chiral Tpp={nc_tpp:+.3e}")
    gc_a = 0.5 * (res_on["ASYM_LH"]["g_charge"] + res_on["ASYM_RH"]["g_charge"])
    gq_a = 0.5 * (res_on["ASYM_LH"]["g_quench"] + res_on["ASYM_RH"]["g_quench"])
    gc_s = 0.5 * (res_on["SYM_LH"]["g_charge"] + res_on["SYM_RH"]["g_charge"])
    gq_s = 0.5 * (res_on["SYM_LH"]["g_quench"] + res_on["SYM_RH"]["g_quench"])
    print(f"    grip asymmetry: ASYM g_charge={gc_a:.3f} g_quench={gq_a:.3f} "
          f"(Δ={gc_a-gq_a:+.3f})  |  SYM g_charge={gc_s:.3f} g_quench={gq_s:.3f} "
          f"(Δ={gc_s-gq_s:+.3f})")
    print(f"    [CONFIRMED-A iff ratio≫1 AND J_dir_SYM~0 AND grip-asym ASYM≫SYM]")

    # ---- local-clock + reactance-pair report (Rule 10) ----
    ra = res_on["ASYM_LH"]
    print(f"  reactance pair (ASYM_LH): C-store ⟨ω²⟩={ra['omega_store_mean']:.3e}  "
          f"L-store ⟨ω_dot²⟩={ra['omegadot_store_mean']:.3e}")
    print(f"  local clock (ASYM_LH): A²_peak={ra['A2_peak_interior']:.3f}  "
          f"ω_local/ω_drive=√(1−A²)={ra['omega_local_frac']:.3f}")

    sweep_out = {}
    if args.sweep:
        print("\n--- τ_relax CLASSIFY sweep (A vs C diagnostic — NOT a value search) ---")
        print("    headline is canonical (mult=1.0); sweep classifies whether the")
        print("    canonical value sits in a wide rectifying band (A) or a tuned sliver (C).")
        for mult in (0.25, 0.5, 1.0, 2.0, 4.0):
            rs = {}
            for label, hand, cf, nc, dm in base_conditions[:4]:  # SYM/ASYM only
                rs[label] = run_condition(
                    label, hand, cf, nc, args.N, args.pml, args.amp, args.lam,
                    args.duty_period, args.n_cycles, args.rec_cycles,
                    drive_mode=dm, latch_on=True, tau_mult=mult)
            jds, jda, jcs, jca, rt = _jdir(rs, "SYM_LH", "SYM_RH", "ASYM_LH", "ASYM_RH")
            gc = 0.5 * (rs["ASYM_LH"]["g_charge"] + rs["ASYM_RH"]["g_charge"])
            gq = 0.5 * (rs["ASYM_LH"]["g_quench"] + rs["ASYM_RH"]["g_quench"])
            tag = " <-- CANONICAL" if mult == 1.0 else ""
            print(f"    τ×{mult:<4}: ratio={rt:7.2f}  J_dir_SYM={jds:+.2e} ASYM={jda:+.2e}  "
                  f"grip(chg/qnch)={gc:.2f}/{gq:.2f}{tag}")
            sweep_out[str(mult)] = {"ratio": rt, "jd_sym": jds, "jd_asym": jda,
                                    "g_charge": gc, "g_quench": gq}

    amp_out = {}
    if args.amp_robust:
        print("\n--- amplitude robustness @ canonical τ_relax (prereg §4 — push wake")
        print("    above yield so the latch ENGAGES; confirm B is 'engaged-but-no-rect',")
        print("    not 'never engaged') ---")
        for amp_r in (args.amp, 2.2, 3.0):
            rs = {}
            for label, hand, cf, nc, dm in base_conditions[:4]:
                rs[label] = run_condition(
                    label, hand, cf, nc, args.N, args.pml, amp_r, args.lam,
                    args.duty_period, args.n_cycles, args.rec_cycles,
                    drive_mode=dm, latch_on=True, tau_mult=1.0)
            jds, jda, jcs, jca, rt = _jdir(rs, "SYM_LH", "SYM_RH", "ASYM_LH", "ASYM_RH")
            gmax = max(rs["ASYM_LH"]["g_max"], rs["ASYM_RH"]["g_max"])
            gfrac = 0.5 * (rs["ASYM_LH"]["g_frac"] + rs["ASYM_RH"]["g_frac"])
            gc = 0.5 * (rs["ASYM_LH"]["g_charge"] + rs["ASYM_RH"]["g_charge"])
            gq = 0.5 * (rs["ASYM_LH"]["g_quench"] + rs["ASYM_RH"]["g_quench"])
            a2 = max(rs["ASYM_LH"]["A2_src_max"], rs["ASYM_RH"]["A2_src_max"])
            print(f"    amp={amp_r:<4}: ratio={rt:6.2f}  A2max={a2:5.2f}  "
                  f"g_max={gmax:.3f} g_frac={gfrac:.3f}  grip(chg/qnch)={gc:.3f}/{gq:.3f}")
            amp_out[str(amp_r)] = {"ratio": rt, "a2max": a2, "g_max": gmax,
                                   "g_frac": gfrac, "g_charge": gc, "g_quench": gq}

    k4_out = {}
    if args.k4_control:
        print("\n--- K4-latch control (use_memristive_saturation=True, latch OFF) ---")
        print("    confirms the engine's canonical K4-sector doc-59 latch is DECOUPLED")
        print("    from the measured Cosserat momentum (disable_cosserat_lc_force=True).")
        rk = run_set(latch_on=False, k4_memristive=True)
        jdk_s, jdk_a, _, _, rtk = _jdir(rk, "SYM_LH", "SYM_RH", "ASYM_LH", "ASYM_RH")
        print(f"    J_dir: SYM={jdk_s:+.3e} ASYM={jdk_a:+.3e}  ratio={rtk:.2f}  "
              f"(vs latch-OFF baseline ratio={ratio0:.2f} — expect ~identical → decoupled)")
        k4_out = {"jd_sym": jdk_s, "jd_asym": jdk_a, "ratio": rtk,
                  "baseline_ratio": ratio0}

    # ---- verdict ----
    print("\n=== VERDICT (prereg §5) ===")
    sym_nulls = abs(jd_sym) < 0.25 * abs(jd_asym) if abs(jd_asym) > 0 else False
    grip_asym = (gc_a - gq_a) > 1.5 * abs(gc_s - gq_s) + 1e-6
    if ratio >= 3.0 and sym_nulls:
        print(f"  → A (CONFIRMED): ratio={ratio:.2f}≫1, SYM nulls, grip-asym present. "
              f"Latch revives rectification at canonical τ_relax (Class-B manifestation).")
    elif ratio < 3.0:
        print(f"  → B (NO rectification): ratio={ratio:.2f} not ≫1 even with the "
              f"canonical stick-slip latch. Rectification dead regardless of hysteresis "
              f"(strongest negative — kills the slow-grip/fast-slip thrust route).")
    else:
        print(f"  → inspect: ratio={ratio:.2f}, SYM-null={sym_nulls}, "
              f"grip-asym={grip_asym}. Check τ-sweep for rescue-fill (C).")
    print("  CAVEAT (ave-driver-script-honesty): SMOKE. Robust = SIGNS/RATIOS/CONTRAST. "
          "Absolute thrust magnitude BLOCKED (same gate as Phase 1/2).")

    if args.json:
        with open(args.json, "w") as f:
            json.dump({
                "args": vars(args), "res_off": res_off, "res_on": res_on,
                "ratio_off": ratio0, "ratio_on": ratio, "ratio_fb_on": ratio_fb,
                "jd_sym_on": jd_sym, "jd_asym_on": jd_asym, "jd_fb_on": jd_fb,
                "grip": {"asym_charge": gc_a, "asym_quench": gq_a,
                         "sym_charge": gc_s, "sym_quench": gq_s},
                "sweep": sweep_out, "amp_robust": amp_out, "k4_control": k4_out,
            }, f, indent=2)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
