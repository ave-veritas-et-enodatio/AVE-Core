#!/usr/bin/env python3
"""
Acoustic-rectification DC momentum — dark-wake thrust, Phase 2 (the RIGHT object).

Phase 1 (rrad_l_darkwake_impedance.py) measured a steady-CW LINEAR radiation
resistance R_rad,L and found the mode propagating but reactance-dominated (high-Q
"poor radiator").  Per Grant's adjudication 2026-06-08 ("genuine substrate bounce,
acoustic rectification") the actual thrust is the SECOND-ORDER, asymmetric-cycle
RECTIFIED DC momentum (the four-stroke ledger's enclosed area), and the high
reactive store X_L from Phase 1 is the RESERVOIR being pumped, not a defect.

Mechanism (home leaf AVE-Propulsion 03_acoustic_rectification.tex):
  - Slow edge (grip): |A| < A_yield -> S(A)~1, high-impedance inductive grip,
        reaction force coupled to the hull.
  - Fast edge (slip): |A| crosses A_yield -> S(A)->0, Gamma=-1, zero-impedance
        backward slip, ZERO negative momentum returned.
  - Time-average over the asymmetric duty cycle -> continuous DC thrust.
  - SYMMETRIC sine/triangle -> exactly ZERO time-averaged thrust.

What this driver measures (NEW object vs Phase 1):
  - PRIMARY: interior substrate x-momentum drift  P_x(t) = rho * sum_interior u_dot_x
        -> linear drift over integer duty cycles = net recoil thrust (the bounce).
  - CORROBORATING: far-plane axial momentum-flux  <T_pp>_far,
        T_ij = -sigma_ij + rho u_dot_i u_dot_j   (Cauchy stress + 2nd-order convective).
  - The constitutive stress sigma is IDENTICAL to the Phase-1 driver's energy-flux
        stress (cosserat_field_3d.py:588 _energy_density_bare, linear part):
            sigma_ij = (4/3)G tr(eps) d_ij + 2G eps_sym,ij + 2 G_c eps_antisym,ij

Protocol (pre-reg 2026-06-08_rrad-l-rectification_prereg.md, criteria 4a-4d):
  2x2  {SYM, ASYM} x {LH, RH}  + (ASYM x non-chiral linear) control.
  4a rectification : |DC_ASYM| >> |DC_SYM| and DC_SYM ~ 0  (ledger pound != 0).
  4b chiral        : sign(DC_LH) = -sign(DC_RH); non-chiral nulls.
  4c both-required : SYM~0 (chirality alone fails); ASYM non-chiral ~0
                     (rectification alone fails); ASYM x {LH,RH} opposite -> directed.
  4d bulk-vs-shear : far-plane (div u)^2 [P-wave, 1/7, electron channel] vs
                     |curl u|^2 [S-wave, 2/7, photon channel]; which carries the DC.
                     BULK -> Q->inf electron pilot-wave unification recovers at mode level.

HONEST SCOPE (ave-driver-script-honesty): the ABSOLUTE thrust magnitude is BLOCKED
(needs a converged radiating sim + a defensible source-current normalization, the
same gate as Phase 1).  The achievable result is the QUALITATIVE rectification
signature (SYM->0, ASYM->nonzero, chiral-directed, both-required) + the
bulk-vs-shear mode verdict.  Robust observables are SIGNS, RATIOS, and the
SYM-vs-ASYM CONTRAST -- not absolute Newtons.  See
research/2026-06-08_rrad-l-rectification_result.md for DERIVED/VERIFIED/BLOCKED.

Prereg: research/2026-06-08_rrad-l-rectification_prereg.md
Phase 1: src/scripts/vol_4_engineering/rrad_l_darkwake_impedance.py
"""

import argparse
import json
import os
import sys

import numpy as np

# Canonical-source imports (ave-canonical-source: never hard-code constants):
from ave.core.constants import ALPHA, C_0, N_NU, Z_0
import ave.core.constants as _avc

