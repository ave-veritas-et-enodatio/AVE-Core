#!/usr/bin/env python3
"""
Phased-array u-sector COMPRESSIONAL rectification — dark-wake thrust, Phase 4 (the
closing test of the exotic-rectification claim).

Phases 2-3 failed by SECTOR MISMATCH.  Phase 2: the engine's Axiom-4 kernel
S(A)=√(1−(A/A_yield)²) is instantaneous + EVEN in A → no rectification.  Phase 3:
the canonical §1.2 Op14/Lenz rate-dependent yield-freeze LATCH (a genuine
hysteretic stick-slip) ALSO did not rectify — because the latch freezes the
ROTATIONAL ω (Cosserat microrotation) sector while the measured directed momentum
ρ⟨u̇²⟩ lives in the TRANSLATIONAL u (P-wave) sector.  The latch was the right
mechanism in the WRONG sector.

Phase 4 (Grant 2026-06-08: "A then B; high-frequency plasma, phased arrays of
emitters causing constructive interference") drives the u-sector DIRECTLY and
co-locates the latch + drive + momentum:

  - DIRECTION from PHASE GRADIENT, not chirality.  A phased array steers/focuses by
    inter-element phase, so directionality no longer needs the ω/rotational chirality
    that trapped the Phase 2-3 source in the shear sector.
  - CONSTRUCTIVE INTERFERENCE = COMPRESSION = u-sector drive.  The focal density peak
    is a longitudinal/P-wave/bulk (u-sector) excitation; the geometric concentration
    G_geom (= array directivity; Q-G42 V_yield^(apparatus)=E_yield/G_geom,
    trampoline-framework.md:455) drives the local field to A_yield.
  - THE u-SECTOR LATCH (NOT the ω Lenz-freeze).  Peierls-Nabarro STZ thixotropic
    re-freeze (peierls-nabarro-paradox.md, clm-ghs75o) + Bingham yield τ_y
    (saturation-operator.md, clm-gdd70j: "the vacuum flows above τ_y=B_snap²/2μ₀").
    Applied to u/u̇ — co-located with the ρ⟨u̇²⟩ observable.
  - COUPLING ENABLED.  disable_cosserat_lc_force=False (Phase 3 had it True; here the
    physical u↔ω coupling channel is ON).

=== SUBSTRATE-NATIVE-CHECK (applied) ===
Time-domain compressional dynamics on the u (translational) sector.  The phased
array is a piston/transducer set launching a longitudinal wake (NOT a phenomenological
array model).  The latch is a per-cell plastic-slip state with thixotropic memory
(NOT a friction coefficient).  Reactance pair recorded (u-sector: C=elastic strain
energy, L=kinetic ρ⟨u̇²⟩).  Local clock ω_local=ω·√(1−A²) at load-bearing sites.

=== RULE-12 GUARD (LOCKED — rescue-fill is NEGATIVE) ===
  - SYMMETRIC control = a NON-FOCUSING / RANDOM-PHASE array.  It MUST null.
  - Array directivity is GEOMETRY (N_elem, element spacing, focal phase gradient) —
    a hardware parameter, NOT tuned-to-rectify.
  - Latch params (τ_relax=ℓ_node/c=1, A_yield=ε_yield=1) are CANONICAL — zero knobs.
  - B (no rectification even sector-matched) is the STRONGEST honest result: report it
    loudly; do NOT rescue-fill toward A.  If rectification appears only for tuned
    latch params or contrived phasing → C → NEGATIVE.
  - DISCRIMINATOR (the honest fork): the FOCUSED beam radiates forward by ordinary
    radiation pressure (the non-exotic beam-shaping path B) whether or not the latch
    is on.  So a focused-vs-random contrast is NOT automatically "exotic
    rectification".  The exotic claim requires the LATCH to ADD directed momentum
    beyond the latch-OFF focused baseline (latch_gain ≫ 1).  latch_gain ≈ 1 ⟹ the
    contrast is pure beam-shaping (path B) ⟹ exotic rectification is DEAD (outcome B).

=== DUAL PAYOFF (report BOTH, regardless of A/B/C) ===
The same phased array beams a directional wake.  The non-exotic beam-shaping thrust
F = G_geom·P_rad/c_shear (directivity × radiated power / slow shear speed,
c_shear=c_0=1 native) is reported alongside the rectification verdict — the path-B
fallback number that stands even if the exotic mechanism is dead.

Prereg : research/2026-06-08_rrad-l-phased-array-phase4_prereg.md
Phase 3: research/2026-06-08_rrad-l-stickslip-phase3_result.md (OUTCOME B, sector mismatch)
"""

import argparse
import json
import os
import sys

import numpy as np

# Canonical-source imports (ave-canonical-source: never hard-code constants):
from ave.core.constants import (
    ALPHA, C_0, L_NODE, N_NU, TAU_RELAX_NATIVE, TAU_RELAX_SI, V_LONG, Z_0,
)
import ave.core.constants as _avc

from ave.topological.cosserat_field_3d import _compute_curvature, _compute_strain
from ave.topological.vacuum_engine import EngineConfig, Source, VacuumEngine3D

