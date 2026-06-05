"""
Motion-stability via back-EMF — native Cosserat/dark-wake τ_zx on VacuumEngine3D.

Grant's hypothesis (stability FROM motion): the native τ_zx back-EMF of a MOVING
self-trap STABILIZES it — retention(v) slope > 0, stability gain tracking the
native τ_zx (positive), MORE than a linear (SM-counterfactual) control at matched
amplitude/saturation.

Canonical default CONTRADICTS: the saturated (2,3) self-trap is a static Γ=−1 knot;
at A²≈8.9 the core saturation S=√(1−A²) clamps to 0 ⇒ z_local at the rupture floor
⇒ c_eff = c·√S → 0 (frozen local clock). A frozen-core trap is PINNED: stable
because static, not via motion.

THIS engine is the real adjudication: the prior Maxwell-engine version (per brief)
saw only the E/H PROJECTION of τ_zx (anti-correlated −0.81); VacuumEngine3D's
DarkWakeObserver carries the NATIVE back-EMF stress τ_zx = z_local·∂_x(A²) directly
(K4 saturation-modulated impedance × strain gradient, vacuum_engine.py:1533).

Brief / prereg: _orchestration/motion-stability-bemf-cosserat.md
Result:        research/2026-06-04_motion-stability-bemf-cosserat-result.md

THE BOOST (the fix — replaces the failed port-pairing of the stalled run):
  The winding-extractor reads the quadrature phasor (ox, oy) = (V0+V1, V2+V3); the
  ansatz plants exactly this (ports {0,1}=cos(2φ+3ψ), {2,3}=sin(2φ+3ψ)). The boost
  rotates ox+i·oy by exp(i k_x x) — a +x spatial phase gradient applied COHERENTLY
  to the full phasor, redistributed onto the ports preserving intra-pair ratios.
  A genuine traveling-wave boost on the channel the winding lives in.

ANTI-STALL: validate the boost on a LINEAR (sub-saturation) pulse FIRST (≤2 boost
  variants). LINEAR moves → proceed; LINEAR does NOT move after 2 variants →
  BLOCKED-boost, write diagnosis, return.

FORWARD-PREDICTED SIGN (pre-run, no fit — ave-driver-script-honesty):
  substrate-default = PIN. LINEAR advects (c_eff≈c); SELF-TRAP does NOT
  (v_knot/v_linear ≪ 1); retention(v) flat-or-falling; native-τ_zx-vs-stability
  correlation ≤ 0. Predicted verdict: CONTRADICTS-via-PIN. A SUPPORTS overturns
  the static-trap canon and triggers full ave-discrimination-check.
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
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)                  # K4-TLM 4-port junction timestep

# Host (Arm-C) geometry — the confirmed durable host (retention ~0.88–0.91, peak A²≈8.9)
HOST_R_FRAC = 0.22                       # R_shell = 0.22·N
HOST_AMP = 0.40                          # peak A²_interior ≈ 8.9 during evolution

# FORWARD-PREDICTED SIGN (no fit). The substrate default at A²≈8.9 (S=0, c_eff→0).
FORWARD_PREDICTED_VERDICT = "CONTRADICTS-via-PIN"
FORWARD_PREDICTED_SIGN = {
    "linear_moves": True,
    "knot_moves": False,
    "retention_slope_sign": "<= 0 (flat or falling)",
    "tau_zx_vs_stability_corr_sign": "<= 0",
}


# ══════════════════════════════════════════════════════════════════════════════
# Engine + host (confirmed config — reused verbatim from
# r10_vacuumengine3d_transverse_2_3_emergence.py:setup_engine / Arm-C)
# ══════════════════════════════════════════════════════════════════════════════
def setup_engine(N, PML):
    """A28-corrected coupled VacuumEngine3D (doc 67 §15 + r10_v8 config)."""
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
    holds retention ~0.88–0.91 at peak A²≈8.9. R = 0.22·N, r = R/φ²."""
    R = HOST_R_FRAC * N
    r = R / (PHI**2)
    initialize_2_3_voltage_ansatz(engine.k4, R=R, r=r, amplitude=amplitude)
    return R, r


def _interior_mask(N, PML):
    m = np.zeros((N, N, N), dtype=bool)
    m[PML : N - PML, PML : N - PML, PML : N - PML] = True
    return m


