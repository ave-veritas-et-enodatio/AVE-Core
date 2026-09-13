# WALK RECORD — the sibling definition debt: one defect, two sector contents, two far-field read-outs (2026-09-13)

**Status: WALK-GRADE / DEFINITION-DEBT throughout. Nothing here is a claim, a ruling, or a
promotion.** Mints no `clm-` / `def-` / `exp-` / `sup-` / `ilk-`, moves no solidity, edits no KB
leaf, no manuscript file, no engine file. Grade stays WALK / DEFINITION-DEBT until the Claims
Gate says otherwise. No FACT promotion. No merge. No driven-G2 / existence-campaign stab
(fenced: [`2026-08-24-static-existence-epic-tracker`](../_orchestration/open-items/2026-08-24-static-existence-epic-tracker.md),
[`2026-08-25-g2-freeze-decisions`](../_orchestration/open-items/2026-08-25-g2-freeze-decisions.md)).
No Op16 form pick. No second force is invented, and A1 ⊥ T2 is not collapsed.

**Lane:** Lane A — physics advance (the lattice-free / sibling-far-fields north star). The
brief's primary notes (the Orchestrator-box tracker item **MATH-1**, "sibling definition debt +
deepdive excerpts") are **not in this repo**; this record pulls SoT from `manuscript/ave-kb/`
only. Distillates (this file included) are **indexes, not sources** — every physics statement
below points at a KB leaf line and carries that line's excerpt.

