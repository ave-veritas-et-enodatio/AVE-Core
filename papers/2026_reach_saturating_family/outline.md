# REACH PAPER — outline + claim inventory [PHASE 1: STRUCTURE ONLY]

**Working title (candidate 1 — see §5):** *Atomic-Precision and Laboratory
Constraints on Saturating-Field Nonlinear Electrodynamics: A Family Exclusion Map*

**Status:** PHASE-1 SKELETON. Outline + claim inventory + exclusion-map mock ONLY.
NO paper prose, NO new physics derivations. Every quoted value is verbatim-verified
against the corpus (two methods) or an external citation; anything unsourced is in
the NEEDS-DERIVATION list (§7), NOT in the paper.

**Register:** sober, falsification-first, zero triumphalism. The main result is a
GENERAL nonlinear-electrodynamics (NLED) constraint, readable by any NLED referee
with ZERO framework dependence. The framework's own saturating branch appears only
as ONE worked member of the family — and its self-exclusion is the demonstration
that the map has teeth.

**Keith's sequencing (Grant-ratified):** a GENERAL NLED-constraint result FIRST;
the framework's branch appears only as one worked member. Rigorous spine: the
zero-birefringence subfamily is COMPLETELY CLASSIFIED (Russo–Townsend 2023 —
exactly four members: Born–Infeld, Plebański, reverse-B-I, extreme-B-I; only B-I
has a Maxwell weak-field limit), so parts of the map are complete-enumeration
arguments, not surveys.

---

## §1. Section skeleton (one-paragraph abstract per section)

> **1-A. Abstract.** Saturating-field nonlinear electrodynamics — constitutive laws
> in which the vacuum response softens (or stiffens) toward an absolute field limit
> — form a family with a 90-year lineage (Born–Infeld 1934). We show that
> atomic-scale precision spectroscopy (the muonic-hydrogen 2S–2P Lamb shift
> foremost) plus existing laboratory optical/birefringence nulls constrain this
> family *as a family*: each member is a coefficient–scale pair, and we map which
> members survive which constraint windows. The map has a rigorous spine — the
> zero-birefringence subfamily is completely classified (four members; only
> Born–Infeld reduces to Maxwell at weak field), so several cells are
> complete-enumeration results rather than surveys. We show that a saturating
> continuum static-field law with no length floor is excluded non-perturbatively by
> muonic hydrogen, and that this exclusion is a *shared* constraint on the whole
> family, not an adjudication of one member against another. We work one member —
> a numerator-softening elliptic branch — through every window explicitly,
> including its own exclusion, as a demonstration that the map's teeth are real.
> [CLASS: this abstract makes theorem-class + computation-class + consistency-class
> claims only; no emergence claim.]

> **1-B. §I Introduction — the saturating-field family and why it is now
> constrainable.** Frames NLED saturation as a family (Born–Infeld ancestor; the
> general coefficient–scale-pair parameterization), states the thesis (atomic +
> lab data constrain the family), and previews the completely-classified
> zero-birefringence spine. Zero framework dependence. [CLASS: exposition.]

> **1-C. §II The family, parameterized.** Defines a saturating-field constitutive
> law by its weak-field coefficient (the O(A²) response) and its saturation scale
> (the ceiling field E_c / b). Introduces the coefficient–scale-pair coordinate.
> States the completely-classified zero-birefringence subfamily (RT 2023: four
> members) as the rigorous backbone and situates birefringent saturating forms
> (generic Born–Infeld-*type*, and constructed representatives — see the
> NEEDS-DERIVATION flag §7-F) around it. [CLASS: theorem (RT enumeration) +
> exposition.]

> **1-D. §III The constraint windows.** Four windows, each a published precision
> measurement or a forward experiment: (W1) muonic-H 2S–2P static-sector Lamb
> shift; (W2) high-Z (U91+) no-real-solution / incomputability; (W3) static-B
> ellipsometry nulls (PVLAS/BMV); (W4) the pump-on E-route (forward column). Each
> window is stated in *its own* measured terms with the external citation.
> [CLASS: computation (window bounds) + external-data.]

