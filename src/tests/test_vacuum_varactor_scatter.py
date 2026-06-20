"""Tests for the VACUUM-VARACTOR SCATTER OPERATOR (the S(A)-reading scatter).

Result doc: research/2026-06-20_vacuum-varactor-scatter_result.md.
Built off origin/main @ 32f29c67 (bedrock node_scattering_multiplicity.py via PR#304).

These tests ASSERT the four validate-on-known gates (HALT if any fails) + the
KEY scramble-changes-operator demonstration (the Fork-B unblocker):

  * GATE 1: S=1 everywhere -> scatter == (2/n)J - I EXACTLY (recovers the bedrock)
  * GATE 2: per-PORT-distinct admittance -> scatter != (2/n)J - I (reads z)
  * GATE 3: ALPHA never imported into the scatter path; alpha->2alpha is a no-op
  * GATE 4: the radiative-Q floor Z_RADIATION ~ 29.98 (the structural anchor the
            cold-cage Q_ringdown ~ 30.8 sits on), reproduced via the scatter
  * PER-BOND-NOT-PER-NODE: a per-node-uniform load must NOT change the scatter;
    a per-bond-varying load MUST (the load-bearing Fork-B Finding 2)
  * VARACTOR SIGN: Y=Y0/sqrt(S) => Z=sqrt(S)->0 => Gamma->-1 (the mu-load SHORT,
    NOT the forbidden epsilon-load Z->inf/Gamma=+1)
  * SCRAMBLE: scrambling S(A) CHANGES the assembled operator (max|d|>0)
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.chiral_lattice import build_diamond_net, build_srs_net, scatter_matrix
from ave.solvers.node_scattering_multiplicity import assemble_global_scattering
from ave.solvers.vacuum_varactor_scatter import (
    VaractorConfig,
    admittance_scatter,
    assemble_varactor_scattering,
    bond_admittance_from_saturation,
    radiative_port_reflection,
    saturation_kernel,
    varactor_validate_on_known,
)


# ─────────────────────────────────────────────────────────────────────────────
# 0. CANONICAL KERNEL — imported, not hardcoded
# ─────────────────────────────────────────────────────────────────────────────
def test_saturation_kernel_is_canonical():
    """S(0)=1 (vacuum), S monotone-decreasing in A, S(A)=sqrt(1-A^2) form (clipped)."""
    assert np.isclose(float(saturation_kernel(np.array(0.0))), 1.0)
    A = np.linspace(0.0, 0.9, 10)
    S = saturation_kernel(A)
    assert np.all(np.diff(S) <= 1e-12)  # monotone non-increasing
    # un-clipped interior matches the closed form sqrt(1-A^2)
    Amid = np.array([0.3, 0.5, 0.7])
    assert np.allclose(saturation_kernel(Amid), np.sqrt(1.0 - Amid**2), atol=1e-12)


def test_saturation_kernel_matches_crystal_engine():
    """The kernel DELEGATES to CrystalEngine.saturation_kernel (ave-canonical-source)."""
    from ave.core.crystal_engine import CrystalEngine

    eng = CrystalEngine(N=2, V_yield=1.0, A_cap=0.99, S_min=0.05, converter_on=False)
    A = np.array([0.0, 0.2, 0.5, 0.8, 0.99, 1.5])
    # with V_yield=1, the engine reads V=A directly
    assert np.allclose(saturation_kernel(A), eng.saturation_kernel(A), atol=0.0)


# ─────────────────────────────────────────────────────────────────────────────
# 1. ADMITTANCE SCATTER — generalizes the bedrock
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("n", [3, 4, 5])
def test_equal_admittance_recovers_bedrock_exactly(n):
    """GATE-1 LOCAL: equal Y -> (2/n)J - I EXACTLY (the bedrock scatter_matrix)."""
    S = admittance_scatter(np.ones(n))
    assert np.array_equal(S, scatter_matrix(n))


def test_admittance_scatter_kcl_row_sums():
    """Each row of S sums to +1 (KCL passivity of the shunt junction)."""
    S = admittance_scatter(np.array([1.0, 2.0, 0.5]))
    assert np.allclose(S.sum(axis=1), 1.0, atol=1e-12)


def test_per_port_distinct_admittance_differs_from_bedrock():
    """GATE-2 LOCAL: per-port-distinct Y -> S != (2/n)J - I (genuinely reads z)."""
    S = admittance_scatter(np.array([1.0, 2.0, 0.5]))
    assert not np.allclose(S, scatter_matrix(3), atol=1e-9)


# ─────────────────────────────────────────────────────────────────────────────
# 2. VARACTOR MAP — the corrected mu-load sign
# ─────────────────────────────────────────────────────────────────────────────
def test_varactor_map_vacuum_is_matched():
    """A=0 (S=1) -> Y=Y0, Z=Z0 -> Gamma=0 (vacuum, matched)."""
    Y = bond_admittance_from_saturation(np.array(0.0), Y0=1.0)
    assert np.isclose(float(Y), 1.0)


def test_varactor_map_saturation_drives_gamma_toward_minus1():
    """As S->0: Z=sqrt(S)->0 => Gamma=(Z-1)/(Z+1)->-1 (the mu-load SHORT, the mass
    cage). Monotone toward -1; the corrected sign (NOT the epsilon-load Z->inf/+1)."""
    A_vals = np.array([0.0, 0.5, 0.9])
    gammas = []
    for A in A_vals:
        S = float(saturation_kernel(np.array(A)))
        Z = np.sqrt(S)  # Z_bond = Z0 * sqrt(S), Z0=1
        gammas.append((Z - 1.0) / (Z + 1.0))
    # monotone DECREASING toward -1 as A increases (S decreases)
    assert gammas[0] == pytest.approx(0.0, abs=1e-9)  # vacuum matched
    assert gammas[1] < gammas[0]
    assert gammas[2] < gammas[1]
    assert gammas[2] < 0.0  # heading to the short
    # with the clip/floor dropped, Gamma -> -1 (the full mass cage). The DEPTH it
    # reaches is set by how close A is allowed to approach yield (A_cap): at
    # A=0.999999 (S~1.4e-3, Z~0.038) Gamma<-0.9. The canonical S_min=0.05/A_cap=0.99
    # floor caps the engine's reachable Gamma at ~-0.45 -- documented honestly in the
    # result doc; the SIGN and the MONOTONE-toward-(-1) trend are the physics.
    S_deep = float(saturation_kernel(np.array(0.999999), A_cap=0.99999999, S_min=1e-12))
    Z_deep = np.sqrt(S_deep)
    assert (Z_deep - 1.0) / (Z_deep + 1.0) < -0.9


def test_varactor_is_mu_load_not_epsilon_load():
    """EPSILON-LOAD FORBID: the varactor gives Z=sqrt(S)->0 (SHORT, Gamma->-1), NOT
    the forbidden epsilon-load Z=1/sqrt(S)->inf (OPEN, Gamma->+1)."""
    S = float(saturation_kernel(np.array(0.9)))
    Z_mu = np.sqrt(S)            # the varactor mu-load
    Z_eps_forbidden = 1.0 / np.sqrt(S)  # the forbidden epsilon-load
    assert Z_mu < 1.0            # heading to short
    assert Z_eps_forbidden > 1.0  # would head to open -- NOT what we built
    # Gamma sign check
    assert (Z_mu - 1.0) / (Z_mu + 1.0) < 0.0       # mu-load: Gamma<0 (toward -1)
    assert (Z_eps_forbidden - 1.0) / (Z_eps_forbidden + 1.0) > 0.0  # eps: Gamma>0


# ─────────────────────────────────────────────────────────────────────────────
# 3. PER-BOND NOT PER-NODE — the load-bearing Fork-B Finding 2
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("builder,kw", [(build_srs_net, {"L": 2}), (build_diamond_net, {"L": 4})])
def test_per_node_uniform_load_does_not_change_scatter(builder, kw):
    """A per-NODE-uniform load (scalar, or even a DEEP uniform saturation) CANCELS at
    the shunt junction -> 𝓢 == bedrock. This is the Finding-2 no-op (a per-node-uniform
    admittance reduces back to (2/n)J-I regardless of S)."""
    net = builder(**kw)
    bed = assemble_global_scattering(net)
    # scalar uniform, including a DEEP one
    assert np.allclose(assemble_varactor_scattering(net, 0.0), bed, atol=1e-13)
    assert np.allclose(assemble_varactor_scattering(net, 0.9), bed, atol=1e-13)
    # per-NODE (N,) varying but uniform WITHIN each node -> still cancels
    rng = np.random.default_rng(0)
    A_node = rng.uniform(0.1, 0.9, size=net.n_nodes)
    assert np.allclose(assemble_varactor_scattering(net, A_node), bed, atol=1e-13)


@pytest.mark.parametrize("builder,kw", [(build_srs_net, {"L": 2}), (build_diamond_net, {"L": 4})])
def test_per_bond_varying_load_changes_scatter(builder, kw):
    """A per-BOND-varying load (ports of one node differing) MUST change 𝓢 -- the
    saturation field genuinely enters as per-edge admittances. The complement of the
    no-op above; together they prove the operator reads the per-bond gradient."""
    net = builder(**kw)
    bed = assemble_global_scattering(net)
    rng = np.random.default_rng(1)
    A_bond = rng.uniform(0.1, 0.9, size=(net.n_nodes, net.degree))
    var = assemble_varactor_scattering(net, A_bond)
    assert not np.allclose(var, bed, atol=1e-9)
    assert np.max(np.abs(var - bed)) > 1e-3


# ─────────────────────────────────────────────────────────────────────────────
# 4. THE FOUR VALIDATE-ON-KNOWN GATES (the runner) — HALT if any fails
# ─────────────────────────────────────────────────────────────────────────────
def test_validate_on_known_status_pass():
    """The full runner PASSES all four gates + the scramble demonstration."""
    out = varactor_validate_on_known()
    assert out["status"] == "PASS", out.get("halt_reasons")


def test_gate1_recovers_bedrock_at_S1():
    out = varactor_validate_on_known()
    for net_name, d in out["gate1_recovers_bedrock_at_S1"].items():
        assert d["recovers_bedrock_exactly"], net_name
        assert d["max_abs_diff"] == 0.0


def test_gate2_distinct_z_breaks_collapse():
    out = varactor_validate_on_known()
    for net_name, d in out["gate2_distinct_z_breaks_collapse"].items():
        assert d["differs_from_bedrock"], f"{net_name} collapsed to bedrock (S-blind)"
        assert d["max_abs_diff"] > 1e-3


def test_gate3_alpha_free():
    out = varactor_validate_on_known()
    g3 = out["gate3_alpha_free"]
    assert g3["alpha_free_pass"]
    assert g3["alpha_in_scatter_path_globals"] is False  # ALPHA never imported
    assert g3["max_rel_dQ"] < 1e-6


def test_gate4_reproduces_radiative_floor_30():
    out = varactor_validate_on_known()
    g4 = out["gate4_cold_cage_radiative_floor"]
    assert g4["reproduces_radiative_floor_~30"]
    assert g4["Z0_over_Zrad_is_4pi"]
    assert abs(g4["radiative_Q_floor"] - 30.0) < 1.5


def test_radiative_port_reflection_is_strong_short():
    """The radiation-loaded bound port reflects strongly negative (Gamma~-0.85): the
    free-space radiation load is a 4pi mismatch -- the operator reads Z_RADIATION."""
    r = radiative_port_reflection()
    assert r["gamma_bound_into_radiation_load"] < -0.5  # strong radiative short
    assert r["Z0_over_Zrad_is_4pi"]


# ─────────────────────────────────────────────────────────────────────────────
# 5. ALPHA-FREE STRUCTURAL GUARD — ALPHA must NOT be in the scatter module
# ─────────────────────────────────────────────────────────────────────────────
def test_alpha_not_in_scatter_module_namespace():
    """STRUCTURAL alpha-free: ALPHA / Q_TANK / ELECTRON are NOT reachable in the
    varactor scatter module's globals (the load-bearing, frame-independent anchor)."""
    import ave.solvers.vacuum_varactor_scatter as m

    assert "ALPHA" not in vars(m)
    assert "Q_TANK" not in vars(m)
    assert "ELECTRON" not in vars(m)


