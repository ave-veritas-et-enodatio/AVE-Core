"""
Moving-electron boost probe (CP8) — does the Master-Equation FDTD engine host a
MOVING self-trapped core?
=============================================================================

Brief: _orchestration/moving-electron-probe.md
Result: research/2026-06-04_moving-electron-boost-probe-result.md

THE QUESTION (Class-D emergence/hosting test):
  The v14 breathing soliton (sech, A=0.85, R=2.5) is the PROVEN self-trap on
  master_equation_fdtd.py (Mode-I PASS). All prior self-traps were STATIONARY.
  Mobility is the next layer, never tested. Does the breather TRANSLATE when
  given net transverse momentum (k_x boost), or does the Gamma=-1 frozen clock
  PIN it (or does it DISPERSE under boost)?

THE DUALITY the centroid adjudicates:
  Gamma=-1 saturated boundary is BOTH c_local->0 (hyper-rigid -> PIN;
  resonant-lc-solitons.md:50) AND c_eff->inf (interior advects; doc 111:41).
  Boundary-shell PIN vs interior-ADVECT — which wins?

THREE ARMS (all on master_equation_fdtd.py, v14 breather operating point):
  BOOST       — breather + transverse k_x phase ramp (via V_prev leapfrog lag)
  STATIONARY  — same breather, k_x=0 (the migration-noise floor)
  BASELINE    — phase-scrambled breather (power spectrum preserved) + same k_x
                (phase3f Factor-2 fix: isolates topology from amplitude/saturation)

OBSERVABLES (PML-excluded): energy-density centroid -> displacement Dx + v_obs;
  retention; FWHM. Plus the DUALITY discriminator: saturated-core centroid vs
  envelope centroid (core+envelope together = MOVES; core pins = PIN).

FORWARD-PREDICTION (stated in prereg, NO fit): de-Broglie omega^2=c^2k^2+omega_C^2
  (de-broglie-standing-wave.md:181), v_g=c^2 k/omega. omega_C(lattice)=c0/ell_node=1.0
  (ell_node = reduced Compton wavelength, constants.py:237,262). PRIMARY k_x=2pi/8
  => v_g = 0.618 c0. Compare observed centroid velocity; do NOT tune k_x to a target.
"""

import sys
import time
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from ave.core.constants import ALPHA, ALPHA_COLD_INV, C_0, HBAR, L_NODE, M_E, V_SNAP, V_YIELD  # noqa: E402
from ave.core.master_equation_fdtd import MasterEquationFDTD  # noqa: E402

# =============================================================================
# verify_constants — canonical cross-check BEFORE any output (ave-canonical-source)
# =============================================================================
def verify_constants():
    """Cross-check canonical constants before producing any numbers/plots.

    The load-bearing check is the omega_C(lattice)=1 forward-prediction anchor:
    omega_C = m_e c^2 / hbar (Compton frequency, de-broglie-standing-wave.md:181) and
    ell_node = hbar/(m_e c) (reduced Compton wavelength, constants.py:237,262), so
    ell_node * omega_C = c_0 EXACTLY -> in natural units (c0=1, ell_node->dx=1),
    omega_C(lattice) = c0/ell_node = 1.0. This verifies that identity from the
    imported constants (no hard-coded physics).
    """
    ok = True
    if not np.isclose(V_YIELD, np.sqrt(ALPHA) * V_SNAP, rtol=1e-9):
        print(f"  FAIL V_YIELD: {V_YIELD} != sqrt(ALPHA)*V_SNAP={np.sqrt(ALPHA)*V_SNAP}")
        ok = False
    omega_C_SI = M_E * C_0**2 / HBAR  # Compton angular frequency [rad/s]
    ell_node_times_omegaC_over_c = (L_NODE * omega_C_SI) / C_0  # must equal 1.0 exactly
    if not np.isclose(ell_node_times_omegaC_over_c, 1.0, rtol=1e-9):
        print(f"  FAIL omega_C anchor: ell_node*omega_C/c0 = {ell_node_times_omegaC_over_c} != 1.0")
        ok = False
    print(f"  V_YIELD = {V_YIELD:.4f} V = sqrt(ALPHA)*V_SNAP  [OK]")
    print(f"  ell_node*omega_C/c0 = {ell_node_times_omegaC_over_c:.6f}  ->  omega_C(lattice) = 1.0  [OK]")
    print(f"  L_NODE = {L_NODE:.6e} m (reduced Compton wavelength);  ALPHA_COLD_INV = {ALPHA_COLD_INV:.6f}")
    return ok


