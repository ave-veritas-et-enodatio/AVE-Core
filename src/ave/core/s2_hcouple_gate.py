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
    """Exact unitary U = e^{-iHdt} via Hermitian eigendecomposition (no Trotter
    error; H Hermitian ⇒ U unitary to machine precision). Mirrors
    node_circulator_coupling._propagator:160-165 (generalized to 2M dims)."""
    evals, evecs = np.linalg.eigh(H)
    return evecs @ np.diag(np.exp(-1j * evals * dt)) @ evecs.conj().T


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