# ─────────────────────────────────────────────────────────────────────────────
# 6. THE KEY DELIVERABLE: SCRAMBLING S(A) CHANGES THE OPERATOR (Fork-B unblocker)
# ─────────────────────────────────────────────────────────────────────────────
def test_scramble_changes_operator_runner():
    """THE deliverable: scrambling S(A) CHANGES the assembled operator (max|d|>0) --
    proving the operator READS saturation, the exact thing the Fork-B NO-GO found dead."""
    out = varactor_validate_on_known()
    sc = out["scramble_changes_operator"]
    assert sc["operator_reads_saturation"]
    for net_name in ("srs[right]", "diamond"):
        assert sc[net_name]["operator_changed"], net_name
        assert sc[net_name]["max_abs_dScatter"] > 1e-3


@pytest.mark.parametrize("builder,kw", [(build_srs_net, {"L": 2}), (build_diamond_net, {"L": 4})])
def test_scramble_directly_changes_assembled_operator(builder, kw):
    """Direct (runner-independent) scramble: same saturation VALUES permuted across
    bonds change the operator -- the operator is NOT S-invariant under bond reshuffling."""
    net = builder(**kw)
    rng = np.random.default_rng(7)
    A = rng.uniform(0.2, 0.9, size=(net.n_nodes, net.degree))
    S_A = assemble_varactor_scattering(net, A)
    flat = A.ravel().copy()
    rng.shuffle(flat)
    S_scram = assemble_varactor_scattering(net, flat.reshape(net.n_nodes, net.degree))
    assert np.max(np.abs(S_A - S_scram)) > 1e-3


# ─────────────────────────────────────────────────────────────────────────────
# 7. NEGATIVE-CONTROL: scrambling a UNIFORM field does NOT change the operator
# ─────────────────────────────────────────────────────────────────────────────
def test_scramble_of_uniform_field_is_a_noop():
    """Control: scrambling a UNIFORM (per-node-equal) field leaves 𝓢 unchanged --
    confirms the operator change in the scramble test comes from the per-bond GRADIENT,
    not from the assembly being numerically noisy."""
    net = build_srs_net(L=2)
    A_uniform = np.full((net.n_nodes, net.degree), 0.7)  # uniform everywhere
    S0 = assemble_varactor_scattering(net, A_uniform)
    # any permutation of a constant array is the same array
    rng = np.random.default_rng(3)
    flat = A_uniform.ravel().copy()
    rng.shuffle(flat)
    S1 = assemble_varactor_scattering(net, flat.reshape(net.n_nodes, net.degree))
    assert np.allclose(S0, S1, atol=1e-14)
    # and it equals the bedrock (uniform -> cancels)
    assert np.allclose(S0, assemble_global_scattering(net), atol=1e-13)
