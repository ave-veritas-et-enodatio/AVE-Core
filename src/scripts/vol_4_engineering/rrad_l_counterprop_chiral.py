#!/usr/bin/env python3
"""
Counter-propagating OPPOSITE-HANDED chiral pair — rarefaction vacuum-pump drive,
dark-wake thrust Phase 5 (the suction half; THE COUNTERACTION).

Phases 1-4 (compression half) ALL returned OUTCOME B with a SINGLE explanatory
mechanism: the measured directed momentum (rho<u_dot^2> radiation-pressure /
streaming) is 2nd-order, EVEN-IN-AMPLITUDE, TIME-symmetric.  Phase 2 found "needs a
hysteretic latch"; Phase 3 found "needs it in the thrust sector"; Phase 4 put it
there (sector-matched, coupling-on) and still got latch_gain=1.0 -> the closing
diagnosis: a substrate rectifier ALSO needs a TEMPORAL symmetry-breaker the carrier
+ plastic-latch never supplied.  All four drove a SINGLE, sector-trapped chirality.

Phase 5 (Grant 2026-06-09: "softening / polarizing / counteracting chirality")
drives the corpus's OWN electron-genesis kinematics SUB-YIELD: two counter-
propagating OPPOSITE-HANDED chiral omega-drives.  Per pair-production-axiom-
derivation.md:51,77 a FULL breach of this configuration tears longitudinal->
transverse ("c_local crashes to zero ... blocked linear KE shatters sideways into
transverse DOF ... contra-rotating vortex dipoles", LH e- + RH e+).  That supplies
BOTH ingredients Phases 1-4 lacked:
  (i)  a SECTOR BRIDGE  (longitudinal<->transverse via the phase-tear at the focal
       interference interface), and
  (ii) a TEMPORAL EVENT (the conversion is an event, not a steady even-in-A drive).
KEPT SUB-YIELD (below the A^2=1 pair-production tear) the conversion is PARTIAL +
directed: energy -> momentum, not rest-mass.

POLARIZING = control the (V_inc, V_ref) phasor trajectory / d-q state.  The Cosserat
realization: the transverse (omega_y, omega_z) phasor loop at the focal interface.
An OPEN / ASYMMETRIC loop has nonzero ENCLOSED AREA == the d-q rectification / the
"Polarization Mismatch" coupling knob (04_chiral_impedance_matching.tex:11).  This is
the temporal symmetry-breaker: a closed (symmetric) loop is time-reversal symmetric
and nets nothing; an open (asymmetric) loop is not.

=========================== substrate-native-check (FIRST, Grant directive) ============
Re-walked because this MODIFIES the drive (single->counter-propagating pair) + the
SECTOR (adds the omega->u phase-tear bridge + rarefaction).  8 checkpoints:

 CP1 dynamics    : time-domain WAVE PROPAGATION on the Cosserat (u,omega) LC-tank via
                   the engine's velocity-Verlet step().  NOT minimization / Helmholtz /
                   Lagrangian.  Two opposing chiral omega-drives + their interference.
 CP2 sector      : Cos-sector, CROSS-COUPLED.  Drive injects omega (microrotation =
                   transverse/shear, 2/7 photon channel).  The counteraction phase-tear
                   is HYPOTHESIZED to bridge omega->u (longitudinal/bulk, 1/7) at the
                   focal interface; rarefaction Tr(eps)=div(u)<0 lives in the u-sector.
                   So coupling MUST be ON (disable_cosserat_lc_force=False) for the
                   omega-drive to produce u-momentum.
 CP3 objective   : NO functional minimized.  Measure (a) net directed interior axial
                   momentum P_x=rho*sum(u_dot_x) [real-space thrust], (b) the phasor-loop
                   ENCLOSED AREA at the focal interface [phase-space asymmetry knob], (c)
                   the pump energy-momentum ledger.  AVE-native: helicity injection +
                   chiral impedance match, not an SM fluid-friction model.
 CP4 phase-space : per A46 the polarization trajectory is a PHASE-SPACE object -> the
                   asymmetry knob (enclosed area) is measured in the (omega_y,omega_z)
                   phasor plane, in matching coordinates.  The thrust is a genuine
                   real-space momentum vector -> measured in real-space.  Both native.
 CP5 local clock : Op14 active (sub-yield, A near but < 1).  Report omega_local =
                   omega_drive*sqrt(1-A^2) at the top-A^2 focal sites.
 CP6 reactance   : time-domain LC.  Record the C-state (transverse omega) AND L-state
                   (omega_dot / u_dot) -> the phasor loop IS the reactance pair traced in
                   phase-space; plus u-sector C (strain-E) and L (rho<u_dot^2>).
 CP7 sampling    : PML-excluded interior; focal interface sampled at the TOP-K |omega|^2
                   density peak (NOT a centroid+offset -> the interference focus is a
                   localized peak).  Both far planes PML-excluded.
 CP8 emergence   : N/A as a hosting test -- and deliberately INVERTED: we do NOT seed /
                   want the finished e-/e+ composite.  Staying SUB-YIELD is exactly NOT
                   nucleating it.  Breaching A^2>=1 == the particle-maker SINK (outcome C).

The rarefaction/tensile limit (the sub-yield bound), substrate-natively:
  - Rarefaction is representable: Tr(eps)=div(u)<0 is below-baseline volumetric strain.
  - Canonical c_eff^2 = c0^2 (1 + rhobar/(1-rhobar^2)), rhobar=delta_rho/rho0 in [-1,1]
    (04_superluminal_transit.tex:86; derived from Ax4, NOT a free parameter).
  - COMPRESSION ceiling: rhobar->+1, c_eff^2->+inf, stiffening (saturation A=1 side).
  - RAREFACTION floor (CAVITATION): c_eff^2->0 at rhobar = (1-sqrt5)/2 = -1/phi ~ -0.618
    (the local light speed crashes -> void); beyond it c_eff^2<0 = tensile failure.
    DERIVED, not tuned.  The ceiling-vs-floor asymmetry IS the substrate's asymmetric
    response (S(A)=sqrt(1-A^2) is even, but c_eff^2(rhobar) is ODD in rhobar).
  - The pair-production tear (the FULL breach) is the A^2=1 / V_SNAP=511kV extreme
    (pair-production-axiom-derivation.md:96).  Stay sub-yield: A^2_focal < 1.

=========================== the HONEST SPINE (ave-driver-script-honesty) ===============
B (symmetric counteraction -> cancels) and C (overunity OR pair-production breach) are
HONEST outcomes -- reported LOUDLY, never rescue-filled toward A.  A requires ALL of:
asymmetric, sub-yield (A^2_focal<1), net directed thrust that SIGN-FLIPS with the
asymmetry, AND the pump ledger closes (no overunity).

Two mandatory controls (prereg sec 6):
  (i)  SYMMETRIC counteraction (equal amp, both circular, Delta_phi=0, exact mirror
       handedness) MUST give zero net momentum -- the symmetric-pair null.
  (ii) SUB-YIELD check: track A^2_focal vs the pair-production threshold.  If net
       "thrust" appears only once A^2_focal breaches 1 -> particle-maker SINK (C).

Prereg : research/2026-06-08_rrad-l-rarefaction-phase5_prereg.md
Phase 4: research/2026-06-08_rrad-l-phased-array-phase4_result.md (OUTCOME B, all sectors)
"""

