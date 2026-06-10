"""NumPy-vectorized re-implementation of the graft-v2 ω-carrier (2,3) extractor.

This is a MEASUREMENT INSTRUMENT, not a physics change. It reproduces — to the
bit, by construction — the per-angle phase walks of
``crystal_graft_v2_run.extract_2_3_omega`` (the toroidal-"2" / poloidal-"3" read
on the independent Cosserat-ω carrier), replacing the Python-loop trilinear
sampler (``_interp_vec`` called n_ang × n_walks × 2 sectors per checkpoint) with a
single vectorized gather per sector.

WHY BIT-EXACT MATTERS (ave-driver-script-honesty): the extractor's output is
compared ACROSS runs (arm vs control, run-length-doubling vs baseline). A silent
behavior change in the instrument would corrupt every cross-run comparison and
manufacture or hide a (2,3). So this module:

* keeps the SAME float64 arithmetic, SAME summation order in the trilinear
  stencil, SAME ``np.unwrap`` reduction, SAME covariance/eigh principal axis,
  SAME modal-integer outlier vote, and SAME reliability contour as the original;
* ships :func:`verify_equivalence`, which takes the ORIGINAL extractor as an
  argument (dependency injection — this library never imports a `src/scripts`
  driver) and asserts identical output on planted-(2,3) / null / random fields.

float64 is REQUIRED, not a default: the same ω field feeds the conservation
canaries (H drift, |L_ω| secular slope) at the 1e-3 level; an f32 extractor would
both miss the 1e-12 equivalence gate and desync the energy ledger. No f32 path.
"""

from __future__ import annotations

from collections import Counter
from typing import Callable, Dict

import numpy as np

__all__ = [
    "winding_from_phases",
    "interp_vec_batch",
    "extract_2_3_omega_fast",
    "verify_equivalence",
]


# ──────────────────────────────────────────────────────────────────────────
# per-walk reduction — reproduced VERBATIM from crystal_graft_v2_run so the
# unwrap/reliability arithmetic is identical (this part was never the bottleneck;
# the bottleneck was the n_ang × n_walks scalar _interp_vec calls below).
# ──────────────────────────────────────────────────────────────────────────
def winding_from_phases(phases, amps):
    """Amplitude-weighted unwrapped winding of a per-site phase around a closed
    loop. Returns (winding_real, reliability) where reliability = (mean amp)/
    (max amp) on valid sites (∈[0,1]); rel>0.1 ⇒ a reliable contour."""
    phases = np.asarray(phases)
    amps = np.asarray(amps)
    ok = np.isfinite(phases) & (amps > 1e-9)
    if ok.sum() < 16:
        return float("nan"), 0.0
    ph = np.unwrap(phases[ok])
    w = (ph[-1] - ph[0]) / (2.0 * np.pi)
    rel = float(amps[ok].mean() / (amps[ok].max() + 1e-30))
    return float(w), rel


def interp_vec_batch(F, c, R, r, phi, psi, N):
    """Vectorized trilinear sample of a 3-vector field ``F`` at a grid of torus
    points ``(phi, psi)`` (arbitrary array shape S).

    Returns ``(vals, valid)`` with ``vals`` shape ``S + (3,)`` and boolean
    ``valid`` shape ``S``. For valid points the result is BIT-IDENTICAL to the
    scalar ``crystal_graft_v2_run._interp_vec``: same torus map, same bounds test
    (``1 <= {x,y,z} < N-1``), same ``int(floor())`` corner, same ``wx*wy*wz``
    product, and the same dx-outer / dy-mid / dz-inner accumulation order. Invalid
    points carry a finite placeholder (caller masks them out via ``valid``)."""
    phi = np.asarray(phi, dtype=np.float64)
    psi = np.asarray(psi, dtype=np.float64)
    rad = R + r * np.cos(psi)
    x = c + rad * np.cos(phi)
    y = c + rad * np.sin(phi)
    z = c + r * np.sin(psi)

    valid = (x >= 1) & (x < N - 1) & (y >= 1) & (y < N - 1) & (z >= 1) & (z < N - 1)

    # placeholder coords for OOB points so advanced indexing stays in range; the
    # value computed there is discarded by the caller (valid mask). 1.0 ⇒ x0=1.
    xs = np.where(valid, x, 1.0)
    ys = np.where(valid, y, 1.0)
    zs = np.where(valid, z, 1.0)

    x0 = np.floor(xs).astype(np.intp)
    y0 = np.floor(ys).astype(np.intp)
    z0 = np.floor(zs).astype(np.intp)
    fx = xs - x0
    fy = ys - y0
    fz = zs - z0

    out = np.zeros(phi.shape + (3,), dtype=np.float64)
    # identical nested order to the scalar version: ((0,1-f),(1,f)) on x,y,z.
    for dx, wx in ((0, 1.0 - fx), (1, fx)):
        for dy, wy in ((0, 1.0 - fy), (1, fy)):
            for dz, wz in ((0, 1.0 - fz), (1, fz)):
                w = (wx * wy * wz)[..., None]
                out = out + w * F[x0 + dx, y0 + dy, z0 + dz]
    return out, valid