from ave.topological.cosserat_field_3d import _compute_curvature, _compute_strain
from ave.topological.vacuum_engine import (
    CosseratBeltramiSource,
    EngineConfig,
    VacuumEngine3D,
)

# Reuse the Phase-1 machinery as the single source of truth for the constitutive
# stress + reservoir energy + constants cross-check (no constitutive-form drift).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rrad_l_darkwake_impedance import (  # noqa: E402
    elastic_energy_density,
    verify_constants,
)

PI = np.pi


# ====================================================================== drive
class DutyCycleBeltramiSource(CosseratBeltramiSource):
    """Asymmetric slow-charge / fast-quench duty-cycle chiral drive.

    Replaces CosseratBeltramiSource's monotonic ramp/sustain envelope with a
    PERIODIC asymmetric triangle amplitude waveform (the flyback stroke of
    03_acoustic_rectification.tex):

        phase = (t mod T_duty) / T_duty
        charge (phase < f):  A = A_peak * phase/f            [slow grip]
        quench (phase >= f): A = A_peak * (1 - (phase-f)/(1-f)) [fast slip]

    Two drive_mode shapes:
      - "triangle": A = A_peak * (slow rise over f, fast fall over 1-f).
            f = charge_frac; f=0.5 is the SYMMETRIC control.  NOTE: a triangle's
            mean-square <A^2> = A_peak^2/3 is INDEPENDENT of f, so any even-in-A
            (quadratic / saturation) response cannot distinguish SYM from ASYM by
            construction -- triangle isolates RATE-asymmetry only.
      - "flyback": the FAITHFUL 03_acoustic_rectification.tex waveform -- slow
            charge to a SUB-yield grip plateau (grip_frac * A_peak, S~1, grips),
            then a fast triangular SPIKE up to A_peak (OVER-yield, S->0, slips)
            and reset.  The over-yield (slip) excursion is concentrated on the
            fast edge ONLY; its symmetric control reaches the same A_peak on a
            symmetric triangle (over-yield on both edges).  This is the waveform
            whose slip-on-fast-edge asymmetry the leaf's rectification needs.

    The carrier (cos(omega t), +/- sin(omega t)) provides the helical chirality;
    `non_chiral=True` drives a LINEAR (single transverse axis, non-rotating)
    pattern with no handedness (the chiral-control of pre-reg 4b/4c).
    """

    def __init__(self, *, duty_period: float, charge_frac: float,
                 ramp_cycles: float = 2.0, non_chiral: bool = False,
                 drive_mode: str = "triangle", grip_frac: float = 0.4,
                 spike_frac: float = 0.12, **kw):
        # parent envelope timing is unused (we override envelope); pass dummies.
        kw.setdefault("t_ramp", 1.0)
        kw.setdefault("t_sustain", 1.0)
        super().__init__(**kw)
        self.duty_period = float(duty_period)
        self.charge_frac = float(charge_frac)
        self.ramp_cycles = float(ramp_cycles)
        self.non_chiral = bool(non_chiral)
        self.drive_mode = str(drive_mode)
        self.grip_frac = float(grip_frac)
        self.spike_frac = float(spike_frac)

    def envelope(self, t: float) -> float:
        if t < 0:
            return 0.0
        phase = (t % self.duty_period) / self.duty_period
        if self.drive_mode == "flyback":
            f = self.charge_frac
            sw = self.spike_frac
            g = self.grip_frac
            if phase < f:                       # slow sub-yield charge -> grip
                a = g * (phase / f)
            elif phase < f + sw:                # fast over-yield spike (slip)
                s = (phase - f) / sw
                spike = 1.0 - abs(2.0 * s - 1.0)   # triangle 0 -> 1 -> 0
                a = g + (1.0 - g) * spike
            else:                               # reset
                a = 0.0
        else:  # "triangle"
            f = self.charge_frac
            if phase < f:
                a = phase / f
            else:
                a = 1.0 - (phase - f) / (1.0 - f)
        ramp = min(1.0, t / (self.ramp_cycles * self.duty_period))
        return a * ramp

    def apply(self, engine, t):
        if not self.non_chiral:
            return super().apply(engine, t)
        # Non-chiral linear drive: single transverse axis oscillates, no helix.
        self._init_if_needed(engine)
        env = self.envelope(t)
        if env <= 0:
            return
        amp_current = self.amplitude * env
        c_t = np.cos(self.omega * t)
        active_slab = self._slab_active_mask(engine)
        pattern = amp_current * self._transverse_profile * active_slab
        ax1, ax2 = self._trans_axes
        slab_view = self._slab_omega_view(engine)
        slab_view[...] = 0.0
        slab_view[..., ax1] = pattern * c_t       # linear polarization (no sin axis)
        self.cumulative_action_injected += float(np.sum(pattern ** 2) * c_t ** 2)


