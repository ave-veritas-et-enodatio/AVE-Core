"""Stage 1 GATE — boundary-observable (𝓜/𝓠/𝓙) self-trap integrator + Z-at-wall.

Keystone reframe (canonical: manuscript/ave-kb/common/boundary-observables-m-q-j.md):
the substrate-correct electron test reads the three boundary observables 𝓜 (mass),
𝓠 (charge), 𝓙 (spin) at the boundary ∂Ω of a self-trapped Γ=−1 region. Prior arc
negatives measured INTERIOR plumbing (a category error: interior eigenmodes are
causally disconnected per clm-sjjvhf). The boundary test never ran.

THIS STAGE is the GATE and computes NO M/Q/J (that is Stage 2/3). It answers ONE
gating question with a FOUR-WAY (NOT binary) verdict:
  Does a self-trapped Γ=−1 region port to the COUPLED engine and remain stable as
  a TRUE STIFFENING confinement (C_eff→∞ ⇒ Z→0 ⇒ |Γ|=1), long enough to later read
  its boundary?

THE LOAD-BEARING TENSION (why the gate is 4-way, not binary):
  The electron self-trap is the STIFFENING route: C_eff→∞ ⇒ Z→0 ⇒ |Γ|=1 — the A1
  longitudinal matter-wall (INVARIANT-S2 Q1=B, Grant-ratified). BUT the
  capability-map (engine-capability-map.md:45,79) says VacuumEngine3D is
  "softening-only ... structurally cannot host the stiffening cage": its scalar is
  a PROJECTION v_scalar_from_v_inc(V_inc), NO independent A1 field. So the
  vacuum_engine Γ=−1 saturated-bond wall is EITHER (a) a true Z→0 stiffening
  confinement OR (b) a softening-route proxy (transverse Meissner Z_eff=√(S_μ/S_ε),
  bulk ρ̄ reflection). WE DETERMINE WHICH BY MEASURING Z AT THE SATURATED WALL.

FOUR-WAY VERDICT (auditor-mandated buckets — NOT collapsed to binary):
  PORTS-STABLE        — known-positive held + Z→0 at wall (TRUE stiffening) + |ω|
                        bounded + full-Hamiltonian flat/decaying + saturated channel
                        persists ≥10 Compton periods while unsaturated decays.
  c_eff(V)-STRUCTURAL-GAP (🔧, NOT echo; a bounded build) — wall forms but Z does
                        NOT →0 (softening proxy, not C_eff→∞). Confirms cap-map
                        :45/:79. → coupled engine needs a true c_eff(V)/independent-A1
                        field (a BOUNDED build: couple the master-equation cage's
                        c_eff(V) in). Report the measured Z behavior as evidence.
  PHYSICAL-NO-TRAP    (🔴, ECHO candidate) — known-positive held AND Z→0 stiffening
                        present, but STILL no stable bounded trap (disperses /
                        destabilizes). Only THIS bucket bears on echo.
  PUMPS               — full-Hamiltonian ledger climbs → trap not passive (ontology).
  (INTEGRATOR-INADEQUATE — bucket 1: if the known-positive standalone cage CANNOT
   be held, any coupled blow-up is numerical, not physics.)

A naive "BLOW-UP" must NOT be reported — it is resolved into (1) numerical,
(2) needs-the-cage, or (3) echo, via the known-positive validation (step 1) + the
Z-at-wall measurement (step 2).

DISCIPLINE (applied, not just named):
  ave-apparatus-floor-attribution — KNOWN-POSITIVE FIRST: run the standalone
    MasterEquationFDTD v14 verdict-II cage (the engine that DOES have c_eff(V));
    confirm the solver holds it. Then dx/dt(cfl) sweep. Bucket-1 gate.
  substrate-native-check CP8 — seed the GENERATIVE PRECURSOR (helical ω-photon);
    let the moving Γ=−1 wall form. A planted-Γ run is LABELED instrumentation-only.
  substrate-native-check CP10 — trap rendered as Op17-bounded BOUNDARY CONDITION
    (use_impedance_boundary=True; _rotate_clamp exact reactance rotation), NOT a
    bulk energy/force term. The bulk V→ω W_refl gradient force (the documented
    runaway channel) is OFF on this path.
  ave-conserved-vs-pumped — full-Hamiltonian witness total_hamiltonian()
    (kinetic+gradient potential), NOT sum(ω²); KEEP-BOTH the engine's own
    impedance_hamiltonian().
  ave-canonical-source — V_SNAP, ALPHA from ave.core.constants; ZERO new free params.

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/boundary_mqj_selftrap_zwall_gate.py
Env overrides for fast smoke: MQJ_N, MQJ_PERIODS.
"""
from __future__ import annotations

