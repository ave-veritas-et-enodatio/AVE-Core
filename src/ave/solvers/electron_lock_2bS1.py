"""Electron-lock 2b-Stage-1 — the BINDING test as a parallel coupling-mode sweep.

Prereg (FROZEN, governs this harness):
    research/2026-07-07_electron-lock-2bS1_prereg_FROZEN.md
Extends the #569 frozen equivalent circuit:
    research/2026-07-07_electron-equivalent-circuit.md

THE ONE QUESTION (prereg §0): does a coupling mode make the empty CAPACITIVE "3"
(V-sector / q-tank) POPULATE from the ringing INDUCTIVE "2" (Cosserat / d-tank)
and SELF-SUSTAIN at ZERO external drive?

SCOPE (prereg §0a): FILLING/BINDING (tanks TUNED to the (2,3) ratio ω_q/ω_d=3/2),
NOT selection over 1:1 (deferred topological question). Reduced-order
equivalent-circuit register, NOT the 3D lattice.

MODEL (prereg §3). Two nonlinear LC tanks in (V,I), non-dimensionalized to ω_d=1,
voltage in units of V_s = Z0·I_max. The ONLY nonlinearity is the Ax4 kernel
S(A)=√(1−A²). All couplings derive from a coupling energy E_c so the total
Ĥ = ê_d + ê_q + ê_c is conserved BY CONSTRUCTION (Ax3-lossless, zero drive):
H-drift is therefore a pure numerical/pump diagnostic, not physics.

    d-tank ("2", Cosserat inductive, SEEDED):
        C_d = C_cell (cold linear);  L_d = L_cell/S(i_d)
    q-tank ("3", V-sector capacitive, EMPTY fill-target):
        C_q = C_q0·S(v_q/v_yield) (collapse cap, Op14 varactor);  L_q = L_cell/S(i_q)
        C_q0 = C_cell/ratio²  ⇒  ω_q/ω_d = ratio  (=3/2 for the (2,3) tuning)

ARMS (prereg §3, the §9 hierarchy fork):
    mutual_M          E_c = κ·i_d·i_q                         (bilinear; A1 slow-bias set)
    co_equal          E_c = κ·i_d·i_q·[1 + g·(i_d²+i_q²)]     (symmetric nonlinear, no hierarchy)
    coupling_varactor E_c = ĉ·(v_d−v_q)²                      (bridging cap; TAUTOLOGY control)

DOUBLE-COUNT LANDMINE (prereg §5). mutual_M / co_equal couple through the
INDUCTIVE flux channel (E_c depends on currents), orthogonal to the q-tank's
capacitive collapse cap C_q(v_q) — the Op14 varactor is carried ONCE, by C_q,
computed SOLELY from v_q. NO ∝V_inc EMF term is added (that is the exact term
that double-counts C_eff, k4_cosserat_coupling.py:223 use_lagrangian_emf_coupling).
`reconcile_q_cap_energy()` proves the q-cap energy recomputes from v_q alone.

FIREWALL (prereg §4). Component VALUES from ave.core.constants (consistency-class).
The FILL/SUSTAIN/SELECT verdict (emergence-class) is topological/scale-invariant:
it depends only on dimensionless (ratio, κ, g, seed_frac, ĉ), none m_e/α-derived.
No ALPHA / M_E token appears on the outcome path (`firewall_scan()` asserts it).
"""

from __future__ import annotations

import ast
import io
import tokenize
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from ave.axioms.scale_invariant import saturation_factor
from ave.core.constants import C_CELL, L_CELL, OMEGA_C, V_YIELD, Z_0
from ave.core.fdtd_3d import I_MAX_MU