> **1-E. §IV The exclusion map (the organizing artifact).** The table of §2:
> rows = family members, columns = windows, cells = survives / excluded / untested
> with the constraining mechanism named, and each cell honestly tagged
> complete-enumeration vs model-dependent. [CLASS: the synthesis; cell classes
> per §3.]

> **1-F. §V The worked member — a numerator-softening elliptic branch (the map's
> teeth).** One member carried through every column, INCLUDING its own
> non-perturbative exclusion at W1 (muonic-H) and its incomputability at W2 (U91+),
> and its survival at W3 (static-B, separate sector) and its distinct forward
> signal at W4 (E-route). Presented soberly as the demonstration that the map
> excludes real theories, its own included. [CLASS: computation +
> forward-prediction; the self-exclusion is honest closure.]

> **1-G. §VI What the map does NOT constrain (honest limits).** Design in §4:
> sub-pitch / lattice-scale accounting; dynamic-sector behavior of members; and
> anything resting on the continuum extrapolation the gauntlet killed — including
> the worked member's own static branch. [CLASS: honest-limits / scope.]

> **1-H. §VII Conclusion.** The family is constrained as a family; the map is a
> reusable instrument (any new saturating law drops into a coefficient–scale cell
> and reads its verdict); the completely-classified spine makes several verdicts
> enumeration-hard. [CLASS: synthesis.]

> **1-I. Appendix A — the muonic-H static-sector bracket integral (method).** The
> reproducible method behind W1: the analytic 1/r⁵ tail, the D-turnover branch
> boundary, the two-independent-code-path reconciliation. [CLASS: computation /
> method; self-contained, external inputs only.]

---

## §2. THE EXCLUSION-MAP TABLE MOCK (the paper's organizing artifact)

**Coordinates.** Rows = family members (coefficient–scale pairs). Columns =
constraint windows. Cells = `SURVIVES` / `EXCLUDED` / `UNTESTED`, each with the
constraining mechanism named and a class tag: **[E]** = complete-enumeration result
(theorem-grade, holds for the whole named subfamily), **[M]** = model-dependent
(holds for the specific member/representative as computed), **[X]** = external-data
consistency (published null), **[F]** = forward (not yet measured).

**Window legend.**
- **W1 — muonic-H static sector.** The 2S–2P Lamb shift (extracted 2P₁ⱼ₂−2S₁ⱼ₂
  interval `202.3706(23) meV`, Antognini/CREMA 2013) vs the member's induced static
  level shift. Window (1σ) = `2.3 µeV`.
- **W2 — high-Z no-real-solution.** Whether the member's constitutive law has a real
  solution in the near-nucleus Coulomb field of a high-Z ion (U91+, Z=92): a
  reality/computability test, not a µeV-fit.
- **W3 — static-B ellipsometry nulls.** PVLAS/BMV static-B birefringence nulls:
  does the member predict a nonzero static-B `Δn`?
- **W4 — pump-on E-route (FORWARD column).** The optical-pump / X-ray-probe
  differential-birefringence measurement: does the member predict a distinct
  tree-level signal separable from QED and from exact B-I?

