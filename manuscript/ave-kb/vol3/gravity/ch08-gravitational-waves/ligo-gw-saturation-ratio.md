[↑ Ch.8 Gravitational Waves](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-07kd5v]
-->

---

The lattice voltage ratio for LIGO GW is:

> **[Resultbox]** *LIGO GW Saturation Ratio*
>
> $$
> \frac{V_{GW}}{V_{\text{snap}}} \approx 1.4 \times 10^{-28}
> $$

Twenty-eight orders of magnitude below saturation. The vacuum is a *perfect* lossless transmission line for gravitational waves, ~~exactly as observed~~ *(clause struck 2026-08-02 per Rule 12 --- preserved, not deleted; see the note below)*.  <!-- rule12-freeze: base=00c38ed470a6a076239e40df5d69fb03b531e5be region=below offset=2 lines=2 bytes=5 sha256=316deeb28892b1cdebfe5c12c2cd620b5b8f29289c1ffe3d4f5fc1b2e6a4ea7d -->

> **[2026-08-02 --- Reading-A bulk admixture (sibling propagation)]** The "exactly as observed" completeness framing is struck for the same reason as in [`gw-propagation-lossless.md`](gw-propagation-lossless.md), which carries the canonical 2026-08-02 statement. Under **Reading-A** (the standing physics as of 2026-07-20) the framework **additionally** predicts a bulk (longitudinal P-wave) admixture radiating on top of the shear decay at $O(1)$ coupling, $F_{\text{bulk}}/F_{\text{shear}} \approx 0.03$--$0.12$ --- carrying a **LIVE** pulsar exclusion of an independent $O(1)$ bulk radiative port plus an **OPEN** constituent-cage fork. The deeply-linear-regime losslessness of the *shear* channel stated above is unaffected and stands; the claim of an exact and complete match to observation does not. Ruled state: Grant's F4 → option (a) (`_orchestration/2026-07-10_rulings-docket.md:2573`; `_orchestration/2026-07-20_pending-rulings-and-frontier-queue.md:113`), executed in the printed chapter by PR #771 (`manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:107`). **The bulk/shear double-count contradiction (Q1-REVERT) remains LIVE and routed** ([`common/port-register.md`](../../../common/port-register.md) line 5) --- Reading-A is the standing physics, not a closure of that contradiction. 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**

---
> **[2026-08-04 — TWO-RULER DISSOLUTION (R13, ruling execution; nothing above is edited and no number moves).** The corpus carries **two** yield rulers that a reader has been comparing as if they measured one thing:
>
> - the **lattice-voltage** ruler — $V_{GW}/V_{\text{snap}} \approx 1.4\times10^{-28}$, the Resultbox above;
> - the **metric-strain** ruler — $h/h_{yield} = 10^{-21}/\sqrt\alpha = 1.171\times10^{-20}$, with $h_{yield} = \sqrt\alpha = 0.0854$.
>
> Across the regime table at [`einstein-field-equation.md`](../ch02-general-relativity/einstein-field-equation.md) the two are related by exactly $V_{GW}/V_{snap} = 10^{-7}h$ on **all four** rows, so the voltage ruler places saturation at $h = 10^{7}$ while the strain ruler places yield at $h = \sqrt\alpha$ — apart by $1.17\times10^{8}$. That $10^8$ was booked as a **corpus-wide debt needing a physics answer** (`_orchestration/docket-entries/2026-08-03-rulings-mr-batch.md` routed follow-on **#8**).
>
> **RULED: there is no contradiction to reconcile — the two are PER-CHANNEL rulers, each read against its OWN channel's wall.** A ratio of a lattice **voltage** to a **voltage** wall and a ratio of a metric **strain** to a **strain** wall are different quantity kinds on different channels; that their walls sit at different places on a shared $h$ axis is a fact about the channels, not a disagreement about "where yield is." **Neither ruler is edited, deprecated or rescaled** — the debt is dissolved, not paid. **What the dissolution requires of every consumer:** name the channel before quoting a regime. *"Regime I"* is not a property of a source; it is a property of a **source-on-a-channel**.
>
> ⚑ **The channel LABELS themselves are FLAGGED, NOT PICKED — and the flag is a live sector-ownership question, not bookkeeping.** The dispatch that relayed this ruling labels the pair *"$V_{GW}/V_{snap}$ = T2-electric channel vs its wall; $h/h_{yield}$ = shear channel vs its wall."* That is **not obviously consistent with a ratified line already in print**: `vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex` §*"Sector re-keying correction"* (2026-08-02, `def-vyvsn1` grade-fork RESOLVED = T2, Grant 2026-06-30) reads verbatim — *"$V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$ kV is the **transverse Cosserat ($T_2$) self-trap wall** … **not** the A1 compliance bound. The longitudinal-A1 compliance diverges at the higher $V_{snap} = m_e c^2/e \approx 511$ kV"* — i.e. canon attaches **$V_{yield}$** to $T_2$ and uses **$V_{snap}$** as the **A1** compliance normalizer, while the staged ch15 text derives $h_{yield} = \sqrt\alpha$ from *"the same Axiom 4 saturation physics that defines $V_{yield}$"*. Two readings survive: (a) the labels are as dispatched and canon's A1-normalizer statement is scoped to *which voltage normalizes the compliance kernel* rather than to sector ownership; (b) the labels are crossed. **This lane picks neither** — the dissolution above holds under both, because it turns on the two rulers being different *kinds*, not on which sector owns which wall. Routed to the auditor/Grant with both quotes.
>
> ⚑ **Print side WAVE-HELD.** The `vol3` ch08 / ch15 printed chapters carry the same two rulers and are **not touched here** — they fire with the ringdown wave (one-print-touch).

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:20`** — *"the framework additionally predicts a bulk (longitudinal P-wave) admixture radiating on top of the shear decay at O(1) coupling"*
  Stamped in place at `:20`.
  **Why it dies (audited row rationale, verbatim):** Sibling propagation banner; the V_GW/V_snap linear-regime ratio content of the leaf is untouched. The :32 channel-label flag (V_snap = A1-compliance normalizer vs T2) stays FLAGGED per the prereg — not adjudicated here.
  **Scope carve (review fix 2026-08-11).** `:32` is NOT demoted and NOT adjudicated here. The audited
  rationale says so verbatim: *"The :32 channel-label flag (V_snap = A1-compliance normalizer vs T2)
  stays FLAGGED per the prereg — not adjudicated here."* It is an A1-vs-T2 sector-ownership flag routed
  to the auditor/Grant; this batch does not touch it.

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
