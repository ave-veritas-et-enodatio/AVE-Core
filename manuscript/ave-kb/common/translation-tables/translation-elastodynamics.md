[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Elastodynamics / seismology translation spoke — maps the elastic-medium sibling discipline to the substrate's elastodynamic sector (hub). Consistency-class external-anchor rows citing merged derivations; mints no new physical claim (no clm-)."
path-stable: "the elastodynamics/seismology spoke of the hub-and-spoke translation architecture (README-architecture.md); the elastic-medium measurement-sibling of the substrate's A1/T2 sector"
-->

# Elastodynamics / Seismology ↔ AVE Translation

Seismology is the **elastic-medium sibling discipline**: the vacuum substrate is a linear-elastic Cosserat solid (Ax 1), so its far-field radiation partitions into a longitudinal (compressional, A1/bulk-dilatation) and a transverse (shear, T2) channel exactly as an isotropic elastic solid partitions a moment-tensor source into P and S waves. Seismology supplies **external, non-AVE textbook anchors** (Aki–Richards moment-tensor radiation, mode conversion at boundaries, Rayleigh/head waves) for the substrate's elastodynamic sector — the measurement-sibling alongside the EE rows of [`translation-circuit.md`](translation-circuit.md).

> **Architecture note.** This spoke follows the [hub-and-spoke rule](README-architecture.md): rows map the discipline (seismology/elastodynamics) to the substrate-native hub, never to a sibling discipline. Every row carries a **means-test receipt**, an **Ax3-compatibility tag**, and a **provenance class** (`consistency-vs-emergence`). Cross-discipline rows are consistency/import-class by construction (a sibling discipline is an external anchor, not an AVE-distinct chord).

## Validated rows (means-test receipt on file)

| Elastodynamics / seismology | AVE (substrate-native hub) equivalent | Means-test receipt | Ax3-compat | Provenance |
|---|---|---|---|---|
| **P/S far-field partition** of an isotropic (Poisson) elastic solid — Aki–Richards moment-tensor radiation | **A1/T2 far-field radiation partition**: A1/bulk-dilatation (longitudinal, P) vs T2/shear-transverse (S) from a rotating mass quadrupole; the substrate's derived angular partition $\mathcal{A}_{ang}=I_P/I_S=(8\pi/15)/(4\pi/5)=2/3$ is the inverse of the *identical* P/S angular integrals | $E_S/E_P=(I_S/I_P)(V_p/V_s)^5=(3/2)(\sqrt3)^5\approx 23.4$ — **means-test PASS at value level** (exact textbook agreement, external non-AVE anchor; not order-of-magnitude) | **CLEAN** — a far-field radiative port is an Ax3-legal loss channel (the substrate stores-and-returns in bulk; radiation is a boundary/radiative port, never a bulk resistor) | **consistency** (external anchor; ★**reads for Q1 Reading A** since the 2026-07-20 revert — [`port-register.md`](../port-register.md):93 verbatim: *"now reads for Reading A: a generic isotropic elastic solid"* **does** radiate its P/bulk channel copiously, which is the structure #761 found AVE's vacuum has, so no generic-elasticity suppression rescues the framework and *"the pulsar exclusion is LIVE against the framework"*. *(Stale label corrected 2026-08-07; was "sharpens Q1 Reading B — … the vacuum's bulk-port suppression cannot come from generic elasticity".)*) 🔴 **[DEMOTED 2026-08-11 — R40-B1; note at EOF]** |

**Source (verify-before-cite, two-method, at build):** merged **PR #753** (`research/2026-07-20_q1-pulsar-hardening.md` §1 the $8\pi/15$ / $4\pi/5$ integrals, §6 the $E_S/E_P\approx 23.4$ receipt) — `gh pr view 753` merged 2026-07-20. Already landed in the EE spoke as a ⚠ cross-discipline entry: [`translation-circuit.md`](translation-circuit.md) §4 (line 157) + §6 means-test #28. Companion: [`port-register.md`](../port-register.md) (the A1/T2 channels + the OPEN Q1 bulk-radiation row).