import json
import os

import numpy as np

# ── Canonical-source imports (ave-canonical-source — zero new free params) ────
from ave.core.constants import ALPHA, C_0, V_SNAP
from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.topological.vacuum_engine import (
    BondObserver,
    EnergyBudgetObserver,
    EngineConfig,
    VacuumEngine3D,
)

import ave.core.constants as _avc  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def _canonical_source_gate() -> None:
    """ave-canonical-source — assert the constants are the canonical ones."""
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants source"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"
    _ = (C_0, V_SNAP)  # referenced for provenance


# ──────────────────────────────────────────────────────────────────────────
# Geometry + units (natural units: dx = ℓ_node, c₀ = 1)
# ──────────────────────────────────────────────────────────────────────────
N = int(os.environ.get("MQJ_N", "24"))
PML = 4
SIGMA, LAM = 3.0, 6.0
A_LOCK = 3.0          # peak |ω| seed for the LOCK regime (engages a soft Γ=−1 wall)
A_PUMP = 6.0          # peak |ω| seed for the PUMP control (hard wall, parametric pump)
K_WALL = 60.0         # soft clamp → engaged + stable + few sub-steps
CFL_SAFE = 0.25       # anti-pump margin on the implicit reactance-rotation
CENTER = (N / 2.0, N / 2.0, N / 2.0)

OMEGA_C_NATURAL = 1.0                        # = c_R/dx ring scale
T_COMPTON = 2.0 * np.pi / OMEGA_C_NATURAL    # one Compton period in natural-time
N_PERIODS = float(os.environ.get("MQJ_PERIODS", "12"))   # ≥10P persistence target + margin


def _steps_for_periods(eng, n_periods: float) -> int:
    """# outer steps to evolve `n_periods` Compton periods (apparatus-floor honest:
    derived from the engine's own outer_dt, not a hard-coded step count)."""
    return int(np.ceil(n_periods * T_COMPTON / eng.outer_dt))


# ══════════════════════════════════════════════════════════════════════════
# STEP 1 — KNOWN-POSITIVE VALIDATION (ave-apparatus-floor-attribution).
# Run the STANDALONE verdict-II self-trap that DOES have c_eff(V): the
# MasterEquationFDTD v14 breathing soliton (master_equation_fdtd.py:13 —
# c_eff(V)=c0·(1−A²)^(−1/4)→∞; v14 Mode I PASS, test_master_equation_v14_mode_i.py).
# This is the cap-map's "the only engine with the A1 cage" (engine-capability-map.md:42).
#
# If the solver CANNOT hold this known-stable standalone trap → bucket (1)
# INTEGRATOR-INADEQUATE: any coupled blow-up downstream is numerical, not physics.
# Validate the INSTRUMENT on a known-positive before trusting any coupled null.
#
# Z-at-wall on the cage: the A1 longitudinal tank has C_eff = C_0/S, so
# Z_long = √(L/C_eff) = √(L·S/C_0) ∝ √S → 0 as S→0 (A→1). The engine exposes
# refractive_index() = S^(1/4), so Z_long/Z_0 = √S = refractive_index()². The
# MIN over the lattice is the deepest saturation (cage core). Z_long→0 there IS
# the stiffening-confinement signature this gate looks for.
# ══════════════════════════════════════════════════════════════════════════
KP_DX = 0.5
KP_SEED_AMP = 0.85     # v14 canonical seed (test_master_equation_v14_mode_i.py:35)
KP_SEED_RADIUS = 2.5
KP_STEPS = 600
KP_TRANSIENT = 200


