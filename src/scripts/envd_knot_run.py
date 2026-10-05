"""ENV-D knot run driver.

Adapts ENV-1c run 2 (~/AVE-runs/ENV-1c/run2/env1c_run2.py) for the ENV-D bond
reflection form with the ENVD-E1 substep driver.

Provenance:
  Method sheet  : ENVD-bond-reflection-method-sheet_2026-10-03.md sha1 342a3254859e §5
  Erratum E1    : ENVD-erratum-E1-rulings_2026-10-04.md sha1 7e3d5d83bd0f
  U4 class      : ENVD-U4-classification_2026-10-04.md sha1 6ed389b0b982
  WRAP rule     : Addendum 4 / R26.168 — per-site vector length |omega|=sqrt(wx^2+wy^2+wz^2)
  Base run      : ~/AVE-runs/ENV-1c/run2/env1c_run2.py
  AVE-Core base : main b51165c6 (PR #1059 + #1060 merged)

Config delta vs ENV-1c run2:
  k_refl          : 0.0  -> 1.0
  reflection_form : "grad" (default) -> "bond"
  reflection_delta: default -> 1e-3 (passed explicitly to constructor)
  G0 share gate   : not gated (k_refl=0 in run2) -> refl_share <= 5%

Adaptive n_sub / touch rule (E1 erratum + U4 PASS-COARSE):
  Each outer cfl_dt step uses n_sub substeps of dt_sub = cfl_dt / n_sub.
  First (n_sub - 1) substeps: step(dt_sub, apply_pml=False).
  Last substep: step(dt_sub, apply_pml=True).  One PML bite per outer step,
  matching the ENV-1c absorber (E1 erratum R3).
  n_sub = N_SUB_TOUCH = 1024 at touch; falls to 1 only at a period boundary
  after a full period with zero touch.
  Touch detection choice: N_eps > 0 OR N_kap > 0 from the PREVIOUS outer
  step's per_step call (1-step lag).  This is the U4-style A2_kick / wall-
  engagement trigger (U4 classification Addendum 4): any alive site has
  A2 >= 1.  Chosen over building the full x_s_min lookup (U3) for
  robustness; the 1-step lag is negligible at the period scale (~P/dt steps).

W1-W5 wall lines (frozen per method sheet §5; W5 from U4 Addendum 3, 19:03 PT):
  W1: per-period regulator share = sum(W_refl[|1-A2| < 10*delta]) /
      sum(W_refl) over alive sites.  INCONCLUSIVE (REGULATOR) if > 1%.
      Early stop if breached 3 consecutive periods.
  W2: raw H <= H0*(1+1e-2) through every period where N_eps > 0.
      NUMERICS if violated.
  W3: count of alive-site bonds with |G_p| > 0.5 per period.
      "wall never engaged" note if REAL UNTYING occurs with W3 == 0.
  W4: n_sub history logged (max, step counts at each level).
  W5: per-quarter H linear slope > +2e-5*H0/period -> LEAK-SUSPECT /
      ENERGY-UNRESOLVED from that quarter onward.

WRAP: omega_max_alive = max over alive sites of sqrt(wx^2+wy^2+wz^2).
  If > pi at any period sample, topology lines from that period onward read
  WRAP-UNRESOLVED (energy, NUMERICS, W1-W4 unaffected; run continues).
  The U4 figure 3.868 was component-max (lower bound); this logger uses
  the full vector length per Addendum 4 / R26.168.

Early stops: NaN, H rise > 1e-2, REAL UNTYING (crossing_count drops to 0
  after period 0 and seed crossing count was > 0), melt f > 0.8, W1 breached
  3 consecutive periods.

Every verdict / wall-line log includes: platform, backend, jax version, dtype
(embedded in PLATFORM_LINE; results from different platforms are never pooled).

Outputs (in OUTDIR):
  periods.csv     all run2 columns + omega_max_alive + wrap_flag + n_sub +
                  w1_share + w3_count
  steps.csv       same columns as run2
  wall.csv        per-period W1-W5 summary
  energy_windows.csv  50-period energy windows (same as run2)
  frames/         same schedule + burst logic as run2
  meta.json       settings + provenance
  progress.log    human-readable progress
  energy_trust.json   A3 late-window trust test + W5 quarter slopes
  g0.json         start-state gate

Usage:
  PYTHONPATH=src nohup caffeinate -i .venv/bin/python src/scripts/envd_knot_run.py \\
      ~/AVE-runs/envd-knot-20261005 2000 > ~/AVE-runs/envd-knot-20261005/run_stdout.log 2>&1 &

Do NOT start the 2000-period run without a GO from the Orchestrator.
"""

import sys, os, json, time, math, hashlib, subprocess, platform
import numpy as np

OUTDIR = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
N_PERIODS = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
os.makedirs(OUTDIR, exist_ok=True)

from ave.topological import cosserat_field_3d as cf
from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    TETRA_OFFSETS,
    _compute_strain,
    _compute_curvature,
    _reflection_density_bond,
)
import jax
import jax.numpy as jnp

jax.config.update("jax_enable_x64", True)

ENGINE = os.path.abspath(cf.__file__)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(ENGINE))))
logf = open(os.path.join(OUTDIR, "progress.log"), "a", buffering=1)

