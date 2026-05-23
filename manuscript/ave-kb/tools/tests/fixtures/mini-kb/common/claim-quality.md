# Mini-KB Common Claim Quality

<!-- path-stable: synthetic fixture register — common scope -->

> **Canonicality preamble.** Common-scope synthetic register. Holds the
> pending claim, the claim poisoned by a pending dependency, and the
> double-framework-edge claim.

---

## Pending Upstream Claim F
<!-- id: clm-ff6666 -->

A claim that has not yet been quality-assessed. Its confidence is `*pending*`,
so its solidity is `*pending*` too.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - Assess this claim so a numeric confidence can be authored.

---

## Numeric Claim G Blocked By A Pending Dependency
<!-- id: clm-gg7777 -->

A claim with a numeric confidence (0.95) whose single dependency is the
pending claim clm-ff6666. Its derivation branch is `*pending*` (pending-ness
propagates like NaN), but a `run` experiment (exp-bench1) strengthens it at
0.80, so its experimental branch is the only non-null branch and final
solidity is RESCUED to 0.80 via the max-branch.

### Quality
- confidence: 0.95
- depends-on:
  - clm-ff6666 — Pending Upstream Claim F (solidity *pending*) [poisoned by the pending upstream]
- solidity: 0.80 (ok to build on, see caveats)
- rationale: synthetic experiment-rescued claim; derivation pending, experimental branch governs.
- strengthen-by:
  - Assess clm-ff6666 so clm-gg7777's derivation branch can also score.

---

## Double-Framework-Edge Claim H
<!-- id: clm-hh8888 -->

A claim whose owner declares the same framework target (INVARIANT-S2) twice,
in two separate depends-on bullets with different context. Both edges must
survive as distinct records.

### Quality
- confidence: 0.70
- depends-on:
  - INVARIANT-S2 (context A — labelling convention for the d-axis treatment)
  - INVARIANT-S2 (context B — labelling convention for the q-axis treatment)
- solidity: 0.70 (ok to build on, see caveats) [= 0.70 × 1.00]
- rationale: synthetic double-INVARIANT-S2-from-one-owner case.
- strengthen-by:
  - Merge the two context treatments so the claim cites INVARIANT-S2 once.

---

## Co-Hosted Prediction Claim I
<!-- id: clm-co1111 -->

A claim stated by the same leaf that ALSO hosts the experiment which tests it
(co-hosting — `claims:` and `exp-id:` are orthogonal node-bodies in one
container, INVARIANT-S9). Its derivation is `*pending*`, so its derivation
branch is null; the co-located `run` experiment exp-cohst1 strengthens it at
0.90, the only non-null branch, so its final solidity is 0.90 (max-branch).

### Quality
- confidence: *pending*
- solidity: 0.90 (ok to build on)
- rationale: synthetic co-hosted claim+experiment; derivation pending, experimental branch governs.
- strengthen-by:
  - Author the derivation so the claim also scores a derivation branch.
