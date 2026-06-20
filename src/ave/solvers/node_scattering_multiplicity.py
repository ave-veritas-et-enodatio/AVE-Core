"""Node-Scattering Multiplicity / Containment Gate — BEDROCK (scope b, Fork A).

Prereg: research/2026-06-20_node-scattering-containment-gate_prereg.md
        (frozen commit f87914fa, the FIRST commit of this branch).

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
GOAL  : test whether the vacuum's CONFINEMENT MULTIPLICITY is set by the lattice's
        NODE VALENCE. The degree-3 chiral srs net and the degree-4 diamond net give
        STRUCTURALLY DISTINCT scattering operators S_n = (2/n)J - I whose DIFFERENTIAL
        (-1) eigenspace has multiplicity n-1 (2 for srs, 3 for diamond).

SCOPE : (b) ONLY = Fork A (the multiplicity/sector test). Forks B/C/D are DEFERRED
        (prereg §7; Grant's bulk-saturation framing for B carried there).

BEDROCK (Stage 1, THIS FILE's load-bearing content): the operator is assembled from
        the lattice's OWN bond-graph CONNECT map (chiral_lattice.scatter_matrix(n) +
        connect_index / build_srs_net / build_diamond_net), so n=3 (srs, degree-3) and
        n=4 (diamond, degree-4) are STRUCTURALLY DIFFERENT operators -- NOT the dense
        TETRA_OFFSETS cube that graded_vacuum_network.py hardwires. This is PURE LINEAR
        ALGEBRA: no dynamics, no core, no boundary.

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-NATIVE-CHECK (walked BEFORE any numerical code, per operating principle 1)
═══════════════════════════════════════════════════════════════════════════════
  * K4 / graph   : the operator is the Op5 shunt-junction scatter S_n = (2/n)J - I
                   (chiral_lattice.py:81-102) composed with the directed-edge CONNECT
                   permutation from connect_index() (chiral_lattice.py:133-147). Built
                   FROM the graph, never imposed on a Cartesian grid. The dense
                   TETRA_OFFSETS cube (graded_vacuum_network.py) is the BUG this fixes.
  * Cosserat     : the winding sector (CHARGE-3) is validated via charge_quantization
                   (omega-grade only, A1-perp-T2 honoured). NEVER wired into the A1
                   (V_inc, V_ref) phasor (master-equation.md:20; genesis-24 caution).
  * phase vs real: S_n eigenvectors live in n-PORT space; A1/Cosserat grades in
                   real-space. The port->grade map is the bond-direction embedding
                   bond_unit[u][p] (chiral_lattice.py:114). Stage 2 SHOWS this map.
  * alpha-free   : S_n contains NO alpha; the winding integer Q_link contains NO alpha.
                   alpha-invariance is STRUCTURAL (the modules don't import ALPHA), and
                   is the load-bearing, frame-independent anchor (prereg §2d).

This file = STAGE 1 (bedrock + bare-spectrum validate-on-known). Stage 2 (the
multiplicity observable + Fork-A test) is built ONLY if Stage 1 passes.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.chiral_lattice import (
    LatticeNet,
    build_diamond_net,
    build_srs_net,
    scatter_matrix,
)

# ─────────────────────────────────────────────────────────────────────────────
# ANTI-LEAK IMPORT-GUARD: this BEDROCK is pure linear algebra on the graph. No
# alpha-carrier, no Q_TANK, no ELECTRON instance may be reachable here. The
# operator and its spectrum are alpha-free BY CONSTRUCTION (the load-bearing
# anchor, prereg §2d).
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "alpha-leak: ALPHA must NOT be imported into the bedrock"
assert "Q_TANK" not in globals(), "alpha-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "ELECTRON" not in globals(), "alpha-leak: ELECTRON instance must NOT be imported"


# ═════════════════════════════════════════════════════════════════════════════
# 1. LOCAL bare-scatter spectrum (validate-on-known §2a) — the distinctness witness
# ═════════════════════════════════════════════════════════════════════════════
def local_scatter_spectrum(n: int) -> dict:
    """Bare spectrum of the single-node scatter S_n = (2/n)J - I.

    S_n is a rank-1 perturbation of -I: the all-ones port-sum vector is the single
    +1 eigenvector (the COMMON MODE = symmetric breathing channel = Grant's
    bulk-saturation channel, Fork B), and its orthogonal complement is the -1
    eigenspace of dimension n-1 (the DIFFERENTIAL modes). The differing -1
    multiplicity (2 for n=3 / 3 for n=4) IS the structural distinctness.

    Returns dict: eigenvalues (sorted), the +1 / -1 multiplicities, the +1
    eigenvector (common mode), and the S^2 = I (orthogonal-reflection) check.
    alpha-FREE: S_n contains no alpha.
    """
    S = scatter_matrix(n)
    evals, evecs = np.linalg.eigh(S)
    evals = np.round(evals, 12)
    mult_plus1 = int(np.sum(np.isclose(evals, 1.0, atol=1e-9)))
    mult_minus1 = int(np.sum(np.isclose(evals, -1.0, atol=1e-9)))
    # common-mode (+1) eigenvector = the symmetric port-sum (up to sign/normalization)
    plus_idx = np.where(np.isclose(evals, 1.0, atol=1e-9))[0]
    common_mode = evecs[:, plus_idx[0]] if len(plus_idx) else None
    return {
        "n": n,
        "eigenvalues": evals.tolist(),
        "mult_plus1": mult_plus1,
        "mult_minus1": mult_minus1,  # = differential multiplicity = n-1
        "differential_multiplicity": mult_minus1,
        "common_mode_eigvec": None if common_mode is None else common_mode.tolist(),
        "common_mode_is_port_sum": bool(
            common_mode is not None
            and np.allclose(np.abs(common_mode), np.abs(common_mode[0]), atol=1e-9)
        ),
        "S_squared_is_identity": bool(np.allclose(S @ S, np.eye(n), atol=1e-12)),
        "spectrum_is_canonical": bool(mult_plus1 == 1 and mult_minus1 == n - 1),
    }


# ═════════════════════════════════════════════════════════════════════════════
# 2. GLOBAL scattering operator on the ACTUAL lattice CONNECT map (the BEDROCK)
# ═════════════════════════════════════════════════════════════════════════════
def assemble_global_scattering(net: LatticeNet) -> np.ndarray:
    """The lattice scattering operator 𝓢 = C @ (I_N ⊗ S_n), as a dense matrix.

    Acts on the per-port amplitude vector V ∈ ℝ^(N·d) (flattened (N, degree)):
      1. SCATTER each node locally by S_n (block-diagonal I_N ⊗ S_n);
      2. CONNECT: permute reflected→incident along the reverse-port map
         (connect_index(): V_new.flat[dst] = V_ref.flat[src]).

    Because srs has degree d=3 and diamond has d=4 with DIFFERENT connectivity,
    𝓢_srs and 𝓢_diamond have DIFFERENT dimension AND different permutation AND
    different spectrum — STRUCTURALLY distinct operators. This is the bedrock
    object the prereg demands (NOT the dense TETRA_OFFSETS cube).

    NOTE: this routes through net.connect_index() — the directed-edge CONNECT of
    the actual srs / diamond bond-graph — which is the call-site
    graded_vacuum_network.py never makes (build_srs_net had ZERO solver
    call-sites before this module). alpha-FREE (geometry + S_n only).
    """
    d = net.degree
    N = net.n_nodes
    ndof = N * d
    S = scatter_matrix(d)

    # block-diagonal local scatter: V_ref[u] = S @ V_inc[u]
    scatter_block = np.zeros((ndof, ndof))
    for u in range(N):
        scatter_block[u * d:(u + 1) * d, u * d:(u + 1) * d] = S

    # CONNECT permutation: V_new.flat[dst] = V_ref.flat[src]
    src_flat, dst_flat = net.connect_index()
    C = np.zeros((ndof, ndof))
    C[dst_flat, src_flat] = 1.0

    return C @ scatter_block


def global_spectrum(net: LatticeNet, *, k_report: int = 12) -> dict:
    """Eigenvalues of the assembled lattice scattering operator 𝓢.

    𝓢 = C @ (I ⊗ S_n) is a product of an orthogonal reflection block and a
    permutation, so it is ORTHOGONAL — all eigenvalues lie on the unit circle.
    Returns the dimension, the magnitude spectrum (should be all 1), and a sample
    of eigenvalues. alpha-FREE.
    """
    M = assemble_global_scattering(net)
    evals = np.linalg.eigvals(M)
    mags = np.abs(evals)
    order = np.argsort(-mags)
    return {
        "net": net.name,
        "degree": net.degree,
        "n_nodes": net.n_nodes,
        "ndof": M.shape[0],
        "is_orthogonal": bool(np.allclose(M @ M.T, np.eye(M.shape[0]), atol=1e-9)),
        "all_eigs_unit_modulus": bool(np.allclose(mags, 1.0, atol=1e-9)),
        "max_abs_eig": float(mags.max()),
        "min_abs_eig": float(mags.min()),
        "sample_eigs": [complex(evals[i]) for i in order[:k_report]],
    }


# ═════════════════════════════════════════════════════════════════════════════
# 3. DIFFERENTIAL projector P_{-1} (fix the sector FROM THE OPERATOR first)
# ═════════════════════════════════════════════════════════════════════════════
def differential_projector(n: int) -> np.ndarray:
    """P_{-1} = the orthogonal projector onto S_n's -1 eigenspace (the n-1
    DIFFERENTIAL modes). For S_n = (2/n)J - I, the -1 eigenspace is the orthogonal
    complement of the all-ones vector, so P_{-1} = I - (1/n)J. alpha-FREE.

    This is the SECTOR fixed from the OPERATOR (prereg §3.1) — before any physics.
    """
    J = np.ones((n, n))
    return np.eye(n) - J / n


def common_mode_projector(n: int) -> np.ndarray:
    """P_{+1} = projector onto the +1 (common-mode) eigenspace = (1/n)J. This is
    Grant's bulk-saturation channel (Fork B, DEFERRED). Exposed so Fork A's
    P_{-1} result can report the complementary common-mode fraction. alpha-FREE."""
    return np.ones((n, n)) / n


# ═════════════════════════════════════════════════════════════════════════════
# 4. H1 collapse check — are srs (n=3) and diamond (n=4) genuinely distinct?
# ═════════════════════════════════════════════════════════════════════════════
def operators_are_distinct(net_a: LatticeNet, net_b: LatticeNet) -> dict:
    """HALT-condition H1 witness: confirm 𝓢_a and 𝓢_b are STRUCTURALLY different.

    Distinct iff (i) different per-node degree, OR (ii) different operator
    dimension, OR (iii) different differential multiplicity. If srs and diamond
    assemble the IDENTICAL operator the collapse (the graded_vacuum_network bug)
    is NOT fixed -> HALT. alpha-FREE.
    """
    spec_a = local_scatter_spectrum(net_a.degree)
    spec_b = local_scatter_spectrum(net_b.degree)
    distinct = (
        net_a.degree != net_b.degree
        or spec_a["differential_multiplicity"] != spec_b["differential_multiplicity"]
    )
    return {
        "net_a": net_a.name, "degree_a": net_a.degree,
        "net_b": net_b.name, "degree_b": net_b.degree,
        "diff_mult_a": spec_a["differential_multiplicity"],
        "diff_mult_b": spec_b["differential_multiplicity"],
        "distinct": bool(distinct),
        "collapse_detected": bool(not distinct),  # H1
    }


# ═════════════════════════════════════════════════════════════════════════════
# 5. BEDROCK validate-on-known runner (Stage-1 HALT gate)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class BedrockConfig:
    """Frozen geometry for the bedrock assembly. alpha-FREE (lattice size only)."""

    L_srs: int = 2       # srs cubic cells/side (8 motif nodes/cell -> 64 nodes @ L=2)
    L_diamond: int = 4   # diamond needs even L>=4


def bedrock_validate_on_known(cfg: BedrockConfig | None = None) -> dict:
    """Run the Stage-1 bedrock validate-on-known and bin HALT vs PROCEED.

    Anchors (prereg §2a, §2e; the winding/photon anchors §2b–2c are checked in the
    test module against charge_quantization and test_l1_photon):
      * §2a bare spectrum: S3 -> {+1×1, -1×2}, S4 -> {+1×1, -1×3}  (HALT H2 if not)
      * H1 distinctness: srs (deg 3) and diamond (deg 4) assemble DIFFERENT operators
      * global operator: orthogonal, all eigs unit-modulus (sanity)
    Returns a dict with each anchor + the binned status (PROCEED / HALT + reason).
    """
    cfg = cfg or BedrockConfig()
    out: dict = {"config": {"L_srs": cfg.L_srs, "L_diamond": cfg.L_diamond}}

    s3 = local_scatter_spectrum(3)
    s4 = local_scatter_spectrum(4)
    out["S3"] = s3
    out["S4"] = s4

    srs = build_srs_net(L=cfg.L_srs)
    dia = build_diamond_net(L=cfg.L_diamond)
    out["distinctness"] = operators_are_distinct(srs, dia)
    out["global_srs"] = global_spectrum(srs)
    out["global_diamond"] = global_spectrum(dia)

    # ── HALT gates (prereg §5) ──
    halt_reasons = []
    if not s3["spectrum_is_canonical"] or s3["differential_multiplicity"] != 2:
        halt_reasons.append(f"H2: S3 spectrum not {{+1, -1x2}} (got {s3['eigenvalues']})")
    if not s4["spectrum_is_canonical"] or s4["differential_multiplicity"] != 3:
        halt_reasons.append(f"H2: S4 spectrum not {{+1, -1x3}} (got {s4['eigenvalues']})")
    if out["distinctness"]["collapse_detected"]:
        halt_reasons.append("H1: srs and diamond collapsed to the IDENTICAL operator")
    if not out["global_srs"]["all_eigs_unit_modulus"]:
        halt_reasons.append("global_srs not orthogonal (eigs off unit circle)")
    if not out["global_diamond"]["all_eigs_unit_modulus"]:
        halt_reasons.append("global_diamond not orthogonal (eigs off unit circle)")

    if halt_reasons:
        out["status"] = "HALT"
        out["halt_reasons"] = halt_reasons
    else:
        out["status"] = "PROCEED"
        out["summary"] = (
            f"srs(deg3) differential mult = {s3['differential_multiplicity']} "
            f"(= photon 2 transverse DOF); diamond(deg4) differential mult = "
            f"{s4['differential_multiplicity']}; operators structurally distinct."
        )
    return out


if __name__ == "__main__":
    import json

    print("NODE-SCATTERING MULTIPLICITY GATE — STAGE 1 BEDROCK (scope b, Fork A)")
    print("=" * 70)
    result = bedrock_validate_on_known()
    print(json.dumps(result, indent=2, default=str))
    print("=" * 70)
    print(f"STATUS: {result['status']}")