# Reuse the Phase-2 machinery as the single source of truth for the constitutive
# stress, the momentum-flux tensor, and the K4-native bulk-vs-shear extractor.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rrad_l_acoustic_rectification import (  # noqa: E402
    cosserat_stress,
    momentum_flux_axial,
    source_saturation_max,
    strain_bulk_shear_split,
)
from rrad_l_darkwake_impedance import elastic_energy_density  # noqa: E402

PI = np.pi
C_SHEAR_NATIVE = 1.0            # transverse/photon speed (G_VAC=ρc₀² → √(G/ρ)=c₀)
C_LONG_NATIVE = float(V_LONG / C_0)  # longitudinal/P-wave = √(2G/ρ)=√2·c₀ (native √2)
GOLDEN_ANGLE = PI * (3.0 - np.sqrt(5.0))


# ------------------------------------------------------------------ canonical-source verify
def verify_constants() -> None:
    """ave-canonical-source Step 4 — fail loudly on drift of the LOCKED params."""
    assert _avc.__file__.endswith("ave/core/constants.py"), \
        "ave.core.constants is not the AVE-Core canonical source"
    assert abs(N_NU - 2.0 / 7.0) < 1e-12, f"N_NU drifted: {N_NU}"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA drift from CODATA"
    assert TAU_RELAX_NATIVE == 1.0, f"TAU_RELAX_NATIVE drifted: {TAU_RELAX_NATIVE}"
    assert abs(TAU_RELAX_SI - L_NODE / C_0) < 1e-30, "TAU_RELAX_SI != ℓ_node/c"
    assert abs(C_LONG_NATIVE - np.sqrt(2.0)) < 1e-9, "V_LONG != √2·c₀ (P-wave speed)"
    print(f"[verify_constants] OK  τ_relax(native)={TAU_RELAX_NATIVE} (=ℓ_node/c)  "
          f"A_yield=1 (ε_yield)  c_shear={C_SHEAR_NATIVE} c_L=√2≈{C_LONG_NATIVE:.4f}  "
          f"Z_0={Z_0:.2f}  ν_vac={N_NU:.4f}")


