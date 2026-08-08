# GW-FORMATION WALK DOSSIER — what canon actually holds the GW carrier to be (receipts only)

**Date:** 2026-08-07 · **Branch:** `research/a1-port-sourcing` (PR #919 lane closing deliverable)
**Purpose:** feeds the GW-FORMATION WALK required by **ruling R24**
(`_orchestration/docket-entries/2026-08-07-rulings-r23-r27.md`; Grant verbatim `[sic]`: *"They
seem different. A GW is a saturation wave, which affects Transverse EM right? but not the same.
Do we need to walk how a GW forms?"*).
**Class:** research NOTE — receipts only. **This dossier ADJUDICATES NOTHING**: no `clm-`/`def-`
minted, no solidity moved, no picture picked. Every pull is verbatim with file:line at worktree
HEAD (base `91a910f8` + this lane's commits); collection = background corpus sweep + first-party
`sed`/`grep` spot-verification of every front-loaded quote; absence claims carry two-method
receipts with named patterns.

---

## §0 — The contested identity (why this dossier exists)

Per R24, the identity *"GW-carrying shear ≡ transverse polarization of the same displacement
field whose longitudinal polarization is the A1 bulk mode"* is **CONTESTED-BY-GRANT** and does
not adjudicate until the walk runs. The unreconciled pair the walk must face (R24's words): the
echo sector treats ringdown as SHEAR DISPLACEMENT waves; the trampoline/observable sector
treats gravitational action as SATURATION/IMPEDANCE modulation read by the EM channel. Both
pictures are pulled below, then the sites where they touch.

## §1 — Picture A: GW = transverse shear wave of the substrate (the echo/ringdown sector)

- **A1 (the canonical carrier line)** — `manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md:13`,
  verbatim: *"Gravitational waves are transverse inductive shear waves in the LC lattice---the
  same medium governed by the same operators."* And `:36`: *"Gravitational waves are
  **transverse shear waves**, not EM transverse waves. The impedance statement above applies to
  $Z_{EM}\equiv Z_0$ **only** … The shear impedance is $Z_{shear}=\rho\,c_{shear}$, which
  **freezes** under saturation."*
- **A2 (the channel row)** — `manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md:21`:
  *"| Shear / GW | $Z_{shear} = \rho_{bulk}\,c_{shear}$ | $\rho_{bulk}\,c_0$ at $S=1$ |
  $\Gamma_{shear}\to -1$ |"* — with `:10`: *"$Z_0\equiv Z_{EM}$ is the **transverse-EM channel
  only**. Shear and bulk channels carry separate device-port impedances."*
- **A3 (ringdown echoes)** — `manuscript/ave-kb/vol3/gravity/ch02-general-relativity/einstein-field-equation.md:62-64`:
  *"GW are **transverse shear** modes, so they **reflect totally** off $r_{sat}$:
  **gravitational ringdown echoes ARE predicted**"*; `:84` (§"Gravitational Waves as Inductive
  Shear"): *"gravitational waves are low-frequency macroscopic inductive strain-waves
  propagating through the structured LC network."*
- **A4 (the band structure)** — `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md:118`:
  the S-branch row — *"**S / transverse (shear)** branch $=c_S=c_0$ — the **light-like
  PROXY** … ⚠ PROXY: the true photon is the **T2 Cosserat MICROROTATION**"* (`:117` marks the
  `√2` A1 bulk-sound *"NOT a Bloch branch"*).
- **Register note:** the exact phrase "shear displacement" has **0 hits** in
  `manuscript/ave-kb/` (two-method: `grep -rn "shear displacement"` and
  `grep -rnE "shear-displacement|transverse displacement"` — no GW-relevant KB hits); the KB's
  Picture-A register is *"transverse inductive shear waves"* / *"transverse shear modes."* The
  displacement-field register lives in the research lineage (#761, the envelope derivation).

## §2 — Picture B: gravitational action = saturation/impedance modulation (the trampoline/observable sector)

- **B1 (★the manuscript's own GW summary is in Picture-B register)** —
  `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:371`, verbatim:
  *"Gravitational waves propagate exclusively as lossless, trace-free, transverse **impedance
  modulations** of the macroscopic LC vacuum lattice."* (Same phrase at `:10`.) This sits
  INSIDE the Picture-A chapter — B-register wording for the A-sector object. The chapter itself
  notices the tension at `:158-163` (the warningbox lineage: the summary's wording vs the KB's
  *"transverse inductive shear waves"* assignment).
- **B2 (the readout is the EM channel)** — `08_gravitational_waves.tex:317-320`: *"A
  gravitational wave detector is an impedance antenna. LIGO's 4 km Fabry–Pérot arms form
  resonant cavities in the LC vacuum, where each light bounce amplifies the GW-induced
  impedance modulation. The passing GW strain $h$ perturbs the local vacuum impedance"* — KB
  twins at `gw-impedance-perturbation.md:10` and `gw-detection-antenna.md:13`. This is
  Grant's *"affects Transverse EM"* as canon.
- **B3 (the operating-point clock)** — `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:38`:
  *"the **gravitational / time-dilation local clock** … is the **Op14 saturation clock**
  $\omega_{local}(r) = \omega_{global}\sqrt{1 - A^2(r)}$ … set by the **A1 saturation
  OPERATING POINT** $A^2(r)$ (the dilatation depth) … the A1 saturation that *makes* the mass
  is the *same* operating point that slows the local clock."*
- **B4 (static gravity = strain→impedance grading)** —
  `manuscript/ave-kb/common/trampoline-analogy-primer.md:292,297-298` (Step 5.5): *"Each
  soliton creates a local strain field $A(\mathbf{r})$ around it … The local strain field maps
  to a local impedance gradient via the kernel: $Z_{local}(\mathbf{r}) =
  Z_0/\sqrt{S(A(\mathbf{r}))}$."*
- **B5 (constitutive grading, Z-invariant)** — `einstein-field-equation.md:37,41-46`: the
  metric ↔ $(\varepsilon_{eff},\mu_{eff})$ isomorphism, *"both constitutive parameters scale
  with the refractive index $n(r)=1+2GM/(rc^2)$"*, resultbox *"$Z(r)=Z_0$ (invariant)"* — the
  EM channel sees static gravity refractively, never reflectively.
- **B6 (corpus census)** — "impedance modulation" + GW co-occurs ONLY at the B1/B2 sites (+
  docs quoting them); "saturation wave" + GW occurs ONLY at def-satshr / def-ncsatw (§3) and in
  R24's own echo. No canon leaf outside those two defs calls the GW a "saturation wave."

## §3 — The fusion canon already holds (the two pictures as one object)

- **F1 (★def-satshr, SOLID for the split)** — `manuscript/ave-kb/common/vocabulary-register.md:1053-1054`,
  verbatim: *"The radiative moment of the slow envelope's bias field is
  $Q_{ij}\propto\int x_i x_j|A|^2$ (the mass second-moment). Its **traceless (deviatoric)**
  projection = the **saturation-SHEAR wave** = the **OBSERVED gravitational wave** — the
  T2-shear channel, quadrupole rotating at $2\Omega$, radiating at $c$, tensor polarization …
  Its **trace** projection = the **saturation-COMPRESSION wave** = the A1-bulk / scalar
  (breathing) channel = the **pulsar-excluded bulk radiative port**."* Status (`:1057`):
  *"SOLID for the trace/traceless DEFINITIONAL SPLIT … NOT a hardening of the coupling
  verdict."* Read-guard (`:1060`): *"The compression channel is the A1-bulk (mechanical
  dilatation), NOT a transverse EM mode."*
  **Walk-relevance (receipt, not adjudication):** canon here names the observed GW a
  *saturation*-something — a wave OF the saturation-bias field's traceless moment — *riding*
  the T2 shear channel. It fuses Grant's two pictures into one object rather than choosing.
- **F2 (def-ncsatw, proposed only)** — `vocabulary-register.md:1065-1078`: free radiated
  saturation waves as *"the far-field / GW radiation class"* — status *"proposed —
  WALK-RATIFIED DIRECTION … NOT SOLID, NOT canon."*
- **F3 (#761 §1.1 — one displacement field)** —
  `research/2026-07-20_mechanical-commonmode-derivation_result.md:46`, verbatim: *"the
  A1-dilatation $θ = ∇·u$ is the **longitudinal polarization of the vector displacement
  field** — … NOT a separate scalar DOF; it is a projection of the same 3-vector $u$ the
  vector survey solves."* The strongest canon-adjacent statement that the compression sector
  and the shear-GW sector are projections of ONE field at linear order. *(This is the R24
  CONTESTED identity's research-side receipt — quoted, graded at its home, not re-asserted
  here.)*

## §4 — The word "longitudinal" is a locked four-way overload

**def-9a4f07** — `vocabulary-register.md:584-604`, status **`ambiguous`**. Adjudicated
meaning (`:586-587`): *"the **real V-sector scalar grade** — the Heaviside/Gibbs-excised
longitudinal compression scalar that is **physical, NOT Gauss-deleted**. It is 'the 3' in its
A1 dilatation-MASS sense … It must **never** be framed in QED-vector terms."* The
open-ambiguity block (`:595-601`) locks FOUR senses: (a) the bulk-volumetric V-sector scalar /
A1 dilatation-mass "3"; (b) the Cosserat longitudinal-shear $\tau_{zx}$; (c) the EM-forbidden
longitudinal photon; (d) the K4 A1 port-mode $\sqrt2 c$. Any walk statement relating "the GW"
to "the longitudinal/saturation sector" must declare which sense it uses — the FLAG-LC1-B
fossil (PR #919 headline) is what happens when the senses blur.

## §5 — How a GW is GENERATED, per canon (every site; the rate is imported everywhere)

- **G1 (the manuscript's generation treatment)** — `08_gravitational_waves.tex:74`, verbatim:
  *"the $(v/c)^5$ quadrupole scaling and the Peters--Mathews coefficients are carried over
  from the standard radiation formula, so the result is a consistency reproduction rather than
  an independent first-principles derivation."* Mechanism prose `:78`: the quadrupole
  *"excites the surrounding elastic LC metric … acquires an inductive phase-retardation slip"*;
  `:107`: the observed decay power is on the shear channel, *"the one the Peters–Mathews
  $(v/c)^5$ formula computes."*
- **G2 (the envelope reduction — the most-derived generation content)** —
  `research/2026-07-20_envelope-sector-reduction_result.md:43`: *"the observed GW is
  carrier-shear sourced by the mass quadrupole's traceless part at $2\Omega$ — a **gapless**
  acoustic branch ⇒ **radiates at the GR rate ⇒ consistency gate PASS for shear**"*; with
  `:13/:108/:129`: **form derived** (gapless + quadrupole order), **rate inherited**
  (`[import]`, Peters–Mathews/HT chain, *"NOT re-derived"*).
- **G3 (the common-source structure)** — `research/2026-07-20_q1-pulsar-hardening.md:29-31`:
  both channels *"driven by the **same** rotating mass quadrupole"* via *"standard
  elastodynamics; Aki-Richards"* — and the translation-table row for this partition is
  explicitly tagged *"⚠ cross-discipline (elastodynamic / seismological analog, NOT
  EE-native)"* (`translation-circuit.md:157`).
- **G4 (the only KB emission prose)** — `einstein-field-equation.md:82`: binaries *"act as
  macroscopic impellers driving transverse shear waves"* — an impeller is a
  displacement-drive (Picture-A source register), vs G2's moving-bias-texture ponderomotive
  drive (Picture-B source register). The two source registers are as unreconciled as the two
  carrier registers.
- **G5 (bulk-side forms, for completeness)** — `scalar-gw-bulk-channel_derivation.md:93,:186`
  (quadrupole RADIATIVE, form only) and `#761 :52` (the imposed delta source) — form-grade,
  conditional, no rate.
- **ABSENCE CLAIM (two-method, SUPPORTED):** *canon contains NO substrate-derived GW
  generation RATE — Peters–Mathews is imported everywhere it appears.* Method 1: `grep -rn
  "Peters" manuscript/ research/` → 26 hits / 9 files, every canon-side hit import-tagged in
  its own sentence (tex `:74/:116/:214/:261`; `gw-propagation-lossless.md:48`; envelope
  `:13/:108/:129`; q1 `:93`; this lane's result), zero presenting it as derived. Method 2:
  `grep -rniE "quadrupole (formula|luminosity|radiation).{0,80}(derived|first.principles)"`
  → 0 hits; cross-pattern `"quadrupole.{0,120}(derive|first.principles)"` → ~40 hits, every
  one either import-tagged or FORM-only. (Engines: BSD/GNU grep -E as shipped on the host;
  patterns as printed.)

## §6 — Contact/contradiction map (where the pictures touch)

| # | Site | What touches |
|---|---|---|
| C1 | **FLAG-LC1-C** (`research/lc1-one-speed` branch, LC-1 result `:780-786`): *"are port-register channels 1 and 2 the same branch? Both $T_2$, both transverse-$u$, both at $c$ … §2.1 finds exactly ONE transverse eigenbranch (multiplicity 2) … **Raised; not decided.**"* | Whether the photon and the GW ride ONE eigenbranch is OPEN in canon — the sharpest form of Grant's *"affects Transverse EM right? but not the same."* |
| C2 | LC-1 §9 (`:679-693`): if C1 resolves to one branch, *"$c_{GW}=c_{EM}$ restates 'one branch has one speed'"* — IDENTITY-or-MANIFESTATION, undecided. | The compliance grade of LC-1 itself hangs on the same question. |
| C3 | `wall-taxonomy.md:157`: at $r_{sat}$, *"$\Gamma_{shear}=-1$ and $\Gamma_{bulk}=-1$, but $\Gamma_{EM}=0$ — the EM channel is matched, not reflecting"* (with `:445-448`: the $\Gamma_{shear}$ SIGN is RHO-A-conditional, *"NOT resolved"*). | The channels demonstrably behave DIFFERENTLY at walls — whatever identity holds in the far field, it breaks at boundaries. |
| C4 | `port-register.md:47-48`: channel 1 (EM-transverse photon, $Z_0$) and channel 2 (mechanical shear/GW, $\rho c_{shear}$) — both $T_2$, both transverse-$u$, both at $c$, two rows. | Two register rows, possibly one eigenbranch (= C1). |
| C5 | `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 (`:75-86`): TWO distinct saturation responses — $c_{EM} = c_0/S$ vs $c_{shear} = c_0\sqrt S$; α exactly invariant under SYM co-scaling; *"use $c_{EM}$ (not $c_{shear}$) in the α formula; … time-dilation … $c_{shear}$."* | Canon already holds that a saturation modulation affects the EM and shear channels DIFFERENTLY — Grant's *"affects Transverse EM … but not the same"* stated as invariant. |
| C6 | B1 vs A1: the manuscript's GW summary says *"impedance modulations"* while its cited KB canon says *"transverse inductive shear waves"* — same object, the two registers, in one derivation chain (the chapter's own `:158-163` notices it). | The register split is INSIDE the canon chain, not between rival sectors. |
| C7 | B5 vs B2: static gravity is $Z$-INVARIANT (refractive only, $\Gamma=0$) — yet the LIGO readout is a *"GW-induced impedance modulation"* the EM cavity SEES. | What exactly does a passing GW modulate such that $Z$ stays invariant statically but the EM antenna reads a perturbation dynamically? A walk question, receipt-grounded. |

## §7 — Questions the walk must face (interrogatives only; no leans offered)

1. **The carrier:** is the GW (a) the displacement S-branch (Picture A), (b) a traveling
   operating-point/impedance modulation (Picture B), or (c) one object with two registers —
   def-satshr's *saturation-SHEAR wave*, the traceless bias-moment wave riding T2? What
   observable would distinguish (a)/(b) from (c)?
2. **One branch or two:** does FLAG-LC1-C resolve to one transverse eigenbranch carrying both
   photon and GW (making $c_{GW}=c_{EM}$ an identity), or two (owing a degeneracy mechanism)?
3. **Which "longitudinal":** for each walk statement, which of def-9a4f07's four locked senses
   is in play?
4. **Generation:** what drives the wave at the source — the impeller (displacement drive, G4)
   or the moving bias texture (ponderomotive drive, G2)? Both are canon; neither derives the
   RATE (§5 absence claim). Does the walk's picture make the rate derivable in principle?
5. **The readout consistency (C7):** if a GW is a saturation wave in Grant's sense, does it
   co-scale $\varepsilon,\mu$ (Z-invariant — then what does the impedance antenna read?), or
   modulate them asymmetrically (then which sector receipt licenses that)?

---

> **Provenance.** Assembled 2026-08-07 by the A1-port sourcing lane as its R24 closing
> deliverable. Collection: background corpus sweep (two-method on every absence claim, patterns
> printed in §5) + first-party `sed`/`grep` spot-verification of every front-loaded quote
> (def-satshr `:1053-1054`, def-9a4f07 `:586-587,:591`, tex `:371`, tex `:74`) at this
> worktree. The LC-1 pulls are from branch `research/lc1-one-speed` (PR #913, DO-NOT-MERGE),
> explicitly noted. **No adjudication anywhere in this document** — the pictures are pulled,
> the touch-points mapped, the questions posed; the walk (Grant + orchestrator) decides.