def _run_known_positive(amplitude=KP_SEED_AMP, cfl=0.4, N_kp=24, nsteps=KP_STEPS):
    """Run the standalone MasterEquationFDTD v14 verdict-II cage and report
    whether the solver HELDS it (bucket-1 gate) + its longitudinal Z-at-core."""
    eng = MasterEquationFDTD(
        N=N_kp, dx=KP_DX, V_yield=1.0, c0=1.0, cfl_safety=cfl, pml_thickness=4
    )
    c = N_kp // 2
    coords = np.arange(N_kp) - c
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * KP_DX
    seed = amplitude * (1.0 / np.cosh(r / KP_SEED_RADIUS))
    eng.V[:] = seed
    eng.V_prev[:] = seed.copy()

    v_peak, n_min, diverged = [], [], None
    for s in range(nsteps):
        eng.step()
        vmax = float(np.abs(eng.V).max())
        if not np.isfinite(vmax) or vmax > 1e3:
            diverged = s
            break
        if s >= nsteps // 3:
            v_peak.append(vmax)
            n_min.append(float(eng.refractive_index().min()))
    if diverged is not None or not v_peak:
        return {
            "held": False, "diverged_at": diverged, "cfl": float(cfl), "N": int(N_kp),
            "v_peak_mean": float("nan"), "std_over_mean": float("nan"),
            "S_core": float("nan"), "Z_long_core": float("nan"),
        }
    vp = np.asarray(v_peak)
    nm = np.asarray(n_min)
    som = float(vp.std() / max(vp.mean(), 1e-9))
    S_core = float(nm.min() ** 4)          # refractive_index = S^(1/4)
    Z_long = float(np.sqrt(max(S_core, 0.0)))  # Z_long/Z_0 = √S
    held = bool(vp.mean() > 0.2 and 0.05 < som < 0.5 and nm.min() < 0.97)
    return {
        "held": held, "diverged_at": diverged, "cfl": float(cfl), "N": int(N_kp),
        "v_peak_mean": float(vp.mean()), "std_over_mean": som,
        "S_core": S_core, "Z_long_core": Z_long,
    }


def _known_positive_gate() -> dict:
    """Bucket-1 gate + apparatus-floor sweep on the KNOWN-POSITIVE cage.
    Held across amplitude × cfl → the instrument is adequate; a coupled failure
    cannot then be blamed on the integrator."""
    base = _run_known_positive(amplitude=KP_SEED_AMP, cfl=0.4)
    sweep = []
    for amp in (0.85, 0.97):
        for cfl in (0.4, 0.2):
            sweep.append(_run_known_positive(amplitude=amp, cfl=cfl))
    held_all = base["held"] and all(p["held"] for p in sweep)
    Z_trend = [p["Z_long_core"] for p in sweep if np.isfinite(p["Z_long_core"])]
    return {
        "instrument_adequate": bool(held_all),
        "base": base,
        "sweep": sweep,
        "Z_long_core_min": float(min(Z_trend)) if Z_trend else float("nan"),
        "note": (
            "KNOWN-POSITIVE = standalone MasterEquationFDTD v14 cage (the engine "
            "with c_eff(V); master_equation_fdtd.py:13). Z_long/Z_0=√S→0 at core IS "
            "the stiffening-confinement signature. If instrument_adequate is True, "
            "any coupled-engine blow-up is NOT numerical (bucket-1 cleared)."
        ),
    }


# ══════════════════════════════════════════════════════════════════════════
# STEP 2/3/4 — COUPLED ENGINE: Op17-bounded Γ=−1 BC (CP10) + precursor seed (CP8)
# ══════════════════════════════════════════════════════════════════════════
def _make_engine(K=K_WALL, cfl=CFL_SAFE, couple_v=True, implicit=True):
    """COUPLED K4⊗Cosserat engine with the moving reflective Γ=−1 boundary.

    CP10 (no-blow-up discipline): use_impedance_boundary=True renders Axiom-4
    saturation as a saturable BOUNDARY CONDITION (Op17-bounded |Γ|→1 as A→1):
      • V-sector "3": Op14 z_local→0 short → bond Γ→−1 (k4_tlm op3_bond_reflection)
      • Cosserat "2": reactive node-clamp by the EXACT reactance-pair rotation
        (_rotate_clamp; energy conserved any τ; cosserat_field_3d.py).
    The bulk V→ω W_refl gradient force (_compute_coupling_force_on_cosserat — the
    documented runaway channel) is NOT on this path; the sectors couple ONLY
    through the shared front. This is the Op17-bounded-wall rendering, NOT a
    bulk energy/force term (the CP10 requirement)."""
    cfg = EngineConfig(
        N=N, pml=PML,
        use_impedance_boundary=True,
        couple_v_sector=couple_v,
        impedance_implicit=implicit,
        impedance_clamp_strength=K,
        impedance_cfl_safety=cfl,
        use_asymmetric_saturation=True,   # κ_chiral chirality bias (default)
    )
    return VacuumEngine3D(cfg)