# ============================================================ phased-array u-source
class PhasedArrayCompressionalSource(Source):
    """u-sector COMPRESSIONAL phased array — direction from PHASE GRADIENT, not chirality.

    N_elem Gaussian emitter elements tile the transverse plane at x=x0; each drives u
    ALONG the propagation axis (longitudinal / compressional / P-wave) with its own
    phase φ_n.  Constructive interference at a focal region is the COMPRESSION peak (a
    u-sector excitation) reaching A_yield via the geometric concentration G_geom.

    focus_mode:
      "focused" : φ_n = k_L·(√(F²+r_n²)−F)  → all elements arrive in-phase at the focal
                  point (x0+F, on axis) → coherent compression peak.  THE DRIVE (ASYM).
      "random"  : φ_n ~ U(0,2π) (seeded)    → incoherent, NO focal peak → the
                  NON-FOCUSING control that MUST null (Rule-12 guard).  THE SYM CONTROL.
      "uniform" : φ_n = 0 (planar broadside) → partial on-axis beam (diagnostic).
      "steered" : φ_n = k_L·sinθ·y_n (linear gradient) → beam TILTS off-axis by θ
                  (demonstrates pure phase-gradient steering — the directivity payoff).

    Overwrites u at the source slab each step (Dirichlet piston BC), mirroring
    CosseratBeltramiSource's ω overwrite (vacuum_engine.py:962).  The injected
    component is u ALONG the propagation axis (a piston launching a longitudinal wake);
    the transverse u-components at the slab are zeroed (pure compression, no shear at
    the source).  c_L=√2 native (V_LONG) sets the focal phase delays.
    """

    def __init__(self, *, x0: int, propagation_axis: int, amplitude: float,
                 omega: float, n_elem: int, focus_mode: str, focal: float,
                 array_radius: float, sigma_elem: float, ramp_cycles: float,
                 carrier_period: float, seed: int = 0, steer_deg: float = 20.0):
        if propagation_axis not in (0, 1, 2):
            raise ValueError(f"propagation_axis must be 0/1/2, got {propagation_axis}")
        if focus_mode not in ("focused", "random", "uniform", "steered"):
            raise ValueError(f"bad focus_mode {focus_mode!r}")
        self.x0 = int(x0)
        self.propagation_axis = int(propagation_axis)
        self.amplitude = float(amplitude)
        self.omega = float(omega)
        self.n_elem = int(n_elem)
        self.focus_mode = str(focus_mode)
        self.focal = float(focal)
        self.array_radius = float(array_radius)
        self.sigma_elem = float(sigma_elem)
        self.ramp_cycles = float(ramp_cycles)
        self.carrier_period = float(carrier_period)
        self.seed = int(seed)
        self.steer_deg = float(steer_deg)
        self._trans_axes = tuple(i for i in (0, 1, 2) if i != self.propagation_axis)
        self._gauss_stack = None    # (n_elem, N, N) element transverse profiles
        self._phi = None            # (n_elem,) per-element phase
        self._active2d = None       # (N, N) alive mask at the source slab
        self.cumulative_action_injected = 0.0

    def _init_if_needed(self, engine) -> None:
        if self._gauss_stack is not None:
            return
        N = engine.N
        center = (N - 1) / 2.0
        # sunflower (golden-angle) element placement on a disk of array_radius
        n = np.arange(self.n_elem, dtype=float)
        rr = self.array_radius * np.sqrt((n + 0.5) / self.n_elem)
        th = n * GOLDEN_ANGLE
        c1 = center + rr * np.cos(th)   # element centers on transverse axis ax1
        c2 = center + rr * np.sin(th)   # ... ax2
        jj, kk = np.indices((N, N), dtype=float)
        gs = np.empty((self.n_elem, N, N), dtype=np.float64)
        for m in range(self.n_elem):
            r2 = (jj - c1[m]) ** 2 + (kk - c2[m]) ** 2
            gs[m] = np.exp(-r2 / (2.0 * self.sigma_elem ** 2))
        self._gauss_stack = gs

        k_L = self.omega / C_LONG_NATIVE   # P-wave wavenumber (focal delays use c_L)
        r_elem = rr                        # transverse radius of each element
        if self.focus_mode == "focused":
            d_n = np.sqrt(self.focal ** 2 + r_elem ** 2)
            self._phi = k_L * (d_n - self.focal)        # in-phase at focal point
        elif self.focus_mode == "random":
            rng = np.random.default_rng(self.seed)
            self._phi = rng.uniform(0.0, 2.0 * PI, size=self.n_elem)
        elif self.focus_mode == "uniform":
            self._phi = np.zeros(self.n_elem)
        else:  # "steered" — linear phase gradient along ax1 ⇒ tilt by steer_deg
            theta = np.deg2rad(self.steer_deg)
            self._phi = k_L * np.sin(theta) * (c1 - center)

        # alive mask at the source slab (transverse plane)
        if self.propagation_axis == 0:
            self._active2d = engine.cos.mask_alive[self.x0].astype(float)
        elif self.propagation_axis == 1:
            self._active2d = engine.cos.mask_alive[:, self.x0].astype(float)
        else:
            self._active2d = engine.cos.mask_alive[:, :, self.x0].astype(float)

    def envelope(self, t: float) -> float:
        if t < 0:
            return 0.0
        return min(1.0, t / (self.ramp_cycles * self.carrier_period))

    def _slab_u_view(self, engine):
        if self.propagation_axis == 0:
            return engine.cos.u[self.x0]
        if self.propagation_axis == 1:
            return engine.cos.u[:, self.x0]
        return engine.cos.u[:, :, self.x0]

    def apply(self, engine, t: float) -> None:
        self._init_if_needed(engine)
        env = self.envelope(t)
        if env <= 0:
            return
        # coherent sum of the element carriers at phase φ_n
        weights = np.cos(self.omega * t + self._phi)        # (n_elem,)
        pattern2d = np.tensordot(weights, self._gauss_stack, axes=(0, 0))  # (N, N)
        pattern2d = self.amplitude * env * pattern2d * self._active2d
        slab_u = self._slab_u_view(engine)                  # (N, N, 3) view into u
        slab_u[...] = 0.0                                   # clean overwrite (Dirichlet)
        slab_u[..., self.propagation_axis] = pattern2d      # COMPRESSIONAL (along prop axis)
        self.cumulative_action_injected += float(np.sum(pattern2d ** 2))