def extract_2_3_omega_fast(omega, pi_omega, R, r, N, n_ang=240, n_walks=12) -> Dict:
    """Vectorized twin of ``crystal_graft_v2_run.extract_2_3_omega``.

    Same coordinate-correct (2,3) read on the INDEPENDENT ω carrier: toroidal "2"
    = winding of arg((ω·ê_R)+i(ω·ê_z)) around the major circle; poloidal "3" =
    winding of the ω-tank LC phase arg((ω·d̂)+i(π_ω·d̂)) around the minor circle,
    with d̂ the principal transverse axis from the ω covariance. Returns the SAME
    dict (w_tor, w_pol, modal counts, raw medians/lists, reliabilities, crossing
    number, is_2_3)."""
    c = (N - 1) / 2.0
    out = {"R": float(R), "r": float(r)}

    # ── toroidal "2": winding of arg(Ψ) around MAJOR φ, at varied ψ0 ──
    # grid (W, A): rows = ψ0 walks, cols = φ angles.
    psi0 = np.linspace(0.0, 2 * np.pi, n_walks, endpoint=False)  # (W,)
    phi = np.linspace(0.0, 2 * np.pi, n_ang, endpoint=False)  # (A,)
    PHI = np.broadcast_to(phi[None, :], (n_walks, n_ang))
    PSI = np.broadcast_to(psi0[:, None], (n_walks, n_ang))
    o, vmask = interp_vec_batch(omega, c, R, r, PHI, PSI, N)  # o:(W,A,3)
    cphi = np.cos(PHI)
    sphi = np.sin(PHI)
    # a1 = o @ ê_R = o0*cosφ + o1*sinφ + o2*0   (+0 term kept for bit-parity)
    a1 = o[..., 0] * cphi + o[..., 1] * sphi + o[..., 2] * 0.0
    a2 = o[..., 2]
    tor_ph = np.where(vmask, np.arctan2(a2, a1), np.nan)
    tor_am = np.where(vmask, np.hypot(a1, a2), 0.0)
    tor_raw, tor_rel = [], []
    for wlk in range(n_walks):
        w, rel = winding_from_phases(tor_ph[wlk], tor_am[wlk])
        if np.isfinite(w):
            tor_raw.append(w)
            tor_rel.append(rel)

    # ── poloidal "3": winding of arg(Z=(ω·d̂)+i(π_ω·d̂)) around MINOR ψ ──
    phi0 = np.linspace(0.0, 2 * np.pi, n_walks, endpoint=False)  # (W,)
    psis = np.linspace(0.0, 2 * np.pi, n_ang, endpoint=False)  # (A,)
    PHI0 = np.broadcast_to(phi0[:, None], (n_walks, n_ang))
    PSI2 = np.broadcast_to(psis[None, :], (n_walks, n_ang))
    op, vmask_o = interp_vec_batch(omega, c, R, r, PHI0, PSI2, N)  # (W,A,3)
    pp, vmask_p = interp_vec_batch(pi_omega, c, R, r, PHI0, PSI2, N)
    # original requires BOTH samples present (o is None or p is None); the bounds
    # test is identical for both fields at the same torus point ⇒ masks coincide.
    vmask_pol = vmask_o & vmask_p
    cphi0 = np.cos(phi0)  # (W,)
    sphi0 = np.sin(phi0)
    # O_full[...,0] = o·ê_R, O_full[...,1] = o·ê_z ; same for π_ω.
    OeR = op[..., 0] * cphi0[:, None] + op[..., 1] * sphi0[:, None] + op[..., 2] * 0.0
    Oz = op[..., 2]
    PeR = pp[..., 0] * cphi0[:, None] + pp[..., 1] * sphi0[:, None] + pp[..., 2] * 0.0
    Pz = pp[..., 2]

    pol_raw, pol_rel = [], []
    for wlk in range(n_walks):
        valid_idx = np.nonzero(vmask_pol[wlk])[0]  # increasing-i order (matches)
        if len(valid_idx) < 16:
            continue
        O = np.stack([OeR[wlk, valid_idx], Oz[wlk, valid_idx]], axis=1)  # (M,2)
        P = np.stack([PeR[wlk, valid_idx], Pz[wlk, valid_idx]], axis=1)
        cov = O.T @ O
        evals, evecs = np.linalg.eigh(cov)
        dhat = evecs[:, np.argmax(evals)]  # (2,) principal transverse axis
        c_state = O @ dhat  # (M,)  C-state ω·d̂
        l_state = P @ dhat  # (M,)  L-state π_ω·d̂ (independent)
        ph = np.arctan2(l_state, c_state)
        am = np.hypot(c_state, l_state)
        full_ph = np.full(n_ang, np.nan)
        full_am = np.zeros(n_ang)
        full_ph[valid_idx] = ph
        full_am[valid_idx] = am
        w, rel = winding_from_phases(full_ph, full_am)
        if np.isfinite(w):
            pol_raw.append(w)
            pol_rel.append(rel)

    def _modal(raws):
        if not raws:
            return 0, 0
        ints = [int(round(abs(w))) for w in raws]
        return Counter(ints).most_common(1)[0]

    mt, ct = _modal(tor_raw)
    mp, cp = _modal(pol_raw)
    out["w_tor"] = mt
    out["w_pol"] = mp
    out["w_tor_modal_count"] = ct
    out["w_pol_modal_count"] = cp
    out["w_tor_raw_median"] = float(np.median([abs(w) for w in tor_raw])) if tor_raw else float("nan")
    out["w_pol_raw_median"] = float(np.median([abs(w) for w in pol_raw])) if pol_raw else float("nan")
    out["w_tor_rel"] = float(np.median(tor_rel)) if tor_rel else 0.0
    out["w_pol_rel"] = float(np.median(pol_rel)) if pol_rel else 0.0
    out["w_tor_raw_list"] = [round(w, 2) for w in tor_raw]
    out["w_pol_raw_list"] = [round(w, 2) for w in pol_raw]
    p, q = mt, mp
    out["crossing_c"] = min(p * (q - 1), q * (p - 1)) if (p >= 1 and q >= 1) else 0
    out["is_2_3"] = ((mt, mp) in [(2, 3), (3, 2)]) and (out["w_tor_rel"] > 0.1) and (out["w_pol_rel"] > 0.1)
    return out


