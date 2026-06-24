"""S2 — a conservative skew-Hermitian H_couple locking A1↔ω (winding stays independent).

FROZEN PRE-REG: research/2026-06-24_engine-s2-hcouple_prereg.md (commit 38066fd2).
This module is the S2 make-or-break gate (pre-reg §Make-or-break): a FIELD-RESOLVED
skew-Hermitian (anti-Hermitian-by-construction) H_couple in the A1↔ω SECTOR PAIR
(A1 bulk-dilatation breather = mass ↔ Cosserat micro-rotation ω = charge winding),
S(A)-gated (saturation front, FORK A=(a) intra-mechanical — NO TKI transducer),
on the α-clean host. PASSES iff ALL FOUR criteria hold; FAIL on any one; Rule-11
INCONCLUSIVE is a legit landing (no rescue).

    (1) CONSERVATION  — |dH/H| < 1e-8 over a long closed-system window
                        (precedent test_l1_photon.py:285; PR#321 reduced gen ≈1.1e-12).
    (2) NON-VACUITY   — transfer MEASURED (a_shear/ω starts EMPTY, fills) AND the
                        |L_ω| pump canary stays BOUNDED (spin_L_omega, graft_v2:300).
    (3) INDEPENDENCE  — ω keeps its OWN conserved winding integer robust under a
                        V-perturbation on the REAL arm, while the SLAVED arm
                        (ω:=F(V)) returns independence=False (reachable-False /
                        AUTO_VOID, s1_winding_conservation_gate.py:439). Normal-mode
                        SPLITTING is DECLARED EXPECTED + bounded (FORK B=(b)) — NOT
                        a violation.
    (4) REDUCED-LIMIT — H_couple recovers the 2-mode circulator generator
                        (node_circulator_coupling.py:124-157) in its 2-mode limit.

ANTI-REBUILD (Rule 14). This gate REUSES the existing immune system:
  * node_circulator_coupling.circulator_generator — the PR#321 2-mode generator,
    the VALIDATE-ON-KNOWN to RECOVER (criterion 4), NOT re-skinned as deliverable.
  * crystal_graft_v2.spin_L_omega — the |L_ω| pump canary (criterion 2 + neg-ctrl).
  * s1_winding_conservation_gate.gate_f_positive_control — the slaved-arm
    reachable-False INDEPENDENCE discriminator (criterion 3).
  * test_l1_photon.py:285 — the |dH/H| < 1e-8 conservation precedent.

GENUINE NEW WORK: there is NO existing field-resolved coupling in the A1↔ω pair.
ADD-2 (crystal_engine.py:222) is bulk↔shear-DISPLACEMENT (V↔w) — the WRONG pair;
recovering it does NOT count (pre-reg WRONG-SECTOR-PAIR guard). S2 BUILDS the
field-resolved A1↔Cosserat-ω skew generator and recovers the 2-mode ODE in limit.

α-CLEAN (pre-reg §α-clean discipline). The chord-deciding readout routes through
the α-clean host _winding_host.py (κ̃=6/5). NEVER ALPHA / KAPPA_CHIRAL_ELECTRON /
V_SNAP / L_NODE / M_E / Q_TANK on the chord path. The chirality PHASE uses the
α-free θ_χ=2π·ν_vac (ν_vac=2/7); the rate scale uses κ̃=6/5. Q=137 slot stays EMPTY.

CLASSIFICATION (consistency-vs-emergence): CONSISTENCY-class (pre-reg §Class). A
green S2 demonstrates a substrate-consistent conservative lock; it is NOT the
α-free chord (the chord-decider is S4). No emergence headline.
"""

from __future__ import annotations

import importlib.util as _ilu
from pathlib import Path as _Path

import numpy as np

# ── α-CLEAN HOST (the chord-deciding readout path; κ̃=6/5, NO α). Importing this
#    module executes its load-time guard triad — an α-leak fails HERE. ──────────
from tests.engine_acceptance import _winding_host as HOST

# ── VALIDATE-ON-KNOWN target to RECOVER (criterion 4): the PR#321 2-mode skew
#    generator. node_circulator_coupling.py lives in src/scripts/vol_9_device/
#    (no package __init__), so we load it BY FILE — importing the EXACT PR#321
#    functions (anti-rebuild, Rule 14), NOT a re-skin. The module's own α-free
#    guard (assert_alpha_free) is NOT run at module load (only in its main()), so
#    importing it cannot pull α onto our chord path; the S2 chord readout still
#    routes through HOST. We use ONLY circulator_generator/evolve/mode_energies. ─
def _load_node_circulator():
    p = (
        _Path(__file__).resolve().parents[2]
        / "scripts"
        / "vol_9_device"
        / "node_circulator_coupling.py"
    )
    spec = _ilu.spec_from_file_location("_ave_node_circulator_coupling", p)
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_NCC = _load_node_circulator()
ncc_circulator_generator = _NCC.circulator_generator  # the 2-mode skew generator
ncc_evolve = _NCC.evolve  # exact unitary trajectory a_k = U^k a0
ncc_mode_energies = _NCC.mode_energies  # |a_bulk|², |a_shear|²


# ═════════════════════════════════════════════════════════════════════════════
# 0.  α-FREE COUPLING INPUTS (named once; both α-free, both routed via the host).
# ═════════════════════════════════════════════════════════════════════════════
# The (2,3)-winding rate scale κ̃ = 6/5, certified α-free by the host (NOT α·κ̃).
KAPPA_TILDE: float = HOST.winding_kappa_tilde(2, 3)  # = 6/5
# The lattice chirality PHASE θ_χ = 2π·ν_vac, ν_vac = 2/7 (α-free — the SAME
# gyrotropic phase node_circulator_coupling.py:117 carries). Hard-coded as a
# rational here so NO constants-module import (and thus no α-carrier) is needed
# on the chord path; value-identical to 2π·NU_VAC.
NU_VAC: float = 2.0 / 7.0
THETA_CHI: float = 2.0 * np.pi * NU_VAC


