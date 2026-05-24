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

---

## Support Beneficiary J — Lifted To 0.90
<!-- id: clm-sb1111 -->

A low-confidence (0.40) dependency-free claim. The free-standing support
sup-free01 (quality 0.90) supports it on-point at f=1.0, lifting its
local_quality to max(0.40, 0.90×1.0) = 0.90, so its derivation solidity is 0.90
(no own deps to gate it). The DERIVATION-branch lift from a support
(INVARIANT-S10).

### Quality
- confidence: 0.40
- solidity: 0.90 (ok to build on)
- rationale: synthetic support-lifted claim; lifted from 0.40 to 0.90 by sup-free01 at f=1.0.
- strengthen-by:
  - Author a stronger first-principles derivation so confidence rises without leaning on the support.

---

## Support Beneficiary K — Fractional Lift To 0.45
<!-- id: clm-sb2222 -->

A second low-confidence (0.40) dependency-free claim, supported by the SAME
sup-free01 but at a smaller on-point fraction f=0.50. Its lift is 0.90×0.50 =
0.45, so local_quality = max(0.40, 0.45) = 0.45 and derivation solidity is 0.45
— demonstrably less than clm-sb1111's f=1.0 lift (multi-beneficiary support;
on-point fraction < 1.0 reduces the contribution).