# ──────────────────────────────────────────────────────────────────────────
# EQUIVALENCE GATE
# ──────────────────────────────────────────────────────────────────────────
_SCALAR_KEYS = (
    "w_tor",
    "w_pol",
    "w_tor_modal_count",
    "w_pol_modal_count",
    "w_tor_raw_median",
    "w_pol_raw_median",
    "w_tor_rel",
    "w_pol_rel",
    "crossing_c",
    "R",
    "r",
)


def _planted_2_3_field(N=52, R=None, r=None, amplitude=0.3, p=2, q=3):
    """Analytic (p,q) ω + π_ω on a torus shell — the SAME construction as
    ``CrystalGraftV2.seed_omega_known_2_3`` but stand-alone (no engine import), so
    this library has no `src/scripts` / heavy-engine dependency."""
    c = (N - 1) / 2.0
    if R is None:
        R = 0.22 * N
    if r is None:
        r = R / ((1.0 + np.sqrt(5.0)) / 2.0) ** 2  # R/φ²
    i, j, k = np.indices((N, N, N))
    xs, ys, zs = i - c, j - c, k - c
    rho = np.sqrt(xs**2 + ys**2)
    phi = np.arctan2(ys, xs)
    psi = np.arctan2(zs, rho - R)
    rtube = np.sqrt((rho - R) ** 2 + zs**2)
    env = np.exp(-(rtube**2) / (2.0 * (0.6 * r) ** 2)) * (rho > 2)
    beta = p * phi
    Theta = q * psi
    dR = np.cos(beta)
    dz = np.sin(beta)
    base = amplitude * env
    omega = np.zeros((N, N, N, 3))
    omega[..., 0] = base * np.cos(Theta) * dR * np.cos(phi)
    omega[..., 1] = base * np.cos(Theta) * dR * np.sin(phi)
    omega[..., 2] = base * np.cos(Theta) * dz
    delta = 0.4
    omega_prev = np.zeros((N, N, N, 3))
    omega_prev[..., 0] = base * np.cos(Theta + delta) * dR * np.cos(phi)
    omega_prev[..., 1] = base * np.cos(Theta + delta) * dR * np.sin(phi)
    omega_prev[..., 2] = base * np.cos(Theta + delta) * dz
    # π_ω = (ω - ω_prev)/dt ; dt scales C/L together ⇒ phase unaffected. Use 1.0.
    pi_omega = omega - omega_prev
    return omega, pi_omega, float(R), float(r)