# ══════════════════════════════════════════════════════════════════════════════
# THE BOOST — coherent phasor traveling wave on (ox, oy) = (V0+V1, V2+V3)
# ══════════════════════════════════════════════════════════════════════════════
def apply_coherent_phasor_boost(engine, k_x, x_c=None):
    """Rotate the winding phasor ox+i·oy by exp(i k_x x) at every active site,
    where ox = V0+V1 (ports {0,1}, +x hemisphere) and oy = V2+V3 (ports {2,3},
    −x hemisphere). The full phasor is rotated COHERENTLY (a +x spatial phase
    gradient = a genuine +x traveling-wave boost on the channel the (2,3) winding
    lives in), then redistributed onto the ports preserving each pair's intra-pair
    ratio. NOT the port-pairs (the stalled run showed port-pairing is not a clean
    traveling wave).

    k_x: +x phase gradient (rad/cell). 0 → identity (no boost).
    x_c: phase reference plane (defaults to lattice center).
    """
    if k_x == 0.0:
        return
    N = engine.N
    if x_c is None:
        x_c = (N - 1) / 2.0
    V = engine.k4.V_inc
    xi = np.arange(N, dtype=float)[:, None, None]
    alpha = k_x * (xi - x_c)                      # (N,1,1) per-x rotation angle
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    ox = V[..., 0] + V[..., 1]
    oy = V[..., 2] + V[..., 3]
    ox_new = ca * ox - sa * oy
    oy_new = sa * ox + ca * oy
    # redistribute preserving intra-pair ratios: scale pair {0,1} by ox_new/ox,
    # pair {2,3} by oy_new/oy. Guard the near-zero-magnitude denominator.
    eps = 1e-12
    s01 = np.where(np.abs(ox) > eps, ox_new / np.where(np.abs(ox) > eps, ox, 1.0), 0.0)
    s23 = np.where(np.abs(oy) > eps, oy_new / np.where(np.abs(oy) > eps, oy, 1.0), 0.0)
    # where the pair sum was ~0 but the rotation wants nonzero, split evenly
    born01 = (np.abs(ox) <= eps) & (np.abs(ox_new) > eps)
    born23 = (np.abs(oy) <= eps) & (np.abs(oy_new) > eps)
    V[..., 0] = np.where(born01, 0.5 * ox_new, V[..., 0] * s01)
    V[..., 1] = np.where(born01, 0.5 * ox_new, V[..., 1] * s01)
    V[..., 2] = np.where(born23, 0.5 * oy_new, V[..., 2] * s23)
    V[..., 3] = np.where(born23, 0.5 * oy_new, V[..., 3] * s23)
    V[~engine.k4.mask_active] = 0.0


# ══════════════════════════════════════════════════════════════════════════════
# LINEAR (sub-saturation) pulse — the SM-counterfactual + the boost smoke test
# ══════════════════════════════════════════════════════════════════════════════
def seed_linear_pulse(engine, N, PML, peak_A2_target=0.5 * A2_OP14):
    """Sub-saturation, ZERO-CARRIER phasor blob with the (ox,oy)=(V0+V1,V2+V3)
    quadrature structure of the host winding, localized and BELOW A²_op14 (no
    self-trap). ZERO carrier (ox=env real, oy=0) so the one-shot coherent boost
    `exp(i k_x x)` imprints a CLEAN momentum (group velocity) with v=0 at k=0 — the
    SM-counterfactual + the boost smoke test. (A pre-existing standing carrier
    washes out the imprinted momentum; verified — the zero-carrier blob advects
    cleanly and sign-symmetrically.) Amplitude scaled so peak A² ≈ peak_A2_target
    (sub-saturation; default = ½·A²_op14)."""
    cx = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N), dtype=float)
    r2 = (i - cx) ** 2 + (j - cx) ** 2 + (k - cx) ** 2
    sigma = max(2.5, 0.10 * N)
    env = np.exp(-r2 / (2.0 * sigma**2))
    V = engine.k4.V_inc
    V[..., 0] = env       # zero-carrier: ox = V0+V1 = 2·env (real), oy = V2+V3 = 0
    V[..., 1] = env
    V[..., 2] = 0.0
    V[..., 3] = 0.0
    V[~engine.k4.mask_active] = 0.0
    # scale to the sub-saturation target peak A²
    A2 = np.sum(V**2, axis=-1) / engine.V_SNAP**2
    m = _interior_mask(N, PML)
    cur = float(A2[m].max())
    if cur > 0:
        scale = np.sqrt(peak_A2_target / cur)
        V *= scale
    return float(np.sum((np.sum(V**2, axis=-1) / engine.V_SNAP**2)[m]))


# ══════════════════════════════════════════════════════════════════════════════
# Observables
# ══════════════════════════════════════════════════════════════════════════════
def a2_field(engine):
    return np.sum(engine.k4.V_inc**2, axis=-1) / engine.V_SNAP**2


