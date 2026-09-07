---
id: ppn-matter-sector-walkback
title: "Matter-sector PPN — sites claiming the perihelion derivation gap is CLOSED and the coefficient is IDENTICAL to GR"
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-27
source: manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex
anchor: "The same perihelion advance is derivable directly from the canonical temporal/spatial refractive metric"
---

**ROUTED-TO-GRANT. This item supersedes nothing and rules nothing. Only Grant rules.**

*(The frontmatter anchor points at Group C1, the sharpest single site — it asserts the exact
`beta = gamma = 1` pair the result contradicts. The KB leaf's own paragraph is duplicated
byte-for-byte at `:10` and `:20`, so it cannot serve as a unique anchor; the full set is below.)*

Basis: [`research/2026-08-27_ppn-tensor-derivation_result.md`](../../research/2026-08-27_ppn-tensor-derivation_result.md).
Sibling: `research/2026-08-27-two-knob-gravity-repair` (a repair reaching GR at $O(m)$; see "What the repair does NOT do" below).

## The finding, in one line

Feeding canon's own matter index `n_scalar = 1 + eps_11/7` (`ponderomotive-equivalence.md`:14) through canon's own Gordon metric (`gordon-optical-metric.md`:17) gives **gamma = 0 exactly and beta = 3/2 exactly**, hence `F = (2 - beta + 2 gamma)/3 = 1/6` — Mercury at `7.163''`/century against `42.98`, Hulse-Taylor at `0.7044 deg/yr` against `4.226595`. Confirmed by direct geodesic integration with a GR isotropic-Schwarzschild control, and independently by a medium-native WKB route on the sibling branch.

## ★ DO NOT EDIT THE SITES BELOW

They are enumerated so Grant can rule on the whole set at once. **This lane edited none of them**, and several are Rule-12 frozen-class (dated scope-corrections, a changelog entry, a research result). What lands where — dated surface-note, `🔴` header, status demotion, or nothing — is the ruling, not the lane's call.

## The enumeration

**METHOD, and its limit.** These are the sites returned by the pattern searches and end-to-end reads recorded at `research/2026-08-27_ppn-tensor-derivation_result.md` §10, cross-run under two different grep binaries. **This is a statement about that search, not about the corpus.** A site phrasing the same claim in words none of those patterns match is not covered. §10.4 names the blind spots.

### Group A — the canonical KB leaf

| # | site | verbatim |
|---|---|---|
| A1 | `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/anomalous-perihelion-advance.md`:10 | *"substrate-native derivation gap CLOSED at leading PPN-1 order via Ponderomotive Equivalence Principle pathway. … the $-GML^2/(mc^2r^3)$ correction term coefficient is **1**, IDENTICAL to GR Schwarzschild. Perihelion advance $\Delta\phi = 6\pi GM/c^2 a(1-e^2)$ is therefore substrate-native at leading PPN-1, NOT borrowed from GR. The "3" coefficient question (Foundation Item 4 open gap) is now answered: substrate-native gives 3 exactly"* |
| A2 | same file, `:20` | **byte-identical duplicate of A1** — the scope-correction block is repeated above and below the `## Anomalous Precession` heading |
| A3 | same file, `:44` | *"which accumulates to $\approx 43$ arcseconds per century---the *identical* result obtained by General Relativity."* |

### Group B — claim-quality and the changelog

| # | site | verbatim |
|---|---|---|
| B1 | `manuscript/ave-kb/vol3/claim-quality.md`:292 (clm-qyn8t0) | *"For Mercury, this gives $\sim 43$ arcsec/century — identical to GR; a category (iii) consistency check."* |
| B2 | `manuscript/ave-kb/vol3/claim-quality.md`:307 (clm-qyn8t0 rationale) | *"then shown substrate-native at leading PPN-1 via the Ponderomotive Equivalence pathway with the "3" coefficient recovered exactly (Item 5)"* |
| B3 | `manuscript/ave-kb/claim-quality-closure-roadmap.md`:205 | *"the $-GML^2/(mc^2r^3)$ correction term has coefficient 1 IDENTICAL to GR Schwarzschild → leading PPN-1 perihelion advance $\Delta\omega = 6\pi GM/(c^2a(1-e^2))$ → Hulse-Taylor periastron rate = 4.226°/yr SUBSTRATE-NATIVE (NOT borrowed from GR)"* |

### Group C — the manuscript

| # | site | verbatim |
|---|---|---|
| C1 | `manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex`:71 | *"The same perihelion advance is derivable directly from the canonical temporal/spatial refractive metric $(n_t, n_s)$ of Vol~3 Ch~1--Ch~2 (the PPN factor $(2-\beta+2\gamma)/3 = 1$ at $\beta = \gamma = 1$ reproduces $6\pi GM/c^2 a(1-e^2)$)"* — **this is the sharpest one: it asserts the exact pair the result contradicts.** Note the surrounding warningbox is otherwise *honest* about the `3` being GR-adopted |
| C2 | `…14_macroscopic_orbital_mechanics.tex`:81 | *"accumulates to $\approx 43$ arcseconds per century---the \textit{identical} result obtained by General Relativity"* |
| C3 | `…14_macroscopic_orbital_mechanics.tex`:23 | table row: `Mercury precession & II (Yield) & $\Delta\phi$ = 43''/century & Exact match with GR \\` |
| C4 | `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md`:16 | `| Mercury precession | II (Yield) | $\Delta\phi$ = 43''/century | Exact match with GR |` — the KB mirror of C3 |
| C5 | `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/index.md`:29 | `| [Anomalous Perihelion Advance](anomalous-perihelion-advance.md) | Tidal impedance correction, $1/r^3$ perturbation, Mercury 43''/century |` — index summary, weakest of the set |

