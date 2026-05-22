# 122 — Q-G47 Sessions 19+ Scope Adjudication: (a) construction-given + (b) factor-verification

**Date:** 2026-05-16 late evening
**Branch:** `research/l3-electron-soliton`
**Status:** **ADJUDICATION CLOSED per Grant 2026-05-16 late evening** — the Q-G47 Sessions 19+ multi-week work is RESCOPED as a verification calculation, not a free-parameter derivation. This significantly narrows the scope.

---

## §0 TL;DR

Per the Grant (a)/(b) adjudication via trampoline-pure language framing (this session, doc 122 captures):

**Mode (a) — substrate construction is GIVEN**:
- K4 lattice (Axiom 1) baked in
- Over-bracing length $r_{\text{secondary}}/d = 1.187$ baked in (Vol 3 Ch 1:33-37)
- I4₁32 chirality from parent-BH spin baked in (Q-G21)
- Bond occupation fraction $p^* = 8\pi\alpha \approx 0.183$ baked in (Vol 3 Ch 1:20)
- Cosserat coupling moduli structure baked in (Q-G47 Session 9 χ_K = 12, Session 11 χ_G = 3, Session 17 ξ_K2/ξ_K1 = 12)

**Mode (b) — verification at the operating point**:
- Compute $f_{\text{Cosserat}}, f_{\text{buckling}}, f_{\text{Cauchy}}$ explicitly at $u_0^* \approx 0.187$
- Verify all three simultaneously equal 1 at this operating point
- If yes: substrate is internally consistent at K=2G operating point — framework verification PASSES
- If no: misframing somewhere in Cosserat moduli construction — flag for revision

This is **NOT a prediction calculation** (where $u_0^*$ would be derived from substrate alone) but a **consistency check** (where $u_0^* = 0.187$ is taken from A-029 canonical and we verify the three factors equal 1 at it).

---

## §1 What Q-G47 Sessions 19+ now needs (rescoped)

### §1.1 The verification computation (1-2 sessions, not multi-week)

Given the (a)+(b) adjudication, the Sessions 19+ work is:

1. **Extract explicit functional forms** of $f_{\text{Cosserat}}, f_{\text{buckling}}, f_{\text{Cauchy}}$ as functions of $(u_0, \ell_c, r_{\text{secondary}}/d)$ from Q-G47 Sessions 5-13 (already developed; just need to be made explicit).
2. **Plug in** the substrate-construction-given values:
   - $u_0 = u_0^* = 0.187$ (A-029 canonical)
   - $r_{\text{secondary}}/d = 1.187$ (Vol 3 Ch 1:33-37)
   - $\ell_c = $ derived from Cosserat dimensional analysis (Session 17: $\ell_c^2 = \ell_{\text{node}}^2 \cdot \xi_{K2}/(2\xi_{K1}) = 6 \cdot \ell_{\text{node}}^2$ → $\ell_c = \sqrt{6} \cdot \ell_{\text{node}}$)
3. **Numerical evaluation**: do the three f-factors all equal 1 (within tolerance)?
4. **Report**: framework-internal consistency check PASS/FAIL, with diagnostics if FAIL.

This is concrete computation work, not open-ended derivation. Probably ~1-2 sessions if the Session 5-13 explicit forms are recoverable.

### §1.2 What's NOT in scope per (a) adjudication

The following are NOT computed because they're given by substrate construction:

- $p^* = 8\pi\alpha$: substrate self-organized to this bond density during cosmic crystallization (Mode a). Not derived from K=2G; it IS the K=2G operating point at $z_0 \approx 51.25$ amorphous coordination.
- $r_{\text{secondary}}/d = 1.187$: substrate construction (Vol 3 Ch 1:33-37). Not a free parameter.
- $u_0^* = 0.187$: A-029 canonical magic-angle from Session 6 sensitivity sweep at $\chi_K = 12$ + quadratic shape function. Taken as given for verification.
- I4₁32 chirality direction: parent-BH spin (Q-G21). Not derivable from inside.

### §1.3 χ_1/K_0 implication

The χ_1/K_0 question from docs 117/118/120/121 then resolves naturally per Mode (a)+(b):

- **Mode (a)**: χ_1, χ_2, χ_3 are O(1) at substrate scale (full chirality from bipartite K4 anti-chirality, per K4-TLM canonical)
- **Mode (b)**: the BULK observables that χ_1 produces are filtered through bipartite cancellation at substrate scale + cosmic-scale Φ_A integration, giving final amplitudes that depend on cosmic-formation conditions ($f_R$)

