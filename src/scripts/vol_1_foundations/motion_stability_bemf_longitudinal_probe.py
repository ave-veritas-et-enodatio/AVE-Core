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
    a localized COMPRESSIBLE +x bump at center. The SAME curl-free longitudinal
    drive then biases it: the SM-counterfactual + the drive smoke test. A directional
    compression bias (zero net momentum) drags this blob's compression pattern +x
    (and as the bulk modulus acts, the energy centroid follows at ~c_L). The V-sector
    is left at vacuum (no competing knot) — pure longitudinal-transport control."""
    cx = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N), dtype=float)
    r2 = (i - cx) ** 2 + (j - cx) ** 2 + (k - cx) ** 2
    sigma = max(3.0, 0.12 * N)
    env = np.exp(-r2 / (2.0 * sigma**2))
    env[~engine.cos.mask_alive] = 0.0
    engine.cos.u[..., 0] = env                       # +x displacement bump (compressible blob)
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


# ══════════════════════════════════════════════════════════════════════════════
# ANTI-STALL smoke test (hard 2-try cap) + the MANDATORY curl/div gate
# ══════════════════════════════════════════════════════════════════════════════
def _imprint_and_gate(engine, drive_fn, v_drive, N, PML, variant, form):
    """Apply a drive, isolate the imprinted field (delta vs pre-drive), and gate its
    curl/div purity. Returns (drive_field_delta, div_rms, curl_rms, ratio)."""
    base = np.array(engine.cos.u_dot if form == "velocity" else engine.cos.u)
    drive_fn(engine, v_drive, N, PML, variant=variant, form=form)
    now = np.array(engine.cos.u_dot if form == "velocity" else engine.cos.u)
    delta = now - base
    d, c, ratio = drive_purity(engine, PML, field=delta)
    return delta, d, c, ratio


def smoke_test_drive(N=40, PML=4, n_steps=60, v_list=(0.0, 0.3, -0.3),
                     form="displacement"):
    """ANTI-STALL smoke + GATE. For each candidate variant (A then B, hard 2-try
    cap): (1) gate the drive purity (curl/div < CURL_DIV_GATE) on the imprinted
    field; (2) seed a sub-saturation LINEAR pulse, apply the drive, confirm the
    |u|²-centroid ADVECTS (v≠0, sign-symmetric, v≈0 at v_drive=0).

    Returns the FIRST variant that passes BOTH gate + advection, plus the full
    per-variant record. If neither passes → variant=None (caller returns
    BLOCKED-drive)."""
    out = {"variants": {}, "gate_threshold": CURL_DIV_GATE, "chosen_variant": None,
           "chosen_form": form}
    for variant in ("A", "B"):
        rec = {"per_v": [], "gate_ratio_at_vmax": None, "gate_passed": None,
               "advects": None, "v0_is_zero": None, "signflips": None}
        # gate on the largest |v| (worst case for purity)
        v_gate = max(v_list, key=abs)
        eng_g = setup_engine(N, PML)
        seed_host(eng_g, N)
        for _ in range(5):
            eng_g.step()
        _, dg, cg, ratio_g = _imprint_and_gate(eng_g, apply_longitudinal_drive,
                                               v_gate, N, PML, variant, form)
        rec["gate_ratio_at_vmax"] = ratio_g
        rec["gate_div_rms"] = dg
        rec["gate_curl_rms"] = cg
        rec["gate_passed"] = bool(ratio_g < CURL_DIV_GATE)
        # LINEAR advection smoke
        for v_drive in v_list:
            eng = setup_engine(N, PML)
            seed_linear_pulse(eng, N, PML)
            apply_longitudinal_drive(eng, v_drive, N, PML, variant=variant, form=form)
            cx0, e0 = x_centroid_cos(eng, PML)
            traj = [(0.0, cx0)]
            for s in range(n_steps):
                eng.step()
                if (s + 1) % 5 == 0:
                    cx, e = x_centroid_cos(eng, PML)
                    traj.append(((s + 1) * DT, cx))
            ts = np.array([t for (t, c) in traj if not np.isnan(c)])
            cs = np.array([c for (t, c) in traj if not np.isnan(c)])
            v = float(np.polyfit(ts, cs, 1)[0]) if len(ts) >= 2 else float("nan")
            rec["per_v"].append({"v_drive": v_drive, "v_centroid": v,
                                 "dx": float(cs[-1] - cs[0]) if len(cs) >= 2 else float("nan")})
        vmax = [d for d in rec["per_v"] if abs(d["v_drive"]) == abs(v_gate) and d["v_drive"] > 0]
        v0 = [d for d in rec["per_v"] if d["v_drive"] == 0.0]
        vneg = [d for d in rec["per_v"] if abs(d["v_drive"]) == abs(v_gate) and d["v_drive"] < 0]
        v_at_max = vmax[0]["v_centroid"] if vmax else float("nan")
        v_at_0 = v0[0]["v_centroid"] if v0 else float("nan")
        v_at_neg = vneg[0]["v_centroid"] if vneg else float("nan")
        rec["advects"] = bool(abs(v_at_max) > 1e-3 and abs(v_at_max) > 5.0 * (abs(v_at_0) + 1e-6))
        rec["v0_is_zero"] = bool(abs(v_at_0) < 1e-3)
        rec["signflips"] = bool(np.sign(v_at_max) != np.sign(v_at_neg)) if vmax and vneg else None
        out["variants"][variant] = rec
        if rec["gate_passed"] and rec["advects"]:
            out["chosen_variant"] = variant
            break   # hard 2-try cap: take the first that clears both
    return out


# ══════════════════════════════════════════════════════════════════════════════
# Instrumented arm runner (the full decisive test)
# ══════════════════════════════════════════════════════════════════════════════
def run_arm(kind, v_drive, N, PML, variant, form, settle=10, n_steps=70, rec_every=5):
    """Run one (arm, v_drive) cell and record the FULL trajectory (CP6 reactance
    pair: both the C-state position-centroid AND the L-state A²(t)/K_u(t) at EVERY
    recorded step over the window — the Rule-10 reactance-tracking corollary).

    kind:
      'selftrap' — durable (2,3) host, CURL-FREE longitudinal-compression driven
                   (the object under test). x-centroid of the V-SECTOR knot.
      'linear'   — sub-saturation Cosserat displacement blob, same drive
                   (SM-counterfactual). x-centroid of the COSSERAT |u|² field.
      'baseline' — host + even standing-compression (matched energy, zero +x bias).

    Records per step: knot/blob x-centroid (→ velocity), interior energy
    (→ retention), FWHM, native max|τ_zx| (DarkWakeObserver, axis=0), peak interior
    A² (saturated-while-moving), Cosserat K_u (longitudinal-channel witness). Also
    records the post-drive curl/div purity of the imprinted field (per-arm gate
    audit trail)."""
    engine = setup_engine(N, PML)
    obs = DarkWakeObserver(cadence=1, propagation_axis=0)
    if kind == "linear":
        seed_linear_pulse(engine, N, PML)
        centroid = x_centroid_cos
    else:
        seed_host(engine, N)
        centroid = x_centroid_vsector
    engine.add_observer(obs)
    for _ in range(settle):
        engine.step()
    # apply the drive at t=0 of the recording window; capture imprinted-field purity
    drive_fn = apply_baseline_longitudinal_drive if kind == "baseline" else apply_longitudinal_drive
    base = np.array(engine.cos.u_dot if form == "velocity" else engine.cos.u)
    drive_fn(engine, v_drive, N, PML, variant=variant, form=form)
    now = np.array(engine.cos.u_dot if form == "velocity" else engine.cos.u)
    div_rms, curl_rms, curl_div = drive_purity(engine, PML, field=(now - base))

    m = _interior_mask(N, PML)
    traj = []   # (t, cx, E_int, fwhm, max_tau_zx, peakA2, K_u)
    cx0, e0 = centroid(engine, PML)
    d0 = obs._capture(engine)
    A2_0 = a2_field(engine)
    traj.append((0.0, cx0, e0, x_fwhm_vsector(engine, PML), d0["max_tau_zx"],
                 float(A2_0[m].max()), cos_kinetic_energy(engine, PML)))
    for s in range(n_steps):
        engine.step()
        if (s + 1) % rec_every == 0:
            cx, e = centroid(engine, PML)
            d = obs._capture(engine)
            A2 = a2_field(engine)
            traj.append(((s + 1) * DT, cx, e, x_fwhm_vsector(engine, PML),
                         d["max_tau_zx"], float(A2[m].max()),
                         cos_kinetic_energy(engine, PML)))
    arr = np.array(traj, dtype=float)
    ts, cxs, es, fwhms, taus, peakA2s, kus = arr.T
    good = ~np.isnan(cxs)
    v = float(np.polyfit(ts[good], cxs[good], 1)[0]) if good.sum() >= 2 else float("nan")
    retention = float(es[-1] / es[0]) if es[0] > 0 else float("nan")
    return {
        "kind": kind, "v_drive": v_drive, "variant": variant, "form": form,
        "v_centroid": v,
        "cx_start": float(cxs[0]), "cx_end": float(cxs[-1]),
        "dx_total": float(cxs[-1] - cxs[0]),
        "E_start": float(es[0]), "E_end": float(es[-1]), "retention": retention,
        "fwhm_start": float(fwhms[0]), "fwhm_end": float(fwhms[-1]),
        "max_tau_zx_mean": float(np.mean(taus)),
        "max_tau_zx_start": float(taus[0]), "max_tau_zx_end": float(taus[-1]),
        "peakA2_mean": float(np.mean(peakA2s)), "peakA2_min": float(np.min(peakA2s)),
        "peakA2_start": float(peakA2s[0]), "peakA2_end": float(peakA2s[-1]),
        "K_u_mean": float(np.mean(kus)), "K_u_start": float(kus[0]), "K_u_end": float(kus[-1]),
        # per-arm drive purity (the audit trail proving the drive was clean)
        "drive_div_rms": div_rms, "drive_curl_rms": curl_rms, "drive_curl_div": curl_div,
        "_traj": arr,
    }


# ══════════════════════════════════════════════════════════════════════════════
# Adjudicator — the verdict map + the FOUR adversarial controls
# ══════════════════════════════════════════════════════════════════════════════
LATTICE_VELOCITY_FLOOR = 1e-3   # |v| below this is lattice/centroid-jitter artifact


def adjudicate_motion_stability(sweep, V_SWEEP):
    """Verdict map (prereg + DRIVE-CORRECTION). A SUPPORTS requires the knot to
    translate (>floor) MORE than LINEAR, retention↑ with |v|, τ_zx-tracking, AND all
    FOUR adversarial controls cleared:
      (1) LINEAR does NOT advect the same (else generic transport, not bemf);
      (2) core A² HOLDS during motion (no decay → not a dying blob being pushed);
      (3) knot velocity > LATTICE_VELOCITY_FLOOR;
      (4) BASELINE matched-energy does NOT show the same retention gain.
    """
    V = sorted({r["v_drive"] for r in sweep["selftrap"].values()})
    v_max = max(V, key=abs)
    pos_v = [v for v in V if v > 0]
    v_pos = max(pos_v) if pos_v else v_max

    def get(arm, v):
        return sweep[arm][v]

    # --- knot vs linear vs baseline translation response (drive-induced, v=0 corrected)
    st_resp = abs(get("selftrap", v_pos)["v_centroid"] - get("selftrap", 0.0)["v_centroid"])
    lin_resp = abs(get("linear", v_pos)["v_centroid"] - get("linear", 0.0)["v_centroid"])
    base_resp = abs(get("baseline", v_pos)["v_centroid"] - get("baseline", 0.0)["v_centroid"])

    linear_advects = bool(lin_resp > LATTICE_VELOCITY_FLOOR)
    knot_moves = bool(st_resp > LATTICE_VELOCITY_FLOOR)

    # sign-flip pin tell on the self-trap: real translation flips sign with v_drive
    has_neg = (-abs(v_max)) in sweep["selftrap"]
    st_signflip = (bool(np.sign(get("selftrap", v_pos)["v_centroid"]) !=
                        np.sign(get("selftrap", -abs(v_max))["v_centroid"]))
                   if has_neg else None)

    # --- retention(|v|) slope on the SELF-TRAP arm (Grant: >0 if motion stabilizes)
    st_ret = [get("selftrap", v)["retention"] for v in V]
    st_vabs = [abs(get("selftrap", v)["v_centroid"]) for v in V]
    ret_slope = (float(np.polyfit(st_vabs, st_ret, 1)[0])
                 if len(V) >= 2 and np.ptp(st_vabs) > 1e-12 else float("nan"))

    # --- native-τ_zx-vs-retention correlation across the v-sweep (Grant: >0)
    tau = [get("selftrap", v)["max_tau_zx_mean"] for v in V]
    if len(V) >= 3 and np.std(tau) > 1e-30 and np.std(st_ret) > 1e-30:
        tau_ret_corr = float(np.corrcoef(tau, st_ret)[0, 1])
    else:
        tau_ret_corr = float("nan")

    # ── FOUR adversarial controls ───────────────────────────────────────────────
    # (1) LINEAR does NOT advect the same as the knot (knot response >> linear)
    ctrl1_linear_distinct = bool(knot_moves and st_resp > 2.0 * lin_resp)
    # (2) core A² HOLDS during motion at the driven cell (no decay → stable soliton,
    #     not a dying blob). peakA2_end/start ratio ≥ 0.8 AND peakA2 stays ≫ 1.
    sc = get("selftrap", v_pos)
    a2_hold = (sc["peakA2_end"] / sc["peakA2_start"]) if sc["peakA2_start"] > 0 else float("nan")
    ctrl2_a2_holds = bool(a2_hold >= 0.8 and sc["peakA2_min"] > 1.0)
    # (3) knot velocity exceeds the lattice-artifact floor
    ctrl3_above_floor = bool(abs(get("selftrap", v_pos)["v_centroid"]) > LATTICE_VELOCITY_FLOOR)
    # (4) BASELINE matched-energy does NOT show the same retention gain as SELF-TRAP
    st_ret_gain = get("selftrap", v_pos)["retention"] - get("selftrap", 0.0)["retention"]
    base_ret_gain = get("baseline", v_pos)["retention"] - get("baseline", 0.0)["retention"]
    ctrl4_baseline_distinct = bool(st_ret_gain > 0 and st_ret_gain > 2.0 * abs(base_ret_gain))
    all_four = bool(ctrl1_linear_distinct and ctrl2_a2_holds and ctrl3_above_floor and ctrl4_baseline_distinct)

    # PIN: linear advects, knot does NOT (response < ¼ linear, no sign-flip)
    knot_pinned = bool(linear_advects and st_resp < 0.25 * lin_resp)
    if has_neg and st_signflip is not None:
        knot_pinned = bool(knot_pinned and (st_signflip is False))

    # ── VERDICT ─────────────────────────────────────────────────────────────────
    if not linear_advects:
        verdict = "BLOCKED-drive"
        text = ("The LINEAR control does NOT advect under the (gated, curl-free) drive — "
                "the drive's directional-compression bias cannot move even a "
                "sub-saturation blob. (Should not occur if the smoke test selected a "
                "variant that advects; if it does, the curl-free directional drive is the "
                "blocker.)")
    elif knot_pinned:
        verdict = "PIN-even-longitudinal"
        text = ("LINEAR advects but the SELF-TRAP knot does NOT (response ≪ linear, "
                "no sign-flip with drive direction). The saturated (2,3) V-core "
                "(A²≫1 ⇒ S→0 ⇒ c_eff→0) does not track the z_local saturation-impedance "
                "bias enough to translate — even though the bulk/longitudinal channel is "
                "NOT frozen by S and the LINEAR compression advects at ~c_L. The knot is a "
                "frozen-clock soliton, PINNED even on the channel the electron physically "
                "moves in. Grant's stability-FROM-motion hypothesis is CONTRADICTED on the "
                "decisive longitudinal channel; flag-worthy tension with de-broglie:50.")
    elif knot_moves and all_four and ret_slope > 0 and tau_ret_corr > 0:
        verdict = "SUPPORTS-pending-discrimination-check"
        text = ("The SELF-TRAP knot TRANSLATES under the curl-free longitudinal drive MORE "
                "than LINEAR, retention RISES with |v|, the gain tracks native τ_zx (>0), "
                "AND all four adversarial controls cleared (LINEAR-distinct, A²-holds, "
                "above-floor, BASELINE-distinct). SUPPORTS Grant — but MANDATORY: complete "
                "the full ave-discrimination-check SM-counterfactual table BEFORE any "
                "positive framing. A positive overturns the static-trap canon (highest bar).")
    elif knot_moves:
        verdict = "CONTRADICTS"
        text = ("The SELF-TRAP knot responds to the drive but the bemf-stabilization "
                "signature FAILS: retention does not rise with |v| (slope≤0) and/or does "
                "not track native τ_zx (corr≤0) and/or an adversarial control fails "
                "(LINEAR matches / A² decays / BASELINE matches). Longitudinal motion here "
                "is generic transport, NOT bemf-stabilized topological translation.")
    else:
        verdict = "CONTRADICTS"
        text = ("Neither a clean translation nor a clean pin: the knot does not move above "
                "floor AND the LINEAR control's advection is marginal. No stability-from-"
                "motion signal on the longitudinal channel.")

    return {
        "verdict": verdict, "text": text,
        "linear_advects": linear_advects, "knot_moves": knot_moves, "knot_pinned": knot_pinned,
        "selftrap_response": st_resp, "linear_response": lin_resp, "baseline_response": base_resp,
        "selftrap_resp_over_linear": float(st_resp / lin_resp) if lin_resp > 0 else float("nan"),
        "selftrap_signflips_with_drive": st_signflip,
        "retention_v_slope_selftrap": ret_slope,
        "native_tau_zx_vs_retention_corr": tau_ret_corr,
        "adversarial_controls": {
            "1_linear_distinct": ctrl1_linear_distinct,
            "2_a2_holds": ctrl2_a2_holds, "a2_end_over_start": a2_hold,
            "3_above_lattice_floor": ctrl3_above_floor,
            "4_baseline_distinct": ctrl4_baseline_distinct,
            "selftrap_retention_gain": st_ret_gain, "baseline_retention_gain": base_ret_gain,
            "all_four_cleared": all_four,
        },
        "forward_predicted_verdict": FORWARD_PREDICTED_VERDICT,
        "forward_predicted_sign": FORWARD_PREDICTED_SIGN,
        "v_by_arm": {arm: {str(v): get(arm, v)["v_centroid"] for v in sorted(sweep[arm])} for arm in sweep},
        "retention_by_arm": {arm: {str(v): get(arm, v)["retention"] for v in sorted(sweep[arm])} for arm in sweep},
        "peakA2_traj_selftrap": {str(v): [get("selftrap", v)["peakA2_start"],
                                          get("selftrap", v)["peakA2_min"],
                                          get("selftrap", v)["peakA2_end"]] for v in sorted(sweep["selftrap"])},
        "curl_div_by_arm": {arm: {str(v): get(arm, v)["drive_curl_div"] for v in sorted(sweep[arm])} for arm in sweep},
    }


# ══════════════════════════════════════════════════════════════════════════════
# Full sweep + main
# ══════════════════════════════════════════════════════════════════════════════
def run_full_sweep(N, PML, variant, form, settle=10, n_steps=70):
    """SELF-TRAP / LINEAR / BASELINE × v_drive ∈ {0, low, mid, −mid}. Fixed host
    config across the sweep (no saturation-depth confound). Per-arm curl/div gate
    enforced (every arm's drive must be ≥90% compression)."""
    V_SWEEP = [0.0, 0.15, 0.30, -0.30]   # 0, low, mid, −mid (sign-flip control)
    arms = ["selftrap", "linear", "baseline"]
    sweep = {a: {} for a in arms}
    gate_fail = []
    for arm in arms:
        for v in V_SWEEP:
            print(f"    [{arm:9s} v={v:+.2f}] ...", flush=True, end=" ")
            t0 = time.time()
            r = run_arm(arm, v, N, PML, variant, form, settle=settle, n_steps=n_steps)
            sweep[arm][v] = r
            gate_ok = (v == 0.0) or (r["drive_curl_div"] < CURL_DIV_GATE)
            if not gate_ok:
                gate_fail.append((arm, v, r["drive_curl_div"]))
            print(f"v={r['v_centroid']:+.5f} ret={r['retention']:.3f} "
                  f"τ_zx={r['max_tau_zx_mean']:.2e} peakA²={r['peakA2_mean']:.2f} "
                  f"curl/div={r['drive_curl_div']:.4f}{'' if gate_ok else ' GATE-FAIL'} "
                  f"({time.time()-t0:.0f}s)", flush=True)
    return sweep, V_SWEEP, gate_fail


def main():
    N, PML = 48, 4
    SMOKE_N = 40
    settle, n_steps = 10, 70
    print("=" * 82, flush=True)
    print("  MOTION-STABILITY via back-EMF — LONGITUDINAL (decisive) channel | VacuumEngine3D")
    print("  Grant: stability FROM motion (retention(|v|)↑, tracks native longitudinal τ_zx).")
    print("  Canon: frozen V-core PINS even longitudinally (S→0, c_eff→0; c_L NOT frozen by S).")
    print("=" * 82, flush=True)
    print(f"  ALPHA={ALPHA} A²_op14={A2_OP14:.4f} c_L=√(10/3)={C_LONG:.4f} (ave-canonical-source) | dt={DT:.4f}")
    print(f"  FORWARD-PREDICTED (no fit): {FORWARD_PREDICTED_VERDICT} | {FORWARD_PREDICTED_SIGN}")
    print(f"  DRIVE GATE: curl/div < {CURL_DIV_GATE} (≥90% compression; the fix the killed run lacked)")

    # ── ANTI-STALL: gate + LINEAR-advection smoke, hard 2-try cap (Variant A → B) ──
    print("\n  ── ANTI-STALL: curl/div gate + LINEAR-advection smoke (A→B, 2-try cap) ──", flush=True)
    ts0 = time.time()
    smoke = smoke_test_drive(N=SMOKE_N, PML=PML, n_steps=60, form="displacement")
    for variant, rec in smoke["variants"].items():
        print(f"    Variant {variant}: gate curl/div={rec['gate_ratio_at_vmax']:.4f} "
              f"(pass={rec['gate_passed']}) | advects={rec['advects']} "
              f"v0≈0={rec['v0_is_zero']} signflip={rec['signflips']}", flush=True)
        for d in rec["per_v"]:
            print(f"        v_drive={d['v_drive']:+.2f}: v_centroid={d['v_centroid']:+.5f} dx={d['dx']:+.4f}")
    chosen = smoke["chosen_variant"]
    print(f"    CHOSEN drive variant: {chosen} (form={smoke['chosen_form']}) ({time.time()-ts0:.0f}s)", flush=True)
    if chosen is None:
        print("\n  BLOCKED-drive: neither Variant A nor B passes BOTH gate + LINEAR advection "
              "(2-try cap reached). STOP — see _orchestration DRIVE-CORRECTION.", flush=True)
        out = {"verdict": {"verdict": "BLOCKED-drive",
                           "text": "Neither curl-free variant cleared gate+advection within the 2-try cap.",
                           "forward_predicted_verdict": FORWARD_PREDICTED_VERDICT},
               "smoke": smoke}
        _save(out, None, None)
        return out["verdict"]

    # ── FULL SWEEP ──
    print(f"\n  ── FULL SWEEP (N={N}): SELF-TRAP / LINEAR / BASELINE × v_drive (variant {chosen}) ──", flush=True)
    sweep, V, gate_fail = run_full_sweep(N, PML, chosen, smoke["chosen_form"],
                                         settle=settle, n_steps=n_steps)
    if gate_fail:
        print(f"\n  BLOCKED-drive: {len(gate_fail)} arm(s) failed the curl/div gate at sweep time: "
              f"{gate_fail}. A mixed drive must NOT be run. STOP.", flush=True)
        verdict = {"verdict": "BLOCKED-drive",
                   "text": f"Per-arm gate failed at sweep time: {gate_fail}",
                   "forward_predicted_verdict": FORWARD_PREDICTED_VERDICT}
    else:
        verdict = adjudicate_motion_stability(sweep, V)

    print("\n" + "=" * 82)
    print("  VERDICT:", verdict["verdict"])
    print("=" * 82)
    if "adversarial_controls" in verdict:
        c = verdict["adversarial_controls"]
        print(f"  knot_moves={verdict['knot_moves']} pinned={verdict['knot_pinned']} | "
              f"selftrap_resp/linear={verdict['selftrap_resp_over_linear']:.3f}")
        print(f"  retention(|v|) slope (self-trap): {verdict['retention_v_slope_selftrap']:.4e}")
        print(f"  native τ_zx vs retention corr: {verdict['native_tau_zx_vs_retention_corr']:.3f}")
        print(f"  adversarial controls — 1_linear_distinct={c['1_linear_distinct']} "
              f"2_a2_holds={c['2_a2_holds']}(A²end/start={c['a2_end_over_start']:.3f}) "
              f"3_above_floor={c['3_above_lattice_floor']} 4_baseline_distinct={c['4_baseline_distinct']} "
              f"→ ALL_FOUR={c['all_four_cleared']}")
        print(f"  per-arm curl/div (proves drive clean): {verdict['curl_div_by_arm']}")
    print(f"\n  {verdict['text']}")
    print(f"\n  Forward-predicted: {verdict['forward_predicted_verdict']} | observed: {verdict['verdict']}")

    _save({"verdict": verdict, "smoke": smoke,
           "config": {"N": N, "PML": PML, "settle": settle, "n_steps": n_steps,
                      "host_R_frac": HOST_R_FRAC, "host_amp": HOST_AMP,
                      "A2_op14": A2_OP14, "ALPHA": ALPHA, "dt": DT, "c_L": C_LONG,
                      "V_sweep": V, "drive_variant": chosen, "drive_form": smoke["chosen_form"],
                      "curl_div_gate": CURL_DIV_GATE}},
          sweep, V)
    return verdict


def _save(out_json, sweep, V):
    if sweep is not None:
        out_json["arms"] = {arm: {str(v): {kk: vv for kk, vv in sweep[arm][v].items() if kk != "_traj"}
                                  for v in sweep[arm]} for arm in sweep}
    out_path = Path(__file__).parent / "motion_stability_bemf_longitudinal_probe_results.json"
    out_path.write_text(json.dumps(out_json, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {out_path.name}", flush=True)
    if sweep is not None:
        npz_path = Path(__file__).parent / "motion_stability_bemf_longitudinal_probe_capture.npz"
        np.savez_compressed(
            npz_path,
            **{f"{arm}_v{str(v).replace('-', 'm').replace('.', 'p')}": sweep[arm][v]["_traj"]
               for arm in sweep for v in sweep[arm]},
            dt=DT, c_L=C_LONG,
        )
        print(f"  Saved {npz_path.name}", flush=True)


if __name__ == "__main__":
    main()