def _seed_photon(eng, amplitude, helicity=1.0):
    """CP8 — seed the GENERATIVE PRECURSOR: a transverse Z₀-matched helical
    ω-photon. NOT a planted finished electron end-state. The K4 V-sector is left
    at 0; the moving Γ=−1 wall must FORM from the confining photon's own
    self-saturation. Scope (honest): tests whether a PRECURSOR-GROWN trap is
    integrator-stable + reads its Z; does NOT claim the (2,3) electron emerges
    (that is the Stage-2 topology read)."""
    eng.cos.initialize_gaussian_wavepacket_omega(
        CENTER, sigma=SIGMA, direction=(1, 0, 0), wavelength=LAM,
        amplitude=amplitude, axis=2, helicity=helicity,
    )


# ──────────────────────────────────────────────────────────────────────────
# THE LOAD-BEARING MEASUREMENT — Z AT THE SATURATED WALL (bucket-2-vs-3 discrim.)
# ──────────────────────────────────────────────────────────────────────────
def _interior_mask(eng) -> np.ndarray:
    """PML-excluded interior (A-Rule 10 corollary — PML cells are frozen-absorbing
    artifact, never interior physics). All Cosserat-alive sites minus PML shell."""
    Nn, pml = eng.N, eng.config.pml
    m = np.zeros((Nn, Nn, Nn), dtype=bool)
    m[pml:Nn - pml, pml:Nn - pml, pml:Nn - pml] = True
    return m & eng.cos.mask_alive


# ──────────────────────────────────────────────────────────────────────────
# Witnesses (ave-conserved-vs-pumped + A-Rule 10 reactance pair)
# ──────────────────────────────────────────────────────────────────────────
def _omega_max(eng) -> float:
    """C-state amplitude — peak |ω| (the blow-up witness)."""
    return float(np.abs(np.asarray(eng.cos.omega)).max())


def _omega_dot_max(eng) -> float:
    """L-state — peak |ω̇| (A-Rule 10 reactance pair: snapshot of ω alone can't
    distinguish a static config from an oscillator caught at peak; record BOTH)."""
    return float(np.abs(np.asarray(eng.cos.omega_dot)).max())


def _H_total(eng) -> float:
    """THE FULL-HAMILTONIAN WITNESS the brief mandates — total_hamiltonian() =
    E_K4 + T_cos(kinetic) + E_cos(GRADIENT POTENTIAL) + E_coupling. NOT sum(ω²)
    (the C-arc false positive, passive_eigenmode_driver.py:1044-1051: amplitude-
    only is blind to the gradient-potential pump). KEEP-BOTH with _H_impedance."""
    return float(eng._coupled.total_hamiltonian())


def _H_impedance(eng) -> float:
    """The engine's OWN conserved invariant on the impedance-boundary path:
    H = E_K4 + T_cos + W_linear(bulk) + V_clamp (the reactive Γ=−1 wall storage,
    k4_cosserat_coupling.py:725). What the dynamics actually integrate; energy
    sloshes between kinetic / linear-elastic / wall-reactive storage (the
    reactance pair). Reported alongside total_hamiltonian() so wall-storage
    exchange is not mis-read as a pump."""
    try:
        return float(eng._coupled.impedance_hamiltonian()["H"])
    except Exception:
        return float("nan")


