#!/usr/bin/env python3
"""Machine checks for the SCX Phase-1 exporter.

Prereg (FROZEN): ``research/2026-08-25_solver-crosscheck-phase1_prereg-FROZEN.md``
GO gate: ``_orchestration/docket-entries/2026-08-24-ruling-r56-scx-trades.md`` (R56).

THE POINT OF THIS FILE
----------------------
``TestFL1DelayConvention`` is the mandated FL-1 gate. THREE live in-tree symbols
encode THREE DIFFERENT bond delays, and the one whose NAME invites the mistake
(``bond_lc``) is the WRONG one for this exporter. Reaching for it applies a
uniform sqrt(3) offset to every frequency the lane measures, which reads as a
spectacular engine defect and is nothing but a label mismatch.

R56 item 2 mandates "the machine check that the emitted delay matches [the
declared convention]". This is that check, and per the self-referential-gate
discipline it fires in BOTH directions: ``test_gate_fires_on_the_r1_delay`` and
``test_gate_fires_on_the_third_convention`` build the wrong delays and assert
the R2 assertion WOULD reject them, so the gate is provably able to fire rather
than vacuously green.

Every fixture below is built from IMPORTED engine symbols. No line number, no
branch name, no hard-coded frequency appears in any assertion.
"""

from __future__ import annotations

import ast
import math
import re

import pytest

from ave.core.chiral_lattice import build_diamond_net, build_srs_net
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR
from ave.core.constants import C_CELL, L_CELL, OMEGA_C, Z_0
from ave.solvers import scx_spice_export as X

# One trivial analysis, so emission is exercised end-to-end rather than in parts.
_AC = [X.AcAnalysis(n=1, f1=1.0e20, f2=1.0e20, out="unused.dat", vectors=("n0",))]

_TD_RE = re.compile(r"\bTD=([0-9eE+\-.]+)")
_Z0_RE = re.compile(r"\bZ0=([0-9eE+\-.]+)")


def _emit_bond(convention: str = X.CONVENTION, **kw) -> str:
    """One bond, open-open (the L1 object) -- the smallest netlist with a TD."""
    return X.emit_tl_network(
        [(0, 1)], 2, 0, _AC, title="FL-1 fixture", convention=convention, **kw
    )


def _emitted_tds(netlist: str) -> list[float]:
    """Every TD on a T card (NOT the header's commentary lines)."""
    return [
        float(_TD_RE.search(ln).group(1))
        for ln in netlist.splitlines()
        if ln.startswith("T") and _TD_RE.search(ln)
    ]


# ═════════════════════════════════════════════════════════════════════════════
class TestFL1DelayConvention:
    """The FL-1 gate: the emitted delay matches the convention the exporter
    DECLARES, and provably rejects the two conventions it does not."""

    def test_exporter_declares_r2(self):
        assert X.CONVENTION == "R2", (
            "R56 item 2 pins R2 as the exporter's emitted label. If this "
            "constant changes, the netlist header, the prereg and this gate "
            "must move together -- deliberately, not by drift."
        )

    def test_emitted_td_is_bit_identical_to_the_r2_form(self):
        """TD == ANALYTIC_NETWORK_FACTOR / OMEGA_C, both imported. Bit-exact."""
        expected = ANALYTIC_NETWORK_FACTOR / OMEGA_C
        tds = _emitted_tds(_emit_bond())
        assert tds, "no T card emitted"
        for td in tds:
            assert td == expected, (
                f"emitted TD {td!r} != the R2 delay {expected!r}. "
                "The exporter's emitted delay does not match the convention it declares."
            )

    def test_emitted_td_is_not_the_r1_bond_lc_delay(self):
        """The wrong-symbol reach: ``bond_lc()`` gives ell_node/c_0 = 1/omega_C."""
        r1 = X.bond_delay_r1_NOT_OURS()
        td = _emitted_tds(_emit_bond())[0]
        assert td != r1, "exporter emitted the R1 delay -- the bond_lc() wrong-symbol reach"
        assert math.isclose(r1 / td, math.sqrt(3.0), rel_tol=1e-12), (
            f"R1/R2 delay ratio {r1 / td!r} is not sqrt(3); the FL-1 fork is not "
            "the fork this gate was written against -- re-derive before trusting it."
        )

    def test_emitted_td_is_not_the_third_convention(self):
        """FL-1(iii): ``bond_length_SI = sqrt(3)*L_NODE`` gives a THIRD delay."""
        third = X.bond_delay_iii_NOT_OURS()
        td = _emitted_tds(_emit_bond())[0]
        assert td != third, "exporter emitted the FL-1(iii) delay"
        assert math.isclose(third / td, 3.0, rel_tol=1e-12)

    # ── both-directions: the gate must be able to FIRE ────────────────────────
    def test_gate_fires_on_the_r1_delay(self):
        """Mutation: emit R1 and assert the R2 assertion REJECTS it."""
        td = _emitted_tds(_emit_bond(convention="R1"))[0]
        assert td != ANALYTIC_NETWORK_FACTOR / OMEGA_C, (
            "ANTI-TAUTOLOGY FAILURE: the R2 assertion accepts an R1 netlist, so "
            "the FL-1 gate cannot fire and is vacuously green."
        )

    def test_gate_fires_on_the_third_convention(self):
        td = _emitted_tds(_emit_bond(convention="III"))[0]
        assert td != ANALYTIC_NETWORK_FACTOR / OMEGA_C

    def test_unknown_convention_is_refused(self):
        with pytest.raises(ValueError, match="unknown delay convention"):
            _emit_bond(convention="R7")

    def test_header_records_all_three_delays_and_the_emitted_one(self):
        """The netlist is the hand-audit artifact: an auditor must be able to
        check the convention without reading any Python."""
        nl = _emit_bond()
        assert "DELAY CONVENTION EMITTED: R2" in nl
        for fn in (X.bond_delay, X.bond_delay_r1_NOT_OURS, X.bond_delay_iii_NOT_OURS):
            assert X._fmt(fn()) in nl, f"header does not carry {fn.__name__}"
            assert isinstance(fn(), float) and not hasattr(fn(), "dtype"), (
                f"{fn.__name__} returns a numpy scalar; repr() of one is "
                "'np.float64(...)', which would emit an unparseable netlist token"
            )
        assert "STAYS OPEN" in nl, (
            "the header must record that the corpus's R1-vs-R2 flag is still open; "
            "R56 item 2 makes that non-optional"
        )