# ── canonical datasheet anchors (consistency-class; prereg §4) ──────────────
I_MAX: float = I_MAX_MU  # ≈ 124.384 A  (= XI_TOPO·C_0, μ-grade circulation threshold)
V_S: float = Z_0 * I_MAX  # natural voltage scale ≈ 46.9 kV
V_YIELD_HAT: float = V_YIELD / V_S  # ≈ 0.931 — where the collapse cap knees (α-echo MAGNITUDE only)
OMEGA_D: float = OMEGA_C  # d-tank frequency anchor (the reference; normalized to 1)

# ── FROZEN thresholds (prereg §7; dimensionless, m_e-free, α-free) ──────────
FILL_THRESH: float = 0.05  # q holds ≥5% of total energy — a substantial populate from ~0
SUSTAIN_THRESH: float = 0.01  # q back-half minimum ≥1% — does not empty back to zero
H_GATE: float = 0.02  # H-drift <2% — conservative, not detonating
LOCK_GATE: float = np.pi  # |ψ| drift < π over the back-half — phase-locked
TAUT_CORR: float = 0.9  # corr(v_q,v_d) > 0.9 ⇒ divider co-keying
TAUT_FAST_FRAC: float = 0.25  # t_fill < 0.25·T_common ⇒ instantaneous fill

# ── FROZEN coupling strengths + run geometry (prereg §3, §6) ────────────────
KAPPA0: float = 0.15
G0: float = 4.0
C_HAT0: float = 0.30  # C_c = 0.30·C_q0 ⇒ ĉ = C_c/C_cell = 0.30/ratio²
SEED_FRAC0: float = 0.30
N_COMMON: int = 120  # recording window = 120 common (2,3) periods
PTS_PER_Q_CYCLE: int = 100

PHI: float = (1.0 + np.sqrt(5.0)) / 2.0  # golden ratio — the can-fire (wrong-ratio) config

_SMIN: float = 1.0e-3  # kernel clamp floor (rupture guard); S never divides by 0


def S(a: np.ndarray | float) -> np.ndarray | float:
    """Ax4 saturation kernel S(A)=√(1−A²), clamped to [_SMIN,1] (rupture guard).

    Canonical kernel: ave.axioms.scale_invariant.saturation_factor (yield_limit=1
    ⇒ A is already the normalized ratio). The ONLY nonlinearity in the model."""
    s = saturation_factor(np.asarray(a, dtype=float), yield_limit=1.0)
    return np.maximum(s, _SMIN)


@dataclass
class ArmParams:
    """A single run configuration (all dimensionless)."""

    mode: str  # "mutual_M" | "co_equal" | "coupling_varactor"
    ratio: float = 1.5  # ω_q/ω_d ; 3/2 = the (2,3) tuning
    kappa: float = KAPPA0
    g: float = G0
    seed_frac: float = SEED_FRAC0
    c_frac: float = C_HAT0  # C_c / C_q0
    v_yield_hat: float = V_YIELD_HAT

    @property
    def c_hat(self) -> float:
        """ĉ = C_c/C_cell = c_frac·(C_q0/C_cell) = c_frac/ratio²."""
        return self.c_frac / self.ratio**2


# ── the vector field (prereg §3 normalized canonical equations) ─────────────
def _derivs(y: np.ndarray, p: ArmParams) -> np.ndarray:
    vd, id_, vq, iq = y
    Sd = S(id_)  # d-inductor kernel (current-keyed)
    Sq = S(iq)  # q-inductor kernel (current-keyed)
    Sqc = S(vq / p.v_yield_hat)  # q-cap COLLAPSE kernel (voltage-keyed; Op14 varactor)
    r2 = p.ratio**2

    # base (uncoupled) canonical LC dynamics
    dvd = id_
    did = -vd * Sd
    dvq = (r2 / Sqc) * iq
    diq = -vq * Sq

    if p.mode == "mutual_M":
        # bilinear inductive coupling — enters the dv equations (momentum-space)
        dvd += 0.5 * p.kappa * Sd * iq
        dvq += (r2 / Sqc) * 0.5 * p.kappa * Sq * id_
    elif p.mode == "co_equal":
        dvd += 0.5 * p.kappa * Sd * iq * (1.0 + p.g * (3.0 * id_**2 + iq**2))
        dvq += (r2 / Sqc) * 0.5 * p.kappa * Sq * id_ * (1.0 + p.g * (3.0 * iq**2 + id_**2))
    elif p.mode == "coupling_varactor":
        # bridging-cap potential coupling — enters the di equations (position-space)
        did += -p.c_hat * Sd * (vd - vq)
        diq += (r2 / Sqc) * p.c_hat * Sq * (vd - vq)
    else:  # pragma: no cover - guarded by ArmParams construction
        raise ValueError(f"unknown coupling mode {p.mode!r}")

    return np.array([dvd, did, dvq, diq])