def verify_equivalence(
    original_extract: Callable,
    *,
    N: int = 52,
    tol: float = 1e-12,
    n_ang: int = 240,
    n_walks: int = 12,
    seed: int = 12345,
    verbose: bool = True,
) -> Dict:
    """Assert the fast extractor reproduces ``original_extract`` to ``tol`` on a
    planted-(2,3), a null, and a random field.

    ``original_extract`` is INJECTED (signature
    ``f(omega, pi_omega, R, r, N, n_ang=, n_walks=)``) so this library never
    imports a driver script. Raises AssertionError on any divergence > tol;
    returns a per-field diff report on success."""
    rng = np.random.default_rng(seed)
    R0 = 0.22 * N
    r0 = R0 / ((1.0 + np.sqrt(5.0)) / 2.0) ** 2

    omega_p, pi_p, Rp, rp = _planted_2_3_field(N=N)
    null_omega = np.zeros((N, N, N, 3))
    null_pi = np.zeros((N, N, N, 3))
    rand_omega = rng.standard_normal((N, N, N, 3))
    rand_pi = rng.standard_normal((N, N, N, 3))

    cases = {
        "planted_2_3": (omega_p, pi_p, Rp, rp),
        "null": (null_omega, null_pi, R0, r0),
        "random": (rand_omega, rand_pi, R0, r0),
    }

    report: Dict[str, Dict] = {}
    for name, (om, pi, R, r) in cases.items():
        ref = original_extract(om, pi, R, r, N, n_ang=n_ang, n_walks=n_walks)
        fast = extract_2_3_omega_fast(om, pi, R, r, N, n_ang=n_ang, n_walks=n_walks)
        max_abs = 0.0
        worst = None
        for key in _SCALAR_KEYS:
            a, b = ref[key], fast[key]
            if a is None or b is None or (isinstance(a, float) and np.isnan(a) and np.isnan(b)):
                continue
            d = abs(float(a) - float(b))
            if d > max_abs:
                max_abs, worst = d, key
        # integer/topology fields must match EXACTLY
        for key in ("w_tor", "w_pol", "w_tor_modal_count", "w_pol_modal_count", "crossing_c"):
            assert ref[key] == fast[key], f"[{name}] integer field {key}: {ref[key]} != {fast[key]}"
        assert ref["is_2_3"] == fast["is_2_3"], f"[{name}] is_2_3 mismatch"
        assert ref["w_tor_raw_list"] == fast["w_tor_raw_list"], f"[{name}] w_tor_raw_list mismatch"
        assert ref["w_pol_raw_list"] == fast["w_pol_raw_list"], f"[{name}] w_pol_raw_list mismatch"
        assert max_abs <= tol, f"[{name}] scalar field '{worst}' diverged by {max_abs:.3e} > {tol:.0e}"
        report[name] = {
            "max_abs_diff": max_abs,
            "worst_field": worst,
            "w_tor": ref["w_tor"],
            "w_pol": ref["w_pol"],
            "is_2_3": ref["is_2_3"],
        }
        if verbose:
            print(
                f"  [{name:12s}] (w_tor,w_pol)=({ref['w_tor']},{ref['w_pol']}) "
                f"is_2_3={ref['is_2_3']} | max|Δ|={max_abs:.2e} "
                f"(worst={worst}) <= {tol:.0e}  OK",
                flush=True,
            )
    return report


if __name__ == "__main__":
    # Self-demonstrating gate: load the ORIGINAL extractor from the graft-v2
    # driver by file path (NOT a package import — the driver is a script) and
    # prove bit-equivalence. Run: python -m ave.utils.fast_winding_extractor
    import importlib.util
    from pathlib import Path

    drv = (
        Path(__file__).resolve().parents[2]
        / "scripts"
        / "vol_1_foundations"
        / "crystal_graft_v2_run.py"
    )
    spec = importlib.util.spec_from_file_location("crystal_graft_v2_run", drv)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print("EQUIVALENCE GATE — fast vs crystal_graft_v2_run.extract_2_3_omega")
    verify_equivalence(mod.extract_2_3_omega)
    print("GATE PASSED (planted / null / random, all fields ≤ 1e-12).")