# ═════════════════════════════════════════════════════════════════════════════
# 1.  THE SATURATION FRONT S(A)  (FORK A=(a): intra-mechanical coupling PORT).
# ═════════════════════════════════════════════════════════════════════════════
def saturation_kernel(A: np.ndarray, *, S_min: float = 2e-3, A_cap: float = 0.999) -> np.ndarray:
    """S(A) = √(1−A²), A = |V|/V_yield, clipped to [S_min, 1] — the A-034 kernel,
    IDENTICAL to crystal_engine.saturation_kernel:191-195 (the canonical reactive
    saturation). S(A→0)=1 (cold vacuum, full coupling), S(A→1)→S_min (frozen
    saturated core, coupling quenched). This is the reactive varactor knob the
    pre-reg's FORK A=(a) names as the coupling PORT (NO sink, NO transducer)."""
    Ac = np.minimum(np.abs(A), A_cap)
    return np.sqrt(np.maximum(1.0 - Ac**2, S_min**2))


def front_gate(A: np.ndarray, *, center: float = 4.0 / 7.0, width: float = 0.18) -> np.ndarray:
    """g_front(A): a thin shell at the Non-Linear→Saturated boundary (CP10) — the
    saturation-FRONT window where the A1↔ω mode-conversion ENGAGES (zero in cold
    vacuum A→0 AND in the deep frozen core A→1). center = R_II = 4/7 (α-free; the
    same shell cross_sector_coupling.saturation_front_window:45-52 uses). This is
    the S(A)-gating that makes the coupling a saturation-FRONT effect (FORK A=(a)),
    not a bulk-volume coupling."""
    return np.exp(-((A - center) ** 2) / (2.0 * width**2))


# ═════════════════════════════════════════════════════════════════════════════
# 2.  THE FIELD-RESOLVED SKEW-HERMITIAN GENERATOR  H_couple  (A1 ↔ ω).
#     This is the GENUINE NEW WORK — no existing field-resolved coupling in the
#     A1↔Cosserat-ω pair (ADD-2 is V↔w, the WRONG pair, NOT recovered here).
# ═════════════════════════════════════════════════════════════════════════════
def build_hcouple(
    A_profile: np.ndarray,
    *,
    omega_b: float = 1.0,
    omega_s: float = 1.3,
    rate: float = 0.3,
    chi: int = +1,
    hop_b: float = 0.0,
    hop_s: float = 0.0,
    gate: str = "front",
    S_min: float = 2e-3,
    A_cap: float = 0.999,
) -> np.ndarray:
    """Assemble the FIELD-RESOLVED Hermitian generator H_couple on an M-node chain.

    STATE LAYOUT (field-resolved): ψ ∈ C^{2M}, interleaved per node n=0..M-1:
        ψ[2n]   = a_A1(n)  — the A1 BULK-DILATATION breather analytic signal at
                             node n (q + i·p/ω; |a_A1|² = trapped bulk = MASS,
                             crystal_engine.py:354; the longitudinal "3").
        ψ[2n+1] = a_ω(n)   — the LOCAL Cosserat (ω, π_ω) LC-quadrature analytic
                             signal at node n (the poloidal winding / CHARGE "3",
                             crystal_graft_v4.py:46-47). PHASE-SPACE reactance pair,
                             NOT the orthogonal global rigid rotation L_ω.

    GENERATOR (Hermitian ⇒ e^{-iHt} unitary ⇒ ‖ψ‖² conserved EXACTLY):
      • diagonal:        H[2n,2n]   = ω_b   (A1 breather frequency at node n)
                         H[2n+1,2n+1] = ω_s (ω-tank LC frequency at node n)
      • A1↔ω ON-NODE off-diagonal (THE COUPLING — the genuine new term):
                         H[2n, 2n+1]   = Ω_n · e^{+i·χ·θ_χ}
                         H[2n+1, 2n]   = Ω_n · e^{-i·χ·θ_χ}   (= conj ⇒ Hermitian)
            Ω_n = rate · g_front(A_n) · S(A_n)   — the SATURATION-FRONT-GATED rate
            (FORK A=(a): the coupling is gated by the saturation front S(A); it
            ENGAGES on the front shell and quenches in cold vacuum + frozen core).
            The chirality PHASE χ·θ_χ is sourced by lattice handedness (a STRUCTURAL
            phase), NOT by reading ω off V (genesis-24 guard, master-equation.md:20).
      • intra-grade NEAREST-NEIGHBOUR hops (the field structure of each grade —
        each grade disperses on its OWN lattice, the field-resolved content):
                         H[2n, 2(n±1)]     = hop_b   (A1 disperses among nodes)
                         H[2n+1, 2(n±1)+1] = hop_s   (ω disperses among nodes)
        hop_b/hop_s default 0 ⇒ the on-node 2×2 blocks DECOUPLE across nodes ⇒
        each node is an independent node_circulator (the REDUCED-LIMIT bridge);
        hop≠0 turns on genuine field-resolved spatial transport within a grade.

    H is Hermitian BY CONSTRUCTION (off-diagonals are conjugate pairs, hops real),
    asserted below — this is the load-bearing anti-Hermitian-generator property
    (criterion 1 + skew-Hermitian assertion): there is NO indefinite trilinear
    potential, so NO detonation pump on the skew-Hermitian path (pre-reg T5).

    REDUCED LIMIT (criterion 4): M=1, hop=0 ⇒ H is the EXACT 2×2 node_circulator
    circulator_generator(ω_b, ω_s, Ω_0, χ) with Ω_0 = rate·gate(A_0). The
    reduced-limit recovery test asserts this BLOCK-EQUALITY against the PR#321
    generator (recover_reduced_limit)."""
    if chi not in (-1, 0, 1):
        raise ValueError("chi must be -1, 0, or +1 (lattice handedness selector)")
    A = np.asarray(A_profile, dtype=float).ravel()
    M = A.shape[0]
    dim = 2 * M
    H = np.zeros((dim, dim), dtype=complex)

    # S(A)-gating of the coupling rate (FORK A=(a)).
    S = saturation_kernel(A, S_min=S_min, A_cap=A_cap)
    if gate == "front":
        g = front_gate(A)
    elif gate == "saturation":
        g = S
    elif gate == "front_times_S":
        g = front_gate(A) * S
    elif gate == "off":
        g = np.zeros_like(A)  # coupling-OFF control arm
    else:
        raise ValueError(f"unknown gate '{gate}'")
    Omega = rate * g  # the saturation-front-gated, per-node coupling rate

    phase = chi * THETA_CHI
    off = np.exp(1j * phase)

    for n in range(M):
        ib, isr = 2 * n, 2 * n + 1
        H[ib, ib] = omega_b
        H[isr, isr] = omega_s
        # the A1↔ω ON-NODE coupling (the new field-resolved skew term).
        H[ib, isr] = Omega[n] * off
        H[isr, ib] = Omega[n] * np.conj(off)
    # intra-grade nearest-neighbour hops (open chain; field-resolved transport).
    for n in range(M - 1):
        ib0, ib1 = 2 * n, 2 * (n + 1)
        is0, is1 = 2 * n + 1, 2 * (n + 1) + 1
        H[ib0, ib1] = hop_b
        H[ib1, ib0] = hop_b
        H[is0, is1] = hop_s
        H[is1, is0] = hop_s

    # LOAD-BEARING: H must be Hermitian (⇒ unitary propagator ⇒ exact norm
    # conservation). This is the skew-Hermitian-by-construction property.
    assert np.allclose(H, H.conj().T), "H_couple generator is not Hermitian"
    return H