import argparse
import json
import os
import sys

import numpy as np

# Canonical-source imports (ave-canonical-source: never hard-code constants):
from ave.core.constants import ALPHA, C_0, L_NODE, N_NU, V_LONG, V_SNAP, V_YIELD, Z_0
import ave.core.constants as _avc

from ave.topological.cosserat_field_3d import _compute_curvature, _compute_strain
from ave.topological.vacuum_engine import (
    CosseratBeltramiSource,
    EngineConfig,
    VacuumEngine3D,
)

# Reuse the Phase 2/4 machinery as the single source of truth for the constitutive
# stress, the momentum-flux tensor, the K4-native bulk-vs-shear split, and the
# reservoir energy (NO constitutive-form drift across phases).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rrad_l_acoustic_rectification import (  # noqa: E402
    cosserat_stress,
    momentum_flux_axial,
    source_saturation_max,
    strain_bulk_shear_split,
)
from rrad_l_darkwake_impedance import elastic_energy_density  # noqa: E402

PI = np.pi
PHI = (1.0 + np.sqrt(5.0)) / 2.0
RHOBAR_CAVITATION = (1.0 - np.sqrt(5.0)) / 2.0     # = -1/phi ~ -0.618 (c_eff^2 -> 0)
C_SHEAR_NATIVE = 1.0                               # transverse/photon speed (sqrt(G/rho))
C_LONG_NATIVE = float(V_LONG / C_0)                # P-wave = sqrt(2)*c0 (native sqrt2)


# ------------------------------------------------------------------ canonical-source verify
def verify_constants() -> None:
    """ave-canonical-source Step 4 -- fail loudly on drift of the LOCKED params."""
    assert _avc.__file__.endswith("ave/core/constants.py"), \
        "ave.core.constants is not the AVE-Core canonical source"
    assert abs(N_NU - 2.0 / 7.0) < 1e-12, f"N_NU drifted: {N_NU}"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA drift from CODATA"
    assert abs(C_LONG_NATIVE - np.sqrt(2.0)) < 1e-9, "V_LONG != sqrt(2)*c0 (P-wave)"
    assert abs(RHOBAR_CAVITATION + 1.0 / PHI) < 1e-12, "cavitation floor != -1/phi"
    # the pair-production tear: A^2=1 == V_SNAP; the yield onset == V_YIELD=sqrt(alpha)*V_SNAP
    assert abs(V_YIELD - np.sqrt(ALPHA) * V_SNAP) < 1e-6, "V_YIELD != sqrt(alpha)*V_SNAP"
    print(f"[verify_constants] OK  A_yield=1 (eps_yield)  omega_yield=pi  "
          f"c_shear={C_SHEAR_NATIVE} c_L=sqrt2~{C_LONG_NATIVE:.4f}  Z_0={Z_0:.2f}  "
          f"nu_vac={N_NU:.4f}")
    print(f"[verify_constants] rarefaction floor rhobar_cav = -1/phi = "
          f"{RHOBAR_CAVITATION:.4f} (c_eff^2->0); pair-tear at A^2=1 (V_SNAP={V_SNAP/1e3:.1f}kV, "
          f"V_yield={V_YIELD/1e3:.2f}kV onset)")