# ═════════════════════════════════════════════════════════════════════════════
class TestAntiTautology:
    """The exporter must not know the answer (prereg sec 5)."""

    def test_exporter_imports_no_band_structure_symbol(self):
        """AST-parsed, not grepped: a docstring may legitimately CITE the band
        leaf, but no ``import`` may reach a band-structure module or name."""
        src = open(X.__file__, encoding="utf-8").read()
        tree = ast.parse(src)
        banned_mod = ("srs_band_survey", "band_structure", "bands")
        banned_name = ("bands_at", "bloch_adjacency", "dense_scan", "OMEGA_LINK_OVER_C",
                       "srs_primitive_bcc", "direct_graph_laplacian_lambda_max")
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names:
                    assert not any(b in a.name for b in banned_mod), f"exporter imports {a.name}"
            elif isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                assert not any(b in mod for b in banned_mod), f"exporter imports from {mod}"
                for a in node.names:
                    assert a.name not in banned_name, f"exporter imports {a.name} from {mod}"

    def test_no_emitted_netlist_carries_a_reference_frequency(self):
        """The band top, the Gamma multiplet and omega_C must not appear as
        numbers anywhere in an emitted netlist. If the netlist knows the answer,
        the comparison is a checklist, not a gate."""
        td = X.bond_delay()
        forbidden = {
            "band top f": 1.0 / (2.0 * td),
            "gamma multiplet f": math.acos(-1.0 / 3.0) / (2.0 * math.pi * td),
            "omega_C as a frequency": OMEGA_C / (2.0 * math.pi),
        }
        edges = X.srs_primitive_cell_edges()
        nl = X.emit_tl_network(edges, 4, 0, _AC, title="anti-tautology fixture")
        numbers = [float(t) for t in re.findall(r"(?<![\w.])[-+]?\d+\.\d+e[-+]?\d+", nl)]
        for label, f in forbidden.items():
            for got in numbers:
                assert not math.isclose(got, f, rel_tol=1e-9), (
                    f"emitted netlist carries {label} ({f!r}) -- the exporter is "
                    "leaking a reference value into the object under test"
                )


# ═════════════════════════════════════════════════════════════════════════════
class TestSubstrateNativeEmission:
    """CP3 machine-enforced: the ratified T2(a) primitive, and NO lumped ladder.

    A one-section-per-bond L-C ladder IS the lumped graph-Laplacian model the
    corpus rejected for failing the frozen 1/sqrt(3) velocity gate. Emitting one
    would be the substrate-native leak in circuit clothing."""

    @pytest.mark.parametrize("builder", ["primitive", "srs2"])
    def test_srs_rungs_emit_only_t_elements(self, builder):
        if builder == "primitive":
            edges, n = X.srs_primitive_cell_edges(), 4
        else:
            net = build_srs_net(2)
            edges, n = X.edges_from_net(net), net.n_nodes
        nl = X.emit_tl_network(edges, n, 0, _AC, title="CP3 fixture")
        devices = [ln.split()[0] for ln in nl.splitlines()
                   if ln and not ln.startswith(("*", ".", "+")) and not ln.startswith("wrdata")
                   and not ln.startswith("ac ") and not ln.startswith("set ")]
        kinds = {d[0].upper() for d in devices}
        assert kinds <= {"T", "I"}, (
            f"srs rung emitted device kinds {sorted(kinds)}; only lossless T lines and the "
            "AC current-source drive are permitted. An L or C here is the rejected lumped model."
        )
        assert sum(1 for d in devices if d.upper().startswith("T")) == len(edges)

    def test_one_t_element_per_bond_on_the_engine_graph(self):
        net = build_srs_net(2)
        edges = X.edges_from_net(net)
        assert net.n_nodes == 64 and len(edges) == 96, (
            f"srs L=2 gave N={net.n_nodes}, B={len(edges)}; expected 8L^3=64 and 12L^3=96"
        )
        nl = X.emit_tl_network(edges, net.n_nodes, 0, _AC, title="fixture")
        assert len([ln for ln in nl.splitlines() if ln.startswith("T")]) == 96

    def test_every_t_card_carries_the_canonical_line_impedance(self):
        nl = _emit_bond()
        for ln in nl.splitlines():
            if ln.startswith("T"):
                assert float(_Z0_RE.search(ln).group(1)) == Z_0

    def test_lumped_lc_appears_only_on_the_l0_smoke_test(self):
        nl = X.emit_lc_tank(_AC, title="L0 fixture")
        body = [ln for ln in nl.splitlines() if ln and not ln.startswith(("*", "."))]
        assert any(ln.startswith("L0 ") for ln in body)
        assert any(ln.startswith("C0 ") for ln in body)
        assert not any(ln.startswith("T") for ln in body), "L0 must carry no TL element"
        assert "NO srs topology" in nl and "smoke test ONLY" in nl, (
            "L0's netlist must say in its own header that it is not a substrate test"
        )


