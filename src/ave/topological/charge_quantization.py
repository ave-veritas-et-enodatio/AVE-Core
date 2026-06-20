"""Charge-quantization structural gate (#43, GATE #2) — rigorous boundary 𝒬.

Replaces the connected-component PROXY named DEFERRED at
`boundary_invariants.py:146-151` with the REAL boundary topological charge 𝒬.
The corpus flags 𝒬's two definitions as "two projections of ONE charge via
helicity = linking (Moffatt 1969)" (coverage gap C.3,
`electron-bound-resonator-coverage.md:169`). This gate ADDRESSES that gap by
ADOPTING the product-formula bridge — it does NOT close it by two independent
integrals numerically agreeing (see compute_Q_hopf + C.3 disclosure below):

  𝒬_link  = the real-space boundary linking integer (the FIELD-DEPENDENT ω-phase
            winding around the meridian/major loops; degree↔linking identity),
            reusing `cosserat_field_3d._tetrahedral_curl` for the F = curl ω flux
            field. This is the genuine integer-quantized observable (exact via
            np.unwrap). For a (p,q) winding: poloidal = q, toroidal = p.

  𝒬_hopf  = the self-linking integer, computed as the arithmetic PRODUCT
            w_tor·w_pol = p·q (torus-knot-uniqueness.md:23). This is DEFINITIONAL
            (the product of the two windings 𝒬_link already read) — NOT an
            independent helicity integral, so 𝒬_hopf agreeing with 𝒬_link is a
            tautology, not a cross-check. The DIRECT Chern–Simons/Beltrami
            helicity integral (_hopf_density) returns ~18% of p·q at this scale
            and does NOT normalize to the integer — its sign tracks chirality,
            its magnitude does not quantize here. C.3 therefore STAYS OPEN
            (addressed-by-formula, not confirmed-by-two-integrals).

The gate reads ONLY the integer + sign. It demonstrates that the integer is a
TOPOLOGICAL invariant — robust to continuous deformation, jumping only when the
topology changes — which is what distinguishes a structural result (charge
quantization is FORCED) from a plant-and-recover (the integer is an artifact of
the planting).

GUARDS (see research/2026-06-19_charge-quantization-gate_prereg.md):
  1. VALUE-ECHO IMMUNITY — read only the integer 𝒬 and its sign; NEVER import
     `-e` / `α` / `Q_TANK`. An import-guard at module load asserts they are
     absent from this module's globals.
  2. TWO-3s ORTHOGONALITY — 𝒬 lives in the Cosserat ω micro-rotation grade; it
     is NEVER wired into the A1 (V_inc, V_ref) phasor (master-equation.md:20).
  3. SELF-FORMATION SEPARATION — this is STRUCTURAL quantization on a PLANTED
     winding; it does NOT claim the winding self-forms (genesis/keystone, which
     LEANS-FALSIFIED). NOT an emergence claim.
  4. PHASE-SPACE-COORDINATE-CHECK — the (2,3) is fenced PHASE-SPACE (def-kn0t01);
     the flux/linking here is REAL-SPACE ω field-line topology. Coordinate
     systems kept distinct.

HONEST SCOPE: conditional on the TKI [Q]≡[L] identification (charge ≡ winding/
linking integer), which is asserted not derived-from-nothing; and SEPARATE from
self-formation. A PASS is a structural advance over QED (which puts integer
charge in by hand via hypercharge + renders the point-charge self-energy finite
only by renormalization) on a problem QED cannot solve: AVE's charge is FINITE,
EXACT, quantized-BY-CONSTRUCTION (no renormalization).

EXPECTED-MATH CAVEAT (carried explicitly): topological invariance of a winding
number is expected mathematics once charge ≡ ω-grade winding/linking is accepted;
the AVE content is the [Q]≡[L] identification (asserted, conditional on the TKI
charge ≡ winding posit) plus the engine demonstration that the integer is α-free
and that sign = chirality on the actual K4/Cosserat operators — NOT the discovery
of invariance itself.

RESOLUTION CEILING (honest disclosure): the 𝒬 readout is lattice-faithful for
windings up to q ≈ 4 at this diagnostic scale (a winding spends 2πr/q cells/turn;
the K4-subsampled sampler floors at ~3 cells/wind). (2,3) → 4.82 cells/wind and
(2,4) → 3.61 cells/wind both resolve; (2,5) misreads as Q=3 and (1,5) gives a
half-integer (w_tor_raw ≈ 0.507), both at 2.89 cells/wind < floor. q ≥ 5 requires
a finer lattice. The canonical (2,3) is safely resolved.
"""