# ============================================================ momentum tensor
def cosserat_stress(cos) -> np.ndarray:
    """Cauchy stress sigma_ij at every site, shape (N,N,N,3,3).

    IDENTICAL constitutive form to the Phase-1 driver's cosserat_energy_flux
    (cosserat_field_3d.py:588 _energy_density_bare linear part):
        sigma_ij = (4/3) G tr(eps) d_ij + 2 G eps_sym,ij + 2 G_c eps_antisym,ij
    """
    G, G_c, dx = cos.G, cos.G_c, cos.dx
    eps = np.asarray(_compute_strain(cos.u, cos.omega, dx))     # eps[...,i,j]
    eps_T = np.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)
    eps_antisym = 0.5 * (eps - eps_T)
    tr_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]
    I3 = np.eye(3)
    sigma = ((4.0 / 3.0) * G * tr_eps[..., None, None] * I3
             + 2.0 * G * eps_sym
             + 2.0 * G_c * eps_antisym)
    return sigma


def momentum_flux_axial(cos, p: int) -> np.ndarray:
    """Axial momentum-flux density T_pp = -sigma_pp + rho u_dot_p^2, shape (N,N,N).

    T_pp = flux of p-momentum across a plane normal to p (the thrust carried
    downstream).  -sigma_pp = linear elastic part (time-averages ~0 for a
    symmetric wave, NONZERO under the rectified slip); rho u_dot_p^2 = the
    2nd-order convective (radiation-pressure / streaming) part.
    """
    sigma = cosserat_stress(cos)
    sig_pp = sigma[..., p, p]
    conv_pp = cos.rho * (cos.u_dot[..., p] ** 2)
    return -sig_pp + conv_pp, -sig_pp, conv_pp


def strain_bulk_shear_split(cos, far_slab, interior: slice) -> dict:
    """Bulk-vs-shear of the EXCITED strain field over a PML-excluded far SLAB.

    K4-NATIVE: decomposes the SAME strain eps = d_j u_i - eps_ijk omega_k the
    stress uses (via _compute_strain's tetrahedral gradient), NOT an np.gradient
    of u.  Rationale (load-bearing): the lattice is bipartite and the u field
    carries a staggered odd-even structure (every other x-plane is a near-node),
    so a single-plane np.gradient decomposition is a sublattice artifact.  The
    far SLAB (several consecutive planes) spans both sublattices and washes it
    out; _compute_strain's tetrahedral stencil is the substrate-native gradient.

        dilatational (BULK, P-wave, 1/7, electron channel) = tr(eps)^2
        deviatoric+rotational (SHEAR, S-wave, 2/7, photon channel)
            = |eps_sym_dev|^2 + |eps_antisym|^2
    A chiral Beltrami omega-source injects eps_antisym = -eps_ijk omega (pure
    rotation), so a SHEAR-dominant far field confirms the as-driven wake lives in
    the shear/microrotation sector (Phase-1 verdict); a BULK-dominant far field
    would mean the bounce rides the compression P-wave and the Q->inf electron
    pilot-wave unification RECOVERS at the mode level.
    """
    eps = np.asarray(_compute_strain(cos.u, cos.omega, cos.dx))
    eps_T = np.swapaxes(eps, -1, -2)
    eps_sym = 0.5 * (eps + eps_T)
    eps_antisym = 0.5 * (eps - eps_T)
    tr_eps = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]
    I3 = np.eye(3)
    eps_sym_dev = eps_sym - (tr_eps[..., None, None] / 3.0) * I3
    bulk_d = tr_eps ** 2
    shear_d = (np.sum(eps_sym_dev ** 2, axis=(-1, -2))
               + np.sum(eps_antisym ** 2, axis=(-1, -2)))
    alive = cos.mask_alive
    sl = (far_slab, interior, interior)
    b = float(np.sum((bulk_d * alive)[sl]))
    s = float(np.sum((shear_d * alive)[sl]))
    return {"strain_bulk_energy": b, "strain_shear_energy": s,
            "strain_bulk_fraction": b / (b + s + 1e-300)}


