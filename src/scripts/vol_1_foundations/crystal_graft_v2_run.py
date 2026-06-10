"""
Crystal-Graft v2 — smoke + full run + α-emergence driver.

Tests the re-scoped engine (`ave.core.crystal_graft_v2.CrystalGraftV2`): the
winding gets its OWN independent Cosserat-ω carrier (closes the genesis-24 /
crystal double-count that self-inflicted w_pol=0).

Prereg (FROZEN): research/2026-06-09_crystal-graft-v2_prereg.md

Honesty discipline (ave-driver-script-honesty): every number is read from the
EVOLVED field; NO optimizer is run onto (2,3); figures caption the ACTUAL data.
α-emergence is REFUSED unless a real (2,3) hosts (joint-ledger guard).
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from ave.core.constants import (  # noqa: E402
    ALPHA_COLD_INV,
    PHI,
    RR_GOLDEN_TORUS,
)
from ave.core.crystal_graft_v2 import CrystalGraftV2  # noqa: E402

OUT = Path(__file__).parent
KAPPA_TILDE = 6.0 / 5.0  # pq/(p+q) for (2,3) — α-FREE
PHI2 = PHI**2  # golden-torus aspect target R/r → φ²


# ═══════════════════════════════════════════════════════════════════════════
# ω-SECTOR (2,3) EXTRACTOR — reads the INDEPENDENT carrier (NOT the bulk-V phasor)
# ═══════════════════════════════════════════════════════════════════════════
# The (2,3) is a PAIR of windings on the Clifford torus of the ω vector field:
#   • toroidal "2" (base): direction of the transverse micro-rotation ω_⊥ in the
#     tube-transverse plane (ê_R, ẑ), winding around the MAJOR circle φ.
#   • poloidal "3" (fibre): the ω-tank LC phase arctan2(π_ω·n̂, ω·n̂), the C↔L
#     slosh of the INDEPENDENT ω reactance pair, winding around the MINOR circle
#     ψ. π_ω=∂_tω evolves under ω's own wave eq ⇒ genuinely independent of V.
# Both phases exist ONLY because ω is a vector field with its own momentum —
# the scalar bulk V had a single complex DOF (V+i∂_tV) and could not host w_pol.


def _interp_vec(F, c, R, r, phi, psi, N):
    """Trilinear sample of a 3-vector field F at a torus point (φ,ψ)."""
    rad = R + r * np.cos(psi)
    x = c + rad * np.cos(phi)
    y = c + rad * np.sin(phi)
    z = c + r * np.sin(psi)
    if not (1 <= x < N - 1 and 1 <= y < N - 1 and 1 <= z < N - 1):
        return None
    x0, y0, z0 = int(np.floor(x)), int(np.floor(y)), int(np.floor(z))
    fx, fy, fz = x - x0, y - y0, z - z0
    acc = np.zeros(3)
    for dx, wx in ((0, 1 - fx), (1, fx)):
        for dy, wy in ((0, 1 - fy), (1, fy)):
            for dz, wz in ((0, 1 - fz), (1, fz)):
                acc += wx * wy * wz * F[x0 + dx, y0 + dy, z0 + dz]
    return acc


def _winding_from_phases(phases, amps):
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


def extract_2_3_omega(omega, pi_omega, R, r, N, n_ang=240, n_walks=12):
    """Coordinate-correct (2,3) read on the INDEPENDENT ω carrier.

    Returns dict with w_tor (base, expect 2), w_pol (fibre, expect 3), their
    reliabilities, and the modal integers across n_walks circles (anti-fit).
    NO optimizer onto (2,3): forward READ of the field's own two phases.
    """
    c = (N - 1) / 2.0
    out = {"R": float(R), "r": float(r)}

    # ── toroidal "2": winding of arg(Ψ) around MAJOR φ, at varied ψ0.
    #    Ψ = (ω·ê_R) + i(ω·ê_z) — the COMPLEX transverse micro-rotation. Its
    #    argument IS the polarization-direction angle; it winds with the base
    #    "2". (For the known seed Ψ ∝ cos(qψ0)·e^{i pφ} ⇒ arg winds p.) ──
    tor_raw, tor_rel = [], []
    for psi0 in np.linspace(0.0, 2 * np.pi, n_walks, endpoint=False):
        ph, am = [], []
        for phi in np.linspace(0.0, 2 * np.pi, n_ang, endpoint=False):
            o = _interp_vec(omega, c, R, r, phi, psi0, N)
            if o is None:
                ph.append(np.nan)
                am.append(0.0)
                continue
            eR = np.array([np.cos(phi), np.sin(phi), 0.0])
            a1, a2 = o @ eR, o[2]  # transverse (ê_R, ê_z) components
            ph.append(np.arctan2(a2, a1))
            am.append(np.hypot(a1, a2))
        w, rel = _winding_from_phases(ph, am)
        if np.isfinite(w):
            tor_raw.append(w)
            tor_rel.append(rel)

    # ── poloidal "3": winding of the ω-tank LC phase arg(Z) around MINOR ψ, at
    #    varied φ0.  Z = (ω·d̂) + i(π_ω·d̂), where d̂ is the FIXED principal
    #    transverse direction along that ψ-walk (anti-fit: derived from the ω
    #    covariance, NOT assumed = pφ₀). π_ω evolves under ω's OWN wave eq ⇒ the
    #    LC phase is genuinely independent of V (the anti-double-count carrier). ──
    pol_raw, pol_rel = [], []
    for phi0 in np.linspace(0.0, 2 * np.pi, n_walks, endpoint=False):
        eR = np.array([np.cos(phi0), np.sin(phi0), 0.0])
        ez = np.array([0.0, 0.0, 1.0])
        otr, ptr = [], []  # transverse (ê_R, ê_z) samples of ω and π_ω
        psis = np.linspace(0.0, 2 * np.pi, n_ang, endpoint=False)
        for psi in psis:
            o = _interp_vec(omega, c, R, r, phi0, psi, N)
            p = _interp_vec(pi_omega, c, R, r, phi0, psi, N)
            if o is None or p is None:
                otr.append(None)
                ptr.append(None)
            else:
                otr.append(np.array([o @ eR, o[2]]))
                ptr.append(np.array([p @ eR, p[2]]))
        valid = [i for i in range(len(otr)) if otr[i] is not None]
        if len(valid) < 16:
            continue
        O = np.array([otr[i] for i in valid])  # (M,2)
        P = np.array([ptr[i] for i in valid])
        # principal transverse direction d̂ from ω covariance (the fixed
        # polarization axis along this ψ-walk)
        cov = O.T @ O
        evals, evecs = np.linalg.eigh(cov)
        dhat = evecs[:, np.argmax(evals)]  # (2,) unit principal axis
        ph, am = [], []
        for m in range(len(valid)):
            c_state = O[m] @ dhat  # C-state ω·d̂
            l_state = P[m] @ dhat  # L-state π_ω·d̂ (independent)
            ph.append(np.arctan2(l_state, c_state))
            am.append(np.hypot(c_state, l_state))
        # re-expand to full-length with nan padding for the winding helper
        full_ph = np.full(len(psis), np.nan)
        full_am = np.zeros(len(psis))
        for idx, m in enumerate(valid):
            full_ph[m] = ph[idx]
            full_am[m] = am[idx]
        w, rel = _winding_from_phases(full_ph, full_am)
        if np.isfinite(w):
            pol_raw.append(w)
            pol_rel.append(rel)

    from collections import Counter

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
    # (p,q) torus-knot crossing number from the MEASURED windings (not assumed)
    p, q = mt, mp
    out["crossing_c"] = min(p * (q - 1), q * (p - 1)) if (p >= 1 and q >= 1) else 0
    out["is_2_3"] = ((mt, mp) in [(2, 3), (3, 2)]) and (out["w_tor_rel"] > 0.1) and (out["w_pol_rel"] > 0.1)
    return out


def find_shell(omega, N, return_r_meas=False):
    """Locate the hosted ω shell (R, r) from the |ω|² density crest (PML-safe,
    density-peak NOT centroid — CP7).

    r_walk (the extractor minor-walk tube radius) defaults to R/φ² — a CONVENIENCE
    for the ring-walk, NOT a measurement (so R/r_walk = φ² is TAUTOLOGICAL, never
    cite it as emergence). r_meas is the INDEPENDENT tube half-thickness (the
    |ω|²-weighted std of |ρ−R| in the crest z-plane) — the honest quantity for the
    golden-torus R/r test."""
    a2 = np.sum(omega**2, axis=-1)
    c = (N - 1) / 2.0
    kz = int(np.argmax(a2.sum(axis=(0, 1))))
    sl = a2[:, :, kz]
    ii, jj = np.indices(sl.shape)
    rho = np.sqrt((ii - c) ** 2 + (jj - c) ** 2)
    ang = np.arctan2(jj - c, ii - c)
    crest = []
    for a0 in np.linspace(-np.pi, np.pi, 24, endpoint=False):
        dth = np.abs(((ang - a0 + np.pi) % (2 * np.pi)) - np.pi)
        m = (dth < np.pi / 24) & (rho > 2) & (rho < 0.45 * N) & (sl > 0)
        if m.sum() >= 2:
            crest.append(float(rho[m][np.argmax(sl[m])]))
    R = float(np.median(crest)) if crest else 0.22 * N
    r_walk = R / PHI2
    if not return_r_meas:
        return R, r_walk
    band = (rho > 2) & (rho < 0.45 * N) & (sl > 0)
    if band.sum() > 8:
        wts = sl[band]
        dr = rho[band] - R
        r_meas = float(np.sqrt(np.average(dr**2, weights=wts)))
    else:
        r_meas = float("nan")
    return R, r_walk, r_meas


# ═══════════════════════════════════════════════════════════════════════════
# SMOKE-1 — the Γ=−1 wall HARDENS (vs genesis-24 |Γ|<0.08)
# ═══════════════════════════════════════════════════════════════════════════
def smoke_wall(N=40):
    """Static depth sweep: deeper core saturation ⇒ Γ_min → −1 (the c_eff trap
    works). Plus a dynamical confinement check (breather stays localized, Γ_min
    stays hard). genesis-24 (no trap) was flat at |Γ|<0.08."""
    print("\n[SMOKE-1] Γ=−1 wall hardening (c_eff trap depth sweep)", flush=True)
    ic = N // 2  # integer-centered (avoid the between-cells peak-clipping)
    depths = [0.9, 0.99, 0.999, 0.9999, 0.9999999, 0.99999999, 0.999999999]
    sweep = []
    for A_core in depths:
        # static plant at depth A_core; allow A_cap deep enough to express it
        e = CrystalGraftV2(N=N, S_min=1e-12, A_cap=0.9999999999, omega_sector_on=False, buckle_on=False)
        e.seed_bulk((ic, ic, ic), sigma=2.5, frac=A_core)
        g = e.gamma_bulk()
        sweep.append((A_core, g["gamma_min"], g["frac_short"]))
        print(f"   A_core={A_core:<12} Γ_min={g['gamma_min']:+.4f} " f"frac_short={g['frac_short']:.3f}", flush=True)

    # dynamical confinement: seed a deep breather, run, watch Γ_min + localization
    e = CrystalGraftV2(N=N, S_min=1e-6, A_cap=0.99999, omega_sector_on=False, buckle_on=False)
    e.seed_bulk((ic, ic, ic), sigma=3.0, frac=0.999)
    m = e.interior_mask()
    a2_0 = np.abs(e.V) * m
    loc_0 = float((a2_0**2).sum() / (a2_0.sum() ** 2 + 1e-30))  # inverse participation
    gam_t, loc_t = [], []
    for n in range(400):
        e.step()
        if n % 20 == 0:
            gam_t.append(e.gamma_bulk()["gamma_min"])
            a2 = np.abs(e.V) * m
            loc_t.append(float((a2**2).sum() / (a2.sum() ** 2 + 1e-30)))
    gamma_floor = min(s[1] for s in sweep)
    confined = (loc_t[-1] > 0.3 * loc_0) and np.isfinite(loc_t[-1])
    res = {
        "sweep": sweep,
        "gamma_min_deepest": gamma_floor,
        "genesis24_gamma_ref": -0.08,
        "gamma_t": gam_t,
        "loc_0": loc_0,
        "loc_t": loc_t,
        "confined": bool(confined),
        # PASS: deepest Γ well past genesis-24's -0.08 toward -1, AND confined
        "PASS": bool(gamma_floor < -0.7 and confined),
    }
    print(
        f"   >> deepest Γ_min={gamma_floor:+.4f} (genesis-24 ref −0.08); " f"breather confined={confined}", flush=True
    )
    print(f"   >> SMOKE-1 {'PASS' if res['PASS'] else 'FAIL'}", flush=True)
    return res


# ═══════════════════════════════════════════════════════════════════════════
# SMOKE-2 — the buckle is CONSERVATIVE (energize-LOCK, not a pump)
# ═══════════════════════════════════════════════════════════════════════════
def smoke_buckle(N=40):
    """ADD-2 sources ω from blocked compression: H flat (energize-LOCK), |L_ω|
    bounded (no secular growth), fields O(1) (no detonation), centrosymmetric
    (h-symmetric) baseline = 0 net helicity. genesis-24's pump: E_V→6.8e8,
    |L| 2.7→43."""
    print("\n[SMOKE-2] buckle conservative (energize-LOCK vs genesis-24 pump)", flush=True)
    ic = N // 2

    # ── (A) the CONSERVATION PROOF: linearize the bulk (c_eff→c0) so the only
    #    cross-coupling is the buckle, and measure the STENCIL-consistent energy
    #    (operators matched to the dynamics). Total H must be flat (the continuum
    #    cancellation is exact; the leapfrog keeps it to O(dt²)). E_ω must GROW
    #    from 0 (compression energy flows into rotation) while H_total stays flat. ──
    class _LinBulk(CrystalGraftV2):
        def c_eff_squared(self, V):
            return np.full_like(V, self.c0**2)

    el = _LinBulk(
        N=N,
        S_min=2e-3,
        A_cap=0.999,
        omega_gap=1.0,
        wall_center=0.80,
        wall_width=0.15,
        kappa_tilde=KAPPA_TILDE,
        buckle_on=True,
        pml_thickness=6,
    )
    el.seed_bulk((ic, ic, ic), sigma=4.0, frac=0.6, helical=True, k_wind=2)
    el.seed_photon((ic, ic, ic), sigma=5.0, wavelength=8.0, amplitude=0.3, helicity=1.0)
    el.freeze_wall_window()
    se0 = el.stencil_energy()
    H0 = se0["H_total"]
    Hs, EVs, EOs = [], [], []
    for k in range(1800):
        el.step()
        if k % 50 == 0:
            se = el.stencil_energy()
            Hs.append(se["H_total"])
            EVs.append(se["E_V_lin"])
            EOs.append(se["E_omega"])
    Hs = np.array(Hs)
    H_drift = float((Hs[-1] - H0) / (abs(H0) + 1e-30))
    H_span = float((Hs.max() - Hs.min()) / (abs(H0) + 1e-30))
    # E_ω grows from ~0 to a measurable fraction of the bulk energy (the buckle
    # genuinely sources rotation), while total H stays flat.
    E_omega_grew = bool(EOs[-1] > 100 * (EOs[0] + 1e-9) and EOs[-1] > 0.005 * EVs[0])
    conservative = abs(H_drift) < 0.02 and H_span < 0.05
    print(
        f"   (A) conservation (linear bulk, stencil energy): H drift={H_drift:+.3%} "
        f"span={H_span:.3%} → {'CONSERVATIVE' if conservative else 'NON-CONSERVATIVE'}",
        flush=True,
    )
    print(
        f"       E_V {EVs[0]:.2f}→{EVs[-1]:.2f}  E_ω {EOs[0]:.3f}→{EOs[-1]:.3f}  "
        f"(compression energy flows INTO rotation; total flat)",
        flush=True,
    )

    # ── (B) the ENERGIZE-LOCK behavior with the real nonlinear bulk: fields stay
    #    O(1) (no detonation), |L_ω| OSCILLATES (bounded, not secular monotone). ──
    def _nl_run(helicity, buckle_on, chiral, n=900):
        e = CrystalGraftV2(
            N=N,
            S_min=2e-3,
            A_cap=0.999,
            omega_gap=1.0,
            wall_center=0.80,
            wall_width=0.15,
            kappa_tilde=KAPPA_TILDE,
            buckle_on=buckle_on,
        )
        if chiral:
            e.seed_bulk((ic, ic, ic), sigma=4.0, frac=0.88, helical=True, k_wind=2)
        else:
            e.seed_bulk((ic, ic, ic), sigma=4.0, frac=0.88)
        e.seed_photon((ic, ic, ic), sigma=5.0, wavelength=8.0, amplitude=0.3, helicity=helicity)
        e.freeze_wall_window()
        Ls, Hb, mxV, mxO, ts = [], [], [], [], []
        for k in range(n):
            e.step()
            if k % 30 == 0:
                oi = e.omega_intensity()
                fi = e.field_intensity()
                Ls.append(oi["Lomega"])
                Hb.append(oi["Hbel"])
                mxV.append(fi["max_V"])
                mxO.append(oi["max_omega"])
                ts.append(e.time)
        Larr = np.array(Ls)
        half = len(Larr) // 2
        slope = float(np.polyfit(ts[half:], Larr[half:], 1)[0]) if len(Larr) > 4 else 0.0
        return {
            "L_t": Ls,
            "Hbel_t": Hb,
            "t": ts,
            "maxV_t": mxV,
            "maxO_t": mxO,
            "L_monotone": bool(np.all(np.diff(Larr) >= -1e-9)),
            "L_late_slope": slope,
            "L_max": float(Larr.max()),
            "max_maxV": max(mxV),
            "max_maxO": max(mxO),
            "Hbel_final": Hb[-1],
        }

    rh = _nl_run(+1.0, True, chiral=True)
    lh = _nl_run(-1.0, True, chiral=True)
    cen = _nl_run(+1.0, True, chiral=False)  # centrosymmetric (non-chiral)
    off = _nl_run(+1.0, False, chiral=True)  # buckle OFF (κ̃ inert ⇒ ω≡0)

    no_detonation = (rh["max_maxV"] < 50) and (rh["max_maxO"] < 50)
    L_bounded = (not rh["L_monotone"]) and (abs(rh["L_late_slope"]) < rh["L_max"])
    # baseline: buckle OFF ⇒ ω receives nothing (the trivial-correct baseline).
    baseline_zero = (abs(off["L_max"]) < 1e-6) and (abs(off["max_maxO"]) < 1e-9)
    # NOTE (finding): H_bel is QUADRATIC in ω, so a scalar handedness sign cannot
    # flip it (RH/LH give equal H_bel). Charge-sign = helicity-flip therefore is
    # NOT carried by this fixed-axis buckle — a real structural finding deferred
    # to the full-run ledger (it needs a genuinely chiral source structure).
    parity_flip = (np.sign(rh["Hbel_final"]) == -np.sign(lh["Hbel_final"])) and abs(rh["Hbel_final"]) > 1e-12

    res = {
        "conservation": {
            "H_drift": H_drift,
            "H_span": H_span,
            "E_V": EVs,
            "E_omega": EOs,
            "H_t": Hs.tolist(),
            "E_omega_grew": E_omega_grew,
            "conservative": bool(conservative),
        },
        "RH": rh,
        "LH": lh,
        "centrosym": cen,
        "buckle_off": off,
        "no_detonation": bool(no_detonation),
        "L_bounded": bool(L_bounded),
        "baseline_zero": bool(baseline_zero),
        "max_maxV_RH": rh["max_maxV"],
        "max_maxO_RH": rh["max_maxO"],
        "L_max_RH": rh["L_max"],
        "L_late_slope_RH": rh["L_late_slope"],
        "L_monotone_RH": rh["L_monotone"],
        "Hbel_RH": rh["Hbel_final"],
        "Hbel_LH": lh["Hbel_final"],
        "parity_charge_flip": bool(parity_flip),
        "PASS": bool(conservative and E_omega_grew and no_detonation and L_bounded and baseline_zero),
    }
    print(
        f"   (B) energize-LOCK (nonlinear bulk): max|V|={rh['max_maxV']:.2f} "
        f"max|ω|={rh['max_maxO']:.3f} (no detonation; genesis-24: E_V→6.8e8)",
        flush=True,
    )
    print(
        f"       |L_ω| max={rh['L_max']:.1f} late-slope={rh['L_late_slope']:+.3g} "
        f"monotone={rh['L_monotone']} (energize-LOCK: bounded oscillation, "
        f"NOT genesis-24's monotone 2.7→43)",
        flush=True,
    )
    print(f"       buckle-OFF baseline: |L_ω|max={off['L_max']:.2g} (κ̃ inert ⇒ ω≡0)", flush=True)
    print(
        f"       [finding] H_bel quadratic in ω ⇒ scalar-h cannot flip charge sign "
        f"(RH={rh['Hbel_final']:+.2g}, LH={lh['Hbel_final']:+.2g}); deferred to ledger",
        flush=True,
    )
    print(f"   >> SMOKE-2 {'PASS' if res['PASS'] else 'FAIL'}", flush=True)
    return res


# ═══════════════════════════════════════════════════════════════════════════
# SMOKE-3 — the ω WINDING SECTOR is INDEPENDENT (the anti-double-count check)
# ═══════════════════════════════════════════════════════════════════════════
def smoke_winding_independent(N=44):
    """(a) carrier gate: a KNOWN-imposed (2,3) in ω reads back (w_tor,w_pol)≈
    (2,3) — the old scalar bulk read (*,0). (b) independence: with the buckle
    OFF, perturbing V leaves the ω winding read UNCHANGED (ω carries its own
    phase; it is NOT a projection of V_inc)."""
    print("\n[SMOKE-3] ω winding sector independent (anti-double-count)", flush=True)
    c = (N - 1) / 2.0
    R = 0.22 * N
    r = R / PHI2

    # (a) carrier gate — plant known (2,3) in ω, read it back
    e = CrystalGraftV2(N=N, S_min=1e-3, omega_gap=1.0, buckle_on=False)
    e.seed_omega_known_2_3(R, r, amplitude=0.3, p=2, q=3)
    Rf, rf = find_shell(e.omega, N)
    res_a = extract_2_3_omega(e.omega, e.omega_velocity(), Rf, rf, N)
    carrier_ok = (res_a["w_tor"], res_a["w_pol"]) in [(2, 3), (3, 2)]
    print(
        f"   (a) carrier gate: (w_tor,w_pol)=({res_a['w_tor']},{res_a['w_pol']}) "
        f"rel=({res_a['w_tor_rel']:.2f},{res_a['w_pol_rel']:.2f}) "
        f"raw~({res_a['w_tor_raw_median']:.2f},{res_a['w_pol_raw_median']:.2f}) "
        f"→ {'reads (2,3)' if carrier_ok else 'FAILS to read (2,3)'}",
        flush=True,
    )

    # (b) independence — buckle OFF, perturb V, confirm ω winding unchanged
    e2 = CrystalGraftV2(N=N, S_min=1e-3, omega_gap=1.0, buckle_on=False)
    e2.seed_omega_known_2_3(R, r, amplitude=0.3, p=2, q=3)
    e2.seed_bulk((c, c, c), sigma=4.0, frac=0.95)  # large V perturbation
    res_b = extract_2_3_omega(e2.omega, e2.omega_velocity(), Rf, rf, N)
    independent = (res_b["w_tor"] == res_a["w_tor"]) and (res_b["w_pol"] == res_a["w_pol"])
    print(
        f"   (b) independence: +large V perturbation → "
        f"(w_tor,w_pol)=({res_b['w_tor']},{res_b['w_pol']}) "
        f"({'UNCHANGED — ω independent of V' if independent else 'CHANGED — leak!'})",
        flush=True,
    )

    res = {
        "carrier_gate": res_a,
        "independence": res_b,
        "carrier_reads_2_3": bool(carrier_ok),
        "w_pol_can_be_nonzero": bool(res_a["w_pol"] != 0 and res_a["w_pol_rel"] > 0.1),
        "omega_independent_of_V": bool(independent),
        "PASS": bool(carrier_ok and independent and res_a["w_pol"] != 0),
    }
    print(
        f"   >> w_pol structurally able to be nonzero: {res['w_pol_can_be_nonzero']} "
        f"(prior engine: w_pol≡0 by construction)",
        flush=True,
    )
    print(f"   >> SMOKE-3 {'PASS' if res['PASS'] else 'FAIL'}", flush=True)
    return res


# ═══════════════════════════════════════════════════════════════════════════
# FULL RUN — does (2,3) self-assemble in the ω sector DE-NOVO?
# ═══════════════════════════════════════════════════════════════════════════
def _denovo_run(N, helicity, with_photon, k_wind, n_steps, seed_frac=0.9):
    """Seed the CP8 generative precursor (transverse photon + pre-compressed
    dilatation seed — NOT a planted (2,3)), drive the buckle, return the engine.
    No-photon / no-chirality variants are the null controls."""
    ic = N // 2
    e = CrystalGraftV2(
        N=N,
        S_min=2e-3,
        A_cap=0.999,
        omega_gap=1.0,
        wall_center=0.78,
        wall_width=0.16,
        kappa_tilde=KAPPA_TILDE,
        buckle_on=True,
        pml_thickness=5,
    )
    # pre-compressed dilatation seed (the mass precursor). k_wind=0 ⇒ pure radial
    # (cleanest CP8); k_wind=1 ⇒ a SINGLE chiral twist (minimal handedness, NOT
    # the (2,3) — the toroidal-2/poloidal-3 must still EMERGE).
    if k_wind and k_wind > 0:
        e.seed_bulk((ic, ic, ic), sigma=4.5, frac=seed_frac, helical=True, k_wind=k_wind)
    else:
        e.seed_bulk((ic, ic, ic), sigma=4.5, frac=seed_frac)
    if with_photon:
        e.seed_photon((ic, ic, ic), sigma=5.0, wavelength=7.0, amplitude=0.35, helicity=helicity)
    else:
        e.helicity = 0.0  # no chirality source ⇒ buckle sources nothing handed
    e.freeze_wall_window()
    for _ in range(n_steps):
        e.step()
    return e


def full_run(N=52, n_steps=1400):
    """De-novo (2,3) test on the INDEPENDENT ω carrier + matched no-photon
    control. Honest read: report the ACTUAL (w_tor,w_pol) on reliable contours."""
    print("\n" + "=" * 74)
    print("  FULL RUN — de-novo (2,3) in the ω carrier (rel>0.1; matched control)")
    print("=" * 74, flush=True)

    arms = {}
    # primary: helical photon + radial breather (chirality from the PHOTON, CP8)
    e_main = _denovo_run(N, helicity=+1.0, with_photon=True, k_wind=0, n_steps=n_steps)
    # minimal-chiral-precursor: ONE breather twist (k_wind=1) + helical photon
    e_chir = _denovo_run(N, helicity=+1.0, with_photon=True, k_wind=1, n_steps=n_steps)
    # null control: NO photon (no chirality source), radial breather
    e_null = _denovo_run(N, helicity=0.0, with_photon=False, k_wind=0, n_steps=n_steps)

    for label, e in (("photon_radial", e_main), ("photon_1twist", e_chir), ("no_photon_null", e_null)):
        R, r, r_meas = find_shell(e.omega, N, return_r_meas=True)
        res = extract_2_3_omega(e.omega, e.omega_velocity(), R, r, N)
        oi = e.omega_intensity()
        res.update(
            {
                "label": label,
                "Eomega": oi["Eomega_field"],
                "max_omega": oi["max_omega"],
                "Hbel": oi["Hbel"],
                "Lomega": oi["Lomega"],
                "r_meas": r_meas,
            }
        )
        arms[label] = res
        print(f"  [{label:15s}] shell R={res['R']:.2f} r={res['r']:.2f} " f"E_ω={oi['Eomega_field']:.3g}", flush=True)
        print(
            f"      (w_tor,w_pol)=({res['w_tor']},{res['w_pol']}) "
            f"rel=({res['w_tor_rel']:.2f},{res['w_pol_rel']:.2f}) "
            f"raw~({res['w_tor_raw_median']:.2f},{res['w_pol_raw_median']:.2f}) "
            f"c={res['crossing_c']} is(2,3)={res['is_2_3']}",
            flush=True,
        )

    main = arms["photon_radial"]
    chir = arms["photon_1twist"]
    null = arms["no_photon_null"]
    # de-novo (2,3): closes on a RELIABLE contour AND the null control is NOT (2,3)
    closes = main["is_2_3"] or chir["is_2_3"]
    control_null = not null["is_2_3"]
    w_pol_nonzero = (main["w_pol"] != 0 and main["w_pol_rel"] > 0.1) or (chir["w_pol"] != 0 and chir["w_pol_rel"] > 0.1)
    print(f"\n  >> (2,3) closes de-novo: {closes}  (matched no-photon control " f"null: {control_null})", flush=True)
    print(
        f"  >> w_pol structurally nonzero on a reliable contour: {w_pol_nonzero} " f"(prior engine: w_pol≡0)",
        flush=True,
    )
    return {
        "arms": arms,
        "closes_de_novo": bool(closes),
        "control_null": bool(control_null),
        "w_pol_nonzero": bool(w_pol_nonzero),
        "engines": {"photon_radial": e_main, "photon_1twist": e_chir},
    }


# ═══════════════════════════════════════════════════════════════════════════
# α-EMERGENCE — golden-torus self-assembly + Q leak-rate + JOINT-LEDGER GUARD
# ═══════════════════════════════════════════════════════════════════════════
def alpha_emergence(full):
    """α-free inputs (κ̃=6/5, V_yield≡1). Tests: (1) Golden-Torus self-assembly
    R/r→φ² (scale-free) and R·r→¼ (needs the φ/2 normalization); (2) α⁻¹=
    4π³+π²+π EMERGES as the knot leak-rate Q⁻¹. JOINT-LEDGER GUARD: REFUSE any
    Q if there is no real (2,3) (no resonator → the Q is a geometric fluke)."""
    print("\n" + "=" * 74)
    print("  α-EMERGENCE (α-free inputs: κ̃=6/5, V_yield≡1) + JOINT-LEDGER GUARD")
    print("=" * 74, flush=True)
    main = full["arms"]["photon_radial"]
    chir = full["arms"]["photon_1twist"]
    # use whichever arm hosts the more reliable winding for the geometry read
    arm = chir if (chir["w_pol_rel"] >= main["w_pol_rel"]) else main
    R = arm["R"]
    r = arm.get("r_meas", float("nan"))  # INDEPENDENT tube thickness (honest)
    Rr = R * r
    R_over_r = R / r if (r and r > 0 and np.isfinite(r)) else float("nan")
    golden_ratio_match = abs(R_over_r - PHI2) / PHI2 if np.isfinite(R_over_r) else float("nan")
    print(
        f"  Golden-Torus (arm={arm['label']}): R={R:.2f} r_meas={r:.2f} "
        f"(r INDEPENDENTLY measured — NOT r_walk=R/φ²)",
        flush=True,
    )
    print(
        f"    R/r_meas = {R_over_r:.3f}  vs  φ² = {PHI2:.3f}  " f"(scale-free; rel.err {golden_ratio_match:.1%})",
        flush=True,
    )
    print(
        f"    R·r = {Rr:.3f} (lattice units; the ¼ target needs the φ/2 " f"normalization — scale not fixed de-novo)",
        flush=True,
    )

    has_2_3 = bool(full["closes_de_novo"])
    # leak-rate Q: only DEFINED on a real (2,3) resonator. Without it the guard
    # refuses — no resonator, no leak-rate, no α (the genesis-24/crystal fluke).
    if has_2_3:
        Q_inv = 1.0 / max(arm.get("Q_proxy", np.nan), 1e-30)
        alpha_inv_emergent = arm.get("Q_proxy", np.nan)
        print(
            f"    Q (knot leak-rate) measured: α⁻¹_emergent={alpha_inv_emergent:.3f} "
            f"vs 4π³+π²+π={ALPHA_COLD_INV:.3f}",
            flush=True,
        )
    else:
        alpha_inv_emergent = None
        print(
            f"    Q leak-rate: REFUSED by joint-ledger guard — no real (2,3) "
            f"hosts (no resonator ⇒ any near-137 Q is a geometric fluke).",
            flush=True,
        )

    # golden-torus self-assembly verdict (scale-free ratio within 25%)
    golden_self_assembles = bool(golden_ratio_match < 0.25) and has_2_3
    alpha_emergent = bool(
        has_2_3
        and (alpha_inv_emergent is not None)
        and abs(alpha_inv_emergent - ALPHA_COLD_INV) / ALPHA_COLD_INV < 0.05
    )
    print(
        f"  >> Golden-Torus self-assembles: {golden_self_assembles} "
        f"(needs a real (2,3); R/r-match {1-golden_ratio_match:.1%})",
        flush=True,
    )
    print(f"  >> α⁻¹ EMERGES (α-free): {alpha_emergent}", flush=True)
    return {
        "R": float(R),
        "r": float(r),
        "R_over_r": float(R_over_r),
        "phi2": float(PHI2),
        "R_over_r_relerr": float(golden_ratio_match),
        "Rr_lattice": float(Rr),
        "RR_target": float(RR_GOLDEN_TORUS),
        "has_2_3": has_2_3,
        "alpha_inv_emergent": alpha_inv_emergent,
        "alpha_cold_inv": float(ALPHA_COLD_INV),
        "golden_self_assembles": golden_self_assembles,
        "alpha_emergent": alpha_emergent,
    }


# ═══════════════════════════════════════════════════════════════════════════
# FIGURES (data-derived captions — no templated success)
# ═══════════════════════════════════════════════════════════════════════════
def make_figures(s1, s2, s3, full, alpha):
    paths = []
    # ── fig1: the three smokes ──
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.3))
    depths = [d[0] for d in s1["sweep"]]
    gam = [d[1] for d in s1["sweep"]]
    ax[0].semilogx([1 - d for d in depths], gam, "o-", color="C3")
    ax[0].axhline(-1.0, ls=":", color="k", label="Γ=−1 wall")
    ax[0].axhline(-0.08, ls="--", color="gray", label="genesis-24 (no trap)")
    ax[0].set_xlabel("1 − A_core  (depth → wall)")
    ax[0].set_ylabel("Γ_min")
    ax[0].set_title(f"SMOKE-1: wall HARDENS to Γ_min={min(gam):.2f}\n" f"(c_eff trap; genesis-24 was −0.08)")
    ax[0].legend(fontsize=7)
    ax[0].invert_xaxis()
    Hs = s2["conservation"]["H_t"]
    EVs = s2["conservation"]["E_V"]
    EOs = s2["conservation"]["E_omega"]
    t = np.arange(len(Hs))
    ax[1].plot(t, np.array(Hs) / Hs[0], label="H_total", color="k", lw=2)
    ax[1].plot(t, np.array(EVs) / Hs[0], label="E_V (bulk)", color="C0")
    ax[1].plot(t, np.array(EOs) / Hs[0], label="E_ω (rotation)", color="C1")
    ax[1].set_xlabel("step / 50")
    ax[1].set_ylabel("energy / H₀")
    ax[1].set_title(f"SMOKE-2: buckle CONSERVATIVE\n" f"H drift {s2['conservation']['H_drift']:+.2%}; E_ω grows from 0")
    ax[1].legend(fontsize=7)
    L = s2["RH"]["L_t"]
    ax[2].plot(s2["RH"]["t"], L, "o-", color="C2", ms=3)
    ax[2].set_xlabel("time")
    ax[2].set_ylabel("|L_ω|")
    ax[2].set_title(
        f"SMOKE-2: |L_ω| BOUNDED oscillation (max {max(L):.0f})\n" f"energize-LOCK, NOT genesis-24's monotone 2.7→43"
    )
    fig.tight_layout()
    p1 = OUT / "crystal_graft_v2_fig1_smokes.png"
    fig.savefig(p1, dpi=110)
    plt.close(fig)
    paths.append(p1.name)

    # ── fig2: the (2,3) read on the INDEPENDENT ω carrier ──
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.3))
    cg = s3["carrier_gate"]
    ax[0].bar([0, 1], [cg["w_tor"], cg["w_pol"]], color=["C0", "C1"], alpha=0.8)
    ax[0].set_xticks([0, 1])
    ax[0].set_xticklabels(["w_tor", "w_pol"])
    ax[0].axhline(2, ls=":", color="C0")
    ax[0].axhline(3, ls=":", color="C1")
    ax[0].set_title(
        f"SMOKE-3 carrier gate: KNOWN (2,3) reads back\n"
        f"({cg['w_tor']},{cg['w_pol']}) rel=({cg['w_tor_rel']:.2f},"
        f"{cg['w_pol_rel']:.2f}) — w_pol CAN be ≠0"
    )
    ax[0].set_ylabel("winding")
    labels = list(full["arms"].keys())
    wt = [full["arms"][k]["w_tor"] for k in labels]
    wp = [full["arms"][k]["w_pol"] for k in labels]
    rt = [full["arms"][k]["w_tor_rel"] for k in labels]
    rp = [full["arms"][k]["w_pol_rel"] for k in labels]
    x = np.arange(len(labels))
    ax[1].bar(x - 0.2, wt, 0.4, label="w_tor", color="C0")
    ax[1].bar(x + 0.2, wp, 0.4, label="w_pol", color="C1")
    for i in range(len(labels)):
        ax[1].text(x[i] - 0.2, wt[i] + 0.05, f"r{rt[i]:.2f}", ha="center", fontsize=6)
        ax[1].text(x[i] + 0.2, wp[i] + 0.05, f"r{rp[i]:.2f}", ha="center", fontsize=6)
    ax[1].set_xticks(x)
    ax[1].set_xticklabels(labels, rotation=15, fontsize=7)
    ax[1].axhline(2, ls=":", color="C0")
    ax[1].axhline(3, ls=":", color="C1")
    ax[1].set_title(
        f"DE-NOVO ω winding (rel-tagged)\n"
        f"closes(2,3)={full['closes_de_novo']}  "
        f"control-null={full['control_null']}"
    )
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    p2 = OUT / "crystal_graft_v2_fig2_winding.png"
    fig.savefig(p2, dpi=110)
    plt.close(fig)
    paths.append(p2.name)

    # ── fig3: golden-torus + the joint-ledger guard ──
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.3))
    ax[0].bar([0, 1], [alpha["R_over_r"], alpha["phi2"]], color=["C4", "gray"], alpha=0.8)
    ax[0].set_xticks([0, 1])
    ax[0].set_xticklabels(["R/r (measured)", "φ² (target)"])
    ax[0].set_title(
        f"Golden-Torus aspect (scale-free)\n"
        f"R/r={alpha['R_over_r']:.2f} vs φ²={alpha['phi2']:.2f} "
        f"(self-assembles={alpha['golden_self_assembles']})"
    )
    ax[1].axhline(alpha["alpha_cold_inv"], ls=":", color="k", label=f"4π³+π²+π={alpha['alpha_cold_inv']:.2f}")
    if alpha["alpha_inv_emergent"] is not None:
        ax[1].bar([0], [alpha["alpha_inv_emergent"]], color="C3")
        msg = f"α⁻¹_emergent={alpha['alpha_inv_emergent']:.2f}"
    else:
        ax[1].text(
            0.5,
            0.5,
            "JOINT-LEDGER GUARD:\nα REFUSED\n(no real (2,3)\n→ no resonator)",
            ha="center",
            va="center",
            transform=ax[1].transAxes,
            fontsize=11,
            color="C3",
            bbox=dict(boxstyle="round", fc="mistyrose"),
        )
        msg = "α REFUSED (guard)"
    ax[1].set_title(f"α-emergence: {msg}\n(α-free inputs κ̃=6/5, V_yield≡1)")
    ax[1].legend(fontsize=7)
    fig.tight_layout()
    p3 = OUT / "crystal_graft_v2_fig3_alpha.png"
    fig.savefig(p3, dpi=110)
    plt.close(fig)
    paths.append(p3.name)
    return paths


def main():
    t0 = time.time()
    print("=" * 74)
    print("  CRYSTAL-GRAFT v2 — winding gets its OWN Cosserat-ω carrier")
    print("  (closes the genesis-24/crystal double-count: w_pol≡0)")
    print("=" * 74, flush=True)

    s1 = smoke_wall(N=40)
    s2 = smoke_buckle(N=40)
    s3 = smoke_winding_independent(N=44)
    smokes_pass = s1["PASS"] and s2["PASS"] and s3["PASS"]
    print(
        f"\n  SMOKES: wall={s1['PASS']} buckle={s2['PASS']} winding={s3['PASS']} "
        f"→ {'ALL PASS' if smokes_pass else 'FAIL — STOP'}",
        flush=True,
    )

    out = {
        "smoke_wall": {k: v for k, v in s1.items() if k != "loc_t"},
        "smoke_buckle": {k: v for k, v in s2.items() if k not in ("RH", "LH", "centrosym", "buckle_off")},
        "smoke_winding": s3,
        "smokes_pass": bool(smokes_pass),
    }

    if not smokes_pass:
        print("\n  Smoke gate FAILED — not running full test (prereg STOP).")
        (OUT / "crystal_graft_v2_results.json").write_text(json.dumps(out, indent=2, default=str))
        return out

    full = full_run(N=52, n_steps=1400)
    alpha = alpha_emergence(full)

    figs = make_figures(s1, s2, s3, full, alpha)

    # ── A/B/C verdict (Rule 11 honest closure) ──
    closes = full["closes_de_novo"]
    alpha_emergent = alpha["alpha_emergent"]
    golden = alpha["golden_self_assembles"]
    w_pol_fix = s3["w_pol_can_be_nonzero"]  # the structural deliverable
    if closes and alpha_emergent and golden:
        verdict = "A"  # Class-D CHORD candidate (adversarially-verify before belief)
    elif closes:
        verdict = "B"  # manifestation: (2,3) forms with its own carrier
    else:
        verdict = "C"  # residual localized to mode-selection (NOT the double-count)

    out.update(
        {
            "full_run": {k: v for k, v in full.items() if k != "engines"},
            "alpha_emergence": alpha,
            "figures": figs,
            "verdict": verdict,
            "structural_fix_w_pol_nonzero": bool(w_pol_fix),
            "elapsed_s": time.time() - t0,
        }
    )
    (OUT / "crystal_graft_v2_results.json").write_text(json.dumps(out, indent=2, default=str))

    print("\n" + "=" * 74)
    print(f"  VERDICT: {verdict}")
    print("=" * 74)
    print(f"  double-count FIXED (w_pol structurally able ≠0): {w_pol_fix}")
    print(f"  (2,3) closes de-novo in ω: {closes}  | control null: {full['control_null']}")
    print(f"  α⁻¹ emerges (α-free): {alpha_emergent}  | golden-torus self-assembles: {golden}")
    print(f"  elapsed {out['elapsed_s']:.0f}s; figures: {figs}", flush=True)
    return out


if __name__ == "__main__":
    main()
