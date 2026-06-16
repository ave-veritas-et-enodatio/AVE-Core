# RESULT — Wall-Branch Fork (H3): the electron's Γ=−1 wall is NOT an independent magnetic-vs-capacitive branch

**Date:** 2026-06-15 · **Lane:** `analysis/2026-06-15-wall-branch-fork` · **Prereg:** [`2026-06-15_wall-branch-fork_prereg_FROZEN.md`](2026-06-15_wall-branch-fork_prereg_FROZEN.md) (frozen `559343e1`) · **Orchestration:** [`_orchestration/2026-06-15_wall-branch-fork.md`](../_orchestration/2026-06-15_wall-branch-fork.md) · **Auditor-gate:** PASS-WITH-AMENDMENTS (A1–A6 applied below).

---

## Verdict: **B3 DEGENERATE** (chirality-set sign residue)

The question "which saturation branch forms the electron's Γ=−1 confining wall — MAGNETIC (μ_eff→0) or CAPACITIVE (C_eff→∞)?" has a **structured, substrate-native answer that is neither cleanly magnetic nor cleanly capacitive**:

1. **The two branches are degenerate on the equilibrium observables (Z, |Γ|).** Both give $Z=Z_0\sqrt{S}$ and $|\Gamma|=1$. [`cvr-dc-operating-point.md`:55; `cvr_model.py`:146 "SAME trajectory — only the moved parameter differs."] The non-equilibrium residues — Γ-**sign**, formation-**order**, **non-reciprocity** (`H_chiral`, `cvr_model.py`:225-258) — are exactly what a discriminator must target; the *equilibrium impedance* cannot. (Amendment A1.)

2. **The substrate default is symmetric CO-SATURATION — but that default is the gravity NULL, not the wall.** At the trace-free condition the kernel acts symmetrically on ε and μ — *"both saturate at the same A value, locked by the trace-free condition"* [`A-034`:14]. Symmetric co-saturation gives $Z=Z_0\sqrt{S_\mu/S_\varepsilon}=Z_0$ **invariant**, $\Gamma=0$ — the impedance-matched **gravity lens**, which does NOT confine. **The electron's $Z\to0$ wall therefore REQUIRES the chirality-broken asymmetry** ($S_\mu\neq S_\varepsilon$); "degenerate" means neither sector is substrate-privileged absent a chirality convention — they are the spin-conjugate pair, not a co-built single wall. (Qualifier per A4: K=2G is a *downstream consistency* the lattice *sits at* given α — `dual-reactance-storage-taxonomy.md`:62-67 — operating-point-true, not axiom-forced. Correction noted 2026-06-15 post-Grant: the earlier "co-saturation builds the wall / co-built" framing was imprecise — co-saturation is the gravity null; the wall is intrinsically the asymmetric case.)

3. **The magnetic-vs-capacitive asymmetry is a CHIRALITY-SET SIGN/SPIN selector, not a derived physical branch.** A chirality bias (Beltrami helicity $h\neq0$) breaks the lock; *which* sector then saturates first is the SIGN selection: μ-first → Γ=−1 (short); ε-first → Γ=+1 (open). **Both walls are totally reflecting (|Γ|=1); only the sign differs, and the sign encodes the spin/chirality direction** [`l3-synthesis`:142-144; `54_pair_production`:199,250 "either sector CAN fire first… chirality picks which"]. The canonical electron is *conventionally* assigned μ-first (magnetic), but this is an **asserted labeling default, not a derivation** — clm-lv3uw1 **confidence 0.65 / solidity 0.50 / rest-mass-mechanism 0.32**, its rationale verbatim "asserted-not-derived" [`vol1/claim-quality.md`:276-280]; the cvr workstream carried it as "HANDOFF-MANDATED PRIMARY" [`2026-06-13_cvr-ee-sweep-doc.md`:59]; the preferential-saturation axis clm-5fu303 (confidence/solidity 0.45) "explicitly disclaims" deriving why ε or μ saturates first. (Amendment A3.)