def log(msg):
    logf.write(time.strftime("%Y-%m-%d %H:%M:%S %Z") + "  " + msg + "\n")

# ---------------- settings (method sheet §5; deltas vs run2 noted) ----------------
AMP = 0.17
G0_MAX_A2 = 0.5
G0_MAX_SHARE_REFL = 0.05    # method sheet §5: share <= 5% (run2 didn't gate; k_refl was 0)
WALL_SHARE = 0.10
N = 64
DELTA = 1e-3                # reflection_delta (frozen per method sheet §6)
N_SUB_TOUCH = 1024          # U4 PASS-COARSE: n_sub at touch

sim = CosseratField3D(N, N, N, dx=1.0, use_saturation=True, pml_thickness=8,
                      damping_gamma=0.0, use_impedance_boundary=False,
                      reflection_form="bond", reflection_delta=DELTA)
sim.k_refl = 1.0            # ENV-D delta: 0.0 -> 1.0
sim.initialize_electron_2_3_sector(R_target=8, r_target=3, amplitude_scale=AMP)
sim.u_dot[...] = 0.0
sim.omega_dot[...] = 0.0
assert sim.u.dtype == np.float64 and sim.omega.dtype == np.float64
dt = sim.cfl_dt             # outer CFL step; substeps use dt_sub = dt / n_sub
P = math.pi
N_STEPS = int(round(N_PERIODS * P / dt))
sample_step = {int(round(k * P / dt)): k for k in range(N_PERIODS + 1)}

# save schedule: identical to ENV-1c run2 section 2
SAVE_PERIODS = ([h / 2.0 for h in range(0, 11)]
                + list(range(6, 21))
                + list(range(30, 201, 10))
                + list(range(250, 2001, 50)))
save_step = {}
for _p in SAVE_PERIODS:
    if _p <= N_PERIODS:
        save_step.setdefault(int(round(_p * P / dt)), "sched_p%g" % _p)
FRAMEDIR = os.path.join(OUTDIR, "frames"); os.makedirs(FRAMEDIR, exist_ok=True)
BURST_EVERY, BURST_LEN = 5, 100
burst = {"first_clip_step": None, "first_clip_neps": None, "double_period": None,
         "active_until": -1, "tag": ""}
H_RISE_MAX, MELT_STOP = 1e-2, 0.8
WIN = 50; S_TRUST = 2e-5    # A3 late-window trust constants (unchanged from run2)

# ---------------- platform banner (Math Addendum 4 / R26.168) ----------------
_omega_dtype = np.asarray(sim.omega).dtype
_u_dtype = np.asarray(sim.u).dtype
PLATFORM_LINE = (
    f"platform={platform.platform()}  backend={jax.default_backend()}"
    f"  jax={jax.__version__}  omega_dtype={_omega_dtype}  u_dtype={_u_dtype}"
    f"  dtype={sim.u.dtype}"
)
print(PLATFORM_LINE)

# ---------------- geometry (identical to run2) ----------------
c0 = (N - 1) / 2.0
I, J, K = sim._i - c0, sim._j - c0, sim._k - c0
alive = sim.mask_alive
rsph = np.sqrt(I**2 + J**2 + K**2)
rho_xy = np.sqrt(I**2 + J**2)
phi = np.arctan2(J, I)
tx, ty = -np.sin(phi), np.cos(phi)
ball = alive & (rsph <= 15.0)
far = alive & (rsph >= 17.0) & (rsph <= 22.0)
far_idx = np.nonzero(far)
CORE_TUBE = 1.5

def core_mask(R):
    return alive & (np.sqrt((rho_xy - R) ** 2 + K**2) <= CORE_TUBE)

EPS_SOFT = 0.408
EPS_Y = sim.epsilon_yield
RING3 = alive & (np.sqrt((rho_xy - 8.0) ** 2 + K**2) <= 3.0)
N_RING3 = int(RING3.sum())

def fro(t):
    return np.sqrt(np.sum(t * t, axis=(-1, -2)))

# ---------------- JIT helpers ----------------
_refl_bond_jit = jax.jit(_reflection_density_bond, static_argnums=(2, 3, 4, 5))
_strain_jit = jax.jit(_compute_strain, static_argnums=(2,))
_curv_jit = jax.jit(_compute_curvature, static_argnums=(1,))


def _q_and_x(u, omega):
    """Impedance proxy q = x_s^0.25 and raw x = 1-A2 (numpy arrays)."""
    u_j = jnp.asarray(u); w_j = jnp.asarray(omega)
    eps_j = np.asarray(_strain_jit(u_j, w_j, sim.dx))
    kap_j = np.asarray(_curv_jit(w_j, sim.dx))
    eps_sq = np.sum(eps_j * eps_j, axis=(-1, -2))
    kap_sq = np.sum(kap_j * kap_j, axis=(-1, -2))
    A2 = eps_sq / sim.epsilon_yield**2 + kap_sq / sim.omega_yield**2
    x = 1.0 - A2
    r = np.sqrt(x * x + DELTA * DELTA)
    x_neg = np.where(x < 0, x, -1.0)
    r_neg = np.sqrt(x_neg * x_neg + DELTA * DELTA)
    x_s = np.where(x >= 0, 0.5 * (x + r), DELTA * DELTA / (2.0 * (r_neg - x_neg)))
    return x_s ** 0.25, x