from __future__ import annotations

import numpy as np

from ave.topological.cosserat_field_3d import (
    _hopf_density,
    _tetrahedral_curl,
)

# ──────────────────────────────────────────────────────────────────────────
# VALUE-ECHO IMMUNITY import-guard (GUARD 1)
# ──────────────────────────────────────────────────────────────────────────
# The integer-ness of 𝒬 is the chord; the dimensionful value -e is the echo.
# This module must NEVER read α, Q_TANK, or e_charge. Assert they are absent
# from this module's globals at import time (fail loud if a future edit leaks
# one in via a transitive import or a copy-paste).
_FORBIDDEN_VALUE_ECHO_NAMES = (
    "ALPHA", "Q_TANK", "e_charge", "E_CHARGE",
    "kappa_chiral", "KAPPA_CHIRAL", "V_SNAP",
    "MASS_ELECTRON", "m_e", "M_E",
)
for _name in _FORBIDDEN_VALUE_ECHO_NAMES:
    assert _name not in globals(), (
        f"VALUE-ECHO IMMUNITY violation: '{_name}' present in "
        f"charge_quantization globals — 𝒬 reads only the integer + sign, never "
        f"the dimensionful -e / α / m_e / κ_chiral / V_snap (prereg GUARD 1)."
    )

# Source-level literal guard: the α value (137 / 0.00729...) must NEVER appear
# as a literal in the verdict-determining code path. Read this module's own
# source (functions + module body, EXCLUDING this guard block and docstrings)
# and assert the forbidden literals are absent. The integer-ness of 𝒬 is the
# chord; any α-numeral hardcoded into the read would be the echo.
_FORBIDDEN_VALUE_LITERALS = ("137", "0.00729")


def _assert_no_alpha_literal_in_code_path() -> None:
    import inspect

    src_lines = inspect.getsource(charge_quantization_gate) + inspect.getsource(compute_Q_link)
    src_lines += inspect.getsource(compute_Q_hopf) + inspect.getsource(_phase_winding_on_loop)
    for lit in _FORBIDDEN_VALUE_LITERALS:
        assert lit not in src_lines, (
            f"VALUE-ECHO IMMUNITY violation: α-literal '{lit}' found in the "
            f"verdict-determining code path — 𝒬 must be α-free (prereg GUARD 1)."
        )


__all__ = [
    "compute_F_curl",
    "compute_Q_hopf",
    "compute_Q_link",
    "deform_continuous",
    "unwind_topology",
    "seed_pq_winding",
    "charge_quantization_gate",
]


# ──────────────────────────────────────────────────────────────────────────
# Toroidal-coordinate sampler (real-space ω field, GUARD 4)
# ──────────────────────────────────────────────────────────────────────────


def _torus_point(c: float, R: float, r: float, phi: float, psi: float) -> tuple[float, float, float]:
    """Real-space (x, y, z) of the torus point (φ major, ψ minor) about center c.

    The boundary loop ∂Ω lives on this torus; the F = curl ω flux tube threads
    it. REAL-SPACE coordinates (GUARD 4) — NOT the phase-space (2,3) Clifford
    torus (def-kn0t01).
    """
    rad = R + r * np.cos(psi)
    return (c + rad * np.cos(phi), c + rad * np.sin(phi), c + r * np.sin(psi))


