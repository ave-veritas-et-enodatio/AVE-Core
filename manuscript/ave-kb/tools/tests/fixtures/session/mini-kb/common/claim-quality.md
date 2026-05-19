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
pending claim clm-ff6666. Pending-ness propagates like NaN: solidity is
`*pending*` regardless of the local confidence.

### Quality
- confidence: 0.95
- depends-on:
  - clm-ff6666 — Pending Upstream Claim F (solidity *pending*) [poisoned by the pending upstream]
- solidity: *pending*
- rationale: synthetic numeric-claim-blocked-by-pending-dependency case.
- strengthen-by:
  - Assess clm-ff6666 so clm-gg7777 can inherit a numeric solidity.

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
