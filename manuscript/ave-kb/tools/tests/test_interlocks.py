"""Unit tests for the `ilk-` interlock spine (INVARIANT-S13).

Covers the interlock-register parser (`parse_interlock_entries`), the
`node_type: interlock-mechanism` materialization + the `interlocks` edge
emission (hub-node encoding), the malformed-entry drift-gate
(`InterlockEntryError`), and the two derived quantities the relation drives —
`compute_independent_parameter_count` (the chord/echo rule: fitted = no drop,
real = −1) and `falsification_net_violations` (a refuted channel flags the
operating-point root). Fully self-contained: synthetic register + synthetic
record dicts; nothing here reads `manuscript/ave-kb/` proper. The live
register's health is covered by `make verify-kb-metadata`.

Run via the `test-tools` make target (sets `PYTHONPATH=manuscript/ave-kb/tools`).
"""

import tempfile
import unittest
from pathlib import Path

# kb_index_lib resolves via PYTHONPATH (set by the test-tools make target).
import kb_index_lib as lib  # noqa: E402


_REGISTER = """[↑ Parent](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "register"
-->

<!-- interlock-meta
operating-point-root: clm-iouqn9
expected-independent-count: 143
-->

# Interlock Register

## Per-node field legend

Each `## <title>` heading carries a `<!-- id: ilk-xxxxxx -->` marker (this inline
placeholder must never parse as an entry).

---

## R·r = 1/4 (Golden-Torus screening)
<!-- id: ilk-rr14gt -->

- **mechanism:** R·r = 1/4 — phasor area equals the Nyquist cell area at
  Axiom-4 saturation onset.
- **real-or-fitted:** fitted-identification
- **status:** proposed
- **interlocks:** clm-iouqn9, clm-0ktpcn
- **derived-endpoint:** clm-0ktpcn
- **canonical-leaf:** `vol1/ch8-alpha-golden-torus.md:11,44-46`
- **grounding:** GROUNDED FITTED per ch8:11.

---

## R − r = 1/2 (crossings)
<!-- id: ilk-rmrhlf -->

- **mechanism:** R − r = 1/2 — self-avoidance at crossings.
- **real-or-fitted:** real-geometric-constraint
- **status:** proposed
- **interlocks:** (none — catalogued)
- **derived-endpoint:** (none)
- **canonical-leaf:** `vol1/ch8-alpha-golden-torus.md:45`
- **grounding:** real per ch8:45.
"""


def _write(tmp: Path, body: str) -> Path:
    kb = tmp / "kb"
    (kb / "common").mkdir(parents=True, exist_ok=True)
    reg = kb / "common" / lib.INTERLOCK_REGISTER_NAME
    reg.write_text(body, encoding="utf-8")
    return kb


class TestInterlockParser(unittest.TestCase):
    def test_parses_entries_and_skips_placeholder(self):
        with tempfile.TemporaryDirectory() as td:
            kb = _write(Path(td), _REGISTER)
            nodes = lib.parse_interlock_entries(
                kb / "common" / lib.INTERLOCK_REGISTER_NAME, kb
            )
        by_id = {n.id: n for n in nodes}
        # The inline `ilk-xxxxxx` legend placeholder must NOT parse.
        self.assertEqual(set(by_id), {"ilk-rr14gt", "ilk-rmrhlf"})
        rr = by_id["ilk-rr14gt"]
        self.assertEqual(rr.real_or_fitted, "fitted-identification")
        self.assertEqual(rr.status, "proposed")
        self.assertEqual(rr.derived_endpoint, "clm-0ktpcn")
        self.assertEqual(rr.interlocked, ("clm-iouqn9", "clm-0ktpcn"))
        self.assertEqual(rr.cited_leaf, "vol1/ch8-alpha-golden-torus.md:11,44-46")
        self.assertEqual(rr.canonical_path, "common/interlock-register.md")
        # A catalogued-but-unwired mechanism: empty interlocked, null endpoint.
        rmr = by_id["ilk-rmrhlf"]
        self.assertEqual(rmr.real_or_fitted, "real-geometric-constraint")
        self.assertEqual(rmr.interlocked, ())
        self.assertIsNone(rmr.derived_endpoint)

    def test_malformed_entries_raise(self):
        bad_cases = [
            # invalid real-or-fitted tag
            _REGISTER.replace("fitted-identification", "maybe-real"),
            # invalid status
            _REGISTER.replace("**status:** proposed", "**status:** SOLIDIFIED", 1),
            # missing required field (drop mechanism on first entry)
            _REGISTER.replace(
                "- **mechanism:** R·r = 1/4 — phasor area equals the Nyquist "
                "cell area at\n  Axiom-4 saturation onset.\n",
                "",
                1,
            ),
        ]
        for body in bad_cases:
            with tempfile.TemporaryDirectory() as td:
                kb = _write(Path(td), body)
                with self.assertRaises(lib.InterlockEntryError):
                    lib.parse_interlock_entries(
                        kb / "common" / lib.INTERLOCK_REGISTER_NAME, kb
                    )


