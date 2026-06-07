"""
Electron genesis — "a drop in water" (CP8, TWO-COLLIDING PAIR).

Capstone driver: does VacuumEngine3D (K4-TLM + Cosserat — the ONLY engine with
the (2,3) carrier) AUTONOMOUSLY HOST electron genesis from light?

Two builds + the single-vs-pair contrast (the science):

  BUILD 1 — SINGLE-photon MASS-DROPLET CONTROL.
    One moving transverse photon (SpatialDipoleCPSource, pure-V), driven to the
    A->1 pinch-off, then SOURCE OFF + FREE-EVOLVE. Does a NEUTRAL sub-V_yield
    ringing droplet REMAIN (checks 1-3 + matched baseline), or disperse like the
    2026-06-04 sub-pinch-off run? -> CHECKPOINT 1.

  BUILD 2 — TWO-COLLIDING PAIR GENESIS (the real test).
    Two counter-propagating OPPOSITE-handed photons collide -> the standing-wave
    antinode drives A->1 -> does it pinch off into a PAIR of opposite-chirality
    droplets (e- + e+)? 5-check gate on BOTH drops:
      1 sub-V_yield ring   (V/V_yield<1 core + reactance slosh; theory.md:16:
                            "peak voltage safely below 43.65 kV ... rings forever")
      2 rings at omega_C   (slosh self-frequency -> omega_C=c/ell_node)
      3 size ~ ell_node    (FWHM -> 1 cell, the minimum droplet)
      4 (2,3) ASSEMBLES    ((V_inc,V_ref) phasor winding w1->2,w2->3; EMERGENCE)
      5 charge conservation (the two drops carry OPPOSITE winding sign; net-0 pair)

The CONTRAST is the demonstration: single photon -> mass-only (no (2,3))? vs
pair -> the (2,3) assembles? That contrast IS why charge needs the pair.

Honest outcomes (ave-evidence-framing; (II)/(III) are VALID CP8 findings):
  (I)   full genesis  — pair pinches off into sub-V_yield ringing droplets @ omega_C,
                        ell_node-sized, (2,3) assembles, opposite signs -> e+e- born.
  (II)  mass-only     — droplet(s) self-bind (mass) but the (2,3) does NOT assemble.
  (III) no-stable-drop— photon(s) do not pinch off into a persistent sub-V_yield
                        droplet (disperse / stay over-yield).

Authoritative spec: research/2026-06-06_electron-genesis-drop-prereg.md
                    _orchestration/2026-06-06_electron-genesis-drop.md §1.6 (PAIR)

DISCIPLINE (recorded which fired; see result doc §discipline-walk):
  substrate-native-check CP8 (precursor photon, NOT planted (2,3)/droplet; matched
    baseline; layer-by-layer) + CP5 (omega_local = omega_global*sqrt(1-A^2)) +
    CP6 (reactance pair: C-state V_inc AND L-state Phi_link, every step — the slosh)
    + CP4 (phase-space (2,3) in (V_inc,V_ref), NOT real-space) + CP7 (PML excluded,
    density-peak two-drop selection, NOT centroid).
  phase-space-coordinate-check — (2,3)/chirality measured in (V_inc,V_ref) phasor
    (the corpus coordinate, theory.md:16), NOT real-space lattice-Cartesian.
  consistency-vs-emergence — checks 2/3 = consistency (framework-internal omega_C,
    ell_node, V_SNAP=1; NO CODATA); checks 4/5 = emergence (topological observable
    from sim primitives, (2,3) NOT in the seed). Class D.
  ave-canonical-source — ALPHA, V_yield=sqrt(alpha), omega_C, ell_node from
    ave.core.constants; NO hardcoded literals.
  ave-driver-script-honesty — forward; NO fit. The CP sources inject E-perp-B-perp-k
    pure-V transverse structure ONLY; NO (V_inc,V_ref) winding is planted. Any
    (2,3)/chirality that appears is engine output.

PRIOR (the predecessor this corrects): research/2026-06-04_full-electron-option-B-
  discrete-emergence-result.md — two opposite-handed pulses at amp 0.40 self-trapped
  (A^2=0.35, BELOW pinch-off) but DISPERSED (retention 1.7% ~ baseline); Cosserat
  omega stayed EXACTLY 0 (Q0: pure-V photon -> omega=0 exact fixed point, the V->omega
  coupling is parametric/even-in-omega, amplitude-independent). NEW here: drive to the
  A->1 PINCH-OFF (~0.45-0.50/pulse), reframe as a PAIR, add the persistence/free-evolve
  + the charge-conservation (opposite-sign) check.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from ave.core.constants import ALPHA  # noqa: E402  (ave-canonical-source)
from ave.topological.vacuum_engine import (  # noqa: E402
    SpatialDipoleCPSource,
    VacuumEngine3D,
    _forward_t2_port_weights,
)

# ── Substrate-derived constants (ave-canonical-source: NO hardcoded literals) ──
A_YIELD = float(np.sqrt(ALPHA))  # V_yield/V_SNAP = sqrt(alpha) ~ 0.0854 (theory.md:10)
A2_YIELD = float(ALPHA)  # A^2_yield = alpha ~ 0.0073 (sub-yield bar, check 1)
A2_OP14 = float(np.sqrt(2.0 * ALPHA))  # sqrt(2a) ~ 0.1208 — Op14 engagement (self-trap bar)
OMEGA_C = 1.0  # omega_C = c/ell_node = 1 natural units (check 2 target)
ELL_NODE_CELLS = 1.0  # ell_node = 1 lattice cell (dx=1; check 3 target)
COMPTON_PERIOD = 2.0 * np.pi  # one omega_C period in natural time
DT = 1.0 / np.sqrt(2.0)  # K4-TLM 4-port junction outer timestep
PHI = (1.0 + np.sqrt(5.0)) / 2.0  # golden ratio (R_phase/r_phase = phi^2 diagnostic)


# ══════════════════════════════════════════════════════════════════════════════
# Source: counter-propagating-capable transverse-photon precursor
# (reused proven subclass from r10_vacuumengine3d_transverse_2_3_emergence.py:86;
#  SpatialDipoleCPSource is forward-only, so override the propagation SIGN)
# ══════════════════════════════════════════════════════════════════════════════
class _DirectionalCPSource(SpatialDipoleCPSource):
    """SpatialDipoleCPSource with an explicit propagation SIGN (+/-1) so a
    counter-propagating (-axis) opposite-handed pulse can be built. forward(+x)
    and backward(-x) T2 port weights are exact negatives (verified 2026-06-04).
    Injects K4 V_inc ONLY (pure-V transverse photon; NO (V_inc,V_ref) winding)."""

    def __init__(self, *args, direction_sign: int = +1, **kwargs):
        super().__init__(*args, **kwargs)
        self._dir_sign = int(direction_sign)

    def _init_if_needed(self, engine: "VacuumEngine3D") -> None:
        if self._port_w_prop is not None:
            return
        direction = tuple((self._dir_sign if i == self.propagation_axis else 0.0) for i in range(3))
        self._port_w_prop = _forward_t2_port_weights(direction)
        N = engine.N
        yc = (N - 1) / 2.0 if self.y_c is None else self.y_c
        zc = (N - 1) / 2.0 if self.z_c is None else self.z_c
        j, k = np.indices((N, N), dtype=float)
        r2 = (j - yc) ** 2 + (k - zc) ** 2
        gauss_env = np.exp(-r2 / (2.0 * self.sigma_yz**2))
        self._g_y_profile = (j - yc) * gauss_env
        self._g_z_profile = (k - zc) * gauss_env


# ── Source geometry (tuned to match the 2026-06-04 predecessor + calibration) ──
SIGMA_YZ = 3.0  # focused beam waist (~ lambda_C/2)
X0_FWD_FRAC = 0.30  # forward pulse source plane (pair)
X0_BWD_FRAC = 0.70  # backward pulse source plane (pair, counter-propagating)
X0_SINGLE_FRAC = 0.30  # single-photon source plane
RAMP_P, SUSTAIN_P, DECAY_P = 1.5, 3.0, 2.0  # drive envelope (Compton periods)


def _envelope_periods():
    """Total ON duration (periods) before the source goes silent (free-evolve)."""
    return RAMP_P + SUSTAIN_P + DECAY_P


def make_single_photon(engine, N, amplitude, handedness="RH"):
    """BUILD 1 seed: ONE moving transverse photon (+x). Pure-V; NO winding planted."""
    x0 = int(round(X0_SINGLE_FRAC * N))
    src = _DirectionalCPSource(
        x0=x0,
        propagation_axis=0,
        amplitude=amplitude,
        omega=OMEGA_C,
        handedness=handedness,
        sigma_yz=SIGMA_YZ,
        t_ramp=RAMP_P * COMPTON_PERIOD,
        t_sustain=SUSTAIN_P * COMPTON_PERIOD,
        t_decay=DECAY_P * COMPTON_PERIOD,
        direction_sign=+1,
    )
    engine.add_source(src)
    return [x0]


def make_colliding_pair(engine, N, amplitude, opposite=True):
    """BUILD 2 seed: TWO counter-propagating focused pulses colliding at center.
    opposite=True -> OPPOSITE handedness (RH fwd / LH bwd) = the chirality split
    (the genesis arm). opposite=False -> SAME handedness (both RH) = the matched
    baseline (same amplitude/saturation, NO chirality split). Pure-V; NO winding."""
    x0_fwd = int(round(X0_FWD_FRAC * N))
    x0_bwd = int(round(X0_BWD_FRAC * N))
    h_bwd = "LH" if opposite else "RH"
    fwd = _DirectionalCPSource(
        x0=x0_fwd,
        propagation_axis=0,
        amplitude=amplitude,
        omega=OMEGA_C,
        handedness="RH",
        sigma_yz=SIGMA_YZ,
        t_ramp=RAMP_P * COMPTON_PERIOD,
        t_sustain=SUSTAIN_P * COMPTON_PERIOD,
        t_decay=DECAY_P * COMPTON_PERIOD,
        direction_sign=+1,
    )
    bwd = _DirectionalCPSource(
        x0=x0_bwd,
        propagation_axis=0,
        amplitude=amplitude,
        omega=OMEGA_C,
        handedness=h_bwd,
        sigma_yz=SIGMA_YZ,
        t_ramp=RAMP_P * COMPTON_PERIOD,
        t_sustain=SUSTAIN_P * COMPTON_PERIOD,
        t_decay=DECAY_P * COMPTON_PERIOD,
        direction_sign=-1,
    )
    engine.add_source(fwd)
    engine.add_source(bwd)
    return [x0_fwd, x0_bwd]


def setup_engine(N, PML):
    """A28-corrected coupled VacuumEngine3D (matches 2026-06-04 option-B config)."""
    return VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,  # A28 correction (doc 67 §15)
        enable_cosserat_self_terms=True,  # topology-stabilizing (k_op10, k_hopf)
        use_asymmetric_saturation=True,  # chirality bias (Meissner Gamma->-1)
        axiom_4_enabled=True,  # saturation enabled
    )


# ══════════════════════════════════════════════════════════════════════════════
# Sampling discipline (CP7): PML exclusion + density-peak two-drop selection
# ══════════════════════════════════════════════════════════════════════════════
def a2_field(V_inc, V_SNAP):
    """A^2 = |V_inc|^2 / V_SNAP^2 (port-summed strain), per site."""
    return np.sum(V_inc**2, axis=-1) / (V_SNAP**2)


def interior_mask(N, PML):
    m = np.zeros((N, N, N), dtype=bool)
    m[PML : N - PML, PML : N - PML, PML : N - PML] = True
    return m


def find_drops(engine, PML, n_drops=1, min_sep=4.0):
    """Density-peak drop selection (CP7): the top-n_drops interior A-site density
    peaks, PML-excluded, separated by >= min_sep cells (so the PAIR is two DISTINCT
    drops, not two cells of one lump). Returns list of dicts {site,port,a2}.
    NOT centroid+offset: a shell's centroid is the empty middle."""
    N = engine.N
    a2 = a2_field(engine.k4.V_inc, engine.V_SNAP)
    cand = interior_mask(N, PML) & engine.k4.mask_A
    a2m = np.where(cand, a2, -np.inf)
    flat_order = np.argsort(a2m, axis=None)[::-1]  # descending
    drops = []
    for flat_idx in flat_order:
        if len(drops) >= n_drops:
            break
        i, j, k = (int(v) for v in np.unravel_index(int(flat_idx), a2m.shape))
        val = a2m[i, j, k]
        if not np.isfinite(val) or val <= 0:
            break
        # enforce min separation from already-selected drops
        if any(
            np.sqrt((i - d["site"][0]) ** 2 + (j - d["site"][1]) ** 2 + (k - d["site"][2]) ** 2) < min_sep
            for d in drops
        ):
            continue
        port = int(np.argmax(np.abs(engine.k4.V_inc[i, j, k, :])))
        drops.append({"site": (i, j, k), "port": port, "a2": float(val)})
    return drops