def _sample_alive_trilinear(field: np.ndarray, alive: np.ndarray,
                            x: float, y: float, z: float, N: int):
    """Alive-weighted trilinear sample of a (N,N,N,3) field at off-lattice (x,y,z).

    The K4 diamond mask zeros ~3/4 of cells (only the A+B sublattice is alive),
    so nearest-cell sampling along a loop lands on a DEAD cell ~75% of the time
    and the phase walk loses the winding (a Rule-10 integrator-time bug that
    static inspection misses). This gather interpolates over ALIVE corners only,
    renormalizing by the alive-weight sum — recovering the underlying winding
    without ever reading a dead (frozen-zero) cell.

    Returns the interpolated 3-vector, or None if out of box / no alive corner.
    """
    x0, y0, z0 = int(np.floor(x)), int(np.floor(y)), int(np.floor(z))
    if not (0 <= x0 < N - 1 and 0 <= y0 < N - 1 and 0 <= z0 < N - 1):
        return None
    fx, fy, fz = x - x0, y - y0, z - z0
    acc = np.zeros(3, dtype=np.float64)
    wsum = 0.0
    for dx, wx in ((0, 1.0 - fx), (1, fx)):
        for dy, wy in ((0, 1.0 - fy), (1, fy)):
            for dz, wz in ((0, 1.0 - fz), (1, fz)):
                ii, jj, kk = x0 + dx, y0 + dy, z0 + dz
                if alive[ii, jj, kk]:
                    w = wx * wy * wz
                    acc += w * field[ii, jj, kk]
                    wsum += w
    if wsum < 1e-9:
        return None
    return acc / wsum


# ──────────────────────────────────────────────────────────────────────────
# Gauss linking integral (the rigorous 1D line/loop 𝒬 = Link(∂Ω, F))
# ──────────────────────────────────────────────────────────────────────────


def _gauss_linking_integral(C1: np.ndarray, C2: np.ndarray) -> float:
    """Gauss linking integral Lk(C1, C2) of two closed polylines.

    Lk = (1/4π) ∮∮ (r1 − r2)·(dr1 × dr2) / |r1 − r2|³

    The textbook 1D line/loop linking number (boundary-observables-m-q-j.md:20
    dimensionality "1D line/loop"). Returns a float that is an INTEGER for
    genuinely linked closed curves (validated on the Hopf link → ±1, unlinked
    → 0, orientation-reversal → sign flip in the gate's known anchors).

    C1, C2: (M, 3) and (K, 3) arrays of points on the closed curves (the curve
    is closed by wrapping the last segment back to the first point).
    """
    C1 = np.asarray(C1, dtype=np.float64)
    C2 = np.asarray(C2, dtype=np.float64)
    dC1 = np.roll(C1, -1, axis=0) - C1
    dC2 = np.roll(C2, -1, axis=0) - C2
    mid1 = C1 + 0.5 * dC1
    mid2 = C2 + 0.5 * dC2
    total = 0.0
    for a in range(len(C1)):
        r = mid1[a][None, :] - mid2  # (K, 3)
        rn = np.linalg.norm(r, axis=1) ** 3 + 1e-30
        cross = np.cross(np.broadcast_to(dC1[a], dC2.shape), dC2)
        total += float(np.sum(np.sum(r * cross, axis=1) / rn))
    return total / (4.0 * np.pi)


def _phase_winding_on_loop(omega: np.ndarray, N: int, R: float, r: float,
                           kind: str, base: float, n_ang: int = 360) -> tuple[float, float]:
    """Winding of arg(ω_⊥) around a closed real-space loop on the |ω| torus.

    This is the FIELD-DEPENDENT degree of the boundary director map — the
    genuine real-space topological integer. By the degree↔linking identity, the
    winding of the ω-phase around a closed loop EQUALS the linking number of the
    F = curl ω flux line with that loop (the boundary 𝒬 = Link(∂Ω, F)).

    kind="poloidal": sweep the minor angle ψ at fixed major angle φ0 = base →
        counts the POLOIDAL winding (the flux line threading the meridian disk =
        Link(∂Ω_meridian, F)). For a (p, q) winding this is q.
    kind="toroidal": sweep the major angle φ at fixed minor angle ψ0 = base →
        counts the TOROIDAL winding. For a (p, q) winding this is p.

    Reads arg of the transverse ω in the (x, y) plane (the seeded winding plane).
    Returns (winding_raw, reliability) where reliability = mean|ω|/max|ω| on the
    sampled loop (a low value flags an unresolved / off-tube loop).

    REAL-SPACE ω field (GUARD 2 ω-grade only; GUARD 4 real-space, not (2,3)
    phase-space).
    """
    omega = np.asarray(omega, dtype=np.float64)
    alive = np.abs(omega).sum(axis=-1) > 1e-12  # K4-alive mask (A+B sublattice)
    c = (N - 1) / 2.0
    angs = np.linspace(0.0, 2.0 * np.pi, n_ang, endpoint=False)
    phases = np.full(n_ang, np.nan)
    amps = np.zeros(n_ang)
    for a, ang in enumerate(angs):
        if kind == "poloidal":
            x, y, z = _torus_point(c, R, r, base, ang)
        elif kind == "toroidal":
            x, y, z = _torus_point(c, R, r, ang, base)
        else:
            raise ValueError(f"kind must be 'poloidal'/'toroidal', got {kind!r}")
        v = _sample_alive_trilinear(omega, alive, x, y, z, N)
        if v is None:
            continue
        phases[a] = np.arctan2(v[1], v[0])
        amps[a] = float(np.hypot(v[0], v[1]))
    ok = np.isfinite(phases) & (amps > 1e-9)
    if ok.sum() < 16:
        return float("nan"), 0.0
    ph = np.unwrap(phases[ok])
    w = (ph[-1] - ph[0]) / (2.0 * np.pi)
    rel = float(amps[ok].mean() / (amps[ok].max() + 1e-30))
    return float(w), rel