> **Flag-don't-fix — duplicate home.** This P/S row currently lives in BOTH this spoke and the EE spoke ([`translation-circuit.md`](translation-circuit.md) §4/§6 #28, ⚠-tagged "cross-discipline / NOT EE"). Per the [hub-and-spoke corollary](README-architecture.md) §3, its discipline home is HERE (elastodynamics); the circuit-spoke entry should be relocated to a pointer — an **auditor-lane cleanup, not done here**. Both cite the same merged source (#753), so this is consistency-class duplication, not a contradiction.

## Candidate / watch rows (no means-test yet — do NOT treat as validated)

The seismology external-anchor toolkit was opened as a **posture-B watch candidate** (Grant-gated, watch-not-mint) at the #753 landing (`_orchestration/index.md` §2026-07-20; `q1-pulsar-hardening.md` §6 routed follow-on ii). These are correspondences the elastic-medium sibling supplies but which have **no AVE means-test on file yet**:

| Seismology anchor | Candidate substrate equivalent | Status |
|---|---|---|
| Mode conversion at a boundary (P↔S at an impedance contrast) | Mode conversion at a $\Gamma$-wall (A1↔T2 at a substrate impedance boundary) | **WATCH** — no means-test; candidate only |
| Rayleigh / boundary (surface) waves | Boundary-localized substrate modes | **WATCH** — no means-test; candidate only |
| Evanescent head waves (refracted along a fast interface) | Evanescent modes on the gapped/fast branch | **WATCH** — no means-test; candidate only |

## Owed / flagged rows (surfaced, not fabricated)

Per **flag-don't-fix** + **verify-before-cite**: two rows named in this batch's dispatch brief could **not** be seeded because they have no verified merged source at build. Recorded here, not invented:

- **"soft-mode / ring-down" row** — the ring-down content in the corpus (`research/2026-07-20_jomega-derivation_result.md`, PR #751) is an **undriven ring-down explicitly labeled POST-HOC CHARACTERIZATION, NOT in the frozen prereg** (§4.2). It is not a validated elastodynamics translation row. Not seeded; routed for a proper derivation if the correspondence is wanted.
- **"Gibbs–Thomson / precipitate" row** — `grep -rn "gibbs.thomson"` over `research/ manuscript/` returned **0 hits** at build (2026-07-20). The precipitate/"matter precipitation" content that exists (`dark-wake-bemf-foc-synthesis.md`, moving-front freeze-in) is a **materials/metallurgy** concept and belongs to [`translation-materials.md`](translation-materials.md) (curvature-dependent solubility is a metallurgy anchor), not elastodynamics. Not seeded; surfaced for Grant/auditor adjudication of where (if anywhere) it lands.

> ↗ See also: [Materials / Metallurgy Translation](translation-materials.md) — the sibling new spoke (quench/anneal, Kibble–Zurek, residual stress); [Circuit / EE Translation](translation-circuit.md) — the privileged operational spoke; [Architecture](README-architecture.md) — the hub-and-spoke rule.

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:19`** — *"A1/T2 far-field radiation partition: A1/bulk-dilatation (longitudinal, P) vs T2/shear-transverse (S) from a rotating mass quadrupole"*
  Stamped in place at `:19`.
  **Why it dies (audited row rationale, verbatim):** The spoke's one validated row: the substrate-side member (a bulk far-field radiation channel) is void; means-test "PASS at value level" loses its substrate referent; the "reads for Q1 Reading A / exclusion LIVE" provenance cell re-reads as the import's self-exclusion. Covers the :11 header ("partitions ... exactly as an isotropic elastic solid") and :21 source note.
  **Also covered by this demotion** (named in the audited row; not separately stamped): `:11`, `:21`.

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