def is_skew_hermitian_generator(H: np.ndarray) -> bool:
    """The coupling is realized as a SKEW generator: the EVOLUTION operator −iH is
    anti-Hermitian ((−iH)† = +iH† = +iH·(−1)·(−1) = −(−iH) since H=H†). Equivalently
    H is Hermitian. Return True iff −iH is anti-Hermitian to machine precision."""
    G = -1j * H
    return bool(np.allclose(G.conj().T, -G, atol=1e-12))


def propagator(H: np.ndarray, dt: float) -> np.ndarray:
    """U = e^{-iHdt}. For a HERMITIAN H (the REAL arm) use the exact Hermitian
    eigendecomposition (no Trotter error; U unitary to machine precision; mirrors
    node_circulator_coupling._propagator:160-165). For a NON-Hermitian H (the
    NEGATIVE-CONTROL arms ONLY — the lossy / directional-gain detonator) fall back
    to the general matrix exponential so the non-unitary (pump/leak) dynamics are
    represented FAITHFULLY (a Hermitian-only eigensolver would silently symmetrize
    the generator and HIDE the very non-conservation the canary must detect)."""
    if np.allclose(H, H.conj().T, atol=1e-12):
        evals, evecs = np.linalg.eigh(H)
        return evecs @ np.diag(np.exp(-1j * evals * dt)) @ evecs.conj().T
    from scipy.linalg import expm
    return expm(-1j * H * dt)


def evolve_field(psi0: np.ndarray, H: np.ndarray, dt: float, n_steps: int) -> np.ndarray:
    """Unitary trajectory ψ_k = U^k ψ0, U = e^{-iHdt}. Returns (n_steps+1, 2M)."""
    U = propagator(H, dt)
    psi = np.asarray(psi0, dtype=complex).copy()
    traj = np.empty((n_steps + 1, psi.shape[0]), dtype=complex)
    traj[0] = psi
    for k in range(1, n_steps + 1):
        psi = U @ psi
        traj[k] = psi
    return traj