# ============================================================ u-sector plastic latch
class PlasticStickSlipLatch:
    """Per-cell u-sector Peierls-Nabarro / Bingham plastic stick-slip g(r,t) ∈ [0,1].

    The TRANSLATIONAL/PLASTIC latch — NOT the ω Lenz-freeze of Phase 3.  Canonical
    leaves (cited on main; the common/substrate-hysteresis-index grouping lives only on
    the unmerged sibling branch and is NOT cited as canon):
      - peierls-nabarro-paradox.md (clm-ghs75o): STZ thixotropic re-freeze — the
        substrate liquefies under local shear above yield (STZ slip) and
        "thixotropically re-freezes" when the stress drops, trapping the configuration.
      - saturation-operator.md (clm-gdd70j): Bingham plastic yield — "the vacuum flows
        above τ_y = B_snap²/2μ₀"; S(A)=√(1−(A/A_c)²).

    g=1 gripped/FROZEN (stick): du/dt blocked — the re-frozen solid holds the
        (plastic) displacement; the config couples.
    g=0 slipped (STZ fluid):    u evolves freely — above yield the substrate liquefies.

    SAME canonical machinery as Phase 3's StickSlipLatch (zero new knobs): the
    operating-point lag A₀, the rate_slow threshold (slow crossing ⇒ thixotropic
    re-freeze), sat=1−S(A₀) (Op14 engagement near S→0), and the doc-59 §9
    backward-Euler memory — ALL at the CANONICAL τ_relax (constants.py:335) and
    A_yield=ε_yield=1.  The ONLY change vs Phase 3 is the SECTOR: the freeze acts on
    u/u_dot (where the thrust momentum ρ⟨u̇²⟩ lives) instead of ω/ω_dot.  This is
    precisely the prereg's sector-match fix — same latch, co-located observable.
    """

    A_YIELD = 1.0  # canonical Γ=−1 boundary (ε_yield); kernel zero S=0 at A=1

    def __init__(self, cos, outer_dt: float, src_x: int, pml: int, N: int,
                 tau_mult: float = 1.0):
        self.cos = cos
        self.dt = float(outer_dt)
        self.tau = float(TAU_RELAX_NATIVE) * float(tau_mult)
        self.g = np.zeros((N, N, N), dtype=np.float64)
        self.A0 = None
        self.A0_prev = None
        ii, jj, kk = np.indices((N, N, N))
        interior = (ii >= pml) & (ii < N - pml) & (jj >= pml) & (jj < N - pml) \
            & (kk >= pml) & (kk < N - pml)
        wake = ii >= (src_x + 2)        # PML-excluded propagating wake (Rule 10)
        self.region = interior & wake & cos.mask_alive
        self.g_max_seen = 0.0
        self.g_frac_sum = 0.0
        self.g_mean_sum = 0.0
        self.n_apply = 0

    def _amplitude(self):
        """Per-cell saturation amplitude A=√(A²), A²=ε²/ε_y²+κ²/ω_y² (same canonical
        form as Phase 2/3 source_saturation_max).  For the compressional u-drive the
        strain ε=∂u−ω× is dominated by the longitudinal ∂_x u_x divergence — i.e. the
        amplitude that gates the latch is read from the u (compressional) sector."""
        eps = np.asarray(_compute_strain(self.cos.u, self.cos.omega, self.cos.dx))
        kappa = np.asarray(_compute_curvature(self.cos.omega, self.cos.dx))
        eps_sq = np.sum(eps ** 2, axis=(-1, -2))
        kappa_sq = np.sum(kappa ** 2, axis=(-1, -2))
        A2 = (eps_sq / (self.cos.epsilon_yield ** 2)
              + kappa_sq / (self.cos.omega_yield ** 2))
        return np.sqrt(np.maximum(A2, 0.0))

    def apply(self, u_prev: np.ndarray):
        A = self._amplitude()
        if self.A0 is None:
            self.A0 = A.copy()
            self.A0_prev = A.copy()
        # operating-point lag A₀ (doc-59 §9 form; the slow saturation state)
        self.A0 = (self.A0 * self.tau + self.dt * A) / (self.tau + self.dt)
        dA0dt = (self.A0 - self.A0_prev) / self.dt
        self.A0_prev = self.A0.copy()

        rate_slow = np.clip(1.0 - np.abs(dA0dt) * self.tau / self.A_YIELD, 0.0, 1.0)
        S0 = np.sqrt(np.clip(1.0 - np.minimum(self.A0 ** 2, 1.0), 0.0, 1.0))
        sat = 1.0 - S0                       # Op14 engagement near S→0 (re-freeze)
        g_eq = sat * rate_slow
        # backward-Euler relaxation at canonical τ_relax (thixotropic memory)
        self.g = (self.g * self.tau + self.dt * g_eq) / (self.tau + self.dt)

        # FREEZE the u-sector: block du/dt by the gripped fraction g, in the wake.
        g_r = self.g[..., None]
        region = self.region[..., None]
        d_u = self.cos.u - u_prev
        self.cos.u = np.where(region, u_prev + (1.0 - g_r) * d_u, self.cos.u)
        self.cos.u_dot = np.where(region, (1.0 - g_r) * self.cos.u_dot, self.cos.u_dot)

        if np.any(self.region):
            g_in = self.g[self.region]
            self.g_max_seen = max(self.g_max_seen, float(np.max(g_in)))
            self.g_frac_sum += float(np.mean(g_in > 0.1))
            self.g_mean_sum += float(np.mean(g_in))
            self.n_apply += 1

    def engagement(self):
        frac = self.g_frac_sum / self.n_apply if self.n_apply else 0.0
        gmean = self.g_mean_sum / self.n_apply if self.n_apply else 0.0
        return self.g_max_seen, frac, gmean


# ============================================================ power / directivity
def axial_power_flux(cos, p: int) -> np.ndarray:
    """Elastic axial energy-flux density P_p = −Σ_j σ_pj·u̇_j (Poynting analog),
    shape (N,N,N).  Integrated over a far plane it is the radiated power carried
    downstream (the P in F = G_geom·P/c_shear)."""
    sigma = cosserat_stress(cos)             # (N,N,N,3,3)
    flux = -np.sum(sigma[..., p, :] * cos.u_dot, axis=-1)
    return flux


def transverse_concentration(cos, x_plane: int, interior: slice) -> float:
    """G_geom proxy at a transverse plane: peak energy density / mean energy density
    over the alive interior of that plane (the focal field-concentration factor)."""
    U = elastic_energy_density(cos)
    alive = cos.mask_alive
    plane = (U * alive)[x_plane, interior, interior]
    am = (alive)[x_plane, interior, interior].astype(bool)
    vals = plane[am]
    if vals.size == 0 or np.mean(vals) <= 0:
        return float("nan")
    return float(np.max(vals) / (np.mean(vals) + 1e-300))


