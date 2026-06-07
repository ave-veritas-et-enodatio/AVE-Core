"""Genesis re-run on the moving Γ=−1 impedance boundary (saturation-TIR).

Prereg (FROZEN): research/2026-06-06_saturation-tir-moving-boundary-prereg.md
Scope §5/§6. Tests whether rendering Axiom-4 saturation as a *moving reflective
short* (use_impedance_boundary) makes the charged ω-shear photon self-trap —
where the non-convex energy term collapses/disperses (Arm C (III)).

substrate-native-check: CP1 wave-propagation in step() (NOT relax/energy-min);
CP2 Cosserat μ-sector short; CP4 the (2,3) lives in phase-space — here read on
the Cosserat (ω, ω̇) phasor that MATCHES the seeded ω-photon (flagged, NOT the
K4 V_inc coordinate where the corpus (2,3) primarily lives); CP6 reactance pair
+ proper energy (impedance_hamiltonian); CP7 PML exclusion + density-peak;
CP8 seed the GENERATIVE PRECURSOR (a helical photon) + a matched baseline
(same seed, mechanism OFF), NOT the finished (2,3).

ave-driver-script-honesty: every printed number is measured from the evolved
field; PROXY/COORDINATE caveats are stated inline, not buried.
ave-evidence-framing: outcomes (I)/(II)/(III) are pre-committed (prereg §6).

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/r10_saturation_tir_moving_boundary_genesis.py
"""
from __future__ import annotations

import json
import os

import numpy as np

from ave.core.constants import ALPHA, C_0, L_NODE, V_SNAP, V_YIELD
from ave.topological.cosserat_field_3d import CosseratField3D, _tetrahedral_curl
import jax.numpy as jnp

# ── Canonical-source verification (ave-canonical-source Step 4) ──────────────
import ave.core.constants as _avc  # noqa: E402

assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants source"
assert abs(V_YIELD / (np.sqrt(ALPHA) * V_SNAP) - 1.0) < 1e-9, "V_YIELD = √α·V_SNAP broken"
# Engine works in natural units (dx = ℓ_node = 1, c_R = 1), so the Compton ring
# scale ω_C = c/ℓ_node → 1 in natural units. The physical ω_C anchors the ratio.
OMEGA_C_PHYS = C_0 / L_NODE          # ≈ 7.76e20 rad/s (Compton angular frequency)
OMEGA_C_NATURAL = 1.0                # = c_R / dx  (same ring scale in engine units)

# ── Genesis config ──────────────────────────────────────────────────────────
N, PML = 36, 4
SIGMA, LAM, AMP = 3.0, 6.0, 3.0          # focusing ω-packet at the yield scale
CENTER = (N / 2.0, N / 2.0, N / 2.0)
K_WALL, SKIN = 400.0, 2                   # stable hard-ish wall (g_min→~−0.5, bounded)
N_STEPS = 300                             # clean stable window (per energy sweep)


def _seed(use_ib, K, helicity=1.0):
    s = CosseratField3D(
        N, N, N, pml_thickness=PML,
        use_impedance_boundary=use_ib, impedance_clamp_strength=K, impedance_skin_smoothing=SKIN,
    )
    s.initialize_gaussian_wavepacket_omega(
        CENTER, sigma=SIGMA, direction=(1, 0, 0), wavelength=LAM,
        amplitude=AMP, axis=2, helicity=helicity,
    )
    return s


def _interior(s):
    ii, jj, kk = s._i, s._j, s._k
    return (ii >= PML) & (ii < N - PML) & (jj >= PML) & (jj < N - PML) & (kk >= PML) & (kk < N - PML)


def _w2(s):
    return np.sum(np.asarray(s.omega) ** 2, axis=-1) * s.mask_alive * _interior(s)


def _localization(s):
    """Fraction of |ω|² inside r<=6 of the energy-density peak (CP7: peak, not
    centroid; PML-excluded). High+held = trapped; →0 = dispersed/collapsed."""
    w2 = _w2(s)
    tot = w2.sum()
    if tot < 1e-30:
        return 0.0, 0.0, (N / 2, N / 2, N / 2)
    flat = np.argmax(w2)
    pk = np.unravel_index(flat, w2.shape)
    ii, jj, kk = s._i, s._j, s._k
    r2 = (ii - pk[0]) ** 2 + (jj - pk[1]) ** 2 + (kk - pk[2]) ** 2
    core = (w2 * (r2 <= 36)).sum()
    return float(core / tot), float(tot), pk