def w1_and_w3(u, omega):
    """W1 regulator share and W3 bond-engagement count.

    W1 (method sheet §5): fraction of W_refl from sites with |1-A2| < 10*delta.
    W3 (method sheet §5): count of alive-site bonds with |G_p| > 0.5.
    Returns (w1_share, w3_count).
    """
    q, x = _q_and_x(u, omega)
    W_site = np.zeros_like(q)
    w3_count = 0
    for p in TETRA_OFFSETS:
        q_p = np.roll(q, shift=(-p[0], -p[1], -p[2]), axis=(0, 1, 2))
        G_p = (q - q_p) / (q + q_p)
        W_site += G_p * G_p
        w3_count += int(np.sum((np.abs(G_p) > 0.5) & alive))
    W_site /= (4.0 * sim.dx * sim.dx)
    near_floor = np.abs(x) < 10.0 * DELTA
    W_total = float(np.sum(W_site[alive]))
    W_floor = float(np.sum(W_site[alive & near_floor]))
    w1_share = W_floor / W_total if W_total > 0.0 else float("nan")
    return w1_share, w3_count


def m10(eps=None):
    if eps is None:
        eps = sim.compute_strain()
    kap = sim.compute_curvature()
    A2 = (np.sum(eps * eps, axis=(-1, -2)) / sim.epsilon_yield**2
          + np.sum(kap * kap, axis=(-1, -2)) / sim.omega_yield**2)
    maxA2 = float(A2[alive].max())
    n_over = int(np.sum(A2[alive] >= 1.0))
    refl = np.asarray(_refl_bond_jit(
        jnp.asarray(sim.u), jnp.asarray(sim.omega),
        sim.dx, sim.omega_yield, sim.epsilon_yield, DELTA))
    E_refl = float(sim.k_refl * np.sum(refl[alive]))
    E_pot = sim.total_energy()
    share = E_refl / E_pot if E_pot != 0 else float("nan")
    return maxA2, n_over, E_refl, E_pot, share


def m10c(eps, kap=None):
    if kap is None:
        kap = sim.compute_curvature()
    e2 = np.sum(eps * eps, axis=(-1, -2))
    k2 = np.sum(kap * kap, axis=(-1, -2))
    A2 = e2 / sim.epsilon_yield**2 + k2 / sim.omega_yield**2
    wm = np.sqrt(np.sum(sim.omega**2, -1))
    return (float(A2[alive].max()),
            int(np.sum(e2[alive] >= sim.epsilon_yield**2)),
            int(np.sum(k2[alive] >= sim.omega_yield**2)),
            int(np.sum(wm[alive] > math.pi)),
            int(np.sum(wm[ball] > math.pi)),
            int(np.sum(wm[core] > math.pi)),
            int(core.sum()))


def save_frame(n, tag):
    np.savez(os.path.join(FRAMEDIR, f"f_s{n:06d}.npz"),
             u=sim.u, omega=sim.omega, u_dot=sim.u_dot, omega_dot=sim.omega_dot,
             step=n, t=sim.time, tag=tag)

# ---------------- meta ----------------
def sh(cmd):
    try:
        return subprocess.check_output(cmd, cwd=REPO, text=True).strip()
    except Exception as e:
        return "ERR " + str(e)

