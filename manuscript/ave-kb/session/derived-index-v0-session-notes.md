# KB Derived Index v0 — Overnight Session Notes

**Session:** 2026-05-15 (overnight, autonomous).
**Scope:** implement the four-step bundle from `kb-improvements.md` §2 — schema, build pipeline, runtime query module, freshness verifier.
**Status:** all four phases complete; 77 tests passing end-to-end; pipeline working through existing `make` targets. **Nothing committed.** Files are on the working tree awaiting review.

---

## What was built

### 1. Schema spec (design artifact)
- `manuscript/ave-kb/.index/SCHEMA.md` — authoritative spec for the 5 JSONL files, build invariants, query semantics, CLI surface, open questions, v0/v0.1 boundary.

### 2. Foundation library (build-side)
- `manuscript/ave-kb/tools/kb_index_lib.py` (~880 LoC after Phase 1b fix + small refactor) — pure-function library: parsers (frontmatter, claim-quality, leaf, index), dataclasses (ClaimEntry, DependsOnEdge, StrengthenByItem, LeafRecord, IndexRecord, KbState), record builders (one per file), serialization (`serialize_records`, `write_jsonl`, `read_jsonl`). Stdlib only.
- `manuscript/ave-kb/tools/tests/test_kb_index_lib.py` (~430 LoC) — 40 unittest cases against the real KB.

### 3. Build pipeline (refresh extension)
- `manuscript/ave-kb/tools/refresh-kb-metadata.py` — extended to also emit `.index/*.jsonl` after the existing frontmatter refresh. Skip-write on byte-identical content (preserves mtime, no spurious `git status` noise). Idempotent.
- `.index` added to `EXCLUDE_DIRS` in all three tooling scripts.
- `manuscript/ave-kb/tools/tests/test_refresh_index.py` (~230 LoC) — 6 unittest cases covering emission, idempotence, record counts, JSONL well-formedness, referential integrity, sort order.

### 4. Runtime query module (consume-side)
- `src/ave/kb/__init__.py` (~35 LoC) — package init, re-exports.
- `src/ave/kb/index.py` (~425 LoC) — `Index` class with all query methods, frozen-slot dataclasses, auto-resolved default path, in-memory inverse indices.
- `src/ave/kb/cli.py` (~245 LoC) — argparse CLI with `deps`, `gated-on`, `cited-by`, `solidity-below`, `subtree`, `show`, `stats` subcommands. `--json` flag and `--index-dir` override on every subcommand.
- `src/ave/kb/__main__.py` (~10 LoC) — for `python -m ave.kb ...`.
- `src/tests/kb/test_index.py` (~245 LoC) — 25 unittest cases (queries + CLI smoke + JSON round-trip).
- `src/tests/kb/__init__.py` — empty.

### 5. Freshness verifier (check extension)
- `manuscript/ave-kb/tools/check-claim-quality.py` — extended with three new checks (well-formedness, freshness diff against canonical state, referential integrity). Added `--index-dir` flag. Adds an `[index] ...` summary line to the output.
- `manuscript/ave-kb/tools/tests/test_check_index.py` (~205 LoC) — 6 unittest cases (passes on fresh state; detects stale, missing, malformed, referential-integrity violations; existing-checks regression smoke test).

---

## Final state on disk

```
manuscript/ave-kb/.index/
  SCHEMA.md              15,603 bytes — design doc
  claims.jsonl          109,557 bytes / 199 lines
  depends-on.jsonl        4,391 bytes /  33 lines
  strengthen-by.jsonl    44,541 bytes / 259 lines
  cites.jsonl            91,620 bytes / 621 lines
  subtree-aggregates.jsonl 20,847 bytes / 111 lines
```

`git status` shows:
- **Modified:** `tools/check-claim-quality.py`, `tools/refresh-kb-metadata.py` (extensions only — preserved all existing behavior).
- **Untracked:** `tools/kb_index_lib.py`, `tools/tests/`, `.index/`, `src/ave/kb/`, `src/tests/kb/`.

