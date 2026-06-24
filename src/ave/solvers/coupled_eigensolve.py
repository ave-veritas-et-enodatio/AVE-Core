"""COUPLED A1+winding EIGENSOLVE — does a confined electron eigenmode (mass+charge)
exist, and where does it sit in the V_yield/V_snap/m_e ladder.

FROZEN PRE-REG: research/2026-06-24_engine-coupled-eigensolve_prereg.md (commit 54d605f8).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (the conservative-existence keystone S3 left untested)
═══════════════════════════════════════════════════════════════════════════════
This is a CONSERVATIVE EIGENVALUE / EXISTENCE problem. We eigensolve the SAME
Hermitian generator H that S3 (coupled_cage_winding._assemble_H) time-evolved and
ask whether a CONFINED STATIONARY BOUND MODE carrying BOTH the A1 mass-amplitude
AND the (2,3) Cosserat winding-charge EXISTS in its spectrum. We report EIGENPAIRS,
NOT trajectories — this does NOT refill the twice-falsified self-formation slot
(A47 v11b; pre-reg §0/§4). Re-posing time-domain self-trap is BARRED.

  fork-b eigensolved the A1-ALONE confined mode (a graph Laplacian on the native
  connect-map). This module EXTENDS that eigensolve to the COUPLED OBJECT: the
  A1 mass-block + the b_ω winding-amplitude block + the S(A)-front-gated on-site
  coupling, the FULL Hermitian H. The genuinely new work is (i) eigensolving the
  COUPLED H, (ii) the BOTH-SECTORS-PRESENT gate (d) on the eigenstate (the
  genesis-24 guard — winding must NOT have bled into the A1 scalar), and (iii)
  the §3 V_yield/V_snap/m_e ladder readout (A*, ω_bound).

═══════════════════════════════════════════════════════════════════════════════
THE OPERATOR + THE BOUND-MODE CONVENTION (load-bearing sign flip vs fork-b)
═══════════════════════════════════════════════════════════════════════════════
H (rigid_template) on the periodic native N³ lattice, state x = [a_A1, b_ω]:
    H_A1 block : ω_b·I − c_A1²·L_D            (L_D = adjoint_div(D ∇), D=1/S(A))
    b_ω block  : ω_s·I − c_ω²·L_D             (b_ω = LC amplitude on the fixed
                                               winding template ê_w; the (2,3)
                                               winding integer lives in ê_w)
    coupling   : a_A1 ← Ω·e^{+iχθ_χ}·b_ω, b_ω ← Ω·e^{−iχθ_χ}·a_A1  (Hermitian)

L_D is the Stage-2 NATIVE K4 stiffness (NOT Cartesian 7-pt; HR1). H is Hermitian
⇒ real eigenvalues ⇒ Im(ω)=0 EXACTLY (the lossless reactive cage; gate c is
structural-by-construction for the closed operator).

SIGN-FLIP vs fork-b (RF-2 corollary): fork-b solves L_D ψ = ω² ψ and the bound
stiff-core breather is the HIGHEST ω² (gap ABOVE the band, D=1/S→∞ stiff core).
HERE the A1 block is ω_b·I − c²·L_D — the MINUS flips it: the SAME stiff-core
breather is the LOWEST-algebraic (most-bound) eigenvalue of H. So we eigensolve
the SMALLEST-algebraic ("SA") end of H, and the fork-b ω² = (ω_b − w_H)/c² maps
the H-eigenvalue back to the fork-b breathing frequency for the HALT-gate
comparison.

═══════════════════════════════════════════════════════════════════════════════
α-CLEAN (operating principle, pre-reg §0)
═══════════════════════════════════════════════════════════════════════════════
The chord-deciding reads route through the _winding_host κ̃=6/5 guard. NO ALPHA /
Q_TANK / KAPPA_CHIRAL_ELECTRON / V_SNAP on the verdict path (the operator reads a
dimensionless A=|a_A1|/V_yield; the α-carrying V_yield CANCELS). V_snap/V_yield
enter ONLY as the declared §3 operating-point CALIBRATION, never on a verdict read.
The import-guard triad below fails the import if an α-carrier leaks in.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# REUSE (anti-rebuild, Rule 14): the S3 coupled Hermitian generator + its config.
from ave.solvers.coupled_cage_winding import (
    CoupledCageWinding,
    CoupledCageWindingConfig,
)

# REUSE (anti-rebuild, Rule 14): fork-b's cluster-aware gap machinery (the bound
# LEVEL vs band-top witness; degeneracy-safe — the core breather is multiply
# degenerate by symmetry).
from ave.solvers.fork_b_saturation_tank import _cluster_spectrum

# REUSE: the (2,3) winding integer reader (the SAME coordinate S1/charge-quant use).
from ave.topological.charge_quantization import compute_Q_link

# ── the α-FREE chord-path winding factor (routed via the host guard) ──
from tests.engine_acceptance._winding_host import (
    assert_winding_host_globals_alpha_clean,
    winding_kappa_tilde,
)

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time). An α-carrier leaking here fails the import.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "α-leak: ELECTRON instance must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) forbidden"

KAPPA_TILDE: float = winding_kappa_tilde(2, 3)  # = 6/5, α-free (chord-path witness)


@dataclass(frozen=True)
class CoupledEigenConfig:
    """Frozen coupled-eigensolve config. The geometry defaults are the CANONICAL
    (2,3) winding scale (R=7, r=2.3, N=32 — the charge_quantization gate scale at
    which the seeded winding reads (2,3) correctly: validate-on-known PASS) with a
    WIDE A1 core (a1_radius=6.0) so the saturation FRONT reaches the winding torus
    radius R (the only regime where the coupling can hybridize A1↔winding)."""

    N: int = 32
    pml_thickness: int = 4
    V_yield: float = 1.0
    a1_amplitude: float = 0.999      # near A_cap ⇒ deep stiff core (S→S_min, D=1/S huge)
    a1_radius: float = 6.0           # WIDE ⇒ front shell reaches the winding torus R
    R: float = 7.0                   # winding torus major radius (canonical (2,3) scale)
    r: float = 2.3                   # winding tube minor radius
    rate: float = 0.3                # S2 coupling rate scale
    omega_b: float = 1.0             # A1 breather frequency
    omega_s: float = 1.0             # ω-tank LC frequency (resonant ⇒ strongest exchange)
    chi: int = +1                    # lattice handedness (matter)
    k_eigs: int = 16                 # how many SA eigenpairs to extract
    core_frac_floor: float = 0.50    # (a) the fork-b GATE1 bar
    winding_torus_floor: float = 0.20  # (d) min fraction of b_ω norm ON the winding torus
    winding_on: bool = True

    def to_coupled_cfg(self) -> CoupledCageWindingConfig:
        return CoupledCageWindingConfig(
            N=self.N,
            pml_thickness=self.pml_thickness,
            V_yield=self.V_yield,
            R=self.R,
            r=self.r,
            rate=self.rate,
            omega_b=self.omega_b,
            omega_s=self.omega_s,
            chi=self.chi,
            winding_mode="rigid_template",
            winding_on=self.winding_on,
        )


def _build_seeded_sim(cfg: CoupledEigenConfig, *, winding_on: bool) -> CoupledCageWinding:
    """Build a CoupledCageWinding at the operating point: a deep saturated A1 core
    (the posited mass, CP8 — PLANTED, not self-formed; flagged) + the separately-
    initialized (2,3) winding template (genesis-24 guard: ω is NEVER grad(V)).
    winding_on toggles the coupling Ω (False ⇒ Ω≡0 ⇒ the A1-alone HALT control)."""
    ccfg = cfg.to_coupled_cfg()
    ccfg = CoupledCageWindingConfig(**{**ccfg.__dict__, "winding_on": winding_on})
    sim = CoupledCageWinding(ccfg)
    sim.seed_A1_sech(amplitude=cfg.a1_amplitude, radius=cfg.a1_radius)
    sim.seed_winding(amplitude=1.0)
    return sim


# ═════════════════════════════════════════════════════════════════════════════
# 1. THE CORE EIGENSOLVE — extract the bound cluster of the coupled Hermitian H
# ═════════════════════════════════════════════════════════════════════════════
def _interior_radius(N: int) -> np.ndarray:
    """Radius-from-center field (N,N,N), the real-space localization coordinate."""
    c = N // 2
    i, j, k = np.indices((N, N, N))
    return np.sqrt((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2)


def _decompose_eigenvector(v: np.ndarray, sim: CoupledCageWinding) -> dict:
    """Split a coupled eigenvector into its A1 and b_ω sector content + read the
    real-space localization of each grade (the genesis-24 BOTH-conserved cert).

    Returns the per-sector NORM FRACTIONS (a1_frac + bw_frac = 1), the A1-core
    localization (core_frac), the fraction of the b_ω norm ON the winding torus
    (bw_on_torus — the (d) winding-presence witness, NOT bled into the A1 core),
    and the (2,3) winding integer read off the b_ω QUADRATURE-INVARIANT |b_ω|·ê_w
    (the winding-host read, robust to the LC L-state quadrature zeros)."""
    N, nd = sim.N, sim.ndof
    a1 = v[:nd]
    bw = v[nd:]
    n_a1 = float(np.sum(np.abs(a1) ** 2))
    n_bw = float(np.sum(np.abs(bw) ** 2))
    tot = n_a1 + n_bw + 1e-300

    r = _interior_radius(N)
    rflat = r.reshape(nd)
    core = rflat <= 4.0  # the A1 stiff-core localization mask (fork-b core scale)
    pa = np.abs(a1) ** 2
    pa = pa / (pa.sum() + 1e-300)
    a1_core_frac = float(pa[core].sum())

    # the winding torus shell (where ê_w lives — the (2,3) winding template).
    bwr = np.abs(bw.reshape(N, N, N))
    torus = (r > sim.cfg.R - 2.0) & (r < sim.cfg.R + 2.0)
    bw_norm = float((bwr ** 2).sum()) + 1e-300
    bw_on_torus = float((bwr[torus] ** 2).sum() / bw_norm)

    # the (2,3) winding integer of the eigenstate's b_ω grade (QUADRATURE-INVARIANT
    # winding-host read: ω = |b_ω|·ê_w; NEVER Re(b_ω), which the LC L-state zeros).
    omega_recon = bwr[..., None] * sim.e_w
    q = compute_Q_link(omega_recon, sim.cfg.R, sim.cfg.r)

    return {
        "a1_frac": n_a1 / tot,
        "bw_frac": n_bw / tot,
        "a1_core_frac": a1_core_frac,
        "bw_on_torus": bw_on_torus,
        "winding_Q_link": int(q["Q_link"]),
        "winding_w_tor": int(q["w_tor"]),
        "winding_Q_raw": float(q["Q_link_raw"]),
    }


def solve_coupled_spectrum(cfg: CoupledEigenConfig, *, winding_on: bool | None = None) -> dict:
    """Eigensolve the coupled Hermitian H at the SMALLEST-algebraic (most-bound)
    end (the sign-flip: the stiff-core breather is the LOWEST-w eigenvalue of H,
    NOT the highest, because the A1 block is ω_b·I − c²·L_D).

    Returns the bound cluster (the most-bound LEVEL, degeneracy-aware), its gap to
    the next level, the per-sector decomposition of its most-A1-core-localized
    member, and the fork-b breathing frequency ω_bound = √((ω_b − w_H)/c²) for the
    HALT comparison. Im(ω)=0 EXACTLY (Hermitian closed cage — gate c structural).
    α-FREE."""
    from scipy.sparse.linalg import eigsh

    won = cfg.winding_on if winding_on is None else winding_on
    sim = _build_seeded_sim(cfg, winding_on=won)
    H = sim._assemble_H()
    # SA = smallest-algebraic: the most-bound end (the sign-flipped stiff core).
    vals, vecs = eigsh(H, k=cfg.k_eigs, which="SA")
    order = np.argsort(vals)
    vals = vals[order]
    vecs = vecs[:, order]

    # the bound LEVEL = the most-bound cluster (cluster-aware, degeneracy-safe; the
    # core breather is multiply degenerate by symmetry — fork-b _cluster_spectrum).
    clusters = _cluster_spectrum(np.sort(vals - vals.min() + 1e-12))
    bound_w = float(vals.min())
    # gap = separation of the most-bound level from the next-higher level.
    bound_mult = clusters[0][1] if clusters else 1
    next_idx = min(bound_mult, len(vals) - 1)
    gap_to_next = float(vals[next_idx] - vals[0])

    # pick the most A1-core-localized member of the bound level (fork-b selector).
    best = None
    for idx in range(bound_mult):
        d = _decompose_eigenvector(vecs[:, idx], sim)
        if best is None or d["a1_core_frac"] > best["a1_core_frac"]:
            best = {**d, "idx": int(idx), "w_H": float(vals[idx])}

    # fork-b breathing frequency: H_A1 = ω_b·I − c²·L_D ⇒ L_D-eig = ω_b − w_H ⇒
    # fork-b ω = √(L_D-eig) (c_A1=1). This is the HALT-gate comparison frequency.
    ld_eig = sim.cfg.omega_b - bound_w
    forkb_omega = float(np.sqrt(abs(ld_eig)))

    return {
        "ok": True,
        "winding_on": won,
        "N": cfg.N,
        "bound_w_H": bound_w,
        "bound_multiplicity": int(bound_mult),
        "gap_to_next": gap_to_next,
        "forkb_omega": forkb_omega,          # the dimensionless ω_bound (FORM)
        "n_clusters_in_window": len(clusters),
        "spectrum_window": [float(x) for x in vals[:8]],
        "bound_mode": best,
        # Im(ω)=0 EXACTLY (Hermitian) — the lossless reactive cage (gate c).
        "omega_im": 0.0,
        "lossless": True,
    }


# ═════════════════════════════════════════════════════════════════════════════
# 2. GATE (e) — ARM-B SCRAMBLE (anti-tautology): destroy the S-STRUCTURE
# ═════════════════════════════════════════════════════════════════════════════
def solve_arm_b_scramble(cfg: CoupledEigenConfig, *, seed: int = 20260624) -> dict:
    """ARM-B (the fork-b LOAD-BEARING control, gate e): spatially PERMUTE the
    saturated A1 strain field A(x) holding its histogram FIXED, then rebuild the
    SAME coupled H (so D=1/S(A) AND the front-gated coupling Ω scramble TOGETHER,
    the consistent operator analog of fork-b's per-bond S permutation) and
    re-eigensolve. A genuine S-structure-decided confinement must DE-CONFINE
    (core_frac drop ≥ 0.30 OR core_frac < 0.50). A mode surviving ARM-B is
    BC/projector-decided = AUTO-VOID (NOT a real confinement).

    The permutation is the SAME histogram-preserving shuffle fork-b uses; the
    bound mode is judged by the IDENTICAL selector as GATE1. α-FREE."""
    from scipy.sparse.linalg import eigsh

    # baseline: the real graded operator (the make-or-break run).
    base = solve_coupled_spectrum(cfg, winding_on=cfg.winding_on)
    base_cf = base["bound_mode"]["a1_core_frac"]

    # ARM-B: build the sim, then PERMUTE the strain field that drives BOTH D and Ω.
    sim = _build_seeded_sim(cfg, winding_on=cfg.winding_on)
    rng = np.random.default_rng(seed)
    # the strain field A(x) the operator reads (from |a_A1|); permute it spatially.
    A_flat = np.abs(sim.a_A1).reshape(-1).copy()
    perm = rng.permutation(A_flat.size)
    A_perm = A_flat[perm].reshape(sim.N, sim.N, sim.N)
    hist_preserved = bool(np.allclose(np.sort(A_flat), np.sort(A_perm.reshape(-1))))
    # plant the permuted strain as the A1 field (so strain()/stiffness_D()/Ω read it)
    sim.a_A1 = A_perm.astype(np.complex128)
    H = sim._assemble_H()
    vals, vecs = eigsh(H, k=cfg.k_eigs, which="SA")
    order = np.argsort(vals)
    vecs = vecs[:, order]
    armb = _decompose_eigenvector(vecs[:, 0], sim)
    armb_cf = armb["a1_core_frac"]

    margin = base_cf - armb_cf
    deconfines = bool(margin >= 0.30 or armb_cf < 0.50)
    survives_auto_void = bool(armb_cf >= 0.50 and not deconfines)
    return {
        "ok": True,
        "baseline_core_frac": base_cf,
        "armB_core_frac": armb_cf,
        "armB_margin": margin,
        "armB_histogram_preserved": hist_preserved,
        "armB_deconfines": deconfines,
        "armB_survives_AUTO_VOID": survives_auto_void,
        "seed": seed,
    }


# ═════════════════════════════════════════════════════════════════════════════
# 3. HALT GATE — winding-OFF must recover the fork-b confined A1 mode
# ═════════════════════════════════════════════════════════════════════════════
COLD_CAGE_OMEGA_CUTOFF = 2.87  # FORM anchor: test_l3_mass_cage.py:18 (NOT m_e — definitional)


def halt_gate(cfg: CoupledEigenConfig) -> dict:
    """HALT GATE (pre-reg §6.1): with winding_on=False (Ω≡0), the eigensolve MUST
    recover the fork-b confined A1 mode (core_frac ≥ 0.50, lossless). If not, the
    instrument is broken → HALT. We ALSO report whether the recovered fork-b ω is
    near the cold-cage ω_cutoff≈2.87 anchor (a FORM cross-check, NOT a pass
    condition — the pass condition is core_frac + lossless only)."""
    r = solve_coupled_spectrum(cfg, winding_on=False)
    bm = r["bound_mode"]
    core_ok = bool(bm["a1_core_frac"] >= cfg.core_frac_floor)
    lossless = bool(r["lossless"])
    near_anchor = bool(abs(r["forkb_omega"] - COLD_CAGE_OMEGA_CUTOFF) / COLD_CAGE_OMEGA_CUTOFF < 0.10)
    return {
        "ok": True,
        "forkb_omega": r["forkb_omega"],
        "a1_core_frac": bm["a1_core_frac"],
        "lossless": lossless,
        "near_cold_cage_anchor_2p87": near_anchor,
        "recovers_forkb": bool(core_ok and lossless),
    }