meta = dict(
    sheet_envd="ENVD-bond-reflection-method-sheet_2026-10-03.md sha1 342a3254859e",
    erratum_e1="ENVD-erratum-E1-rulings_2026-10-04.md sha1 7e3d5d83bd0f",
    u4_class="ENVD-U4-classification_2026-10-04.md sha1 6ed389b0b982",
    wrap_rule="Addendum 4 / R26.168 per-site vector length |omega|=sqrt(wx^2+wy^2+wz^2)",
    base_run="~/AVE-runs/ENV-1c/run2/env1c_run2.py",
    ave_core_base="main b51165c6 (PR #1059 + #1060 merged)",
    engine=ENGINE,
    engine_sha256=hashlib.sha256(open(ENGINE, "rb").read()).hexdigest(),
    repo_head=sh(["git", "rev-parse", "HEAD"]),
    repo_status_porcelain=sh(["git", "status", "--porcelain"]),
    script_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
    python=sys.version, jax=jax.__version__, numpy=np.__version__,
    platform=platform.platform(), platform_line=PLATFORM_LINE,
    grid=N, dx=1.0, dtype="float64", pml_thickness=8, use_saturation=True,
    damping_gamma=0.0, use_impedance_boundary=False,
    seed="initialize_electron_2_3_sector(R_target=8, r_target=3, amplitude_scale=0.17)",
    reflection_form="bond", reflection_delta=DELTA, k_refl=sim.k_refl,
    config_delta_vs_run2=dict(
        k_refl="0.0 -> 1.0",
        reflection_form="grad -> bond",
        reflection_delta="default -> 1e-3 (explicit)",
        g0_share_gate="none -> <= 5%",
    ),
    n_sub_touch=N_SUB_TOUCH,
    touch_rule=(
        "n_sub = N_SUB_TOUCH when N_eps>0 or N_kap>0 from previous outer step "
        "(1-step lag, U4-style A2_kick trigger); falls to 1 only at period "
        "boundary after a full period with zero touch"
    ),
    early_stops=(
        "NaN; H rise > 1e-2*H0; REAL UNTYING (crossing_count==0 after k>10 when "
        "seed cc>0); melt f > 0.8; W1 breached 3 consecutive periods"
    ),
    wall_lines=dict(
        W1="regulator share <= 1%; INCONCLUSIVE(REGULATOR) if exceeded; stop ×3",
        W2="raw H <= H0*(1+1e-2) when N_eps>0; NUMERICS if violated",
        W3="count of alive bonds with |G_p|>0.5 per period",
        W4="n_sub history (max, step counts at each level)",
        W5="per-quarter H slope > +2e-5*H0/period -> LEAK-SUSPECT / ENERGY-UNRESOLVED",
    ),
    save_periods=SAVE_PERIODS,
    n_ring3=N_RING3,
    velocities="zero", relax=False, k4=False,
    dt=dt, P=P, n_periods=N_PERIODS, n_steps=N_STEPS,
    params=dict(G=sim.G, G_c=sim.G_c, gamma=sim.gamma, rho=sim.rho,
                I_omega=sim.I_omega, k_op10=sim.k_op10, k_refl=sim.k_refl,
                k_hopf=sim.k_hopf, omega_yield=sim.omega_yield,
                epsilon_yield=sim.epsilon_yield),
    definitions=dict(
        centre=c0,
        M1_ball="alive & |r - centre| <= 15",
        M3="extract_shell_radii()",
        M4="extract_crossing_count(), extract_hopf_charge(), find_soliton_centroids()",
        core=f"alive & sqrt((rho_xy-R)^2+z^2) <= {CORE_TUBE}",
        M5="max |omega| over core",
        M6="Frobenius |eps_sym|, |eps_anti|; max and pot-energy-weighted mean over ball",
        M7=f"core max Frobenius |eps| and fraction with |eps|>{EPS_SOFT}; dwell fraction",
        M8="mean omega.phi_hat over core and far shell",
        M9="H_total = total_hamiltonian()",
        M10c="maxA2, N_eps, N_kap, N_wrap (alive), N_wrap_ball, N_wrap_core, n_core",
        M10_legacy="max A^2, n A^2>=1, E_refl (bond form), share = E_refl/E_pot",
        omega_max_alive="max over alive of sqrt(wx^2+wy^2+wz^2) — vector length per Addendum 4",
        rereference="H0, E_ball0 = step-0 values",
        sampling="period k sampled at step round(k*P/dt)",
    ),
)
json.dump(meta, open(os.path.join(OUTDIR, "meta.json"), "w"), indent=1)
log(f"START outdir={OUTDIR} pid={os.getpid()} dt={dt:.6f} n_steps={N_STEPS}"
    f" n_periods={N_PERIODS}"
    f" script_sha256={meta['script_sha256']}"
    f" repo_head={meta['repo_head']}"
    f" status_clean={meta['repo_status_porcelain'] == ''}")
log("PLATFORM " + PLATFORM_LINE)

# ---------------- CSV headers ----------------
pcols = [
    "k", "step", "t", "H_total", "E_pot_total", "E_kin_total", "E_ball",
    "R", "r", "crossing", "hopf", "n_centroids",
    "cent_x", "cent_y", "cent_z", "cent_dist",
    "core_omega_peak", "ball_omega_peak",
    "eps_sym_max", "eps_sym_wmean", "eps_anti_max", "eps_anti_wmean",
    "eps_max_ball", "trace_eps_absmax",
    "dwell_frac", "n_steps_in_period", "core_eps_max_pmax",
    "maxA2", "n_A2_over1", "E_refl", "refl_share", "wall_touch",
    "H_rel", "E_ball_rel",
    "N_eps", "N_kap", "N_wrap", "N_wrap_ball", "N_wrap_core", "n_core", "melt_f",
    "nan", "wall_s",
    # ENV-D additions
    "omega_max_alive", "wrap_flag", "n_sub", "w1_share", "w3_count",
]
pf = open(os.path.join(OUTDIR, "periods.csv"), "w", buffering=1)
pf.write(",".join(pcols) + "\n")

scols = [
    "step", "t", "H_total", "N_eps", "N_kap",
    "core_eps_max", "core_frac_soft",
    "core_epssym_max", "core_epsanti_max", "core_omega_peak",
    "probe_core_tan", "probe_far_tan",
]
sf = open(os.path.join(OUTDIR, "steps.csv"), "w")
sf.write(",".join(scols) + "\n")

ewf = open(os.path.join(OUTDIR, "energy_windows.csv"), "w")
ewf.write("k_start,k_end,H_start,H_end,rawH_loss,rawH_loss_over_H0,"
          "window_mean_H_periods_kstart_to_kend-1,total_loss_since_step0,"
          "total_loss_over_H0\n")

wallf = open(os.path.join(OUTDIR, "wall.csv"), "w", buffering=1)
wallf.write("k,step,w1_share,w1_breach,w3_count,n_sub,omega_max_alive,"
            "wrap_flag,w2_ok,q_idx,w5_slope,w5_status\n")