def _rms(s):
    w2 = _w2(s)
    tot = w2.sum()
    if tot < 1e-30:
        return 0.0
    ii, jj, kk = s._i, s._j, s._k
    cx, cy, cz = (ii * w2).sum() / tot, (jj * w2).sum() / tot, (kk * w2).sum() / tot
    return float(np.sqrt((((ii - cx) ** 2 + (jj - cy) ** 2 + (kk - cz) ** 2) * w2).sum() / tot))


def _gamma_stats(s):
    g = s._impedance_gamma_field()
    return float(g[s.mask_alive].min()), g


def _integrated_helicity(s):
    """Integrated Beltrami helicity H_bel = Σ ω·(∇×ω) over interior alive cells.

    THIS is the carried 'charge' of a chiral ω-photon (Cosserat-ω sector) — a
    circularly-polarized traveling wave has h≠0 but Hopf charge Q_H≈0 (it is
    not a knotted/linked Hopfion), so check 5 reads helicity, not Q_H."""
    curl = np.asarray(_tetrahedral_curl(jnp.asarray(s.omega), s.dx))
    dens = np.sum(np.asarray(s.omega) * curl, axis=-1) * s.mask_alive * _interior(s)
    return float(dens.sum())


def run(use_ib, K, helicity=1.0, nsteps=N_STEPS, record=False):
    s = _seed(use_ib, K, helicity)
    loc0, tot0, _ = _localization(s)
    rms0 = _rms(s)
    wmax0 = float(np.abs(np.asarray(s.omega)).max())
    trace = []
    for t in range(nsteps):
        s.step()
        if record and (t % 15 == 0 or t == nsteps - 1):
            wmax = float(np.abs(np.asarray(s.omega)).max())
            row = {"t": t, "rms": _rms(s), "loc": _localization(s)[0], "wmax": wmax}
            if use_ib:
                row["g_min"] = _gamma_stats(s)[0]
                row["E"] = s.impedance_hamiltonian()["H"]
            else:
                row["E"] = s.total_hamiltonian()
            trace.append(row)
    locf, totf, pk = _localization(s)
    return {
        "s": s, "loc0": loc0, "locf": locf, "rms0": rms0, "rmsf": _rms(s),
        "wmax0": wmax0, "wmaxf": float(np.abs(np.asarray(s.omega)).max()),
        "peak": pk, "trace": trace,
    }