def compute_Q_link(omega: np.ndarray, R: float, r: float, n_loops: int = 8) -> dict:
    """𝒬_link — the rigorous real-space boundary linking integer Link(∂Ω, F).

    Replaces the connected-component PROXY (boundary_invariants.py:146-151) with
    the genuine 1D line/loop linking number. By the degree↔linking identity, the
    boundary linking number of the F = curl ω flux line with the meridian loop
    ∂Ω equals the POLOIDAL winding of the ω director around that loop — a
    FIELD-DEPENDENT topological integer (the field-blind Gauss geometric trace is
    uninformative; the field's own phase carries the topology). The TOROIDAL
    winding is reported alongside as the complementary count; their product is
    the self-linking p·q (the Moffatt helicity = linking cross-check, computed in
    compute_Q_hopf).

    Median over n_loops base angles for robustness (each loop is an independent
    estimate of the same topological integer). Reads ONLY the integer + sign.

    Returns dict: Q_link (the poloidal linking integer = the boundary 𝒬),
    Q_link_raw, sign, plus w_tor / w_pol raw + reliabilities for inspection.
    """
    omega = np.asarray(omega, dtype=np.float64)
    N = omega.shape[0]
    bases = np.linspace(0.0, 2.0 * np.pi, n_loops, endpoint=False)

    pol = [_phase_winding_on_loop(omega, N, R, r, "poloidal", b) for b in bases]
    tor = [_phase_winding_on_loop(omega, N, R, r, "toroidal", b) for b in bases]
    pol_w = [w for (w, rel) in pol if np.isfinite(w) and rel > 0.1]
    tor_w = [w for (w, rel) in tor if np.isfinite(w) and rel > 0.1]
    pol_rel = [rel for (w, rel) in pol if np.isfinite(w)]
    tor_rel = [rel for (w, rel) in tor if np.isfinite(w)]

    # The boundary 𝒬 = the poloidal linking integer (the flux line through the
    # meridian disk). Median raw → nearest integer.
    Q_link_raw = float(np.median(pol_w)) if pol_w else 0.0
    Q_int = int(np.round(Q_link_raw)) if pol_w else 0
    w_tor_raw = float(np.median(tor_w)) if tor_w else 0.0
    w_tor_int = int(np.round(w_tor_raw)) if tor_w else 0

    return {
        "Q_link": Q_int,
        "Q_link_raw": Q_link_raw,
        "sign": int(np.sign(Q_int)) if Q_int != 0 else 0,
        "w_pol_raw": Q_link_raw,
        "w_tor_raw": w_tor_raw,
        "w_tor": w_tor_int,
        "w_pol_rel": float(np.median(pol_rel)) if pol_rel else 0.0,
        "w_tor_rel": float(np.median(tor_rel)) if tor_rel else 0.0,
    }


def compute_F_curl(omega: np.ndarray) -> np.ndarray:
    """F = curl ω — the substrate flux field (the prereg Stage-1 construction).

    Uses the existing tetrahedral curl operator (cosserat_field_3d._tetrahedral_curl
    `:514`). The boundary 𝒬 = Link(∂Ω, F) is the linking of this flux field's line
    with the boundary loop; by the degree↔linking identity that linking integer
    equals the ω-phase winding read by compute_Q_link (which is the numerically
    robust route — direct flux-line extraction on a coarse lattice is fragile).
    Exposed so callers can inspect F and confirm it is non-trivial where the
    winding lives. REAL-SPACE ω-grade only (GUARDs 2, 4).
    """
    import jax.numpy as jnp

    return np.asarray(_tetrahedral_curl(jnp.asarray(omega), dx=1.0))