# ---------------- run-state ----------------
R_cur = 8.0
REF = {}
core = core_mask(R_cur); core_idx = np.nonzero(core)
dwell_hits = 0; dwell_n = 0; core_eps_pmax = 0.0
t_wall0 = time.time()

# E1 substep state
n_sub_cur = 1
_neps_last = 0; _nkap_last = 0      # touch flags from previous outer step
_nsub_touch_this_period = False      # any touch in the current period?

# W1 breach streak
_w1_streak = 0

# W4 history
_n_sub_hist = {}                     # {n_sub_value: outer_step_count}
_n_sub_max = 1
_n_sub_change_log = []               # [(outer_step, new_n_sub)] at each change

# W5 quarter state
_QUARTER = N_PERIODS // 4 if N_PERIODS >= 4 else N_PERIODS
_w5_leak_from_quarter = None
_w5_slopes = {}

# REAL UNTYING tracking
_seed_crossing = None

H_HIST = []


def _update_nsub(outer_step):
    """Set n_sub before this outer step; called from main loop (post previous per_step)."""
    global n_sub_cur, _nsub_touch_this_period, _n_sub_max, _n_sub_change_log
    prev = n_sub_cur
    if _neps_last > 0 or _nkap_last > 0:
        n_sub_cur = N_SUB_TOUCH
        _nsub_touch_this_period = True
    # fall to 1 only at period boundary (handled at end of per_period)
    if n_sub_cur != prev:
        _n_sub_change_log.append((outer_step, n_sub_cur))
    _n_sub_max = max(_n_sub_max, n_sub_cur)
    _n_sub_hist[n_sub_cur] = _n_sub_hist.get(n_sub_cur, 0) + 1
    return n_sub_cur


def per_step(n):
    global dwell_hits, dwell_n, core_eps_pmax, _neps_last, _nkap_last
    eps = sim.compute_strain()
    kap = sim.compute_curvature()
    Hn = sim.total_hamiltonian()
    neps = int(np.sum(np.sum(eps * eps, axis=(-1, -2))[alive] >= sim.epsilon_yield**2))
    nkap = int(np.sum(np.sum(kap * kap, axis=(-1, -2))[alive] >= sim.omega_yield**2))
    _neps_last = neps
    _nkap_last = nkap
    ec = eps[core_idx]
    et = np.swapaxes(ec, -1, -2)
    e_full = fro(ec)
    e_sym = fro(0.5 * (ec + et))
    e_anti = fro(0.5 * (ec - et))
    w = sim.omega
    tan = w[..., 0] * tx + w[..., 1] * ty
    cmax = float(e_full.max()) if e_full.size else float("nan")
    wc = np.sqrt(np.sum(w[core_idx] ** 2, axis=-1))
    row = [n, sim.time, Hn, neps, nkap, cmax,
           float(np.mean(e_full > EPS_SOFT)),
           float(e_sym.max()), float(e_anti.max()), float(wc.max()),
           float(tan[core_idx].mean()), float(tan[far_idx].mean())]
    sf.write(",".join(
        f"{v:.10g}" if isinstance(v, float) else str(v) for v in row) + "\n")
    if not (math.isfinite(cmax) and math.isfinite(row[10])
            and math.isfinite(row[11]) and math.isfinite(Hn)):
        sf.flush()
        finalize(f"NaN at step {n}")
        log(f"NAN_DETECTED at step {n}; stopping")
        sys.exit(2)
    dwell_n += 1
    dwell_hits += int(cmax > EPS_SOFT)
    core_eps_pmax = max(core_eps_pmax, cmax)
    if "H0s" not in REF:
        REF["H0s"] = Hn
    if Hn - REF["H0s"] > H_RISE_MAX * REF["H0s"]:
        sf.flush()
        save_frame(n, "stop_numerics_rise")
        finalize(f"NUMERICS rise at step {n}")
        log(f"NUMERICS STOP step {n}: H rise {Hn - REF['H0s']:.6g} > 1e-2 H0"
            f" [{PLATFORM_LINE}]")
        sys.exit(4)
    if burst["first_clip_step"] is None and (neps > 0 or nkap > 0):
        burst["first_clip_step"] = n
        burst["active_until"] = n + BURST_LEN
        burst["tag"] = "burst1_firstclip"
        log(f"FIRST CLIP step {n} t={sim.time:.4f}: N_eps={neps} N_kap={nkap};"
            f" burst1 every {BURST_EVERY} steps for {BURST_LEN} steps")
    if burst["first_clip_neps"] is None and neps > 0:
        burst["first_clip_neps"] = neps
    if burst["first_clip_step"] is not None and n <= burst["active_until"]:
        start = burst["active_until"] - BURST_LEN
        if (n - start) % BURST_EVERY == 0:
            save_frame(n, burst["tag"])
    if n in save_step:
        save_frame(n, save_step[n])
    return eps


def window_report(k):
    Hs = dict(H_HIST); H0 = REF["H0s"]
    if (k - WIN) in Hs and k in Hs:
        wvals = [h for (kk, h) in H_HIST if k - WIN <= kk < k]
        loss_w = Hs[k - WIN] - Hs[k]
        row = [k - WIN, k, Hs[k - WIN], Hs[k], loss_w, loss_w / H0,
               float(np.mean(wvals)), H0 - Hs[k], (H0 - Hs[k]) / H0]
        ewf.write(",".join(
            f"{v:.12g}" if isinstance(v, float) else str(v) for v in row) + "\n")
        ewf.flush()
        log(f"ENERGY window {k-WIN}-{k}: raw-H loss {loss_w:.6g}"
            f" ({loss_w/H0:.3e} H0)")