### Quality
- confidence: 0.40
- solidity: 0.45 (use as input only, don't build deeper)
- rationale: synthetic fractional-support claim; lifted from 0.40 to 0.45 by sup-free01 at f=0.50.
- strengthen-by:
  - Establish a more on-point support so the fraction can rise toward 1.0.

---

## Support Beneficiary L — Lifted By A Dep-Gated Support
<!-- id: clm-sb3333 -->

A low-confidence (0.30) dependency-free claim, supported at f=1.0 by sup-dep001,
whose OWN solidity is dep-gated below its quality (quality 0.90 × dep clm-aa1111
final 0.90 = 0.81). So the lift is 0.81, local_quality = max(0.30, 0.81) = 0.81,
and derivation solidity is 0.81.

### Quality
- confidence: 0.30
- solidity: 0.81 (ok to build on, see caveats)
- rationale: synthetic claim lifted by a dep-gated support; the support's own deps throttle its solidity below its quality.
- strengthen-by:
  - Discharge the support's dependency so its solidity can rise toward its quality.

---

## Support Beneficiary M — Not Poisoned By A Pending Support
<!-- id: clm-sb4444 -->

A claim with valid confidence (0.55) supported by the PENDING-quality support
sup-pend01. A pending support contributes nothing to the max (no NaN, no
poison), so local_quality stays 0.55 and derivation solidity is 0.55 — the
pending support neither lifts nor drags it to pending (INVARIANT-S10).

### Quality
- confidence: 0.55
- solidity: 0.55 (use as input only, don't build deeper)
- rationale: synthetic claim with a pending support; the pending support contributes nothing and does not poison.
- strengthen-by:
  - Evaluate sup-pend01 so its (currently pending) lift can either raise or leave this claim's solidity.

---

## Support Beneficiary N — Lifted By A Co-Hosted Support
<!-- id: clm-sb5555 -->

A mid-confidence (0.50) dependency-free claim lifted to 0.85 by sup-coh001
(quality 0.85, free-standing, f=1.0). sup-coh001 is co-hosted on a leaf that ALSO
declares its own `claims:` — `claims:` and `sup-id:` are orthogonal node-bodies
in one container (INVARIANT-S10).

### Quality
- confidence: 0.50
- solidity: 0.85 (ok to build on)
- rationale: synthetic claim lifted by a co-hosted support; lifted from 0.50 to 0.85 by sup-coh001.
- strengthen-by:
  - Author a stronger derivation so the claim's own confidence approaches the supported value.

---

## Support Beneficiary O — Lifted By One Of Two Co-Hosted Supports
<!-- id: clm-sb6666 -->

A low-confidence (0.40) dependency-free claim, beneficiary of TWO supports
co-hosted on one container (leaf-multi-sup.md): sup-mlt001 lifts it at f=1.0
(lift 0.80), while sup-mlt002 names it at a `*pending*` on-point fraction (which
contributes nothing — an unassessed edge is excluded from the max). So
local_quality = max(0.40, 0.80) = 0.80 and derivation solidity is 0.80.

### Quality
- confidence: 0.40
- solidity: 0.80 (ok to build on, see caveats)
- rationale: synthetic claim lifted by one of two co-hosted supports; the pending-fraction support edge contributes nothing.
- strengthen-by:
  - Assess the pending on-point fraction from sup-mlt002 so its lift can be realized.

---

## Support Beneficiary P — Fractional Lift From A Second Co-Hosted Support
<!-- id: clm-sb7777 -->

A low-confidence (0.30) dependency-free claim, supported only by sup-mlt002
(quality 0.70, free-standing) at f=0.50. Its lift is 0.70×0.50 = 0.35, so
local_quality = max(0.30, 0.35) = 0.35 and derivation solidity is 0.35 —
demonstrating that the SECOND sup-id on a multi-sup container fans out
independently.

### Quality
- confidence: 0.30
- solidity: 0.35 (do not build on this yet)
- rationale: synthetic claim lifted by the second of two co-hosted supports at a fractional on-point relevance.
- strengthen-by:
  - Establish a more on-point support so the fraction can rise toward 1.0.

---

## Support: First Of Two Co-Hosted Supports
<!-- id: sup-mlt001 -->

The first of TWO support nodes hosted on one container (leaf-multi-sup.md),
free-standing (quality 0.80, sup_solidity 0.80). It supports clm-sb6666 at
f=1.0. Hosting MULTIPLE sup-ids on one leaf is allowed — a container hosts any
number of any combination of clm/exp/sup node-bodies (INVARIANT-S10).

### Quality
- quality: 0.80
- solidity: 0.80 (ok to build on, see caveats)
- rationale: synthetic first support on a multi-sup container; free-standing, sup_solidity equals quality.
- supports:
  - clm-sb6666 (f=1.0)

---

## Support: Second Of Two Co-Hosted Supports
<!-- id: sup-mlt002 -->

The second of two support nodes on the SAME container, free-standing (quality
0.70, sup_solidity 0.70). It supports clm-sb6666 at a `*pending*` on-point
fraction (intended-but-unassessed; contributes nothing) and clm-sb7777 at
f=0.50.

### Quality
- quality: 0.70
- solidity: 0.70 (ok to build on, see caveats)
- rationale: synthetic second support on a multi-sup container; one beneficiary edge carries a pending on-point fraction.
- supports:
  - clm-sb6666 (f=*pending*) and clm-sb7777 (f=0.50)

---

## Support: Free-Standing Analytical Support
<!-- id: sup-free01 -->

A non-physical analytical support node (INVARIANT-S10) with NO dependencies of
its own (free-standing), so its sup_solidity equals its quality, 0.90. It
supports two beneficiaries — clm-sb1111 at f=1.0 and clm-sb2222 at f=0.50
(experiment-like multi-beneficiary fan-out, claim-like internals).

### Quality
- quality: 0.90
- solidity: 0.90 (ok to build on)
- rationale: synthetic free-standing support; sup_solidity equals quality (no deps).
- supports:
  - clm-sb1111 (f=1.0) and clm-sb2222 (f=0.50)

---

## Support: Dep-Gated Analytical Support
<!-- id: sup-dep001 -->

A support that consumes its own dependency (clm-aa1111, final 0.90), so its
sup_solidity is dep-gated below its quality: round2(0.90 × 0.90) = 0.81. It
supports clm-sb3333 at f=1.0.

### Quality
- quality: 0.90
- depends-on:
  - clm-aa1111 — Foundation Claim A (solidity 0.90) [the support builds on the anchor claim]
- solidity: 0.81 (ok to build on, see caveats) [= 0.90 × 0.90]
- rationale: synthetic dep-gated support; its own dependency throttles sup_solidity below its quality.
- supports:
  - clm-sb3333 (f=1.0)

---

## Support: Pending-Quality Analytical Support
<!-- id: sup-pend01 -->

A support whose local rigor has not yet been evaluated (`quality: *pending*`),
so its sup_solidity is `*pending*` and it contributes NOTHING to any
beneficiary's max (no poison). It supports clm-sb4444 at f=1.0.

### Quality
- quality: *pending*
- solidity: *pending*
- rationale: *pending*
- supports:
  - clm-sb4444 (f=1.0)

---

## Support: Co-Hosted Analytical Support
<!-- id: sup-coh001 -->

A free-standing support (quality 0.85, sup_solidity 0.85) hosted on a leaf that
ALSO declares its own `claims:` list — orthogonal node-bodies in one container.
It supports clm-sb5555 at f=1.0.

### Quality
- quality: 0.85
- solidity: 0.85 (ok to build on)
- rationale: synthetic co-hosted support; free-standing, sup_solidity equals quality.
- supports:
  - clm-sb5555 (f=1.0)