**Grep receipt (the debt's own name has no corpus home).** At `origin/main` @ `451bf480`
(2026-09-13): `sibling[ -]definition`, `definition[ -]debt`, `sibling[ -]far[ -]field`,
`lattice[ -]free` → **0 hits** each across `manuscript/`, `research/`, `_orchestration/`
(case-insensitive `grep -rn -E`, `*.md`/`*.tex`/`*.jsonl`). `port famil` / `two-port famil` /
`Link[–-]Γ` / `dilatation *→ *Z` → **0 hits** in the sense the brief uses (the only "two ports"
hits are the EM↔mechanical domain-boundary rows, e.g. `device-circuit-models.md:216`). So the
packaging below is the **first in-repo statement** of the split; it restates canon, it does
not derive.

---

## §0 — Sync receipt (do this first, per the brief)

| step | receipt |
|---|---|
| local `main` before | `5a36cea5` — `## main...origin/main [behind 2]`, working tree clean |
| `origin/main` | `451bf480` (merge of #1043, `cursor/regen-board-2026-09-13-5d9c`) |
| action | `git pull --ff-only origin main` → **fast-forwarded** `5a36cea5..451bf480`, one file (`_orchestration/BOARD.md`, +28/−5) |
| BOARD regen landed | `git log -1 --oneline -- _orchestration/BOARD.md` → `6afb54b8 chore: regenerate BOARD.md from current main` ✔ |
| working branch | `claude/lane-a-sibling-def-debt` off `451bf480` |
| shared-checkout collision (receipt) | reflog of the primary checkout: `08:59:24 checkout: moving from main to claude/lane-a-sibling-def-debt` (this lane) → `09:00:01 checkout: moving from claude/lane-a-sibling-def-debt to main` (**a concurrent session, not this lane**, 37 s later). The first commit attempt therefore ran on `main` and was **refused by the commit gate** (exit 1) — **nothing landed on `main`**; the staged file was unstaged and the lane moved to a dedicated worktree (`~/AVE-staging/wt-lane-a-sibling-def-debt`, same branch, same base). The documented shared-working-tree failure mode (`CLAUDE.md` §Pre-commit discipline), met live. |
| commit-gate note | the refusal was `research/drivers/r40_quote_claim_strength_number_check.py` — 26 violations, **all** inside three `.claude/worktrees/wf_*/` copies of the checker's own file nested in the primary checkout; the same checker run from the dedicated worktree (no nested copies) reports `0 violation(s)`. An environment false positive of the shared checkout, not a defect in this record; routed as hygiene (stale workflow worktrees under `.claude/worktrees/`). |

---

## §1 — Session receipt: leaves deep-read

All reads at `451bf480`. "Currency" = last commit touching the leaf (`git log -1 --format=%h %ad`).

| # | leaf (SoT) | lines read | what it carries for this debt | currency |
|---|---|---|---|---|
| L1 | [`boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) | full | the $\mathcal{M},\mathcal{Q},\mathcal{J}$ table; the T6 KEEP-BOTH note ("MASS (A1) ⊥ CHARGE/spin (T2) — never one phasor"); the observability rule; the four boundary registers | `00c33c29` 2026-08-06 |
| L2 | [`trampoline-framework.md`](../manuscript/ave-kb/common/trampoline-framework.md) | §5–§6 (`:512-706`) + headers | §5.3 gravity as propagated strain / impedance gradient; §4.3 invariants + the mass-sector scope-note | `ddf4f241` 2026-08-18 |
| L3 | [`master-equation.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md) | full | `:20` two-"3"s (A1 ⊥ T2); `:24` two rotation flavours; `:30-43` mass=A1 / flywheel=T2 / FOC-refuted / two clocks / G2 dissolution; `:115` SYM gravity preserves $Z_0$; `:121-193` R40 bound-response demotion + BIAS-DEBT | `8f75ca5e` 2026-08-12 |
| L4 | [`form-deriving-value-importing.md`](../manuscript/ave-kb/common/form-deriving-value-importing.md) | full | FORM/VALUE principle; the charge-flux row; the London "missing leg"; the AC/DC carve (`clm-acdc07`) and its DC-medium-state table | `c0c26ddd` 2026-08-10 |
| L5 | [`eq_axiom_5.tex`](../manuscript/common_equations/eq_axiom_5.tex) + [`axiom-register.md`](../manuscript/ave-kb/common/axiom-register.md) `:306-440` | full / §source-law | the Substrate DC Bias source law: clause S (deposit), G (bias↔bound response), Q (quiescence); the falsifier; what it forbids | register `2026-08-24` (R55) |
| L6 | [`vocabulary-register.md`](../manuscript/ave-kb/common/vocabulary-register.md) | `def-portmp` `:506-518`, `def-tk1xfm` `:434-452`, `def-1mpanl` `:938-950`, `def-q1escn` `:490-502`, `def-9a4f07` `:583-600`, `def-3638f2` `:241-256`, `def-69f472` `:160-172`, `def-cmdiff` `:1533-1549` | the proposed port↔DOF↔sector map (the closest existing object to a "port family"); the impedance-analogy sign convention; the common-mode MODE-vs-INFLUENCE hazard | `2e480851` 2026-08-25 |
| L7 | [`port-register.md`](../manuscript/ave-kb/common/port-register.md) | `:1-135` | the PORT definition (radiative iff $\mathrm{Re}\,Z>0$); channels-inherent / ports-emergent; P1 $R_{rad}\equiv Z_0$; P4 electron wall CLOSED; P9 near-field NOT-A-PORT; the R40 stamps on channel 3 / Q1 | `8f75ca5e` 2026-08-12 |
| L8 | [`resonant-lc-solitons.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) `:41,:116-130`; [`node-up-small-large-signal.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md) `:1-60` | targeted | the three-channel ROLES (carrier port / charge boundary / mass store); the §0 multi-port table across two domains | — |
| L9 | [`electron-identification.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md) | `:1-120` | "self-trapped" = boundary-condition sense; the three orthogonal identity labels; core vs far-field (D3 COEXIST); the three-way FORM/VALUE accounting | — |
| L10 | [`dual-reactance-storage-taxonomy.md`](../manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md) | full | `:221` $X_L$ = flywheel, NOT the rest-mass store; `:189` magnetic branch = sign-selector | — |
| L11 | [`k4-port-irrep-decomposition.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) `:1-45`; [`ponderomotive-equivalence.md`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md); [`refractive-index-of-gravity.md`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md) `:1-25`; [`gravitational-coupling-constant.md`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/gravitational-coupling-constant.md) `:1-25`; [`envelope-anatomy.md`](../manuscript/ave-kb/common/envelope-anatomy.md) `:50-90`; [`the-sourced-charge-no-go-cascade.md`](../manuscript/ave-kb/common/the-sourced-charge-no-go-cascade.md) `:140-160,:270-290`; [`newtonian-inertia-as-lenz.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md) `:1-16` | targeted | the $A_1\oplus T_2$ root and the G2 photon relabel; weight ≡ inertia; $n(r)$; $G$ form/value; far-field Hookean ladder + endpoint-vs-ledger; the charge framing fork; inertia-as-inductance (do-not-build) | — |
| L12 | open-items: [`sector-of-storage`](../_orchestration/open-items/2026-07-26-sector-of-storage.md), [`acdc-gravity-circuit-map`](../_orchestration/open-items/2026-08-29-acdc-gravity-circuit-map.md), [`terminal-charge-framing-fork`](../_orchestration/open-items/2026-07-03-terminal-charge-framing-fork.md), [`exterior-field-profile-derivation`](../_orchestration/open-items/2026-07-03-exterior-field-profile-derivation.md), [`axiom5-b-glyph`](../_orchestration/open-items/2026-08-24-axiom5-b-glyph.md), [`invariant-s2-sector-split`](../_orchestration/open-items/2026-08-25-invariant-s2-sector-split.md), [`ua-transverse-identity-collapse`](../_orchestration/open-items/2026-07-20-ua-transverse-identity-collapse.md), [`phase-space-tank-state`](../_orchestration/open-items/2026-08-29-phase-space-tank-state.md) | full | the live forks this packaging must not pre-empt | BOARD `451bf480` |
| L13 | context, NOT SoT: [`2026-08-29_picture-lock-spillover.md`](2026-08-29_picture-lock-spillover.md) (S2 signed / H1–H6 held); `research/2026-08-29_h1-dc-circuit-objects_WALK.md` **`[branch:#1034]`** (H1 CLOSES, three circuit objects KEEP-ALL — not on `main`); [`2026-08-10_bound-constitutive_result.md`](2026-08-10_bound-constitutive_result.md) `:96` (exterior uniqueness $u_0 = B\,\hat r/r^2$); [`2026-08-09-ruling-r38-bound-response.md`](../_orchestration/docket-entries/2026-08-09-ruling-r38-bound-response.md) `:14-16` | targeted | the most recent walks on the same A1/T2 join | — |

Solidity of every claim pinned below, read from the index (`kb_cmd show`, tool-computed, 2026-09-13):
`clm-ze4clw` 0.55 · `clm-ofys5v` 0.55 · `clm-sjjvhf` 0.55 · `clm-3bwhad` 0.55 · `clm-acdc07` 0.55 ·
`clm-rd9cjm` 0.55 · `clm-1klgo2` 0.55 · `clm-nogo4l` 0.55 · `clm-relcnc` 0.50 · `clm-efo113` 0.50 ·
`clm-lv3uw1` 0.50 · `clm-ppasym` 0.45 · `clm-wcoul2` 0.70 · `clm-4r4jiy` 0.70 · `clm-uatcql` 0.70 ·
`clm-j550uh` 0.85 · `clm-vca7r1` 0.85 · `clm-fy05jc` 0.85 · `clm-kezk9z` 0.90 · `clm-uu1qbo` 0.78 ·
`clm-jwyy6l` **0.30 do-not-build** · `clm-533gvm` **0.30 do-not-build** · `clm-9kd2t3` **0.42 do-not-build**.
Every input-only row (0.55 and below) is used here as **input only**; nothing is built deeper on it.

---

## §2 — Collisions found (each is a packaging hazard, none is fixed here)

**C1 — "one self-trapped medium stress" vs canon's "two objects, not one".**
[`master-equation.md:20`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)
— *"The electron is the unknot dilatation-mass **carrying** the `(2,3)` winding — two objects, not one."*
The brief's noun ("one stress") must not be read as one sector content. The reconciling canon is
the electron's three orthogonal identity labels,
[`electron-identification.md:53`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md)
— *"These three are orthogonal: real-space body ⊥ phase-space winding ⊥ mass dilatation. Charge and spin live on the Cosserat $(2,3)$ micro-rotation (the T₂ core, property 4); mass lives on A1. **Never cross-wire**"*.
So the honest noun is **one real-space defect** ($0_1$ unknot body, `:49` — *"the mass-bearing carrier body"*)
carrying **two sector contents**. "Self-trapped" is itself scoped: `:13` — *""self-trapped" must be read in its **boundary-condition** sense"*.

**C2 — "port family" collides with the register meaning of PORT, and the A1 slot has NO port.**
[`port-register.md:21`](../manuscript/ave-kb/common/port-register.md) — *"A port is **RADIATIVE iff $\mathrm{Re}(Z) > 0$** there"*; `:26` — *"If either fails, the port is **REACTIVE** ($\mathrm{Re}(Z) = 0$; stores-and-returns) or **CLOSED**."*
Canon for the mass side: [`master-equation.md:139-143`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)
— *"Under clause **G** the A1 / bulk slot is a **bound response** … with **no independent propagating branch, no port and zero longitudinal characteristic speed**."*;
[`2026-08-09-ruling-r38-bound-response.md:14-16`](../_orchestration/docket-entries/2026-08-09-ruling-r38-bound-response.md)
— *"**bound response field** (controlled-source class — the circuit-theory dependent source: no autonomy, no independent flux, no port; bound to the sectors that drive it)"*.
The only in-corpus object that uses "port" the way the brief does is the **proposed, gated**
[`def-portmp`](../manuscript/ave-kb/common/vocabulary-register.md) (`:513` — `- **status:** proposed`), whose own
ambiguity flag says (`:517`) — *"THIS map's "port" means a **sector/grade channel**, NOT the four K4 bond-ports nor a single-$\Gamma$ impedance boundary."*
→ the packaging must either qualify "port" in the def-portmp sense every time, or use **read-out family**.

**C3 — "Link–Γ" vs "dilatation→Z" names the two families by ONE Smith-chart object.**
$\Gamma$ and $Z$ are the same coordinate ($\Gamma=(Z-Z_0)/(Z+Z_0)$; the sign convention is pinned at
[`def-1mpanl`](../manuscript/ave-kb/common/vocabulary-register.md) `:942` — *"**$Z\to0$ = short = pressure-release / free boundary = $\Gamma=-1$**, and **$Z\to\infty$ = open = rigid / clamped boundary = $\Gamma=+1$**"*).
Labelling the families "Γ" and "Z" invites reading them onto one phasor — exactly the guard at
[`boundary-observables-m-q-j.md:25`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)
— *"**MASS (A1) $\perp$ CHARGE/spin (T2) — never one phasor** (def-portmp)"*.
Which $Z$? The mass family's $Z$ is the **mechanical** $Z_{\mathrm{bulk}}$ (Pa·s/m), not $Z_{\mathrm{EM}}$:
[`node-up-small-large-signal.md:51`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md)
— `| **MASS** — A1 dilatation | trace-of-translation … | longitudinal bond compliance $\to Z_{\mathrm{bulk}}$ |`, and `:57` — *"the MASS, CHARGE, and deviatoric-shear rows are **mechanical**"*.
On the EM channel the gravitational far field is **matched**:
[`master-equation.md:115`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)
— *"This produces a continuous refractive gradient radially outward while preserving $Z_0$."*;
[`translation-circuit.md:117`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md)
— `Concurrent $\varepsilon$ and $\mu$ modulation = isotropic gradient-index (impedance-matched, $\Gamma = 0$)`.
→ "dilatation→Z" is a $Z_{\mathrm{bulk}}$ **store** read through an **index / clock**, with $\Gamma_{\mathrm{EM}}=0$ — not a reflection.

**C4 — "charge/EM" bundles two rotation flavours, and the charge far field is not derived.**
[`master-equation.md:24`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)
— *"Two rotation-flavored fields, ONE name "micro-rotation": the mechanical ω is gapped and short-range; the EM-inductive B-rotation is massless and matched."*;
[`k4-port-irrep-decomposition.md:35`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md)
— *"what is relabeled is *which sector is the photon* — the massless transverse-$u$ pair at $c=\sqrt{G/\rho}$, not the $\omega$ sector"*.
The Link rides the gapped mechanical ω sector; the EM read-out rides the massless $T_2$ channel. Two open joints sit between them:
[`2026-07-03-exterior-field-profile-derivation`](../_orchestration/open-items/2026-07-03-exterior-field-profile-derivation.md) — *"the clean 1/r far-field that atoms require is **asserted, not derived**"* (status OPEN), and
[`2026-07-03-terminal-charge-framing-fork`](../_orchestration/open-items/2026-07-03-terminal-charge-framing-fork.md) — ROUTED-TO-GRANT; the fork verbatim at
[`the-sourced-charge-no-go-cascade.md:148-149`](../manuscript/ave-kb/common/the-sourced-charge-no-go-cascade.md)
— *"(is the electron's charge a net-`∇·E` monopole at all, or purely the far-field of a harmonic/winding holonomy?)"*.
Also the pair interaction the corpus HAS is screened: [`form-deriving-value-importing.md:589`](../manuscript/ave-kb/common/form-deriving-value-importing.md) — *"Yukawa screening ⇒ no source-free far-field"*.
→ the Link→Γ leg is canon at the **integer** and **open at the far-field profile**.

**C5 — "weight/inertia": inertia-as-inductance is a translation-image and its leaf is do-not-build.**
[`boundary-observables-m-q-j.md:25`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)
— *"The $\mathcal{M}$-row EE-projection "inductance $L$" is a TKI translation-image, NOT a sector-ownership claim"*;
[`newtonian-inertia-as-lenz.md:14`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/newtonian-inertia-as-lenz.md)
— *"STORED INDUCTIVE ENERGY = the FLYWHEEL (spin/frequency-regulation), the REST MASS *store* is A1"* (`clm-jwyy6l` 0.30, do-not-build);
[`dual-reactance-storage-taxonomy.md:221`](../manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md)
— *"$X_L$ = the FLYWHEEL (spin/frequency-regulation) sector, NOT the rest-mass store"*.
Weight ≡ inertia IS canon but in stale wording:
[`ponderomotive-equivalence.md:30`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md)
— *"guaranteeing that inertial mass and gravitational mass are identical ($m_i \equiv m_g$)"* (`clm-rd9cjm`), while `:14` still says *"its internal inductive rest mass ($m_i c^{2}$)"* — pre-2026-06-20 "inductive mass" wording that the mass = A1 ruling superseded. **Flag-don't-fix** (Rule-12 banner candidate for a hygiene lane).
→ "inertia" in this family must be pinned to the A1 near-field store / added-mass, never to $L$.

**C6 — the siblings are NOT symmetric: one is a deposited net flux by law, the other has no deposit.**
[`eq_axiom_5.tex:71`](../manuscript/common_equations/eq_axiom_5.tex) — `Mass is an enclosed compression charge BY LAW` and `Clause S is MECHANISM-AGNOSTIC`;
`:100` — *"any EM/winding-sector deposit (the four locks are untouched --- the A1 sector's transportability, not a new source, is what breaks the A1/EM symmetry)"* (in the forbids-block);
`:169-170` (EE-mapping comment) — `an electret's frozen state is a` / `DIPOLE (net-zero monopole), while clause S deposits a NET MONOPOLE flux`.
→ "sibling" can only mean *shared far-field FORM and shared Gauss-surface read*, never shared source mechanism.

**C7 — two clocks.** [`master-equation.md:38`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)
— *"the **time-dilation clock rides A1**, while the **spin/Larmor clock rides the T2 flywheel**"*. The inertia family's clock is the A1-Op14 clock; do not let it ride the flywheel.

**C8 — common-mode MODE vs common-mode INFLUENCE.** [`def-cmdiff`](../manuscript/ave-kb/common/vocabulary-register.md) `:1547`
— *"**Rule: never read a common-mode MODE as a common-mode INFLUENCE.** A1 is a sector (mass); the influence class is a gauge statement."*
The mass family IS the A1 common-mode **irrep** ([`k4-port-irrep-decomposition.md:10`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) — *"the $+1$ eigenvector is the $A_1$ "common mode" (all ports equal)"*) and it is read as a **differential** bias ([`translation-circuit.md:116`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) — `**Differential bias** — a bias gradient across the ladder (differential varactor operating points; the load-transfer / gravity-ledger direction)`). Both words are needed; keep them apart.

**C9 — cite-shifts met on the way (routed, not repaired).**
(a) [`2026-07-03-exterior-field-profile-derivation.md:11`](../_orchestration/open-items/2026-07-03-exterior-field-profile-derivation.md) cites `vol4/claim-quality.md:1311` for *"WHY topological strain equals ℓ_node/r …"*; at HEAD `:1311` reads `- strengthen-by:` and the sentence sits at **`:1552`**.
(b) `master-equation.md:24` cites `node-up-small-large-signal.md:39` for the MECHANICAL Cosserat → $Z_{\mathrm{shear}}$ reference; `:39` is blank at HEAD and the content is the `:52` CHARGE row. Inside a Rule-12 preserved body → auditor lane, not this one.
(c) `def-portmp` (`:514`, `:518`) cites `resonant-lc-solitons.md:118-125` for the three-channel roles; at HEAD the channel bullets are `:122-124` and the ROLE resultbox `:126-129`.
(d) **Stale-vs-R40:** [`def-9a4f07`](../manuscript/ave-kb/common/vocabulary-register.md) `:594` (sharpened 2026-08-07) still carries *"it is a propagating P-branch wave"*; the R40 sweep (2026-08-11) stamped this register's `:575,:727,:870,:891,:1069` and did **not** stamp `:594`. The clause is exactly the "P-branch-propagates" family R40 demoted ([`master-equation.md:178-188`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)). Flag for the R40 batch owner.

**C10 — in-flight overlap on the same join.** PR **#1034** (`analysis/2026-08-29-tank-state-h1-join`; H1 CLOSES — *"three circuit objects, not one mesh"*, KEEP-ALL, WALK-GRADE) and PR **#1033** (`research/2026-08-28-qpoint-constitutive`; ε₁₁ as A1 Q-point) work the circuit-object side of A1 ⊥ T2. Neither is on `main`. This record is the **far-field / observable side** of the same split; it pre-empts none of H2–H6 ([`2026-08-29_picture-lock-spillover.md:65-70`](2026-08-29_picture-lock-spillover.md)).

---

## §3 — Packaging draft: the owed split (WALK / DEFINITION-DEBT — restates canon, derives nothing)

> **One real-space defect. Two orthogonal sector contents (A1 ⊥ T2). Two far-field read-outs, each a surface integral over the same enclosing boundary, neither a shared phasor.**

**P0 — The object and what the far field can see.** The electron is one real-space defect — the
$0_1$ unknot body — self-trapped in the boundary-condition sense
([`electron-identification.md:13`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md) — *"the lattice self-creates a Γ=−1 **TIR mirror = a BOUNDARY**"*).
Its interior is not observable:
[`boundary-observables-m-q-j.md:37`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)
— *"**Only $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ are externally measurable.** Interior eigenmode wavelengths, microrotation profiles, soliton topology, and bond-stress distributions are invisible to the substrate."* (`clm-ofys5v`, input-only).
Whatever "the stress" is inside, the far field reads **boundary data** only — `:59` (electron-identification) — *"identity is topological boundary data, carried by the far-field projection."*

**P1 — Two sector contents, held at 90°.**
[`master-equation.md:33`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md)
— *"the substrate holds mass (A1) and spin/charge (T2) at $90°$ so they share no $(V_{inc}, V_{ref})$ phasor"*; `:36` — *"**A1 ⊥ T2 is the ratified GRADE orthogonality**"* … *"which is **FOC-INDEPENDENT**"*.
Group-theoretic root: [`k4-port-irrep-decomposition.md:10`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md) — `$V_{\text{4-port}} = A_1 \oplus T_2$` (`clm-j550uh` 0.85).

| | **Family A — weight / inertia (A1 dilatation)** | **Family B — charge / EM (T2 winding)** |
|---|---|---|
| **content** | rest-mass **store** = A1 longitudinal dilatation — [`master-equation.md:31`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md) *(grade-ASSIGNMENT, PR#260 — `"mass = A1" is RATIFIED-CONSISTENCY — the adjudicated grade-ASSIGNMENT (PR#260), **NOT driver-validated**`)*; the **work-doing reactive MASS STORE**, [`resonant-lc-solitons.md:129`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) | the **static Link integer** $\mathcal{Q}=\mathrm{Link}(\partial\Omega,\mathbf F)\in\mathbb Z$, [`boundary-observables-m-q-j.md:20`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) (`clm-ze4clw`); STATIC and reactive — [`def-3638f2`](../manuscript/ave-kb/common/vocabulary-register.md) `:256` *"the $(2,3)$ phase-space winding is **STATIC** (a deformation-invariant texture, NOT a dynamical/energetic time-orbit) and is the boundary linking integer"*; the **static reactive CHARGE BOUNDARY**, [`resonant-lc-solitons.md:128`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) |
| **source structure** | a **deposited net flux BY LAW** — [`eq_axiom_5.tex:68`](../manuscript/common_equations/eq_axiom_5.tex) `\oint_S \mathbf{u}\cdot\hat{\mathbf{n}} = 4\pi B(M)`; `:71` `Mass is an enclosed compression charge BY LAW` (mechanism-agnostic, genesis-deposited) | **no deposit** — `:100` *"any EM/winding-sector deposit"* is forbidden; the sourced-net-monopole route is CLOSED (`clm-nogo4l`); the far field is, on the strong lean, a **holonomy**, fork ROUTED (C4) |
| **domain / impedance** | **mechanical** $Z_{\mathrm{bulk}}$ ([`node-up-small-large-signal.md:51`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md)); at the cage $Z_{bulk}\to0\Rightarrow\Gamma_{bulk}=-1$ — [`bulk-impedance-at-saturation-boundary.md:76`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md) `| Bulk channel | $Z_{bulk} \to 0$ at TIR wall $\Rightarrow \Gamma_{bulk} = -1$ |` | **mechanical** $Z_{\mathrm{shear}}$ carries the Link ([`node-up-small-large-signal.md:52`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md)); the **EM** $Z_{\mathrm{EM}}\equiv Z_0$ is the read-out channel — [`resonant-lc-solitons.md:127`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md) `**$Z_{\mathrm{EM}}\equiv Z_0$ = the radiative CARRIER PORT**`; bridged only by the TKI transducer ([`def-tk1xfm`](../manuscript/ave-kb/common/vocabulary-register.md) `:438` *"identity-by-translation, NOT a derivation"*) |
| **far-field FORM (the 1/r sibling)** | the **bias** $\varepsilon_{11}=7GM/c^2 r$ — [`eq_axiom_5.tex:94`](../manuscript/common_equations/eq_axiom_5.tex) *"the canon bias profile $\varepsilon_{11} = 7GM/c^2 r$"*; source law [`gordon-optical-metric.md:25`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md) `-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)`; bound response $u_0=B\,\hat r/r^2$ ([`axiom-register.md:423`](../manuscript/ave-kb/common/axiom-register.md) `the exterior uniqueness of the bound response u₀ = B r̂/r²`); `:96` (eq_axiom_5) `the $1/r$ bias profile and the $1/r^2$ bound response are free geometry from the elliptic solve` | the **1/r Coulomb tail** — **asserted, not derived** ([`2026-07-03-exterior-field-profile-derivation`](../_orchestration/open-items/2026-07-03-exterior-field-profile-derivation.md)); only the integer and the sign of the pair leg are canon (`clm-wcoul2`, [`boundary-observables-m-q-j.md:27`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) *"like windings repel / unlike attract with Coulomb sign structure"*) |
| **read-out type** | **index / clock**, not reflection: $n(r)=1+2GM/c^2r$ ([`refractive-index-of-gravity.md:14`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md), `clm-rd9cjm`); *"impedance gradient, not geometric"* ([`boundary-observables-m-q-j.md:110`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md), `clm-3bwhad`); $\Gamma_{\mathrm{EM}}=0$ ([`master-equation.md:115`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md) *"preserving $Z_0$"*); the A1-Op14 clock ([`op14-local-clock-modulation.md:11`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md) *"it **modulates the local clock rate**"*); a **differential** read of DC ([`2026-08-29_picture-lock-spillover.md:61`](2026-08-29_picture-lock-spillover.md), Grant-signed — *"Gravity-as-interaction is a **differential** of that DC, read by AC probes."*); **no port** (bound response, C2) | **reflection / interaction** on the EM channel — the matched radiative port $R_{rad}\equiv Z_0$ ([`port-register.md:69`](../manuscript/ave-kb/common/port-register.md)) and the Ax-2 interaction leg; the read-out of a **DC topology** through an AC channel ([`form-deriving-value-importing.md:296-297`](../manuscript/ave-kb/common/form-deriving-value-importing.md) — *"**every AVE-distinct observable is an AC reading of a DC gradient or topology**"*) |
| **path structure** | **ledger** (volume integral, unscreened) — [`envelope-anatomy.md:71`](../manuscript/ave-kb/common/envelope-anatomy.md) `**Gravity = LEDGER physics (a volume integral).**` (`clm-ppasym` 0.45) | **endpoint** (boundary integral, collar) — `:70` `**EM correction = ENDPOINT physics (a boundary integral).**` |
| **FORM / VALUE** | FORM derived, VALUE imported: $G$ MIXED — [`gravitational-coupling-constant.md:10`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/gravitational-coupling-constant.md) *"$G = c^4/(7\xi T_{EM})$ is **form**-derived … but its **value** is a calibration input"*; $\mathcal{A}_g$ UNVALUED (eq_axiom_5 `:96`) | FORM derived, VALUE imported: [`form-deriving-value-importing.md:90`](../manuscript/ave-kb/common/form-deriving-value-importing.md) — the Link integer, holonomy, linking-DOF and neutrality *"are ALL FORM-derived"*; the flux-per-Link quantum rides $\xi_{topo}$ — **[DOORWAY-NO-PINNING]**; `:192` *"the integer never becomes a pinned flux **VALUE**"* |
| **weight ≡ inertia** | derived via the /7 projection — [`ponderomotive-equivalence.md:30`](../manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md) *"guaranteeing that inertial mass and gravitational mass are identical ($m_i \equiv m_g$)"* (wording stale, C5) | — |

**P2 — What "sibling" does and does not mean.** Shared: one defect; one enclosing surface
$\partial\Omega$; both read-outs are **surface integrals of enclosed content** (Link over $\partial\Omega$; $\oint_S \mathbf u\cdot\hat n$);
both far fields are $1/r$ in FORM; both are FORM-derived / VALUE-imported
([`form-deriving-value-importing.md:46-49`](../manuscript/ave-kb/common/form-deriving-value-importing.md) — *"The geometry and topology of the chiral K4 Cosserat substrate FORCE the dimensionless FORMS … The dimensionful VALUES of the handful of calibration constants the substrate is *fed* are calibration INPUTS"*);
both are DC medium content read differentially ([`form-deriving-value-importing.md:284`](../manuscript/ave-kb/common/form-deriving-value-importing.md) `gravity = the `S(A)` operating-point field`; `:286` `charge = topological boundary data`).
**Not shared:** source structure (deposited net flux vs no deposit, C6); sector (A1 vs T2); domain of the store (mechanical bulk vs mechanical shear + EM read-out); read-out type (index/clock at $\Gamma_{\mathrm{EM}}=0$ vs reflection/interaction); path structure (ledger vs endpoint); the clock each rides (C7).

**P3 — No second force.** Gravity is not an interaction added to the substrate:
[`trampoline-framework.md:552`](../manuscript/ave-kb/common/trampoline-framework.md) — *"**No separate "gravitational interaction" needed.** Gravity is the macroscopic limit of the shared-spring propagator that already exists at the lattice level."*;
`:550` — *"Gravity is the **gradient of substrate strain** — exactly what an EE probe would measure as a local impedance gradient (Vol 4 Ch 1)"*.
The charge interaction is the Axiom-2 leg (`clm-wcoul2`, consistency-class). Two read-outs of one defect are not two forces.

**P4 — Why this is the lattice-free north star.** Neither read-out carries $\ell_{node}$ in its FORM:
$\mathrm{Link}(\partial\Omega,\mathbf F)$ is an integer; $\oint_S\mathbf u\cdot\hat n=4\pi B(M)$ is a flux over any enclosing exterior surface.
$\ell_{node}$ enters only through the VALUE imports ($\xi_{topo}\equiv e/\ell_{node}$; $\kappa$, $\mathcal{A}_g$).
The interior is exempt from lattice constraints ([`boundary-observables-m-q-j.md:100`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md) — *"Interior eigenmodes are not lattice-Nyquist-constrained."*, `clm-sjjvhf`), and the Stokes structure
(`:23` — *"The three dimensions are exhaustive: there is no fourth integrated boundary observable at this scale-invariant structure."*) is asserted at **input-only** grade (`clm-ze4clw` 0.55 — the register's own caveat: *"Does NOT claim a formal proof that no fourth observable exists"*).

**P5 — A1 ⊥ T2 preserved; the only join is constitutive grading.** The two families share no
$(V_{inc},V_{ref})$ phasor (P1). The join the corpus is walking is **A1 Q-point grades T2 constitutives**
([`2026-08-29_picture-lock-spillover.md:65`](2026-08-29_picture-lock-spillover.md) H1, held; closed WALK-grade on `[branch:#1034]`) — a photoelastic coupling, not a shared port. This record adds no join.

---

## §4 — Ledger: CANON / RESTATEMENT vs OWED

| # | statement | grade | pin | what would move it |
|---|---|---|---|---|
| K1 | A1 ⊥ T2 grade orthogonality; no shared phasor; FOC-independent | **CANON** (Grant-ratified) | `master-equation.md:20,:33,:36` | — |
| K2 | mass = A1 dilatation (rest-mass store) | **CANON as grade-ASSIGNMENT**, not driver-validated | `master-equation.md:31`; `boundary-observables-m-q-j.md:25` | a driver that discriminates A1-mass from T2-mass (none exists, `:31`) |
| K3 | $\mathcal{Q}=\mathrm{Link}(\partial\Omega,\mathbf F)\in\mathbb Z$; STATIC, reactive | **CANON** (`clm-ze4clw` 0.55 input-only; `def-3638f2` sharpen PROPOSED) | `boundary-observables-m-q-j.md:20`; `vocabulary-register.md:256` | Grant ratification of the 2026-06-24 sharpen |
| K4 | observability rule (only $\mathcal M,\mathcal Q,\mathcal J$ escape) | **CANON** (`clm-ofys5v` 0.55 input-only) | `boundary-observables-m-q-j.md:33-39` | local derivation of the rule (register caveat) |
| K5 | clause S / G / Q; bound response, no port; $u_0=B\hat r/r^2$; $\varepsilon_{11}=7GM/c^2r$ | **CANON** (source law, POSTULATED; R38/R40/R43–R55) | `eq_axiom_5.tex:68,:75-77,:84,:94,:100`; `axiom-register.md:338-342,:423` | — (postulated, not derivable from Ax 1–4 by its own status line) |
| K6 | $n(r)=1+2GM/c^2r$; compression = impedance gradient; $\Gamma_{\mathrm{EM}}=0$ under SYM | **CANON** (`clm-rd9cjm` 0.55, `clm-3bwhad` 0.55) | `refractive-index-of-gravity.md:14`; `boundary-observables-m-q-j.md:110`; `master-equation.md:115` | — |
| K7 | two clocks (A1-Op14 time dilation; T2 flywheel spin) | **CANON** | `master-equation.md:38` | — |
| K8 | weight ≡ inertia derived via /7 | **CANON** (`clm-rd9cjm`), **wording stale** | `ponderomotive-equivalence.md:12,:14,:30` | Rule-12 banner on "inductive rest mass" (hygiene lane) |
| K9 | all measurement is AC; distinct observables = AC read of DC gradient/topology | **CANON, organizing-principle class** (`clm-acdc07` 0.55) | `form-deriving-value-importing.md:296-297`; spillover `:61` (Grant-signed) | a forward DC→AC falsifier landing |
| K10 | FORM-derived / VALUE-imported on both families | **CANON** (per-constant rows) | `form-deriving-value-importing.md:46-49,:86,:90` | flip-tests (Chain B′ for G; London leg for charge) |
| K11 | no sourced net monopole; pair sign structure | **CANON** (`clm-nogo4l` 0.55; `clm-wcoul2` 0.70) | `the-sourced-charge-no-go-cascade.md:148-149`; `boundary-observables-m-q-j.md:27` | the terminal fork ruling |
| R1 | port↔DOF↔sector map (MASS→$Z_{bulk}$, CHARGE→$Z_{shear}$, ε/μ→$Z_{EM}$) | **RESTATEMENT, proposed/gated** | `vocabulary-register.md:506-518` (`def-portmp`) | auditor + Grant review; the $V_{yield}$-fork role attribution |
| R2 | three-channel ROLES (carrier port / charge boundary / mass store) | **RESTATEMENT, consistency-class** (Z_bulk row R40-stamped) | `resonant-lc-solitons.md:127-129` | R40 re-derivation of the Z_bulk row |
| R3 | port taxonomy (radiative iff Re Z>0; channels inherent, ports emergent) | **RESTATEMENT, walk-wording ratified by firing** | `port-register.md:19-37` | — |
| R4 | §3 P0–P5 above (the packaging sentence) | **RESTATEMENT over K1–K11, WALK-GRADE** | this file | Grant wording call + Claims Gate |
| **O1** | **the one-place definition** — one defect, two sector contents, two far-field read-outs — stated nowhere in `ave-kb` (grep receipt above) | **OWED-DEFINITION** | — | Grant picks the noun ("read-out family" vs qualified "port family", C2) and the sentence lands in a KB leaf under review |
| **O2** | **why ONE defect carries BOTH** contents (the Link and the A1 deposit together) — clause S is mechanism-agnostic; the genesis-phase law is named-open (c2) | **OWED — definition or derivation, unadjudicated** | `eq_axiom_5.tex:71,:98` | a Grant call on whether this is a definitional join or a derivation target; **must not** be discharged by inventing a coupling |
| **O3** | the charge-side far-field profile ($1/r$ tail) and the net-monopole-vs-holonomy fork | **OWED-DERIVATION + ROUTED-TO-GRANT** | open-items `exterior-field-profile-derivation`, `terminal-charge-framing-fork` | the fork ruling; the engine-blocked derivation |
| **O4** | the mass-side finite-speed dynamics — THE BIAS PROPAGATION THEOREM | **OWED (standing debt, c1)** | `eq_axiom_5.tex:98`; `master-equation.md:149-152` *"owed, not held"* | the theorem |
| **O5** | sector-of-storage D1 (which sector's $c^2$ divides $E_{trapped}$) | **OPEN-IN-WALK** (Grant walking) | open-item `sector-of-storage` | Grant ruling |
| **O6** | the 1:1 Kirchhoff map of DC strain; H2–H6 | **OPEN-IN-WALK** (H1 closed WALK-grade on `[branch:#1034]`) | open-item `acdc-gravity-circuit-map`; spillover `:65-70` | #1034 review; H2–H6 walks |
| **O7** | vocabulary: "port family" (no def); "weight" (no def-node); $B(M)$ glyph across the A1 ⊥ T2 fence | **OWED-VOCAB / ROUTED** | `def-portmp` proposed; open-item `axiom5-b-glyph` | Grant naming calls |
| **O8** | the four cite-shifts + the unstamped `def-9a4f07:594` (C9) | **HYGIENE, routed** | C9 (a)–(d) | auditor / R40 batch owner |

---

## §5 — Fences (what this record does not do)

- Promotes nothing to FACT; mints no id; edits no KB / manuscript / engine file.
- Does not pick "read-out family" over "port family" — it shows the collision (C2) and leaves the noun to Grant.
- Does not close O2 with a mechanism. The four-lock no-go and clause S's mechanism-agnostic status stand as read.
- Does not touch Op16 (`operators.md:56`), the G2 freeze decisions, or the static-existence epic.
- Does not treat `[branch:#1034]` / `[branch:#1033]` content as canon; cited as context only.

## §6 — Suggested next actions (Orchestrator's call; none taken here)

1. **Naming ruling (Grant):** "port family" (def-portmp sense, qualified every use) vs "read-out family". Cheap; unblocks O1.
2. **O2 classification (Grant):** is "one defect carries both contents" a **definition** (boundary data co-deposited at genesis, c2) or a **derivation** target? A wrong class here wastes a lane (pre-test-physics-check trigger 8).
3. **Open-item stub, if wanted** (not minted here to avoid a second home while MATH-1 lives on the tracker): `id: sibling-definition-debt`, `status: OPEN-IN-WALK`, `owner: grant`, `source: research/2026-09-13_sibling-definition-debt_RECORD.md`, `anchor: "One real-space defect. Two orthogonal sector contents"`.
4. **Hygiene routing:** C9 (a)–(d) to the auditor lane / R40 batch owner; K8 wording banner to a hygiene lane.
5. **Sequencing:** land nothing from §3 into `translation-circuit.md` or `boundary-observables-m-q-j.md` before #1034 (H1) is reviewed — same join, two sides.