def w5_quarter_check(k):
    """W5: check per-quarter H slope at each quarter boundary. Returns (q_idx, slope, status)."""
    global _w5_leak_from_quarter
    if k == 0:
        return None, float("nan"), "N/A"
    Hs = dict(H_HIST); H0 = REF.get("H0s")
    if H0 is None or _QUARTER == 0:
        return None, float("nan"), "N/A"
    q_idx = (k - 1) // _QUARTER
    q_end = (q_idx + 1) * _QUARTER
    if k != q_end:
        return None, float("nan"), "N/A"
    q_start = q_idx * _QUARTER
    ks_in_q = sorted(kk for kk in Hs if q_start <= kk <= q_end)
    if len(ks_in_q) < 2:
        return q_idx, float("nan"), "INSUFFICIENT"
    ks_arr = np.array(ks_in_q, dtype=np.float64)
    Hs_arr = np.array([Hs[kk] for kk in ks_in_q], dtype=np.float64)
    slope = float(np.polyfit(ks_arr, Hs_arr, 1)[0]) / H0
    _w5_slopes[q_idx] = slope
    LEAK_THRESH = S_TRUST    # 2e-5 H0 per period
    if slope > LEAK_THRESH:
        status = "LEAK-SUSPECT"
        if _w5_leak_from_quarter is None:
            _w5_leak_from_quarter = q_idx
        log(f"W5 LEAK-SUSPECT Q{q_idx} (periods {q_start}-{q_end}):"
            f" slope={slope:.4e} H0/period > {LEAK_THRESH};"
            f" ENERGY-UNRESOLVED from Q{q_idx} [{PLATFORM_LINE}]")
    else:
        status = "OK"
    return q_idx, slope, status


def finalize(reason):
    """A3 late-window trust test + W5 summary written to energy_trust.json."""
    H0 = REF.get("H0s")
    out = dict(reason=reason, H0=H0,
               label_energy_loss="left the box (radiation + numerics, not separated)",
               platform_line=PLATFORM_LINE,
               w5_quarter_slopes=_w5_slopes,
               w5_leak_from_quarter=_w5_leak_from_quarter,
               w4_n_sub_max=_n_sub_max,
               w4_n_sub_hist=_n_sub_hist,
               w4_n_sub_change_log=_n_sub_change_log)
    if H0 is None or not H_HIST:
        out["s"] = None
    else:
        Hs = dict(H_HIST); kmax = max(Hs)
        out["total_rawH_loss"] = H0 - Hs[kmax]
        out["total_rawH_loss_over_H0"] = (H0 - Hs[kmax]) / H0
        out["last_period"] = kmax
        centres, means = [], []
        for w0 in range(150, 2000, WIN):
            vals = [Hs[kk] for kk in range(w0, w0 + WIN) if kk in Hs]
            if len(vals) == WIN:
                centres.append(w0 + (WIN - 1) / 2.0)
                means.append(float(np.mean(vals)))
        out["late_windows_used"] = len(centres)
        out["late_windows_expected"] = 37
        if len(centres) >= 2:
            sl = float(np.polyfit(centres, means, 1)[0]) / H0
            out["s"] = sl
            out["abs_s_le_2e-5"] = bool(abs(sl) <= S_TRUST)
            out["energy_lines"] = "COUNT AS WRITTEN" if abs(sl) <= S_TRUST else "ENERGY-UNRESOLVED"
            if len(centres) < 37:
                out["note"] = "run stopped early: slope from partial late range"
        else:
            out["s"] = None
            out["energy_lines"] = "not computable (fewer than 2 complete late windows)"
        out["late_window_centres"] = centres
        out["late_window_mean_H"] = means
    json.dump(out, open(os.path.join(OUTDIR, "energy_trust.json"), "w"), indent=1)
    log(f"ENERGY TRUST TEST ({reason}): s={out.get('s')} (|s|<=2e-5 required)"
        f" -> {out.get('energy_lines')};"
        f" W5 leak_from_Q={_w5_leak_from_quarter} slopes={_w5_slopes};"
        f" W4 n_sub_max={_n_sub_max} hist={_n_sub_hist}"
        f" [{PLATFORM_LINE}]")