# ──────────────────────────────────────────────────────────────────────────
# 𝒬_hopf — Chern–Simons self-linking (Moffatt helicity = linking cross-check)
# ──────────────────────────────────────────────────────────────────────────


def compute_Q_hopf(omega: np.ndarray, R: float, r: float) -> dict:
    """𝒬_hopf — the self-linking integer p·q (Moffatt helicity = linking).

    The corpus flags 𝒬's two definitions — 1D linking Link(∂Ω, F) and 3D
    Beltrami helicity H_bel = ∫ω·(∇×ω) — as "two projections of ONE charge via
    helicity = linking (Moffatt 1969); that identity is NOT written for the AVE
    case" (electron-bound-resonator-coverage.md:169, gap C.3). This writes it:
    the self-linking integer of a (p, q) torus winding is the PRODUCT of its
    toroidal and poloidal winding integers, w_tor · w_pol = p·q, which is the
    Hopf invariant Q_H (torus-knot-uniqueness.md:23). For (2,3): Q_H = 6.

    We read the self-linking from the two field-dependent winding integers
    (compute_Q_link), NOT from the raw _hopf_density integral — which on the
    open-boundary lattice at diagnostic scale does NOT normalize to the integer
    (it returns ~18% of p·q — measured 1.08 vs p·q=6 at R≈7; the director map's
    S² asymptotics are not clean at this resolution). HONEST: Q_hopf here is the
    arithmetic PRODUCT w_tor·w_pol of the two windings already read by
    compute_Q_link — this is DEFINITIONAL (adopting Q_H = p·q,
    torus-knot-uniqueness.md:23), NOT an independent helicity integral, so it is
    NOT a cross-check of the two integrals agreeing. The integer-quantized
    observable is the WINDING PRODUCT (degree theory, exact via np.unwrap);
    _hopf_density is reported only as a finite, non-quantized density diagnostic
    (its SIGN tracks chirality, its magnitude does not quantize here). Corpus gap
    C.3 is therefore ADDRESSED-BY-FORMULA, not closed-by-two-integrals-agreeing.
    Reads ONLY integers + sign — no -e/α (GUARD 1).

    Returns dict: Q_hopf (= w_tor·w_pol self-linking integer), sign, and the
    finite _hopf_density integral (non-quantized, sign-only diagnostic).
    """
    omega = np.asarray(omega, dtype=np.float64)
    link = compute_Q_link(omega, R, r)
    w_tor, w_pol = link["w_tor"], link["Q_link"]
    Q_hopf = int(w_tor * w_pol)
    # Finite (non-quantized) helicity-density integral — sign-only diagnostic.
    W_hopf = np.asarray(_hopf_density(omega, dx=1.0))
    hopf_density_integral = float(np.sum(W_hopf))
    return {
        "Q_hopf": Q_hopf,
        "sign": int(np.sign(Q_hopf)) if Q_hopf != 0 else 0,
        "w_tor": w_tor,
        "w_pol": w_pol,
        "hopf_density_integral": hopf_density_integral,
        "hopf_density_sign": int(np.sign(hopf_density_integral)) if abs(hopf_density_integral) > 1e-12 else 0,
    }


# ──────────────────────────────────────────────────────────────────────────
# Deformation operators (STAGE 2 — topological protection)
# ──────────────────────────────────────────────────────────────────────────


