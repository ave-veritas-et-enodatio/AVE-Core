# FROZEN PREREG — v1 spin-mapping adjudication (ω_R AND τ vs corrected Kerr)

**Lane:** v1-spin-mapping-adjudication (routed follow-on of PR #774's § FORK-REOPEN)
**Date frozen:** 2026-07-20
**Branch:** `research/v1-spin-mapping-adjudication` (off `origin/main`)
**Status of THIS document:** frozen reference + convention + comparators + bins. Contains **no**
verdict. The re-run + adjudication land in a *separate later commit* against the bins frozen here.
**Upstream:** PR #774 (`fix/kerr-qnm-table-correction` @ `7aaec46c`, UNMERGED — every #774 cite below
is tagged `[branch @ 7aaec46c]`; do **not** assume merged).

---

## 0. The question (the reopened fork's evidence)

PR #774's honest re-adjudication walked back the banked spinning-remnant match as a **MATCH-ARTIFACT**
(source-vs-detector frame mixing × a genuine below-Kerr deficit) and, in its § FORK-REOPEN
`[branch @ 7aaec46c]`, surfaced that the **retired v1** spin mapping sits **+2.63% mean** vs corrected
Kerr on the frozen C-1 dimensionless comparator — *inside* the `MATCH-SURVIVES |D̄| < 3%` band — while
the **retained v2** fails at −9.53%. The 2026-05-18 Option-A adjudication that retired v1 rode the SAME
two errors #774 corrects (corrupt Kerr QNM table + frame mixing), so the v1→v2 fork is **reopened**.

**This lane asks, under a properly frozen adjudication:** does the pre-artifact v1 spin mapping
`x_sat,v1 = 7·r_ph⁺/3M` (the whole-cavity-compliant single-component form) match TRUE (corrected)
Kerr (2,2,0) across the banked catalog events — on **BOTH** observables (ω_R **and** the damping/τ
side) — the evidence Grant's v1↔v2 fork re-ruling needs?