def x_centroid(engine, PML, weight_floor=0.0):
    """Energy-weighted x-centroid over the interior (A² weighting). The motion
    observable. Returns (centroid_x, total_interior_energy)."""
    N = engine.N
    A2 = a2_field(engine)
    m = _interior_mask(N, PML) & engine.k4.mask_active
    w = np.where(m, A2, 0.0)
    if weight_floor > 0:
        w = np.where(w >= weight_floor * w.max(), w, 0.0)
    tot = float(w.sum())
    if tot <= 0:
        return float("nan"), 0.0
    xi = np.arange(N, dtype=float)[:, None, None]
    cx = float((w * xi).sum() / tot)
    return cx, tot


def x_fwhm(engine, PML):
    """FWHM of the interior A² profile projected onto x (localization width)."""
    N = engine.N
    A2 = a2_field(engine)
    m = _interior_mask(N, PML) & engine.k4.mask_active
    prof = np.where(m, A2, 0.0).sum(axis=(1, 2))
    if prof.max() <= 0:
        return float("nan")
    half = 0.5 * prof.max()
    idx = np.where(prof >= half)[0]
    if len(idx) < 2:
        return float(DT)  # sub-cell
    return float(idx[-1] - idx[0] + 1)


def smoke_test_boost(N=40, PML=4, n_steps=60, k_list=(0.0, 0.15, 0.30)):
    """ANTI-STALL smoke test: seed a zero-carrier LINEAR sub-saturation pulse,
    apply the ONE-SHOT coherent boost exp(i k_x x), confirm the centroid MOVES
    (monotone, sign-symmetric, v=0 at k=0). Returns per-k_x velocity.

    The boost is a ONE-SHOT momentum imprint (the physical traveling-wave boost);
    a re-imposed-every-step variant is a sustained PUMP (injects energy → blows up
    the field) and is NOT a clean boost — rejected (verified: overflow). The
    one-shot phasor rotation is the genuine `rotate ox+i·oy by exp(i k_x x)` boost.
    """
    out = {"per_kx": []}
    for k_x in k_list:
        engine = setup_engine(N, PML)
        seed_linear_pulse(engine, N, PML)
        apply_coherent_phasor_boost(engine, k_x)   # one-shot momentum imprint
        cx0, e0 = x_centroid(engine, PML)
        traj = [(0.0, cx0, e0)]
        for s in range(n_steps):
            engine.step()
            if (s + 1) % 5 == 0:
                cx, e = x_centroid(engine, PML)
                traj.append(((s + 1) * DT, cx, e))
        ts = np.array([t for (t, c, e) in traj if not np.isnan(c)])
        cs = np.array([c for (t, c, e) in traj if not np.isnan(c)])
        v = float(np.polyfit(ts, cs, 1)[0]) if len(ts) >= 2 else float("nan")
        out["per_kx"].append({
            "k_x": k_x, "v_centroid": v,
            "cx_start": float(cs[0]) if len(cs) else float("nan"),
            "cx_end": float(cs[-1]) if len(cs) else float("nan"),
            "dx_total": float(cs[-1] - cs[0]) if len(cs) >= 2 else float("nan"),
        })
    vs = [abs(d["v_centroid"]) for d in out["per_kx"]]
    # MOVES: v at largest k meaningfully exceeds the k=0 (≈static) value
    out["moves"] = bool(vs[-1] > 5.0 * (vs[0] + 1e-6) and vs[-1] > 1e-3)
    out["monotone"] = bool(vs[-1] >= vs[1] - 1e-9 >= vs[0] - 1e-9)
    out["v0_is_zero"] = bool(vs[0] < 1e-3)
    return out


if __name__ == "__main__":
    print("=" * 80, flush=True)
    print("  SMOKE TEST — does the one-shot coherent phasor boost ADVECT a LINEAR pulse?")
    print("=" * 80, flush=True)
    print(f"  ALPHA={ALPHA} A²_op14={A2_OP14:.4f} (ave-canonical-source) | dt={DT:.4f}")
    print(f"  FORWARD-PREDICTED: {FORWARD_PREDICTED_VERDICT} | {FORWARD_PREDICTED_SIGN}")
    t0 = time.time()
    res = smoke_test_boost(k_list=(0.0, 0.15, 0.30, -0.30))
    for d in res["per_kx"]:
        print(f"    k_x={d['k_x']:+.2f}: v_centroid={d['v_centroid']:+.4f} cell/τ "
              f"dx_total={d['dx_total']:+.3f} (cx {d['cx_start']:.2f}→{d['cx_end']:.2f})")
    print(f"    MOVES={res['moves']} MONOTONE={res['monotone']} v0≈0={res['v0_is_zero']} "
          f"({time.time()-t0:.0f}s)")
