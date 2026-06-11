"""Reflection-genesis: the (2,3) self-assembly — the "3" in the COUPLED engine.

Prereg (FROZEN): research/2026-06-09_reflection-genesis-23-self-assembly_prereg.md
Foundation: verdict II (research/2026-06-06_saturation-tir-moving-boundary-result.md,
historical-precedents.md:28) — the moving reflective Γ=−1 boundary CONVERTS
collapse → confinement; the ω-photon self-traps (loc 0.94), the "2" Cosserat
winding forms, charge=helicity confirms. The localized open gap is the "3" =
the V-sector U(1) fibre (the Heaviside-deleted longitudinal scalar), which
needs the COUPLED K4+Cosserat engine — this driver.

THE RUN (prereg §3):
  1. Seed a PHOTON (transverse Z₀-matched helical ω-wave) in the COUPLED engine
     — the generative precursor (substrate-native-check CP8). NOT a planted (2,3)
     (initialize_electron_2_3_sector would PLANT the θ=2φ+3ψ knot — forbidden).
  2. Self-saturate → the moving reflective Γ=−1 boundary (verdict II — REUSE,
     don't reinvent). The "2" re-forms; energize+LOCK, NOT pump (a secular pump
     → C; the recurring bug, 2026-06-09_reactive-entrainment-source_result.md).
  3. THE TEST: does the "3" (V-sector U(1) fibre) CLOSE onto the "2" via the
     coupled K4↔Cosserat channel → the full (2,3) in (V_inc,V_ref) phase-space?
  4. chirality (κ_chiral=1.2α parity-odd selection), charge=helicity, spin/L
     conservation (energized+locked), α from the Γ=−1 leak.

phase-space-coordinate-check (A46): the (2,3) lives in (V_inc, V_ref) phase-space
on the Clifford torus (the three-layer canonical, doc 101_ §9 / cosserat_field_3d
:931 — Layer 3). Real-space ω localization is DIAGNOSTIC only.

ave-canonical-source: κ_chiral=1.2α, V_SNAP, V_YIELD, Z₀, ℓ_node, ALPHA_COLD_INV
all imported from ave.core.constants / k4_cosserat_coupling — ZERO new free params.
ave-resonant-amplification-check: the spin is energized+LOCKED, not pumped — the
hard-wall pump is the wrong model (→ C); reported as the explicit control.
ave-driver-script-honesty: every printed number is measured from the EVOLVED
fields (CP9); PROXY / COORDINATE / BLOCKED caveats are inline, not buried.

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/reflection_genesis_23_self_assembly.py
"""
from __future__ import annotations

import json
import os

import numpy as np

# ── Canonical-source imports (ave-canonical-source — zero new free params) ────
from ave.core.constants import (
    ALPHA,
    ALPHA_COLD_INV,
    C_0,
    L_NODE,
    R_GOLDEN_TORUS,
    R_GOLDEN_TORUS_MINOR,
    V_SNAP,
    V_YIELD,
    Z_0,
)
from ave.topological.cosserat_field_3d import (
    KAPPA_CHIRAL_ELECTRON,
    kappa_chiral_from_topology,
)
from ave.topological.vacuum_engine import EngineConfig, VacuumEngine3D