def _cosserat_confined_energy(eng) -> float:
    """Interior (PML-excluded) Cosserat trap energy: ½I_ω|ω|² + ½ρ|u|² + kinetic.
    The channel an ω-photon precursor actually populates (the K4 Φ_link bond
    channel stays 0 when V_inc=0 on this path — surfaced below)."""
    interior = _interior_mask(eng)[..., None]
    w = np.asarray(eng.cos.omega) * interior
    u = np.asarray(eng.cos.u) * interior
    wd = np.asarray(eng.cos.omega_dot) * interior
    ud = np.asarray(eng.cos.u_dot) * interior
    return float(
        0.5 * eng.cos.I_omega * np.sum(w**2)
        + 0.5 * eng.cos.rho * np.sum(u**2)
        + 0.5 * eng.cos.I_omega * np.sum(wd**2)
        + 0.5 * eng.cos.rho * np.sum(ud**2)
    )


def _record_step(eng) -> dict:
    """One witness sample: reactance PAIR (ω C-state, ω̇ L-state) + BOTH
    Hamiltonian witnesses + Z-at-wall + the Cosserat confined-energy channel."""
    z = _z_at_wall(eng)
    return {
        "t": float(eng.time),
        "step": int(eng.step_count),
        "omega_C": _omega_max(eng),
        "omega_dot_L": _omega_dot_max(eng),
        "H_total": _H_total(eng),
        "H_impedance": _H_impedance(eng),
        "max_V_inc": float(np.abs(np.asarray(eng.k4.V_inc)).max()),
        "E_cos_confined": _cosserat_confined_energy(eng),
        "Z_wall_med": z.get("Z_eff_at_wall_median", float("nan")),
        "Z_wall_min": z.get("Z_eff_at_wall_min", float("nan")),
        "Z_peakA2": z.get("Z_eff_at_peakA2", float("nan")),
        "n_sat": z.get("n_saturated", 0),
        "max_A2_cos": z.get("max_A2_cos_interior", 0.0),
    }