# ============================================================ polarized chiral source
class PolarizedChiralSource(CosseratBeltramiSource):
    """Opposite-handed chiral omega-drive with a CONTROLLABLE polarization trajectory.

    Extends CosseratBeltramiSource (the canonical helical-omega Dirichlet-slab drive,
    vacuum_engine.py:832) with the two POLARIZING knobs the counteraction needs:

      - phase0 (Delta_phi) : a temporal phase offset on this source's carrier.  The
            RELATIVE phase between the two counter-propagating drives sets where the
            interference fringe sits AND the handedness of the COMBINED phasor rotation
            at the focal interface.  Delta_phi -> -Delta_phi flips the enclosed-area
            sign (the rectification sign-flip test).
      - ellipticity (b/a) : the minor/major axis ratio of the transverse polarization
            ellipse.  ell=1 -> circular (the original CosseratBeltramiSource).  ell!=1
            -> elliptical -> the combined loop is genuinely OPEN (not merely rotated),
            i.e. nonzero enclosed area == the d-q / Polarization-Mismatch knob.

    With ell=1, phase0=0 this is byte-identical to the parent's circular helical drive
    (the parent's apply() is reused for that path).  The asymmetry is OFF by default;
    it is turned ON only in the ASYM conditions.  Handedness + slab placement give the
    counter-propagation: RH at the left slab radiates +x, LH at the right slab radiates
    -x; the beams overlap (counter-propagate) at the focal interface.
    """

    def __init__(self, *, phase0: float = 0.0, ellipticity: float = 1.0, **kw):
        super().__init__(**kw)
        self.phase0 = float(phase0)
        self.ellipticity = float(ellipticity)

    def apply(self, engine: "VacuumEngine3D", t: float) -> None:
        # Fast path: circular + no phase offset == the canonical parent drive.
        if self.phase0 == 0.0 and self.ellipticity == 1.0:
            return super().apply(engine, t)
        self._init_if_needed(engine)
        env = self.envelope(t)
        if env <= 0:
            return
        amp_current = self.amplitude * env
        ph = self.omega * t + self.phase0
        c_t = np.cos(ph)                          # major axis
        s_t = np.sin(ph) * self._sign * self.ellipticity  # minor axis (ell<1 -> open loop)
        active_slab = self._slab_active_mask(engine)
        pattern = amp_current * self._transverse_profile * active_slab
        ax1, ax2 = self._trans_axes
        slab_view = self._slab_omega_view(engine)
        slab_view[...] = 0.0
        slab_view[..., ax1] = pattern * c_t
        slab_view[..., ax2] = pattern * s_t
        self.cumulative_action_injected += float(np.sum(pattern ** 2) * (c_t ** 2 + s_t ** 2))


# ============================================================ phase-space asymmetry knob
class PhasorLoopRecorder:
    """Record the transverse (omega_y, omega_z) phasor trajectory at the focal interface
    and return its signed ENCLOSED AREA (shoelace) -- the d-q rectification knob (CP4/CP6).

    The focal cell is chosen ONCE (top |omega|^2 interior, PML-excluded -- CP7 density
    peak, not a centroid) after the ramp, then traced over the steady window.  A
    symmetric circular counter-pair traces a (near-)closed loop -> area ~ 0; an open /
    asymmetric loop -> nonzero area == net injected helicity == the temporal symmetry-
    breaker Phases 1-4 lacked.
    """

    def __init__(self, prop_axis: int):
        self.prop_axis = int(prop_axis)
        self._trans = tuple(i for i in (0, 1, 2) if i != prop_axis)
        self.cell = None
        self.wy, self.wz = [], []

    def pick_cell(self, cos, region_mask: np.ndarray) -> None:
        """Top |omega|^2 cell WITHIN the focal-interface region (CP7 density peak, NOT a
        source slab -- the loop must trace the interference focus, not the drive)."""
        w2 = np.sum(cos.omega ** 2, axis=-1)
        flat = np.where(region_mask & cos.mask_alive, w2, -1.0).ravel()
        idx = int(np.argmax(flat))
        self.cell = np.unravel_index(idx, w2.shape)

    def record(self, cos) -> None:
        if self.cell is None:
            return
        ax1, ax2 = self._trans
        self.wy.append(float(cos.omega[self.cell][ax1]))
        self.wz.append(float(cos.omega[self.cell][ax2]))

    def enclosed_area(self) -> float:
        if len(self.wy) < 4:
            return float("nan")
        y = np.array(self.wy)
        z = np.array(self.wz)
        # shoelace over the closed polyline (wrap last->first)
        return float(0.5 * np.sum(y * np.roll(z, -1) - z * np.roll(y, -1)))

    def amplitude(self) -> float:
        if not self.wy:
            return float("nan")
        return float(np.sqrt(np.mean(np.array(self.wy) ** 2 + np.array(self.wz) ** 2)))