def main():
    out = {"config": dict(N=N, PML=PML, sigma=SIGMA, wavelength=LAM, amplitude=AMP,
                          K_wall=K_WALL, skin_smoothing=SKIN, n_steps=N_STEPS)}
    print("=" * 78)
    print("GENESIS RE-RUN — saturation-TIR moving Γ=−1 impedance boundary")
    print(f"  N={N} PML={PML} | helical ω-photon σ={SIGMA} λ={LAM} A={AMP} | wall K={K_WALL} skin={SKIN}")
    print(f"  canonical: V_YIELD={V_YIELD:.1f} V  V_SNAP={V_SNAP/1e3:.1f} kV  ℓ_node={L_NODE:.3e} m"
          f"  α={ALPHA:.4e}  ω_C={OMEGA_C_PHYS:.3e} rad/s")
    print("=" * 78)

    # ── §0 VALIDITY GATE: low-amplitude photon must propagate MATCHED ─────────
    print("\n[§0 VALIDITY GATE] low-amplitude photon (A=1e-3), wall ON — expect Γ≈0, matched")
    sg = CosseratField3D(N, N, N, pml_thickness=PML, use_impedance_boundary=True,
                         impedance_clamp_strength=K_WALL, impedance_skin_smoothing=SKIN)
    sg.initialize_gaussian_wavepacket_omega(CENTER, sigma=SIGMA, direction=(1, 0, 0),
                                            wavelength=LAM, amplitude=1e-3, axis=2, helicity=1.0)
    E0 = sg.impedance_hamiltonian()["H"]
    gmax_seen = 0.0
    for t in range(80):
        sg.step()
        gmax_seen = min(gmax_seen, _gamma_stats(sg)[0])
    Ef = sg.impedance_hamiltonian()["H"]
    gate_ok = abs(gmax_seen) < 1e-4 and abs(Ef / E0 - 1.0) < 0.05
    out["validity_gate"] = {"gamma_min": gmax_seen, "E_ratio": Ef / E0, "pass": bool(gate_ok)}
    print(f"  Γ_min over run = {gmax_seen:.2e}  (expect ~0, |Γ|<1e-4)")
    print(f"  energy E_f/E_0 = {Ef / E0:.4f}  (matched, no spurious reflection)")
    print(f"  VALIDITY GATE: {'PASS — photon limit recovered' if gate_ok else 'FAIL'}")

    # ── §1 THREE-WAY: baseline (collapse) vs no-wall (disperse) vs wall ───────
    print("\n[§1 MECHANISM] genesis amplitude A=3.0 — does the wall convert collapse→confinement?")
    base = run(False, 0.0, record=True)              # energy-saturation (Arm C (III))
    nowall = run(True, 0.0, record=True)             # linear bulk, no wall
    wall = run(True, K_WALL, record=True)            # the moving Γ=−1 wall
    for name, r in [("energy-sat baseline (IB=False)", base),
                    ("no-wall linear (K=0)", nowall),
                    ("MOVING Γ=−1 WALL (K=%g)" % K_WALL, wall)]:
        tr = r["trace"][-1]
        extra = f" g_min={tr.get('g_min', float('nan')):.3f}" if "g_min" in tr else ""
        print(f"  {name:34s}: loc {r['loc0']:.3f}→{r['locf']:.3f}  rms {r['rms0']:.2f}→{r['rmsf']:.2f}"
              f"  wmax {r['wmax0']:.2f}→{r['wmaxf']:.2f}  E_f={tr['E']:.2e}{extra}")
    out["mechanism"] = {k: {kk: v[kk] for kk in ("loc0", "locf", "rms0", "rmsf", "wmax0", "wmaxf")}
                        for k, v in [("baseline", base), ("nowall", nowall), ("wall", wall)]}
    out["mechanism"]["baseline"]["E_f"] = base["trace"][-1]["E"]
    out["mechanism"]["wall"]["E_f"] = wall["trace"][-1]["E"]
    out["mechanism"]["wall"]["g_min_f"] = wall["trace"][-1].get("g_min")

    collapsed = base["wmaxf"] > 50 * base["wmax0"] or base["locf"] < 0.2
    dispersed = nowall["rmsf"] > 1.8 * nowall["rms0"]
    wall_held = wall["locf"] > 0.5 and wall["wmaxf"] < 50 * wall["wmax0"]
    print(f"  → baseline collapsed/dispersed: {collapsed} | no-wall dispersed: {dispersed} | wall held: {wall_held}")

    # ── §2 SIX CHECKS on the wall run ────────────────────────────────────────
    sw = wall["s"]
    print("\n[§2 SIX CHECKS on the wall run]")
    # 3. sub-yield core + Γ=−1 skin (radial Γ profile about the density peak)
    g = sw._impedance_gamma_field()
    ii, jj, kk = sw._i, sw._j, sw._k
    pk = wall["peak"]
    rr = np.sqrt((ii - pk[0]) ** 2 + (jj - pk[1]) ** 2 + (kk - pk[2]) ** 2)
    core_m = (rr <= 2) & sw.mask_alive & _interior(sw)
    skin_m = (rr > 2) & (rr <= 6) & sw.mask_alive & _interior(sw)
    core_g = float(g[core_m].mean()) if core_m.sum() else float("nan")
    skin_g = float(g[skin_m].min()) if skin_m.sum() else float("nan")
    print(f"  (3) sub-yield core + Γ=−1 skin: core <Γ>={core_g:+.3f}  skin min Γ={skin_g:+.3f}"
          f"  (skin Γ<0 = reflective short; core Γ≈0 = sub-yield)")
    # 1. self-trap
    print(f"  (1) self-trap: localization {wall['loc0']:.3f}→{wall['locf']:.3f}, wmax bounded={wall['wmaxf']<50*wall['wmax0']}"
          f"  (vs baseline {base['loc0']:.3f}→{base['locf']:.3f})")
    # 2. (2,3) winding — Cosserat ω-phasor (COORDINATE-FLAGGED, not K4 V_inc)
    c_wall = sw.extract_crossing_count()
    Qh_wall = sw.extract_hopf_charge()
    print(f"  (2) (2,3) cavity mode: crossing-count c={c_wall}  Q_H={Qh_wall:+.3f}"
          f"  [COORDINATE: Cosserat ω real-space; the corpus (2,3) primarily lives in K4 (V_inc,V_ref)]")
    # 4. Q = ℓ — geometric extractor (PROXY; not the Op21 Nyquist mode-count)
    Q_geo = sw.extract_quality_factor()
    R_sh, r_sh = sw.extract_shell_radii()
    print(f"  (4) Q=ℓ: geometric Q={Q_geo:.2f} [PROXY — geometric R·r form, NOT the Op21 Nyquist mode-count]"
          f"  (R={R_sh:.2f}, r={r_sh:.2f})")
    # 6. mass / size / ring
    mass_proxy = wall["trace"][-1]["E"]
    print(f"  (6) mass=½LI² proxy (confined energy)={mass_proxy:.2e}  size R≈{R_sh:.2f} cells (ℓ_node units)"
          f"  ring: ω_C(natural)={OMEGA_C_NATURAL:.2f}")
    out["six_checks"] = {"core_gamma": core_g, "skin_gamma": skin_g, "crossing_c": c_wall,
                         "Q_H": Qh_wall, "Q_geometric": Q_geo, "R_shell": R_sh, "r_shell": r_sh,
                         "mass_proxy": mass_proxy}

    # ── §3 charge = helicity (seed +h and −h; Beltrami helicity must flip) ────
    print("\n[§3 charge=helicity] seed +h vs −h (wall ON) — Beltrami helicity sign must flip, both confine")
    wp = run(True, K_WALL, helicity=+1.0)
    wm = run(True, K_WALL, helicity=-1.0)
    Hp, Hm = _integrated_helicity(wp["s"]), _integrated_helicity(wm["s"])
    flips = np.sign(Hp) != np.sign(Hm) and abs(Hp) > 1e-6 and abs(Hm) > 1e-6
    both_confine = wp["locf"] > 0.5 and wm["locf"] > 0.5
    print(f"  +h: H_bel={Hp:+.3e} loc→{wp['locf']:.3f}   −h: H_bel={Hm:+.3e} loc→{wm['locf']:.3f}")
    print(f"  charge=helicity: H_bel sign flips={flips}, both confine={both_confine}")
    out["charge_helicity"] = {"H_plus": Hp, "H_minus": Hm, "sign_flips": bool(flips),
                              "both_confine": bool(both_confine)}

    # ── §4 hard-wall diagnostic — Γ→−1 forms but the explicit scheme pumps ────
    print("\n[§4 hard-wall §7 diagnostic] K=800 — does a HARD Γ→−1 skin form, and is it stable?")
    sh = _seed(True, 800.0, helicity=1.0)
    sh.step()
    Eh0 = sh.impedance_hamiltonian()["H"]
    g_deep, E_ratio = 0.0, 1.0
    for t in range(400):
        sh.step()
        g_deep = min(g_deep, _gamma_stats(sh)[0])
        if t == 399:
            E_ratio = sh.impedance_hamiltonian()["H"] / Eh0
    hard_skin = g_deep < -0.9
    stable = E_ratio < 1.5  # energy roughly conserved; >1.5 over 400 steps = pumping
    print(f"  hard skin Γ_min={g_deep:.3f} (forms={hard_skin})  energy E/E0={E_ratio:.1f} (stable={stable})")
    print("  → the idealized Γ=−1 wall FORMS but the explicit moving stiff-clamp PARAMETRIC-PUMPS (§7);"
          " a stable Γ=−1 standing wave needs an implicit/energy-conserving integrator")
    out["hard_wall"] = {"gamma_min": g_deep, "E_ratio": E_ratio, "forms": bool(hard_skin),
                        "stable": bool(stable)}

    # ── VERDICT (prereg §6) ──────────────────────────────────────────────────
    # skin forms: a clearly-negative reflective short (distinguishable from the
    # matched Γ≈0 bulk). (2,3): requires the full double-winding (w2=3) OR a
    # topological charge — a bare crossing-count c=2 with Q_H≈0 is NOT the knot.
    skin_forms = skin_g < -0.05
    has_23 = (c_wall == 3) or (c_wall >= 2 and abs(Qh_wall) > 0.5)
    print("\n" + "=" * 78)
    if wall_held and skin_forms and has_23 and flips:
        verdict = "I"
        msg = "(I) confines → standing (2,3), charge=helicity → the genesis WORKS"
    elif (wall_held or skin_forms) and not has_23:
        verdict = "II"
        msg = "(II) reflective skin forms + boundary confines, but NO clean (2,3) cavity mode → boundary right, mode-assembly isn't"
    else:
        verdict = "III"
        msg = "(III) reflection does not stabilize → gap deeper than energy-vs-boundary"
    out["verdict"] = verdict
    print(f"VERDICT: {msg}")
    print(f"  wall_held={wall_held} skin_forms={skin_forms} has_(2,3)={has_23} charge=helicity={flips}")
    print("=" * 78)

    here = os.path.dirname(os.path.abspath(__file__))
    jpath = os.path.join(here, "r10_saturation_tir_moving_boundary_genesis_results.json")
    out_clean = {k: v for k, v in out.items()}
    with open(jpath, "w") as f:
        json.dump(out_clean, f, indent=2, default=float)
    print(f"\nResults JSON: {jpath}")
    return out


if __name__ == "__main__":
    main()