def _rk4(y: np.ndarray, p: ArmParams, dt: float) -> np.ndarray:
    k1 = _derivs(y, p)
    k2 = _derivs(y + 0.5 * dt * k1, p)
    k3 = _derivs(y + 0.5 * dt * k2, p)
    k4 = _derivs(y + dt * k3, p)
    return y + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)


# ── normalized energies (closed form; the H-ledger, prereg §6) ──────────────
def _e_couple(y: np.ndarray, p: ArmParams) -> float:
    vd, id_, vq, iq = y
    if p.mode == "mutual_M":
        return float(p.kappa * id_ * iq)
    if p.mode == "co_equal":
        return float(p.kappa * id_ * iq * (1.0 + p.g * (id_**2 + iq**2)))
    if p.mode == "coupling_varactor":
        return float(p.c_hat * (vd - vq) ** 2)
    raise ValueError(p.mode)  # pragma: no cover


def _energies(y: np.ndarray, p: ArmParams) -> tuple[float, float, float]:
    """(e_d, e_q, e_c) — normalized by E_scale=½L_cell·I_max². q-cap energy uses
    v_q ALONE (the double-count guard: the Op14 collapse cap is carried once)."""
    vd, id_, vq, iq = y
    e_Ld = 2.0 * (1.0 - S(id_))
    e_Cd = vd**2
    e_Lq = 2.0 * (1.0 - S(iq))
    e_Cq = (2.0 * p.v_yield_hat**2 / (3.0 * p.ratio**2)) * (1.0 - S(vq / p.v_yield_hat) ** 3)
    return float(e_Ld + e_Cd), float(e_Lq + e_Cq), _e_couple(y, p)


@dataclass
class ArmResult:
    params: ArmParams
    fill_max: float
    fill_mean: float
    fill_min: float
    h_drift: float
    lock_drift: float
    w_d: float
    w_q: float
    div_corr: float
    t_fill_frac: float  # t_fill / T_common (np.inf if never fills)
    ruptured: bool
    bin: str = ""
    series: dict = field(default_factory=dict, repr=False)