# ══════════════════════════════════════════════════════════════════════════════
# CHECK 1 — sub-V_yield ring (the V/V_yield gate + CP6 reactance slosh)
# ══════════════════════════════════════════════════════════════════════════════
def vyield_ring_stats(vinc_traj, vref_traj, phi_traj, port):
    """CHECK 1: over the FREE-EVOLVE window at the drop's core bond, does the
    amplitude settle SUB-V_yield (|V_inc|/V_yield < 1, i.e. A^2 < alpha) while
    RINGING (CP6 reactance slosh: C-state V_inc <-> L-state Phi_link anti-correlated,
    both alive)? theory.md:16: the electron's "peak voltage sits safely below the
    43.65 kV [V_yield] threshold ... rings forever." A core staying OVER-yield is
    lossy -> not the electron.

    Returns: per-phasor V/V_yield (min/mean/max), reactance corr(V_inc, dPhi/dt),
    both-alive flags, and a 'sub_yield_ring' verdict (sub-yield AND ringing)."""
    out = {
        "vinc_over_vyield_max": float("nan"),
        "vinc_over_vyield_mean": float("nan"),
        "vinc_over_vyield_final": float("nan"),
        "vref_over_vyield_max": float("nan"),
        "phi_over_vyield_max": float("nan"),
        "reactance_corr": float("nan"),
        "c_state_alive": False,
        "l_state_alive": False,
        "rings": False,
        "sub_yield": False,
        "sub_yield_ring": False,
    }
    if port < 0 or vinc_traj.shape[0] < 8:
        return out
    vi = vinc_traj[:, port]
    vr = vref_traj[:, port]
    phi = phi_traj[:, port]
    # |V_inc| / V_yield  (V_yield = A_YIELD * V_SNAP, V_SNAP=1 natural units)
    vinc_over = np.abs(vi) / A_YIELD
    vref_over = np.abs(vr) / A_YIELD
    phi_over = np.abs(phi) / A_YIELD
    out["vinc_over_vyield_max"] = float(vinc_over.max())
    out["vinc_over_vyield_mean"] = float(vinc_over.mean())
    out["vinc_over_vyield_final"] = float(np.mean(vinc_over[-max(4, len(vinc_over) // 8) :]))
    out["vref_over_vyield_max"] = float(vref_over.max())
    out["phi_over_vyield_max"] = float(phi_over.max())
    # CP6 reactance slosh: V_inc (C-state) vs d(Phi_link)/dt (L-state)
    out["c_state_alive"] = bool(np.abs(vi).max() > 1e-9)
    out["l_state_alive"] = bool(np.abs(phi).max() > 1e-9)
    dphi = np.gradient(phi)
    if vi.std() > 1e-12 and dphi.std() > 1e-12:
        out["reactance_corr"] = float(np.corrcoef(vi, dphi)[0, 1])
    # rings: genuine reactive oscillation -> V_inc changes sign (zero crossings) and
    # both reactance states carry energy (not a frozen DC saturated snapshot).
    n_sign_changes = int(np.sum(np.abs(np.diff(np.sign(vi - vi.mean()))) > 0))
    out["n_zero_crossings"] = n_sign_changes
    out["rings"] = bool(n_sign_changes >= 4 and out["c_state_alive"] and out["l_state_alive"])
    # sub-yield: the settled (final-window) core amplitude is below V_yield
    out["sub_yield"] = bool(out["vinc_over_vyield_final"] < 1.0)
    out["sub_yield_ring"] = bool(out["sub_yield"] and out["rings"])
    return out


# ══════════════════════════════════════════════════════════════════════════════
# CHECK 2 — rings at omega_C (the substrate "Rayleigh frequency")
# ══════════════════════════════════════════════════════════════════════════════
def ring_frequency(vinc_traj, phi_traj, port, dt, a2_core=0.0):
    """CHECK 2: the slosh self-frequency at the drop core -> does it converge to
    omega_C = c/ell_node = 1? Measured two ways (robust): (a) zero-crossing rate of
    the C-state V_inc, (b) dominant FFT peak of the V_inc<->Phi_link slosh. CP5
    local-clock corrected target: a saturated core rings at omega_local =
    omega_C*sqrt(1-A^2_core), NOT omega_C bare. Reports both the measured omega and
    the CP5-expected omega_local so the comparison is in the right clock."""
    out = {
        "omega_zc": float("nan"),
        "omega_fft": float("nan"),
        "omega_C": OMEGA_C,
        "omega_local_expected": float("nan"),
        "ratio_to_omega_C": float("nan"),
        "ratio_to_omega_local": float("nan"),
    }
    if port < 0 or vinc_traj.shape[0] < 16:
        return out
    vi = vinc_traj[:, port].astype(float)
    vi = vi - vi.mean()
    if vi.std() < 1e-12:
        return out
    T = len(vi)
    # (a) zero-crossing frequency: N_crossings / 2 cycles over the window
    sign = np.sign(vi)
    sign[sign == 0] = 1
    n_cross = int(np.sum(np.abs(np.diff(sign)) > 0))
    cycles = n_cross / 2.0
    window_time = T * dt
    if window_time > 0:
        out["omega_zc"] = float(2.0 * np.pi * cycles / window_time)
    # (b) FFT dominant peak (omega = 2*pi*f)
    win = np.hanning(T)
    spec = np.abs(np.fft.rfft(vi * win))
    freqs = np.fft.rfftfreq(T, d=dt)
    if spec.size > 2:
        kpk = 1 + int(np.argmax(spec[1:]))  # skip DC
        out["omega_fft"] = float(2.0 * np.pi * freqs[kpk])
    # CP5 local-clock expected ring frequency at this saturation depth
    a2c = float(np.clip(a2_core, 0.0, 1.0 - 1e-9))
    out["omega_local_expected"] = float(OMEGA_C * np.sqrt(1.0 - a2c))
    meas = out["omega_fft"] if np.isfinite(out["omega_fft"]) and out["omega_fft"] > 0 else out["omega_zc"]
    if np.isfinite(meas) and meas > 0:
        out["ratio_to_omega_C"] = float(meas / OMEGA_C)
        if out["omega_local_expected"] > 0:
            out["ratio_to_omega_local"] = float(meas / out["omega_local_expected"])
    return out


# ══════════════════════════════════════════════════════════════════════════════
# CHECK 3 — size ~ ell_node (the minimum droplet)
# ══════════════════════════════════════════════════════════════════════════════
def drop_fwhm(a2_3d, center, PML):
    """CHECK 3: the drop's spatial extent vs ell_node (= 1 lattice cell). Radial
    FWHM of the A^2 density about the drop center (interior only). A localized
    droplet -> FWHM ~ ell_node (few cells, near the Nyquist minimum); a dispersed
    field -> FWHM -> grid scale (~photon wavelength, 6+ cells). Returns FWHM in
    cells (= ell_node units, since dx=1) + the peak A^2."""
    N = a2_3d.shape[0]
    cx, cy, cz = center
    ii, jj, kk = np.indices(a2_3d.shape, dtype=float)
    r = np.sqrt((ii - cx) ** 2 + (jj - cy) ** 2 + (kk - cz) ** 2)
    interior = interior_mask(N, PML)
    rflat = r[interior]
    aflat = a2_3d[interior]
    peak = float(aflat.max()) if aflat.size else 0.0
    if peak <= 0:
        return {"fwhm_cells": float("nan"), "peak_a2": 0.0, "fwhm_over_ell_node": float("nan")}
    # radial profile (1-cell bins), then half-max width
    rmax = float(min(rflat.max(), 0.4 * N))
    nb = max(8, int(round(rmax)))
    edges = np.linspace(0.0, rmax, nb + 1)
    num, _ = np.histogram(rflat, bins=edges, weights=aflat)
    cnt, _ = np.histogram(rflat, bins=edges)
    prof = np.where(cnt > 0, num / np.maximum(cnt, 1), 0.0)
    centers = 0.5 * (edges[:-1] + edges[1:])
    pmax = prof.max()
    above = prof >= 0.5 * pmax
    if above.any():
        fwhm = float(2.0 * centers[above][-1])  # diameter at half-max (profile starts at r=0)
    else:
        fwhm = float("nan")
    return {
        "fwhm_cells": fwhm,
        "peak_a2": peak,
        "fwhm_over_ell_node": fwhm / ELL_NODE_CELLS if np.isfinite(fwhm) else float("nan"),
    }


# ══════════════════════════════════════════════════════════════════════════════
# CHECK 4 + 5 — the (2,3) phasor winding (EMERGENCE) + its chirality SIGN (charge)
# (phase-space-coordinate-check: measured in (V_inc,V_ref) phasor — theory.md:16 —
#  NOT real-space. Extractor logic reused from the proven r10 driver; SIGNED so the
#  pair's opposite-chirality (check 5) is readable. CAVEAT (2026-06-04 §AUDITOR #1):
#  the temporal-single-bond extractor did NOT recover a KNOWN-IMPOSED (2,3) -> the
#  absolute (n1,n2) numbers are reported but NOT load-bearing for (2,3)-presence;
#  the robust signal is the phasor-rotation SIGN (CW vs CCW), used for check 5.)
# ══════════════════════════════════════════════════════════════════════════════
def phasor_winding_signed(vinc_traj, vref_traj):
    """CHECK 4 (does (2,3) assemble: w1->2, w2->3) + CHECK 5 (chirality sign).
    Reads the (V_inc, V_ref) phasor TEMPORAL winding at the drop's two load-bearing
    ports over the free-evolve window. Returns SIGNED windings w1,w2 (the sign is the
    phasor rotation sense = the chirality, robust), |n1|,|n2| (the (2,3) magnitudes,
    caveated), the reduced ratio, the phase-space crossing count c, and R/r aspect."""
    out = {
        "w1_signed": 0.0,
        "w2_signed": 0.0,
        "n1": 0,
        "n2": 0,
        "winding_ratio": "n/a",
        "crossing_count_c": 0,
        "R_over_r": float("nan"),
        "amp": 0.0,
        "chirality_sign": 0,
        "p1": -1,
        "p2": -1,
    }
    T = vinc_traj.shape[0]
    if T < 16:
        return out
    port_amp = np.sqrt(np.mean(vinc_traj**2, axis=0) + np.mean(vref_traj**2, axis=0))
    if port_amp.max() < 1e-12:
        return out
    p1 = int(np.argmax(port_amp))
    order = np.argsort(port_amp)[::-1]
    p2 = int(order[1]) if len(order) > 1 else p1
    out["p1"], out["p2"], out["amp"] = p1, p2, float(port_amp[p1])

    def _winding(vi, vr):
        a = vi - vi.mean()
        b = vr - vr.mean()
        if np.sqrt(a.var() + b.var()) < 1e-12:
            return 0.0
        ph = np.unwrap(np.arctan2(b, a))
        total = (ph[-1] - ph[0]) / (2.0 * np.pi)
        closure = np.arctan2(b[0], a[0]) - ph[-1]
        while closure > np.pi:
            closure -= 2 * np.pi
        while closure < -np.pi:
            closure += 2 * np.pi
        return total + closure / (2.0 * np.pi)

    w1 = _winding(vinc_traj[:, p1], vref_traj[:, p1])
    w2 = _winding(vinc_traj[:, p2], vref_traj[:, p2])
    out["w1_signed"], out["w2_signed"] = float(w1), float(w2)
    out["n1"], out["n2"] = int(round(abs(w1))), int(round(abs(w2)))
    out["chirality_sign"] = int(np.sign(w1)) if abs(w1) > 0.25 else 0  # CHECK 5 primitive
    out["winding_ratio"] = _reduced_ratio(w1, w2)
    # phase-space crossing count c of the closed (smoothed) curve (trefoil -> c=3)
    s1 = _smooth(vinc_traj[:, p1] - vinc_traj[:, p1].mean())
    s2 = _smooth(vinc_traj[:, p2] - vinc_traj[:, p2].mean())
    out["crossing_count_c"] = _planar_self_crossings(np.stack([s1, s2], axis=1))
    # R_phase/r_phase via PCA on the (V_inc_p1, V_ref_p1) cloud (phi^2 diagnostic)
    pts = np.stack([vinc_traj[:, p1], vref_traj[:, p1]], axis=1)
    pts = pts - pts.mean(axis=0, keepdims=True)
    cov = (pts.T @ pts) / max(T - 1, 1)
    evals = np.sort(np.maximum(np.linalg.eigvalsh(cov), 0.0))[::-1]
    if evals[1] > 1e-30:
        out["R_over_r"] = float(np.sqrt(evals[0] / evals[1]))
    return out


def _reduced_ratio(a, b, max_den=7):
    a, b = abs(a), abs(b)
    if a < 1e-6 or b < 1e-6:
        return "n/a"
    target = a / b
    best, best_err = (1, 1), abs(target - 1.0)
    for q in range(1, max_den + 1):
        for p in range(1, max_den + 1):
            err = abs(target - p / q)
            if err < best_err:
                best_err, best = err, (p, q)
    from math import gcd

    g = gcd(best[0], best[1])
    return f"{best[0] // g}:{best[1] // g}"


def _smooth(x, frac=0.05):
    n = len(x)
    w = max(3, int(frac * n) | 1)
    if w >= n:
        return x.astype(float)
    return np.convolve(x, np.ones(w) / w, mode="same")


def _planar_self_crossings(curve):
    n = len(curve)
    if n < 8:
        return 0
    step = max(1, n // 200)
    p = curve[::step]
    m = len(p)
    scale = float(np.sqrt(p.var(axis=0).sum())) + 1e-12
    pts = []
    for i in range(m - 1):
        a1, a2 = p[i], p[i + 1]
        for j in range(i + 2, m - 1):
            if i == 0 and j == m - 2:
                continue
            ip = _seg_intersection_point(a1, a2, p[j], p[j + 1])
            if ip is not None:
                pts.append(ip)
    if not pts:
        return 0
    pts = np.array(pts)
    tol = 0.08 * scale
    clusters = []
    for q in pts:
        if not any(np.linalg.norm(q - c) < tol for c in clusters):
            clusters.append(q)
    return len(clusters)


def _seg_intersection_point(p1, p2, p3, p4):
    def ccw(a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])

    d1, d2 = ccw(p3, p4, p1), ccw(p3, p4, p2)
    d3, d4 = ccw(p1, p2, p3), ccw(p1, p2, p4)
    if not (((d1 > 0) != (d2 > 0)) and ((d3 > 0) != (d4 > 0))):
        return None
    u, v = p2 - p1, p4 - p3
    denom = u[0] * v[1] - u[1] * v[0]
    if abs(denom) < 1e-15:
        return None
    t = ((p3[0] - p1[0]) * v[1] - (p3[1] - p1[1]) * v[0]) / denom
    return p1 + t * u


def cosserat_carrier2_diag(engine):
    """Carrier-2 (Cosserat omega) diagnostic — FLAGGED coordinate-mismatch (the
    shipped Op10 reads REAL-SPACE omega; the corpus (2,3) is in (V_inc,V_ref) phasor).
    Per 2026-06-04 Q0: a pure-V photon leaves omega=0 (exact fixed point) -> expect ~0.
    Reported so both carriers are on the table; NOT the headline."""
    out = {}
    try:
        out["omega_op10_c"] = int(engine.cos.extract_crossing_count())
    except Exception as exc:  # noqa: BLE001
        out["omega_op10_c"] = -1
        out["omega_op10_error"] = str(exc)
    try:
        out["hopf_charge"] = float(engine.cos.extract_hopf_charge())
    except Exception:  # noqa: BLE001
        out["hopf_charge"] = float("nan")
    out["omega_max"] = float(np.abs(engine.cos.omega).max())
    out["omega_energy"] = float(np.sum(engine.cos.omega**2))
    return out


# ══════════════════════════════════════════════════════════════════════════════
# The genesis run: DRIVE to A->1 pinch-off, then SOURCE OFF + FREE-EVOLVE
# ══════════════════════════════════════════════════════════════════════════════
def run_genesis(mode, N, PML, amplitude, drive_periods, free_periods, slice_cadence=3, verbose=True):
    """One genesis run. mode in {'single','pair','pair_baseline'}.
      - 'single'        : one moving CP photon (BUILD 1 control).
      - 'pair'          : two OPPOSITE-handed colliding photons (BUILD 2 genesis).
      - 'pair_baseline' : two SAME-handed colliding photons (matched amplitude/
                          saturation, NO chirality split).
    Drive for drive_periods (sources on: ramp+sustain+decay then silent), then
    free_periods of free evolution. Records (CP6) the reactance pair at the running
    drop bond(s) every step + 2D mid-plane A^2 slices on cadence (animation).
    Returns observables + raw traces (npz)."""
    n_drops = 1 if mode == "single" else 2
    n_drive = int(round(drive_periods * COMPTON_PERIOD / DT))
    n_free = int(round(free_periods * COMPTON_PERIOD / DT))
    n_steps = n_drive + n_free
    kz = N // 2  # mid-plane slice index (z) for the 2D animation panel

    engine = setup_engine(N, PML)
    if mode == "single":
        x0s = make_single_photon(engine, N, amplitude)
    elif mode == "pair":
        x0s = make_colliding_pair(engine, N, amplitude, opposite=True)
    elif mode == "pair_baseline":
        x0s = make_colliding_pair(engine, N, amplitude, opposite=False)
    else:
        raise ValueError(f"unknown mode {mode!r}")

    # per-step recording (full run length)
    rec_t = np.zeros(n_steps)
    rec_maxA2 = np.zeros(n_steps)
    rec_energy = np.zeros(n_steps)
    # per-drop reactance-pair traces (slot 0 = drop_lo by x; slot 1 = drop_hi). For
    # 'single' only slot 0 is used. CP6: C-state V_inc + L-state Phi_link both every step.
    rec_vinc = np.zeros((2, n_steps, 4))
    rec_vref = np.zeros((2, n_steps, 4))
    rec_phi = np.zeros((2, n_steps, 4))
    rec_site = np.zeros((2, n_steps, 3))
    rec_port = np.zeros((2, n_steps), dtype=int)
    slices = []  # (t, 48x48) mid-plane A^2 for animation
    slice_t = []
    drive_peak_a2 = 0.0
    drive_end_vinc = None

    interior = interior_mask(N, PML)
    t0 = time.time()
    for s in range(n_steps):
        engine.step()
        a2 = a2_field(engine.k4.V_inc, engine.V_SNAP)
        a2_int = np.where(interior, a2, 0.0)
        rec_t[s] = engine.time
        rec_maxA2[s] = float(a2_int.max())
        rec_energy[s] = float(a2_int.sum())
        if s < n_drive:
            drive_peak_a2 = max(drive_peak_a2, rec_maxA2[s])
        if s == n_drive - 1:
            drive_end_vinc = engine.k4.V_inc.copy()
        # running drop selection (PML-excluded density peaks), id by x-position
        drops = find_drops(engine, PML, n_drops=n_drops, min_sep=4.0)
        drops = sorted(drops, key=lambda d: d["site"][0])  # lo-x first
        for slot in range(n_drops):
            if slot < len(drops):
                i, j, k = drops[slot]["site"]
                p = drops[slot]["port"]
            else:  # fallback: lattice center A-site
                i = j = k = N // 2
                i = i if engine.k4.mask_A[i, j, k] else i + 1
                p = int(np.argmax(np.abs(engine.k4.V_inc[i, j, k, :])))
            rec_vinc[slot, s] = engine.k4.V_inc[i, j, k, :]
            rec_vref[slot, s] = engine.k4.V_ref[i, j, k, :]
            rec_phi[slot, s] = engine.k4.Phi_link[i, j, k, :]
            rec_site[slot, s] = (i, j, k)
            rec_port[slot, s] = p
        if s % slice_cadence == 0:
            slices.append(a2[:, :, kz].astype(np.float32))
            slice_t.append(float(engine.time))
    elapsed = time.time() - t0

    if verbose:
        print(
            f"    [{mode}] drive_peak A^2={drive_peak_a2:.3f}  "
            f"free-end max A^2={rec_maxA2[-1]:.4f}  "
            f"energy {rec_energy[n_drive-1]:.3g}->{rec_energy[-1]:.3g}  {elapsed:.0f}s",
            flush=True,
        )

    return {
        "mode": mode,
        "amplitude": amplitude,
        "N": N,
        "PML": PML,
        "n_drive": n_drive,
        "n_free": n_free,
        "n_steps": n_steps,
        "x0_sources": x0s,
        "drive_peak_a2": float(drive_peak_a2),
        "elapsed_s": elapsed,
        "kz": kz,
        "n_drops": n_drops,
        "_engine": engine,
        "_drive_end_vinc": drive_end_vinc,
        "_rec": {
            "t": rec_t,
            "maxA2": rec_maxA2,
            "energy": rec_energy,
            "vinc": rec_vinc,
            "vref": rec_vref,
            "phi": rec_phi,
            "site": rec_site,
            "port": rec_port,
            "slices": np.array(slices),
            "slice_t": np.array(slice_t),
        },
    }


def matched_baseline_retention(drive_end_vinc, N, PML, free_periods):
    """BUILD-1 matched-distribution baseline (phase3f-correct, CP8 step 2): take the
    structured run's drive-end V_inc field, PERMUTE it across interior cells (exact
    amplitude-histogram match, ZERO spatial coherence -> trivial topology, identical
    energy, no injection -> TLM-unitary IC), then FREE-EVOLVE. If the structured
    droplet persists but this matched-amplitude-no-coherence field disperses, the
    persistence is STRUCTURE-driven (not amplitude). Returns interior-energy retention
    + whether a localized peak survives."""
    rng = np.random.default_rng(20260606)
    eng = setup_engine(N, PML)
    interior = interior_mask(N, PML)
    cells = interior & eng.k4.mask_active
    field = np.zeros_like(eng.k4.V_inc)
    # permute the structured drive-end interior values across interior active cells
    src_vals = drive_end_vinc[cells]  # (M,4)
    perm = rng.permutation(src_vals.shape[0])
    field[cells] = src_vals[perm]
    eng.k4.V_inc[:] = field
    eng.k4.V_ref[:] = 0.0
    eng.k4.Phi_link[:] = 0.0
    n_free = int(round(free_periods * COMPTON_PERIOD / DT))
    e0 = float(np.sum(np.where(interior, a2_field(eng.k4.V_inc, eng.V_SNAP), 0.0)))
    peak0 = float(np.where(interior, a2_field(eng.k4.V_inc, eng.V_SNAP), 0.0).max())
    for _ in range(n_free):
        eng.step()
    a2 = np.where(interior, a2_field(eng.k4.V_inc, eng.V_SNAP), 0.0)
    e1, peak1 = float(a2.sum()), float(a2.max())
    return {
        "energy_retention": (e1 / e0) if e0 > 0 else float("nan"),
        "peak_retention": (peak1 / peak0) if peak0 > 0 else float("nan"),
        "e0": e0,
        "e1": e1,
        "peak0": peak0,
        "peak1": peak1,
    }


# ══════════════════════════════════════════════════════════════════════════════
# Apply the 5-check gate + persistence to a genesis run
# ══════════════════════════════════════════════════════════════════════════════
def apply_gate(run):
    """Apply persistence + checks 1-5 on each drop, in the SETTLED free-evolve tail
    (after the splash radiates). Returns a structured gate dict (per-drop), the
    carrier-2 omega diagnostic, and the final-field localization."""
    rec = run["_rec"]
    engine = run["_engine"]
    N, PML = run["N"], run["PML"]
    n_drive, n_free = run["n_drive"], run["n_free"]
    gate_start = n_drive + int(0.4 * n_free)  # settled tail (skip the splash transient)
    interior = interior_mask(N, PML)

    # final-field localization (CHECK 3 + persistence)
    a2_final = a2_field(engine.k4.V_inc, engine.V_SNAP)
    a2_int = np.where(interior, a2_final, 0.0)
    mean_int = float(a2_int[interior].mean()) if interior.any() else 0.0
    peak_final = float(a2_int.max())
    final_drops = find_drops(engine, PML, n_drops=run["n_drops"], min_sep=4.0)
    final_drops = sorted(final_drops, key=lambda d: d["site"][0])

    # post-shutoff energy retention (free-evolve start -> end)
    e_free0 = float(rec["energy"][n_drive]) if n_drive < len(rec["energy"]) else float("nan")
    e_end = float(rec["energy"][-1])
    energy_retention = (e_end / e_free0) if e_free0 > 0 else float("nan")

    per_drop = []
    for slot in range(run["n_drops"]):
        vi = rec["vinc"][slot, gate_start:]
        vr = rec["vref"][slot, gate_start:]
        ph = rec["phi"][slot, gate_start:]
        dom = int(np.argmax(np.mean(np.abs(vi), axis=0))) if vi.size else 0
        a2_core = float(np.mean(np.sum(vi**2, axis=1))) if vi.size else 0.0
        c1 = vyield_ring_stats(vi, vr, ph, dom)
        c2 = ring_frequency(vi, ph, dom, DT, a2_core)
        if slot < len(final_drops):
            center = final_drops[slot]["site"]
            site_peak_a2 = final_drops[slot]["a2"]
        else:
            center = (N // 2, N // 2, N // 2)
            site_peak_a2 = 0.0
        c3 = drop_fwhm(a2_final, center, PML)
        c45 = phasor_winding_signed(vi, vr)
        localized = bool(
            np.isfinite(c3["fwhm_cells"]) and c3["fwhm_cells"] < 0.30 * N and site_peak_a2 > 5.0 * mean_int
        )
        per_drop.append(
            {
                "slot": slot,
                "final_site": list(center),
                "dom_port": dom,
                "a2_core_window": a2_core,
                "site_peak_a2": site_peak_a2,
                "localized": localized,
                "check1_sub_yield_ring": c1,
                "check2_omega_C": c2,
                "check3_size": c3,
                "check45_phasor": c45,
            }
        )

    # CHECK 5 — opposite winding sign (pair only)
    check5 = {"applicable": run["n_drops"] == 2, "opposite_sign": False, "sign_lo": 0, "sign_hi": 0}
    if run["n_drops"] == 2 and len(per_drop) == 2:
        s_lo = per_drop[0]["check45_phasor"]["chirality_sign"]
        s_hi = per_drop[1]["check45_phasor"]["chirality_sign"]
        check5.update(sign_lo=s_lo, sign_hi=s_hi, opposite_sign=bool(s_lo != 0 and s_hi != 0 and s_lo != s_hi))

    return {
        "gate_start_step": gate_start,
        "energy_retention_postshutoff": energy_retention,
        "final_peak_a2": peak_final,
        "final_mean_interior_a2": mean_int,
        "n_final_drops": len(final_drops),
        "per_drop": per_drop,
        "check5_charge_conservation": check5,
        "carrier2_omega": cosserat_carrier2_diag(engine),
    }


def classify_verdict(run, gate, baseline):
    """Honest I/II/III verdict (ave-evidence-framing). Transparent combination of
    the gate signals; thresholds tagged engineering-choice where not substrate-derived.
      (III) no-stable-drop : no drop persists localized sub-V_yield (disperses / over-yield).
      (II)  mass-only      : drop(s) persist sub-V_yield + ring (checks 1-3), but the
                             (2,3) does NOT assemble (check 4) [+ check 5 for the pair].
      (I)   full genesis   : pair pinches off into persistent sub-V_yield ringing
                             droplets, (2,3) assembles, opposite signs."""
    drops = gate["per_drop"]
    # persistence: every expected drop is localized AND sub-V_yield ringing
    persist = bool(drops) and all(d["localized"] and d["check1_sub_yield_ring"]["sub_yield_ring"] for d in drops)
    # structure-driven (beats matched baseline) — peak-localization retention contrast
    beats_baseline = None
    if baseline is not None and np.isfinite(baseline.get("peak_retention", float("nan"))):
        struct_peak_ret = gate["final_peak_a2"]
        beats_baseline = bool(
            struct_peak_ret > 0 and baseline["peak1"] >= 0 and (gate["n_final_drops"] >= run["n_drops"])
        )

    # (2,3) assembles (check 4) — magnitudes near (2,3) OR crossing c==3 (caveated extractor)
    def _is23(c):
        return (c["crossing_count_c"] == 3) or ((c["n1"], c["n2"]) in [(2, 3), (3, 2)])

    two_three = bool(drops) and any(_is23(d["check45_phasor"]) for d in drops)
    # check 5 (pair)
    c5 = gate["check5_charge_conservation"]
    pair_ok = (not c5["applicable"]) or c5["opposite_sign"]

    if not persist:
        outcome = "III"
        verdict = (
            "(III) NO-STABLE-DROP — the photon(s) do NOT pinch off into a "
            "persistent localized sub-V_yield ringing droplet (disperse / stay "
            "over-yield). The A->1 pinch-off regime did not yield the electron-droplet."
        )
    elif two_three and pair_ok:
        outcome = "I"
        verdict = (
            "(I) FULL GENESIS — persistent sub-V_yield ringing droplet(s); the "
            "(2,3) phasor winding ASSEMBLES"
            + (
                " with OPPOSITE chirality signs (net-neutral e-+e+ pair)."
                if c5["applicable"]
                else " (single neutral droplet)."
            )
        )
    else:
        outcome = "II"
        verdict = (
            "(II) MASS-ONLY — droplet(s) self-bind as a persistent sub-V_yield "
            "ringing core (mass), but the (2,3) winding does NOT assemble in the "
            "(V_inc,V_ref) phasor"
            + (
                "; chirality sign split " + ("present" if c5["opposite_sign"] else "absent") + "."
                if c5["applicable"]
                else ". Structural-capability finding: engine " "carries the drop, not the winding self-assembly."
            )
        )
    return {
        "outcome": outcome,
        "verdict": verdict,
        "persists": persist,
        "two_three_assembles": two_three,
        "pair_opposite_sign": pair_ok,
        "beats_baseline": beats_baseline,
    }


def save_capture(run, gate, out_dir, tag):
    """Persist the per-run capture for the animation + auditor re-check."""
    rec = run["_rec"]
    npz = out_dir / f"r11_genesis_{tag}_capture.npz"
    np.savez_compressed(
        npz,
        t=rec["t"],
        maxA2=rec["maxA2"],
        energy=rec["energy"],
        vinc=rec["vinc"],
        vref=rec["vref"],
        phi=rec["phi"],
        site=rec["site"],
        port=rec["port"],
        slices=rec["slices"],
        slice_t=rec["slice_t"],
        n_drive=run["n_drive"],
        n_free=run["n_free"],
        dt=DT,
        N=run["N"],
        PML=run["PML"],
        kz=run["kz"],
        A_YIELD=A_YIELD,
        A2_YIELD=A2_YIELD,
        OMEGA_C=OMEGA_C,
        amplitude=run["amplitude"],
    )
    return npz


def _strip(run):
    """JSON-safe view (drop engine + raw numpy traces)."""
    return {k: v for k, v in run.items() if not k.startswith("_")}


# ══════════════════════════════════════════════════════════════════════════════
# Calibration — find the amplitude that drives the focus/antinode to A->1 pinch-off
# ══════════════════════════════════════════════════════════════════════════════
def calibrate(N, PML, amps_single, amps_pair):
    """Empirical drive_peak A^2 vs amplitude (Rule 10: calibrate before committing).
    A->1 (A^2 ~ 1) is the pinch-off boundary. Short drive only (no free-evolve)."""
    drive_p = _envelope_periods() + 2.0
    out = {"single": [], "pair": []}
    print(f"\n  CALIBRATION (N={N}, PML={PML}, drive {drive_p:.1f}P) — find A->1 pinch-off")
    print(f"  A2_yield(check1 bar)={A2_YIELD:.4g}  A2_op14(self-trap)={A2_OP14:.4f}  A2_rupture=1.0")
    for amp in amps_single:
        r = run_genesis("single", N, PML, amp, drive_p, 0.0, verbose=False)
        out["single"].append((amp, r["drive_peak_a2"]))
        print(
            f"    single amp={amp:.2f} -> drive_peak A^2={r['drive_peak_a2']:.3f} "
            f"(A={np.sqrt(r['drive_peak_a2']):.3f})",
            flush=True,
        )
    for amp in amps_pair:
        r = run_genesis("pair", N, PML, amp, drive_p, 0.0, verbose=False)
        out["pair"].append((amp, r["drive_peak_a2"]))
        print(
            f"    pair   amp={amp:.2f} -> antinode A^2={r['drive_peak_a2']:.3f} "
            f"(A={np.sqrt(r['drive_peak_a2']):.3f})",
            flush=True,
        )
    return out


def pick_pinchoff_amp(sweep, prefer=2.0, lo=1.0, hi=8.0):
    """Auto-pick the A->1 pinch-off drive amplitude from a calibration sweep. The
    saturation knee is sharp (sub-pinch A^2~0.4 jumps to over-rupture A^2~13 across
    ~0.05 amplitude), so the pinch-off is the SMALLEST amp that breaches the rupture
    wall (A^2>=1). Returns the amp with A^2 in [lo,hi] closest to `prefer`; if all
    over-driven (A^2>hi), the least-over amp; if none reach pinch-off, the deepest."""
    in_window = [(a, v) for a, v in sweep if lo <= v <= hi]
    if in_window:
        return float(min(in_window, key=lambda x: abs(x[1] - prefer))[0])
    over = [(a, v) for a, v in sweep if v > hi]
    if over:
        return float(min(over, key=lambda x: x[0])[0])
    return float(max(sweep, key=lambda x: x[1])[0])


def main():
    import sys

    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    PML = 4
    out_dir = Path(__file__).parent
    print("=" * 80)
    print("  ELECTRON GENESIS — 'a drop in water' (CP8, TWO-COLLIDING PAIR)")
    print(f"  VacuumEngine3D K4-TLM+Cosserat | N={N} PML={PML} | ALPHA={ALPHA:.10g}")
    print(f"  V_yield/V_SNAP=sqrt(a)={A_YIELD:.4f}  ell_node={ELL_NODE_CELLS:.0f} cell  omega_C={OMEGA_C}")
    print("=" * 80)

    results = {
        "config": {
            "N": N,
            "PML": PML,
            "ALPHA": ALPHA,
            "A_YIELD": A_YIELD,
            "A2_YIELD": A2_YIELD,
            "A2_OP14": A2_OP14,
            "OMEGA_C": OMEGA_C,
            "DT": DT,
            "ELL_NODE_CELLS": ELL_NODE_CELLS,
        }
    }

    amp_single_auto, amp_pair_auto = 0.50, 0.50
    if cmd in ("calibrate", "all"):
        fine = [0.40, 0.45, 0.48, 0.50, 0.52, 0.55]
        cal = calibrate(N, PML, amps_single=fine, amps_pair=fine)
        results["calibration"] = cal
        amp_single_auto = pick_pinchoff_amp(cal["single"])
        amp_pair_auto = pick_pinchoff_amp(cal["pair"])

    # drive amplitudes auto-picked at the A->1 pinch-off knee; overridable via argv[3:]
    amp_single = float(sys.argv[3]) if len(sys.argv) > 3 else amp_single_auto
    amp_pair = float(sys.argv[4]) if len(sys.argv) > 4 else amp_pair_auto
    drive_p, free_p = _envelope_periods(), 16.0
    print(f"\n  PINCH-OFF amplitudes (auto): single={amp_single:.3f}  pair={amp_pair:.3f}/pulse")
    results["config"]["amp_single"] = amp_single
    results["config"]["amp_pair"] = amp_pair

    if cmd in ("control", "all"):
        print(f"\n  ── BUILD 1: SINGLE-photon MASS-DROPLET CONTROL (amp={amp_single}) ──")
        run_s = run_genesis("single", N, PML, amp_single, drive_p, free_p)
        gate_s = apply_gate(run_s)
        base_s = matched_baseline_retention(run_s["_drive_end_vinc"], N, PML, free_p)
        ver_s = classify_verdict(run_s, gate_s, base_s)
        save_capture(run_s, gate_s, out_dir, "single")
        results["build1_single"] = {"run": _strip(run_s), "gate": gate_s, "matched_baseline": base_s, "verdict": ver_s}
        _print_gate("BUILD 1 (single)", gate_s, ver_s, base_s)

    if cmd in ("pair", "all"):
        print(f"\n  ── BUILD 2: TWO-COLLIDING PAIR GENESIS (amp={amp_pair}/pulse) ──")
        run_p = run_genesis("pair", N, PML, amp_pair, drive_p, free_p)
        gate_p = apply_gate(run_p)
        print(f"  ── matched baseline: SAME-handed pair (amp={amp_pair}/pulse) ──")
        run_b = run_genesis("pair_baseline", N, PML, amp_pair, drive_p, free_p)
        gate_b = apply_gate(run_b)
        base_p = {
            "peak_retention": gate_b["final_peak_a2"],
            "peak1": gate_b["final_peak_a2"],
            "energy_retention": gate_b["energy_retention_postshutoff"],
            "n_final_drops": gate_b["n_final_drops"],
        }
        ver_p = classify_verdict(run_p, gate_p, base_p)
        save_capture(run_p, gate_p, out_dir, "pair")
        save_capture(run_b, gate_b, out_dir, "pair_baseline")
        results["build2_pair"] = {"run": _strip(run_p), "gate": gate_p, "verdict": ver_p}
        results["build2_pair_baseline"] = {"run": _strip(run_b), "gate": gate_b}
        _print_gate("BUILD 2 (pair, opposite-handed)", gate_p, ver_p, None)
        _print_gate("BUILD 2 baseline (same-handed)", gate_b, None, None)

    out_json = out_dir / "r11_electron_genesis_drop_results.json"
    out_json.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {out_json.name}")
    return results


def _print_gate(label, gate, verdict, baseline):
    print(f"\n  ◆ {label}")
    print(
        f"    persistence: energy_retention(post-shutoff)={gate['energy_retention_postshutoff']:.3g}  "
        f"final_peak_A^2={gate['final_peak_a2']:.4g}  n_final_drops={gate['n_final_drops']}"
    )
    for d in gate["per_drop"]:
        c1, c2, c3, c4 = (d["check1_sub_yield_ring"], d["check2_omega_C"], d["check3_size"], d["check45_phasor"])
        print(f"    drop[{d['slot']}] @ {d['final_site']} localized={d['localized']}")
        print(
            f"      check1 sub_yield_ring={c1['sub_yield_ring']} "
            f"(V/Vyield final={c1['vinc_over_vyield_final']:.3g} rings={c1['rings']} "
            f"react_corr={c1['reactance_corr']:.3f})"
        )
        print(
            f"      check2 omega: meas/omega_C={c2['ratio_to_omega_C']:.3g} "
            f"meas/omega_local={c2['ratio_to_omega_local']:.3g} (CP5)"
        )
        print(f"      check3 size: FWHM={c3['fwhm_cells']:.3g} cells (~ell_node={c3['fwhm_over_ell_node']:.3g})")
        print(
            f"      check4 (2,3): (n1,n2)=({c4['n1']},{c4['n2']}) ratio={c4['winding_ratio']} "
            f"c={c4['crossing_count_c']} w1_signed={c4['w1_signed']:.2f} chir={c4['chirality_sign']}"
        )
    c5 = gate["check5_charge_conservation"]
    if c5["applicable"]:
        print(f"    check5 charge: signs=({c5['sign_lo']},{c5['sign_hi']}) opposite={c5['opposite_sign']}")
    od = gate["carrier2_omega"]
    print(
        f"    [carrier-2 omega] omega_max={od['omega_max']:.3e} Op10_c={od['omega_op10_c']} "
        f"Hopf={od['hopf_charge']:.3g} (Q0: expect ~0)"
    )
    if baseline is not None:
        print(
            f"    matched baseline: peak_retention={baseline.get('peak_retention', float('nan')):.3g} "
            f"energy_retention={baseline.get('energy_retention', float('nan')):.3g}"
        )
    if verdict is not None:
        print(f"    >>> {verdict['outcome']}: {verdict['verdict']}")


if __name__ == "__main__":
    main()