### Group D — the research document the whole chain rests on

`research/2026-05-17_hulse-taylor-substrate-native-derivation-sketch.md`, whose own header at `:7` reads **`**Status**: SKETCHED, not rigorous. Multi-session full rigor pass deferred.`**

| # | site | verbatim |
|---|---|---|
| D1 | `:93` | *"**Same as GR Schwarzschild at this leading order.** The substrate-native derivation reproduces the 4.226°/yr value"* |
| D2 | `:99` | *"**Substrate-native PPN-1 at leading order: MATCHES GR Schwarzschild 4.226°/yr.**"* |
| D3 | `:173` | *"**Outcome A (substrate "3" = 3 exactly, ~70% prior)**: ✅ **CONFIRMED AT LEADING PPN-1**"* |
| D4 | `:186` | *"**Hulse-Taylor consistent with both AVE and GR at PPN-1 leading order** (the 4.226°/yr value is structurally identical)"* |
| D5 | `:204` | *"✅ **Leading-order periastron advance = 4.226°/yr** (substrate-native, not GR-borrowed)"* |
| D6 | `:215` | *"**The substrate-native derivation gives 4.226°/yr at leading PPN-1 from independent path** (NOT borrowing GR). This closes the Foundation Item 4 open gap"* |

### Group E — downstream consumer

| # | site | verbatim |
|---|---|---|
| E1 | `research/2026-07-20_q1-pulsar-hardening.md`:84 | *"The corpus already claims GR-consistency for periastron advance (the ponderomotive `n_scalar` derivation, structurally identical to GR — `claim-quality-closure-roadmap.md:204` `[canon]`; `anomalous-perihelion-advance.md` `[canon]`)."* Its own load-bearing conclusion — that `Ṗ_b` is the discriminator because the conservative sector agrees — **depends on this**. *(Its cite `:204` is stale by one line; the content is at `:205`.)* |

## ★ The document that already said this, and was superseded the same night

`research/2026-05-17_hulse-taylor-substrate-native-derivation-result.md` — the **Outcome C** result, dated the same day as Group D — states the finding correctly at `:143`:

> *"The framework's PPN-1 weak-field gravity recovery via Gordon optical-metric isomorphism is **structurally limited to OPTICS** (light propagation); for MECHANICS (massive-particle orbital dynamics), the substrate-native PPN-1 coefficient **has NOT been derived**."*

and at `:145`:

> *"The mechanics-sector PPN-1 recovery is currently **asserted-via-borrowing, not derived**."*

**§2 of the result doc re-derives exactly that, and sharpens it from "not derived" to "derived, and it is `1/6`."** So the standing question is not only what to do with Groups A–E; it is **which of two same-day 2026-05-17 documents is standing** — a `RESULT` graded Outcome-C-confirmed, or a `SKETCH` self-graded *"not rigorous"* whose own annotations `:49` and `:80` carry the counter-evidence.

## What the repair does NOT do

The sibling branch reaches GR at $O(m)$ with $(a_1, b_1, b_2) = (2, 1, 1/2)$ on a two-knob constitutive parameterisation. **It does not reduce this debt.** Groups A–E are wrong under **both** readings: under the pre-repair reading because `gamma = 0`, and under the post-repair reading because they claim a *derivation* of a coefficient that is presently a *chosen admissible point* — whether the constitutive map **forces** `(2, 1, 1/2)` is OPEN. Grant should rule on A–E with the repair in view, not instead of it.

## Also surfaced by the same lane, routed here rather than minting more items

- **The 2026-06-05 audit's beta statement is scope-limited and reads as general.** `research/2026-06-05_gravity-ppn-coherence-result.md`:69 — *"No canonical AVE statement derives β"* — and `src/scripts/verify/gravity_ppn_coherence.py`:349 pinning `beta=1` under the comment *"no canonical AVE statement sets beta independently"*. True of the S1–S4 pair it examined; **false once the ponderomotive matter index is in scope**, and that index is absent from its structure list (verified two ways). The audit is frozen-class: a dated surface-note, never a rewrite.
- **`double-deflection.md`:44 and `02_general_relativity_and_gravity.tex`:202 present `delta_matter = 2GM/(bc^2)` "(Newton / Soldner 1801)" as a derived AVE result.** That IS the `gamma = 0` matter sector, stated as a feature. Whatever Grant rules above, the relationship between the Double Deflection's `2:1` ratio and the matter sector's PPN failure should be stated at one of those sites, because they are the same fact.

## The one plumber-physical question this turns on

> **Does the vacuum's series impedance and its shunt impedance grade together under gravity, or by a factor of two?**
>
> A scalar refractive index says *together* — one knob, so the wave slows and the tank detunes by the same factor. GR says the tank detunes by `U` while the wave slows by `2U`. **That factor of two is `gamma`**, and it is five sixths of Mercury's perihelion advance.