def run_arm(p: ArmParams, *, n_common: int = N_COMMON, keep_series: bool = False) -> ArmResult:
    """Integrate one arm at ZERO drive from an inductive d-seed; return metrics.

    Seed: i_d(0)=seed_frac (the "2" rings); v_d=v_q=i_q=0 (the "3" is empty)."""
    T_d = 2.0 * np.pi  # ω_d=1
    T_q = 2.0 * np.pi / p.ratio
    # (2,3) common period = 2·T_d = 3·T_q (d winds 2×, q winds 3×). Used as the
    # window unit + t_fill normalizer; the winding-2 reference for every config.
    T_common = 2.0 * T_d
    dt = T_q / PTS_PER_Q_CYCLE
    t_max = n_common * T_common
    n_steps = int(np.ceil(t_max / dt))

    y = np.array([0.0, p.seed_frac, 0.0, 0.0])  # inductive d-seed only
    H0 = sum(_energies(y, p))

    vd_s = np.empty(n_steps + 1)
    id_s = np.empty(n_steps + 1)
    vq_s = np.empty(n_steps + 1)
    iq_s = np.empty(n_steps + 1)
    eq_s = np.empty(n_steps + 1)
    H_s = np.empty(n_steps + 1)
    t_s = np.empty(n_steps + 1)

    ruptured = False
    for k in range(n_steps + 1):
        vd_s[k], id_s[k], vq_s[k], iq_s[k] = y
        ed, eq, ec = _energies(y, p)
        eq_s[k] = eq
        H_s[k] = ed + eq + ec
        t_s[k] = k * dt
        if abs(vq_s[k]) >= p.v_yield_hat or abs(id_s[k]) >= 1.0 or abs(iq_s[k]) >= 1.0:
            ruptured = True
        if k < n_steps:
            y = _rk4(y, p, dt)

    eq_frac = eq_s / H0
    half = n_steps // 2
    fill_max = float(np.max(eq_frac))
    fill_mean = float(np.mean(eq_frac[half:]))
    fill_min = float(np.min(eq_frac[half:]))
    h_drift = float(np.max(np.abs(H_s - H0)) / abs(H0))

    # phase-space winding + lock (A46; each phase-plane whitened to its own std)
    def _phase(v: np.ndarray, i: np.ndarray) -> np.ndarray:
        sv = np.std(v) or 1.0
        si = np.std(i) or 1.0
        return np.unwrap(np.arctan2(i / si, v / sv))

    th_d = _phase(vd_s, id_s)
    th_q = _phase(vq_s, iq_s)
    w_d = float((th_d[-1] - th_d[0]) / (2.0 * np.pi))
    w_q = float((th_q[-1] - th_q[0]) / (2.0 * np.pi))
    psi = 3.0 * th_d - 2.0 * th_q  # resonant (2,3) combination
    lock_drift = float(np.max(psi[half:]) - np.min(psi[half:]))

    # independence / co-keying (anti-tautology): corr(v_q, v_d) is scale-invariant,
    # so it equals corr with the capacitive-divider image (∝ v_d) — prereg §6.
    if np.std(vq_s) > 1e-12 and np.std(vd_s) > 1e-12:
        div_corr = float(abs(np.corrcoef(vq_s, vd_s)[0, 1]))
    else:
        div_corr = 0.0

    crossings = np.where(eq_frac >= FILL_THRESH)[0]
    t_fill_frac = float(t_s[crossings[0]] / T_common) if crossings.size else float(np.inf)

    res = ArmResult(
        params=p,
        fill_max=fill_max,
        fill_mean=fill_mean,
        fill_min=fill_min,
        h_drift=h_drift,
        lock_drift=lock_drift,
        w_d=abs(w_d),
        w_q=abs(w_q),
        div_corr=div_corr,
        t_fill_frac=t_fill_frac,
        ruptured=ruptured,
    )
    if keep_series:
        res.series = {"t": t_s, "vd": vd_s, "id": id_s, "vq": vq_s, "iq": iq_s, "eq_frac": eq_frac, "H": H_s}
    return res


def classify(res_main: ArmResult, res_golden: ArmResult) -> str:
    """Route the frozen bin (prereg §7) for the 3:2 config, using the golden-ratio
    run as the can-fire (selectivity) control. Reported honestly; never rationalized."""
    p = res_main.params
    is_inductive = p.mode in ("mutual_M", "co_equal")
    co_keyed = (res_main.div_corr > TAUT_CORR) and (res_main.t_fill_frac < TAUT_FAST_FRAC)
    golden_sustains = (res_golden.fill_mean >= FILL_THRESH) and (res_golden.fill_min >= SUSTAIN_THRESH)

    # TAUTOLOGY: co-keying divider fill OR vacuous can-fire (golden also sustains)
    if (co_keyed and not is_inductive) or golden_sustains:
        # only call it tautology if the main config actually fills (else it's just DOESN'T-FILL)
        if res_main.fill_max >= FILL_THRESH:
            return "TAUTOLOGY"

    if res_main.fill_max < FILL_THRESH:
        return "DOESN'T-FILL"

    fills_and_sustains = (
        res_main.fill_mean >= FILL_THRESH
        and res_main.fill_min >= SUSTAIN_THRESH
        and res_main.h_drift < H_GATE
        and res_main.lock_drift < LOCK_GATE
        and not (co_keyed and not is_inductive)
        and not golden_sustains
    )
    if fills_and_sustains:
        return "FILLS-AND-SUSTAINS"
    return "FILLS-BUT-DECAYS"


