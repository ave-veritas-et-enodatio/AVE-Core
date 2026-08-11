[↑ Ch.8 Gravitational Waves](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-07kd5v]
path-stable: "referenced from vol3 as sec:gw_propagation"
-->

---

## GW Propagation as Impedance Modulation

Gravitational waves are transverse inductive shear waves in the LC lattice---the same medium governed by the same operators. In accordance with the **Symmetric Scaling** axiom required to preserve a uniform optical vacuum, gravity scales both the local permittivity and permeability symmetrically via the refractive metric $n(r) = (1 - r_s/r)^{-1}$:

$$
\begin{align}
\varepsilon_{eff}(r) &= \varepsilon_0 \cdot n(r) \\
\mu_{eff}(r) &= \mu_0 \cdot n(r)
\end{align}
$$

where $r_s = 2GM/c^2$. Because both components scale proportionally, the macroscopic gravitational impedance remains invariant everywhere:

> **[Resultbox]** *Invariant Gravitational Impedance*
>
> $$
> Z(r) = \sqrt{\frac{\mu_{eff}(r)}{\varepsilon_{eff}(r)}} = \sqrt{\frac{\mu_0 \cdot n}{\varepsilon_0 \cdot n}} \equiv Z_0
> $$

~~Therefore, the reflection coefficient $\Gamma$ across any gravitational gradient evaluates identically to zero ($\Gamma = 0$). While the local speed of light slows down near mass ($c_l = c/n$), the impedance matching remains perfect. Gravitational waves experience zero reflection and zero scattering as they traverse deep gravitational wells, propagating seamlessly.~~ *(Paragraph struck 2026-08-02 per Rule 12 — preserved verbatim above and in git, not deleted; replaced below by the already-ruled 2026-06-11 channel correction.)*

Therefore, the **EM-transverse** reflection coefficient $\Gamma_{EM}$ across any gravitational gradient evaluates identically to zero ($\Gamma_{EM} = 0$). While the local speed of light slows down near mass ($c_l = c/n$), the EM impedance matching remains perfect under SYM scaling. Radio-frequency and optical signals experience zero EM reflection as they traverse deep gravitational wells.

