"""
Motion-stability via back-EMF — the LONGITUDINAL (decisive) channel.

Grant's hypothesis (stability FROM motion): a moving self-trap's back-EMF /
dark-wake reaction STABILIZES it — retention(v) slope > 0, stability gain tracking
the native longitudinal τ_zx (positive), MORE than a linear (SM-counterfactual)
control at matched amplitude/saturation.

WHY LONGITUDINAL IS DECISIVE (the prior runs were on the WRONG channel):
  Both transverse runs (Maxwell 059ae318 NULL-lean-CONTRADICTS; native-Cosserat
  c6613c26 CONTRADICTS-via-PIN) boosted the V-SECTOR winding phasor (ox,oy)=
  (V0+V1, V2+V3). But:
    1. The electron moves LONGITUDINALLY, not transversally —
       de-broglie-standing-wave.md:50: "its motion displaces the lattice,
       generating longitudinal acoustic pressure waves governed by the vacuum's
       Bulk Modulus."
    2. The dark-wake τ_zx IS a longitudinal shear strain (the bemf) —
       vacuum_engine.py:46, dark-wake-bemf-foc-synthesis.md §3.
  ∴ drive in the channel the electron moves (longitudinal displacement u) + read
  the channel the bemf lives in (native longitudinal τ_zx). THIS is the coherent
  adjudication.

THE ONLY CHANGE vs the validated Cosserat run (c6613c26): swap the transverse
phasor boost on V_inc for a LONGITUDINAL displacement-field (u) drive on the
bulk-modulus compression channel. Everything else (durable Arm-C host, native
DarkWakeObserver, LINEAR/BASELINE arms, adjudicator) is reused.

THE LONGITUDINAL DRIVE (substrate map):
  The displacement DOF is the Cosserat u field (cosserat_field_3d.py:817), velocity
  u_dot, velocity-Verlet integrated. The bulk/longitudinal channel runs at
  c_L = √((2G + 4G/3)/ρ) = √(10/3) ≈ 1.826 (cosserat_field_3d.py:1500) — separate
  from and faster than the transverse c_T = √(G/ρ) = 1, and NOT frozen by the
  V-sector saturation S (c_L depends on G/ρ, not S). The drive imparts NET +x
  longitudinal momentum by writing a +x displacement-velocity blob onto
  u_dot[...,0] (Variant A) localized on the host: the lattice moves +x (net
  momentum) with an x-varying envelope ⇒ ∂_x u_x ≠ 0 ⇒ div u ≠ 0 ⇒ bulk
  compression excited. ONE-SHOT momentum imprint (a sustained pump injects energy —
  rejected, same as the Cosserat run).

COUPLING (honest, load-bearing): with disable_cosserat_lc_force=True (validated
  config), the K4→Cosserat FORCE channel is OFF. The path is u-strain → ε_sym →
  A²_ε → S_ε → z_local = √(S_μ/S_ε) (k4_cosserat_coupling.py:393), which both
  modulates the K4 scatter (asymmetric impedance) AND is the prefactor of
  τ_zx = z_local·∂_x A². A longitudinal u-momentum biases the saturation-impedance
  field along +x; if the knot tracks that bias it translates (and the native τ_zx
  carries it). If it does NOT (z_local bias too weak to move a c_eff→0 frozen core)
  → a clean PIN-EVEN-LONGITUDINAL finding (a tension with de-broglie:50).

ANTI-STALL (hard 2-try cap): validate the drive on a sub-saturation LINEAR
  displacement pulse FIRST. Moves (v>0, sign-symmetric) → proceed. Does NOT move
  after 2 drive variants → BLOCKED-drive, return.

FORWARD-PREDICTED SIGN (pre-run, no fit — ave-driver-script-honesty):
  substrate-default = PIN-EVEN-LONGITUDINAL. The LINEAR pulse advects (~c_L); the
  SELF-TRAP knot's frozen V-core does NOT track the z_local bias enough to
  translate; retention(v) flat-or-falling; native-τ_zx-vs-stability corr ≤ 0.
  A SUPPORTS overturns the static-trap canon → FULL ave-discrimination-check.

Brief / prereg: _orchestration/motion-stability-bemf-longitudinal.md
Result:        research/2026-06-04_motion-stability-bemf-longitudinal-result.md
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.core.constants import ALPHA  # noqa: E402
from ave.topological.vacuum_engine import (  # noqa: E402
    DarkWakeObserver,
    VacuumEngine3D,
)
from tlm_electron_soliton_eigenmode import (  # noqa: E402
    initialize_2_3_voltage_ansatz,
)

# ── Substrate-derived constants (ave-canonical-source: NO hardcoded literals) ──
A2_OP14 = float(np.sqrt(2.0 * ALPHA))   # √(2α) ≈ 0.1208 — Op14 engagement (self-trap bar)
PHI = (1.0 + np.sqrt(5.0)) / 2.0
DT = 1.0 / np.sqrt(2.0)                  # K4-TLM 4-port junction outer timestep
C_LONG = float(np.sqrt(10.0 / 3.0))     # bulk-modulus longitudinal sound speed (K=2G, ρ=G=1)

# Host (Arm-C) geometry — the confirmed durable host (retention ~0.88–0.91, peak A²≈8.9)
HOST_R_FRAC = 0.22                       # R_shell = 0.22·N
HOST_AMP = 0.40                          # peak A²_interior ≈ 8.9 during evolution

# FORWARD-PREDICTED SIGN (no fit). Substrate default: frozen V-core pins even
# longitudinally (the longitudinal channel moves the LINEAR pulse but not the knot).
FORWARD_PREDICTED_VERDICT = "PIN-even-longitudinal"
FORWARD_PREDICTED_SIGN = {
    "linear_moves": True,
    "knot_moves": False,
    "retention_slope_sign": "<= 0 (flat or falling)",
    "tau_zx_vs_stability_corr_sign": "<= 0",
}


# ══════════════════════════════════════════════════════════════════════════════
# Engine + host (confirmed config — reused verbatim from the Cosserat run c6613c26)
# ══════════════════════════════════════════════════════════════════════════════
def setup_engine(N, PML):
    """A28-corrected coupled VacuumEngine3D (doc 67 §15 + r10_v8 config).
    disable_cosserat_lc_force=True ⇒ K4→Cos FORCE off; coupling is via z_local
    (the saturation-impedance channel τ_zx reads)."""
    return VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )


def seed_host(engine, N, amplitude=HOST_AMP):
    """Plant the durable (2,3) host (Arm-C config): the confirmed self-trap that
    holds retention ~0.88–0.91 at peak A²≈8.9. R = 0.22·N, r = R/φ². Populates
    V_inc only; the Cosserat u field starts at zero (the drive lives there)."""
    R = HOST_R_FRAC * N
    r = R / (PHI**2)
    initialize_2_3_voltage_ansatz(engine.k4, R=R, r=r, amplitude=amplitude)
    return R, r


def _interior_mask(N, PML):
    m = np.zeros((N, N, N), dtype=bool)
    m[PML : N - PML, PML : N - PML, PML : N - PML] = True
    return m


# ══════════════════════════════════════════════════════════════════════════════
# THE LONGITUDINAL DRIVE — CURL-FREE compression on the Cosserat u field (A₁/bulk)
# ══════════════════════════════════════════════════════════════════════════════
# DRIVE CORRECTION (2026-06-04): the prior drive (radial-Gaussian u_dot[...,0]) was
# a longitudinal/SHEAR MIX (curl/div = 1.414 — verified) — the exact mislabel the
# transverse-vs-longitudinal audit warned about. A clean longitudinal (compression)
# field is CURL-FREE: u = ∇φ ⇒ curl u ≡ 0 (continuum) and div u = ∇²φ ≠ 0. On the
# K4 tetrahedral operator the discrete curl(grad φ) = 0 to machine epsilon (5e-18,
# verified) — the operators commute, so the gate cannot false-fail from operator
# non-commutation. See _orchestration/...-DRIVE-CORRECTION.md.
#
# REFRAMING (per DRIVE-CORRECTION lines 67-70): a localized curl-free field carries
# ZERO net linear momentum by ∮ — EXPECTED and fine. The drive is a DIRECTIONAL +x
# COMPRESSION BIAS (compression ahead, rarefaction behind), NOT a momentum blob. The
# motion test is whether that bias DRAGS THE KNOT CENTROID via the z_local
# saturation-impedance gradient — not whether momentum is injected.


def _dipole_potential(N, PML, sigma_frac=0.18):
    """Variant-A scalar potential φ(x,y,z) = (x − c_x)·exp(−r²/2σ²): a +x/−x-
    asymmetric COMPRESSION dipole (the moving-electron longitudinal wake of
    de-broglie:50). Returns (phi, cx). The drive is u = v_drive·∇φ (curl-free)."""
    cx = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N), dtype=float)
    r2 = (i - cx) ** 2 + (j - cx) ** 2 + (k - cx) ** 2
    sigma = max(3.0, sigma_frac * N)
    phi = (i - cx) * np.exp(-r2 / (2.0 * sigma**2))
    return phi, cx


def _grad_of(phi, dx):
    """∇φ via the SAME tetrahedral_gradient stencil the engine uses for ε, κ. Using
    this exact operator (not an analytic ∇φ) is what makes the discrete curl of the
    drive vanish to machine epsilon → the gate is honest about THIS operator."""
    from ave.topological.cosserat_field_3d import tetrahedral_gradient
    return np.asarray(tetrahedral_gradient(phi)) / dx          # (N,N,N,3)


def _planar_x_pulse(N, PML, k_x=0.5, sigma_frac=0.18):
    """Variant-B anti-stall field: u_x = w(x)·sin(k_x·(x−c_x)), uniform across y,z
    ⇒ ∂_y u_x = ∂_z u_x = 0 ⇒ curl u ≡ 0 EXACTLY, div u = ∂_x u_x ≠ 0. A one-sided
    x-planar longitudinal pulse (CAN carry net +x momentum, at the cost of being a
    transverse slab). Used ONLY if Variant A fails the LINEAR smoke test."""
    cx = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N), dtype=float)
    sigma = max(3.0, sigma_frac * N)
    wx = np.exp(-((i - cx) ** 2) / (2.0 * sigma**2))
    u = np.zeros((N, N, N, 3), dtype=float)
    u[..., 0] = wx * np.sin(k_x * (i - cx))
    return u, cx


def apply_longitudinal_drive(engine, v_drive, N, PML, variant="A", form="velocity"):
    """CURL-FREE +x longitudinal-compression drive on the Cosserat u field (the
    A₁/bulk channel de-broglie:50 says the electron moves in). ONE-SHOT imprint.

    Variant A (PRIMARY — compression dipole / co-moving wake): u = v_drive·∇φ,
      φ = (x−c_x)·exp(−r²/2σ²). Curl-free by construction (discrete curl ≈ 5e-18).
      Directional +x compression (compression ahead, rarefaction behind); zero net
      linear momentum (expected — see header). v_drive=0 → identity.
    Variant B (ANTI-STALL fallback — x-planar pulse): u_x = w(x)·sin(k_x x), uniform
      in y,z. curl ≡ 0 exactly; CAN carry net +x momentum.

    form='velocity' → imprint on u_dot (kinetic kick); 'displacement' → on u
      (compression step). Default velocity (matches the C-state/L-state pair: the
      drive enters as an L-state u_dot kick that the bulk modulus converts to a
      traveling compression). On alive sites only.
    """
    if v_drive == 0.0:
        return
    dx = engine.cos.dx
    if variant == "A":
        phi, _ = _dipole_potential(N, PML)
        field = v_drive * _grad_of(phi, dx)              # u = v·∇φ, curl-free
    elif variant == "B":
        u_pulse, _ = _planar_x_pulse(N, PML)
        field = v_drive * u_pulse
    else:
        raise ValueError(f"unknown drive variant {variant!r}")
    field[~engine.cos.mask_alive] = 0.0
    if form == "velocity":
        engine.cos.u_dot[...] = engine.cos.u_dot + field
    elif form == "displacement":
        engine.cos.u[...] = engine.cos.u + field
    else:
        raise ValueError(f"unknown drive form {form!r}")
    engine.cos.u_dot[~engine.cos.mask_alive] = 0.0
    engine.cos.u[~engine.cos.mask_alive] = 0.0


def apply_baseline_longitudinal_drive(engine, v_drive, N, PML, variant="A", form="velocity"):
    """BASELINE(v) — matched-energy STANDING compression with NET-ZERO directional
    bias (ave-discrimination-check matched control). Same bulk-channel energy + same
    |drive| spectral content + same curl-free purity as SELF-TRAP(v), but with NO
    directional +x bias: use the EVEN compression potential φ_even = G(r) (a radial
    breathing compression), so ∇φ_even points radially inward/outward symmetrically
    — Σ_x(drive·x̂) = 0, no +x translation bias. (For Variant B: an even standing
    wave cos(k_x x) instead of the one-sided sin.) NOT a phase-scramble (energy +
    saturation matched). The genuinely-matched 'directional-bias vs standing-
    compression' decider: isolates whether the +x DIRECTIONALITY (not the bulk
    excitation per se) is what retains the knot."""
    if v_drive == 0.0:
        return
    dx = engine.cos.dx
    cx = (N - 1) / 2.0
    if variant == "A":
        # even (radial breathing) potential: φ_even = exp(-r²/2σ²) ⇒ ∇φ_even radial,
        # zero net +x first moment ⇒ standing compression, no directional bias.
        i, j, k = np.indices((N, N, N), dtype=float)
        r2 = (i - cx) ** 2 + (j - cx) ** 2 + (k - cx) ** 2
        sigma = max(3.0, 0.18 * N)
        phi_even = np.exp(-r2 / (2.0 * sigma**2))
        field = v_drive * _grad_of(phi_even, dx)
    elif variant == "B":
        i, j, k = np.indices((N, N, N), dtype=float)
        sigma = max(3.0, 0.18 * N)
        wx = np.exp(-((i - cx) ** 2) / (2.0 * sigma**2))
        u = np.zeros((N, N, N, 3), dtype=float)
        u[..., 0] = wx * np.cos(0.5 * (i - cx))          # even standing wave
        field = v_drive * u
    else:
        raise ValueError(f"unknown drive variant {variant!r}")
    field[~engine.cos.mask_alive] = 0.0
    if form == "velocity":
        engine.cos.u_dot[...] = engine.cos.u_dot + field
    elif form == "displacement":
        engine.cos.u[...] = engine.cos.u + field
    else:
        raise ValueError(f"unknown drive form {form!r}")
    engine.cos.u_dot[~engine.cos.mask_alive] = 0.0
    engine.cos.u[~engine.cos.mask_alive] = 0.0


# ══════════════════════════════════════════════════════════════════════════════
# LINEAR (sub-saturation) displacement pulse — the SM-counterfactual + drive smoke
# ══════════════════════════════════════════════════════════════════════════════
def seed_linear_pulse(engine, N, PML, peak_A2_target=0.5 * A2_OP14):
    """A sub-saturation Cosserat DISPLACEMENT blob (below A²_op14 ⇒ no self-trap),
    localized at center, so the longitudinal drive imprints a CLEAN +x momentum
    that advects at c_L — the SM-counterfactual + the drive smoke test. Seeds a
    small static +x displacement gradient (a compression) whose symmetric strain
    ε_sym sets A²_ε below the Op14 bar; the drive then adds the +x momentum. (The
    V-sector is left at vacuum so there is no competing knot — pure
    longitudinal-transport control.)"""
    env, cx = _host_envelope(engine, N, PML, sigma_frac=0.12)
    # seed a tiny +x displacement bump so there is a localized compressible blob
    engine.cos.u[..., 0] = env
    engine.cos.u[~engine.cos.mask_alive] = 0.0
    # scale displacement so peak electric-sector strain A²_ε ≈ target (sub-saturation)
    A2e = _cos_electric_A2(engine)
    m = _interior_mask(N, PML) & engine.cos.mask_alive
    cur = float(A2e[m].max()) if m.any() else 0.0
    if cur > 0:
        scale = np.sqrt(peak_A2_target / cur)
        engine.cos.u[..., 0] *= scale
    return float(env[m].sum())


# ══════════════════════════════════════════════════════════════════════════════
# Observables
# ══════════════════════════════════════════════════════════════════════════════
def a2_field(engine):
    """V-sector A² (the knot's electric energy density)."""
    return np.sum(engine.k4.V_inc**2, axis=-1) / engine.V_SNAP**2


def _cos_electric_A2(engine):
    """Cosserat electric-sector strain amplitude A²_ε = ε_sym²/ε_yield² (the
    longitudinal-strain witness; the part of A²_ε that the u-drive sets). Same
    symmetric-strain operator the saturation kernel uses (_compute_strain →
    symmetric part)."""
    from ave.topological.cosserat_field_3d import _compute_strain
    import jax.numpy as jnp
    eps = np.asarray(_compute_strain(jnp.asarray(engine.cos.u),
                                     jnp.asarray(engine.cos.omega), engine.cos.dx))
    eps_sym = 0.5 * (eps + np.swapaxes(eps, -1, -2))
    eps_sym_sq = np.sum(eps_sym * eps_sym, axis=(-1, -2))
    return eps_sym_sq / (engine.cos.epsilon_yield ** 2)


def x_centroid_vsector(engine, PML):
    """Energy-weighted x-centroid of the V-SECTOR knot (A² weighting). The motion
    observable for the SELF-TRAP arm — does the KNOT translate? Returns
    (centroid_x, total_interior_energy)."""
    N = engine.N
    A2 = a2_field(engine)
    m = _interior_mask(N, PML) & engine.k4.mask_active
    w = np.where(m, A2, 0.0)
    tot = float(w.sum())
    if tot <= 0:
        return float("nan"), 0.0
    xi = np.arange(N, dtype=float)[:, None, None]
    return float((w * xi).sum() / tot), tot


def x_centroid_cos(engine, PML):
    """Energy-weighted x-centroid of the COSSERAT displacement field (|u|²
    weighting). The motion observable for the LINEAR arm (pure longitudinal
    transport) — does the displacement blob advect? Returns (centroid_x, total)."""
    N = engine.N
    U2 = np.sum(engine.cos.u**2, axis=-1)
    m = _interior_mask(N, PML) & engine.cos.mask_alive
    w = np.where(m, U2, 0.0)
    tot = float(w.sum())
    if tot <= 0:
        return float("nan"), 0.0
    xi = np.arange(N, dtype=float)[:, None, None]
    return float((w * xi).sum() / tot), tot


def x_fwhm_vsector(engine, PML):
    """FWHM of the V-sector A² profile projected onto x (knot localization width)."""
    N = engine.N
    A2 = a2_field(engine)
    m = _interior_mask(N, PML) & engine.k4.mask_active
    prof = np.where(m, A2, 0.0).sum(axis=(1, 2))
    if prof.max() <= 0:
        return float("nan")
    half = 0.5 * prof.max()
    idx = np.where(prof >= half)[0]
    if len(idx) < 2:
        return float(DT)
    return float(idx[-1] - idx[0] + 1)


def _per_component_grads(field, dx):
    """g[c][...,j] = ∂_j (field_c) via the SAME tetrahedral_gradient stencil used
    for ε, κ and for the drive. Shared source of div AND curl so the gate is
    self-consistent with the operator the drive was built on."""
    from ave.topological.cosserat_field_3d import tetrahedral_gradient
    return [np.asarray(tetrahedral_gradient(field[..., c])) / dx for c in range(3)]


def cos_div_rms(engine, PML, field=None):
    """RMS |div u| over the interior — the bulk/compression (A₁) witness. div u =
    Σ_c ∂_c u_c via the tetrahedral operator. Nonzero ⇒ longitudinal/bulk mode is
    live. field=None reads engine.cos.u; pass u_dot to witness a velocity drive."""
    if field is None:
        field = np.asarray(engine.cos.u)
    g = _per_component_grads(field, engine.cos.dx)
    div = g[0][..., 0] + g[1][..., 1] + g[2][..., 2]
    m = _interior_mask(engine.N, PML) & engine.cos.mask_alive
    vals = div[m]
    return float(np.sqrt(np.mean(vals**2))) if vals.size else 0.0


def cos_curl_rms(engine, PML, field=None):
    """RMS |curl u| over the interior — the SHEAR (T₂) witness the killed probe
    LACKED. curl u = (∂_y u_z−∂_z u_y, ∂_z u_x−∂_x u_z, ∂_x u_y−∂_y u_x), built from
    the SAME per-component tetrahedral gradients as div u. A clean longitudinal
    (compression) drive has curl ≈ 0; a longitudinal/shear MIX has curl ~ div. The
    gate curl/div < 0.10 = "≥90% compression". field=None reads engine.cos.u."""
    if field is None:
        field = np.asarray(engine.cos.u)
    g = _per_component_grads(field, engine.cos.dx)
    curl = np.stack([
        g[2][..., 1] - g[1][..., 2],     # ∂_y u_z − ∂_z u_y
        g[0][..., 2] - g[2][..., 0],     # ∂_z u_x − ∂_x u_z
        g[1][..., 0] - g[0][..., 1],     # ∂_x u_y − ∂_y u_x
    ], axis=-1)
    cmag = np.sqrt(np.sum(curl * curl, axis=-1))
    m = _interior_mask(engine.N, PML) & engine.cos.mask_alive
    vals = cmag[m]
    return float(np.sqrt(np.mean(vals**2))) if vals.size else 0.0


# Drive-purity gate threshold: curl_rms/div_rms < CURL_DIV_GATE ⇒ "≥90% compression".
CURL_DIV_GATE = 0.10


def drive_purity(engine, PML, field=None):
    """(div_rms, curl_rms, ratio) of the drive field. ratio < CURL_DIV_GATE is the
    MANDATORY GATE before accepting any drive (the fix the killed run lacked)."""
    d = cos_div_rms(engine, PML, field=field)
    c = cos_curl_rms(engine, PML, field=field)
    ratio = c / max(d, 1e-30)
    return d, c, ratio


def cos_kinetic_energy(engine, PML):
    """Cosserat translational kinetic energy K_u = Σ ½|u_dot|² over the interior —
    the longitudinal-channel excitation witness (is the bulk mode actually live?)."""
    u_dot = np.asarray(engine.cos.u_dot)
    m = _interior_mask(engine.N, PML) & engine.cos.mask_alive
    return float(0.5 * np.sum((u_dot**2)[m]))