# ============================================================ rarefaction diagnostic
def rarefaction_state(cos, region) -> dict:
    """Volumetric strain Tr(eps)=div(u) over an interior region -> the rarefaction
    (suction) side.  rhobar ~ Tr(eps) (normalized volumetric strain, the
    04_superluminal_transit.tex:86 variable).  Reports the deepest rarefaction
    min(Tr(eps)) and whether it reaches the cavitation floor rhobar_cav=-1/phi.
    """
    eps = np.asarray(_compute_strain(cos.u, cos.omega, cos.dx))
    tr = eps[..., 0, 0] + eps[..., 1, 1] + eps[..., 2, 2]
    vals = tr[region]
    if vals.size == 0:
        return {"tr_min": float("nan"), "tr_max": float("nan"),
                "rarefied_frac": float("nan"), "cavitation_reached": False}
    tr_min = float(np.min(vals))
    return {"tr_min": tr_min, "tr_max": float(np.max(vals)),
            "rarefied_frac": float(np.mean(vals < 0.0)),       # fraction in suction
            "cavitation_reached": bool(tr_min <= RHOBAR_CAVITATION)}


# ============================================================ pump energy-momentum ledger
def field_energy(cos, region) -> dict:
    """Interior field energy split: elastic (C-store) + kinetic (L-store).  The
    overunity check: in steady state the kinetic store must PLATEAU (input balances PML
    loss); a persistent positive drift relative to the pump input == free energy."""
    U_elastic = elastic_energy_density(cos)
    ke = 0.5 * cos.rho * np.sum(cos.u_dot ** 2, axis=-1)        # u-sector kinetic
    rot = 0.5 * np.sum(cos.omega ** 2, axis=-1)                 # rotational store
    return {"E_elastic": float(np.sum(U_elastic[region])),
            "E_kin_u": float(np.sum(ke[region])),
            "E_rot": float(np.sum(rot[region]))}