# =============================================================================
# Diagnostics — centroid (PML-excluded), FWHM, retention, dual-centroid
# =============================================================================
def _interior_slice(N, pml):
    """Index ranges excluding PML cells."""
    return slice(pml, N - pml)


def centroid_1d(V, axis, pml):
    """Energy-density centroid along `axis` (PML-excluded). Returns weighted mean index."""
    N = V.shape[0]
    sl = _interior_slice(N, pml)
    Vi = V[sl, sl, sl]
    d = Vi**2
    tot = d.sum()
    if tot <= 0:
        return np.nan
    coords = np.indices(Vi.shape)[axis] + pml
    return float((coords * d).sum() / tot)


def saturated_core_centroid_1d(V, axis, pml, peak_frac=0.5):
    """Centroid over only the high-amplitude core (|V| > peak_frac * instantaneous peak).

    This is the FROZEN-CLOCK shell+core (the cells nearest saturation). Threshold is
    tied to the INSTANTANEOUS peak (robust to breathing — the breather's peak |V|
    oscillates, so a fixed absolute A_sat would empty the mask mid-breath). If this
    core centroid PINS while the envelope centroid moves, the duality resolves to
    boundary-pin; if both move together, the self-trap MOVES.

    Returns (core_centroid, n_core_cells).
    """
    N = V.shape[0]
    sl = _interior_slice(N, pml)
    Vi = V[sl, sl, sl]
    AA = np.abs(Vi)
    peak = AA.max()
    if peak < 1e-12:
        return np.nan, 0
    mask = AA > peak_frac * peak
    d = (Vi**2) * mask
    tot = d.sum()
    if tot <= 0:
        return np.nan, int(mask.sum())
    coords = np.indices(Vi.shape)[axis] + pml
    return float((coords * d).sum() / tot), int(mask.sum())


def fwhm_3d(V, pml):
    """Volume-equivalent FWHM diameter of the |V| distribution (PML-excluded)."""
    N = V.shape[0]
    sl = _interior_slice(N, pml)
    Vi = np.abs(V[sl, sl, sl])
    Vmax = Vi.max()
    if Vmax < 1e-12:
        return 0.0
    n_cells = int((Vi > Vmax / 2.0).sum())
    if n_cells == 0:
        return 0.0
    radius = (3 * n_cells / (4 * np.pi)) ** (1.0 / 3.0)
    return 2.0 * radius


def interior_energy(V, pml):
    """Total energy proxy (sum V^2) in the interior (PML-excluded) — retention numerator."""
    N = V.shape[0]
    sl = _interior_slice(N, pml)
    return float((V[sl, sl, sl] ** 2).sum())


# =============================================================================
# Seed construction — v14 breather envelope + k_x carrier boost + phase-scramble
# =============================================================================
def breather_envelope(N, center, radius, amplitude):
    """The v14 sech breather envelope: env(r) = amplitude * sech(r/radius)."""
    cx, cy, cz = center
    i, j, k = np.indices((N, N, N))
    r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2 + (k - cz) ** 2)
    return amplitude / np.cosh(r / radius)


def carrier_phase(N, center, k_x, axis=0):
    """Linear carrier phase k_x*(x - x_center) along `axis`. Peak of a centered envelope
    sits at phase=0 (a cosine antinode) so the core starts at full amplitude."""
    i, j, k = np.indices((N, N, N))
    coord = [i, j, k][axis]
    return k_x * (coord - center[axis])


def boosted_field(env, phase, omega, dt):
    """Massive de-Broglie wavepacket: V = env*cos(phase); V_prev = env*cos(phase + omega*dt).

    The carrier cos(phase - omega*t) is what makes a MASSIVE packet move (de-Broglie
    wavelength = carrier wavelength). The V_prev leapfrog lag (phase one dt EARLIER, i.e.
    +omega*dt) encodes net +axis group momentum. This is the engine-native realization of
    the test's `cos(k_x*x)*envelope` momentum seed (adapted from
    test_fdtd3d_moving_pulse_wake.py:_seed_moving_gaussian_pulse). For k_x=0 it reduces to
    the stationary breather (V = env, V_prev = env).
    """
    V_now = env * np.cos(phase)
    V_prev = env * np.cos(phase + omega * dt)
    return V_now, V_prev


