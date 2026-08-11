[↑ Ch.8 Gravitational Waves](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-07kd5v]
path-stable: "referenced from vol3 as sec:gw_detection"
-->

---

## GW Detection: The Impedance Antenna

A gravitational wave detector is an impedance antenna. LIGO's 4 km Fabry--Perot arms form resonant cavities in the LC vacuum, where each light bounce amplifies the GW-induced impedance modulation.

The passing GW strain $h$ perturbs the local vacuum impedance:

> **[Resultbox]** *GW-Induced Impedance Perturbation*
>
> $$
> \delta Z = Z_0 \cdot h
> $$

The accumulated phase shift after $N$ bounces is:

> **[Resultbox]** *Fabry-Perot Accumulated Phase Shift*
>
> $$
> \Delta\phi = \frac{2\pi f_{GW}}{c} \cdot L \cdot N \cdot h
> $$

For LIGO ($L = 4$ km, $N = 280$, $h = 10^{-21}$, $f = 100$ Hz), $\Delta\phi \approx 2.3 \times 10^{-21}$ rad---resolved via homodyne readout against 750 kW circulating laser power.

The strain sensitivity is bounded by two quantum noise sources: shot noise (phase) and radiation pressure (amplitude), whose geometric mean is the Standard Quantum Limit:

> **[Resultbox]** *Standard Quantum Limit (Strain)*
>
> $$
> h_{SQL}(f) = \sqrt{h_{shot}^2 + h_{RP}^2}
> $$

The lattice voltage ratio for LIGO GW is:

> **[Resultbox]** *LIGO GW Saturation Ratio*
>
> $$
> \frac{V_{GW}}{V_{\text{snap}}} \approx 1.4 \times 10^{-28}
> $$

Twenty-eight orders of magnitude below saturation. The vacuum is a *perfect* lossless transmission line for gravitational waves, ~~exactly as observed~~ *(clause struck 2026-08-02 per Rule 12 --- preserved, not deleted; see the note below)*.

> **[2026-08-02 --- Reading-A bulk admixture (sibling propagation)]** The "exactly as observed" completeness framing is struck for the same reason as in [`gw-propagation-lossless.md`](gw-propagation-lossless.md), which carries the canonical 2026-08-02 statement. Under **Reading-A** (the standing physics as of 2026-07-20) the framework **additionally** predicts a bulk (longitudinal P-wave) admixture radiating on top of the shear decay at $O(1)$ coupling, $F_{\text{bulk}}/F_{\text{shear}} \approx 0.03$--$0.12$ --- carrying a **LIVE** pulsar exclusion of an independent $O(1)$ bulk radiative port plus an **OPEN** constituent-cage fork. The deeply-linear-regime losslessness of the *shear* channel stated above is unaffected and stands; the claim of an exact and complete match to observation does not. Note this leaf describes **detection**: what LIGO's antenna reads out is the observed transverse-shear channel, and that identification is Reading-independent and untouched. Ruled state: Grant's F4 → option (a) (`_orchestration/2026-07-10_rulings-docket.md:2573`; `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md:113`), executed in the printed chapter by PR #771 (`manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:107`). **The bulk/shear double-count contradiction (Q1-REVERT) remains LIVE and routed** ([`common/port-register.md`](../../../common/port-register.md) line 5) --- Reading-A is the standing physics, not a closure of that contradiction. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**

---

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:51`** — *"the framework additionally predicts a bulk (longitudinal P-wave) admixture radiating on top of the shear decay at O(1) coupling"*
  Stamped in place at `:51`.
  **Why it dies (audited row rationale, verbatim):** Sibling propagation of the canonical :48 statement; the leaf's own detection content (LIGO reads transverse shear) is Reading-independent and untouched — only the additional bulk radiative channel dies.
  **Scope carve (review fix 2026-08-11).** No site in THIS file is additionally covered. The
  audited row's `:48` is a CROSS-FILE referent — the canonical statement at
  `manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md:48`, which this
  batch stamps in its own file; line 48 of THIS file is blank. The audited rationale carves the rest
  verbatim: *"the leaf's own detection content (LIGO reads transverse shear) is Reading-independent and
  untouched — only the additional bulk radiative channel dies."*

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
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).
