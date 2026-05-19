# Mini-KB Claim Quality

<!-- path-stable: synthetic fixture register — root scope -->

> **Canonicality preamble.** This is a hand-built synthetic register used only as input for `kb_index_lib` function tests. It is not a real KB and is not refreshable.

## Quality Convention (per-entry assessment format)

Each claim entry carries a `### Quality` section. The format of a Quality section:

```markdown
## Some Entry Title
<!-- id: clm-xxxxxx -->

### Quality
- confidence: 0.X
- depends-on:
  - <id> — Other Entry Title (solidity 0.X)
- solidity: 0.X (build-status phrase) [= <confidence> × <min-dep-solidity>]
- rationale: one-sentence statement of why
- strengthen-by:
  - [specific work that would raise confidence]
```

The fenced `<!-- id: clm-xxxxxx -->` marker above sits inside a code fence and must NOT be counted as a real claim entry.

---

## Foundation Claim A — No Dependencies
<!-- id: clm-aa1111 -->

A leaf-level claim with no entry-level dependencies. Its solidity equals its
confidence. The on-disk `- solidity:` line below is deliberately stale (it
reads 0.10, not the computed 0.90) so a test can prove records take solidity
from `compute_solidity`, not from the parsed line.

### Quality
- confidence: 0.90
- solidity: 0.10 (refuted, do not use)
- rationale: synthetic no-dependency anchor claim.
- strengthen-by:
  - Run an independent derivation to confirm the anchor value.

---

## Foundation Claim B — Input-Only Band
<!-- id: clm-bb2222 -->

A second no-dependency claim, deliberately at a lower confidence so it lands
in the input-only build band.

### Quality
- confidence: 0.60
- solidity: 0.60 (use as input only, don't build deeper)
- rationale: synthetic mid-band no-dependency claim.
- strengthen-by:
  - Tighten the bounding argument so confidence can rise above the input-only band.

---

## Single-Dependency Claim C
<!-- id: clm-cc3333 -->

A claim with exactly one claim-target dependency. Its solidity is
confidence × the dependency's solidity.

### Quality
- confidence: 0.80
- depends-on:
  - clm-aa1111 — Foundation Claim A (solidity 0.90) [builds directly on the anchor claim]
- solidity: 0.72 (ok to build on, see caveats) [= 0.80 × 0.90]
- rationale: synthetic single-dependency claim.
- strengthen-by:
  - Close the open step so the dependency on clm-aa1111 can be discharged.

---

## Multi-Dependency Claim D
<!-- id: clm-dd4444 -->

A claim with two claim-target dependencies. Its solidity is
confidence × min(dependency solidities) — the weakest link governs.

### Quality
- confidence: 0.90
- depends-on:
  - clm-aa1111 — Foundation Claim A (solidity 0.90)
  - clm-bb2222 — Foundation Claim B (solidity 0.60)
- solidity: 0.54 (use as input only, don't build deeper) [= 0.90 × 0.60]
- rationale: synthetic multi-dependency claim; min() over two claim deps.
- strengthen-by:
  - Strengthen both clm-aa1111 and clm-bb2222 so the min() over the dependency set rises.
  - Add an independent cross-check of the combined result.

---

## Framework-Dependency Claim E
<!-- id: clm-ee5555 -->

A claim whose only dependencies are framework nodes (an invariant and an
axiom). Framework deps contribute solidity 1.0, so solidity equals confidence.

### Quality
- confidence: 0.75
- depends-on:
  - INVARIANT-S2 (axiom-numbering scaffold — used for the labelling convention)
  - Axiom 4 (saturation kernel — framework input to the bound)
- solidity: 0.75 (ok to build on, see caveats) [= 0.75 × 1.00]
- rationale: synthetic framework-only-dependency claim; solidity == confidence.
- strengthen-by:
  - Derive the bound end-to-end so confidence can move toward the ok-to-build band.