# ============================================================ one condition run
def run_condition(label: str, asym: float, *, both_rh: bool = False,
                  coupling_on: bool = True, N: int = 28, pml: int = 4,
                  amp: float = 0.55, lam: float = 4.0, n_cycles: float = 14.0,
                  rec_cycles: float = 8.0, imbal: float = 0.5) -> dict:
    """Two counter-propagating opposite-handed chiral drives meeting at the focal
    interface, swept by a single SIGNED asymmetry knob `asym` = AMPLITUDE IMBALANCE.

    DERIVATION (why amplitude imbalance is the ONLY knob that opens the d-q loop):
    two EQUAL-amplitude counter-propagating OPPOSITE-handed circular beams superpose,
    at the focal point, to a LINEAR (zero-enclosed-area) standing polarization for ANY
    relative phase -- cos(t)+cos(t+phi) and sin(t)-sin(t+phi) are both proportional to
    cos(t+phi/2), i.e. a tilted LINE.  So phase/ellipticity cannot open the combined
    phasor loop; only an AMPLITUDE imbalance (a != b) makes the superposition elliptical
    with nonzero enclosed area (signed by which beam dominates).  The symmetric-pair null
    is therefore STRUCTURAL (a=b -> linear -> area 0), not a tuned coincidence.

      asym = 0  -> SYMMETRIC: equal amplitude, mirror handedness -> linear standing pol
                   -> zero enclosed area -> the mandatory symmetric-pair NULL.
      asym > 0  -> amp_L = amp(1 + imbal*asym) > amp_R -> open loop one way (left dominates).
      asym < 0  -> amp_R dominates -> loop opens the OTHER way -> directed momentum flips.

    THE CONFOUND this exposes: amplitude imbalance ALSO just means the stronger beam
    pushes harder (unbalanced radiation pressure).  So a nonzero net Px is NOT by itself
    chiral rectification.  The discriminator is opposite-handed-vs-co-handed at the SAME
    imbalance (both_rh) + coupling-on-vs-off: a chiral d-q rectification must EXCEED the
    co-handed unbalanced-push baseline AND need the omega->u coupling.

    both_rh=True : co-handed control (both RH, same imbalance) = the unbalanced-push
                   baseline; opposite-handed minus this = the chiral rectification, if any.
    """
    cfg = EngineConfig(
        N=N, pml=pml, temperature=0.0,
        use_asymmetric_saturation=True,        # chiral S_mu != S_eps path (asymmetric medium)
        disable_cosserat_lc_force=(not coupling_on),  # coupling ON => omega->u phase-tear bridge
        enable_cosserat_self_terms=(not coupling_on),
    )
    engine = VacuumEngine3D(cfg)
    prop_axis = 0
    src_xL = pml + 2
    src_xR = N - pml - 3
    omega_drive = 2.0 * PI / lam
    carrier_period = lam
    n_steps = int((3.0 + n_cycles) * carrier_period)   # 3 ramp cycles + n_cycles
    t_ramp = 3.0 * carrier_period
    t_sustain = n_steps * float(engine.outer_dt) + carrier_period
    sigma_yz = max(2.0, N / 8.0)

    hand_R = "RH" if both_rh else "LH"
    amp_L = amp * (1.0 + imbal * asym)        # left dominates for asym>0 (opens the loop +)
    amp_R = amp * (1.0 - imbal * asym)        # right dominates for asym<0 (opens the loop -)

    # LEFT drive: RH, circular (radiates +x toward the focal interface)
    src_left = PolarizedChiralSource(
        x0=src_xL, propagation_axis=prop_axis, amplitude=amp_L, omega=omega_drive,
        handedness="RH", sigma_yz=sigma_yz, t_ramp=t_ramp, t_sustain=t_sustain,
        phase0=0.0, ellipticity=1.0)
    # RIGHT drive: LH (counteraction), circular (radiates -x toward the focal interface)
    src_right = PolarizedChiralSource(
        x0=src_xR, propagation_axis=prop_axis, amplitude=amp_R, omega=omega_drive,
        handedness=hand_R, sigma_yz=sigma_yz, t_ramp=t_ramp, t_sustain=t_sustain,
        phase0=0.0, ellipticity=1.0)
    engine.add_source(src_left)
    engine.add_source(src_right)
    drives = (src_left, src_right)

    cos = engine.cos
    interior = slice(pml, N - pml)
    interior3 = (interior, interior, interior)
    far_left = slice(pml + 1, pml + 3)            # PML-excluded near-left boundary plane
    far_right = slice(N - pml - 3, N - pml - 1)    # PML-excluded near-right boundary plane
    focal_x = (src_xL + src_xR) // 2
    focal_slab = (slice(focal_x - 1, focal_x + 2), interior, interior)
    focal_region = np.zeros((N, N, N), dtype=bool)
    focal_region[focal_x - 1:focal_x + 2, interior, interior] = True
    focal_region &= cos.mask_alive

    rec_steps = int(rec_cycles * carrier_period)
    record_start = n_steps - rec_steps

    loop = PhasorLoopRecorder(prop_axis)
    Px_series, gL_series, gR_series = [], [], []
    A2focal_series, bulk_series = [], []
    Eel_series, Ekin_series, Erot_series = [], [], []
    tr_min_series, rar_frac_series = [], []
    cav_reached = False
    blew_up = False
    cell_picked = False

    for step in range(n_steps):
        engine.step()
        umax = float(np.abs(cos.u).max())
        wmax = float(np.abs(cos.omega).max())
        if not np.isfinite(umax) or not np.isfinite(wmax) or umax > 1e3 or wmax > 1e3:
            blew_up = True
            break
        if step >= record_start:
            if not cell_picked:
                loop.pick_cell(cos, focal_region)
                cell_picked = True
            loop.record(cos)
            alive = cos.mask_alive
            ux_dot = cos.u_dot[..., prop_axis]
            Px_series.append(float(cos.rho * np.sum((ux_dot * alive)[interior3])))
            # signed boundary momentum density (which way momentum leaves each end)
            gL_series.append(float(cos.rho * np.sum((ux_dot * alive)[(far_left, interior, interior)])))
            gR_series.append(float(cos.rho * np.sum((ux_dot * alive)[(far_right, interior, interior)])))
            A2focal_series.append(source_saturation_max(cos, focal_slab))
            ss = strain_bulk_shear_split(cos, slice(focal_x - 1, focal_x + 2), interior)
            bulk_series.append(ss["strain_bulk_fraction"])
            fe = field_energy(cos, interior3)
            Eel_series.append(fe["E_elastic"]); Ekin_series.append(fe["E_kin_u"])
            Erot_series.append(fe["E_rot"])
            rar = rarefaction_state(cos, focal_region)
            tr_min_series.append(rar["tr_min"]); rar_frac_series.append(rar["rarefied_frac"])
            cav_reached = cav_reached or rar["cavitation_reached"]

    W_in = sum(getattr(s, "cumulative_action_injected", 0.0) for s in drives)

    if blew_up or not Px_series:
        return {"label": label, "asym": asym, "both_rh": both_rh,
                "coupling_on": coupling_on, "blew_up": True, "n_rec": 0,
                "Px_mean": float("nan"), "Px_drift": float("nan"),
                "gL_mean": float("nan"), "gR_mean": float("nan"),
                "loop_area": float("nan"), "loop_amp": float("nan"),
                "A2_focal_max": float("nan"), "bulk_frac": float("nan"),
                "tr_min": float("nan"), "rarefied_frac": float("nan"),
                "cavitation_reached": False, "W_in": W_in,
                "E_kin_mean": float("nan"), "E_kin_drift": float("nan"),
                "u_max": umax, "omega_max": wmax}

    Px = np.array(Px_series)
    steps_axis = np.arange(len(Px), dtype=float)
    Px_drift = float(np.polyfit(steps_axis, Px, 1)[0]) if len(Px) > 2 else float("nan")
    Ekin = np.array(Ekin_series)
    Ekin_drift = float(np.polyfit(steps_axis, Ekin, 1)[0]) if len(Ekin) > 2 else float("nan")
    # hard overunity: total field energy must never exceed cumulative pumped work
    E_field_total = (float(np.mean(Eel_series)) + float(np.mean(Ekin_series))
                     + float(np.mean(Erot_series)))

    return {
        "label": label, "asym": asym, "both_rh": both_rh, "coupling_on": coupling_on,
        "blew_up": False, "n_rec": int(len(Px)),
        "Px_mean": float(np.mean(Px)),                 # PRIMARY net directed momentum
        "Px_drift": Px_drift,                          # net force (momentum/step)
        "gL_mean": float(np.mean(gL_series)),          # signed efflux left end
        "gR_mean": float(np.mean(gR_series)),          # signed efflux right end
        "loop_area": loop.enclosed_area(),             # PHASE-SPACE asymmetry knob (CP4)
        "loop_amp": loop.amplitude(),
        "A2_focal_max": float(np.max(A2focal_series)), # sub-yield check
        "bulk_frac": float(np.mean(bulk_series)),      # sector bridge omega->u check
        "tr_min": float(np.min(tr_min_series)),        # deepest rarefaction (suction)
        "rarefied_frac": float(np.mean(rar_frac_series)),
        "cavitation_reached": bool(cav_reached),
        "W_in": float(W_in),                           # pump work-in (cumulative action)
        "E_field_total": E_field_total,                # elastic+kinetic+rot (overunity vs W_in)
        "E_over_Win": float(E_field_total / W_in) if W_in > 0 else float("nan"),
        "E_kin_mean": float(np.mean(Ekin)),
        "E_kin_drift": Ekin_drift,                     # steady-state plateau check (informational)
        "E_elastic_mean": float(np.mean(Eel_series)),
        "E_rot_mean": float(np.mean(Erot_series)),
        "u_max": float(np.abs(cos.u).max()), "omega_max": float(np.abs(cos.omega).max()),
    }