---

## Tests

```
$ cd /Users/benn/projects/AVE-Umbrella/AVE-Core/manuscript/ave-kb/tools
$ python -m unittest tests.test_kb_index_lib tests.test_refresh_index tests.test_check_index
Ran 52 tests in 3.035s — OK

$ cd /Users/benn/projects/AVE-Umbrella/AVE-Core
$ PYTHONPATH=src python -m unittest tests.kb.test_index
Ran 25 tests in 0.312s — OK

Total: 77 tests passing.
```

---

## End-to-end pipeline (existing `make` targets work unchanged)

```
$ make refresh-kb-metadata
... (stderr: ~200 diagnostic lines about dropped non-claim id matches — see "Real KB findings" below)
[refresh] Updated 0 subtree-claims field(s).
[refresh-index] Wrote 0 file(s) under manuscript/ave-kb/.index/ (5 unchanged).

$ make verify-claim-quality
[claim-quality] Scanned 657 files (657 with frontmatter, 546 leaves, 521 with claims, 25 no-claim, 77 multi-claim) and 199 canonical entries.
[index] 5 JSONL files (199 claims, 33 depends-on, 259 strengthen-by, 621 citations, 111 aggregates).
[claim-quality] PASS.

$ PYTHONPATH=src python -m ave.kb stats
claims: 199
depends_on_edges: 33
strengthen_by_items: 259
citation_edges: 621
subtree_aggregates: 111
```

Performance: 3.45 ms cold load of the runtime module; all 9 query methods combined run in 0.017 ms.

---

## Real KB findings surfaced during implementation (NOT fixed)

These are pre-existing properties of the KB that the new tooling has illuminated. None were fixed; all are flagged for review.

### Finding 1: 199 canonical entries, not 200

