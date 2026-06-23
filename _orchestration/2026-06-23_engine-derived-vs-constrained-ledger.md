# AVE Engine — State-of-Engine Derived-vs-Constrained Ledger

**Date:** 2026-06-23 · **Status:** for review — orchestrator adversarial audit + Grant merge pending.
**Lane:** engine-consolidation (D1). **Scope:** AVE-Core engine + KB, HEAD = `origin/main`.

> **PLACEMENT IS A GRANT-CALL.** This document is staged in `_orchestration/` (the lane's staging
> area). Its proposed canonical home is a KB common leaf — e.g.
> `manuscript/ave-kb/common/engine-derived-vs-constrained-ledger.md` — which would make it greppable
> and citable but would require KB front-matter + claim-ids + the `verify-kb-metadata` gate. The two
> options for Grant:
> - **(a)** Promote to `common/` as a canonical leaf (full KB metadata, cross-linked from
>   `claim-quality.md` and `interlock-register.md`). Best if this is to be cited as the cross-cutting
>   tier authority.
> - **(b)** Keep in `_orchestration/` as a living lane artifact (no KB metadata burden, clearly a
>   "derived summary, not a leaf"). Best if `claim-quality.md` + `interlock-register.md` remain the
>   sole canonical registers and this is a navigational overlay.
>
> Either way this is a **derived summary**: the canonical leaves are the source of truth. Where this
> ledger and a leaf disagree, the leaf wins.

---

## 0. Why this document exists

The corpus already carries two canonical registers of claim quality:

- `manuscript/ave-kb/claim-quality.md` — the cross-cutting **per-claim** tripwire register (what each
  claim asserts and, precisely, what it does **not**).
- `manuscript/ave-kb/common/interlock-register.md` — the CI-gated **calibration** register
  (`calibration-params: clm-0ktpcn clm-5xon03 clm-dsb560`; `expected-independent-count: 3`).

What no single leaf carries is the **cross-cutting tier view**: a most-derived → least-derived ranking
of the engine's results along the one axis that the project's north-star cares about —
**does AVE derive this, or import/echo it?** This ledger is that view. It complements
`claim-quality.md` (per-claim) and `form-deriving-value-importing.md` (the form-vs-value thesis);
it does not replace either.

It was produced from (i) a 6-agent engine-map + derived-vs-constrained ranking pass (2026-06-23) and
(ii) a refute-by-default verification workflow that re-checked every load-bearing tier claim against
HEAD. The **discipline that governs it**: nothing is ranked above its **value-evidence** tier. A FORM
that AVE forces but whose dimensionful VALUE is imported is ranked by the VALUE.

---

## 1. The standing meta-finding — FORMS vs VALUES

AVE **forces the FORMS** (ratios, selection rules, scaling exponents, topological integers) and
**imports the dimensionful VALUES** of its calibration constants. The calibration set is exactly three,
CI-gated (`interlock-register.md`): **{m_e, α, G}**. Every dimensionful magnitude the engine reports is,
by construction, an **echo** of those three plus SI-definitional constants — matching CODATA/PDG is a
*consistency* of the calibration, not an AVE-distinct emergence. This is not an AVE weakness specific to
the framework: the Standard Model imports α, the Yukawas, Λ, and charge quantization too
(**symmetric-standard** — see `form-deriving-value-importing.md`). The honest claim is **structural**:
the FORMS are forced. **The AVE-distinct *chord* — if there is one — lives only in the forward
predictions** (§7), not anywhere inside this ledger.

---

## 2. The 7-tier ledger (most-derived → least)

Columns: **FORM** = what the engine genuinely forces; **VALUE** = what is imported/fitted/echoed;
**Band** = corpus solidity where a `clm-` carries one. Read every row as *form-derived,
value-`<as-noted>`*.