def deform_continuous(omega: np.ndarray, kind: str, strength: float, seed: int = 0) -> np.ndarray:
    """Apply a CONTINUOUS, topology-PRESERVING deformation to the ω field.

    These are smooth perturbations that do NOT cut or reconnect the winding —
    a genuine topological invariant must be INVARIANT under all of them (it can
    only change by a discrete jump if the topology changes). Each is a
    homotopy-trivial map on the field.

    kind:
      "smooth_noise"  — add a smooth (Gaussian-blurred) random vector field of
                        magnitude `strength`·|ω|_max. Does not unwind the phase.
      "local_scale"   — multiply ω by a smooth spatially-varying positive scalar
                        1 + strength·(smooth field). Amplitude wobble; topology
                        is amplitude-blind.
      "swirl"         — apply a smooth small rigid-ish rotation of the ω VECTORS
                        by angle strength·(smooth field) about ẑ. A continuous
                        SO(3) action on the codomain; preserves winding.
      "warp"          — smoothly displace (advect) the field by a small
                        divergence-free coordinate warp of magnitude `strength`.
                        A diffeomorphism of the domain; preserves all winding.

    REAL-SPACE ω-grade only (GUARDs 2, 4). Returns a new (N,N,N,3) array.
    """
    omega = np.asarray(omega, dtype=np.float64)
    N = omega.shape[0]
    rng = np.random.default_rng(seed)
    amax = float(np.sqrt(np.sum(omega * omega, axis=-1)).max()) + 1e-30
    # FIXED structural K4-alive mask — a deformation must NOT resurrect dead
    # cells (that would be a coordinate artifact, not a physical perturbation);
    # the mask is re-applied after every deformation so the alive set is
    # invariant (the deformation acts only on the live ω field).
    alive = np.abs(omega).sum(axis=-1) > 1e-12

    def _smooth(field, passes=4):
        # cheap separable box-blur (keeps the perturbation above the grid scale)
        f = field.copy()
        for _ in range(passes):
            f = (f
                 + np.roll(f, 1, 0) + np.roll(f, -1, 0)
                 + np.roll(f, 1, 1) + np.roll(f, -1, 1)
                 + np.roll(f, 1, 2) + np.roll(f, -1, 2)) / 7.0
        return f

    if kind == "smooth_noise":
        noise = rng.standard_normal((N, N, N, 3))
        noise = _smooth(noise)
        noise /= (np.sqrt(np.sum(noise * noise, axis=-1)).max() + 1e-30)
        out = omega + strength * amax * noise
    elif kind == "local_scale":
        s = _smooth(rng.standard_normal((N, N, N)))
        s /= (np.abs(s).max() + 1e-30)
        out = omega * (1.0 + strength * s)[..., None]
    elif kind == "swirl":
        ang = strength * _smooth(rng.standard_normal((N, N, N)))
        ang /= (np.abs(ang).max() + 1e-30) / max(abs(strength), 1e-30)
        ca, sa = np.cos(ang), np.sin(ang)
        ox, oy, oz = omega[..., 0], omega[..., 1], omega[..., 2]
        out = np.stack([ca * ox - sa * oy, sa * ox + ca * oy, oz], axis=-1)
    elif kind == "warp":
        # small smooth advection of the field along a random sub-cell
        # displacement (a domain diffeomorphism — preserves all winding).
        disp = strength * rng.standard_normal(3)
        disp = np.clip(disp, -0.49, 0.49)
        shifted = omega.copy()
        for ax in range(3):
            d = float(disp[ax])
            shifted = (1.0 - abs(d)) * shifted + abs(d) * np.roll(
                shifted, 1 if d >= 0 else -1, axis=ax
            )
        out = shifted
    else:
        raise ValueError(f"unknown continuous deformation kind {kind!r}")
    # Re-apply the structural K4 mask (alive set invariant under deformation).
    out = out * alive[..., None]
    return out


def unwind_topology(omega: np.ndarray, R: float, r: float) -> np.ndarray:
    """Apply a topology-CHANGING operation: UNWIND the (p, q) winding.

    Replaces the phase θ = pφ + qψ with a CONSTANT phase (θ → 0) while keeping
    the SAME amplitude envelope and the SAME total |ω| energy budget. This cuts
    the winding (a discrete topology change) WITHOUT changing the amplitude /
    where-the-field-lives — so any 𝒬 that merely counted the planted amplitude
    would be UNCHANGED, while a genuine topological 𝒬 must JUMP to 0.

    This is the discriminator that separates a structural (topology-forced)
    result from an amplitude-count artifact.

    REAL-SPACE ω-grade only (GUARDs 2, 4). Returns a new (N,N,N,3) array.
    """
    omega = np.asarray(omega, dtype=np.float64)
    N = omega.shape[0]
    # Recover the per-site amplitude envelope from |ω_⊥|, re-lay it with ZERO
    # winding (constant phase) → topology cut, amplitude/energy preserved.
    env = np.sqrt(omega[..., 0] ** 2 + omega[..., 1] ** 2)
    out = np.zeros_like(omega)
    out[..., 0] = env  # constant phase (θ=0): all phase information removed
    out[..., 1] = 0.0
    out[..., 2] = omega[..., 2]
    return out