# ============================================================ one condition run
def run_condition(label: str, focus_mode: str, N: int, pml: int, amp: float,
                  lam: float, n_elem: int, focal: float, array_radius: float,
                  sigma_elem: float, n_cycles: float, rec_cycles: float,
                  latch_on: bool, coupling_on: bool, tau_mult: float = 1.0,
                  seed: int = 0, steer_deg: float = 20.0) -> dict:
    cfg = EngineConfig(
        N=N, pml=pml, temperature=0.0,
        use_asymmetric_saturation=True,
        # COUPLING: prereg flag #2.  coupling_on ⇒ disable_cosserat_lc_force=False
        # (the u↔ω channel is ON — Phase 3 had it disabled/True).  enable_cosserat_
        # _self_terms tracks the A28 convention (self-terms ON only under A28/disable).
        disable_cosserat_lc_force=(not coupling_on),
        enable_cosserat_self_terms=(not coupling_on),
    )
    engine = VacuumEngine3D(cfg)
    prop_axis = 0
    src_x = pml + 2
    omega_drive = 2.0 * PI / lam
    carrier_period = lam
    n_steps = int((2.0 + n_cycles) * carrier_period)

    engine.add_source(PhasedArrayCompressionalSource(
        x0=src_x, propagation_axis=prop_axis, amplitude=amp, omega=omega_drive,
        n_elem=n_elem, focus_mode=focus_mode, focal=focal, array_radius=array_radius,
        sigma_elem=sigma_elem, ramp_cycles=2.0, carrier_period=carrier_period,
        seed=seed, steer_deg=steer_deg,
    ))

    cos = engine.cos
    interior = slice(pml, N - pml)
    far_slab = slice(N - pml - 6, N - pml - 2)
    src_slab = (src_x, interior, interior)
    focal_x = min(int(round(src_x + focal)), N - pml - 1)

    latch = PlasticStickSlipLatch(cos, engine.outer_dt, src_x, pml, N,
                                  tau_mult=tau_mult) if latch_on else None

    rec_steps = int(rec_cycles * carrier_period)
    record_start = n_steps - rec_steps

    Tpp_series, conv_series, Px_series = [], [], []
    Prad_series, Udot_series, strainE_series, A2max_series, Ggeom_series = [], [], [], [], []
    blew_up = False

    for step in range(n_steps):
        u_prev = cos.u.copy() if latch_on else None
        engine.step()
        if latch_on:
            latch.apply(u_prev)
        # stability guard.  Physical |u|~2, |ω|~0.5 in these runs; a threshold of
        # 1e3 is huge headroom yet catches the OVERDRIVE numerical runaway (the
        # latch-ON velocity-Verlet goes unstable when the focus is driven FAR past
        # yield, e.g. amp≳2.2 → |u|~1e4, A²~1e6).  That runaway is a NUMERICAL
        # artifact, NOT physics (and NOT rectification — see the result doc); flag it
        # BLOCKED rather than letting it manufacture a spurious latch_gain.
        umax = float(np.abs(cos.u).max())
        wmax = float(np.abs(cos.omega).max())
        if not np.isfinite(umax) or not np.isfinite(wmax) or umax > 1e3 or wmax > 1e3:
            blew_up = True
            break
        if step >= record_start:
            alive = cos.mask_alive
            Tpp, _neg, conv = momentum_flux_axial(cos, prop_axis)
            sl = (far_slab, interior, interior)
            nplanes = far_slab.stop - far_slab.start
            Tpp_series.append(float(np.sum((Tpp * alive)[sl]) / nplanes))
            conv_series.append(float(np.sum((conv * alive)[sl]) / nplanes))
            ux_dot = cos.u_dot[..., prop_axis]
            Px_series.append(float(cos.rho * np.sum((ux_dot * alive)[(interior, interior, interior)])))
            Prad = axial_power_flux(cos, prop_axis)
            Prad_series.append(float(np.sum((Prad * alive)[sl]) / nplanes))
            Udot_series.append(float(np.sum((np.sum(cos.u_dot ** 2, axis=-1) * alive)[(interior, interior, interior)])))
            U = elastic_energy_density(cos)
            strainE_series.append(float(np.sum((U * alive)[(interior, interior, interior)])))
            A2max_series.append(source_saturation_max(cos, (focal_x, interior, interior)))
            Ggeom_series.append(transverse_concentration(cos, focal_x, interior))

    if blew_up or not Tpp_series:
        return {"label": label, "focus_mode": focus_mode, "latch_on": latch_on,
                "coupling_on": coupling_on, "blew_up": True, "n_rec": 0,
                "Tpp_far_dc": float("nan"), "conv_dc": float("nan"),
                "Px_mean": float("nan"), "P_rad_mean": float("nan"),
                "G_geom_focal": float("nan"), "A2_focal_max": float("nan"),
                "strain_bulk_fraction": float("nan"), "Udot_mean": float("nan"),
                "strainE_mean": float("nan"), "g_max": 0.0, "g_frac": 0.0,
                "g_mean": 0.0, "omega_max": float("nan"), "u_max": float("nan")}

    strain_split = strain_bulk_shear_split(cos, far_slab, interior)
    g_max, g_frac, g_mean = latch.engagement() if latch_on else (0.0, 0.0, 0.0)

    # local-clock (Rule 10): ω_local=ω_drive·√(1−A²) at the top-A² interior sites
    eps = np.asarray(_compute_strain(cos.u, cos.omega, cos.dx))
    kappa = np.asarray(_compute_curvature(cos.omega, cos.dx))
    A2_field = (np.sum(eps ** 2, axis=(-1, -2)) / (cos.epsilon_yield ** 2)
                + np.sum(kappa ** 2, axis=(-1, -2)) / (cos.omega_yield ** 2))
    msk = np.zeros_like(A2_field, dtype=bool)
    msk[interior, interior, interior] = True
    flat = np.where(msk & cos.mask_alive, A2_field, 0.0).ravel()
    topk = np.argpartition(flat, -8)[-8:] if flat.size > 8 else np.arange(flat.size)
    A2_peak = float(np.mean(flat[topk]))
    omega_local_frac = float(np.sqrt(max(0.0, 1.0 - min(A2_peak, 1.0))))

    return {
        "label": label, "focus_mode": focus_mode, "latch_on": latch_on,
        "coupling_on": coupling_on, "tau_mult": tau_mult, "blew_up": False,
        "Tpp_far_dc": float(np.mean(Tpp_series)),     # directed axial momentum flux
        "conv_dc": float(np.mean(conv_series)),       # ρu̇² streaming (radiation pressure)
        "Px_mean": float(np.mean(Px_series)),
        "P_rad_mean": float(np.mean(Prad_series)),    # radiated power (path-B thrust)
        "Udot_mean": float(np.mean(Udot_series)),
        "strainE_mean": float(np.mean(strainE_series)),
        "G_geom_focal": float(np.nanmean(Ggeom_series)),   # focal concentration = directivity
        "A2_focal_max": float(np.max(A2max_series)),       # yield engagement at focus
        "strain_bulk_fraction": strain_split["strain_bulk_fraction"],  # u-sector check
        "g_max": g_max, "g_frac": g_frac, "g_mean": g_mean,
        "A2_peak_interior": A2_peak, "omega_local_frac": omega_local_frac,
        "omega_max": float(np.abs(cos.omega).max()), "u_max": float(np.abs(cos.u).max()),
        "n_rec": int(len(Tpp_series)),
    }