> **[2026-06-11 — three-impedance-law channel correction, propagated here 2026-08-02; KB-lockstep. Discharged-decision propagation of an already-ruled state — it adjudicates *nothing new*.]**
>
> Gravitational waves are **transverse shear waves**, not EM transverse waves. The impedance statement above applies to $Z_{EM} \equiv Z_0$ **only** (field-symbol registry §3.11; vocab-operator-unification audit §4b #1). The shear impedance is $Z_{shear} = \rho\,c_{shear}$, which **freezes** under saturation ($c_{shear} = c_0(1-A^2)^{1/4} \to 0$). Whether GWs reflect at the saturated wall ($r_{\text{sat}}$, where $G_{shear} \to 0$ and $\Gamma_{shear} \to -1$) is **distinct** from the EM $\Gamma_{EM} = 0$ result. The LIGO free-space propagation through weak-field gradients is unaffected; the saturated-interior question is flagged in [`bulk-impedance-at-saturation-boundary.md`](../../cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md).
>
> **Provenance.** This is the byte-mirror of the correction the sibling leaf received on 2026-06-11 and this leaf never did: [`invariant-gravitational-impedance.md`](invariant-gravitational-impedance.md):28 (the corrected $\Gamma_{EM}$ paragraph) and :30 (the correction banner this one mirrors). Both leaves carry `clm-07kd5v`; until now they disagreed on the channel attribution of the same $Z(r) \equiv Z_0$ result. **No new physics, no value change, no new claim** — the bare $\Gamma$ acquires the channel subscript the three-impedance law already required, and the *"Gravitational waves experience zero reflection"* sentence is withdrawn because $Z_0$ matching is an **EM-channel** statement, not a shear-channel one.

### Lossless Propagation

LIGO gravitational waves have strain $h \sim 10^{-21}$. The equivalent voltage per lattice cell is $V_{GW} = h \cdot c \cdot \ell_{\text{node}} \cdot 2\pi f \sim 10^{-19}$ V, which is $\sim 10^{-24}$ times smaller than $V_{\text{snap}} \approx 511$ kV. Far below the saturation threshold, the lattice acts as a perfect lossless linear transmission line. Gravitational waves propagate to cosmological distances without dissipation---~~matching LIGO observations exactly, with zero free parameters~~ *(clause struck 2026-08-02 per Rule 12 --- see the Reading-A admixture note below; the struck text is preserved, not deleted)*.

> **[2026-08-02 --- Reading-A bulk admixture: the ruled propagation of the ch08 item-3 wording]**
>
> **Status of this note.** Discharged-decision propagation of an already-ruled state --- it adjudicates nothing new. Grant ruled the #766-review F4 routed question to **option (a)** (`_orchestration/2026-07-10_rulings-docket.md:2573`; queue row `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md:113`, "✅ RULED 2026-07-20 → option (a)"). That ruling was EXECUTED in the printed chapter by **PR #771** (merged 2026-07-21), whose own body records the debt this note discharges: *"any KB-leaf propagation of the item-3 admixture wording"*. Until now this leaf lagged the printed chapter --- an inversion of the standing rule that the KB is the truth source.
>
> **What this leaf omitted.** The identification of the **observed** gravitational wave as a **transverse shear** excitation (line 13 above) is **Reading-independent and stands untouched** --- it is the channel the Peters--Mathews $(v/c)^5$ formula computes and pulsar timing measures. What the leaf silently dropped is the *additional* channel. Mirroring the chapter's Reading-A statement (`manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:107`): under **Reading-A** (the standing physics as of 2026-07-20) the framework **additionally predicts a bulk (longitudinal P-wave) admixture radiating on top of the shear decay at $O(1)$ coupling**, $F_{\text{bulk}}/F_{\text{shear}} \approx 0.03$--$0.12$; that admixture is **not** part of the observed shear decay. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**
>
> **Why the clause above is struck.** "matching LIGO observations exactly, with zero free parameters" asserts a clean and *complete* match, while the framework simultaneously carries a **LIVE** pulsar exclusion of an independent $O(1)$ bulk radiative port plus an **OPEN** constituent-cage fork. The lossless linear-regime propagation of the *shear* channel is unaffected and stands; the exactness/completeness framing does not.
>
> **⚠ The bulk/shear double-count contradiction (Q1-REVERT) remains LIVE and routed. Reading-A is the standing physics --- it is NOT a closure of that contradiction.** [`common/port-register.md`](../../../common/port-register.md) (line 5) carries the live flag: the Q1 row was **REVERTED** 2026-07-20 to Reading-A-live --- the make-or-break mechanical common-mode derivation returned NONE-DERIVES (merged #761), firing the row's own clause, so the independent-radiative-port exclusion is **live against the framework**. The companion constituent-cage fork is **OPEN**: the deep-rail $k$-scaling adjudicator (#775) returned **BIN-3 / form-undetermined** --- the decisive measurement is not lattice-accessible in the quasistatic regime. This note states the honest standing state; it neither claims a clean gravitational chord nor pretends the bulk sector is settled.
>
> **⚑ FLAGGED, NOT FIXED (adjacent honesty-lag, outside this lane's scope --- flag-don't-fix).** The $\Gamma = 0$ paragraph at line 30 above is the *un-corrected* twin of [`invariant-gravitational-impedance.md`](invariant-gravitational-impedance.md) line 28, which received the **2026-06-11 three-impedance-law channel correction** ($\Gamma \to \Gamma_{EM}$; "Radio-frequency and optical signals experience zero EM reflection", not gravitational waves). This leaf never received that correction. Surfaced for adjudication, deliberately not edited here --- it is a *channel-attribution* lag, a different question from the Reading-A admixture this note propagates.
>
> > ✅ **DISCHARGED 2026-08-02 (KB-lockstep lane).** The flag above is now closed: the $\Gamma = 0$ paragraph has received the 2026-06-11 three-impedance-law channel correction, mirroring the sibling leaf's wording ($\Gamma \to \Gamma_{EM}$; *"Radio-frequency and optical signals experience zero EM reflection"*, not gravitational waves). **The flag text above is preserved verbatim per Rule 12 and nothing in it is struck** --- it remains the accurate record of what was found and why it was not fixed in that lane. The correction sits with the struck paragraph and its own banner in the *"GW Propagation as Impedance Modulation"* section above. The **Reading-A admixture** question this note propagates is a separate axis and is **unaffected**: it stays exactly as stated, including the LIVE Q1-REVERT contradiction and the OPEN constituent-cage fork.

---

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:48`** — *"additionally predicts a bulk (longitudinal P-wave) admixture radiating on top of the shear decay at O(1) coupling, F_bulk/F_shear ≈ 0.03–0.12"*
  Stamped in place at `:48`.
  **Why it dies (audited row rationale, verbatim):** Prereg-named site: an O(1) far-field bulk radiative port IS the phantom; its voiding is the carve's content. Same note's LIVE pulsar exclusion (:50) re-reads as the imported reading's self-exclusion, and the Q1-REVERT double-count dissolves (no bulk port to double-count).
  **Also covered by this demotion** (named in the audited row; not separately stamped): `:50`.

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun, "halo"-for-the-physics and "retardation" are retired).