# ============================================================ saturation state
def source_saturation_max(cos, src_slab) -> float:
    """Max Axiom-4 saturation state A^2 = |eps|^2/eps_y^2 + |kappa|^2/omega_y^2
    on the source slab -- CP5 slip-engagement indicator (does the fast edge
    cross A_yield, i.e. A^2 -> 1?)."""
    eps = np.asarray(_compute_strain(cos.u, cos.omega, cos.dx))
    kappa = np.asarray(_compute_curvature(cos.omega, cos.dx))
    eps_sq = np.sum(eps ** 2, axis=(-1, -2))
    kappa_sq = np.sum(kappa ** 2, axis=(-1, -2))
    A2 = eps_sq / (cos.epsilon_yield ** 2) + kappa_sq / (cos.omega_yield ** 2)
    return float(np.max(A2[src_slab]))


# ============================================================ one condition run
def run_condition(label: str, handedness: str, charge_frac: float,
                  non_chiral: bool, N: int, pml: int, amp: float,
                  lam: float, duty_period: float, n_cycles: float,
                  rec_cycles: float, drive_mode: str = "triangle") -> dict:
    cfg = EngineConfig(
        N=N, pml=pml, temperature=0.0,
        use_asymmetric_saturation=True,     # chiral S_mu != S_eps path
        disable_cosserat_lc_force=True,     # A28-corrected bounded |omega|
        enable_cosserat_self_terms=True,
    )
    engine = VacuumEngine3D(cfg)
    prop_axis = 0
    src_x = pml + 2
    omega_drive = 2.0 * PI / lam
    n_steps = int((2.0 + n_cycles) * duty_period)   # 2 ramp cycles + n_cycles

    engine.add_source(DutyCycleBeltramiSource(
        x0=src_x, propagation_axis=prop_axis, amplitude=amp,
        omega=omega_drive, handedness=handedness, sigma_yz=max(2.0, N / 8.0),
        duty_period=duty_period, charge_frac=charge_frac,
        ramp_cycles=2.0, non_chiral=non_chiral, drive_mode=drive_mode,
    ))

    cos = engine.cos
    interior = slice(pml, N - pml)
    # PML-excluded far SLAB (spans both bipartite sublattices -> washes the
    # staggered odd-even u-node structure; single-plane sampling is artifact-prone)
    far_slab = slice(N - pml - 6, N - pml - 2)
    src_slab = (src_x, interior, interior)

    # record an INTEGER number of duty cycles in the steady window
    rec_steps = int(rec_cycles * duty_period)
    record_start = n_steps - rec_steps

    Px_series, Tpp_far_series, sigpp_far_series, conv_far_series = [], [], [], []
    Unear_series, A2max_series = [], []
    near_lo, near_hi = src_x + 1, min(src_x + 7, N - pml - 1)

    for step in range(n_steps):
        engine.step()
        if step >= record_start:
            alive = cos.mask_alive
            # PRIMARY: interior total x-momentum (substrate recoil)
            ux_dot = cos.u_dot[..., prop_axis]
            Px = float(cos.rho * np.sum((ux_dot * alive)[(interior, interior, interior)]))
            Px_series.append(Px)
            # CORROBORATING: far-SLAB axial momentum flux (per-plane mean)
            Tpp, neg_sig, conv = momentum_flux_axial(cos, prop_axis)
            sl = (far_slab, interior, interior)
            nplanes = far_slab.stop - far_slab.start
            Tpp_far_series.append(float(np.sum((Tpp * alive)[sl]) / nplanes))
            sigpp_far_series.append(float(np.sum((neg_sig * alive)[sl]) / nplanes))
            conv_far_series.append(float(np.sum((conv * alive)[sl]) / nplanes))
            # reactance pair (CP6): near-field grip reservoir
            U = elastic_energy_density(cos)
            near_slab = (slice(near_lo, near_hi), interior, interior)
            Unear_series.append(float(np.sum((U * alive)[near_slab])))
            # CP5: source saturation-state (slip engagement)
            A2max_series.append(source_saturation_max(cos, src_slab))

    Px = np.array(Px_series)
    Tpp = np.array(Tpp_far_series)

    # DC = integer-cycle mean (the carrier + duty AC average out over whole cycles)
    Tpp_dc = float(np.mean(Tpp))
    sigpp_dc = float(np.mean(sigpp_far_series))
    conv_dc = float(np.mean(conv_far_series))
    # P_x drift = net momentum accumulation rate = recoil force (linear slope)
    steps_axis = np.arange(len(Px), dtype=float)
    if len(Px) > 2 and np.std(steps_axis) > 0:
        Px_drift = float(np.polyfit(steps_axis, Px, 1)[0])  # momentum / step
    else:
        Px_drift = float("nan")

    strain_split = strain_bulk_shear_split(cos, far_slab, interior)

    return {
        "label": label, "handedness": handedness, "charge_frac": charge_frac,
        "non_chiral": non_chiral,
        "Px_drift": Px_drift,                 # PRIMARY directed DC momentum/step
        "Px_mean": float(np.mean(Px)),
        "Tpp_far_dc": Tpp_dc,                 # corroborating far-plane DC flux
        "neg_sigma_pp_dc": sigpp_dc,          # linear part of the DC flux
        "conv_pp_dc": conv_dc,                # 2nd-order convective part of the DC flux
        "U_near_mean": float(np.mean(Unear_series)),
        "A2_src_max": float(np.max(A2max_series)),   # CP5 slip engagement
        "A2_src_mean": float(np.mean(A2max_series)),
        "omega_max": float(np.abs(cos.omega).max()),
        "strain_bulk_fraction": strain_split["strain_bulk_fraction"],
        "strain_bulk_energy": strain_split["strain_bulk_energy"],
        "strain_shear_energy": strain_split["strain_shear_energy"],
        "n_rec": int(len(Px)),
    }


