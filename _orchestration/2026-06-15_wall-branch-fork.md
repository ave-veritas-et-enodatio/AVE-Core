[↑ Orchestration Index](index.md)

# Wall-Branch Fork (H3): the electron's Γ=−1 wall — MAGNETIC or CAPACITIVE saturation?

**Lane founded:** 2026-06-15 · **Branch:** `analysis/2026-06-15-wall-branch-fork` (off `main` @ `40a2a2e7`) · **Worktree:** `AVE-Core-wall-wt` · **Status:** ACTIVE — Phase 1 (corpus map + prereg)

**Arc:** corpus-grep prereg → Rule-11 freeze → auditor-gate → driver → result → adjudicate to Grant. `main` PROTECTED; all edits via reviewed PR; **Grant merges**.

---

## 1. Charter (derivation target)

Which saturation branch forms the electron's Γ=−1 confining wall?

- **MAGNETIC** branch: $\mathbf{B}$ saturates $\mu_{eff}\to0$ first → $Z=\sqrt{\mu_{eff}/\varepsilon_0}\to0$ → Γ→−1 (short). [`master-equation.md`:85, `clm-lv3uw1`]
- **CAPACITIVE** branch: the local topological twist drives dielectric saturation $C_{eff}\to\infty$ → $Z_{core}=\sqrt{\mu_0/C_{eff}}\to0$ → Γ=−1. [`resonant-lc-solitons.md`:29–46, `clm-kezk9z`]
- **THIRD config (reserved, NOT the wall):** ε-rupture → $\varepsilon_{eff}\to0$ → $Z\to\infty$ → the anti-confinement / opaque / photon branch. [`master-equation.md`:84] — distinguish, do **not** conflate.

**Discriminator (charter):** the branch (μ vs ε) that reaches Z→0 *first* and *stably confines* = the wall mechanism. **If degenerate / co-saturating → report it** (a real result; informs the A1-vs-T2 fork).