**Table mock (illustrative structure; magnitudes carried where corpus-verified,
"?" where a member's window verdict is NEEDS-DERIVATION — see §7):**

| member (coeff–scale pair) | W1 muonic-H static | W2 high-Z (U91+) | W3 static-B nulls | W4 pump-on E-route (fwd) |
|---|---|---|---|---|
| **Born–Infeld** (stiffening, `−½` denom; Maxwell weak-field limit) | UNTESTED-here [M] — stiffening branch; static-sector shift is a distinct computation from the softening branch, NOT run in this corpus (§7-A) | SURVIVES [M] — denominator form `D=E/√(1−(E/b)²)` stays real for all E (stiffens, no turnover); reality is not the B-I failure mode | SURVIVES [E] — exact B-I is the zero-birefringence theory (Boillat 1970; RT 2023): both polarizations share one light cone in any constant background → `Δn=0` static-B | SURVIVES / DISTINCT [E,F] — exact B-I predicts EXACTLY ZERO differential birefringence on the pump route; this is the leg that separates it from the softening member and from QED (three-way discriminator) |
| **Plebański** (zero-bir member; NO Maxwell weak-field limit) | ? [NEEDS-DERIVATION §7-B] — no weak-field Maxwell limit ⟹ the standard atomic perturbative bracket may not apply as-worked; static-sector shift not computed | ? [NEEDS-DERIVATION §7-B] | SURVIVES [E] — member of the RT zero-birefringence four; `Δn=0` static-B by construction | ? [F, NEEDS-DERIVATION §7-B] — differential-bir verdict on the propagating pump not computed (constant-background single-cone only) |
| **reverse-Born–Infeld** (zero-bir; NO Maxwell weak-field limit) | ? [NEEDS-DERIVATION §7-B] | ? [NEEDS-DERIVATION §7-B] | SURVIVES [E] — RT zero-birefringence four | ? [F, NEEDS-DERIVATION §7-B] |
| **extreme-Born–Infeld** (zero-bir; NO Maxwell weak-field limit) | ? [NEEDS-DERIVATION §7-B] | ? [NEEDS-DERIVATION §7-B] | SURVIVES [E] — RT zero-birefringence four | ? [F, NEEDS-DERIVATION §7-B] |
| **elliptic softening branch** (the worked member; `+½` num; `S=√(1−(E/E_c)²)`, `E_c≈1.13e17 V/m`; Maxwell weak-field limit) | **EXCLUDED [M]** — non-perturbatively: induced 2P−2S shift `[1.5e6, 2.3e7] µeV` continuum / `[4.9e4, 6.2e5] µeV` lattice-scoped, i.e. `~2e4×` the `2.3 µeV` window even at the smallest variant; overshoots the *entire* 202.37 meV interval. Mechanism: `1/r⁵` near-nucleus enhancement surviving the `ℓ_node` cutoff | **EXCLUDED / INCOMPUTABLE [M]** — at U91+ `A²=(E/E_c)²=12.6>1`: NO real solution over 72.5% of the 1s density; the continuum kernel has no solution at all near-nucleus | SURVIVES [X] — static-B transparency by a SEPARATE (magnetic) sector: circulation-keyed `S_µ=1` for static B → `Δn_µ=0`; consistent with PVLAS/BMV | SURVIVES / DISTINCT [F] — predicts a large tree-level differential `~3.75π/α²` above QED; separable from QED (loop) AND from exact B-I (zero) in one pump-on shot |
| **generic Born–Infeld-*TYPE*** (birefringent; representative, NOT the exact 1934 theory) | ? [NEEDS-DERIVATION §7-C] — depends on the specific type-member coefficient–scale pair | ? [NEEDS-DERIVATION §7-C] | GENERICALLY EXCLUDED-from-transparency [E-adjacent] — generic B-I-*type* members DO birefringe (zero-bir is the exact theory's uniqueness, RT 2023); a nonzero static-B `Δn` is then testable against PVLAS/BMV | ? [F, NEEDS-DERIVATION §7-C] |
| **tanh saturating form** (constructed representative; birefringent) | ? [NEEDS-DERIVATION §7-F — this member is NOT in the corpus] | ? [NEEDS-DERIVATION §7-F] | ? [NEEDS-DERIVATION §7-F] | ? [NEEDS-DERIVATION §7-F] |
| **rational saturating form** (constructed representative; birefringent) | ? [NEEDS-DERIVATION §7-F — this member is NOT in the corpus] | ? [NEEDS-DERIVATION §7-F] | ? [NEEDS-DERIVATION §7-F] | ? [NEEDS-DERIVATION §7-F] |

**Honest cell-class summary.**
- The **W3 zero-birefringence column is the enumeration-hard spine [E]**: the four
  RT members are `Δn=0` static-B *by classification* (Boillat 1970 uniqueness +
  RT 2023 completeness), and generic B-I-*type* members birefringe *by the same
  classification* (zero-bir is exactly the four). These cells are theorem-grade.
- The **elliptic-branch row is fully computed [M/X/F]** — its W1/W2 exclusions are
  the worked-member teeth (two independent code paths + live ReconcileGate,
  `clm-sve3xc` solidity 0.80).
- **Every `?` cell is a NEEDS-DERIVATION item (§7), not a paper claim.** The map
  ships with the `?` cells shown as open — that honesty is part of the instrument.

---

## §3. CLAIM INVENTORY (every claim the paper will make)

Each claim: statement · CLASS (theorem / computation / consistency / forward) ·
PROVENANCE (corpus file + claim-id + solidity band, or external citation). Claims
with no source are in the NEEDS-DERIVATION list (§7), NOT here.

| # | claim (paper will assert) | class | provenance (solidity) |
|---|---|---|---|
| C1 | The zero-birefringence NLED subfamily is completely classified: exactly four members — Born–Infeld, Plebański, reverse-B-I, extreme-B-I — and B-I is the unique member WITH a Maxwell weak-field limit. | THEOREM | EXTERNAL: Russo & Townsend, JHEP 01 (2023) 039, arXiv:2211.10689 (Crossref DOI + arXiv verified in Letter refs.bib `RussoTownsend2023`; verbatim in Letter `main.tex:100-104,632-635`). |
| C2 | Exact Born–Infeld predicts zero birefringence: both photon polarizations share one effective light cone in any constant electromagnetic background (single-cone uniqueness). | THEOREM | EXTERNAL: Boillat, J. Math. Phys. 11(3), 941 (1970), DOI 10.1063/1.1665231 (Crossref-verified, Letter `Boillat1970`); RT 2023. Verbatim in Letter `main.tex:628-644`. |
| C3 | Saturating-field NLED is a family with a Born–Infeld (1934) ancestor; a general member is a coefficient–scale pair (weak-field O(A²) response coefficient + saturation ceiling field). | CONSISTENCY / EXPOSITION | EXTERNAL: Born & Infeld, Proc. R. Soc. A 144, 425 (1934), DOI 10.1098/rspa.1934.0059 (Letter `BornInfeld1934`). Family framing corpus-grounded: `manuscript/ave-kb/common/historical-precedents.md` "Root 3" (consistency-class, not a derivation). |
| C4 | A saturating continuum static-E constitutive law with no length floor, applied to the muonic-H near-nucleus Coulomb field, induces a 2S–2P level shift that overshoots the CREMA 2.3 µeV window by 4–7 orders of magnitude — non-perturbatively (the correction exceeds the entire 202.3706(23) meV interval). | COMPUTATION | CORPUS: `research/2026-07-05_problem3-muonic-lamb_RESULT.md` (bands `[1.5e6,2.3e7]`/`[4.9e4,6.2e5]` µeV); claim-id `clm-sve3xc` (solidity **0.80**). EXTERNAL window: Antognini/CREMA 2013, Science 339, 417, DOI 10.1126/science.1230016. |
| C5 | The exclusion is robust to a lattice-pitch cutoff: the super-pitch remainder ALONE overshoots the window by `~2×10⁴×`. | COMPUTATION | CORPUS: round-3 finding [18] band-split, `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md` §9 (driver `band_split_C_iii`, standing pin test); `clm-sve3xc` rationale. |
| C6 | At high Z (U91+, Z=92) the continuum elliptic kernel has NO real solution over the bulk of the 1s orbit (`A²=(E/E_c)²=12.6>1`; 72.5% of 1s density inside the no-solution radius): the law is incomputable near-nucleus, not merely window-violating. | COMPUTATION | CORPUS: `research/2026-07-05_problem3-muonic-lamb_RESULT.md` "SECONDARY — U91+" + fork-memo §1 Z-table (`A²(U91+)=12.6`); `clm-sve3xc`. |
| C7 | This muonic-H exclusion is a SHARED (whole-family) constraint at atomic scales, not an adjudication of one saturating member against another: any continuum saturating static-E law with no floor faces the same near-nucleus exposure. | CONSISTENCY | CORPUS: `manuscript/ave-kb/common/historical-precedents.md:47` ("B-I is lineage and co-constrained sibling, not defeated rival"; "whole-family constraint"). |
| C8 | For a saturating member with no OWN DC-block mechanism, a held static field is a real operating-point bias that loads the ε-sector (charge-keyed, mean-square, DC-included at leading order) — so the atomic-sector exposure is not contingent on an open keying escape. | CONSISTENCY (input-only band) | CORPUS: `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md` [DERIVED: CHARGE-KEYED]; claim-id `clm-chgky3` (solidity **0.55**, "use as input only, don't build deeper" — srs-C₄₄ cross-lattice borrow gates it). **Cite AT that band; do NOT build headline structure on it.** |
| C9 | The worked elliptic member's static-B sector is TRANSPARENT (a separate, magnetic sector): circulation-keyed `S_µ=1` for static B → `Δn_µ=0`, consistent with PVLAS/BMV nulls. A static-E exclusion does NOT cross-wire into the magnetic sector. | CONSISTENCY | CORPUS: `clm-pvlas1` (solidity **0.80**), `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md`. EXTERNAL nulls: PVLAS (Ejlli 2020, Phys. Rep. 871, 1), BMV. |
| C10 | The pump-on E-route is a THREE-WAY discriminator: the softening member predicts a large tree-level differential (`~3.75π/α²` above QED), QED predicts its small one-loop signal, and exact B-I predicts EXACTLY ZERO — separable in one pump-on measurement. | FORWARD PREDICTION | CORPUS: `clm-pp3qwf` (solidity **0.80**), Letter `main.tex` signature § (FIX-2 / DEFECT-C). EXTERNAL: HIBEF/ReLaX LoI (BirefHibefLoI2025); QED Heisenberg–Euler/Karbstein2015. |
| C11 | Exact B-I shares the static-B transparency (C2/C9), so a `Δn` polarimeter (PVLAS/BMV) alone does NOT separate the softening member from exact B-I on the magnetic route; the E-route (C10) is what separates them. | CONSISTENCY | CORPUS: Letter `main.tex` (FIX-2 MINOR-1 transparency-conflation correction); RT 2023 / Boillat 1970. |
| C12 | The single-cone (zero-bir) statement is proved for CONSTANT backgrounds; carrying it to the propagating pump uses an explicit locally-constant-field (geometric-optics) scoping (keV probe wavelength ≪ optical pump variation scale). | THEOREM (scoped) | CORPUS: Letter `main.tex` (FIX-2 DEFECT-C license); EXTERNAL: Boillat 1970 / RT 2023 (constant-background scope). |

**Solidity-band honesty note (for Grant/Keith):** the load-bearing computed claims
(C4/C5/C6 = `clm-sve3xc` 0.80; C9 = `clm-pvlas1` 0.80; C10 = `clm-pp3qwf` 0.80) are
all at the 0.80 band. C8 (`clm-chgky3`) is at **0.55, input-only** — it is cited to
close the "is the exposure contingent on an open keying escape?" question, but NO
headline claim rests on it; if a referee pushes on C8, the fallback is that the
whole-family exposure (C7) does not require C8 at all (it is a floor-independence
argument). This is the KEEP-BOTH posture: C7 stands without C8.

---

## §4. HONEST-LIMITS SECTION DESIGN (§VI of the paper)

What the map does NOT constrain — stated as first-class content, not a hedge:

- **L1 — Sub-pitch / lattice-scale accounting.** The dominant band of the worked
  member's overshoot magnitude (`~103%`) rides on the sub-pitch region
  `[159.6, 386.2] fm` where a continuum gradient is below one node pitch. The map's
  *verdict* does not depend on it (the super-pitch remainder alone excludes, C5),
  but the map does NOT resolve whether the sub-pitch continuum integral is the
  right lattice-scale accounting — that is the open [B-AVE] lattice-scale
  regime-boundary arm. PROVENANCE: round-3 §9 finding [18].
- **L2 — Dynamic-sector behavior of members.** Every W1/W2/W3 window is a STATIC or
  quasi-static sector. The map does NOT constrain the dynamic (radiative, `∂_t≠0`)
  behavior of any member; the worked member's own AC pump–probe prediction (W4) is
  a SEPARATE sector from its excluded static branch, and a static exclusion is
  silent on it. PROVENANCE: fork-memo §3 [C] survival ledger; Letter sector-scope
  paragraph.
- **L3 — The continuum extrapolation the gauntlet killed — INCLUDING the worked
  member's own static branch.** The map's teeth are demonstrated *by* the worked
  member's own static-branch exclusion. Stated plainly: the elliptic softening
  branch's continuum static-E law is EXCLUDED at atomic scales (C4/C6); the map
  does not rescue it, and the paper does not claim to. Anything resting on
  extending a saturating continuum law below the near-nucleus scale is outside what
  the map licenses. PROVENANCE: `clm-sve3xc`; `historical-precedents.md:47`.
- **L4 — The `?` cells.** The map ships with open cells (§2): the three
  no-Maxwell-limit zero-bir members (Plebański, reverse-B-I, extreme-B-I) at W1/W2,
  the generic B-I-type row at W1/W2/W4, and the constructed tanh/rational
  representatives at every column. These are NEEDS-DERIVATION (§7), shown open. The
  map does not claim verdicts it has not computed.
- **L5 — Self-energy / finiteness properties across branches.** The map is a
  field-response/level-shift instrument; it does NOT compare self-energy or
  finiteness properties across branches (that is the Born–Infeld design axis, a
  different question). PROVENANCE: Letter `main.tex` §"Family context" scope clause.

---

## §5. VENUE + LENGTH PROPOSAL + TITLE CANDIDATES

**Document class.** This is a methods/constraints paper (a reusable exclusion-map
instrument + one worked member), NOT a discovery Letter. It is longer than a Letter
and reference-heavy. Estimated length: full-article, `~8–12 pages` two-column
(the birefringence Letter is already 9 pp as a Letter; this superset is an article).

**Candidate venues (3, with fit rationale):**

1. **Physical Review D (regular article).** Best fit. PRD carries strong-field /
   NLED / precision-test constraint papers; the muonic-H + NLED + laboratory-null
   combination is squarely in scope; no length pressure as a regular article
   (vs the PRD-Letter cap the birefringence Letter strains against). Referee pool
   overlaps the NLED-constraints literature (Fouché 2016, Ejlli 2020 are PR-family).
2. **New Journal of Physics (NJP).** Good fit for a methods/map paper with a
   forward-experiment column; open-access (no paywall — widest reader reach);
   NJP already carries the XFEL-birefringence line (Karbstein 2021). Length-tolerant.
3. **European Physical Journal C / Journal of High Energy Physics (JHEP).** Fit for
   the theorem-spine framing (the RT 2023 classification is a JHEP paper); a
   referee here is most likely to already know the zero-birefringence enumeration.
   Trade-off: less natural home for the atomic-precision (muonic-H) window than PRD.

**Recommendation to surface (Grant decides):** target **PRD regular article** as
primary (widest referee overlap across all four windows); NJP as the open-access
fallback if paywall-free reach is weighted higher.

**Title candidates (3):**

1. *Atomic-Precision and Laboratory Constraints on Saturating-Field Nonlinear
   Electrodynamics: A Family Exclusion Map*
2. *A Family Exclusion Map for Saturating-Field Electrodynamics: From the
   Muonic-Hydrogen Lamb Shift to Vacuum Birefringence*
3. *Which Saturating Vacua Survive? Mapping the Nonlinear-Electrodynamics Family
   Against Atomic and Optical Precision Data*

---

## §6. provenance.md skeleton

See sibling file `provenance.md` (section structure mirrors the birefringence
Letter's `provenance.md`: number-by-number map, external-reference verification,
cell-class audit, discipline tags, FLAGGED-FOR-GRANT, build+verify).

---

## §7. NEEDS-DERIVATION LIST (claims the paper may WANT but has NO source for yet)

Anything here is EXCLUDED from the paper until derived + verified. Each item is a
gated follow-on, not a phase-1 deliverable.

- **§7-A — Born–Infeld static-sector muonic-H shift (stiffening branch).** The W1
  cell for B-I is UNTESTED-here: the muonic bracket integral was run for the
  *softening* elliptic branch only. The stiffening B-I response (`D=E/√(1−(E/b)²)`,
  no turnover) is a DISTINCT computation and is not in the corpus. Needs: the B-I
  static-sector level-shift computation with B-I's own `b`.
- **§7-B — The three no-Maxwell-limit zero-bir members at W1/W2/W4.** Plebański,
  reverse-B-I, extreme-B-I lack a Maxwell weak-field limit, so the standard atomic
  perturbative bracket may not apply as-worked; their static-sector shifts,
  high-Z reality, and propagating-pump differential-bir verdicts are NOT computed.
  Needs: a weak-field-limit-free treatment (or an explicit statement that the
  atomic window is inapplicable to a non-Maxwell-limit member — itself a result).
- **§7-C — Generic Born–Infeld-*type* members at W1/W2/W4.** "Generic type-member
  birefringes" (W3) is enumeration-grounded, but the specific W1/W2/W4 verdicts
  depend on the type-member's coefficient–scale pair and are not computed. Needs:
  a representative type-member's windows, OR a parameterized bound over the
  coefficient–scale plane.
- **§7-D — A coefficient–scale-plane bound (the map as a continuous region, not a
  row list).** The strongest form of the paper would show a REGION of the
  coefficient–scale plane excluded by each window, so any member reads its verdict
  by its coordinates. Not derived; the corpus has point-computations
  (the elliptic branch at its specific `E_c`), not the plane bound. Needs: the
  window bound as a function of (coefficient, scale).
- **§7-E — The W3 external nulls quantified per member.** The paper cites PVLAS/BMV
  static-B nulls (consistency, C9/C11) but does not yet carry the numerical null
  bound (the measured `Δn` upper limit) against a per-member predicted static-B
  `Δn`. Needs: the published PVLAS/BMV `Δn` bound number + per-member prediction.
  (External-data retrieval item; verify Crossref before citing.)
- **§7-F — The tanh + rational saturating representatives.** **FLAG (verify-before-
  cite / flag-don't-fix):** the brief characterizes the family table as containing
  "elliptic / Born–Infeld / tanh / rational as coefficient–scale pairs" and
  attributes it to the fork memo. **A two-method grep (the two named files +
  corpus-wide) finds NO tanh or rational member anywhere in the corpus.** The fork
  memo contains ONLY the elliptic kernel's exposure; `historical-precedents.md`
  "Root 3" frames the B-I family and elliptic branch but lists no tanh/rational
  member. So the tanh and rational rows are CONSTRUCTED REPRESENTATIVES the paper
  would introduce as illustrative birefringent saturating forms — they are NOT
  corpus-sourced and their window verdicts are entirely NEEDS-DERIVATION.
  Surfaced for Grant/Keith: either (a) derive these two representatives' windows as
  new work, or (b) drop them and present the map on the corpus-grounded rows only
  (RT four + elliptic branch + generic B-I-type). Recommend (b) for a first
  submission; (a) as a strengthening follow-on.

---

## Discipline log (phase 1)

- **verify-before-cite:** every solidity band (`clm-sve3xc` 0.80, `clm-pvlas1` 0.80,
  `clm-pp3qwf` 0.80, `clm-chgky3` 0.55) re-grepped from `claims.jsonl` +
  `claim-quality.md` at worktree HEAD; the RT four-member classification + Boillat
  uniqueness read verbatim from the Letter's `main.tex` + `refs.bib` this session.
- **flag-don't-fix:** §7-F — the tanh/rational family table the brief cites does NOT
  exist in the corpus (two-method grep); surfaced, not silently invented as
  corpus-sourced.
- **consistency-vs-emergence:** the whole map is theorem/computation/consistency/
  forward-class; NO emergence claim. The worked member's `E_c` is CODATA-derived
  through α, m_e (Letter honesty ledger) — falsification/consistency-class, matching
  `clm-sve3xc`.
- **Rule 11 honest closure:** the worked member's self-exclusion (C4/C6) is
  presented AS the demonstration the map has teeth — the falsification is the
  result, not something to rescue.
- **pure-AVE-corpus:** no external-context references of any kind; the paper is
  pure NLED physics; the framework's branch is one worked member,
  framework-name-optional.