def per_period(k, n, eps):
    global R_cur, core, core_idx, dwell_hits, dwell_n, core_eps_pmax
    global _nsub_touch_this_period, n_sub_cur, _seed_crossing, _w1_streak
    Epot = sim.total_energy()
    Ekin = sim.kinetic_energy()
    H = Epot + Ekin
    dens = sim.energy_density()
    kin = (0.5 * sim.rho * np.sum(sim.u_dot**2, -1)
           + 0.5 * sim.I_omega * np.sum(sim.omega_dot**2, -1))
    E_ball = float(np.sum((dens + kin)[ball]))
    R, r = sim.extract_shell_radii()
    cc = sim.extract_crossing_count()
    hq = sim.extract_hopf_charge()
    cents = sim.find_soliton_centroids()
    if cents:
        tot = sum(c["n_cells"] for c in cents)
        cx = sum(c["center"][0] * c["n_cells"] for c in cents) / tot
        cy = sum(c["center"][1] * c["n_cells"] for c in cents) / tot
        cz = sum(c["center"][2] * c["n_cells"] for c in cents) / tot
    else:
        cx = cy = cz = float("nan")
    cd = math.sqrt((cx - c0) ** 2 + (cy - c0) ** 2 + (cz - c0) ** 2)
    wmag = np.sqrt(np.sum(sim.omega**2, -1))
    core_pk = float(wmag[core].max())

    # WRAP: vector length per Addendum 4 / R26.168
    omega_max_alive = float(wmag[alive].max())
    wrap_flag = int(omega_max_alive > math.pi)

    eb = eps[ball]; ebt = np.swapaxes(eb, -1, -2)
    es = fro(0.5 * (eb + ebt)) / EPS_Y
    ea = fro(0.5 * (eb - ebt)) / EPS_Y
    wts = dens[ball]; wsum = float(np.sum(np.abs(wts)))
    tr = np.abs(eb[..., 0, 0] + eb[..., 1, 1] + eb[..., 2, 2])
    dfrac = dwell_hits / dwell_n if dwell_n else float("nan")

    maxA2, n_over, E_refl, _, share = m10(eps)
    _a2, N_eps, N_kap, N_wrap, N_wrap_ball, N_wrap_core, n_core = m10c(eps)
    melt_f = N_eps / N_RING3

    # W1 + W3
    w1_share, w3_count = w1_and_w3(sim.u, sim.omega)
    w1_breach = int(not math.isnan(w1_share) and w1_share > 0.01)
    if w1_breach:
        _w1_streak += 1
    else:
        _w1_streak = 0

    # W2: raw H <= H0*(1+1e-2) when N_eps > 0
    H0s = REF.get("H0s", H)
    w2_ok = 1
    if N_eps > 0 and H > H0s * (1.0 + H_RISE_MAX):
        w2_ok = 0
        log(f"W2 NUMERICS period {k}: H={H:.8g} > H0*(1+1e-2)"
            f" with N_eps={N_eps} [{PLATFORM_LINE}]")

    # burst N_eps doubling
    REF.setdefault("f_hist", []).append(melt_f)
    if (burst["first_clip_neps"] is not None
            and burst["double_period"] is None
            and N_eps >= 2 * burst["first_clip_neps"]):
        burst["double_period"] = k
        burst["active_until"] = n + BURST_LEN
        burst["tag"] = "burst2_neps_double"
        log(f"N_eps DOUBLED period {k} (N_eps={N_eps} vs first {burst['first_clip_neps']})")
        save_frame(n, "burst2_neps_double")

    share = E_refl / Epot if Epot != 0 else float("nan")
    wt = int(share > WALL_SHARE)
    if "H0" not in REF:
        REF["H0"] = H; REF["E_ball0"] = E_ball
    H_HIST.append((k, H))

    # W5 quarter check
    q_idx, w5_slope, w5_status = w5_quarter_check(k)

    H_rel = H / REF["H0"] - 1.0
    E_ball_rel = E_ball / REF["E_ball0"] if REF.get("E_ball0") else float("nan")

    row = [k, n, sim.time, H, Epot, Ekin, E_ball,
           R, r, cc, hq, len(cents),
           cx, cy, cz, cd, core_pk, float(wmag[ball].max()),
           float(es.max()),
           float(np.sum(es * np.abs(wts)) / wsum) if wsum > 0 else float("nan"),
           float(ea.max()),
           float(np.sum(ea * np.abs(wts)) / wsum) if wsum > 0 else float("nan"),
           float(fro(eb).max()), float(tr.max()),
           dfrac, dwell_n, core_eps_pmax,
           maxA2, n_over, E_refl, share, wt,
           H_rel, E_ball_rel,
           N_eps, N_kap, N_wrap, N_wrap_ball, N_wrap_core, n_core, melt_f,
           0, time.time() - t_wall0,
           # ENV-D additions
           omega_max_alive, wrap_flag, n_sub_cur, w1_share, w3_count]
    bad = (any(isinstance(v, float) and not math.isfinite(v)
               for v in [H, E_ball, R, r, hq, maxA2, E_refl])
           or not np.all(np.isfinite(sim.omega)))
    row[pcols.index("nan")] = int(bad)
    pf.write(",".join(
        f"{v:.12g}" if isinstance(v, float) else str(v) for v in row) + "\n")
    sf.flush()

    # wall.csv row
    w5_slope_s = f"{w5_slope:.8g}" if not math.isnan(w5_slope) else "nan"
    q_idx_s = str(q_idx) if q_idx is not None else ""
    wallf.write(f"{k},{n},{w1_share:.8g},{w1_breach},{w3_count},{n_sub_cur},"
                f"{omega_max_alive:.8g},{wrap_flag},{w2_ok},"
                f"{q_idx_s},{w5_slope_s},{w5_status}\n")

    dwell_hits = 0; dwell_n = 0; core_eps_pmax = 0.0
    R_cur = R; core = core_mask(R_cur); core_idx = np.nonzero(core)

    # n_sub period boundary: revert to 1 if no touch in this period
    if not _nsub_touch_this_period:
        n_sub_cur = 1
    _nsub_touch_this_period = False

    if bad or k == N_PERIODS:
        save_frame(n, "final" if not bad else "stop_nan")
    el = time.time() - t_wall0
    eta = el / max(n, 1) * (N_STEPS - n)
    if wt:
        log(f"WALL-TOUCH period {k} refl_share={share:.4f} maxA2={maxA2:.4f}")
    if wrap_flag:
        log(f"WRAP period {k}: omega_max_alive={omega_max_alive:.6f} > pi;"
            f" topology lines WRAP-UNRESOLVED [{PLATFORM_LINE}]")
    log(f"period {k}/{N_PERIODS} step {n}/{N_STEPS} t={sim.time:.4f}"
        f" H={H:.8g} R={R:.3f} r={r:.3f} cross={cc} hopf={hq:.5f}"
        f" N_eps={N_eps} N_kap={N_kap} f={melt_f:.4f} H_rel={H_rel:+.3e}"
        f" w1={w1_share:.3e} w3={w3_count} n_sub={n_sub_cur}"
        f" omega_max_alive={omega_max_alive:.4f}"
        f" nan={int(bad)} elapsed={el/60:.1f}min eta={eta/60:.1f}min"
        f" [{PLATFORM_LINE}]")
    if k > 0 and k % WIN == 0:
        window_report(k)
    # melt-out early stop (same as run2 §A3)
    if k >= 200 and (k - 150) % 50 == 0:
        fslice = REF["f_hist"][k - 50:k]
        if np.mean(fslice) > MELT_STOP:
            save_frame(n, "stop_meltout")
            finalize(f"MELT-OUT at period {k}")
            log(f"MELT-OUT STOP period {k}: window mean f={np.mean(fslice):.4f}"
                f" [{PLATFORM_LINE}]")
            sys.exit(5)

    # REAL UNTYING
    if k == 0:
        _seed_crossing = cc
    elif k > 10 and _seed_crossing is not None and _seed_crossing > 0 and cc == 0:
        note = "wall never engaged (W3=0)" if w3_count == 0 else f"W3={w3_count}"
        save_frame(n, "stop_real_untying")
        finalize(f"REAL UNTYING at period {k} ({note})")
        log(f"REAL UNTYING STOP period {k}: cc=0 (seed cc={_seed_crossing}) {note}"
            f" [{PLATFORM_LINE}]")
        sys.exit(6)

    # W1×3 early stop
    if _w1_streak >= 3:
        save_frame(n, "stop_w1_breach")
        finalize(f"W1 breached {_w1_streak} consecutive periods ending at {k}")
        log(f"W1 BREACH STOP period {k}: streak={_w1_streak}"
            f" w1_share={w1_share:.4e} > 0.01 [{PLATFORM_LINE}]")
        sys.exit(7)

    return bad