# ====================================================================== main
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=24)
    ap.add_argument("--pml", type=int, default=4)
    ap.add_argument("--amp", type=float, default=0.8, help="peak |omega| drive")
    ap.add_argument("--lam", type=float, default=4.0, help="carrier period (steps)")
    ap.add_argument("--duty-period", type=float, default=16.0, help="duty period (steps)")
    ap.add_argument("--charge-frac", type=float, default=0.85, help="asymmetric grip fraction")
    ap.add_argument("--n-cycles", type=float, default=8.0, help="duty cycles after ramp")
    ap.add_argument("--rec-cycles", type=float, default=4.0, help="integer cycles to average")
    ap.add_argument("--json", type=str, default="")
    args = ap.parse_args()

    verify_constants()
    print(f"\n=== acoustic-rectification DC-momentum driver (SMOKE) ===")
    print(f"N={args.N} pml={args.pml} amp={args.amp} lam={args.lam} "
          f"duty={args.duty_period} charge_frac(ASYM)={args.charge_frac}")
    print(f"transverse template R_perp=Z_0/(4pi)={Z_0/(4*PI):.3f} ohm  "
          f"nu_vac={N_NU:.4f} (2/7, shear/photon)  c_L=sqrt(2)c_0 (bulk/electron, 1/7)\n")

    # 2x2 (triangle) + non-chiral control + flyback (faithful leaf waveform).
    # SYM = symmetric triangle (charge_frac=0.5); ASYM = asymmetric triangle;
    # FB  = flyback (sub-yield grip + over-yield fast spike).  Same peak amp.
    conditions = [
        ("SYM_LH",  "LH", 0.5,               False, "triangle"),
        ("SYM_RH",  "RH", 0.5,               False, "triangle"),
        ("ASYM_LH", "LH", args.charge_frac,  False, "triangle"),
        ("ASYM_RH", "RH", args.charge_frac,  False, "triangle"),
        ("ASYM_NC", "LH", args.charge_frac,  True,  "triangle"),  # non-chiral linear
        ("FB_LH",   "LH", args.charge_frac,  False, "flyback"),
        ("FB_RH",   "RH", args.charge_frac,  False, "flyback"),
    ]
    results = {}
    for label, hand, cf, nc, dm in conditions:
        r = run_condition(label, hand, cf, nc, args.N, args.pml, args.amp,
                          args.lam, args.duty_period, args.n_cycles, args.rec_cycles,
                          drive_mode=dm)
        results[label] = r
        print(f"[{label:8s}] Px_drift={r['Px_drift']:+.4e}/step  "
              f"Tpp_far_dc={r['Tpp_far_dc']:+.4e}  conv_dc={r['conv_pp_dc']:+.4e}  "
              f"A2_src_max={r['A2_src_max']:.3f}  "
              f"strain_bulk_frac={r['strain_bulk_fraction']:.3f}  "
              f"|w|max={r['omega_max']:.2e}")

    # Primary DIRECTED-momentum observable = the chiral-ANTISYMMETRIC part of the
    # far-slab axial momentum flux, J_dir(drive) = (Tpp_RH - Tpp_LH)/2.  This is
    # the handedness-directed momentum (the thrust vector); the common-mode
    # (Tpp_LH + Tpp_RH)/2 is the non-chiral offset.  (Px_drift is reported too but
    # is transient-fill-contaminated -- positive for all conditions, not chiral.)
    def tpp(lbl):
        return results[lbl]["Tpp_far_dc"]
    J_dir_sym = 0.5 * (tpp("SYM_RH") - tpp("SYM_LH"))
    J_dir_asym = 0.5 * (tpp("ASYM_RH") - tpp("ASYM_LH"))
    J_dir_fb = 0.5 * (tpp("FB_RH") - tpp("FB_LH"))
    J_cm_sym = 0.5 * (tpp("SYM_RH") + tpp("SYM_LH"))
    J_cm_asym = 0.5 * (tpp("ASYM_RH") + tpp("ASYM_LH"))
    J_cm_fb = 0.5 * (tpp("FB_RH") + tpp("FB_LH"))

    # ---- 4a rectification: does ASYM / FLYBACK produce DIRECTED momentum SYM lacks? ----
    rect_ratio = abs(J_dir_asym) / abs(J_dir_sym) if abs(J_dir_sym) > 0 else float("inf")
    rect_ratio_fb = abs(J_dir_fb) / abs(J_dir_sym) if abs(J_dir_sym) > 0 else float("inf")

    # ---- 4b chiral-directed (LH vs RH opposite sign in Tpp) + non-chiral null ----
    chiral_opposite = (np.sign(tpp("ASYM_LH")) == -np.sign(tpp("ASYM_RH"))
                       and abs(tpp("ASYM_LH")) > 0 and abs(tpp("ASYM_RH")) > 0)
    nc_tpp = tpp("ASYM_NC")

    # ---- 4d bulk-vs-shear (ASYM, averaged LH/RH; K4-native strain split) ----
    strain_bulk_frac = 0.5 * (results["ASYM_LH"]["strain_bulk_fraction"]
                              + results["ASYM_RH"]["strain_bulk_fraction"])
    mode = "BULK (P-wave, 1/7, electron channel)" if strain_bulk_frac > 0.5 \
        else "SHEAR (S-wave, 2/7, photon channel)"
    a2_engaged = max(results["ASYM_LH"]["A2_src_max"], results["ASYM_RH"]["A2_src_max"])

    print("\n--- ADJUDICATION (pre-reg 4a-4d) ---")
    print("primary directed-momentum observable J_dir = (Tpp_RH - Tpp_LH)/2 "
          "(chiral-antisymmetric far-slab axial momentum flux)")
    print(f"4a rectification  : |J_dir_ASYM|/|J_dir_SYM| = {rect_ratio:.2f}  "
          f"|J_dir_FLYBACK|/|J_dir_SYM| = {rect_ratio_fb:.2f}   "
          f"(J_dir_SYM={J_dir_sym:+.3e}, ASYM={J_dir_asym:+.3e}, FB={J_dir_fb:+.3e})  "
          f"[CONFIRMED if >>1 AND J_dir_SYM~0; ~1 => chiral GRIP not rectification]")
    print(f"   common-mode rad.pressure: SYM={J_cm_sym:+.3e} ASYM={J_cm_asym:+.3e} "
          f"FB={J_cm_fb:+.3e}  [identical => <A^2>-invariant, no rectification]")
    print(f"4b chiral-directed: Tpp_LH={tpp('ASYM_LH'):+.3e} Tpp_RH={tpp('ASYM_RH'):+.3e} "
          f"opposite-sign={chiral_opposite}  non-chiral Tpp={nc_tpp:+.3e}  "
          f"common-mode J_cm_ASYM={J_cm_asym:+.3e}")
    print(f"4c both-required  : J_dir_SYM (chirality-only) = {J_dir_sym:+.3e} ; "
          f"J_cm_ASYM (rectification-only / non-chiral) = {J_cm_asym:+.3e}")
    print(f"CP5 slip-engage   : max A2_src(ASYM) = {a2_engaged:.3f}  "
          f"[>1 => fast edge crosses A_yield, slip valve IS engaged]")
    print(f"4d bulk-vs-shear  : strain_bulk_frac(ASYM) = {strain_bulk_frac:.3f} "
          f"(K4-native, far-slab) -> {mode}")
    print(f"(transient channel: Px_drift signs LH/RH = "
          f"{np.sign(results['ASYM_LH']['Px_drift']):+.0f}/"
          f"{np.sign(results['ASYM_RH']['Px_drift']):+.0f} -- non-chiral => fill transient)")
    print("\nCAVEAT (ave-driver-script-honesty): SMOKE run.  Robust = SIGNS / RATIOS "
          "/ SYM-vs-ASYM contrast / bulk-frac.  Absolute magnitude (Newtons) BLOCKED "
          "on converged sim + source-current normalization (same gate as Phase 1).")

    if args.json:
        with open(args.json, "w") as f:
            json.dump({"args": vars(args), "results": results,
                       "J_dir_sym": J_dir_sym, "J_dir_asym": J_dir_asym,
                       "J_dir_fb": J_dir_fb,
                       "J_cm_sym": J_cm_sym, "J_cm_asym": J_cm_asym,
                       "J_cm_fb": J_cm_fb,
                       "rect_ratio": rect_ratio, "rect_ratio_fb": rect_ratio_fb,
                       "chiral_opposite": bool(chiral_opposite),
                       "non_chiral_tpp": nc_tpp,
                       "strain_bulk_fraction": strain_bulk_frac,
                       "a2_engaged": a2_engaged}, f, indent=2)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