def split_modes(traj: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Split a (T, 2M) field trajectory into A1 amplitudes (even idx) and ω
    amplitudes (odd idx), each (T, M)."""
    return traj[:, 0::2], traj[:, 1::2]


def joint_energy(traj: np.ndarray) -> np.ndarray:
    """The joint H = Σ_n (|a_A1(n)|² + |a_ω(n)|²) along the trajectory (the norm
    ‖ψ‖²; |a|² = mode energy/ω, so this IS E_A1 + E_ω + the exchanged H_couple in
    the rotating frame). Conserved EXACTLY under the unitary map."""
    return np.sum(np.abs(traj) ** 2, axis=1)


def L_omega_pump(traj: np.ndarray, A_profile: np.ndarray) -> np.ndarray:
    """|L_ω|(t) — the field-resolved analogue of crystal_graft_v2.spin_L_omega:300:
    the spatial first-moment of the ω-mode energy about the chain centre,
        |L_ω|(t) = | Σ_n (n − n_c) · |a_ω(n,t)|² | .
    A bounded reactive exchange keeps this O(1); a PUMP (the v3 t^0.43 runaway) makes
    it grow secularly. This is the |L_ω| pump CANARY (criterion 2 + the lock-OFF /
    photon_deplete neg-control). On a unitary (skew-Hermitian) generator it is bounded
    by construction; the negative control must make it FIRE on a DIFFERENT generator."""
    _, aw = split_modes(traj)
    M = aw.shape[1]
    nc = (M - 1) / 2.0
    coord = np.arange(M) - nc
    e_w = np.abs(aw) ** 2  # (T, M)
    return np.abs(e_w @ coord)


# ═════════════════════════════════════════════════════════════════════════════
# 3.  THE FOUR MAKE-OR-BREAK CRITERIA (pre-reg §Make-or-break).
# ═════════════════════════════════════════════════════════════════════════════
# Pre-stated tolerances (FROZEN before the run — do NOT tune to force a verdict).
CONS_TOL = 1e-8            # criterion 1: |dH/H| < 1e-8 (test_l1_photon.py:285)
TRANSFER_MIN = 0.05        # criterion 2: ω fill ≫ the failed 2% inert arm
# criterion 2: the |L_ω| pump is BOUNDED ⇔ NO SECULAR GROWTH. The pre-reg names
# "|L_ω| pump BOUNDED" — the substrate-native distinction is bounded-reactive
# (oscillates, late≈early) vs a PUMP (secular runaway, the v3 t^0.43 / S1's 9.5×).
# We bin on the late/early quartile-mean ratio (a runaway pump has ratio≫1), NOT an
# absolute magnitude (the natural oscillation amplitude scales with M+loaded energy,
# so an absolute cap would be arbitrary). Plus a sanity ceiling at the physical
# energy-available bound N0·(M−1)/2 (the moment can never exceed it).
L_OMEGA_SECULAR_RATIO = 1.5  # late-quartile/early-quartile |L_ω| mean ratio bound
NEG_CTRL_PUMP_RATIO = 3.0  # neg-control: lock-OFF/detonating |L_ω| must FIRE ≥3×
NEG_CTRL_DH_FLOOR = 1e-6   # neg-control: open/lossy arm |dH/H| must FIRE ≫ tol


def criterion_1_conservation(
    M: int = 8,
    omega_b: float = 1.0,
    omega_s: float = 1.3,
    rate: float = 0.3,
    chi: int = +1,
    hop_b: float = 0.05,
    hop_s: float = 0.07,
    dt: float = 0.05,
    n_steps: int = 40000,
    seed: int = 7,
) -> dict:
    """CRITERION 1 — CONSERVATION (pre-reg §Make-or-break 1). The joint
    H = E_A1 + E_ω + H_couple drifts |dH/H| < 1e-8 over a long CLOSED-system
    window. The system is closed (NO loss port — T2 guard: conservation must NOT
    be bought by spurious damping). Generic loaded state, long run, report max
    drift + late-time pump slope."""
    A = np.linspace(0.1, 0.9, M)
    rng = np.random.default_rng(seed)
    psi0 = rng.standard_normal(2 * M) + 1j * rng.standard_normal(2 * M)
    H = build_hcouple(A, omega_b=omega_b, omega_s=omega_s, rate=rate, chi=chi,
                      hop_b=hop_b, hop_s=hop_s, gate="front")
    traj = evolve_field(psi0, H, dt, n_steps)
    N = joint_energy(traj)
    drift = float(np.max(np.abs(N - N[0])) / N[0])
    tail = N[int(0.75 * len(N)):]
    slope = float(np.polyfit(np.arange(len(tail), dtype=float), tail, 1)[0])
    passed = (drift < CONS_TOL) and (abs(slope) < 1e-12)
    return {
        "dH_over_H_max": drift, "late_pump_slope_per_step": slope,
        "n_steps": n_steps, "closed_system": True,
        "skew_hermitian": is_skew_hermitian_generator(H),
        "PASS": bool(passed),
    }


def criterion_2_non_vacuity(
    M: int = 8,
    omega_b: float = 1.0,
    omega_s: float = 1.0,  # resonant ⇒ full sloshing (strongest measured flow)
    rate: float = 0.3,
    chi: int = +1,
    hop_b: float = 0.05,
    hop_s: float = 0.07,
    dt: float = 0.05,
    n_steps: int = 40000,
) -> dict:
    """CRITERION 2 — NON-VACUITY (pre-reg §Make-or-break 2, LOAD-BEARING). The
    coupling TRANSFERS: load the A1 (bulk) modes ONLY, ω EMPTY; ω fills measurably
    (the ~2% inert arm of cross_sector_coupling FAILS this), AND the |L_ω| pump
    canary stays BOUNDED. ω(0)=0 so any |a_ω|²>0 is energy that physically arrived
    from A1 through the off-diagonal (a MEASURED flow, not a closure identity)."""
    A = np.linspace(0.1, 0.9, M)
    psi0 = np.zeros(2 * M, dtype=complex)
    psi0[0::2] = 1.0  # all A1 loaded, ω EMPTY
    H = build_hcouple(A, omega_b=omega_b, omega_s=omega_s, rate=rate, chi=chi,
                      hop_b=hop_b, hop_s=hop_s, gate="front")
    traj = evolve_field(psi0, H, dt, n_steps)
    aA1, aw = split_modes(traj)
    N0 = float(joint_energy(traj)[0])
    omega_initial = float(np.sum(np.abs(aw[0]) ** 2))
    omega_max = float(np.max(np.sum(np.abs(aw) ** 2, axis=1)))
    transfer_frac = omega_max / N0
    # ω genuinely OSCILLATES (Rabi flop) — non-vacuity witness (not a static offset)
    e_w = np.sum(np.abs(aw) ** 2, axis=1)
    centered = e_w - e_w.mean()
    sgn = np.sign(centered)
    crossings = int(np.sum((sgn[:-1] < 0) & (sgn[1:] >= 0)))
    # |L_ω| pump canary: BOUNDED ⇔ NO SECULAR GROWTH (bounded-reactive, not a pump).
    Lom = L_omega_pump(traj, A)
    q = len(Lom) // 4
    early = float(Lom[:q].mean()) + 1e-12
    late = float(Lom[3 * q:].mean())
    secular_ratio = late / early
    ceiling = N0 * (M - 1) / 2.0  # physical energy-available bound on the moment
    L_max = float(np.max(Lom))
    L_bounded = bool(secular_ratio < L_OMEGA_SECULAR_RATIO and L_max <= ceiling)
    passed = (omega_initial < 1e-15) and (transfer_frac > TRANSFER_MIN) \
        and (crossings >= 1) and L_bounded
    return {
        "omega_initial_energy": omega_initial,
        "transfer_fraction": transfer_frac,
        "vs_failed_2pct": f"{transfer_frac / 0.02:.0f}x the failed 2%",
        "omega_oscillation_crossings": crossings,
        "L_omega_max": L_max, "L_omega_secular_ratio": secular_ratio,
        "L_omega_physical_ceiling": ceiling, "L_omega_bounded": L_bounded,
        "transfer_measured": bool(omega_initial < 1e-15 and transfer_frac > TRANSFER_MIN),
        "PASS": bool(passed),
    }


def criterion_3_independence(N: int = 48, R: float = 11.0, r: float = 4.0) -> dict:
    """CRITERION 3 — INDEPENDENCE (pre-reg §Make-or-break 3, FORK B=(b)). ω keeps
    its OWN conserved winding integer robust under a V-perturbation on the REAL
    arm, while the SLAVED arm (ω:=F(V)) returns independence=False (reachable-False
    / AUTO_VOID). NORMAL-MODE SPLITTING IS DECLARED EXPECTED + bounded — NOT a
    violation (the eigenfrequency-pull below is the S(A) modulation working, the
    same modulation that with a spatial gradient IS gravity).

    ANTI-REBUILD (Rule 14): the independence discriminator is the EXISTING S1
    reachable-False slaved-arm gate (s1_winding_conservation_gate.gate_f_positive_
    control:396-441) run on the REAL engine (CrystalGraftV4, V↔ω coupled). The S1
    gate already encodes the precise discriminator the pre-reg cites (:439). We do
    NOT re-implement it — we INVOKE it (this is the operationalization the pre-reg
    §FORK B names: 'Independence is operationalized by the S1 reachable-False
    slaved-arm discriminator').

    SPLITTING witness: the field-resolved H_couple's normal-mode eigenfrequencies
    SPLIT by ≈2Ω at resonance (node_circulator_coupling.py:124-157) — we report the
    split magnitude as EXPECTED+bounded, explicitly NOT scoring it as a violation."""
    from ave.core import s1_winding_conservation_gate as S1

    f = S1.gate_f_positive_control(N, R, r)

    # SPLITTING witness on the field-resolved H_couple: at resonance (ω_b=ω_s) the
    # on-node 2×2 block eigenvalues are ω ± Ω ⇒ split = 2Ω (EXPECTED, bounded).
    A = np.array([4.0 / 7.0])  # front-center single node ⇒ Ω = rate
    rate = 0.3
    H_split = build_hcouple(A, omega_b=1.0, omega_s=1.0, rate=rate, chi=+1, gate="front")
    eig = np.linalg.eigvalsh(H_split)
    split = float(np.max(eig) - np.min(eig))
    split_expected = bool(np.isclose(split, 2.0 * rate, rtol=1e-6))

    return {
        "real_arm_independent": bool(f["real_arm_independent"]),
        "slaved_arm_independence_false": bool(f["slaved_arm_independence_false"]),
        "AUTO_VOID": bool(f["AUTO_VOID"]),
        "real_winding": f["real"]["w_ref"], "real_winding_pert": f["real"]["w_pert"],
        "slaved_winding_ref": f["slaved"]["w_ref"], "slaved_winding_pert": f["slaved"]["w_pert"],
        "normal_mode_split": split, "split_equals_2Omega_EXPECTED": split_expected,
        "splitting_is_violation": False,  # FORK B=(b): splitting EXPECTED, NOT a violation
        # PASS ⇔ real arm independent AND slaved arm reachable-False (NOT AUTO_VOID)
        "PASS": bool(f["real_arm_independent"] and f["slaved_arm_independence_false"]
                     and not f["AUTO_VOID"]),
    }


def criterion_4_reduced_limit(
    omega_b: float = 1.0, omega_s: float = 1.3, rate: float = 0.3, chi: int = +1,
    dt: float = 0.05, n_steps: int = 5000,
) -> dict:
    """CRITERION 4 — REDUCED-LIMIT (pre-reg §Make-or-break 4). The field-resolved
    H_couple recovers the 2-mode node_circulator circulator_generator
    (node_circulator_coupling.py:124-157) in its 2-mode (M=1, hop=0) limit.

    Recovery is asserted at THREE levels:
      (i)   GENERATOR EQUALITY — build_hcouple(M=1, front-center A ⇒ g=1) == the
            EXACT node_circulator circulator_generator(ω_b, ω_s, rate, χ) (to
            machine precision). [This is the load-bearing structural recovery.]
      (ii)  TRAJECTORY EQUALITY — evolving the field generator on a 2-vector state
            == node_circulator's own evolve() on the same state (same dynamics).
      (iii) RABI ANCHOR — the reduced-limit transfer fraction matches the analytic
            Rabi formula Ω²/(Ω²+Δ²/4) (the integrator-independent anchor the PR#321
            gates rest on, node_circulator validate_on_known:664-689).
    NOTE: recovering ADD-2 (V↔w) would NOT count — this recovers the A1↔ω 2-mode
    generator (pre-reg WRONG-SECTOR-PAIR + ANTI-SUBSTITUTION guards)."""
    A0 = np.array([4.0 / 7.0])  # front center ⇒ g_front=1 ⇒ Ω = rate exactly
    g0 = float(front_gate(A0)[0])
    Omega0 = rate * g0

    H_field = build_hcouple(A0, omega_b=omega_b, omega_s=omega_s, rate=rate, chi=chi,
                            hop_b=0.0, hop_s=0.0, gate="front")
    H_ncc = ncc_circulator_generator(omega_b, omega_s, Omega0, chi)
    generator_equal = bool(np.allclose(H_field, H_ncc, atol=1e-13))

    # trajectory equality on an identical 2-vector state
    a0 = np.array([1.0 + 0j, 0.0 + 0j])  # bulk loaded, shear empty
    traj_field = evolve_field(a0, H_field, dt, n_steps)
    traj_ncc = ncc_evolve(a0, H_ncc, dt, n_steps)
    traj_equal = bool(np.allclose(traj_field, traj_ncc, atol=1e-10))

    # Rabi anchor at resonance (Δ=0) — full transfer; and detuned throttle
    A0r = np.array([4.0 / 7.0])
    H_res = build_hcouple(A0r, omega_b=1.0, omega_s=1.0, rate=rate, chi=chi, gate="front")
    tr = evolve_field(np.array([1.0 + 0j, 0.0 + 0j]), H_res, dt, n_steps)
    _, aw = split_modes(tr)
    transfer = float(np.max(np.abs(aw[:, 0]) ** 2))
    f_rabi = Omega0**2 / (Omega0**2 + 0.0)  # Δ=0 ⇒ 1.0
    rabi_match = bool(np.isclose(transfer, f_rabi, rtol=1e-3, atol=1e-3))

    return {
        "reduced_Omega": Omega0, "g_front_at_center": g0,
        "generator_equals_node_circulator": generator_equal,
        "trajectory_equals_node_circulator": traj_equal,
        "rabi_anchor_match": rabi_match, "reduced_transfer": transfer,
        "PASS": bool(generator_equal and traj_equal and rabi_match),
    }


# ═════════════════════════════════════════════════════════════════════════════
# 4.  DUAL-CANARY LIVE NEGATIVE CONTROLS  (each leg demonstrates reachable-FAIL).
#     T6 guard: a canary no arm can trip is VACUOUS. NEVER photon_deplete=True on
#     the REAL arm (T5 detonation, cross_sector_coupling.py:130-141).
# ═════════════════════════════════════════════════════════════════════════════
def _detonating_generator(A_profile: np.ndarray, *, rate: float = 0.3,
                          gain: float = 0.02) -> np.ndarray:
    """A deliberately NON-skew, NON-Hermitian generator with an ANTI-CONSERVATIVE
    (indefinite / gain) off-diagonal — the field-resolved analogue of the indefinite
    trilinear H (photon_deplete=True) that DETONATES (H_bel −4107,
    cross_sector_coupling.py:130-141). Used ONLY by the |L_ω| negative control to
    prove the pump canary CAN fire. The ω-block carries a REAL secular-pump term
    (a positive-feedback hop that funnels energy to one end of the chain ⇒ the
    spatial first-moment |L_ω| grows secularly). This generator is NEVER on the
    real arm — it exists only to demonstrate the canary is not decorative."""
    A = np.asarray(A_profile, dtype=float).ravel()
    M = A.shape[0]
    H = build_hcouple(A, rate=rate, hop_b=0.05, hop_s=0.07, gate="front")
    # break Hermiticity with a directional gain on the ω chain: a one-way amplifying
    # hop a_ω(n+1) += i·gain·a_ω(n) (NOT its conjugate) ⇒ −iH no longer anti-Herm
    # ⇒ the propagator is NON-unitary and PUMPS the ω spatial moment one-way.
    for n in range(M - 1):
        H[2 * (n + 1) + 1, 2 * n + 1] += 1j * gain  # asymmetric ⇒ non-Hermitian
    return H


def negative_control_L_omega_pump(
    M: int = 8, rate: float = 0.3, dt: float = 0.05, n_steps: int = 4000,
) -> dict:
    """LIVE NEGATIVE CONTROL (i) — the |L_ω| PUMP must FIRE (pre-reg dual-canary).
    The real skew-Hermitian arm keeps |L_ω| BOUNDED (no secular growth). A pre-stated
    DETONATING arm (non-Hermitian directional-gain generator, the field analogue of
    photon_deplete=True) MUST pump |L_ω| by ≥ NEG_CTRL_PUMP_RATIO×. A canary no arm
    can trip is vacuous (T6). Reports the real-arm bound AND the neg-arm firing."""
    A = np.linspace(0.1, 0.9, M)
    psi0 = np.zeros(2 * M, dtype=complex)
    psi0[0::2] = 1.0

    # REAL arm (skew-Hermitian, unitary) — |L_ω| bounded.
    H_real = build_hcouple(A, rate=rate, hop_b=0.05, hop_s=0.07, gate="front")
    traj_real = evolve_field(psi0, H_real, dt, n_steps)
    L_real = L_omega_pump(traj_real, A)
    real_max = float(np.max(L_real))

    # DETONATING arm (non-Hermitian gain) — |L_ω| pumps. (analogue of photon_deplete)
    H_det = _detonating_generator(A, rate=rate)
    traj_det = evolve_field(psi0, H_det, dt, n_steps)
    L_det = L_omega_pump(traj_det, A)
    det_max = float(np.max(L_det))

    pump_ratio = det_max / (real_max + 1e-12)
    fired = bool(pump_ratio >= NEG_CTRL_PUMP_RATIO)
    return {
        "L_omega_real_max": real_max, "L_omega_detonating_max": det_max,
        "pump_ratio": pump_ratio, "is_skew_real_arm": is_skew_hermitian_generator(H_real),
        "is_skew_detonating_arm": is_skew_hermitian_generator(H_det),
        "dh_negative_control_fired": fired,  # named per deliverable
        "L_omega_negative_control_fired": fired,
        "PASS": fired,
    }


def negative_control_conservation(
    M: int = 8, rate: float = 0.3, loss: float = 0.02, dt: float = 0.05,
    n_steps: int = 4000,
) -> dict:
    """LIVE NEGATIVE CONTROL (ii) — the |dH/H| conservation canary must FIRE on an
    OPEN/LOSSY arm (pre-reg dual-canary). The real CLOSED arm conserves |dH/H|<1e-8;
    a pre-stated OPEN arm (an anti-Hermitian diagonal loss term — energy leaks)
    MUST blow |dH/H| ≫ tol. This proves the conservation canary is not decorative
    AND guards T2 (a leak hidden by 'conservation' would be a FAIL): if the canary
    could not detect a leak, a damping-bought conservation would pass silently."""
    A = np.linspace(0.1, 0.9, M)
    rng = np.random.default_rng(11)
    psi0 = rng.standard_normal(2 * M) + 1j * rng.standard_normal(2 * M)

    # REAL closed arm.
    H_real = build_hcouple(A, rate=rate, hop_b=0.05, hop_s=0.07, gate="front")
    N_real = joint_energy(evolve_field(psi0, H_real, dt, n_steps))
    real_drift = float(np.max(np.abs(N_real - N_real[0])) / N_real[0])

    # OPEN/LOSSY arm: add an anti-Hermitian diagonal (−i·loss on the ω modes) ⇒ a
    # decaying (non-unitary) propagator ⇒ |dH/H| grows (the norm is NOT conserved).
    H_open = H_real.astype(complex).copy()
    for n in range(M):
        H_open[2 * n + 1, 2 * n + 1] += -1j * loss  # anti-Hermitian ⇒ loss port
    N_open = joint_energy(evolve_field(psi0, H_open, dt, n_steps))
    open_drift = float(np.max(np.abs(N_open - N_open[0])) / N_open[0])

    fired = bool(open_drift > NEG_CTRL_DH_FLOOR and real_drift < CONS_TOL)
    return {
        "dH_over_H_real_closed": real_drift, "dH_over_H_open_lossy": open_drift,
        "real_is_hermitian": bool(np.allclose(H_real, H_real.conj().T)),
        "open_is_hermitian": bool(np.allclose(H_open, H_open.conj().T)),
        "dh_negative_control_fired": fired,  # named per deliverable
        "PASS": fired,
    }


# ═════════════════════════════════════════════════════════════════════════════
# 5.  α-CLEAN CONFIRMATION  (the chord-deciding readout carries NO α-carrier).
# ═════════════════════════════════════════════════════════════════════════════
def assert_alpha_clean() -> dict:
    """Confirm the S2 chord path is α-clean (pre-reg §α-clean discipline): the host
    guard triad live, κ̃=6/5 (NOT α·κ̃), κ̃ ∉ the 117–157 α⁻¹ landing band, and NO
    forbidden α-carrier is a bound name in THIS module's globals. NEVER ALPHA /
    KAPPA_CHIRAL_ELECTRON / V_SNAP / L_NODE / M_E / Q_TANK."""
    HOST.assert_winding_host_globals_alpha_clean()
    HOST.assert_no_alpha_literal_in_chord_path()
    HOST.assert_not_in_landing_zone(KAPPA_TILDE, "S2 winding κ̃")
    forbidden = ("ALPHA", "ALPHA_COLD_INV", "KAPPA_CHIRAL_ELECTRON", "V_SNAP",
                 "L_NODE", "M_E", "Q_TANK", "ELECTRON", "RHO_BULK")
    g = globals()
    leaked = [s for s in forbidden if s in g]
    assert not leaked, f"α-leak: forbidden symbol(s) {leaked} bound in the S2 gate globals"
    return {
        "kappa_tilde": KAPPA_TILDE, "kappa_is_six_fifths": bool(KAPPA_TILDE == 6.0 / 5.0),
        "theta_chi_is_2pi_nu_vac": bool(np.isclose(THETA_CHI, 2.0 * np.pi * (2.0 / 7.0))),
        "no_forbidden_in_globals": not leaked, "alpha_clean": True,
    }


# ═════════════════════════════════════════════════════════════════════════════
# 6.  THE GATE RUNNER  (bins the verdict per the FROZEN pre-reg).
# ═════════════════════════════════════════════════════════════════════════════
def run_s2_gate(N: int = 48, R: float = 11.0, r: float = 4.0,
                cons_steps: int = 40000, fast: bool = False) -> dict:
    """Run the full S2 H_couple gate and bin the verdict per the FROZEN pre-reg
    (research/2026-06-24_engine-s2-hcouple_prereg.md §Make-or-break).

    S2 PASSES iff ALL FOUR criteria hold AND the dual canary fires reachable-FAIL
    on BOTH negative controls AND the readout is α-clean. Any failing criterion ⇒
    FAIL. INCONCLUSIVE (Rule 11, NOT rescued) iff the integrator cannot carry the
    dynamics to a clean verdict (NaN/non-finite drift, or the reduced-limit recovery
    cannot be formed). The negative-control firing is a PREREQUISITE for a
    non-vacuous PASS; the slaved-arm reachable-False is a PREREQUISITE (AUTO_VOID
    otherwise). Normal-mode SPLITTING is EXPECTED (FORK B=(b)), NOT scored as a FAIL.

    fast=True shortens the conservation window (structural smoke), used by the
    fast pytest path; the full closed-system window is the headline."""
    steps = 4000 if fast else cons_steps
    out: dict = {"config": {"N": N, "R": R, "r": r, "cons_steps": steps,
                            "kappa_tilde": KAPPA_TILDE, "theta_chi": THETA_CHI}}

    out["alpha_clean"] = assert_alpha_clean()
    out["validate_on_known_node_circulator"] = _validate_node_circulator()

    out["criterion_1_conservation"] = criterion_1_conservation(n_steps=steps)
    out["criterion_2_non_vacuity"] = criterion_2_non_vacuity(n_steps=steps)
    out["criterion_4_reduced_limit"] = criterion_4_reduced_limit()
    out["criterion_3_independence"] = criterion_3_independence(N, R, r)

    out["negative_control_L_omega_pump"] = negative_control_L_omega_pump()
    out["negative_control_conservation"] = negative_control_conservation()

    c1 = out["criterion_1_conservation"]
    c2 = out["criterion_2_non_vacuity"]
    c3 = out["criterion_3_independence"]
    c4 = out["criterion_4_reduced_limit"]
    ncL = out["negative_control_L_omega_pump"]
    ncH = out["negative_control_conservation"]

    out["immune_system"] = {
        "slaved_arm_independence_false": bool(c3["slaved_arm_independence_false"]),
        "dh_negative_control_fired": bool(ncH["dh_negative_control_fired"]),
        "l_omega_negative_control_fired": bool(ncL["L_omega_negative_control_fired"]),
        "transfer_measured": bool(c2["transfer_measured"]),
        "real_dynamics_ran": bool(c3["real_winding"] is not None),
    }
    out["skew_hermitian"] = bool(c1["skew_hermitian"])
    out["reduced_limit_recovers_2mode"] = bool(c4["generator_equals_node_circulator"]
                                               and c4["trajectory_equals_node_circulator"])
    out["alpha_clean_flag"] = bool(out["alpha_clean"]["alpha_clean"])

    # INCONCLUSIVE detection (Rule 11 — report, do NOT rescue).
    inconclusive = (not np.isfinite(c1["dH_over_H_max"])) \
        or (not np.isfinite(c2["transfer_fraction"])) \
        or c3.get("AUTO_VOID", False) is None
    out["inconclusive_reason"] = (
        "non-finite conservation/transfer — integrator could not carry the dynamics"
        if inconclusive else None
    )

    crit = {
        "1_conservation": c1["PASS"], "2_non_vacuity": c2["PASS"],
        "3_independence": c3["PASS"], "4_reduced_limit": c4["PASS"],
        "neg_ctrl_L_omega_fires": ncL["PASS"], "neg_ctrl_conservation_fires": ncH["PASS"],
        "alpha_clean": out["alpha_clean_flag"], "skew_hermitian": out["skew_hermitian"],
    }
    out["criterion_pass_flags"] = crit
    out["failing_criteria"] = [k for k, v in crit.items() if not v]

    if inconclusive:
        out["verdict"] = "INCONCLUSIVE"
    elif c3.get("AUTO_VOID", False):
        out["verdict"] = "AUTO_VOID"
    elif all(crit.values()):
        out["verdict"] = "PASS"
    else:
        out["verdict"] = "FAIL"
    return out


def _validate_node_circulator() -> dict:
    """VALIDATE-ON-KNOWN floor: re-confirm the PR#321 node_circulator generator
    the reduced limit recovers is itself sound (Hermitian, unitary, norm-conserving)
    — the recover-in-limit anchor (pre-reg §Validate-on-known). Reads ONLY the
    generator's structural properties (α-free)."""
    H = ncc_circulator_generator(1.0, 1.3, 0.3, +1)
    U = propagator(H, 0.1)
    hermitian = bool(np.allclose(H, H.conj().T))
    unitary = bool(np.allclose(U @ U.conj().T, np.eye(2), atol=1e-12))
    a0 = np.array([0.6 + 0.3j, -0.2 + 0.5j])
    traj = ncc_evolve(a0, H, 0.05, 5000)
    nb, ns = ncc_mode_energies(traj)
    Nn = nb + ns
    norm_ok = bool(np.max(np.abs(Nn - Nn[0])) < 1e-9)
    return {"node_circulator_hermitian": hermitian, "node_circulator_unitary": unitary,
            "node_circulator_norm_conserved": norm_ok,
            "PASS": bool(hermitian and unitary and norm_ok)}


def main() -> None:
    import json
    import sys

    print("S2 H_COUPLE GATE — field-resolved skew-Hermitian A1↔ω lock")
    print("=" * 70)
    out = run_s2_gate()
    print(json.dumps(out, indent=2, default=str))
    print("=" * 70)
    print(f"VERDICT: {out['verdict']}")
    if out["failing_criteria"]:
        print(f"FAILING: {out['failing_criteria']}")
    sys.exit(0 if out["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
