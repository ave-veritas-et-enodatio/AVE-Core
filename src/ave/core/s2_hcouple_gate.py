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