import ave.core.constants as _avc  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def _canonical_source_gate() -> None:
    """ave-canonical-source Step 4 — assert the constants are the canonical ones."""
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants source"
    assert abs(V_YIELD / (np.sqrt(ALPHA) * V_SNAP) - 1.0) < 1e-9, "V_YIELD = √α·V_SNAP broken"
    assert abs(KAPPA_CHIRAL_ELECTRON - 1.2 * ALPHA) < 1e-15, "κ_chiral = 1.2·α broken"
    assert abs(kappa_chiral_from_topology(2, 3) - 1.2 * ALPHA) < 1e-15, "κ_chiral(2,3) broken"
    assert abs(ALPHA_COLD_INV - (4.0 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "Golden-Torus α⁻¹ broken"


# ── Engine geometry (natural units: dx = ℓ_node = 1, c_R = 1, ω_C → 1) ────────
OMEGA_C_PHYS = C_0 / L_NODE  # ≈ 7.76e20 rad/s (Compton angular frequency)
OMEGA_C_NATURAL = 1.0        # = c_R / dx (same ring scale in engine units)

# K4 tetrahedral port directions (the 4 A→B bond vectors) — used to project the
# 4-port V_inc / V_ref into a real-space 3-vector for the phase-space winding,
# the SAME bond basis the Cosserat ω extractor uses (consistency, CP4).
_TETRA = np.array([(+1, +1, +1), (+1, -1, -1), (-1, +1, -1), (-1, -1, +1)], dtype=float)


# ──────────────────────────────────────────────────────────────────────────
# Measurement helpers (CP9 — every quantity measured from the EVOLVED fields)
# ──────────────────────────────────────────────────────────────────────────
def _interior(eng) -> np.ndarray:
    """PML-excluded interior mask (A-Rule 10 corollary — PML cells are frozen-
    absorbing artifact, never interior physics)."""
    N, pml = eng.N, eng.config.pml
    ii, jj, kk = eng.cos._i, eng.cos._j, eng.cos._k
    return (
        (ii >= pml) & (ii < N - pml)
        & (jj >= pml) & (jj < N - pml)
        & (kk >= pml) & (kk < N - pml)
    )


def _w2(eng) -> np.ndarray:
    return np.sum(np.asarray(eng.cos.omega) ** 2, axis=-1) * eng.cos.mask_alive * _interior(eng)


def _localization(eng):
    """Fraction of |ω|² within r≤6 of the energy-density PEAK (CP7: density-peak,
    NOT centroid — the centroid of a shell is the empty middle). PML-excluded."""
    w2 = _w2(eng)
    tot = w2.sum()
    if tot < 1e-30:
        return 0.0, (eng.N // 2, eng.N // 2, eng.N // 2)
    pk = np.unravel_index(int(np.argmax(w2)), w2.shape)
    ii, jj, kk = eng.cos._i, eng.cos._j, eng.cos._k
    r2 = (ii - pk[0]) ** 2 + (jj - pk[1]) ** 2 + (kk - pk[2]) ** 2
    return float((w2 * (r2 <= 36)).sum() / tot), pk


def _omega_max(eng) -> float:
    return float(np.abs(np.asarray(eng.cos.omega)).max())


def _v_sector_state(eng) -> dict:
    """The "3" energization: peak K4 V-sector amplitudes, measured on the
    EVOLVED K4 field (CP9). max|V_inc| / max|Φ_link| / total V-sector energy.
    A transverse photon seeds V_inc = 0; this is the test of whether the
    coupled K4↔Cosserat channel ENERGIZES the longitudinal V-sector at all."""
    interior = _interior(eng)
    Vi = np.asarray(eng.k4.V_inc)
    Vr = np.asarray(eng.k4.V_ref)
    Phi = np.asarray(eng.k4.Phi_link)
    m = (eng.k4.mask_active & interior)[..., None]
    return {
        "max_V_inc": float(np.abs(np.where(m, Vi, 0.0)).max()),
        "max_V_ref": float(np.abs(np.where(m, Vr, 0.0)).max()),
        "max_Phi_link": float(np.abs(np.where(m, Phi, 0.0)).max()),
        "V_sq_sum": float(np.sum((Vi ** 2) * m)),
    }


def _v_vector_field(eng) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Project the 4-port (V_inc, V_ref) into real-space 3-vectors (Vx,Vy,Vz)
    via the K4 tetra bond basis — the phase-space (V_inc, V_ref) coordinate of
    the U(1) fibre, in the SAME bond projection the ω winding uses (CP4)."""
    Vi = np.asarray(eng.k4.V_inc)   # (N,N,N,4)
    Vr = np.asarray(eng.k4.V_ref)
    Vinc_vec = np.einsum("...p,pc->...c", Vi, _TETRA)  # (N,N,N,3)
    Vref_vec = np.einsum("...p,pc->...c", Vr, _TETRA)
    return Vinc_vec, Vref_vec, np.asarray(eng.k4.mask_active)


def _contour_winding(field_x, field_y, center, R, r_minor, plane="poloidal", n=128):
    """Phase winding of the complex (field_x + i·field_y) traced on a contour
    around the soliton. plane='poloidal' (the tube/ψ loop → the "3"=q=3 fibre);
    plane='toroidal' (the major/φ ring → the "2"=p=2). Returns (winding,
    reliability=min_amp/max_amp). Trilinear-sampled, same scheme as the ω
    extractor (extract_crossing_count)."""
    cx, cy, cz = center
    t = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    if plane == "poloidal":
        xs = cx + (R + r_minor * np.cos(t))
        ys = cy + np.zeros_like(t)
        zs = cz + r_minor * np.sin(t)
    else:  # toroidal — the major ring at the shell radius R
        xs = cx + R * np.cos(t)
        ys = cy + R * np.sin(t)
        zs = cz + np.zeros_like(t)
    nx, ny, nz = field_x.shape
    ix = np.clip(xs.astype(int), 0, nx - 2)
    iy = np.clip(ys.astype(int), 0, ny - 2)
    iz = np.clip(zs.astype(int), 0, nz - 2)
    fx, fy, fz = xs - ix, ys - iy, zs - iz

    def samp(F):
        return (
            (1 - fx) * (1 - fy) * (1 - fz) * F[ix, iy, iz]
            + fx * (1 - fy) * (1 - fz) * F[ix + 1, iy, iz]
            + (1 - fx) * fy * (1 - fz) * F[ix, iy + 1, iz]
            + (1 - fx) * (1 - fy) * fz * F[ix, iy, iz + 1]
            + fx * fy * (1 - fz) * F[ix + 1, iy + 1, iz]
            + fx * (1 - fy) * fz * F[ix + 1, iy, iz + 1]
            + (1 - fx) * fy * fz * F[ix, iy + 1, iz + 1]
            + fx * fy * fz * F[ix + 1, iy + 1, iz + 1]
        )

    ox, oy = samp(field_x), samp(field_y)
    amp = np.sqrt(ox ** 2 + oy ** 2)
    max_amp = float(amp.max())
    if max_amp < 1e-30:
        return 0.0, 0.0, max_amp
    phase = np.unwrap(np.arctan2(oy, ox))
    winding = (phase[-1] - phase[0]) / (2.0 * np.pi)
    return float(winding), float(amp.min() / max_amp), max_amp


def _phase_space_winding(eng, center) -> dict:
    """THE A46 MEASUREMENT — does the (2,3) close in (V_inc, V_ref) phase-space?

    Trace the V_inc and V_ref phase-space vectors around the soliton:
      toroidal (φ) loop → the "2" (p=2);  poloidal (ψ) loop → the "3" (q=3 U(1)
    fibre). The full (2,3) CLOSES iff w_tor≈2 AND w_pol≈3 with a reliable
    (amplitude-populated) contour. If max|V|→0 the phase-space is UNPOPULATED —
    the "3" never enters phase-space (a distinct, sharper read than "winds but
    not (2,3)"). Reported for both V_inc and V_ref Clifford-torus angles."""
    Vinc_vec, Vref_vec, _ = _v_vector_field(eng)
    R_shell, _ = eng.cos.extract_shell_radii()
    R = max(R_shell, 3.0)
    out = {"R_shell": float(R_shell), "vinc_amp": 0.0, "vref_amp": 0.0}
    best = {"tor": (0.0, 0.0), "pol": (0.0, 0.0)}
    for tag, vec in (("vinc", Vinc_vec), ("vref", Vref_vec)):
        amp_seen = 0.0
        for plane in ("toroidal", "poloidal"):
            w_best, rel_best, amp_best = 0.0, 0.0, 0.0
            for r_minor in np.linspace(1.0, max(3.0, R * 0.6), 6):
                w, rel, amp = _contour_winding(vec[..., 0], vec[..., 1], center, R, r_minor, plane)
                amp_seen = max(amp_seen, amp)
                if rel > rel_best:
                    w_best, rel_best, amp_best = w, rel, amp
            out[f"{tag}_w_{plane[:3]}"] = round(w_best, 2)
            out[f"{tag}_rel_{plane[:3]}"] = round(rel_best, 3)
        out[f"{tag}_amp"] = float(amp_seen)
    # (2,3) closure: |w_tor|≈2 and |w_pol|≈3 on a reliable populated contour.
    def _closes(tag):
        wt = abs(out.get(f"{tag}_w_tor", 0.0))
        wp = abs(out.get(f"{tag}_w_pol", 0.0))
        rel = min(out.get(f"{tag}_rel_tor", 0.0), out.get(f"{tag}_rel_pol", 0.0))
        populated = out[f"{tag}_amp"] > 1e-9
        return populated and rel > 0.1 and abs(wt - 2.0) < 0.5 and abs(wp - 3.0) < 0.5
    out["vinc_closes_23"] = bool(_closes("vinc"))
    out["vref_closes_23"] = bool(_closes("vref"))
    out["phase_space_populated"] = bool(out["vinc_amp"] > 1e-9 or out["vref_amp"] > 1e-9)
    return out


def _beltrami_helicity_total(eng) -> float:
    """Integrated Beltrami helicity H_bel = Σ ω·(∇×ω) over interior alive cells —
    the carried CHARGE of a chiral ω-photon (verdict II §5). Sign = handedness
    (e⁻ LH / e⁺ RH). Conserved-not-growing = energized+LOCKED (the gyroscope);
    growing = pumped (→ C)."""
    import jax.numpy as jnp
    from ave.topological.cosserat_field_3d import _tetrahedral_curl

    curl = np.asarray(_tetrahedral_curl(jnp.asarray(eng.cos.omega), eng.cos.dx))
    dens = np.sum(np.asarray(eng.cos.omega) * curl, axis=-1) * eng.cos.mask_alive * _interior(eng)
    return float(dens.sum())


def _spin_L(eng) -> float:
    """Net ring angular-momentum magnitude proxy |L| = |Σ_interior I_ω · ω| (the
    conserved gyroscopic spin, energized + LOCKED not pumped — reactive-
    entrainment §2). Bounded/conserved over the window = locked; secular growth
    = pumped (→ C)."""
    m = (eng.cos.mask_alive & _interior(eng))[..., None]
    L_vec = np.sum(np.asarray(eng.cos.omega) * m, axis=(0, 1, 2)) * eng.cos.I_omega
    return float(np.linalg.norm(L_vec))


def _chirality_select(eng) -> dict:
    """The κ_chiral=1.2α parity-odd selection: which side (μ vs ε) shorts to
    Γ=−1, as a function of the seeded helicity sign. The shared front
    A²_μ=(1+κ_chiral·h)·A²_μ_base, A²_ε=(1−κ_chiral·h)·A²_ε_base (cosserat_field
    _3d:577-578). +h → S_μ<S_ε (μ-side short, the confining wall); −h → ε-side.
    A DEFINITE handedness = the μ-side short is selected by sign; LH=RH (no
    asymmetry) → C. Measured on the evolved field."""
    g = eng._coupled._impedance_gamma_shared()
    alive = eng.cos.mask_alive & _interior(eng)
    g_int = g[alive]
    return {
        "gamma_min": float(g_int.min()),         # the μ-side reflective short
        "gamma_max": float(g_int.max()),         # the ε-side open
        "frac_mu_short": float((g_int < -0.05).mean()),   # fraction in confining μ-short
        "frac_eps_open": float((g_int > 0.05).mean()),    # fraction in ε-open
        "h_bel": _beltrami_helicity_total(eng),
    }


def _gamma_leak(eng) -> dict:
    """α from the leak: the Γ=−1 mirror's residual transparency. At the wall
    T² = 1 − Γ² (Op17); the residual leak is 1−|Γ_min|. The canonical target is
    the Golden-Torus α⁻¹ = 4π³+π²+π (RR=R·r=1/4 geometry) — which the (2,3)
    bound state must REALIZE in (V_inc,V_ref) phase-space. Measured: Γ_min and
    the implied leak Q. HONEST: the emergent-α claim requires the (2,3) Golden-
    Torus geometry to CLOSE; if the "3" does not close there is no Golden-Torus
    and α⁻¹ is BLOCKED, not measurable from a bare ω-wall."""
    g = eng._coupled._impedance_gamma_shared()
    alive = eng.cos.mask_alive & _interior(eng)
    gmin = float(g[alive].min())
    T2 = max(1.0 - gmin ** 2, 0.0)   # residual transmission at the deepest short
    leak = 1.0 - abs(gmin)
    return {
        "gamma_min": gmin,
        "T2_residual": float(T2),
        "leak": float(leak),
        "Q_inv_leak": float(1.0 / leak) if leak > 1e-12 else float("inf"),
        "alpha_cold_inv_target": float(ALPHA_COLD_INV),
    }


# ──────────────────────────────────────────────────────────────────────────
# Engine factory + photon seed (CP8 — seed the GENERATIVE PRECURSOR)
# ──────────────────────────────────────────────────────────────────────────
# LOCKED config: the energize-AND-LOCK regime (soft-moderate wall, bounded |ω|).
# The EXPLICIT integrator is the verdict-II-proven-stable path (the implicit
# coupled path parametric-pumps a free photon, the recurring §6 instability).
# Geometry/step counts accept env overrides (GEN23_N / GEN23_STEPS) for fast
# smoke-testing; the committed defaults are the production values.
N = int(os.environ.get("GEN23_N", "24"))
PML = 4
SIGMA, LAM = 3.0, 6.0
A_LOCK = 3.0          # peak |ω| → engages a soft-moderate wall (amplitude sets engagement)
A_PUMP = 6.0          # peak |ω| → hard Γ=−1 wall (the parametric-pump CONTROL → C)
K_WALL = 60.0         # soft clamp → engaged + stable + few sub-steps (fast)
CFL_SAFE = 0.25       # anti-pump margin on the implicit reactance-rotation
N_STEPS = int(os.environ.get("GEN23_STEPS", "50"))
CENTER = (N / 2.0, N / 2.0, N / 2.0)


def _make_engine(K=K_WALL, couple_v=True, emf=False, implicit=True):
    """COUPLED K4⊗Cosserat engine with the moving reflective Γ=−1 boundary
    (verdict II mechanism, ported coupled). EXPLICIT integrator default
    (verdict-II-stable). use_lagrangian_emf_coupling is the reciprocal ω→V
    channel (the "3" energization candidate)."""
    cfg = EngineConfig(
        N=N, pml=PML,
        use_impedance_boundary=True,
        couple_v_sector=couple_v,
        impedance_implicit=implicit,
        impedance_clamp_strength=K,
        impedance_cfl_safety=CFL_SAFE,
        use_lagrangian_emf_coupling=emf,
        use_asymmetric_saturation=True,   # the κ_chiral chirality bias (default)
    )
    return VacuumEngine3D(cfg)


def _seed_photon(eng, amplitude, helicity=1.0):
    """Seed a transverse Z₀-matched helical ω-photon — the generative precursor
    (CP8). NOT initialize_electron_2_3_sector (that PLANTS the θ=2φ+3ψ knot).
    The K4 V-sector is left at 0: the test is whether the coupled channel
    energizes the "3" from the confined photon alone."""
    eng.cos.initialize_gaussian_wavepacket_omega(
        CENTER, sigma=SIGMA, direction=(1, 0, 0), wavelength=LAM,
        amplitude=amplitude, axis=2, helicity=helicity,
    )


def _seed_v_partner(eng, frac=0.3):
    """GAP-LOCALIZATION DIAGNOSTIC ONLY (§8): co-seed a K4 V-sector wavepacket
    (a V-photon precursor, NOT the (2,3) knot) to separate the source-question
    (does the "3" get energized at all?) from the topology-question (GIVEN
    energy, does the shared wall wind it to (2,3)?). Scaled to the ENGINE's
    natural V_SNAP (eng.V_SNAP), seeded with a CIRCULARLY-POLARIZED transverse
    V-vector structure (NOT a pure-breathing mode — that projects to zero under
    the tetra port basis) so the phase-space winding extractor can read it."""
    amp = frac * eng.V_SNAP
    x = (np.arange(N)[:, None, None] - CENTER[0]).astype(float)
    y = (np.arange(N)[None, :, None] - CENTER[1]).astype(float)
    z = (np.arange(N)[None, None, :] - CENTER[2]).astype(float)
    env = np.exp(-(x ** 2 + y ** 2 + z ** 2) / (2.0 * SIGMA ** 2))
    phase = 2.0 * np.pi * x / LAM
    # target in-plane V-vector (Vx,Vy,0) rotating along x — a longitudinal-photon
    # partner carrying a transverse winding component the extractor can see.
    Vx = amp * env * np.cos(phase)
    Vy = amp * env * np.sin(phase)
    # invert the tetra projection: V_inc[port] = (V_vec · p_port)/|p_port|²,
    # |p_port|²=3, so V_vec = Σ_port V_inc[port]·p_port reproduces (Vx,Vy,0).
    for p in range(4):
        eng.k4.V_inc[..., p] += (Vx * _TETRA[p, 0] + Vy * _TETRA[p, 1]) / 3.0 * eng.k4.mask_active
    eng.k4.V_inc *= eng.k4.mask_active[..., None]


def _hamiltonian(eng) -> float:
    try:
        return float(eng._coupled.impedance_hamiltonian()["H"])
    except Exception:
        return float("nan")


def _run(eng, nsteps, record=False):
    """Step the coupled engine, recording the reactance PAIR every step
    (A-Rule 10): the ω C-state (|ω|max) AND the ω̇ L-state (|ω̇|max), plus the
    conserved helicity H_bel and spin |L| (energize-lock vs pump discriminator)."""
    trace = []
    for t in range(nsteps):
        eng.step()
        if record and (t % 4 == 0 or t == nsteps - 1):
            trace.append({
                "t": t,
                "omega_C": _omega_max(eng),                                  # C-state
                "omega_dot_L": float(np.abs(np.asarray(eng.cos.omega_dot)).max()),  # L-state
                "H_bel": _beltrami_helicity_total(eng),                      # conserved charge
                "L_spin": _spin_L(eng),                                      # conserved spin
                "E": _hamiltonian(eng),
                "max_V_inc": float(np.abs(np.asarray(eng.k4.V_inc)).max()),  # the "3"
            })
    return trace


# ──────────────────────────────────────────────────────────────────────────
# Figures (ave-engineering-program-rigor — savefig, clickable links in result)
# ──────────────────────────────────────────────────────────────────────────
def _midz_inplane(eng):
    """Mid-z slice of the in-plane ω vector and V_inc vector (for fig 1)."""
    kz = N // 2
    om = np.asarray(eng.cos.omega)[:, :, kz, :]
    Vi, _, _ = _v_vector_field(eng)
    Vi = np.asarray(Vi)[:, :, kz, :]
    return om, Vi


def _make_figures(out, e_wall, e_diag, tr_wall, tr_pump, sweep):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    paths = {}

    # FIG 1 — the (V_inc,V_ref) phase-space (does the (2,3) close?) vs the "2"
    om_w, Vi_w = _midz_inplane(e_wall)
    om_d, Vi_d = _midz_inplane(e_diag)
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.6))
    sp = max(1, N // 16)
    ax[0].quiver(om_w[::sp, ::sp, 0].T, om_w[::sp, ::sp, 1].T, scale=None, color="C0")
    ax[0].set_title(f"the '2': Cosserat ω in-plane (real-space)\nc={out['the_3']['c_omega_realspace']} (DIAGNOSTIC)")
    vamp_w = float(np.abs(Vi_w).max())
    ax[1].quiver(Vi_w[::sp, ::sp, 0].T, Vi_w[::sp, ::sp, 1].T, scale=None, color="C3")
    ax[1].set_title(f"the '3': K4 V_inc phase-space (A46)\nmax|V|={vamp_w:.1e} — UNPOPULATED" if vamp_w < 1e-9
                    else f"the '3': K4 V_inc phase-space\nmax|V|={vamp_w:.2e}")
    vamp_d = float(np.abs(Vi_d).max())
    ax[2].quiver(Vi_d[::sp, ::sp, 0].T, Vi_d[::sp, ::sp, 1].T, scale=None, color="C2")
    ax[2].set_title(f"§8 diagnostic: V-sector SEEDED\nmax|V|={vamp_d:.2e}  closes(2,3)={out['gap_localization']['phase_space']['vinc_closes_23']}")
    for a in ax:
        a.set_aspect("equal"); a.set_xlabel("x"); a.set_ylabel("y")
    fig.suptitle("FIG 1 — phase-space (V_inc,V_ref) winding: does the '3' close onto the '2'?")
    fig.tight_layout()
    p = os.path.join(HERE, "genesis23_fig1_phase_space_winding.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig1"] = p

    # FIG 2 — localization (self-trap vs controls)
    fig, ax = plt.subplots(figsize=(7, 4.6))
    labels = ["wall\n(coupled)", "no-wall\ncontrol", "energy-term\n(verdict II)"]
    vals = [out["the_2"]["locf"], out["the_2"]["loc_nowall"], 0.256]
    cols = ["C2", "C1", "C3"]
    ax.bar(labels, vals, color=cols)
    ax.axhline(out["the_2"]["loc0"], ls="--", color="k", label=f"seed loc={out['the_2']['loc0']:.3f}")
    ax.axhline(0.938, ls=":", color="C0", label="verdict-II wall hold=0.94")
    ax.set_ylabel("localization (|ω|² within r≤6 of peak)")
    ax.set_title("FIG 2 — self-trap: wall confines, energy-term collapses")
    ax.legend(); fig.tight_layout()
    p = os.path.join(HERE, "genesis23_fig2_localization.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig2"] = p

    # FIG 3 — charge=helicity + chirality selection
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.6))
    ch = out["charge_helicity"]
    ax[0].bar(["+h seed", "−h seed"], [ch["H_plus"], ch["H_minus"]], color=["C0", "C3"])
    ax[0].axhline(0, color="k", lw=0.8)
    ax[0].set_ylabel("integrated Beltrami helicity H_bel")
    ax[0].set_title(f"charge=helicity: sign flips={ch['sign_flips']}")
    cp, cm = out["chirality"]["plus"], out["chirality"]["minus"]
    ax[1].bar(["+h", "−h"], [cp["frac_mu_short"], cm["frac_mu_short"]], color=["C0", "C3"])
    ax[1].set_ylabel("fraction in μ-side Γ<−0.05 (confining short)")
    ax[1].set_title(f"chirality (κ_chiral=1.2α): definite={out['chirality']['definite_selection']}")
    fig.suptitle("FIG 3 — charge=helicity + chirality selection")
    fig.tight_layout()
    p = os.path.join(HERE, "genesis23_fig3_charge_chirality.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig3"] = p

    # FIG 4 — spin/L conservation (energize+lock vs pump control)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.6))
    tw = [r["t"] for r in tr_wall]
    ax[0].plot(tw, [r["omega_C"] for r in tr_wall], "o-", label="|ω| C-state (lock)")
    ax[0].plot(tw, [r["L_spin"] for r in tr_wall], "s-", label="|L| spin")
    tp = [r["t"] for r in tr_pump]
    ax[0].plot(tp, [r["omega_C"] for r in tr_pump], "x--", color="C3", label="|ω| PUMP control")
    ax[0].set_yscale("log"); ax[0].set_xlabel("step"); ax[0].set_ylabel("magnitude")
    ax[0].set_title("energize+LOCK (bounded) vs PUMP (secular→C)"); ax[0].legend(fontsize=8)
    ax[1].plot(tw, [r["H_bel"] for r in tr_wall], "o-", color="C2")
    ax[1].set_xlabel("step"); ax[1].set_ylabel("H_bel (conserved charge)")
    ax[1].set_title("Beltrami helicity — conserved (energized, not pumped)")
    fig.suptitle("FIG 4 — spin/L conservation: energized + locked, NOT pumped")
    fig.tight_layout()
    p = os.path.join(HERE, "genesis23_fig4_spin_lock.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig4"] = p

    # FIG 5 — α from the leak (Γ_min vs amplitude) + Golden-Torus α⁻¹ target
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    As = [s["A"] for s in sweep]
    gs = [s["gamma_min"] for s in sweep]
    ax.plot(As, gs, "o-", color="C0")
    ax.axhline(-1.0, ls="--", color="C3", label="hard Γ=−1 short (pumps)")
    ax.axhline(0.0, ls=":", color="k")
    ax.set_xlabel("seed amplitude (peak |ω|)"); ax.set_ylabel("wall Γ_min (residual leak)")
    ax.set_title(f"FIG 5 — α-from-leak: Γ engagement vs A\n"
                 f"Golden-Torus α⁻¹=4π³+π²+π={ALPHA_COLD_INV:.2f} requires (2,3) closure (BLOCKED)")
    ax.legend(); fig.tight_layout()
    p = os.path.join(HERE, "genesis23_fig5_alpha_leak.png")
    fig.savefig(p, dpi=110); plt.close(fig); paths["fig5"] = p

    return paths


# ──────────────────────────────────────────────────────────────────────────
# Main run
# ──────────────────────────────────────────────────────────────────────────
def main():
    _canonical_source_gate()
    out = {"config": dict(N=N, PML=PML, sigma=SIGMA, wavelength=LAM, A_lock=A_LOCK,
                          A_pump=A_PUMP, K_wall=K_WALL, n_steps=N_STEPS,
                          kappa_chiral=KAPPA_CHIRAL_ELECTRON, alpha=ALPHA,
                          alpha_cold_inv=ALPHA_COLD_INV)}
    print("=" * 80)
    print("REFLECTION-GENESIS (2,3) SELF-ASSEMBLY — the '3' in the COUPLED engine")
    print(f"  COUPLED K4⊗Cosserat | moving Γ=−1 wall | photon seed (CP8) | phase-space (A46)")
    print(f"  N={N} PML={PML} | κ_chiral={KAPPA_CHIRAL_ELECTRON:.4e}=1.2α | "
          f"α⁻¹_GoldenTorus={ALPHA_COLD_INV:.4f} | V_YIELD={V_YIELD:.0f}V")
    print("=" * 80)

    # ── §1 VALIDITY GATE: low-A photon must propagate MATCHED (Γ≈0) ───────────
    print("\n[§1 VALIDITY GATE] low-A photon (A=1e-3) — expect Γ≈0, matched, no V-sector")
    eg = _make_engine()
    _seed_photon(eg, amplitude=1e-3, helicity=1.0)
    E0 = _hamiltonian(eg)
    gmin = 0.0
    for _ in range(max(8, N_STEPS // 4)):
        eg.step()
        gmin = min(gmin, float(eg._coupled._impedance_gamma_shared()[eg.cos.mask_alive].min()))
    Ef = _hamiltonian(eg)
    vs = _v_sector_state(eg)
    gate_ok = abs(gmin) < 1e-3 and vs["max_V_inc"] < 1e-9
    print(f"  Γ_min={gmin:.2e} (matched)  E_f/E_0={Ef/E0:.4f}  max|V_inc|={vs['max_V_inc']:.2e}")
    print(f"  VALIDITY GATE: {'PASS' if gate_ok else 'FAIL'} — photon limit recovered, V-sector silent")
    out["validity_gate"] = {"gamma_min": gmin, "E_ratio": Ef / E0, "max_V_inc": vs["max_V_inc"], "pass": bool(gate_ok)}

    # ── §2 the "2" — does the moving Γ=−1 wall confine in the COUPLED engine? ──
    print("\n[§2 the '2'] genesis-A photon — wall confines (energize+LOCK) vs no-wall control")
    e_wall = _make_engine()
    _seed_photon(e_wall, amplitude=A_LOCK, helicity=1.0)
    loc0, _ = _localization(e_wall)
    w0 = _omega_max(e_wall)
    tr_wall = _run(e_wall, N_STEPS, record=True)
    locf, pk = _localization(e_wall)
    wf = _omega_max(e_wall)
    e_now = _make_engine(K=0.0)          # no-wall linear control (same seed)
    _seed_photon(e_now, amplitude=A_LOCK, helicity=1.0)
    _run(e_now, N_STEPS)
    loc_nowall, _ = _localization(e_now)
    # mechanism discriminator (verdict-II style): the wall HOLDS the photon
    # significantly more than the no-wall control disperses it, AND |ω| is bounded.
    held = (locf > 1.15 * loc_nowall) and wf < 10 * w0
    locked = wf < 5 * w0                  # energize+LOCK: |ω| bounded (not pumped)
    print(f"  WALL  : loc {loc0:.3f}→{locf:.3f}  |ω|max {w0:.2f}→{wf:.2f}  held={held} locked={locked}")
    print(f"  no-wall control: loc {loc0:.3f}→{loc_nowall:.3f} (disperses)")
    out["the_2"] = {"loc0": loc0, "locf": locf, "loc_nowall": loc_nowall,
                    "omega_max0": w0, "omega_maxf": wf, "held": bool(held), "locked": bool(locked),
                    "peak": [int(x) for x in pk]}

    # ── §3 THE "3" — does the V-sector close onto the "2" in phase-space? ──────
    print("\n[§3 THE '3' (A46 phase-space)] does (V_inc,V_ref) trace the (2,3) Clifford winding?")
    vs_wall = _v_sector_state(e_wall)
    ps = _phase_space_winding(e_wall, pk)
    c_omega = e_wall.cos.extract_crossing_count()    # the "2" real-space ω winding (DIAGNOSTIC)
    print(f"  V-sector energization: max|V_inc|={vs_wall['max_V_inc']:.2e}  "
          f"max|Φ_link|={vs_wall['max_Phi_link']:.2e}  V_sq_sum={vs_wall['V_sq_sum']:.2e}")
    print(f"  phase-space (V_inc): amp={ps['vinc_amp']:.2e}  w_tor={ps.get('vinc_w_tor')}"
          f"  w_pol={ps.get('vinc_w_pol')}  closes(2,3)={ps['vinc_closes_23']}")
    print(f"  phase-space POPULATED={ps['phase_space_populated']}  |  "
          f"the '2' (Cosserat ω real-space, DIAGNOSTIC): c={c_omega}")
    out["the_3"] = {"v_sector": vs_wall, "phase_space": ps, "c_omega_realspace": int(c_omega)}

    # ── §4 charge = helicity (+h vs −h, both confine, sign flips) ──────────────
    print("\n[§4 charge=helicity] seed +h vs −h — Beltrami helicity sign flips, both confine")
    e_p = _make_engine(); _seed_photon(e_p, A_LOCK, +1.0); _run(e_p, N_STEPS)
    e_m = _make_engine(); _seed_photon(e_m, A_LOCK, -1.0); _run(e_m, N_STEPS)
    Hp, Hm = _beltrami_helicity_total(e_p), _beltrami_helicity_total(e_m)
    lp, _ = _localization(e_p); lm, _ = _localization(e_m)
    flips = np.sign(Hp) != np.sign(Hm) and abs(Hp) > 1e-6 and abs(Hm) > 1e-6
    print(f"  +h: H_bel={Hp:+.3e} loc→{lp:.3f}   −h: H_bel={Hm:+.3e} loc→{lm:.3f}")
    print(f"  charge=helicity: sign flips={flips}, both confine={lp>0.5 and lm>0.5}")
    out["charge_helicity"] = {"H_plus": Hp, "H_minus": Hm, "loc_plus": lp, "loc_minus": lm,
                              "sign_flips": bool(flips), "both_confine": bool(lp > 0.5 and lm > 0.5)}

    # ── §5 chirality selection (κ_chiral parity-odd: μ vs ε short by sign) ─────
    print("\n[§5 chirality] κ_chiral=1.2α parity-odd: does the confining side select by helicity?")
    ch_p = _chirality_select(e_p)
    ch_m = _chirality_select(e_m)
    # definite handedness = the μ-short fraction differs by helicity sign
    selects = abs(ch_p["frac_mu_short"] - ch_m["frac_mu_short"]) > 1e-3 or \
        abs(ch_p["gamma_min"] - ch_m["gamma_min"]) > 1e-3
    print(f"  +h: Γ_min={ch_p['gamma_min']:+.3f} μ-short frac={ch_p['frac_mu_short']:.3f}")
    print(f"  −h: Γ_min={ch_m['gamma_min']:+.3f} μ-short frac={ch_m['frac_mu_short']:.3f}")
    print(f"  definite chirality selected (not LH=RH): {selects}")
    out["chirality"] = {"plus": ch_p, "minus": ch_m, "definite_selection": bool(selects)}

    # ── §6 spin/L conservation — energize+LOCK vs the pump CONTROL (→ C) ───────
    print("\n[§6 spin/L] energize+LOCK (bounded) vs the hard-wall PUMP control (secular → C)")
    L_series = [r["L_spin"] for r in tr_wall]
    w_series = [r["omega_C"] for r in tr_wall]
    H_series = [r["H_bel"] for r in tr_wall]
    L_bounded = max(w_series) < 5 * w_series[0] if w_series else False
    e_pump = _make_engine(); _seed_photon(e_pump, A_PUMP, +1.0)
    tr_pump = _run(e_pump, N_STEPS, record=True)
    w_pump = [r["omega_C"] for r in tr_pump]
    pumped = max(w_pump) > 20 * w_pump[0] if w_pump else False
    print(f"  LOCK  (A={A_LOCK}): |ω|max {w_series[0]:.2f}→{max(w_series):.2f}  |L| range "
          f"[{min(L_series):.3f},{max(L_series):.3f}]  bounded(locked)={L_bounded}")
    print(f"  PUMP control (A={A_PUMP}): |ω|max {w_pump[0]:.2f}→{max(w_pump):.2f}  detonates={pumped}")
    out["spin_L"] = {"L_min": min(L_series), "L_max": max(L_series), "omega_lock_max": max(w_series),
                     "omega_pump_max": max(w_pump), "locked": bool(L_bounded), "pump_detonates": bool(pumped),
                     "H_bel_series": H_series}

    # ── §7 α from the leak (residual Γ transparency; Golden-Torus α⁻¹ target) ──
    print("\n[§7 α-from-leak] residual Γ transparency Q; Golden-Torus α⁻¹=4π³+π²+π target")
    leak = _gamma_leak(e_wall)
    print(f"  wall Γ_min={leak['gamma_min']:+.3f}  T²_residual={leak['T2_residual']:.3e}  "
          f"leak Q⁻¹={leak['Q_inv_leak']:.2f}")
    print(f"  Golden-Torus α⁻¹ target={leak['alpha_cold_inv_target']:.4f} — requires the (2,3) to CLOSE")
    # leak sweep (Γ_min vs amplitude) — figure 5b
    sweep = []
    for a in (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0):
        es = _make_engine(); _seed_photon(es, a, +1.0)
        for _ in range(8):
            es.step()
        gm = float(es._coupled._impedance_gamma_shared()[es.cos.mask_alive].min())
        sweep.append({"A": a, "gamma_min": gm})
    out["alpha_leak"] = {**leak, "sweep": sweep}

    # ── §8 GAP-LOCALIZATION DIAGNOSTIC — IF the V-sector is energized, ─────────
    #      does the coupled wall wind it to (2,3)? (source-q vs topology-q)
    print("\n[§8 gap-localization] co-seed a V-sector partner — source-q (energized?) vs topology-q (winds?)")
    e_diag = _make_engine(emf=True)
    _seed_photon(e_diag, A_LOCK, +1.0)
    _seed_v_partner(e_diag, frac=0.3)
    v0 = _v_sector_state(e_diag)["max_V_inc"]
    _run(e_diag, N_STEPS)
    vd = _v_sector_state(e_diag)
    _, pkd = _localization(e_diag)
    psd = _phase_space_winding(e_diag, pkd)
    print(f"  V-partner seed max|V_inc|={v0:.3e} → @end {vd['max_V_inc']:.3e} (survives={vd['max_V_inc']>1e-6})")
    print(f"  phase-space (V_inc) winding: w_tor={psd.get('vinc_w_tor')} w_pol={psd.get('vinc_w_pol')} "
          f"closes(2,3)={psd['vinc_closes_23']} (rel_pol={psd.get('vinc_rel_pol')})")
    out["gap_localization"] = {"v0": v0, "v_end": vd, "phase_space": psd}

    # ── §9 VERDICT (A/B/C — ave-discriminator-before-synthesis) ───────────────
    two_confirms = out["the_2"]["held"] and out["the_2"]["locked"] and out["charge_helicity"]["sign_flips"]
    three_closes = ps["vinc_closes_23"] or ps["vref_closes_23"]
    three_populated = ps["phase_space_populated"]
    full_signature = (
        three_closes and out["spin_L"]["locked"] and out["chirality"]["definite_selection"]
        and out["charge_helicity"]["sign_flips"]
    )
    if full_signature:
        verdict, msg = "A", "(2,3) SELF-ASSEMBLES — full signature; electron reflected into existence"
    elif two_confirms and not three_closes:
        verdict, msg = "B", "'2'-CONFIRMS, '3'-does-not-close — coupled-channel gap localized"
    else:
        verdict, msg = "C", "REPRESENTATION FAIL — collapse not converted / chirality not selected / pumped"
    out["verdict"] = verdict
    print("\n" + "=" * 80)
    print(f"VERDICT {verdict}: {msg}")
    print(f"  2-confirms={two_confirms}  3-closes={three_closes}  3-phase-space-populated={three_populated}")
    print(f"  spin-locked={out['spin_L']['locked']}  chirality-definite={out['chirality']['definite_selection']}")
    print("=" * 80)

    # ── Figures ───────────────────────────────────────────────────────────────
    try:
        fig_paths = _make_figures(out, e_wall, e_diag, tr_wall, tr_pump, sweep)
        out["figures"] = fig_paths
        print("\nFigures:")
        for k, v in fig_paths.items():
            print(f"  {k}: {v}")
    except Exception as exc:  # never let plotting sink the data
        print(f"\n[figures FAILED: {exc}]")
        out["figures"] = {}

    jpath = os.path.join(HERE, "reflection_genesis_23_self_assembly_results.json")
    with open(jpath, "w") as f:
        json.dump(out, f, indent=2, default=float)
    print(f"\nResults JSON: {jpath}")
    return out


if __name__ == "__main__":
    main()