### T1 — AXIOM-FORCED (forms only; no value import)
| Result | FORM (forced) | VALUE | Band | Anchor |
|---|---|---|---|---|
| 4 axioms | the framework's primitives | — | — | `CLAUDE.md` Axioms 1–4 |
| Saturation kernel S(A)=√(1−(A/A_yield)²) | quarter-arc kernel, all scales | A_yield is a per-system ratio, not a number here | ~0.85 | Axiom 4; A-034 catalog |
| Op5 K4 scattering S_ij = 0.5 − δ_ij | **EXACT** unitary 4-port equal-admittance junction | none | spine/EXACT | `universal_operators.py:279`; `k4_tlm.py:69-82` |
| Op3 reflection Γ (min-\|Γ\|²) | boundary-reflection extremization | none | — | Axiom 3 |
| Tetrahedral-gradient stencil | the stencil FORM | none | — | engine stencil |
| K4 update rule | bipartite tetrahedral propagation | none | — | `k4_tlm.py` |

*Verified:* Op5 S_ijᵀS_ij = I exactly (det = −1, eigenvalues {+1,−1,−1,−1}) — orthogonal/unitary, zero
imported value.

### T2 — DERIVED, α-FREE (forced dimensionless structure)
| Result | FORM (forced) | VALUE | Band | Anchor |
|---|---|---|---|---|
| κ̃ = pq/(p+q) = 6/5 | **α-free** topological formula | electron (2,3) winding is a *stipulated* topology input | spine | `cosserat_field_3d.py:94,98-112`; `test_kappa_tilde_topology.py` asserts α-free |
| ξ_topo = e/ℓ_node | the FORM (TKI charge↔length isomorphism) | **VALUE imported**: ξ_topo = e·m_e·c/ℏ via ℓ_node = ℏ/(m_e c) → rides CODATA e + m_e | 0.90 "no fitting"† | `constants.py:278,324`; clm-i9l284 |
| Z₀ as √(L/C) of the LC bond | the LC-network FORM | value is SI-definitional (√(μ₀/ε₀)) | 0.90 | KB circuit leaves |
| spin-½ / g=2 | FR-braid spin-statistics structure | — | 0.70 | carrier-sector arc |
| ξ_K2/ξ_K1 = 12, ℓ_c/ℓ_node = √6 | forced lattice ratios | — | — | lattice geometry leaves |

† **OVER-REACH WATCH (see §5).** "0.90 no-fitting" is correct for the *translation-table algebra*
(no free knob is tuned) but the *value* imports e + m_e. This ledger labels ξ_topo
**derived-FORM / imported-VALUE** — not bare "derived." Reading "0.90 no-fitting" as "value derived"
would be the over-reach.

### T3 — DERIVED-CONDITIONAL (forced form, riding a disclosed import/ansatz)
| Result | FORM (forced) | VALUE | Band | Anchor |
|---|---|---|---|---|
| Charge Q = Link ∈ ℤ | exact integer topological charge | reconciliation **OPEN** (C.3: helicity returns ~18% of p·q) | — | carrier-sector arc |
| sin²θ_W = 2/9 | forced ratio from ν_vac=2/7 + PAT | **conditional on the K=2G import** (ν_vac=2/7 is GR-borrowed) | 0.85‡ | clm-5zuo7g |
| α_s = α^(3/7) | forced exponent 3/7 | dimensionless **value rides the α echo** | 0.50 | clm-ome498 |
| proton m_p/m_e | cinquefoil-confined Faddeev-Skyrme topology forced | rides imported m_e + α + **chosen Skyrme ansatz + Gaussian flux-tube** | 0.63 | clm-mnb3lt, clm-oygz1i |
| baryon ladder | shared no-retune ladder structure | each mass value rides m_e echo + ansatz; ~2% band | 0.63 | clm-mnb3lt |
| finite-by-construction / no-renorm | geometric ℓ_node cutoff removes UV divergences (**structural, no value**) | — (QED-equivalent, not AVE-distinct) | T1-strong | q-g20a/q-g20f; `vol2/claim-quality.md:1425-1429` |

‡ **GENUINE OVER-REACH — Grant-call (see §5).** The 0.85 does **not** propagate the ν_vac=2/7
(= K=2G, clm-iouqn9, **0.55 input-only**) import cap, because the `depends-on` graph wires
clm-5zuo7g only to Axiom-1 + INVARIANT-S2, **not** to the import. By the project's own
min-over-dependencies solidity rule, a ratio riding a 0.55 import should not out-rank it at 0.85.