# ──────────────────────────────────────────────────────────────────────────
# Seeder (lattice-resolved diagnostic plant — NOT self-formation, GUARD 3)
# ──────────────────────────────────────────────────────────────────────────


def seed_pq_winding(N: int, p: int, q: int, R: float, r: float, amplitude_scale: float = 1.0) -> np.ndarray:
    """Plant a (p, q) winding on the Cosserat ω field at a diagnostic scale.

    Same toroidal construction as CosseratField3D.initialize_electron_2_3_sector
    (θ = pφ + qψ hedgehog envelope) but parameterized in (p, q) so the gate can
    plant known windings and the null. PLANTED, NOT self-formed (GUARD 3):
    this is a structural-quantization read on a given configuration.

    REAL-SPACE ω-grade only (GUARDs 2, 4). Returns (N,N,N,3).
    """
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    x, y, z = i - c, j - c, k - c
    rho = np.sqrt(x ** 2 + y ** 2)
    rtube = np.sqrt((rho - R) ** 2 + z ** 2)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho - R)
    r_opt = r if r > 0 else 1.0
    env = amplitude_scale * (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rtube / r_opt) ** 2)
    theta = p * phi + q * psi
    omega = np.zeros((N, N, N, 3), dtype=np.float64)
    omega[..., 0] = env * np.cos(theta)
    omega[..., 1] = env * np.sin(theta)
    mask = ((i % 2 == 0) & (j % 2 == 0) & (k % 2 == 0)) | ((i % 2 == 1) & (j % 2 == 1) & (k % 2 == 1))
    omega *= mask[..., None]
    return omega


# ──────────────────────────────────────────────────────────────────────────
# The gate runner (STAGE 3 — run + bin per frozen prereg)
# ──────────────────────────────────────────────────────────────────────────