# ── the double-count guard: q-cap energy reconciles from v_q ALONE ──────────
def reconcile_q_cap_energy(p: ArmParams, v_samples: np.ndarray | None = None):
    """ReconcileGate: the CLOSED-FORM q-cap energy (used in the fill metric) vs an
    INDEPENDENT numerical quadrature of ∫₀^v v'·C_q(v')dv' — a different code path,
    depending ONLY on v_q (never on the coupling E_c). Proves the Op14 collapse cap
    is carried once (prereg §5). Returns a ReconcileGateResult (can-fire proven)."""
    from ave.validation.reconcile_gate import ReconcileGate

    if v_samples is None:
        v_samples = np.linspace(0.0, 0.6 * p.v_yield_hat, 13)
    pref = 2.0 * p.v_yield_hat**2 / (3.0 * p.ratio**2)

    def closed() -> np.ndarray:
        return pref * (1.0 - S(v_samples / p.v_yield_hat) ** 3)

    def independent() -> np.ndarray:  # numerical quadrature — different code path
        out = []
        for v in v_samples:
            grid = np.linspace(0.0, v, 4000)
            # U_C,q(v)=∫₀^v v'·C_q(v')/C_q0 dv' normalized; C_q/C_q0 = S(v'/v_yield);
            # E_scale-normalized prefactor (2/(3·ratio²))·v_yield² folds into the same units.
            integrand = grid * S(grid / p.v_yield_hat)
            out.append((2.0 / p.ratio**2) * np.trapezoid(integrand, grid))
        return np.array(out)

    gate = ReconcileGate(
        label=f"q_cap_energy[{p.mode},r={p.ratio:.3f}]",
        claimed=closed,
        independent=independent,
        rtol=1e-3,
        atol=1e-9,
    )
    return gate.enforce(prove_first=True)


# ── firewall: no ALPHA / M_E token on the outcome path (prereg §4, §10) ──────
_OUTCOME_FUNCS = ("_derivs", "_energies", "_e_couple", "run_arm", "classify", "S")
_FORBIDDEN_TOKENS = ("ALPHA", "ALPHA_COLD_INV", "M_E", "m_e")


def firewall_scan(module_path: str | Path | None = None) -> dict:
    """AST-extract each outcome function's source span, tokenize it, and assert no
    m_e/α NAME token appears in the FILL/SUSTAIN/SELECT logic. Component-value
    imports at module scope are consistency-class and permitted; the OUTCOME must be
    scale-invariant. Docstrings (STRING tokens) are ignored — only NAME tokens count,
    so a mention of α in a comment/docstring is not a violation, a *use* is."""
    path = Path(module_path) if module_path else Path(__file__)
    src = path.read_text()
    tree = ast.parse(src)
    hits: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in _OUTCOME_FUNCS:
            func_src = ast.get_source_segment(src, node) or ""
            for tok in tokenize.generate_tokens(io.StringIO(func_src).readline):
                if tok.type == tokenize.NAME and tok.string in _FORBIDDEN_TOKENS:
                    hits.append(f"{node.name}: {tok.string} (line {node.lineno + tok.start[0] - 1})")
    return {"clean": len(hits) == 0, "hits": hits, "outcome_funcs": list(_OUTCOME_FUNCS)}
