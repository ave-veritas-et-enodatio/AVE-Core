# CODE-PROVENANCE INDEX (prototype)

Systematic infrastructure to track the **code/implementation behind a claim**
the same way `manuscript/ave-kb/.index/claims.jsonl` tracks the **claim text**.

## Why this exists

Claims are tracked; the code that *computes* a claim's number was not. So tier
distinctions that matter for honest framing — *is this quantity solver-forward
or a matched closed form? is it gated? does it have a dead input? is the
"radius" actually dimensionless?* — were discovered only by **manual audit**,
never recorded. Two audited quantities can read identically in the manuscript
while one is a forward eigenvalue and the other is a constant fit to PDG inside
a `±2%` band. This index makes that distinction a tracked, drift-gated record.

It is the code-side mirror of the KB claim spine:

| KB claim spine | Code-provenance index |
| --- | --- |
| `manuscript/ave-kb/.index/claims.jsonl` | `src/scripts/verify/code_provenance.jsonl` |
| `manuscript/ave-kb/tools/verify-kb-metadata.py` | `src/scripts/verify/verify_code_provenance.py` |
| one record per **claim** | one record per **load-bearing computed quantity** |

## Status: 6-seed PROTOTYPE — NOT "all code tracked"

This registry currently holds **6 quantities** seeded from one audit session
(`m_p/m_e`, `m_Delta/m_e`, `m_mu/m_e`, `m_tau/m_e`, `m_n`, `r_opt`). It is a
proof-of-mechanism, not a complete map of the engine. It is grown **per-check**:
the next quantity gets a record when it next gets audited — not by a bulk sweep
that would re-introduce the trust-without-verification failure this index exists
to prevent.

## Record schema (one JSON object per line)

```json
{
  "clm":         ["clm-xxxxxx", ...],   // cross-link to claims.jsonl (may be empty/multi)
  "quantity":    "m_p/m_e",             // the computed quantity
  "impl":        "path.py:symbol -> path.py:symbol ; literal=path.py:SYMBOL",
  "provenance":  "solver-forward | matched-closed-form | empirical-input | geometric-constant",
  "solver":      true,                   // is a numerical solver actually invoked?
  "ci_gate":     "path::Test::func[param]" or null,  // null => UNGATED
  "inputs":      ["8pi (KAPPA_FS_COLD constants.py:687)", ...],
  "dead_inputs": ["node_pitch (faddeev_skyrme.py:87 ... never read)"],
  "dim_type":    "ratio | mass | length | dimensionless | energy | frequency | angle",
  "magnitude":   "forward-miss / agreement, with the literal vs PDG",
  "flags":       ["mislabels, conventions, residual-counts, pending audits"]
}
```

### `provenance` taxonomy

- **solver-forward** — a numerical solver is invoked and its output *is* the
  quantity (e.g. baryon masses via `solve_scalar_trace`). `solver: true`.
- **matched-closed-form** — a module-scope algebraic constant fit to a target;
  no solver runs (e.g. `M_MU`, `M_TAU`). `solver: false`.
- **empirical-input** — a CODATA/PDG anchor inserted, not derived (e.g. `m_n`).
- **geometric-constant** — fixed by geometry/axiom, not solved (e.g. `r_opt`).

## How the two skills POPULATE a record

A record is **not** authored free-hand. Each field comes from a named skill so
the provenance of the *provenance record itself* is auditable:

- **`live-fire-derivation-provenance`** → `provenance`, `solver`, `ci_gate`,
  `dead_inputs`, `magnitude`. This skill runs the derivation live (not by
  reading the docstring), watches which inputs actually move the output, greps
  for the CI gate, and records the forward-miss against the experimental anchor.
  Dead inputs (assigned-but-never-read parameters such as `node_pitch`) surface
  here.
- **`dimensional-provenance-check`** → `dim_type`. This catches the
  "`r_opt` is a radius" trap: `r_opt` carries `dim_type: dimensionless`
  (lattice-node counts `ell_node`), **not** length. Phase-space-vs-real-space
  coordinate discipline (A46) lives in this field.

`clm`, `quantity`, `impl`, and `inputs` are filled from the verify-before-cite
grep that the audit already performs.

## How the verifier MAINTAINS it (drift-gate)

`verify_code_provenance.py` is read-only and runs five checks per record:

1. **impl-exists** — every `*.py` path named in `impl` exists on disk.
   Missing → **hard fail (exit 1)**. This is the drift-gate: if a refactor
   moves or deletes the implementing file, CI breaks until the record is
   re-pointed.
2. **symbol-present** — every `path.py:symbol` token greps to an occurrence in
   that file. Not found → WARN (locals like `r_opt_max` and dict keys are
   legitimately non-greppable in the prototype).
3. **ci-gate-or-flag-UNGATED** — `ci_gate: null` prints an `UNGATED` warning;
   otherwise the named test file + function must be locatable.
4. **dim-consistency** — `dim_type` present and in the known set.
5. **canonical cross-check** (`ave-canonical-source`) — imports the cited
   literals `from ave.core.constants import ...` (and `cosserat`) and echoes
   them, so the registry's quoted values are confirmed against the live module
   on every run, never against a stale copy.

UNGATED, symbol-not-greppable, and ci-not-located are **warnings, not
failures**, for the prototype: they are signal to be surfaced, not gates to
block on. Only impl-missing / malformed-JSON / missing-dim trip exit 1.

### Run it

```bash
make verify                 # (once wired into the Makefile target)
PYTHONPATH=src ./.venv/bin/python src/scripts/verify/verify_code_provenance.py
```

## Seed-vs-code corrections already captured

Recording these is the point — the seed was an audit hypothesis, the registry
holds the verified truth, and the deltas are flagged not silently fixed
(flag-don't-fix):

- **Leptons are GATED, not UNGATED.** The seed marked `m_mu`/`m_tau` as
  `ci=NULL`. They are gated by `test_cosserat.py::TestMuonMass::test_vs_pdg`
  and `::TestTauMass::test_vs_pdg` (+ a duplicate-formula gate
  `test_framework_25_derived.py::test_m_tau`). The gates are loose `±2%`
  bands that do **not** flag the existing sub-2% forward-miss — recorded as a
  flag, not erased.
- **`m_tau` input label `8pi/p_c` is wrong.** Code is `M_E*P_C/ALPHA**2 =
  8pi/alpha`.
- **`m_n` "Dm=1.293 inserted" is imprecise.** No literal `1.293` exists in
  `src/ave/`; the split is the difference of two CODATA anchors
  (`M_N_MEV_TARGET - M_P_MEV_CODATA`). Two engine conventions coexist
  (`m_n ≈ m_p` in `condensed_matter.py`; CODATA anchor in
  `coupled_resonator.py`).
- **`m_p`/`m_Delta` impl path correction.** The compute function lives in
  `_constants_compute.py:_compute_baryon_ladder`, not in `constants.py`
  (which holds only the `BARYON_LADDER` literal + formula comment).

## Growing the index

When the next load-bearing quantity is audited: run the two skills, append one
JSONL line, run the verifier, commit. Do **not** bulk-populate from docstrings —
that would assert tracking without the live-fire + dimensional + grep evidence
the schema demands.