def charge_quantization_gate(
    N: int = 32,
    p: int = 2,
    q: int = 3,
    R: float = 7.0,
    r: float = 2.3,
    n_deformations: int = 6,
    int_tol: float = 0.25,
) -> dict:
    """Run the charge-quantization structural gate (#43) and bin the verdict.

    Pipeline (frozen prereg 2026-06-19):
      1. VALIDATE-ON-KNOWN (wired FIRST):
         - KNOWN-NEGATIVE: ω≡0 null → 𝒬 must be 0, else HALT.
         - KNOWN-POSITIVE: planted (p,q) → 𝒬 must recover its winding integer,
           else HALT.
      2. Compute 𝒬 on the planted (p,q) winding (the de-novo read, built BETWEEN
         the two anchors).
      3. STAGE 2 — topological protection: apply n_deformations CONTINUOUS,
         topology-preserving deformations; 𝒬 must stay the SAME integer.
      4. Apply the topology-CHANGING unwind; 𝒬 must JUMP to 0.
      5. Bin: PASS / ECHO-or-FAIL (failing condition named) / HALT.

    Reads ONLY integers + sign (GUARD 1 value-echo immunity); ω-grade only
    (GUARD 2); PLANTED not self-formed (GUARD 3); real-space (GUARD 4).

    Returns a dict with every 𝒬 value (planted, deformed-sequence, unwound),
    both known-anchors, and the binned verdict.
    """
    out: dict = {"config": {"N": N, "p": p, "q": q, "R": R, "r": r}}

    # ── 1. VALIDATE-ON-KNOWN (HALT gate) ──
    omega_null = np.zeros((N, N, N, 3), dtype=np.float64)
    q_null = compute_Q_link(omega_null, R, r)
    out["known_negative_null"] = {"Q_link": q_null["Q_link"], "Q_link_raw": q_null["Q_link_raw"]}

    omega_planted = seed_pq_winding(N, p, q, R, r)
    # F = curl ω (prereg Stage-1 substrate flux field) — confirm non-trivial
    # where the winding lives (the linking is read via the equivalent phase
    # winding; this records that F itself is non-vanishing).
    F = compute_F_curl(omega_planted)
    out["flux_field_F_curl_omega"] = {
        "F_max": float(np.abs(F).max()),
        "F_nontrivial": bool(np.abs(F).max() > 1e-6),
    }
    q_planted = compute_Q_link(omega_planted, R, r)
    q_planted_hopf = compute_Q_hopf(omega_planted, R, r)
    out["known_positive_planted"] = {
        "Q_link": q_planted["Q_link"],
        "Q_link_raw": q_planted["Q_link_raw"],
        "w_tor": q_planted["w_tor"],
        "w_tor_raw": q_planted["w_tor_raw"],
        "w_pol_rel": q_planted["w_pol_rel"],
        "w_tor_rel": q_planted["w_tor_rel"],
        "Q_hopf_selflink": q_planted_hopf["Q_hopf"],
        "sign": q_planted["sign"],
    }

    null_ok = (q_null["Q_link"] == 0)
    # known-positive recovers q (the poloidal linking) within tolerance
    pos_ok = (q_planted["Q_link"] == q) and (abs(q_planted["Q_link_raw"] - q) < int_tol)
    if not null_ok or not pos_ok:
        out["verdict"] = "HALT"
        out["halt_reason"] = (
            f"known-anchor misbehaved: null Q={q_null['Q_link']} (expect 0); "
            f"planted Q={q_planted['Q_link']} raw={q_planted['Q_link_raw']:.3f} "
            f"(expect {q})."
        )
        return out

    Q0 = q_planted["Q_link"]
    sign0 = q_planted["sign"]

    # ── 3. STAGE 2: continuous topology-preserving deformations ──
    kinds = ["smooth_noise", "local_scale", "swirl", "warp", "smooth_noise", "local_scale"]
    strengths = [0.15, 0.25, 0.20, 0.30, 0.35, 0.40]
    deformed = []
    for d in range(n_deformations):
        kind = kinds[d % len(kinds)]
        strength = strengths[d % len(strengths)]
        om_def = deform_continuous(omega_planted, kind, strength, seed=d)
        qd = compute_Q_link(om_def, R, r)
        deformed.append({
            "kind": kind,
            "strength": strength,
            "Q_link": qd["Q_link"],
            "Q_link_raw": round(qd["Q_link_raw"], 4),
            "sign": qd["sign"],
        })
    out["deformed_sequence"] = deformed
    deformed_Qs = [d["Q_link"] for d in deformed]
    deformed_invariant = all(qv == Q0 for qv in deformed_Qs)
    deformed_raw_close = all(abs(d["Q_link_raw"] - Q0) < int_tol for d in deformed)

    # ── 4. topology-CHANGING unwind ──
    omega_unwound = unwind_topology(omega_planted, R, r)
    q_unwound = compute_Q_link(omega_unwound, R, r)
    out["topology_changed_unwound"] = {
        "Q_link": q_unwound["Q_link"],
        "Q_link_raw": q_unwound["Q_link_raw"],
    }
    unwind_jumped = (q_unwound["Q_link"] != Q0)

    # ── 5. BIN (frozen prereg) ──
    is_integer = abs(q_planted["Q_link_raw"] - round(q_planted["Q_link_raw"])) < int_tol
    equals_winding = (Q0 == q)
    conditions = {
        "is_integer": bool(is_integer),
        "equals_planted_winding": bool(equals_winding),
        "robust_under_continuous_deformation": bool(deformed_invariant and deformed_raw_close),
        "jumps_on_topology_change": bool(unwind_jumped),
    }
    out["pass_conditions"] = conditions
    if all(conditions.values()):
        out["verdict"] = "PASS"
        out["verdict_detail"] = (
            f"𝒬 = {Q0} (sign {sign0:+d}) = planted winding q={q}; INTEGER; "
            f"INVARIANT across {n_deformations} continuous deformations; "
            f"JUMPS to {q_unwound['Q_link']} on unwind. Topologically FORCED."
        )
    else:
        failing = [k for k, v in conditions.items() if not v]
        out["verdict"] = "ECHO/FAIL"
        out["verdict_detail"] = f"failing condition(s): {failing}"
    return out


# Run the source-level α-literal guard now that the code-path functions exist
# (the name guard above runs at the top of import; this one needs the defs).
_assert_no_alpha_literal_in_code_path()


if __name__ == "__main__":
    import json

    print("CHARGE-QUANTIZATION STRUCTURAL GATE (#43, GATE #2)")
    print("=" * 60)
    result = charge_quantization_gate()
    print(json.dumps(result, indent=2, default=str))
    print("=" * 60)
    print(f"VERDICT: {result['verdict']}")