### T4 — CONSISTENCY-CHECK (reproduces a known result via reinterpretation)
| Result | Status | Band | Anchor |
|---|---|---|---|
| BCS B_c(T) | reproduced, 0.00% (calibrated) | — | A-034 catalog |
| **A-034 universal-saturation-kernel catalog** | **26 instances** (19 physical + 2 biological + 5 engineered) — *see D2(a) count reconciliation* | 0.62 | `backmatter/07_universal_saturation_kernel.tex` |
| EW masses / CKM / PMNS | 0.5–5% consistency; forms forced, values echo | 0.60 (PMNS clm-7o8clt) | ch06 leaves |
| H_∞ | self-consistency **identity** with G (not independent) — see D4 Chain B′ | — | `mathematical-closure.md:168` |
| p_c = 8πα | forced form; **imports α** | — | clm-cmic3e |
| three-impedance + per-DOF node circuit | predicts *no* new α/m_e (structural) | — | vacuum-circuit arc |

### T5 — IMPORTED / MIXED (the value-anchors)
| Result | Nature | Band | Anchor |
|---|---|---|---|
| m_e | **definitional** input scale (ℓ_node = ℏ/(m_e c) circular) | calibration | clm-5xon03 |
| K = 2G / ν_vac = 2/7 | **GR-imported** trace-reversal identity; crystalline route closed **NEGATIVE** (PR #261) | 0.55 input-only | clm-iouqn9; `trace-reversal-mechanism.md:20-23` |
| G | **MIXED** — form from achromatic-lens; value-fitted (ξ back-solved from CODATA G) | calibration | clm-dsb560 |
| V_yield | existence = chord; √α value = echo | — | keystone leaves |

### T6 — ECHO (value is a calibration identity the substrate does not independently select)
| Result | Nature | Band | Anchor |
|---|---|---|---|
| α three-route α⁻¹ = 4π³+π²+π | FORM is a chord; **VALUE is a standing ECHO** — all 3 named lift-routes closed-negative; **22 dependents** | 0.63 | clm-0ktpcn; `ch8-alpha-golden-torus.md` |
| δ_strain magnitude | definitional residual (1 − CODATA/α_cold); magnitude route **closed-negative** (FT-1, ~31 OOM) — see D4 | 0.55 | `delta-strain-cosmic-tcc.md`; FT-1 |

### T7 — FITTED / ASSERTED / REFUTED
| Result | Nature | Band | Anchor |
|---|---|---|---|
| nuclear mass-defect (0.0000%) | the "0%" is fitting tolerances, not a prediction | — | vol6/nuclear leaves |
| optical-activity magnitude | **demoted** (PRs #374/#376) — FORM-only, magnitude not bankable | — | #374/#376 |
| Sagnac = proton | "do not build" | 0.20 | Sagnac leaf |
| spin-statistics **theorem** | **ASSERTED / provisional** — distinct from the *derived* spin-½ VALUE (T2) | provisional | carrier-sector arc |
| chirality-as-phase-polarity | **REFUTED** | 0.10 | strain-parity arc |

---

## 3. The SPINE (survives any reframing)

Verified `spine_confirmed = true` against engine code + corpus this lane:

- The **4 axioms** + the operators they force **exactly** — Op5 S_ij = 0.5 − δ_ij is exactly unitary
  (checked by arithmetic).
- The two **α-free derived results**: **κ̃ = pq/(p+q) = 6/5** (test asserts α-independence) and the
  **ξ_topo = e/ℓ_node FORM** (the TKI isomorphism — spine at the **FORM** level; its VALUE imports
  e + m_e, see §5).
- **finite-by-construction** (geometric cutoff removes UV divergences; honestly scoped as
  QED-*equivalent*, not AVE-distinct).

**NOT in the spine:** the **Master Equation** (`clm-efo113`, solidity **0.50**, EFT-only,
"use as input only, don't build deeper") — it drops the ∇ε·∇V first-derivative gradient term;
saturated-regime confinement rides that term being negligible-by-symmetry, which is **asserted, not
derived**. Treat the Master Equation as input, not as a spine load-bearer.

---

## 4. SOFT EDGES (every value-anchor; most "forced ratios" sit downstream of an import)

The structural wins are real, but **every dimensionful anchor is soft**, and a large share of the
"forced ratios" (Weinberg, α_s, CKM, PMNS) are **downstream of the K = 2G import** because they ride
ν_vac = 2/7. Refuting the calibration node of α (`clm-0ktpcn`), G (`clm-dsb560`), or m_e
(`clm-5xon03`) propagates a verifier failure through the operating-point root (`clm-iouqn9`). The
ledger's "derived" tiers (T1–T3) are only as load-bearing as the imports they ride; T1 is the only tier
with no value dependency at all.

---

## 5. Operators the engine-map omitted but that load-bear ranked results

Two universal operators do real ranking work and belong in this ledger:

- **Op20 — Universal Regime Boundary Eigenvalue**, `universal_operators.py:911`:
  ω = ℓ · c_wave / r_eff (r_eff = r_sat/(1+ν_vac)). **Load-bears the baryon/orbital ladders and the
  BH ring-down** eigenvalue (ω_R M_g ≈ 18/49, 1.7% from GR-exact — a *consistency* match, not
  AVE-distinct).
- **Op21 — Universal Phase Transition Quality Factor**, `universal_operators.py:932`: returns
  Q = ℓ (an **integer mode number**, BH/baryon scale).
  **CORRECTION to the engine-map brief:** Op21 is **not** the "α Q_tank close-route." Op21's Q = ℓ is
  the integer mode count; the α-related **Q_tank = 1/α echo is baked separately** in `cvr_model.py`
  (a distinct, separately-flagged echo). Do not conflate Q = ℓ with Q = 1/α.

### Over-reach watch (carried from the refute-by-default audit)
1. **ξ_topo (T2)** — derived-FORM / **imported-VALUE**. Carry the qualifier; never headline it as
   "value derived." *(Canonicalization risk, not a current index error.)*
2. **Weinberg sin²θ_W = 2/9 (T3)** — scored 0.85 but rides the 0.55 K=2G import; the `depends-on` edge
   to the import is **missing**, so the score is not import-capped. **GRANT-CALL** (§6, Q1).

---

## 6. Grant-calls surfaced (do not resolve in this lane)

- **Q0 — Placement** of this ledger: KB `common/` leaf (a) vs `_orchestration/` artifact (b). See header.
- **Q1 — Weinberg import-cap.** The vacuum Poisson ratio 2/7 is scored as if it were a free dial, but
  it is the GR-borrowed K=2G value. Should sin²θ_W=2/9's tier be **capped at the import's 0.55** (wire
  the `depends-on` edge clm-5zuo7g → clm-iouqn9), or **stay 0.85 with a "conditional-on-import"
  asterisk**? This ledger uses the asterisk (‡) pending the call; it does **not** rewire the index.
- *(Cross-lane, for context)* D2(a) surfaces the `eq_axiom_4.tex` physical-subset(19)-vs-total(26)
  fork; D2(b) surfaces the √(3/7) "torsion-shear" label; D2(c) surfaces the predictions.yaml
  type-axis re-tags. Those are owned by the D2 PR.

---

## 7. Where the AVE-distinct chord actually lives

Nothing inside this ledger is an AVE-distinct *chord* — the internal structure is uniformly
**peer-with-SM** (both frameworks force some forms and import some values). The structural wins worth
keeping are real and should not be walked back: **no renormalization, exact integer charge,
spin-statistics-derived, real (not point) mass.** But the make-or-break AVE-distinct content is
**only** in the **untested forward predictions** — optical-activity sign-flip, the (q·ℓ_node)⁴
dispersion, GW-echo, vacuum birefringence ~10⁶× QED, the α-invariance-under-gravity null. Those are
where a chord (or its falsification) will come from; this ledger exists so that consolidation work does
not mistake a forced FORM riding an imported VALUE for one of them.

---

## 8. Provenance

Built from: the engine-map + derived-vs-constrained ranking (2026-06-23, verify HIGH) and a
refute-by-default verification workflow (5 lanes: A-034 count, predictions congruence, stale-import
sweep, ledger over-reach audit, owed-derivation scoping). Spine + soft-edges + the two over-reach
findings (ξ_topo qualifier, Weinberg import-cap) are file:line-grounded against HEAD. Every solidity
band cited is the corpus's own `clm-` band, not a band minted here.