**Knock-on (flag-don't-fix to Grant):** this couples to the **A1-vs-T2 mass-sector fork** — magnetic/μ ↔ T2 inductive/micro-rotation (charge-"3" winding); capacitive/ε ↔ A1 dilatation/E (mass-"3"). The result tells which "3" carries the mass.

---

## 2. ⚠ CRITICAL PRE-FINDING — this is NOT a green-field fork (ave-prereg payoff)

The corpus is **already self-aware of this exact fork** and has worked it substantially. The prompt's grounded-starting-state did not mention this; verified 2026-06-15. The fork is a **named open flag (FLAG-2)** with a layered, *partially self-contradictory* corpus state and a recent (2026-06-13) candidate **gauge-dissolution**. Verbatim, verified:

### 2a. It is already FLAG-2
`vol4/claim-quality.md`:1256 (clm-fd1e7a) + `cvr-dc-operating-point.md`:55 (AUDITOR_STATE FLAG-2):
> "which constitutive parameter moves at the wall (capacitive $C_{eff}\to\infty$ vs magnetic $\mu_{eff}\to0$) … **both routes give the same $Z=Z_0\sqrt{S}$ curve, so the bundle is robust but the attribution is unsettled.** **Magnetic is PRIMARY** per the handoff; the capacitive route is the flagged co-attribution."

→ **The equilibrium impedance observable $Z=Z_0\sqrt{S}$ is DEGENERATE between the two branches by the corpus's own admission.** The naive "which reaches Z→0 first" on the operating-point curve cannot discriminate. The charter anticipated this ("if degenerate → report it").

### 2b. `clm-lv3uw1` (magnetic) is INPUT-ONLY
The magnetic-branch claim is tagged an asserted **input**, not a derived result (`vol4/claim-quality.md`:1268 "rests on the input-only clm-lv3uw1").

### 2c. 2026-06-02 Grant-adjudicated dual-branch table (`dual-reactance-storage-taxonomy.md`:193-206)
| Branch | Saturates | Z, Γ | Sector | Outcome |
|---|---|---|---|---|
| **Electric** | $\varepsilon_{eff}\to0$ (μ intact) | $Z\to\infty$, Γ→+1, open | **X_C** (capacitive/transl-E) | **τ_yield** (dielectric breakdown) |
| **Magnetic** | $\mu_{eff}\to0$ (ε intact) | $Z\to0$, Γ→−1, short | **X_L** (inductive/microrot-B) | **rest mass** (Fermion confinement), clm-lv3uw1 |

Claims branch↔sector is "**canonical, not asserted**" via `translation-circuit.md`:464,526.

### 2d. ⚠ DIRECT CONTRADICTION (the heart of the fork)
- **Taxonomy (2c):** the **capacitive/X_C** sector saturating → $\varepsilon_{eff}\to0$ → **Z→∞** → τ_yield/rupture (NOT the electron wall).
- **`resonant-lc-solitons.md`:29-46:** the **capacitive** sector saturating → $C_{eff}\to\infty$ → **Z→0** → the electron wall (Γ=−1).

Same dielectric sector, **opposite** impedance limit. The pivot is the INVARIANT-S2 specialization $C_{eff}=C_0/S\;(\uparrow\infty)$ **vs** $\varepsilon_{eff}=\varepsilon_0 S\;(\downarrow0)$ — C and ε move *oppositely* in the AVE kernel, so "dielectric sector saturates" gives Z→0 in the C-form and Z→∞ in the ε-form. `cvr-dc-operating-point.md`:57 acknowledges the convention pair but sidesteps it by using the convention-independent $Z=Z_0\sqrt{S}$ form — which is exactly what makes the attribution degenerate.

### 2e. 2026-06-13 candidate gauge-dissolution (MOST RECENT; `cvr-reflection-smith.md`:67)
> "the apparent $\mu_{eff}\to0$-vs-$C_{eff}\to\infty$ split is **partly the two gauge sides of one wall** ($Z\to0$ inside ↔ $Z\to\infty$ outside, Möbius $Z\leftrightarrow1/Z$, $|\Gamma|=1$) — **not a physical branch.** The physical, gauge-invariant axis is the **two-'3's** (mass-dilatation ⊥ charge-winding; `master-equation.md`:20)."

→ The corpus already proposes the fork **largely reduces to the A1-vs-T2 / two-"3"s question**, with the Z→0/Z→∞ μ-vs-C distinction substantially a **gauge** (inside/outside Möbius) artifact. "**Partly**" = NOT a complete dissolution; a genuine sector residue remains. Consistent with memory `project_electron_two_threes_vortex_ring` (SECTOR⊥GAUGE advance).

**Working thesis (to verify, not assume):** the magnetic-vs-capacitive *impedance* fork is **not an independent physical branch** — the equilibrium observable is degenerate, the Z→0/∞ sign is gauge (Möbius inside/outside), and the genuine physical content is the **A1(ε/dilatation/mass-"3") vs T2(μ/microrotation/charge-"3") sector** question: *does the electron's confining excitation load the ε-sector (a STATIC dilatational twist — INVARIANT-S2: a static field has no ∂B/∂t, loads ε-only) or the μ-sector (a circulating winding current)?* INVARIANT-S2's static-field rule leans **ε/capacitive/A1**; `clm-lv3uw1` asserts **magnetic/T2 PRIMARY**. These conflict — the live flag.

---

## 3. MODE / REGIME / PHASE-STATE declaration (ave-regime-phase-state-check)

Declared before any run, per discipline:
- **MODE:** longitudinal-bulk dielectric (ε / A1 / capacitive `X_C`) **and** microrotational inductive (μ / T2 / `X_L`) saturation at the soliton **core/wall**. NOT EM-transverse propagation. The observable is a **boundary impedance** (Γ at the core↔ambient interface), rendered as a boundary condition (Op17-bounded), not a bulk force term (substrate-native-check CP10).
- **REGIME:** **near-yield / saturating** ($S\to0$, $A\to A_{yield}$). The wall exists only at saturation; linear-regime statements are off-target. Two sub-regimes matter and must be kept distinct: (i) the **formation transient** (which reactance's kernel argument reaches 1 *first* as the soliton assembles) — the charter's discriminator; (ii) the **formed operating point** ($A_\star\to1$, residual $\sqrt{S_\star}\approx\alpha/4$) — where Z is degenerate.
- **PHASE-STATE:** forming → formed **bound resonator** (a confined soliton = the electron). Bound-resonator-class, not free-propagating. Q baked in as $Q_e=1/\alpha$ at the operating point.

---

## 4. Discriminator design (substrate-native, NON-degenerate)

The equilibrium Z curve is degenerate (§2a). Candidate discriminators that are NOT degenerate:
1. **Formation-order (engine):** instrument whether $C_{eff}(V)$ [varactor] or $L_{eff}(I)$ [varinductor] (`cosserat_field_3d.py`:411-413) reaches its kernel argument = 1 **first** as a soliton forms on `crystal_engine` / `master_equation_fdtd` (the A1-cage's engine home — harness lacks the cage, per index 2026-06-13 addendum). Requires the engine to evolve BOTH reactances independently (S_μ, S_ε tracks) — VERIFY it does.
2. **Energy-sector / static-loading (analytical):** which sector does the electron's *defining* excitation load? The static topological twist (charge="3", winding) — does it load ε-only (INVARIANT-S2 static-field rule → A1/capacitive) or drive a circulating current → μ (T2/magnetic)? Virial says E_C = E_L = ½m_ec² at equilibrium (degenerate on energy *partition*), so the discriminator is FORMATION-order / which-saturates-first, not equilibrium energy.
3. **Gauge vs physical test:** is the μ↔C, Z↔1/Z, Γ-sign distinction a Möbius gauge pair (one wall, two frames) or two physically distinct walls? If gauge → the fork dissolves into the two-"3"s axis (the 2026-06-13 thesis).

**Adjudication rule:** branch reaching Z→0 first AND stably confining = wall mechanism. Degenerate/co-saturating / gauge-dual → report degeneracy + relocate to the A1-vs-T2 axis.

---

## 5. Arc plan (phases)

- **Phase 1 — corpus map + prereg** ✅ DONE (workflow `wf_c8a6cb2d-a99`, 10 agents): see §8. Prereg FROZEN at [`research/2026-06-15_wall-branch-fork_prereg_FROZEN.md`](../research/2026-06-15_wall-branch-fork_prereg_FROZEN.md).
- **Phase 2 — auditor-gate** ✅ DONE: ave-auditor PASS-WITH-AMENDMENTS (A1–A6 applied). See §9.
- **Phase 3 — driver:** the analytical/corpus-map workflow IS the driver (§6 of prereg). A fresh engine driver NOT run — justified (degenerate/assumption-baked engines). See §9.
- **Phase 4 — result + adjudicate to Grant** ✅ DONE: [`result`](../research/2026-06-15_wall-branch-fork_result.md). Flag to Grant = §6. Arc COMPLETE.

## 6. Open questions for Grant (flag-don't-fix — populated from Phase 1)

1. **Ratify the verdict: B3 DEGENERATE.** The magnetic-vs-capacitive fork is NOT a substrate-forced independent branch — at trace-free K=2G the ε and μ sectors CO-SATURATE (A-034:14); the asymmetry is a **chirality-set SIGN/spin selector** (μ-first→Γ−1, ε-first→Γ+1; `l3-synthesis`:144), not a derived branch. Accept B3? Or do you read a substrate-forced first-sector (B1/B2)?
2. **"Magnetic PRIMARY" is asserted, not derived** (clm-lv3uw1 0.50/0.32; cvr handoff "PRIMARY by mandate"). Recommend DEMOTING it from a quasi-derived claim to an explicit chirality-conventional sign-assignment. Agree?
3. **A1-vs-T2 knock-on:** mass=A1 is settled (ontology, `master-equation.md`:20). Since the wall is co-built (not uniquely T2/charge-winding), the fork does NOT independently decide "which 3 carries mass." Confirm the fork is mute on the mass-sector question (mass already A1), and the only live residue is the wall's chirality-SIGN.
4. **Two fixable corpus defects surfaced** (flag-don't-fix → your call whether this lane fixes them or spawns): (a) `resonant-lc-solitons.md`:38 derives the right Z→0 by a dimensionally-irregular capacitive route (μ₀-for-L) that contradicts the taxonomy's capacitive→Z→∞; (b) the impedance-operator ambiguity self-flagged at `vol1/claim-quality.md`:731 (Z→0 knot-core vs Z=Z₀-invariant SYM).

## 7. Verified-citation ledger (verify-before-cite)
| Claim | Source | Verified |
|---|---|---|
| Magnetic branch = wall (Z→0, Γ−1) | `master-equation.md`:85, clm-lv3uw1 | ✅ 2026-06-15 read |
| ε-rupture = Z→∞ (third config) | `master-equation.md`:84 | ✅ |
| Capacitive branch = wall (C_eff→∞, Z→0) | `resonant-lc-solitons.md`:29-46 | ✅ |
| FLAG-2 / Z=Z₀√S degenerate / magnetic PRIMARY | `cvr-dc-operating-point.md`:55 | ✅ |
| 2026-06-02 dual-branch table | `dual-reactance-storage-taxonomy.md`:193-206 | ✅ |
| 2026-06-13 gauge recontextualization | `cvr-reflection-smith.md`:67 | ✅ |
| varactor C_eff + varinductor L_eff (two reactances) | `cosserat_field_3d.py`:411-413 | ✅ |
| branch↔sector "canonical" | `translation-circuit.md`:**491** (NOT :464/:526 = table separators) | ✅ APPLIED back-cite to clm-lv3uw1, not derived; "canonical, not asserted" lives in `dual-reactance-storage-taxonomy.md`:198, self-classed Class-B near-definitional (:219-223) |
| Möbius gauge pair | `trampoline-framework.md`:**643** (cited :641 §6.1; heading reads §4.1) | ✅ rigorous BUT for INSIDE/OUTSIDE Γ-sign axis, ORTHOGONAL to μ-vs-C route axis; does NOT dissolve formation-order residue |
| L3 originating adjudication (μ-first, chirality-set) | `_archive/L3_electron_soliton/54_*`:167,199,250; `A-034`:14 | ✅ |
| trace-free K=2G locks ε↔μ (co-saturate) | `A-034`:14; `crystal_engine` single-kernel | ✅ |
| crystal_engine = single symmetric kernel (no μ/ε split) | `crystal_engine.py`:18-20,191-200 | ✅ |
| Cosserat μ-first = hand-set by (1±κh) sign | `cosserat_field_3d.py`:522-530 | ✅ |
| NO varinductor L_eff(I) in executed code | grep L_eff/varinductor/I_max = ∅ | ✅ comment-only at `cosserat_field_3d.py`:411-413 |
| impedance-operator ambiguity self-flag | `vol1/claim-quality.md`:731 | ✅ |

## 8. Phase-1 synthesis (verified; workflow `wf_c8a6cb2d-a99`, 10 agents, verbatim-grounded)

**The fork is NOT an independent substrate-forced physical branch.** Layers, none yielding a unique sector:
1. **DEGENERATE on the equilibrium observables (Z, |Γ|)** (Z=Z₀√S, |Γ|=1 both ways; FLAG-2 + `cvr_model.py`:146 "SAME trajectory — only the moved parameter differs"). The non-equilibrium residues — Γ-sign, formation-order, non-reciprocity — are what a discriminator targets; the equilibrium-Z discriminator is dead by construction. [A1/A6]
2. **Substrate DEFAULT = symmetric co-saturation — but that is the GRAVITY NULL, not the wall** (corrected 2026-06-15 post-Grant; earlier "co-built" framing was imprecise). Symmetric `S_μ=S_ε` → `Z=Z₀√(S_μ/S_ε)=Z₀` invariant, Γ=0 = impedance-matched gravity lens, does NOT confine (`A-034`:14; `l3-synthesis`:144). **The `Z→0` wall REQUIRES the chirality-broken asymmetry** — "degenerate" = neither sector substrate-privileged absent a chirality convention (spin-conjugate pair), NOT a co-built single wall.
3. **The asymmetry (which-first) is a CHIRALITY-SET SIGN/SPIN selector, not a derived branch.** μ-first→Γ=−1 (one chirality); ε-first→Γ=+1 (conjugate). Canonical electron conventionally μ-first but **asserted-not-derived** (clm-lv3uw1 confidence 0.65 / solidity 0.50 / rest-mass-mechanism 0.32 [A3]; clm-5fu303 0.45; cvr "PRIMARY by mandate"; `54_*`:250 "either sector CAN fire first… chirality picks which").
4. **Pre-thesis "static-loading→capacitive" REFUTED** — ε-only static state is the Z→∞ rupture branch, not confinement; soliton rings (∂B/∂t present), static premise fails. (Phase-0 anchoring caught by the adversarial gate.)
5. **Engine cannot independently resolve it** — `crystal_engine` single-kernel/degenerate; Cosserat magnetic-first **hand-assigned by (1±κh) sign**; no temporal first-cross observer. An engine driver reconstructs an assumption-baked/degenerate path. NOT warranted.
6. **Live corpus tensions** (flag-don't-fix): `resonant-lc-solitons.md`:38 capacitive-route defect (μ₀-for-L, contradicts taxonomy); impedance-operator ambiguity (`vol1/claim-quality.md`:731).

**Adversarial verdicts** (auditor-assessed confidence, NOT claim-quality solidity [A5]): contradiction-real = CONFIRMED-REAL (high); gauge-dissolution = PARTIAL (high, formation-order residue survives); static-loading = REFUTED-RECONCILED (high).

**Knock-on to A1-vs-T2** [A2 — mass=A1 is the independent premise, not derived from "co-built"]: mass=A1 SETTLED *independently* by ontology (`master-equation.md`:20, Grant-ratified; the `electron-identification.md`:121-125 open flag is citation-wording, NOT the mass-sector). Therefore the wall-formation-order fork CANNOT re-assign the mass sector — mass is A1; the wall *confines* it, does not *constitute* it. Under B3 the wall is co-built, so there's no unique wall-sector to identify with mass anyway. Only live residue = wall's **chirality-SIGN** (which sector chirality amplifies = spin). "Magnetic PRIMARY" IF ratified ⇒ T2/charge-winding builds the sign-−1 wall confining the A1/mass — a labeling default, not derived.

---

## 9. Phase-2 auditor-gate + Phase-4 result (DONE)

**Auditor-gate (ave-auditor, independent):** **PASS-WITH-AMENDMENTS.** All load-bearing pillars of B3 confirmed verbatim; six framing/precision amendments (A1–A6), none flips the verdict. Notable catch: the `electron-identification.md`:121-125 open flag is citation-wording (not mass-sector) → mass=A1 genuinely settled (strengthens the knock-on). A1–A6 applied to the result doc + this §8.

**Result doc:** [`research/2026-06-15_wall-branch-fork_result.md`](../research/2026-06-15_wall-branch-fork_result.md) — verdict B3 + flag-don't-fix recommendation to Grant. Arc COMPLETE; awaiting Grant ratification + PR review (Grant merges).

> NOTE on line-number drift: claim-quality/taxonomy cite `master-equation.md`:78-79,81 for the branch text; the live `.md` carries it at :84-87. Content verified; cite the live `.md` lines.

---

## 10. Grant rulings applied (2026-06-15) + cross-lane handoff

**Grant ratified** B3 + the demotion + mute-on-mass-sector + "fix the 2 defects in-lane." Applied:
- **Dimensional bug FIXED** — `resonant-lc-solitons.md`:35-39 broken `√(μ₀/C_eff)` → canonical convention-independent `Z₀√S`.
- **"Magnetic PRIMARY" DEMOTED** to chirality-conventional SIGN at the FLAG-2 sites (`cvr-dc-operating-point.md`:55, `resonant-lc-solitons.md`:98) + scope-pointer on clm-lv3uw1 (`vol1/claim-quality.md`).
- **Mechanism corrected** (mine): "co-built" → chirality-broken asymmetry; symmetric co-saturation = gravity `Z=Z₀` null, NOT the wall. Verdict B3 unchanged; cleaner.

**Two verify-before-cite catches (re-reading the actual sites before editing):**
1. **Defect #2 was ALREADY RESOLVED** — the impedance-operator ambiguity (`vol1/claim-quality.md`:731) carries a "RESOLVED (2026-06-06 doc-reconcile)" strengthen-by at `:734` (disambiguated by sector via `electron-bh-isomorphism.md`:23-34). Phase-1 flagged the stale *rationale prose*, not a live defect. NOT re-fixed.
2. **DEEPER ROOT flagged to Grant** — the dimensional bug is the tip of an INVARIANT-S2 inconsistency: `C_eff=C₀/S` (↑) while `ε_eff=ε₀S` (↓) is **inverse monotonicity** (violates `C∝ε`), which is *why* the ε-route reads `Z→0` (C-form) vs `Z→∞` (ε-form). A μ₀→L cosmetic fix would paper over it; routed through `Z₀√S` instead + flagged.

**Provenance≠state reconciliation (Grant):** Lane-3 "mute on sector" (state = A1, `master-equation.md`:20) and Lane-2 "live flag" (provenance = T2, `cosserat-mass-gap.md`:108) are two frames of one hybrid mode — not a contradiction.

**Cross-lane handoff → Lane 2 (eigenmode):** this lane fixes Lane-2's operating point. Lane 2 should impose the **chirality-signed winding as the odd-drive BC** at the **K=2G-locked** point and solve for the dissipationless stable hybrid (V,ω) mode, then **measure its radiative Q** (= 1/α — NOT solve for Q=∞/lossless, the α=0 decoupled false-negative). (Per Grant's tri-lane synthesis: Lane 3 sets the point, Lane 2 measures Q=1/α, Lane 1 derives it — **but see §11: Grant 2026-06-15b corrected the geometric leg; the α-chord is most likely CLOSING AS AN ECHO, so the keystone is Lane-2's eigenmode EXISTENCE, not Q-agreement.**)

---

## 11. Grant ratification (2026-06-15b) + triangulation correction

**Lane 3 RATIFIED, closed.** Grant: the co-saturation=gravity / chirality-broken=matter-wall sharpening is correct and load-bearing.

**RECORDED (Grant: "record it") — K=2G IS the symmetric/gravity-lock operating point.** Symmetric co-saturation = the gravity lens (Z=Z₀, Γ=0); **matter is the chirality-broken excitation that breaks the lock** (Z→0, Γ=−1). So the triangulation's operating point IS the gravity (symmetric) lock, and matter breaks it. **Knock-on:** K=2G's provenance is **α-downstream** (`dual-reactance-storage-taxonomy.md`:62-67: "downstream consistency the lattice sits at *given* α, NOT the driver of α") → the operating-point anchor is itself α-circular, which **reinforces α=echo**.

**Triangulation correction (Grant owns it; I walk back my recorded version).** My §10 "Lane-1 derives Q=1/α=137 from geometry → agreement = chord" was OVERSTATED (inherited from the earlier tri-lane synthesis). Grant's grounding: z₀=52=4·13 is a **multiplicative path-product**, not an additive Maxwell–Calladine constraint count (honest crystalline count ≈ 4+12 = 16 → 1/α≈49, **not** 137); the "1.46%→137" rode the 8πα identity (α-circular). **The z₀/coordination route to α is CLOSED as an ECHO.** This re-confirms `[[project_alpha_keystone_echo_resolved]]` (α=ECHO at value level, scale forced) from the electron-operating-point angle: **chord = FORM** (hybrid-eigenmode existence + chirality-signed wall + gravity-lock operating point), **echo = VALUE** (α=137).

**Lane-3 → Lane-2 pre-flight discriminator (refinement of the handoff).** Lane 3 confirmed wall = **magnetic** branch (S_μ→0 leads → Z→0, Γ→−1); symmetric = gravity (Z=Z₀, Γ=0, NO wall); electric = rupture (S_ε→0 → Z→∞, Γ→+1). So Lane-2's platform pre-flight must verify Op14 drives the projected scalar to the **inductive/magnetic short** (S_μ→0 leads, Z→0, Γ→−1) on the sech — discriminator: **sign of (S_ε−S_μ) > 0 at the wall**. If it only reaches the capacitive/softening **open** (Z→∞), it is clamping the WRONG wall → escalate; do NOT take the cross-firewall (b) sign-off.

**Two future-lane candidates registered (flag-don't-fix; Grant's calls 4 + the C-flag):**
- **(C-flag)** `C_eff=C₀/S`(↑) vs `ε_eff=ε₀S`(↓) inverse-monotonicity (INVARIANT-S2) — compliance-softening picture or sign error? Roots the whole Z→0-vs-Z→∞ contradiction. Small future lane.
- **(K=2G provenance)** crystalline (α-free) re-derivation of K=2G — tests whether the operating-point anchor is α-free (chord) or α-circular (echo). **Recommend YES**, pre-registered to likely land ECHO (taxonomy:62-67 already flags K=2G as α-downstream); value = settling whether ANY triangulation leg is α-free.