Per A-031 cosmic-parameter horizon, the amplitude is FUNDAMENTALLY UNDETERMINED without parent BH parameters. **This is the honest framework state** — already captured in doc 121 §9.6.

---

## §2 Implications for doc 119/120/121 status

### §2.1 Doc 119 (α²-universal-operator adjudication)

Doc 119 §7 verdict: NOT canonical-ready. **Stands** per this adjudication — the α² appearances are heterogeneous (cross-sectional porosity at cosmic, two-vertex polarization at electroweak, Rydberg at atomic, etc.), not unified at substrate scale.

### §2.2 Doc 120 (χ_1/K_0 by analogy = O(1))

Doc 120 conclusion: χ_1/K_0 ~ O(1) at substrate scale. **VALIDATED** per this adjudication — Mode (a) confirms full chirality at substrate scale (no α-suppression).

The "by analogy with χ_K = 12, χ_G = 3" reasoning in doc 120 §2 is RIGHT: chirality moduli at substrate scale are O(1) like the diagonal Cosserat moduli. The doc 121 §1-§5 plumber re-examination that overruled it was the actual error (scale mixing).

### §2.3 Doc 121 (plumber re-examination)

Doc 121 §1-§5: WRONG (Φ_A is cosmic-scale, not substrate cross-coupling). Already corrected in doc 121 §9.

Doc 121 §9-§10 honest closure: framework predicts P_2(cosθ) angular profile sharply, amplitude is undetermined per A-031 cosmic-parameter horizon. **Stands** per this adjudication.

### §2.4 omega-freeze + CODATA G prereg

Current "α^N undetermined" bracket framing is correct per the (a)+(b) adjudication. NO further propagation needed (peer-review Items 3+4 abandoned per doc 121 §9.6).

---

## §3 What's now the actual derivation arc

Given the (a)+(b) adjudication, the open derivation arc clarifies to:

| Piece | Status | Scope |
|---|---|---|
| Q-G47 Sessions 19+ verification calculation | Rescoped (1-2 sessions, not multi-week) | Compute three f-factors at $u_0^* = 0.187$, verify all = 1 |
| f_R bounds from cosmic formation | Open | Even with A-031 limiting access to parent BH params, may have bounds from CMB anisotropy budget |
| Angular-profile-only empirical test | Open | CODATA G dataset re-analysis for ANY $P_2(\cos\theta)$ profile at any amplitude |
| Doc 117 §10 K_phys ~ α² conjecture | Status: reverse-engineered matching, plumber-defensible if χ_1 has any additional cosmic-scale Φ_A factor; needs Mode (b) verification to either close or refute |
| Doc 118 §9 ΔG/G amplitude prediction | Status: α^N undetermined per A-031 horizon; angular profile P_2 sharply predicted |

---

## §4 Recommended next action

The Q-G47 Sessions 19+ verification (§1.1) is now bounded scope. Either:

1. **Attempt the verification now** (~1-2 sessions): extract f-factor explicit forms from Sessions 5-13, evaluate at $u_0^* = 0.187$, report PASS/FAIL with diagnostics. If PASS: framework-internal consistency check closed. If FAIL: flag misframing in Cosserat moduli construction.

2. **Queue for later**: capture this adjudication doc as the scope, pick up when there's a dedicated session for the computation.

Grant's call on which.

---

## §5 Cross-references

- doc 117 §10 — K_phys ~ α² (reverse-engineered, needs verification via Mode b)
- doc 118 §9 — ΔG/G amplitude (α^N undetermined per A-031)
- doc 119 §7 — α² NOT canonical-ready (stands)
- doc 120 §2 — χ_1/K_0 ~ O(1) at substrate (VALIDATED per this adjudication)
- doc 121 §9-§10 — Φ_A scale conflation acknowledged; angular profile sharp, amplitude undetermined
- AVE-QED Q-G47 Sessions 1-18 — substrate-physics framework
- AVE-QED Q-G47 Session 17:49 — ratio ξ_K2/ξ_K1 = 12 closed, individuals deferred (now rescoped per this doc)
- Vol 3 Ch 1:17-23 — p* = 8πα EMT operating point + K=2G derivation
- trampoline-analogy-primer §Step 2 — Cauchy + over-bracing + Cosserat trampoline framing