4. **No engine can independently resolve the fork** — and a fresh driver is therefore not warranted. `crystal_engine` (the electron's designated bulk-trap) confines via a **single symmetric scalar kernel** with no μ/ε split [`crystal_engine.py`:18-20,191-200] — degenerate by construction. The Cosserat coupled engine's "magnetic-first" is **hand-assigned by the (1±κ_chiral·h) sign convention** [`cosserat_field_3d.py`:519-523, sourced to `54_*`:218-219] — it reads back its own input. No observer records the temporal first-cross of S_μ vs S_ε. An engine instrumentation would reconstruct an assumption-baked or degenerate path (substrate-native-check CP9; pre-test-physics-check Trigger 7/8).

### What the fork is NOT
- **NOT cleanly magnetic** (the corpus "magnetic PRIMARY" is an asserted convention, and the bulk-trap engine that actually hosts the electron confines capacitively/A1 by a single kernel).
- **NOT cleanly capacitive** (the static-loading argument that would point there is refuted — see below).
- **NOT fully gauge** (B4 fails): the Möbius Z↔1/Z map is rigorous but identifies the INSIDE(Z→0,Γ−1)/OUTSIDE(Z→∞,Γ+1) frames of *one* wall — an axis **orthogonal** to the μ-vs-C route axis (both μ→0 and C→∞ give the same *inside* Z→0). A real, frame-invariant formation-order residue survives the gauge argument [verify:gauge-dissolution = PARTIAL, auditor-assessed high]. (Amendment A5: "high" = auditor/adversarial-reader confidence, not a claim-quality solidity.)

---

## The pre-registered prediction that was REFUTED (honest scoring)

The pre-thesis (committed `945acb66`, before the corpus-map workflow) predicted INVARIANT-S2's static-field rule would point the wall toward **capacitive/ε/A1**. **This was refuted** by the adversarial gate [verify:static-loading-rule = REFUTED-RECONCILED, auditor-assessed high]:
- The ε-only static-asymmetric state (ε_eff→0, S_ε<1, S_μ=1) the argument derives is the **Z→∞ dielectric-rupture branch** [`master-equation.md`:84], NOT confinement. Static-loading lands the electron on the *rupture* branch and mislabels it mass.
- The static premise fails anyway: the soliton is a *ringing* LC tank with peak inductive energy ½L_e I_max² = ½m_ec² [`resonant-lc-solitons.md`:23] — a circulating current ⇒ ∂B/∂t ⇒ μ-loading. "No ∂B/∂t" is false for a self-resonant soliton; INVARIANT-S2's static rule is scoped to genuine static-E drives (Op14 mirror bench, PONDER-05 quartz).

Recording the refutation per prereg hygiene: the right answer (B3) is symmetric co-saturation, not the predicted ε-lean.

---

## Knock-on to the A1-vs-T2 mass-sector fork (the charter deliverable)

(Amendment A2 — argument ordered so mass=A1 is the independent premise, not derived from "co-built.")

- **Mass = A1 is SETTLED, independently of this fork** (ontology, Grant-ratified): "the electron is the unknot dilatation-mass *carrying* the (2,3) winding — two objects, not one" [`master-equation.md`:20]; the A1 standing-V is the state/order-parameter and the (2,3) winding (charge, T2) rides it [`photon-identification.md`:11-17]. The open Grant-flag at `electron-identification.md`:121-125 is a **citation-wording** issue (what "longitudinal" denotes), **not** a mass-sector question — it does not reopen mass=A1.
- **Therefore the wall-formation-order fork, whatever its verdict, cannot re-assign the mass sector.** Mass is A1 by ontology; the wall *confines* the A1 mass, it does not *constitute* it. Under B3 the wall's sector is the chirality-broken **spin-sign**, not a mass-carrier — so there is no wall-sector to identify with mass anyway.
- **Provenance≠state (Grant's refinement):** the apparent Lane-2/Lane-3 "disagreement" on the mass sector dissolves — **provenance = T2** (`cosserat-mass-gap.md`:108, the photon-origin/charge-winding leaf) and **state = A1** (`master-equation.md`:20, the rest-mass). Both unretracted, both right *in their frame*: the hybrid (V,ω) mode's rest energy sits on the A1 state; the T2 leaf is its provenance. Not a contradiction — two frames of one mode. Lane-3's "mute on sector" (the *state* is A1) and Lane-2's "live flag" (the *provenance* is T2) are both correct.
- **Net:** this fork is **mute on "which 3 carries the mass"** (already A1). Its only live residue is the wall's **chirality-SIGN** — which sector the chirality bias amplifies = the electron's spin/handedness. IF Grant ratifies "magnetic PRIMARY," it means the T2/charge-winding sector forms the (sign-−1) wall that confines the A1/mass — but that is a chirality-conventional labeling choice, not a derivation, and it does not touch the settled mass=A1.

---

## Live corpus tensions surfaced (flag-don't-fix; not fixed in this lane)

1. **`resonant-lc-solitons.md`:38 capacitive-route derivation defect.** It reaches the correct Z→0/Γ=−1 wall but via $Z_{core}=\sqrt{\mu_0/C_{eff}}$ — dimensionally irregular (μ₀ substituted for L; μ₀ is inductance-*per-length*) and attributing the wall to the capacitive sector, contradicting the taxonomy's capacitive→Z→∞ [`dual-reactance-storage-taxonomy.md`:195]. The leaf already flags the attribution PROVISIONAL (`:98`).
2. **Impedance-operator ambiguity self-flagged at `vol1/claim-quality.md`:731** — Vol-1 says Z→0 at the saturated knot core; Vol-3 SYM leaves say Z=Z₀ invariant. "Currently ambiguous across leaves."
3. **Stale line-pins** (verify-before-cite repair queue): `cvr-dc-operating-point.md`:55 cites `master-equation.md`:78-79 (clm marker is :85); `cvr-reflection-smith.md`:67 cites trampoline "§6.1" = line 643 under heading §4.1; `translation-circuit.md` :464/:526 are table separators (content at :491). All resolve via clm-ids. (Amendment A6: the synthesis's `cvr_model.py:144` quote is at `:146`.)

---

## Recommendation to Grant (flag-don't-fix — you decide; nothing edited)

1. **Ratify B3 DEGENERATE** — the magnetic-vs-capacitive wall is the chirality-broken asymmetric case (symmetric co-saturation is the gravity $Z=Z_0$ null, not the wall), with the μ-vs-ε choice a chirality-set SIGN/spin selector, not an independent substrate-forced branch.
2. **Demote "magnetic PRIMARY"** from a quasi-derived claim to an explicit chirality-conventional sign-assignment (it is asserted-not-derived: clm-lv3uw1 0.50 solidity, "HANDOFF-MANDATED").
3. **Accept the A1-vs-T2 knock-on:** mass=A1 is already settled; this fork is mute on the mass sector and only fixes the wall's spin-sign.
4. **Queue the two fixable corpus defects** (resonant-lc-solitons:38 route; impedance-operator ambiguity vol1/cq:731) — fix in this lane, or spawn.

**Plumber's one-liner:** when both windings stiffen *together* the cell stays impedance-matched (`Z=Z₀`) — that's gravity, no wall. The electron's short-circuit wall only appears when one winding (electric or magnetic) leads the other, and *which one leads* is the electron's handedness (spin). So "the magnetic wall" is just naming the lead winding for one spin — not a separate kind of wall. The mass it traps is the longitudinal compression (A1) either way.