`grep -c '<!-- id: '` over all `claim-quality.md` files returns 200, but one of those is the example placeholder inside a fenced ` ```markdown ` block in the root `claim-quality.md`'s "Quality Convention" preamble. The existing `check-claim-quality.py` already strips code fences before counting (it reports 199); the new tooling matches that.

**Action taken:** SCHEMA.md §"Test coverage definition of done" updated to specify "code-fence-scrubbed count" and the concrete value 199.

### Finding 2: 3 spurious depends-on edges in claim-quality registers (pre-Phase-1b)

Real claim-quality entries reference INVARIANTs in their `depends-on:` bullets, e.g.:

```
- INVARIANT-S2 / Axiom 4 (saturation kernel — for the running-coupling sketch)
- INVARIANT-C1 ($V_{yield} \approx 43.65$ kV — referenced in the catalogue's key-parameter column)
```

The naive 6-char-id regex `\b([a-z0-9]{6})\b` matched incidental words `kernel` and `approx` on those lines, producing 3 orphan edges.

**Action taken (Phase 1b):** library now does two-pass parsing — collects the set of known canonical claim IDs first, then filters depends-on targets to known IDs only. Diagnostic emitted to stderr per dropped match. `depends-on.jsonl` is now 33 records, not 36.

**Open question for you:** these INVARIANT-targeting `depends-on` bullets are real semantic claims (the author intends to express "this claim depends on INVARIANT-X"). The v0 schema is claim-to-claim only; INVARIANT dependencies are silently dropped (with diagnostic). If they're worth tracking explicitly, a v0.1 addition could be `depends-on-invariant.jsonl` or a typed-target extension to `depends-on.jsonl`.

### Finding 3: ~196 false-positive strengthen-by mentions filtered

The same 6-char regex matched 6-letter English / physics words on strengthen-by bullets — `unknot`, `lepton`, `sector`, `proton`, `vacuum`, `regime`, `factor`, `chiral`, `master`, `either`, `rather`, `approx`, `kernel`, etc. The Phase 1b fix filters these out the same way.

**Diagnostic noise:** running `make refresh-kb-metadata` now emits ~200 stderr lines listing the filtered matches. This is informative but noisy. Worth deciding whether to:
- Keep as-is (informative, no further action needed)
- Suppress by default; surface only via a `--verbose` flag
- Aggregate into a count summary at the end (e.g., "filtered 196 non-claim mentions")

The diagnostics don't affect exit code or the JSONL output; they're informational only.

### Finding 4: 6-char claim ID format is lexically ambiguous with English

This is the structural cause of Findings 2 and 3. The claim-quality framework chose `[a-z0-9]{6}` for compactness, but ~200 6-letter English/physics words exist in the corpus. The two-pass-filter approach handles it cleanly at parse time, but a more distinctive ID format (e.g., `cq:` prefix or a hyphenated form like `cq-xqz3p9`) would have made parsing fully syntactic.

**Worth noting:** this is a real lesson for Personant's symbol-anchor extractor. The 6-char claim-ID lexical collision with English is exactly the kind of failure mode the Personant identifier scheme should avoid.

---

## Design decisions surfaced for review

These are calls I made where the SCHEMA.md spec was ambiguous or silent. They're all reversible; flagged here so you can override if any seem wrong.

### A. Diagnostic stream default

`kb_index_lib.discover_kb` accepts a `diagnostic_stream` kwarg. Default is `sys.stderr` (so production refresh emits diagnostics by default). Pass `None` to silence; pass a `StringIO` for tests. The verifier passes `None` — diagnostics are signal for refresh, not for verify.

### B. Build-band for null solidity

Some claim entries have malformed/missing solidity. SCHEMA.md doesn't specify the band for those. Library emits `"unknown"`. Currently no entries trigger this (all 199 parse cleanly), but the behavior is defensive.

### C. CLI subcommand JSON output schemas

| Command | JSON shape |
|---|---|
| `deps`, `gated-on`, `subtree` | array of strings (claim ids) |
| `cited-by` | array of full CitationEdge objects (not just leaf paths — preserves `tier2_marked` flag) |
| `solidity-below`, `in-band` | array of full Claim objects |
| `show` | single Claim object |
| `stats` | object (dict of counts) |

The "full record for typed-list commands" choice was the agent's call. Alternative: bare arrays of ids, leaving users to call `show` to get details. Current choice gives shell users richer pipeable data; the cost is larger output for `solidity-below`.

### D. `solidity_below` excludes null-solidity claims

Claims with `solidity: null` are excluded from `solidity_below(threshold)` regardless of threshold. Treating `None < threshold` as True felt semantically wrong for a build-readiness filter ("all malformed entries are below every threshold"). Documented in the docstring.

### E. Subtree path normalization

`idx.subtree_claims(...)` accepts:
- `""` or `"."` → entry-point aggregate (all 199 IDs)
- `"vol1"` or `"vol1/"` → falls back to `"vol1/index.md"` lookup
- `"vol1/index.md"` → exact lookup
- Unknown paths → empty list (no exception)

### F. Test location for runtime module

`src/tests/kb/` is the first test subpackage in this repo (existing tests are flat under `src/tests/`). Tests are stdlib `unittest`, runnable via `PYTHONPATH=src python -m unittest tests.kb.test_index`. They also work under pytest if anyone runs the full repo suite. The new subdir + `__init__.py` is a minor convention divergence; happy to flatten if you prefer.

### G. Refactor extracted `serialize_records` from `write_jsonl`

Phase 4 needed byte-level comparison against canonical state. The cleanest path was extracting a pure `serialize_records(records) -> bytes` function from `write_jsonl`. Phase 1 tests still pass; this is a no-op refactor.

---

## Open questions / things to discuss when you're back

1. **Diagnostic noise from refresh.** ~200 stderr lines listing filtered non-claim word matches. Keep, suppress, or aggregate?
2. **INVARIANT-targeting depends-on bullets.** Silently filtered out of `depends-on.jsonl`. Worth a `depends-on-invariant.jsonl` in v0.1, or just live with the schema-mismatch?
3. **Tracking `.index/*.jsonl` in git.** Per SCHEMA.md and §kb-improvements.md §2, these SHOULD be tracked (the whole point is free history). The files exist but are untracked. Adding to git is one `git add manuscript/ave-kb/.index/` away.
4. **Make targets to add?** Possible new targets:
   - `make ave-kb-stats` — quick `ave-kb stats` invocation
   - `make verify` — meta-target running `verify-claim-quality` + the unittest suite
   - `make refresh` — alias for `refresh-kb-metadata`
   None are required; existing targets work.
5. **Documentation surface.** SCHEMA.md is reasonably complete. Worth a short note in `manuscript/ave-kb/CLAUDE.md` pointing at the `.index/` directory and the `ave.kb.index` query API? Or a README in `src/ave/kb/`?
6. **Frontmatter on SCHEMA.md.** Currently SCHEMA.md has no kb-frontmatter block. It's in `.index/` which is in EXCLUDE_DIRS, so the verifier doesn't flag it. Fine to leave, or add a `kind: leaf-as-index`/`no-claim:` frontmatter for symmetry.
7. **CLI installation.** Currently invoked as `PYTHONPATH=src python -m ave.kb ...`. A real `ave-kb` shell entry-point would need either a setup.py entry-point or a small wrapper script in `bin/`. Defer until packaging matters.

---

## What's explicitly NOT in this v0

Carried from SCHEMA.md §"v0 → v0.1 candidate refinements":

- Embeddings / full-text search
- Synonym resolution (any two surface forms referring to the same claim are encoded by id only)
- Solidity recomputation drift check (`solidity = confidence × min(dep_solidity)` is recorded as written, not verified)
- Cross-claim consistency checks (e.g., the `trf3bd`/`unk0bd` mutual-exclusion is informal prose)
- Pre-commit hook installation (the freshness verifier exists; wiring to git hooks is a separate decision)
- INVARIANT-targeting depends-on (Finding 2 above)

---

## How to verify everything works

From a fresh terminal:

```bash
cd /Users/benn/projects/AVE-Umbrella/AVE-Core

# Build pipeline
make refresh-kb-metadata        # emits .index/*.jsonl
make verify-claim-quality       # validates everything

# Tests
cd manuscript/ave-kb/tools
python -m unittest tests.test_kb_index_lib tests.test_refresh_index tests.test_check_index
cd /Users/benn/projects/AVE-Umbrella/AVE-Core
PYTHONPATH=src python -m unittest tests.kb.test_index

# Runtime CLI
PYTHONPATH=src python -m ave.kb stats
PYTHONPATH=src python -m ave.kb show 0ktpcn
PYTHONPATH=src python -m ave.kb deps 5xon03                  # → unk0bd
PYTHONPATH=src python -m ave.kb deps -i unk0bd               # → 5xon03
PYTHONPATH=src python -m ave.kb solidity-below 0.4
PYTHONPATH=src python -m ave.kb solidity-below 0.5 --json | jq '.[].id'
PYTHONPATH=src python -m ave.kb gated-on unk0bd              # → 5xon03 (strengthen-by mentions it)
PYTHONPATH=src python -m ave.kb cited-by trf3bd
PYTHONPATH=src python -m ave.kb subtree vol1
PYTHONPATH=src python -m ave.kb subtree ""                   # entry-point: all 199
```

---

## If you want to roll back

Two modified files restore via `git checkout --`:

```bash
git checkout -- manuscript/ave-kb/tools/check-claim-quality.py
git checkout -- manuscript/ave-kb/tools/refresh-kb-metadata.py
```

Untracked additions can be removed with `git clean` (review first):

```bash
git clean -nfd manuscript/ave-kb/.index/ manuscript/ave-kb/tools/{kb_index_lib.py,tests/} src/ave/kb/ src/tests/kb/
# Drop -n when ready to actually delete.
```

But there's nothing to roll back unless you don't want this — pipeline is clean, idempotent, well-tested, and the existing make targets continue to work as before plus the new index emission/verification.