**The FORK RULING itself remains Grant's.** This lane produces the frozen evidence brief, not the ruling
(standing Grant authorization: derivation-class proceeds; the fork verdict is Grant's).

### Known-at-freeze prior (disclosed, per anti-seduction)

- The **ω_R** side is a **review-produced prior**: #774's § FORK-REOPEN `[branch @ 7aaec46c]` already
  computed v1 = **+2.63% mean** (per-event +2.24% / +2.50% / +3.17% at a* = 0.64 / 0.67 / 0.74) and
  v1 = **+6.5%** at a* = 0.95. This lane REPRODUCES that number deterministically and re-verifies the
  corrected Kerr reference by an independent in-lane second method (BCW-2006 analytic fit) — it does not
  discover it. **The freeze's value is the τ side + the extended set + the proper adjudication grade.**
- The **cold Q = ℓ = 2** topological damping model (`qnm-quality-factor.md`, clm-395gps) is
  **spin-independent** — a structural fact of the model, stated here so it is not mistaken for a
  post-hoc verdict.

### ★ ANTI-SEDUCTION (frozen)

v1-resurrection is now the **seductive direction**: it rescues the ringdown story AND Grant's original
formula. The day's pattern (6/6 lanes caught a seductive rescue) governs this freeze:
1. Every number in the verdict **ships with its computation** in the committed deterministic driver.
   No prose-string conclusions; the verdict cites frozen-criteria driver outputs only.
2. The lane **declines to fabricate** any under-specified corpus input (e.g. a hand-tuned frame-dragging
   Ω) to manufacture a τ match. An under-specified input is reported as UNDETERMINED, not filled.
3. A decisive split (ω_R matches, τ does not) is the discipline working — recorded, not rescued.

---

## 1. Corrected Kerr (2,2,0) reference (verified two independent methods)

The corrected Kerr reference is #774's three-source table `[branch @ 7aaec46c]`
(`research/2026-07-20_kerr-table-correction_prereg-FROZEN.md` §0): {`qnm` package [Stein 2019] +
Berti-Cardoso-Will 2006 analytic fit + #772 auditor from-scratch Leaver}. **This lane re-verifies it
in-lane as the second method** by the BCW-2006 fitting formulae (Phys.Rev. D73 064030):

- ω_R:  `ω_R·M = 1.5251 − 1.1568·(1−a*)^0.1292`
- Q:    `Q = 0.7000 + 1.4187·(1−a*)^(−0.4990)`,  then `ω_I·M = ω_R·M / (2Q)`

The driver prints the BCW-fit values against the hard-coded qnm-verified table and asserts agreement
to **< 1.5%** at every adjudicated spin (the in-lane cross-check). Both observables are re-verified:
the ω_R table (the #772 finding) **and** the ω_I table (the additional #774 finding: in-repo ω_I was
high by +11%/+26% at a* = 0.90/0.95).

### Corrected Kerr (2,2,0) reference values (M = 1 geometric units; qnm-verified, `[branch @ 7aaec46c]`)

| a* | event | ω_R·M | ω_I·M | Kerr Q = ω_R/(2ω_I) |
|----|-------|-------|-------|---------------------|
| 0.00 | (cold anchor) | 0.37367 | 0.08896 | 2.100 |
| 0.64 | GW170104 | 0.50819 | 0.08275 | (driver-computed) |
| 0.67 | GW150914 | 0.51986 | 0.08185 | (driver-computed) |
| 0.72 | GW190521 (2nd) | (interp) | (interp) | (driver-computed) |
| 0.74 | GW151226 | 0.55163 | 0.07909 | (driver-computed) |
| 0.81 | GW170729 (2nd) | (interp) | (interp) | (driver-computed) |
| 0.90 | (near-extremal) | 0.67161 | 0.06487 | (driver-computed) |
| 0.95 | (near-extremal) | 0.74632 | 0.05315 | (driver-computed) |

Q-column values are left driver-computed on purpose (no pre-stated verdict). The BCW Q-fit provides the
independent second method for the ω_I side; the extremal ZDM analytic limit (ω_R·M → m/2 = 1, ω_I·M → 0
as a* → 1) is the third, table-free cross-check.

---

## 2. The v1 and v2 spin mappings (both from `ave-merger-ringdown-eigenvalue.md`, clm-395gps)

Shared cold anchor (both v1 and v2, a* = 0): `ω_R·M = ℓ(1+ν_vac)/x_sat = 18/49 = 0.36735`
(ℓ = 2, ν_vac = 2/7, x_sat = 7 from Ax 4 `ε_11(r_sat) = 1`), and the prograde photon orbit
`r_ph⁺(a*) = 2GM/c²·(1 + cos[⅔·arccos(−a*)])` (a* = 0 → 3M; a* → 1 → M).

- **v1 (pre-artifact, whole-cavity compliant):** `x_sat,v1 = 7·r_ph⁺/3M`; `ω_R·M = ℓ(1+ν_vac)/x_sat,v1`.
  Equivalent frequency-ratio form (`ligo-ringdown-driver-design.md` §2):
  `f_ring(a*) = f_ring(0)·r_ph,Schw/r_ph⁺(a*)`, r_ph,Schw = 3M. Closed rational: `ω_R·M = 54/(49·r_ph⁺)`.
- **v2 (retained, two-component rigid-skeleton + compliant):** `x_sat,v2 = 7·[ν_vac + (1−ν_vac)·r_ph⁺/3M]
  = 2 + 5·r_ph⁺/3M`; `ω_R·M = ℓ(1+ν_vac)/x_sat,v2`.

Both reduce to 18/49 at a* = 0. The driver implements both from these forms (no hard-coded eigenvalues
except the qnm-verified Kerr reference).

---

## 3. Frozen comparators (both frame- AND mass-independent — the substrate-native meters)

- **(C-1) ω_R comparator** = the dimensionless eigenvalue ratio, per #774's frozen convention
  `[branch @ 7aaec46c]`: `dev_ωR(a*) = (ω_R·M)_AVE(a*) / (ω_R·M)_Kerr(a*) − 1`. Depends only on the
  (well-measured) final spin a*; sidesteps every mass/redshift/f_obs import and the frame-mixing that
  produced the artifact. `D̄_ωR` = mean over the event set.
- **(C-τ) τ comparator** = the dimensionless quality factor `Q ≡ (ω_R·M)/(2·ω_I·M)`, equivalently the
  dimensionless damping eigenvalue `ω_I·M`. Frame- AND mass-independent (a-function-of-a* only), exactly
  parallel to C-1. `dev_Q(a*) = Q_AVE(a*)/Q_Kerr(a*) − 1`; `D̄_Q` = mean over the event set. **This is the
  new content — v1's τ prediction has never been evaluated against the corrected ω_I table.**

**AVE damping models to be evaluated (frozen enumeration; each model's corpus-specification status is a
FINDING the driver reports, not a criterion):**
- **Model A — cold topological Q = ℓ = 2** (`qnm-quality-factor.md`, clm-395gps). Spin-independent,
  v1/v2-independent, FULLY SPECIFIED. Prediction: `ω_I·M(a*) = (ω_R·M)_AVE(a*)/(2ℓ)`, `Q_AVE = ℓ = 2`.
- **Model B — spin-refined** `ω_I = (ω_R − mΩ)/(2ℓ)` at `r_Ω = r_ph·√(1+ν_vac)`
  (`ave-merger-ringdown-eigenvalue.md` "Kerr Quality Factor"). Requires the frame-dragging rate Ω(a*).
  The driver reports whether Ω is **numerically pinned anywhere in the corpus**. If Ω is not pinned
  (the τ_v1 = 3.5/2.7/1.2 ms were asserted, not coded), Model B is **UNDETERMINED** — the lane declines
  to fabricate an Ω (anti-seduction clause 2). A disclosed reverse-engineered *bound* on Q_v1 from the
  rounded KB τ values may be reported as a non-frozen sensitivity only.

Cold-eigenvalue (a* = 0) survives independently either way (18/49 = 0.36735 vs Kerr 0.37367, −1.69%);
NOT under adjudication here.

---

## 4. Event sets (frozen)

- **PRIMARY (frozen; the banked catalog):** GW150914 (a* = 0.67), GW170104 (a* = 0.64),
  GW151226 (a* = 0.74). C-1 and C-τ depend on a* only; a* imports per GWTC-1.
- **SECONDARY (pre-declared extension; import-tagged a* only):** GW170729 (a* = 0.81, GWTC-1),
  GW190521 (a* = 0.72, GWTC-2 IMBH-class). Both inside the BCW table range (a* < 0.95). These carry an
  `[IMPORT: GWTC-…]` tag on the spin; no f_obs / mass import is used (C-1/C-τ are dimensionless).
- **NEAR-EXTREMAL organizer (frozen; NOT a catalog event — a forward-prediction probe):** a* = 0.90,
  0.95, and the analytic a* → 1 limit. Used to compare v1 vs v2 extremal behavior against the exact ZDM
  limit; routed to Grant as a candidate testable organizer, **not banked**.

---

## 5. FROZEN adjudication bins (criteria set BEFORE the run)

**ω_R (C-1), per event set:**
- **V1-MATCHES(ω_R)** — `|D̄_ωR| < 3%`.
- **V1-FAILS(ω_R)** — `|D̄_ωR| ≥ 5%`.
- (3–5% = marginal, reported per-event.)

**τ (C-τ), stated SEPARATELY (the ω_R and τ verdicts may split):**
- **τ-MATCHES** — `|D̄_Q| < 3%` under a **fully-specified** AVE damping model.
- **τ-FAILS** — `|D̄_Q| ≥ 5%` under the fully-specified model, with no fully-specified rescuing model.
- **τ-UNDETERMINED** — the only model that could plausibly match (Model B) has a corpus-under-specified
  input the lane declines to fabricate.

**Overall bin:**
- **V1-MATCHES** — both ω_R and τ match.
- **V1-FAILS** — both fail.
- **MIXED** — ω_R vs τ split, OR primary-vs-secondary split.
- **UNDETERMINED** — imports too poor for any comparator to decide.

**Rule-11 discipline (frozen):** a decisive negative (or split) here is the discipline working, not a
failure to be rescued. No post-hoc bin redefinition; no dropping the τ criterion to convert a split
into a clean MATCH. The fork RULING is Grant's; this lane hands him the frozen bins' output.

**Provenance-rider (frozen, inherited from #774 / #772 finding 2):** `ν_vac = 2/7` is a corpus INPUT
whose VALUE is GR-imported via K = 2G (PR #261), FORM-derived only; `x_sat = 7` is Ax-4-derived. Any
re-banked eigenvalue floored by these (18/49, 54/49, 54/77) inherits that grade. This lane does not
re-derive ν_vac or x_sat.

---

## 6. v1-provenance question (frozen scope for the grade, not the grade itself)

Leg 4 grades what *derives* `x_sat,v1 = 7·r_ph⁺/3M`: the frequency-ratio ansatz treating the **entire**
cavity as compliant (scaling with the photon-orbit radius, no rigid-skeleton fraction). The driver /
result cite the original derivation chain with claim-id + solidity (clm-395gps, `qnm-quality-factor.md`
+ `ave-merger-ringdown-eigenvalue.md`), pull the register solidity, and NOTE (claim nothing new) whether
the `7/3` factor sits in the same `/7` family as the PPN `/7` couplings (x_sat = 7 saturation multiplier;
r_ph,Schw = 3M). Connections noted; no new claim minted.