def _avg_random(common_kw, latch_on, coupling_on, seeds, tau_mult=1.0):
    """Average the NON-FOCUSING control over several random-phase seeds (a single
    draw can accidentally partially focus; the control must null ON AVERAGE)."""
    rs = [run_condition(f"RANDOM_s{s}", "random", latch_on=latch_on,
                        coupling_on=coupling_on, tau_mult=tau_mult, seed=s, **common_kw)
          for s in seeds]
    ok = [r for r in rs if not r["blew_up"]]
    if not ok:
        return rs[0]
    agg = dict(ok[0])
    for key in ("Tpp_far_dc", "conv_dc", "Px_mean", "P_rad_mean", "G_geom_focal",
                "A2_focal_max", "strain_bulk_fraction", "g_max", "g_frac",
                "Udot_mean", "strainE_mean"):
        agg[key] = float(np.mean([r[key] for r in ok]))
    agg["label"] = "RANDOM_avg"
    agg["n_seeds"] = len(ok)
    return agg


# ====================================================================== main
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=28)
    ap.add_argument("--pml", type=int, default=4)
    ap.add_argument("--amp", type=float, default=1.6)
    ap.add_argument("--lam", type=float, default=4.0)
    ap.add_argument("--n-elem", type=int, default=16)
    ap.add_argument("--focal", type=float, default=8.0)
    ap.add_argument("--array-radius", type=float, default=7.0)
    ap.add_argument("--sigma-elem", type=float, default=1.2)
    ap.add_argument("--n-cycles", type=float, default=10.0)
    ap.add_argument("--rec-cycles", type=float, default=6.0)
    ap.add_argument("--sweep", action="store_true", help="τ_relax CLASSIFY sweep")
    ap.add_argument("--n-sweep", action="store_true", help="directivity N_elem sweep (path-B)")
    ap.add_argument("--json", type=str, default="")
    args = ap.parse_args()

    verify_constants()
    print(f"\n=== phased-array u-sector COMPRESSIONAL rectification (Phase 4, SMOKE) ===")
    print(f"N={args.N} pml={args.pml} amp={args.amp} lam={args.lam} n_elem={args.n_elem} "
          f"focal={args.focal} R_array={args.array_radius}")
    print(f"COUPLING ON (disable_cosserat_lc_force=False)  τ_relax=1 (canonical)  "
          f"A_yield=1  c_shear={C_SHEAR_NATIVE} c_L=√2\n")

    common = dict(N=args.N, pml=args.pml, amp=args.amp, lam=args.lam,
                  n_elem=args.n_elem, focal=args.focal, array_radius=args.array_radius,
                  sigma_elem=args.sigma_elem, n_cycles=args.n_cycles,
                  rec_cycles=args.rec_cycles)
    seeds = (1, 2, 3)

    # ----- the four cells: {FOCUSED, RANDOM} × {latch ON, latch OFF}, coupling ON -----
    print("--- coupling ON · the four cells (FOCUSED=ASYM drive, RANDOM=SYM control) ---")
    foc_on = run_condition("FOCUSED", "focused", latch_on=True, coupling_on=True,
                           seed=0, **common)
    foc_off = run_condition("FOCUSED", "focused", latch_on=False, coupling_on=True,
                            seed=0, **common)
    rnd_on = _avg_random(common, latch_on=True, coupling_on=True, seeds=seeds)
    rnd_off = _avg_random(common, latch_on=False, coupling_on=True, seeds=seeds)

    def show(tag, r):
        if r["blew_up"]:
            print(f"  [{tag:14s}] *** BLEW UP (coupling-on A28 runaway) — no measurement ***")
            return
        print(f"  [{tag:14s}] Tpp_dc={r['Tpp_far_dc']:+.3e}  conv={r['conv_dc']:+.3e}  "
              f"P_rad={r['P_rad_mean']:+.3e}  A2_focal={r['A2_focal_max']:.2f}  "
              f"G_geom={r['G_geom_focal']:.2f}  bulk_frac={r['strain_bulk_fraction']:.3f}  "
              f"g_max={r['g_max']:.3f}  |u|={r['u_max']:.1e} |w|={r['omega_max']:.1e}")
    show("FOC latch-ON", foc_on)
    show("FOC latch-OFF", foc_off)
    show("RND latch-ON", rnd_on)
    show("RND latch-OFF", rnd_off)

    blew = any(r["blew_up"] for r in (foc_on, foc_off, rnd_on, rnd_off))

    # ----- the two discriminators -----
    def absratio(a, b):
        return abs(a) / abs(b) if abs(b) > 1e-300 else float("inf")
    rect_ratio = absratio(foc_on["Tpp_far_dc"], rnd_on["Tpp_far_dc"]) if not blew else float("nan")
    latch_gain = absratio(foc_on["Tpp_far_dc"], foc_off["Tpp_far_dc"]) if not blew else float("nan")
    conv_rect = absratio(foc_on["conv_dc"], rnd_on["conv_dc"]) if not blew else float("nan")

    print("\n--- DISCRIMINATORS ---")
    print(f"  rect_ratio  |Tpp_FOCUSED| / |Tpp_RANDOM|  (latch ON) = {rect_ratio:.2f}")
    print(f"      → focusing produces directed momentum the non-focusing control lacks")
    print(f"  latch_gain  |Tpp_FOC_latchON| / |Tpp_FOC_latchOFF|   = {latch_gain:.2f}")
    print(f"      → THE EXOTIC TEST: ≫1 ⇒ the LATCH rectifies (exotic);  ≈1 ⇒ the")
    print(f"        focused momentum is pure radiation pressure (beam-shaping, path B)")
    print(f"  conv streaming ratio (FOC/RND, latch ON)             = {conv_rect:.2f}")

    # ----- beam-shaping thrust (path B) — reported REGARDLESS of A/B/C -----
    print("\n--- DUAL PAYOFF: beam-shaping thrust F = G_geom·P_rad/c_shear (path B) ---")
    if not foc_on["blew_up"]:
        D = foc_on["G_geom_focal"]
        P = abs(foc_on["P_rad_mean"])
        F_shear = D * P / C_SHEAR_NATIVE
        F_long = D * P / C_LONG_NATIVE
        print(f"  directivity G_geom (focal concentration) = {D:.2f}  "
              f"(N_elem={args.n_elem}; random-phase G_geom≈{rnd_on['G_geom_focal']:.2f})")
        print(f"  radiated power P_rad (far-slab axial flux) = {P:.3e} (native)")
        print(f"  F_beam = G_geom·P_rad/c_shear = {F_shear:.3e} (native, c_shear=1)")
        print(f"         = G_geom·P_rad/c_L     = {F_long:.3e} (native, c_L=√2, P-wave alt)")
        print(f"  sector check: focused bulk_frac={foc_on['strain_bulk_fraction']:.3f} "
              f"(u-sector/P-wave if >0.5 — co-located with the latch + observable)")
    else:
        D = P = F_shear = F_long = float("nan")
        print("  *** focused run blew up — beam-shaping number BLOCKED (see verdict) ***")

    # ----- Rule-10 reactance pair + local clock (FOCUSED latch-ON) -----
    if not foc_on["blew_up"]:
        print(f"\n  reactance pair (FOCUSED): C-store strain-E={foc_on['strainE_mean']:.3e}  "
              f"L-store ρ⟨u̇²⟩={foc_on['Udot_mean']:.3e}")
        print(f"  local clock (FOCUSED): A²_peak={foc_on['A2_peak_interior']:.3f}  "
              f"ω_local/ω_drive=√(1−A²)={foc_on['omega_local_frac']:.3f}")

    # ----- optional τ_relax classify sweep (rescue-fill guard) -----
    sweep_out = {}
    if args.sweep and not blew:
        print("\n--- τ_relax CLASSIFY sweep (rescue-fill guard — NOT a value search) ---")
        for mult in (0.25, 0.5, 1.0, 2.0, 4.0):
            f_on = run_condition("FOC", "focused", latch_on=True, coupling_on=True,
                                 tau_mult=mult, seed=0, **common)
            r_on = _avg_random(common, latch_on=True, coupling_on=True, seeds=seeds,
                               tau_mult=mult)
            lg = absratio(f_on["Tpp_far_dc"], foc_off["Tpp_far_dc"])
            rr = absratio(f_on["Tpp_far_dc"], r_on["Tpp_far_dc"])
            tag = " <-- CANONICAL" if mult == 1.0 else ""
            print(f"    τ×{mult:<4}: latch_gain={lg:6.2f}  rect_ratio={rr:6.2f}  "
                  f"g_max={f_on['g_max']:.3f}{tag}")
            sweep_out[str(mult)] = {"latch_gain": lg, "rect_ratio": rr,
                                    "g_max": f_on["g_max"]}

    # ----- optional N_elem directivity sweep (path-B characterization) -----
    n_sweep_out = {}
    if args.n_sweep and not blew:
        print("\n--- directivity sweep: G_geom + F_beam vs N_elem (path-B, geometry) ---")
        for ne in (4, 8, 16, 24):
            kw = dict(common); kw["n_elem"] = ne
            f = run_condition("FOC", "focused", latch_on=True, coupling_on=True,
                              seed=0, **kw)
            if f["blew_up"]:
                print(f"    N_elem={ne:<3}: blew up")
                continue
            Fb = f["G_geom_focal"] * abs(f["P_rad_mean"]) / C_SHEAR_NATIVE
            print(f"    N_elem={ne:<3}: G_geom={f['G_geom_focal']:5.2f}  "
                  f"P_rad={abs(f['P_rad_mean']):.3e}  A2_focal={f['A2_focal_max']:.2f}  "
                  f"F_beam={Fb:.3e}")
            n_sweep_out[str(ne)] = {"G_geom": f["G_geom_focal"],
                                    "P_rad": abs(f["P_rad_mean"]), "F_beam": Fb}

    # ----- steered-beam demo (pure phase-gradient steering, no chirality) -----
    steer = run_condition("STEERED", "steered", latch_on=True, coupling_on=True,
                          seed=0, steer_deg=20.0, **common)
    if not steer["blew_up"]:
        print(f"\n  phase-gradient STEER demo (θ=20°, no chirality): "
              f"Tpp_dc={steer['Tpp_far_dc']:+.3e}  bulk_frac={steer['strain_bulk_fraction']:.3f}")

    # ====================================================================== VERDICT
    print("\n=== VERDICT (prereg §4) ===")
    if blew:
        print("  → BLOCKED: the coupling-ON (disable_cosserat_lc_force=False) config is")
        print("    the A28 runaway-prone path and blew up under the compressional drive.")
        print("    Rectification verdict cannot be cleanly read at coupling-on; see the")
        print("    result doc for the coupling-OFF fallback measurement.")
    else:
        exotic = (latch_gain >= 3.0) and (rect_ratio >= 3.0) \
            and (foc_on["strain_bulk_fraction"] > 0.5)
        if exotic:
            print(f"  → A (CONFIRMED): latch_gain={latch_gain:.2f}≫1 AND rect_ratio="
                  f"{rect_ratio:.2f}≫1, sector-matched (bulk_frac="
                  f"{foc_on['strain_bulk_fraction']:.2f}). The u-sector latch RECTIFIES")
            print(f"    at canonical params — exotic mechanism revived. (→ discrimination-check)")
        elif latch_gain < 3.0:
            print(f"  → B (NO rectification, sector-matched): latch_gain={latch_gain:.2f} ≈ 1 —")
            print(f"    the latch adds ~nothing beyond the focused radiation-pressure baseline.")
            print(f"    The FOCUSED-vs-RANDOM contrast (rect_ratio={rect_ratio:.2f}) is pure")
            print(f"    BEAM-SHAPING (path B), NOT exotic rectification. With the ω-sector")
            print(f"    closed in Phase 3 and the u-sector closed here, ALL sectors are")
            print(f"    exhausted ⇒ exotic rectification DEFINITIVELY DEAD. The beam-shaping")
            print(f"    thrust F=G_geom·P/c_shear (above) is the surviving path-B payoff.")
        else:
            print(f"  → inspect/C: latch_gain={latch_gain:.2f} but rect_ratio={rect_ratio:.2f} "
                  f"or sector mismatch — check the τ-sweep for rescue-fill (C).")
    print("  CAVEAT (ave-driver-script-honesty): SMOKE. Robust = SIGNS/RATIOS/CONTRAST. "
          "Absolute thrust magnitude BLOCKED (converged sim + source-current norm).")

    if args.json:
        with open(args.json, "w") as f:
            json.dump({"args": vars(args),
                       "foc_on": foc_on, "foc_off": foc_off,
                       "rnd_on": rnd_on, "rnd_off": rnd_off, "steered": steer,
                       "rect_ratio": rect_ratio, "latch_gain": latch_gain,
                       "conv_rect": conv_rect,
                       "beam_shaping": {"G_geom": D, "P_rad": P,
                                        "F_shear": F_shear, "F_long": F_long,
                                        "n_elem": args.n_elem},
                       "sweep": sweep_out, "n_sweep": n_sweep_out,
                       "blew_up": blew}, f, indent=2)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