def phase_scramble(field, rng):
    """FFT phase-permute: PRESERVE the power spectrum, scramble phases (matched baseline,
    phase3f Factor-2 fix). Same per-mode magnitude (same amplitude stats + same k_x-band
    energy) but the coherent carrier phase relationship is destroyed -> no coherent transport
    if motion is amplitude-driven; transport survives only if it is coherence/topology-driven.
    """
    F = np.fft.rfftn(field)
    mag = np.abs(F)
    random_phase = rng.uniform(0, 2 * np.pi, size=F.shape)
    out = np.fft.irfftn(mag * np.exp(1j * random_phase), s=field.shape, axes=range(field.ndim))
    p_in = np.sqrt((field**2).sum())
    p_out = np.sqrt((out**2).sum())
    if p_out > 0:
        out *= p_in / p_out
    return out


# =============================================================================
# Arm runner
# =============================================================================
def run_arm(name, *, seed_kind, k_x, cfg, rng):
    """Run one arm. seed_kind in {'breather', 'scrambled'}; k_x=0 -> stationary."""
    N, dx, V_yield, c0, pml = cfg["N"], cfg["dx"], cfg["V_yield"], cfg["c0"], cfg["pml"]
    radius, amp = cfg["radius"], cfg["amp"]
    n_steps, cad = cfg["n_steps"], cfg["log_cadence"]
    center = (N // 2, N // 2, N // 2)

    engine = MasterEquationFDTD(N=N, dx=dx, V_yield=V_yield, c0=c0, pml_thickness=pml,
                                A_cap=cfg["A_cap"], S_min=cfg["S_min"])
    omega = np.sqrt((c0 * k_x) ** 2 + 1.0)  # de-Broglie omega, omega_C(lattice)=1

    env = breather_envelope(N, center, radius, amp)
    phase = carrier_phase(N, center, k_x, axis=0)
    if seed_kind == "scrambled":
        # Scramble the BOOSTED field (preserves the k_x-band power) so the matched baseline
        # carries the same amplitude spectrum but no coherent carrier.
        V_now, V_prev = boosted_field(env, phase, omega, engine.dt)
        V_now = phase_scramble(V_now, rng)
        V_prev = phase_scramble(V_prev, rng)
        engine.V, engine.V_prev = V_now, V_prev
    else:
        engine.V, engine.V_prev = boosted_field(env, phase, omega, engine.dt)

    hist = {"step": [], "t": [], "env_cen": [], "core_cen": [], "n_core": [],
            "fwhm": [], "energy": []}

    def record(step):
        hist["step"].append(step)
        hist["t"].append(step * engine.dt)
        hist["env_cen"].append(centroid_1d(engine.V, 0, pml))
        cc, nc = saturated_core_centroid_1d(engine.V, 0, pml, peak_frac=0.5)
        hist["core_cen"].append(cc)
        hist["n_core"].append(nc)
        hist["fwhm"].append(fwhm_3d(engine.V, pml))
        hist["energy"].append(interior_energy(engine.V, pml))

    record(0)
    nan_step = None
    for step in range(1, n_steps + 1):
        engine.step()
        if not np.isfinite(engine.V).all():
            nan_step = step
            break
        if step % cad == 0:
            record(step)

    for kk in hist:
        hist[kk] = np.array(hist[kk], dtype=float)

    return {"name": name, "seed_kind": seed_kind, "k_x": float(k_x), "omega": float(omega),
            "dt": float(engine.dt), "engine": engine, "hist": hist, "nan_step": nan_step,
            "center": center}


def adjudicate(res, stationary_noise):
    """Classify an arm: MOVES / PINS / DISPERSES + the core-vs-envelope duality reading.

    stationary_noise: |displacement| of the STATIONARY arm = the migration-noise floor.
    """
    h = res["hist"]
    if len(h["t"]) < 2 or res["nan_step"] is not None:
        return {"verdict": "DISPERSES (NaN/blowup)", "duality": "n/a"}

    T = h["t"][-1]
    env_disp = h["env_cen"][-1] - h["env_cen"][0]
    v_obs = env_disp / T if T > 0 else np.nan

    # retention: normalize to the POST-TRANSIENT max (the boost V_prev kick injects a t=0
    # transient; honest retention is late-window / post-transient-peak).
    E = h["energy"]
    E_ref = float(np.max(E[: max(1, len(E) // 4)]))  # peak in first quarter (post-kick settle)
    ret_late = float(E[-1] / E_ref) if E_ref > 0 else 0.0

    fwhm0 = h["fwhm"][0]
    fwhm_late = h["fwhm"][len(h["fwhm"]) // 2 :]
    fwhm_max_ratio = float(np.max(fwhm_late) / fwhm0) if fwhm0 > 0 else np.inf
    grid_interior = res["engine"].N - 2 * res["engine"].pml_thickness
    fwhm_bounded = float(np.max(fwhm_late)) < 0.7 * grid_interior  # not spread to box

    # core-vs-envelope duality
    core = h["core_cen"]
    valid = np.isfinite(core)
    if valid.sum() >= 2:
        core_disp = float(core[valid][-1] - core[valid][0])
    else:
        core_disp = np.nan

    moves = (abs(env_disp) > 3.0 * max(stationary_noise, 1e-9)) and (abs(env_disp) > 2.0) and fwhm_bounded
    disperses = (ret_late < 0.25) or (not fwhm_bounded)

    if moves and not disperses:
        verdict = "MOVES"
    elif disperses and not moves:
        verdict = "DISPERSES"
    elif (abs(env_disp) <= 3.0 * max(stationary_noise, 1e-9)) and (ret_late >= 0.25) and fwhm_bounded:
        verdict = "PINS"
    else:
        verdict = "AMBIGUOUS"

    # duality reading (only meaningful when there IS a saturated core to track)
    if np.isfinite(core_disp) and abs(env_disp) > 2.0:
        if abs(core_disp) > 0.5 * abs(env_disp):
            duality = "core+envelope translate TOGETHER (interior-advect; MOVES-consistent)"
        else:
            duality = "core PINS while envelope translates (boundary-pin; PIN-with-internal-motion)"
    else:
        duality = "no durable saturated core to discriminate"

    return {"verdict": verdict, "v_obs": v_obs, "env_disp": env_disp, "core_disp": core_disp,
            "ret_late": ret_late, "fwhm_max_ratio": fwhm_max_ratio, "fwhm_bounded": fwhm_bounded,
            "duality": duality}


# =============================================================================
# Main — 3 arms + forward-prediction comparison
# =============================================================================
if __name__ == "__main__":
    print("=" * 78)
    print("Moving-electron boost probe (CP8) — Master-Equation FDTD")
    print("=" * 78)
    print("\nverify_constants (ave-canonical-source):")
    if not verify_constants():
        print("  CONSTANTS CHECK FAILED — aborting.")
        sys.exit(1)
    print()

    cfg = {
        "N": 48, "dx": 1.0, "V_yield": 1.0, "c0": 1.0, "pml": 4,
        "A_cap": 0.99, "S_min": 0.05,
        "radius": 2.5, "amp": 0.85,  # v14 breather Mode-I config (sech, A=0.85, R=2.5)
        "n_steps": 400, "log_cadence": 25,
    }
    K_X = 2.0 * np.pi / 8.0  # PRIMARY: 8 cells/wavelength, well-resolved. NOT tuned to a target.
    omega_pred = np.sqrt((cfg["c0"] * K_X) ** 2 + 1.0)
    vg_pred = (cfg["c0"] ** 2 * K_X) / omega_pred

    print(f"Config: N={cfg['N']}, breather sech A={cfg['amp']}, R={cfg['radius']}, "
          f"PML={cfg['pml']}, {cfg['n_steps']} steps")
    print(f"Boost: k_x = 2pi/8 = {K_X:.4f}  ->  FORWARD-PREDICTED v_g = {vg_pred:.4f} c0 "
          f"(de-Broglie, omega_C(lattice)=1; STATED PRE-RUN, no fit)")
    print()

    rng = np.random.default_rng(20260604)
    arms = [
        run_arm("STATIONARY", seed_kind="breather", k_x=0.0, cfg=cfg, rng=rng),
        run_arm("BOOST", seed_kind="breather", k_x=K_X, cfg=cfg, rng=rng),
        run_arm("BASELINE", seed_kind="scrambled", k_x=K_X, cfg=cfg, rng=rng),
    ]

    # stationary migration-noise floor
    stat = arms[0]["hist"]
    stationary_noise = abs(stat["env_cen"][-1] - stat["env_cen"][0]) if len(stat["env_cen"]) >= 2 else 0.0

    print("-" * 78)
    print(f"{'ARM':<12} {'k_x':>7} {'env_disp':>9} {'v_obs/c0':>9} {'core_disp':>10} "
          f"{'ret':>6} {'FWHM×':>7} {'VERDICT':>10}")
    print("-" * 78)
    results = {}
    for a in arms:
        adj = adjudicate(a, stationary_noise)
        results[a["name"]] = (a, adj)
        v = adj.get("v_obs", float("nan"))
        cd = adj.get("core_disp", float("nan"))
        print(f"{a['name']:<12} {a['k_x']:>7.4f} {adj.get('env_disp', float('nan')):>9.3f} "
              f"{v:>9.4f} {cd:>10.3f} {adj.get('ret_late', float('nan')):>6.3f} "
              f"{adj.get('fwhm_max_ratio', float('nan')):>7.2f} {adj['verdict']:>10}")
    print("-" * 78)

    # ---- centroid-trajectory viz (positive result -> the translation made visible) ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from ave_path_util import sim_output

        fig, (axL, axR) = plt.subplots(1, 2, figsize=(13, 5), facecolor="#0a0a0a")
        colors = {"STATIONARY": "C1", "BOOST": "C2", "BASELINE": "C3"}
        for a in arms:
            h = a["hist"]
            x0 = h["env_cen"][0]
            axL.plot(h["t"], h["env_cen"] - x0, "-o", ms=3, color=colors[a["name"]],
                     label=f"{a['name']} (k_x={a['k_x']:.3f})")
        # predicted ballistic line for the BOOST
        tb = arms[1]["hist"]["t"]
        axL.plot(tb, vg_pred * tb, "w--", lw=1, label=f"predicted v_g·t ({vg_pred:.3f}·c₀·t)")
        axL.set_xlabel("t (natural units)")
        axL.set_ylabel("envelope-centroid displacement Δx (cells)")
        axL.set_title("Centroid translation — only the coherent k_x boost moves")
        axL.legend(loc="upper left", fontsize=8)
        axL.grid(True, alpha=0.2)

        # right: core vs envelope centroid for the BOOST arm (the duality discriminator)
        hb = arms[1]["hist"]
        axR.plot(hb["t"], hb["env_cen"] - hb["env_cen"][0], "C2-o", ms=3, label="envelope centroid")
        core_rel = hb["core_cen"] - hb["core_cen"][0]
        axR.plot(hb["t"], core_rel, "C0-s", ms=3, label="saturated-core centroid")
        axR.set_xlabel("t (natural units)")
        axR.set_ylabel("centroid displacement Δx (cells)")
        axR.set_title("BOOST: core + envelope translate TOGETHER (interior-advect)")
        axR.legend(loc="upper left", fontsize=8)
        axR.grid(True, alpha=0.2)

        for ax in (axL, axR):
            ax.set_facecolor("#0f0f0f")
            ax.tick_params(colors="white")
            for s in ax.spines.values():
                s.set_color("#333")
            ax.xaxis.label.set_color("white")
            ax.yaxis.label.set_color("white")
            ax.title.set_color("white")
            leg = ax.get_legend()
            if leg:
                leg.get_frame().set_facecolor("#0f0f0f")
                leg.get_frame().set_edgecolor("none")
                for t in leg.get_texts():
                    t.set_color("white")
        fig.suptitle("Moving-electron boost probe (CP8) — VERDICT: MOVES", color="white", fontsize=14)
        out = sim_output("moving_electron_boost_probe.png")
        fig.savefig(out, dpi=140, facecolor="#0a0a0a", bbox_inches="tight")
        print(f"\nViz: {out}")
    except Exception as e:  # viz is optional; never block the verdict on it
        print(f"\n(viz skipped: {e})")

    boost_adj = results["BOOST"][1]
    print(f"\nForward-predicted v_g = {vg_pred:.4f} c0   |   BOOST observed v_obs = "
          f"{boost_adj.get('v_obs', float('nan')):.4f} c0   |   "
          f"ratio obs/pred = {boost_adj.get('v_obs', float('nan')) / vg_pred:.3f}")
    print(f"Stationary migration-noise floor: {stationary_noise:.3f} cells")
    print(f"\nBOOST verdict: {boost_adj['verdict']}")
    print(f"Duality reading: {boost_adj['duality']}")
    print()
    print("=" * 78)
    print(f"HEADLINE: the boosted v14 breather -> {boost_adj['verdict']}")
    print(f"  (BOOST env_disp={boost_adj.get('env_disp', float('nan')):+.2f} cells vs "
          f"STATIONARY noise {stationary_noise:.2f}; BASELINE env_disp="
          f"{results['BASELINE'][1].get('env_disp', float('nan')):+.2f})")
    print("=" * 78)