class TestInterlockEmission(unittest.TestCase):
    def _state(self):
        node = lib.InterlockMechanismNode(
            id="ilk-rr14gt",
            title="R·r = 1/4",
            mechanism="R·r = 1/4",
            real_or_fitted="fitted-identification",
            status="proposed",
            derived_endpoint="clm-0ktpcn",
            canonical_path="common/interlock-register.md",
            canonical_anchor="rr-14",
            cited_leaf="vol1/ch8-alpha-golden-torus.md:11",
            interlocked=("clm-iouqn9", "clm-0ktpcn"),
        )
        return lib.KbState(
            claim_entries=(),
            leaves=(),
            indexes=(),
            framework_nodes=(),
            experiments=(),
            interlock_mechanisms=(node,),
        )

    def test_node_record_shape(self):
        recs = lib.build_claims_records(self._state())
        ilk = [r for r in recs if r["node_type"] == "interlock-mechanism"]
        self.assertEqual(len(ilk), 1)
        self.assertEqual(
            list(ilk[0]),
            ["node_type", "id", "title", "mechanism", "real_or_fitted",
             "status", "derived_endpoint", "canonical_path",
             "canonical_anchor", "cited_leaf"],
        )

    def test_interlocks_edges_hub_encoding(self):
        edges = lib.build_depends_on_records(self._state())
        ilk_edges = [e for e in edges if e["relation"] == "interlocks"]
        # One edge per interlocked constant, all sharing the mechanism hub.
        self.assertEqual(len(ilk_edges), 2)
        self.assertEqual({e["target"] for e in ilk_edges}, {"ilk-rr14gt"})
        self.assertEqual(
            {e["source"] for e in ilk_edges}, {"clm-iouqn9", "clm-0ktpcn"}
        )
        for e in ilk_edges:
            self.assertEqual(e["target_kind"], "interlock-mechanism")
            self.assertIsNone(e["strength"])
            self.assertIsNone(e["fraction"])
            self.assertEqual(e["context"], "fitted-identification")
            self.assertEqual(list(e), [
                "source", "target", "relation", "target_kind",
                "target_solidity_recorded", "strength", "context", "fraction",
            ])


def _claim(cid, band):
    return {"node_type": "claim", "id": cid, "build_band": band}


def _mech(mid, tag, de):
    return {"node_type": "interlock-mechanism", "id": mid,
            "real_or_fitted": tag, "derived_endpoint": de}


def _edge(src, tgt):
    return {"source": src, "target": tgt, "relation": "interlocks"}


class TestDerivedQuantities(unittest.TestCase):
    def test_fitted_does_not_reduce_count(self):
        claims = [_claim("clm-a", "input-only"), _claim("clm-b", "input-only"),
                  _mech("ilk-x", "fitted-identification", "clm-b")]
        deps = [_edge("clm-a", "ilk-x"), _edge("clm-b", "ilk-x")]
        self.assertEqual(
            lib.compute_independent_parameter_count(claims, deps), 2
        )

    def test_real_wired_reduces_count(self):
        claims = [_claim("clm-a", "input-only"), _claim("clm-b", "input-only"),
                  _mech("ilk-x", "real-geometric-constraint", "clm-b")]
        deps = [_edge("clm-a", "ilk-x"), _edge("clm-b", "ilk-x")]
        self.assertEqual(
            lib.compute_independent_parameter_count(claims, deps), 1
        )

    def test_real_but_unwired_does_not_reduce(self):
        # A real mechanism with no interlocks edges (catalogued) removes nothing.
        claims = [_claim("clm-a", "input-only"), _claim("clm-b", "input-only"),
                  _mech("ilk-x", "real-geometric-constraint", "clm-b")]
        self.assertEqual(
            lib.compute_independent_parameter_count(claims, []), 2
        )

    def test_channels_exclude_root(self):
        deps = [_edge("clm-iouqn9", "ilk-x"), _edge("clm-0ktpcn", "ilk-x")]
        self.assertEqual(
            lib.interlock_channels(deps, "clm-iouqn9"), {"clm-0ktpcn"}
        )

    def test_falsification_net_fires_on_refuted_channel(self):
        deps = [_edge("clm-iouqn9", "ilk-x"), _edge("clm-0ktpcn", "ilk-x")]
        clean = [_claim("clm-iouqn9", "input-only"),
                 _claim("clm-0ktpcn", "input-only")]
        self.assertEqual(
            lib.falsification_net_violations(clean, deps, "clm-iouqn9"), []
        )
        refuted = [_claim("clm-iouqn9", "input-only"),
                   _claim("clm-0ktpcn", "refuted")]
        self.assertEqual(
            lib.falsification_net_violations(refuted, deps, "clm-iouqn9"),
            [("clm-0ktpcn", "clm-iouqn9")],
        )


if __name__ == "__main__":
    unittest.main()