# ---------------- G0 start-state gate ----------------
g0A2, g0n, g0Er, g0Ep, g0share = m10()
g0pass = (g0A2 <= G0_MAX_A2) and (math.isnan(g0share) or g0share <= G0_MAX_SHARE_REFL)
g0H0 = sim.total_hamiltonian()
json.dump(dict(max_A2=g0A2, n_sites_A2_ge_1=g0n, E_refl=g0Er, E_pot=g0Ep,
               refl_share=g0share, H0=g0H0, k_refl=sim.k_refl, delta=DELTA,
               limits=dict(max_A2=G0_MAX_A2, max_refl_share=G0_MAX_SHARE_REFL),
               passed=bool(g0pass), platform_line=PLATFORM_LINE),
          open(os.path.join(OUTDIR, "g0.json"), "w"), indent=1)
log(f"G0 max_A2={g0A2:.6f} (<={G0_MAX_A2}) share={g0share:.4e} (<={G0_MAX_SHARE_REFL})"
    f" n_A2>=1={g0n} H0={g0H0:.6f} -> {'PASS' if g0pass else 'FAIL'}"
    f" [{PLATFORM_LINE}]")
if not g0pass:
    log("G0 FAILED: not stepping.")
    sys.exit(3)

# ---------------- initial sample ----------------
eps0 = per_step(0)
dwell_hits = 0; dwell_n = 0; core_eps_pmax = 0.0
if per_period(0, 0, eps0):
    finalize("NaN at period 0")
    log("NAN_DETECTED at period 0; stopping")
    sys.exit(2)

# ---------------- main loop ----------------
for n in range(1, N_STEPS + 1):
    # E1: set n_sub from previous step's touch flags
    n_sub = _update_nsub(n)
    dt_sub = dt / n_sub
    for _sub in range(n_sub - 1):
        sim.step(dt_sub, apply_pml=False)
    sim.step(dt_sub, apply_pml=True)

    eps = per_step(n)
    if n in sample_step:
        if per_period(sample_step[n], n, eps):
            finalize(f"NaN at period sample step {n}")
            log(f"NAN_DETECTED at step {n}; stopping")
            sys.exit(2)

finalize("completed")
log(f"DONE n_steps={N_STEPS} wall={(time.time()-t_wall0)/3600:.3f} h"
    f" W4: n_sub_max={_n_sub_max} hist={_n_sub_hist}"
    f" [{PLATFORM_LINE}]")