# ═════════════════════════════════════════════════════════════════════════════
class TestGraphSource:
    """T3: the graph comes from the engine, and the wrong graph fails loudly."""

    def test_carrier_guard_rejects_the_z4_diamond_instrument(self):
        with pytest.raises(ValueError, match="carrier guard"):
            X.edges_from_net(build_diamond_net(4))

    def test_carrier_guard_accepts_srs(self):
        assert X.edges_from_net(build_srs_net(2))

    def test_srs_primitive_cell_wraps_to_the_k4_complete_graph(self):
        """3-regular on 4 vertices == K_4 complete. Asserted from the ENGINE's
        own motif symbols, not from a hand-typed edge list."""
        edges = X.srs_primitive_cell_edges()
        assert sorted(edges) == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

    def test_node_names_never_collide_with_ground(self):
        assert X.node_name(0) != X.GROUND


# ═════════════════════════════════════════════════════════════════════════════
class TestEmissionIntegrity:
    """CTRL-RT, the T6 native companion, and the planted-defect disclosure."""

    def test_every_emitted_number_round_trips_bit_exactly(self):
        """The one place a %g format could silently truncate a canonical constant."""
        for value in (Z_0, OMEGA_C, ANALYTIC_NETWORK_FACTOR, L_CELL, C_CELL, X.bond_delay()):
            assert float(X._fmt(value)) == value, f"{value!r} does not round-trip"
        nl = _emit_bond()
        for ln in nl.splitlines():
            if ln.startswith("T"):
                assert float(_TD_RE.search(ln).group(1)) == X.bond_delay()
                assert float(_Z0_RE.search(ln).group(1)) == Z_0

    def test_native_scaling_emits_unit_line_parameters(self):
        nl = _emit_bond(native=True)
        for ln in nl.splitlines():
            if ln.startswith("T"):
                assert float(_TD_RE.search(ln).group(1)) == 1.0
                assert float(_Z0_RE.search(ln).group(1)) == 1.0
        assert "UNITS SCALING: native" in nl

    def test_planted_defect_is_disclosed_in_the_header_and_applied_once(self):
        edges = X.srs_primitive_cell_edges()
        nl = X.emit_tl_network(edges, 4, 0, _AC, title="positive control",
                               perturb_bond=(2, 1.05))
        assert "PLANTED DEFECT" in nl and "DELIBERATELY WRONG" in nl
        tds = _emitted_tds(nl)
        clean = X.bond_delay()
        assert sum(1 for t in tds if t != clean) == 1, "exactly one bond must be perturbed"
        assert math.isclose(max(tds) / clean, 1.05, rel_tol=1e-12)

    def test_header_echoes_every_imported_symbol(self):
        """SCX-REQ-ELEMENTS.2 -- the hand-audit must be mechanical."""
        nl = _emit_bond()
        for sym in ("Z_0", "OMEGA_C", "ANALYTIC_NETWORK_FACTOR", "L_CELL", "C_CELL"):
            assert sym in nl, f"netlist header does not echo {sym}"
        assert "CANONICAL SOURCE:" in nl

    def test_sector_declaration_travels_on_every_netlist(self):
        for nl in (_emit_bond(), X.emit_lc_tank(_AC, title="t"),
                   X.emit_two_junction(_AC, title="t")):
            assert "REGIME I cold sub-yield lossless-reactive" in nl
            assert "CHANNEL scalar-translational ONLY" in nl
            assert "IMPLEMENTATION-VERIFICATION" in nl

    def test_two_junction_declares_its_resistors_as_ports(self):
        nl = X.emit_two_junction(_AC, title="AUX-B")
        assert "PORTS" in nl and "NOT" in nl
        assert len([ln for ln in nl.splitlines() if ln.startswith("R")]) == 2
        for ln in nl.splitlines():
            if ln.startswith("R"):
                assert float(ln.split()[-1]) == Z_0 / 2.0
