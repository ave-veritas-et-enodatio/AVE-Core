"""
CRUX test: does the K4 to Cosserat (Op14 = trace-reversal) coupling's
microrotational response A2_mu scale with resonant cavity Q (a drivable KNOB)
or is it capped (a WALL)?

Settles the three-way verdict (KNOB / WALL-physics / WALL-engine) and the
load-bearing substrate-native distinction: is A2_mu DYNAMICALLY evolved (the
Cosserat omega field actually builds through the K4<->Cosserat coupling) or
ALGEBRAICALLY set (by a direct Cosserat-omega source painting omega on the
slab)?

Architecture facts established by reading the engine (load-bearing):
  - A2_mu = (1 + kappa_chiral*h_local) * kappa(omega)^2 / omega_yield^2.
    It depends ONLY on the Cosserat omega-field curvature. The K4 voltage V
    feeds A2_eps (electric sector), NOT A2_mu. So a K4 drive can raise A2_mu
    ONLY indirectly, via the V->omega coupling force d L_c / d omega.
  - That coupling force lives in
    CoupledK4Cosserat._compute_coupling_force_on_cosserat() and is ZEROED when
    disable_cosserat_lc_force=True (the A28 double-count correction). With it
    True (A28-correct), there is NO dynamical K4->omega pump at all.
  - At omega=0 the coupling force d L_c / d omega = 0 (omega=0 is a fixed
    point); a cold (traceless) photon cannot seed the microrotation. (Corpus:
    doc 50_:131 "Autoresonant drive on a cold vacuum behaves identically to
    fixed-f CW -- zero Cosserat response.")
  - omega_yield = pi, epsilon_yield = 1, kappa_chiral = alpha*1.2 ~ 8.76e-3.

Q knob (reported honestly): the engine has NO scalar "Q" parameter. The
resonant build-up is governed by (i) drive amplitude (sets how high the driven
sector's A2 climbs) and (ii) resonance tracking -- AutoresonantCWSource (PLL,
high-Q regenerative feedback, tracks the Duffing-softened resonance) vs fixed-f
CWSource (low-Q, detuning-limited). We use the realized driven-sector build-up
(peak A2_K4) as the empirical resonant-build-up axis and contrast autoresonant
vs fixed-f as the Q-quality contrast.

Anchors (verified in source):
  - 0.012  : 70_phase5_resume_methodology.md:58 (Phase-5e, K4 autoresonant on a
             T=0.1 thermally-seeded omega; "K4->Cosserat coupling weakness").
  - 1.009  : vacuum_engine.py:104-105 / doc 50_ (autoresonant, T=0.1 thermal
             seed; doc 50_:57 -- 0/20 reproducible, known tail outcome).

Skills fired: substrate-native-check (dynamical-vs-heuristic, Checkpoint 8
precursor, Checkpoint 7 PML exclusion, Checkpoint 6 reactance pair),
ave-canonical-source (constants from the engine), verify-before-cite (anchors),
ave-driver-script-honesty, ave-engineering-program-rigor (figure + anchors).
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

# matplotlib non-interactive
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Ensure src on path when run from repo root or scripts dir
_HERE = Path(__file__).resolve()
_SRC = _HERE.parents[3] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from ave.core.constants import ALPHA  # noqa: E402
from ave.topological.cosserat_field_3d import (  # noqa: E402
    KAPPA_CHIRAL_ELECTRON,
    _beltrami_helicity,
    _compute_curvature,
)
from ave.topological.vacuum_engine import (  # noqa: E402
    AutoresonantCWSource,
    CosseratBeltramiSource,
    CWSource,
    PairNucleationGate,
    VacuumEngine3D,
)

np.seterr(all="ignore")

N = 32
PML = 6
PERIOD = 8.0
OMEGA_C = 2.0 * np.pi / PERIOD
LAMBDA_COS = 3.5  # Phase III-B canonical Cosserat wavelength
K_COS = 2.0 * np.pi / LAMBDA_COS
OMEGA_YIELD = float(np.pi)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def interior_mask(engine: VacuumEngine3D) -> np.ndarray:
    """Active Cosserat sites with PML cells excluded (Rule 10 / Checkpoint 7).

    mask_alive = mask_A | mask_B does NOT exclude PML; we AND with an explicit
    interior box pml <= i,j,k <= N-pml-1 so the A2_mu max is interior physics,
    not a frozen-absorbing PML artifact.
    """
    n = engine.N
    box = np.zeros((n, n, n), dtype=bool)
    box[PML : n - PML, PML : n - PML, PML : n - PML] = True
    return engine.cos.mask_alive & box


def measure(engine: VacuumEngine3D, gate: PairNucleationGate, imask: np.ndarray) -> dict:
    """Snapshot the dynamical Cosserat + K4 observables, interior-masked.

    A2_mu uses the gate's canonical _compute_A2_mu (reads engine.cos.omega ->
    the actually-evolved field). We ALSO report A2_mu_base (no chirality
    factor) to isolate the <=0.88% (1+kappa_chiral*h) modulation from genuine
    omega build-up.
    """
    omega = np.asarray(engine.cos.omega)
    kappa = np.asarray(_compute_curvature(omega, engine.cos.dx))
    kappa_sq = np.sum(kappa * kappa, axis=(-1, -2))
    a2_mu_base = kappa_sq / (OMEGA_YIELD**2)
    a2_mu = np.asarray(gate._compute_A2_mu(engine))  # canonical (with chirality)

    Vsq = np.sum(np.asarray(engine.k4.V_inc) ** 2, axis=-1)
    a2_k4 = Vsq / (engine.V_SNAP**2)

    eps_str = None
    if imask.any():
        a2_mu_max = float(a2_mu[imask].max())
        a2_mu_base_max = float(a2_mu_base[imask].max())
        a2_k4_max = float(a2_k4[engine.k4.mask_active & _interior_box(engine)].max())
        omega_max = float(np.abs(omega[imask]).max())
        omega_dot_max = float(np.abs(np.asarray(engine.cos.omega_dot)[imask]).max())
    else:
        a2_mu_max = a2_mu_base_max = a2_k4_max = omega_max = omega_dot_max = 0.0

    # Rupture: any interior site with total A2 >= 1
    a2_total = a2_k4  # K4 contribution; Cosserat A2 from gate kernel
    rupture_k4 = bool((a2_total[engine.k4.mask_active & _interior_box(engine)] >= 1.0).any())
    rupture_cos = bool(a2_mu_max >= 1.0)

    H = float(engine._coupled.total_hamiltonian())
    return {
        "t": float(engine.time),
        "A2_mu": a2_mu_max,
        "A2_mu_base": a2_mu_base_max,
        "A2_K4": a2_k4_max,
        "omega_max": omega_max,
        "omega_dot_max": omega_dot_max,
        "H": H,
        "rupture": rupture_k4 or rupture_cos,
    }


def _interior_box(engine: VacuumEngine3D) -> np.ndarray:
    n = engine.N
    box = np.zeros((n, n, n), dtype=bool)
    box[PML : n - PML, PML : n - PML, PML : n - PML] = True
    return box


def seed_beltrami_omega(engine: VacuumEngine3D, a2_mu_target: float) -> float:
    """Paint a clean interior Beltrami omega initial condition calibrated to a
    target A2_mu_base, then return the realized interior A2_mu_base.

    omega(x) = amp*(0, cos(k x), sin(k x)) -> |curl omega| ~ amp*k ->
    A2_mu_base ~ (amp*k/pi)^2. Solve amp = pi*sqrt(target)/k, paint interior
    only, measure the actual realized A2_mu_base.
    """
    amp = OMEGA_YIELD * np.sqrt(max(a2_mu_target, 0.0)) / K_COS
    n = engine.N
    xs = np.arange(n)
    phase = K_COS * xs
    omega = np.zeros((n, n, n, 3), dtype=float)
    cos_kx = np.cos(phase)[:, None, None]
    sin_kx = np.sin(phase)[:, None, None]
    omega[..., 1] = amp * np.broadcast_to(cos_kx, (n, n, n))
    omega[..., 2] = amp * np.broadcast_to(sin_kx, (n, n, n))
    box = _interior_box(engine)
    omega[~(engine.cos.mask_alive & box)] = 0.0
    engine.cos.omega[:] = omega
    kappa = np.asarray(_compute_curvature(engine.cos.omega, engine.cos.dx))
    kappa_sq = np.sum(kappa * kappa, axis=(-1, -2))
    a2 = kappa_sq / (OMEGA_YIELD**2)
    imask = interior_mask(engine)
    return float(a2[imask].max()) if imask.any() else 0.0


def make_engine(disable_lc: bool, temperature: float = 0.0, seed: int | None = None) -> VacuumEngine3D:
    eng = VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=temperature,
        amplitude_convention="V_SNAP",
        use_memristive_saturation=True,
        disable_cosserat_lc_force=disable_lc,
        enable_cosserat_self_terms=False,
    )
    if temperature > 0 and seed is not None:
        # Re-thermalize with a fixed seed for reproducibility
        eng.initialize_thermal(temperature, seed=seed)
    return eng


def add_k4_drive(eng: VacuumEngine3D, amp: float, resonant: bool, n_periods_sustain: float = 20.0) -> None:
    off = PML + 3
    t_ramp = 2.0 * PERIOD
    t_sustain = n_periods_sustain * PERIOD
    Src = AutoresonantCWSource if resonant else CWSource
    eng.add_source(
        Src(
            x0=off,
            direction=(1.0, 0.0, 0.0),
            amplitude=amp,
            omega=OMEGA_C,
            sigma_yz=3.0,
            t_ramp=t_ramp,
            t_sustain=t_sustain,
        )
    )
    eng.add_source(
        Src(
            x0=N - off,
            direction=(-1.0, 0.0, 0.0),
            amplitude=amp,
            omega=OMEGA_C,
            sigma_yz=3.0,
            t_ramp=t_ramp,
            t_sustain=t_sustain,
        )
    )


def run_trajectory(eng: VacuumEngine3D, n_steps: int, record_every: int = 10) -> dict:
    gate = PairNucleationGate(cadence=record_every)
    eng.add_observer(gate)
    imask = interior_mask(eng)
    traj = []
    peak = {"A2_mu": 0.0, "A2_K4": 0.0, "omega_max": 0.0}
    for s in range(n_steps):
        eng.step()
        if eng.step_count % record_every == 0:
            m = measure(eng, gate, imask)
            traj.append(m)
            peak["A2_mu"] = max(peak["A2_mu"], m["A2_mu"])
            peak["A2_K4"] = max(peak["A2_K4"], m["A2_K4"])
            peak["omega_max"] = max(peak["omega_max"], m["omega_max"])
    final = measure(eng, gate, imask)
    return {"trajectory": traj, "peak": peak, "final": final}


# ---------------------------------------------------------------------------
# Arms
# ---------------------------------------------------------------------------
def arm1_cold_k4(amps, n_steps=200) -> list[dict]:
    """Cold (T=0), K4-only, legacy pump ON. Autoresonant vs fixed-f.

    Expectation (and corpus doc 50_:131): A2_mu = 0 exactly; autoresonant ==
    fixed-f. The Q knob does nothing on a cold (traceless) photon -- no seed
    channel.
    """
    rows = []
    for resonant in (True, False):
        for amp in amps:
            eng = make_engine(disable_lc=False, temperature=0.0)
            add_k4_drive(eng, amp, resonant=resonant)
            r = run_trajectory(eng, n_steps)
            rows.append(
                {
                    "arm": "cold_k4",
                    "source": "autoresonant" if resonant else "fixed_f",
                    "amp": amp,
                    "peak_A2_mu": r["peak"]["A2_mu"],
                    "peak_A2_K4": r["peak"]["A2_K4"],
                    "peak_omega": r["peak"]["omega_max"],
                    "final": r["final"],
                }
            )
            print(
                f"[arm1 cold] src={'auto' if resonant else 'fixd'} amp={amp:.2f} "
                f"-> A2_mu={r['peak']['A2_mu']:.3e} A2_K4={r['peak']['A2_K4']:.3e} "
                f"omega={r['peak']['omega_max']:.3e}",
                flush=True,
            )
    return rows


def arm2_seeded_amplify(amps, a2_mu_seed=0.012, n_steps=260) -> list[dict]:
    """Seed a clean interior Beltrami omega (A2_mu ~ 0.012, the phase5e anchor),
    then drive K4 autoresonant at swept amplitude (rising Q build-up) with NO
    Cosserat source. Pure test of whether the coupling AMPLIFIES the seed.

    Run legacy (pump ON, disable_lc=False) AND A28-correct (pump OFF,
    disable_lc=True). KNOB if A2_mu grows with K4 build-up; WALL if A2_mu
    stays ~seed (or decays). Track A2_mu(t) to distinguish stable-lock vs
    runaway vs decay.
    """
    rows = []
    for disable_lc in (False, True):
        for amp in amps:
            eng = make_engine(disable_lc=disable_lc, temperature=0.0)
            realized_seed = seed_beltrami_omega(eng, a2_mu_seed)
            add_k4_drive(eng, amp, resonant=True)
            r = run_trajectory(eng, n_steps)
            traj_a2 = [m["A2_mu"] for m in r["trajectory"]]
            rows.append(
                {
                    "arm": "seeded_amplify",
                    "config": "A28_pumpOFF" if disable_lc else "legacy_pumpON",
                    "amp": amp,
                    "realized_seed_A2_mu": realized_seed,
                    "peak_A2_mu": r["peak"]["A2_mu"],
                    "final_A2_mu": r["final"]["A2_mu"],
                    "peak_A2_K4": r["peak"]["A2_K4"],
                    "rupture": r["final"]["rupture"],
                    "A2_mu_traj": traj_a2,
                    "final": r["final"],
                }
            )
            print(
                f"[arm2 seed] {('A28-OFF' if disable_lc else 'legacy-ON'):>9} amp={amp:.2f} "
                f"seed={realized_seed:.4f} -> peak_A2_mu={r['peak']['A2_mu']:.4f} "
                f"final_A2_mu={r['final']['A2_mu']:.4f} A2_K4={r['peak']['A2_K4']:.3e} "
                f"rupture={r['final']['rupture']}",
                flush=True,
            )
    return rows


def arm3_beltrami_painted(amps, n_steps=160) -> list[dict]:
    """Drive ONLY with CosseratBeltramiSource at swept amplitude. A2_mu is set
    DIRECTLY by the source amplitude (~ (amp*k/pi)^2) -- the ALGEBRAIC /
    heuristic baseline. Demonstrates that reaching A2_mu ~ 1 (the 1.009 anchor
    regime) requires source-painting omega at amp ~ pi/k ~ 1.75, NOT a
    dynamical amplification of the alpha-weak coupling.
    """
    rows = []
    off = PML + 3
    for amp in amps:
        eng = make_engine(disable_lc=False, temperature=0.0)
        eng.add_source(
            CosseratBeltramiSource(
                x0=off,
                propagation_axis=0,
                amplitude=amp,
                omega=2.0 * np.pi / LAMBDA_COS,
                handedness="RH",
                sigma_yz=3.0,
                t_ramp=2.0 * PERIOD,
                t_sustain=18.0 * PERIOD,
            )
        )
        r = run_trajectory(eng, n_steps)
        predicted = (amp * K_COS / OMEGA_YIELD) ** 2
        rows.append(
            {
                "arm": "beltrami_painted",
                "amp": amp,
                "peak_A2_mu": r["peak"]["A2_mu"],
                "predicted_algebraic_A2_mu": predicted,
                "peak_A2_K4": r["peak"]["A2_K4"],
                "rupture": r["final"]["rupture"],
                "final": r["final"],
            }
        )
        print(
            f"[arm3 paint] amp={amp:.2f} -> peak_A2_mu={r['peak']['A2_mu']:.4f} "
            f"(algebraic pred {predicted:.4f}) rupture={r['final']['rupture']}",
            flush=True,
        )
    return rows


# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
def make_figure(arm1, arm2, arm3, out_png: Path) -> None:
    fig, (ax_main, ax_traj) = plt.subplots(1, 2, figsize=(13.5, 5.2))

    # --- Left: A2_mu vs resonant build-up (peak A2_K4) ---
    # Arm1 cold: A2_mu ~ 0 across all build-up (the WALL floor at cold-seed).
    a1_x = [r["peak_A2_K4"] for r in arm1]
    a1_y = [max(r["peak_A2_mu"], 1e-6) for r in arm1]
    ax_main.scatter(a1_x, a1_y, marker="x", s=70, color="#888888",
                    label="cold T=0, K4-only (auto+fixed): no seed")

    # Arm2 seeded: A2_mu vs K4 build-up, per config.
    for cfg, color, mk in (("legacy_pumpON", "#c0392b", "o"), ("A28_pumpOFF", "#2471a3", "s")):
        xs = [r["peak_A2_K4"] for r in arm2 if r["config"] == cfg]
        ys = [max(r["peak_A2_mu"], 1e-6) for r in arm2 if r["config"] == cfg]
        ax_main.plot(xs, ys, mk + "-", color=color, label=f"seeded omega + K4 drive ({cfg})")

    # Arm3 painted: A2_mu set by Cosserat-source amp (algebraic) -- plot vs its
    # own A2_K4 (~0, since it injects no V) but annotate the source-amp reach.
    a3_y = [max(r["peak_A2_mu"], 1e-6) for r in arm3]
    a3_x = [max(r["peak_A2_K4"], 1e-6) for r in arm3]
    ax_main.scatter(a3_x, a3_y, marker="^", s=70, color="#27ae60",
                    label="Beltrami-painted omega (algebraic source)")

    # Anchors
    ax_main.axhline(0.012, ls=":", color="#7f8c8d", lw=1.2)
    ax_main.text(ax_main.get_xlim()[0], 0.0125, "  0.012  (Phase-5e anchor, thermal seed)",
                 va="bottom", fontsize=8, color="#7f8c8d")
    ax_main.axhline(1.0, ls="--", color="#000000", lw=1.0)
    ax_main.text(ax_main.get_xlim()[0], 1.02, "  A2_mu=1  rupture / 1.009 anchor",
                 va="bottom", fontsize=8, color="#000000")
    ax_main.set_xscale("log")
    ax_main.set_yscale("log")
    ax_main.set_xlabel("resonant build-up of driven sector  (peak A2_K4)")
    ax_main.set_ylabel("dynamical Cosserat A2_mu (interior, PML-excluded)")
    ax_main.set_title("A2_mu vs Q (resonant build-up)")
    ax_main.legend(fontsize=7, loc="lower right")
    ax_main.grid(True, which="both", alpha=0.2)

    # --- Right: A2_mu(t) trajectories for the seeded amplify arm (lock window?) ---
    for r in arm2:
        traj = r["A2_mu_traj"]
        if not traj:
            continue
        ts = np.arange(len(traj))
        ls = "-" if r["config"] == "legacy_pumpON" else "--"
        color = plt.cm.viridis(min(r["amp"] / 1.6, 1.0))
        ax_traj.plot(ts, traj, ls=ls, color=color,
                     label=f"{r['config'][:6]} amp={r['amp']:.1f}")
    ax_traj.axhline(0.012, ls=":", color="#7f8c8d", lw=1.0)
    ax_traj.axhline(1.0, ls="--", color="#000000", lw=1.0)
    ax_traj.set_xlabel("record step (x10 engine steps)")
    ax_traj.set_ylabel("A2_mu (interior)")
    ax_traj.set_title("seeded-omega A2_mu(t): amplify / lock / decay?")
    ax_traj.legend(fontsize=6, ncol=2, loc="upper right")
    ax_traj.grid(True, alpha=0.2)

    fig.suptitle(
        "K4<->Cosserat (Op14 trace-reversal) coupling: A2_mu vs resonant Q  "
        f"(kappa_chiral = alpha*1.2 = {KAPPA_CHIRAL_ELECTRON:.3e})",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=130)
    print(f"[figure] wrote {out_png}", flush=True)


def main() -> None:
    t0 = time.time()
    print(f"alpha={ALPHA:.6e}  kappa_chiral={KAPPA_CHIRAL_ELECTRON:.6e}  omega_yield={OMEGA_YIELD:.4f}", flush=True)

    amps_k4 = [0.3, 0.6, 1.0]
    amps_seed = [0.3, 0.6, 1.0, 1.5]
    amps_paint = [0.2, 0.5, 1.0, 1.75]

    arm1 = arm1_cold_k4(amps_k4)
    arm2 = arm2_seeded_amplify(amps_seed)
    arm3 = arm3_beltrami_painted(amps_paint)

    out_dir = _HERE.parents[3] / "research"
    out_json = out_dir / "2026-06-09_a2mu-vs-Q-crux_data.json"
    out_png = out_dir / "2026-06-09_a2mu-vs-Q-crux_figure.png"

    payload = {
        "meta": {
            "N": N,
            "pml": PML,
            "alpha": ALPHA,
            "kappa_chiral": KAPPA_CHIRAL_ELECTRON,
            "omega_yield": OMEGA_YIELD,
            "anchors": {"phase5e_thermal": 0.012, "doc50_autoresonant_tail": 1.009},
            "elapsed_s": None,
        },
        "arm1_cold_k4": arm1,
        "arm2_seeded_amplify": [{k: v for k, v in r.items() if k != "A2_mu_traj"} | {"A2_mu_traj": r["A2_mu_traj"]} for r in arm2],
        "arm3_beltrami_painted": arm3,
    }
    payload["meta"]["elapsed_s"] = time.time() - t0
    out_json.write_text(json.dumps(payload, indent=2))
    print(f"[json] wrote {out_json}", flush=True)

    make_figure(arm1, arm2, arm3, out_png)
    print(f"[done] elapsed {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