def _ledger_ramp(series) -> float:
    """ave-conserved-vs-pumped ramp metric: tail/baseline of a positive-definite
    energy series (post-transient). ramp ≈ 1 → flat (passive); < 1 → decaying;
    >> 1 → PUMP. Uses post-transient baseline (wall forms over ~1 Compton period)
    so the seed→trap transient is not mis-counted as a pump."""
    arr = np.asarray([h for h in series if np.isfinite(h)], dtype=float)
    if arr.size < 3:
        return float("nan")
    k = max(1, arr.size // 5)
    base = float(np.median(np.abs(arr[:k])))
    tail = float(np.median(np.abs(arr[-k:])))
    if base < 1e-30:
        return float("inf") if tail > 1e-30 else 1.0
    return tail / base


def _z_at_wall(eng, sat_frac=0.5) -> dict:
    """Measure the local impedance Z_eff = Z₀·√(S_μ/S_ε) AT the saturated
    bond(s) of the COUPLED engine — the bucket-2-vs-3 discriminator.

    Reuses the engine's OWN wall infrastructure:
      • _impedance_gamma_shared() → Γ(r) = (Z_eff−1)/(Z_eff+1) at every cell
        (k4_cosserat_coupling.py:647-675), from which Z_eff = (1+Γ)/(1−Γ).
      • the saturated set = cells where Cosserat A² ≥ sat_frac (the wall).

    READING (INVARIANT-S2 Q1=B, Grant-ratified):
      Z_eff → 0  at the wall  ⇒ |Γ|→1 with Γ<0 (μ-short)  ⇒ TRUE stiffening A1
                  confinement (the electron route). bucket → PORTS / NO-TRAP.
      Z_eff → ∞ (or not collapsing) ⇒ ε-side rupture / softening proxy, NOT the
                  A1 stiffening cage. bucket → c_eff(V)-STRUCTURAL-GAP.

    CRITICAL CAVEAT (engine-reality, surfaced not papered): this Z_eff is the
    TRANSVERSE Meissner impedance √(S_μ/S_ε) (k4_cosserat_coupling.py:548,
    INVARIANT-S2 "transverse-T2 √(μ/ε)"), NOT the LONGITUDINAL A1 tank
    √(L/C_comp). The capability-map (engine-capability-map.md:45,79) says
    VacuumEngine3D has NO independent A1 field — so a Z_eff→0 here is the
    TRANSVERSE sector's confinement, and whether that IS the A1 stiffening cage
    or merely its transverse proxy is exactly the bucket-2 question. The
    standalone known-positive (step 1) carries the genuine LONGITUDINAL Z_long=√S;
    comparing the two is what distinguishes a true cage from the projection."""
    coupled = eng._coupled
    gamma = coupled._impedance_gamma_shared()          # Γ(r) over the lattice
    # Z_eff from Γ: Z_eff = (1+Γ)/(1−Γ); clamp denom for Γ→1
    Z_eff = (1.0 + gamma) / np.maximum(1.0 - gamma, 1e-12)

    # Cosserat A² per site (the wall = cells at/above sat_frac).
    from ave.topological.vacuum_engine import _cosserat_A_squared
    A2_cos = _cosserat_A_squared(
        eng.cos.u, eng.cos.omega, eng.cos.dx,
        eng.cos.omega_yield, eng.cos.epsilon_yield,
    )
    # PML-excluded interior only (A-Rule 10 corollary).
    interior = _interior_mask(eng)
    sat = (A2_cos >= sat_frac) & interior
    n_sat = int(np.sum(sat))

    if n_sat == 0:
        # no wall yet → report the deepest-saturation cell's Z as the proto-wall
        idx = np.unravel_index(np.argmax(np.where(interior, A2_cos, -1.0)), A2_cos.shape)
        return {
            "n_saturated": 0,
            "max_A2_cos_interior": float(A2_cos[interior].max()) if interior.any() else 0.0,
            "Z_eff_at_peakA2": float(Z_eff[idx]),
            "gamma_at_peakA2": float(gamma[idx]),
            "Z_eff_at_wall_median": float("nan"),
            "Z_eff_at_wall_min": float("nan"),
            "gamma_at_wall_median": float("nan"),
        }
    return {
        "n_saturated": n_sat,
        "max_A2_cos_interior": float(A2_cos[interior].max()),
        "Z_eff_at_wall_median": float(np.median(Z_eff[sat])),
        "Z_eff_at_wall_min": float(Z_eff[sat].min()),
        "Z_eff_at_wall_max": float(Z_eff[sat].max()),
        "gamma_at_wall_median": float(np.median(gamma[sat])),
        "gamma_at_wall_min": float(gamma[sat].min()),
    }


# ──────────────────────────────────────────────────────────────────────────
# Persistence read — saturated vs unsaturated channel (the engine's own signal)
# ──────────────────────────────────────────────────────────────────────────
def _persistence_periods(hist, key, drop=1.0 / np.e) -> float:
    """# Compton periods the channel `key` stays above 1/e of its peak. After
    the trap forms, the saturated channel should persist ≥10 periods while the
    unsaturated decays in ~3 (the Phase-3 persistence asymmetry)."""
    if not hist:
        return 0.0
    ts = np.asarray([d["t"] for d in hist], dtype=float)
    vals = np.asarray([d.get(key, 0.0) for d in hist], dtype=float)
    if vals.max() < 1e-30:
        return 0.0
    pk = int(np.argmax(vals))
    thr = vals[pk] * drop
    after = vals[pk:]
    below = np.where(after < thr)[0]
    survive = (ts[-1] - ts[pk]) if below.size == 0 else (ts[pk + int(below[0])] - ts[pk])
    return float(survive / T_COMPTON)


def _run_one(K=K_WALL, amplitude=A_LOCK, cfl=CFL_SAFE, n_periods=N_PERIODS,
             sample_every=4, bond_cadence=4):
    """Seed the photon precursor in a fresh Op17-bounded engine, evolve
    n_periods Compton periods, record the witness trajectory + Z-at-wall + the
    saturated/unsaturated channels."""
    eng = _make_engine(K=K, cfl=cfl)
    _seed_photon(eng, amplitude=amplitude, helicity=1.0)
    bond_obs = BondObserver(cadence=bond_cadence, saturation_frac=0.5)
    energy_obs = EnergyBudgetObserver(cadence=sample_every)
    eng.add_observer(bond_obs)
    eng.add_observer(energy_obs)

    nsteps = _steps_for_periods(eng, n_periods)
    traj = [_record_step(eng)]
    diverged = None
    for s in range(nsteps):
        eng.step()
        if (s % sample_every == 0) or (s == nsteps - 1):
            rec = _record_step(eng)
            traj.append(rec)
            if (not np.isfinite(rec["omega_C"])) or rec["omega_C"] > 1e4 * max(amplitude, 1e-6):
                diverged = s
                break

    oc = [r["omega_C"] for r in traj]
    odl = [r["omega_dot_L"] for r in traj]
    Ht = [r["H_total"] for r in traj]
    Hi = [r["H_impedance"] for r in traj]

    # Z-at-wall trajectory (the discriminator). Median over saturated cells
    # while ≥1 cell is saturated; the post-transient median is the headline.
    z_med = [r["Z_wall_med"] for r in traj if np.isfinite(r["Z_wall_med"])]
    z_min = [r["Z_wall_min"] for r in traj if np.isfinite(r["Z_wall_min"])]
    z_wall_post = (float(np.median(z_med[len(z_med) // 5:])) if z_med else float("nan"))
    z_wall_floor = (float(np.nanmin(z_min)) if z_min else float("nan"))

    cos_traj = [{"t": r["t"], "E_cos_confined": r["E_cos_confined"]} for r in traj]
    cos_persist = _persistence_periods(cos_traj, "E_cos_confined")
    sat_p = _persistence_periods(bond_obs.history, "phi_at_saturated_bonds_rms")
    unsat_p = _persistence_periods(bond_obs.history, "phi_at_unsaturated_bonds_rms")

    return {
        "K_wall": float(K), "amplitude": float(amplitude), "cfl": float(cfl),
        "nsteps": int(nsteps), "outer_dt": float(eng.outer_dt),
        "n_sub": int(eng._coupled.n_sub), "dt_sub": float(eng._coupled.dt_sub),
        "diverged_at_step": diverged,
        "omega_C_seed": float(oc[0]) if oc else 0.0,
        "omega_C_max": float(np.nanmax(oc)) if oc else 0.0,
        "omega_C_final": float(oc[-1]) if oc else 0.0,
        "omega_dot_L_max": float(np.nanmax(odl)) if odl else 0.0,
        "H_total_ramp": _ledger_ramp(Ht), "H_impedance_ramp": _ledger_ramp(Hi),
        "H_total_series": [float(h) for h in Ht],
        "H_impedance_series": [float(h) for h in Hi],
        # ── THE Z-AT-WALL DISCRIMINATOR ──
        "Z_wall_post_median": z_wall_post,
        "Z_wall_floor": z_wall_floor,
        "Z_wall_series": [float(r["Z_wall_med"]) for r in traj],
        "max_A2_cos_final": float(traj[-1]["max_A2_cos"]) if traj else 0.0,
        "n_sat_peak": int(max((r["n_sat"] for r in traj), default=0)),
        # ── persistence ──
        "cos_confined_persist_periods": cos_persist,
        "E_cos_confined_peak": float(max((r["E_cos_confined"] for r in traj), default=0.0)),
        "E_cos_confined_final": float(traj[-1]["E_cos_confined"]) if traj else 0.0,
        "sat_persist_periods": sat_p, "unsat_persist_periods": unsat_p,
        "V_sector_energized": bool(float(np.nanmax([r["max_V_inc"] for r in traj])) > 1e-9),
        "trajectory": traj,
    }


# ══════════════════════════════════════════════════════════════════════════
# FOUR-WAY BINNING — the auditor-mandated buckets (NOT collapsed to binary).
# Pre-registered adjudication thresholds (frozen; NOT dropped post-hoc, Rule 11):
# ══════════════════════════════════════════════════════════════════════════
RAMP_PUMP_CEIL = 2.0        # H_total ramp > this → PUMPS
OMEGA_BLOWUP_FACTOR = 1e3   # |ω|max / seed > this → numerical blow-up flag
Z_STIFFENING_CEIL = 0.5     # Z_wall ≤ this (→0) = TRUE stiffening confinement
SAT_PERSIST_MIN = 10.0      # confined channel must persist ≥ this many periods


def _bin_run(r: dict, instrument_adequate: bool) -> tuple[str, str]:
    """Resolve a coupled run into one of the FOUR auditor buckets + reason.
    A naive 'BLOW-UP' is NOT a bucket — it is resolved via the known-positive
    gate (bucket 1) + the Z-at-wall measurement (buckets 2/3)."""
    seed = max(r["omega_C_seed"], 1e-6)
    blew = (r["diverged_at_step"] is not None) or (not np.isfinite(r["omega_C_max"])) \
        or (r["omega_C_max"] / seed > OMEGA_BLOWUP_FACTOR)

    # ── Bucket 1: INTEGRATOR-INADEQUATE — only if the known-positive FAILED ──
    if blew and not instrument_adequate:
        return "INTEGRATOR-INADEQUATE", (
            f"|ω|max/seed={r['omega_C_max']/seed:.1e} blew up AND the known-positive "
            f"standalone cage did NOT hold → numerical, not physics."
        )

    ramp = r["H_total_ramp"]
    Zw = r["Z_wall_post_median"]
    Zf = r["Z_wall_floor"]
    z_stiffening = np.isfinite(Zw) and (Zw <= Z_STIFFENING_CEIL or Zf <= Z_STIFFENING_CEIL)

    # ── PUMPS: full-Hamiltonian ledger climbs (checked before the Z buckets so a
    #    pumping run is named as an ontology finding, not mis-binned) ──
    if np.isfinite(ramp) and ramp > RAMP_PUMP_CEIL:
        return "PUMPS", (
            f"full-Hamiltonian ledger ramp={ramp:.2f} > {RAMP_PUMP_CEIL} "
            f"(H_impedance ramp={r['H_impedance_ramp']:.2f}) → trap not passive; "
            f"Z_wall={Zw:.3f}"
        )

    # ── If it blew up but the instrument is adequate → physics blow-up; route by Z ──
    persists = r["cos_confined_persist_periods"] >= SAT_PERSIST_MIN
    zdetail = (
        f"Z_wall_post={Zw:.3f} floor={Zf:.3f} (A²_cos_final={r['max_A2_cos_final']:.1f}, "
        f"n_sat_peak={r['n_sat_peak']}); |ω|max/seed={r['omega_C_max']/seed:.2f}; "
        f"H_total ramp={ramp:.2f}; cos_persist={r['cos_confined_persist_periods']:.1f}P"
    )

    # ── Bucket 2: c_eff(V)-STRUCTURAL-GAP — wall forms (A²≫1, n_sat>0) but Z does
    #    NOT →0. The softening proxy, not C_eff→∞. Confirms cap-map :45/:79. ──
    wall_formed = r["n_sat_peak"] > 0 or r["max_A2_cos_final"] >= 0.5
    if wall_formed and not z_stiffening:
        return "c_eff(V)-STRUCTURAL-GAP", (
            "🔧 wall forms but Z does NOT collapse to 0 — the TRANSVERSE softening "
            f"proxy (Z_eff=√(S_μ/S_ε)≈Z₀), NOT the C_eff→∞/Z→0 longitudinal A1 "
            f"stiffening cage. Confirms engine-capability-map.md:45/:79. → coupled "
            f"engine needs a true c_eff(V)/independent-A1 field (a BOUNDED build). "
            f"{zdetail}"
        )

    # ── From here Z IS stiffening (Z→0) — buckets 3 / PORTS depend on stability ──
    if z_stiffening and (blew or not persists):
        return "PHYSICAL-NO-TRAP", (
            "🔴 Z→0 stiffening confinement IS present AND the known-positive held, "
            f"but the trap does NOT remain bounded/persistent ({'diverged' if blew else 'dispersed'}). "
            f"ECHO candidate (the only bucket that bears on echo). {zdetail}"
        )

    if z_stiffening and not blew and persists:
        return "PORTS-STABLE", (
            "Z→0 stiffening confinement + |ω| bounded + ledger flat + trap persists "
            f"≥10P → boundary readable, Stage 2 greenlit. {zdetail}"
        )

    # bounded, passive, no wall, no stiffening Z → integrator-stable but no trap
    return "c_eff(V)-STRUCTURAL-GAP", (
        "🔧 no Z→0 stiffening confinement formed (Z stays ≈Z₀); integrator-stable "
        f"and passive but no longitudinal A1 cage. {zdetail}"
    )


def main() -> dict:
    raise NotImplementedError("skeleton — sections land incrementally")


if __name__ == "__main__":
    main()