# ====================================================================== main
def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=28)
    ap.add_argument("--pml", type=int, default=4)
    ap.add_argument("--amp", type=float, default=0.55, help="per-drive peak |omega| (sub-yield)")
    ap.add_argument("--lam", type=float, default=4.0)
    ap.add_argument("--n-cycles", type=float, default=14.0)
    ap.add_argument("--rec-cycles", type=float, default=8.0)
    ap.add_argument("--asym", type=float, default=1.0, help="asymmetry magnitude for ASYM+/-")
    ap.add_argument("--amp-sweep", action="store_true", help="sub-yield-vs-breach amplitude sweep")
    ap.add_argument("--json", type=str, default="")
    args = ap.parse_args()

    verify_constants()
    print(f"\n=== counter-propagating OPPOSITE-HANDED chiral pair (Phase 5, SMOKE) ===")
    print(f"N={args.N} pml={args.pml} amp(per-drive)={args.amp} lam={args.lam}  "
          f"coupling ON (omega->u phase-tear bridge)\n")

    kw = dict(N=args.N, pml=args.pml, amp=args.amp, lam=args.lam,
              n_cycles=args.n_cycles, rec_cycles=args.rec_cycles)

    # ---- the conditions: SYM null + ASYM+/- (sign-flip) + co-handed control ----
    sym = run_condition("SYM (mirror, circular)", 0.0, **kw)
    ap_p = run_condition("ASYM+ (open loop +)", +abs(args.asym), **kw)
    ap_m = run_condition("ASYM- (open loop -)", -abs(args.asym), **kw)
    cohand = run_condition("CO-HANDED (both RH, asym+)", +abs(args.asym), both_rh=True, **kw)
    coup_off = run_condition("ASYM+ coupling-OFF", +abs(args.asym), coupling_on=False, **kw)

    def show(r):
        if r["blew_up"]:
            print(f"  [{r['label']:30s}] *** BLEW UP (|u|={r['u_max']:.1e} |w|={r['omega_max']:.1e}) ***")
            return
        print(f"  [{r['label']:30s}] Px={r['Px_mean']:+.3e} drift={r['Px_drift']:+.2e}  "
              f"loop_area={r['loop_area']:+.3e}  A2_foc={r['A2_focal_max']:.3f}  "
              f"bulk={r['bulk_frac']:.3f}  tr_min={r['tr_min']:+.3f}  "
              f"E_kin_drift={r['E_kin_drift']:+.2e}")
    print("--- conditions (Px = net directed interior momentum; loop_area = d-q knob) ---")
    for r in (sym, ap_p, ap_m, cohand, coup_off):
        show(r)

    blew = any(r["blew_up"] for r in (sym, ap_p, ap_m))

    # ---------------------------------------------------------- discriminators
    def absr(a, b):
        return abs(a) / abs(b) if abs(b) > 1e-300 else float("inf")

    print("\n--- DISCRIMINATORS (prereg sec 4-6) ---")
    if not blew:
        # PRIMARY directed-momentum observable = the SIGN-FLIPPING (rectified) part,
        # extracted by the asymmetry-antisymmetric combination (Phase-2 lesson: the raw
        # interior Px is common-mode transient-fill contaminated; the part that REVERSES
        # when the asymmetry reverses is the genuine rectification):
        #   J_rect = (Px(ASYM+) - Px(ASYM-)) / 2   (flips sign with asym -> the thrust)
        #   J_cm   = (Px(ASYM+) + Px(ASYM-)) / 2   (common-mode fill offset, non-directed)
        # rectified (sign-flipping) net directed momentum and its common-mode fill:
        J_rect = 0.5 * (ap_p["Px_mean"] - ap_m["Px_mean"])
        J_cm = 0.5 * (ap_p["Px_mean"] + ap_m["Px_mean"])
        sym_floor = abs(sym["Px_mean"])
        rect_over_sym = absr(J_rect, sym_floor)
        sign_flip = (np.sign(ap_p["Px_mean"]) == -np.sign(ap_m["Px_mean"])
                     and abs(ap_p["Px_mean"]) > 0 and abs(ap_m["Px_mean"]) > 0)
        loop_flip = (np.sign(ap_p["loop_area"]) == -np.sign(ap_m["loop_area"]))
        # THE CENTRAL A-GATE -- chiral d-q rectification vs mundane unbalanced push:
        # at the SAME amplitude imbalance, opposite-handed (chiral) minus co-handed (pure
        # push baseline).  If they match -> the net momentum is just unbalanced radiation
        # pressure (B, AVE reduces to mundane); if opposite-handed >> co-handed AND it
        # needs the omega->u coupling -> a genuine chiral rectification (candidate A).
        push_baseline = cohand["Px_mean"]
        J_chiral = ap_p["Px_mean"] - push_baseline
        chiral_over_push = absr(J_chiral, push_baseline)
        coupling_sens = absr(ap_p["Px_mean"] - coup_off["Px_mean"], ap_p["Px_mean"])
        # (ii) sub-yield: net present while A^2_focal < 1 (no breach)
        sub_yield = ap_p["A2_focal_max"] < 1.0
        overunity = ap_p["E_over_Win"] > 1.0       # HARD: field energy must not exceed work
        print(f"  CENTRAL A-GATE chiral-vs-push: Px(opp-handed)={ap_p['Px_mean']:+.3e}  "
              f"Px(co-handed)={push_baseline:+.3e}  J_chiral=Px_opp-Px_co={J_chiral:+.3e}  "
              f"|J_chiral|/|push|={chiral_over_push:.2f}")
        print(f"      => chiral_over_push >> 1 AND needs coupling => candidate A; "
              f"~0 (opp ~ co) => mundane unbalanced radiation pressure (B)")
        print(f"  coupling on vs off    : Px(ON)={ap_p['Px_mean']:+.3e}  "
              f"Px(OFF)={coup_off['Px_mean']:+.3e}  |sens|={coupling_sens:.3f}  "
              f"(~0 => omega->u phase-tear NOT involved => no sector bridge)")
        print(f"  (i) symmetric NULL    : Px_SYM={sym['Px_mean']:+.3e}  "
              f"|J_rect|/|Px_SYM|={rect_over_sym:.2f}   J_rect={J_rect:+.3e} J_cm={J_cm:+.3e}")
        print(f"  phase-space d-q loop  : area(SYM)={sym['loop_area']:+.2e} "
              f"area(ASYM+)={ap_p['loop_area']:+.2e} area(ASYM-)={ap_m['loop_area']:+.2e}  "
              f"opens={abs(ap_p['loop_area'])>3*abs(sym['loop_area'])} flips={loop_flip}")
        print(f"  (ii) SUB-YIELD        : A2_focal(ASYM+)={ap_p['A2_focal_max']:.3f}  "
              f"sub_yield={sub_yield}  cavitation_reached={ap_p['cavitation_reached']}  "
              f"(pair-tear at A2=1)")
        print(f"  ledger / overunity    : W_in={ap_p['W_in']:.3e}  "
              f"E_field_total={ap_p['E_field_total']:.3e}  E_field/W_in={ap_p['E_over_Win']:.3e}  "
              f"overunity={overunity}  (E_kin_drift={ap_p['E_kin_drift']:+.2e} -> 0 = settled)")
        print(f"  sector bridge omega->u: bulk_frac(ASYM+)={ap_p['bulk_frac']:.3f} "
              f"(focal interference is naturally compressional; check vs coupling sens)")
        print(f"  rarefaction (suction) : tr_min={ap_p['tr_min']:+.3f}  "
              f"rarefied_frac={ap_p['rarefied_frac']:.3f}  "
              f"(cavitation floor rhobar_cav={RHOBAR_CAVITATION:.3f}; sub-cavitation)")
    else:
        J_rect = J_chiral = chiral_over_push = coupling_sens = float("nan")
        rect_over_sym = sign_flip = sub_yield = overunity = float("nan")
        print("  *** core conditions blew up -- discriminators BLOCKED ***")

    # ---------------------------------------------------------- sub-yield-vs-breach amp sweep
    sweep_out = {}
    if args.amp_sweep and not blew:
        print("\n--- amplitude sweep: does net thrust need the pair-production breach? (control ii) ---")
        for a in (0.3, 0.45, 0.6, 0.8, 1.1):
            kw2 = dict(kw); kw2["amp"] = a
            rp = run_condition(f"ASYM+ amp={a}", +abs(args.asym), **kw2)
            rm = run_condition(f"ASYM- amp={a}", -abs(args.asym), **kw2)
            if rp["blew_up"]:
                print(f"    amp={a:<4}: blew up"); continue
            flip = (np.sign(rp["Px_mean"]) == -np.sign(rm["Px_mean"]))
            tag = " <-- SUB-YIELD" if rp["A2_focal_max"] < 1.0 else " <-- BREACHED (C-zone)"
            print(f"    amp={a:<4}: A2_foc={rp['A2_focal_max']:.3f}  Px+={rp['Px_mean']:+.2e}  "
                  f"Px-={rm['Px_mean']:+.2e}  flip={flip}  loop_area={rp['loop_area']:+.2e}{tag}")
            sweep_out[str(a)] = {"A2_focal": rp["A2_focal_max"], "Px_p": rp["Px_mean"],
                                 "Px_m": rm["Px_mean"], "flip": bool(flip),
                                 "loop_area": rp["loop_area"]}

    # ====================================================================== VERDICT
    print("\n=== VERDICT (prereg sec 5) ===")
    if blew:
        print("  -> BLOCKED: core conditions blew up; see result doc for the stable regime.")
    else:
        # A = chiral rectification clears the mundane unbalanced-push baseline AND needs
        # the omega->u coupling, sub-yield, ledger-closed.  Pure push (opp ~ co, no
        # coupling sensitivity) = B.
        chiral_clears = (chiral_over_push >= 1.0) and (coupling_sens >= 0.25)
        verdict_A = (chiral_clears and sign_flip and sub_yield and (not overunity)
                     and (not ap_p["cavitation_reached"]))
        if verdict_A:
            print(f"  -> A (REAL): the OPPOSITE-handed (chiral) counteraction nets directed "
                  f"momentum BEYOND the co-handed unbalanced-push baseline "
                  f"(|J_chiral|/|push|={chiral_over_push:.1f}), it NEEDS the omega->u coupling "
                  f"(sens={coupling_sens:.2f}), stays SUB-YIELD (A2={ap_p['A2_focal_max']:.2f}<1), "
                  f"ledger closes. A counter-rotating cavitating vacuum PUMP -- a pump, not a warp.")
        elif overunity:
            print(f"  -> C (SINK/CRANK -- OVERUNITY): total field energy exceeds pumped work "
                  f"(E_field/W_in={ap_p['E_over_Win']:.2f}>1). Ledger violated -> free energy. "
                  f"NOT a thruster.")
        elif chiral_clears and not sub_yield:
            print(f"  -> C (SINK/CRANK -- PAIR-PRODUCTION BREACH): net chiral 'thrust' only with "
                  f"A2_focal={ap_p['A2_focal_max']:.2f}>=1 -> energy goes to rest-mass (e-/e+), "
                  f"a particle-MAKER not a drive.")
        else:
            print(f"  -> B (DEAD): the counteraction nets NO chiral directed momentum beyond "
                  f"mundane unbalanced radiation pressure (|J_chiral|/|push|={chiral_over_push:.2f}; "
                  f"opp-handed ~ co-handed; coupling sensitivity={coupling_sens:.2f}~0). The net "
                  f"Px is just the stronger beam pushing harder -- AVE-reduces to ordinary "
                  f"radiation pressure. The symmetric pair nulls STRUCTURALLY (equal beams -> "
                  f"linear standing pol -> zero d-q area). Same single mechanism as Phases 1-4: "
                  f"no temporal symmetry-breaker reaches the directed u-sector momentum.")
    print("  CAVEAT (ave-driver-script-honesty): SMOKE. Robust = SIGNS / RATIOS / SYM-vs-ASYM "
          "CONTRAST / sign-flip. Absolute thrust (Newtons) + absolute-Joules ledger BLOCKED "
          "(converged sim + source-current normalization, same gate as Phases 1-4).")

    if args.json:
        with open(args.json, "w") as f:
            json.dump({"args": vars(args), "sym": sym, "asym_p": ap_p, "asym_m": ap_m,
                       "cohanded": cohand, "coupling_off": coup_off,
                       "amp_sweep": sweep_out, "blew_up": blew}, f, indent=2)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
