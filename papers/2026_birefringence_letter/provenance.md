# INTERNAL provenance — saturable-vacuum birefringence Letter

**NOT part of the paper.** This is the audit trail the public Letter deliberately
does not carry (pure-physics rule: the paper cites no private repo, no framework
volumes, no program history). Every quantitative claim in `main.tex` maps here to
its corpus source: canonical claim-id, driver, output JSON, and the merged PR.

> 📐 **REVISION-4 (2026-07-04, exposition armor): Appendix A "Derivation of the eigen-indices" + §II pointer.**
> No numbers move — this makes the tensor derivation EXPLICIT so the experimentalist audience does not read the
> stated-not-shown tensor as phenomenological insertion.
> - **Appendix A** shows the full chain, every step displayed (no "it can be shown"): `D_i=ε₀S(u)E_i` (A1) →
>   chain-rule tensor `ε_ij=ε₀S δ_ij + 2ε₀S' E_0i E_0j` with `∂u/∂E_j=2E_j` shown (A2) → `S'(u)=−1/(2E_c²S)` (A3)
>   → eigen-indices `n_⊥=√S=(1−A²)^(1/4)`, `n_∥=√(S−A²/S)=√((1−2A²)/√(1−A²))` (A4/A5) → small-A `1−¼A²`/`1−¾A²`
>   (A6) → `δn_bir≈−½A²`, `δn_iso≈−¼A²` (A7).
> - **Cross-check:** every line matches the OQ-1 derivation `research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`
>   §1 (the canonical DERIVED chain; PR #345). **Re-verified symbolically this session** (sympy): `dε/du=−1/(2E_c²S)`,
>   `2ε'E₀²/ε₀=−A²/S`, `S−A²/S=(1−2A²)/√(1−A²)` (the two n_∥ forms identical), small-A expansions, and `δn_bir/δn_iso→2`
>   — all confirmed. INTERNAL grounding only; the appendix cites nothing private.
> - **§II pointer sentence** (after Eq. 3): "Every coefficient in this paper follows from Eq. (1) by
>   differentiation … no additional parameter or coupling enters anywhere (Appendix A)." — the pre-emptive answer
>   to phenomenological-insertion dismissal.
> - Build: 6→**7 pp** (appendix + refs page; at the 7pp threshold, not over), pdflatex+bibtex+pdflatex×2 clean,
>   zero undefined refs/citations, no large overfull boxes, 11 refs resolve. main.pdf rebuilt + committed. make
>   verify GREEN. Grep-clean of lattice/framework terms. Fresh branch off merged HEAD d357bec9.
>   Grant's five standing decisions UNTOUCHED.

> ⚙️ **REVISION-3 (2026-07-03, reinforcement round): three external-reviewer-driven additions.** Each converts
> an objection into a theorem or a prediction. Public-safe (no lattice/framework terms; grep-clean).
> 1. **Kernel uniqueness (§II.B):** the `√(1−(E/E_c)²)` form is the UNIQUE lossless-oscillator response under a
>    hard-bound + energy-conservation constraint (`E²+E_c²S²=E_c²`, Pythagorean complement); an Lᵖ invariant
>    forces `S=(1−(E/E_c)ᵖ)^(1/p)`, a different curve for every `p`, and only the quadratic (energy) norm `p=2`
>    is selected. **Internal grounding:** the Ax4 buckling-kernel shape-derivation — the √ form is the axial
>    projection of a fixed-arc-length compressible-strut bowing, an α-free geometric theorem (`axiom-register.md`
>    Ax4 `residual_content`/`derived_by`; `research/2026-07-02_axiom4-buckling-kernel_result.md` PR #459,
>    `research/2026-07-02_axiom4-forced_result.md` the L² 1-to-1 map). CITED NOTHING PRIVATE — restated in
>    public oscillator/EE language. Plus: kernel exponent testable at 2nd order (common-mode vs differential
>    leading-order ratio is `p`-dependent — sympy-verified: `p=2` → iso `−A²/4`, `p=4` → iso `−A⁴/8`).
> 2. **Dispersion bound (§II.D):** scale separation `ω_probe/ω_0 = E_probe/(m_ec²) = 9835/511000 ≈ 0.019`
>    (~1.7 OOM below); fractional dispersive correction `~(ω_probe/ω_0)² ≈ 3.7×10⁻⁴` (<0.1%), computed properly.
> 3. **SME/sidereal (§II.D):** SVE classified in the SME preferred-frame photon-sector class (cite Kostelecký-
>    Russell 2011, Rev.Mod.Phys. 83, 11, DOI 10.1103/RevModPhys.83.11, Crossref-verified). NEW PREDICTION:
>    sidereal modulation sidebands at `(v/c)² = (370e3/c)² = 1.523×10⁻⁶` — the model's THIRD falsifiable
>    signature (coefficient / E-B asymmetry / sidereal). Ref added to refs.bib (now 11 refs).
> Build: pdflatex+bibtex+pdflatex×2 clean, 6pp, 11 refs resolve, zero undefined/citation warnings. main.pdf
> rebuilt + committed (standing pattern). make verify GREEN. Fresh branch `analysis/letter-reinforcement` off
> merged HEAD 81180f15. Grant's five standing decisions (headline form, SVE name, author, venue, floors) UNTOUCHED.

> ⚠️ **REVISION-2 (2026-07-03, post-referee): QED-normalization correction landed.** The two-lane hostile
> referee pass (PR #498) found the QED electric leg `(3/45)α²` understated by `1/(2πα) ≈ 21.8` vs the repo's own
> PVLAS-anchored magnetic leg. **Independently re-derived and CONFIRMED** (analytic + numeric): the corrected
> ratio is `7.5π/α² ≈ 4.42×10⁵` (propagating/LoI-matched headline; `15π/α² ≈ 8.85×10⁵` static). The AVE leg is
> UNAFFECTED; falsifier logic survives (AVE ~7 OOM above floor, corrected QED ~4 OOM below). The numbers in the
> tables below marked "(REV-2)" are the corrected values now in the paper. Full reconciliation:
> `research/2026-07-03_birefringence-qed-normalization-correction.md`. Code harness:
> `src/ave/bench/birefringence.py::delta_n_qed_electric_pvlas / coefficient_ratio_differential_pvlas`.
> **Surfaced-beyond-referee (flag-don't-fix): a static-vs-propagating factor of 2** — the referee anchored to the
> static value `15π/α²`; the propagating (LoI-matched, HIBEF-pump-correct, conservative) value `7.5π/α²` is the
> paper's headline. Both stated in the paper.

- **Paper:** `papers/2026_birefringence_letter/main.tex`
- **Canonical claim:** `clm-pp3qwf` (E-route vacuum birefringence)
- **Canonical leaf:** `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`
- **Frozen pre-reg (public artifact draws from this):** `research/2026-07-03_birefringence-hibef-prediction_registered.md` (merged PR #497)
- **Drivers (re-run this session, all reconcile):**
  - `src/scripts/vol_9_device/birefringence_gap1_hibef_feasibility.py` (readout chain, single source of truth)
  - `src/scripts/vol_9_device/birefringence_hibef_scenario_predictions.py` (the scenario table)
  - `src/scripts/vol_9_device/birefringence_prior_art_exposure_scan.py` (CLEAN-FIELD gate + the figure)
- **Merged PRs:** #496 (campaign opening / GAP-1 feasibility), #497 (prediction doc). Worktree HEAD = 66530938.

---

## 1. Number-by-number map (paper claim -> source)

| Paper location | Claim | Source |
|---|---|---|
| Abstract, Eq.(1),(4); §II.B | Kernel `S=sqrt(1-(E/E_c)^2)`; `E_c ~ 1.13e17 V/m` | `ave.core.constants.E_YIELD = V_YIELD/L_NODE` (constants.py:475); live-verified `1.1304e17`. The paper's `E_c` **is** the corpus `E_YIELD`. |
| Eq.(2) | Eigen-indices `n_perp=(1-A^2)^{1/4}`, `n_par=sqrt((1-2A^2)/sqrt(1-A^2))` | `ave.qed.birefringence.birefringence_eigenindices`; leaf :30. |
| Eq.(3) boxed | `delta_n_bir = n_par - n_perp ~ -1/2 A^2` | `ave.bench.delta_n_ave_differential_exact` (birefringence.py:193); leaf :31 (boxed, verbatim match). |
| Eq.(4) | `E_c = sqrt(alpha) E_crit`, `E_crit = m_e^2 c^3/(e hbar)` | constants.py:469 (`E_CRIT`), :475 (`E_YIELD`). `E_crit` live = `1.3233e18`. |
| Eq.(5) | `(E_crit/E_c)^2 = 1/alpha` | `ave.bench.substrate_identity_holds()` = True; live `(E_CRIT/E_YIELD)^2 = 137.036 = 1/ALPHA`. |
| Eq.(7) **(REV-2)** | `delta_n_QED = (alpha/15pi)(E/E_crit)^2` (propagating) | `ave.bench.delta_n_qed_electric_pvlas(E, geometry="propagating")` (birefringence.py). ANCHORED to (a) PVLAS `A_e=1.32e-24` via `E↔cB` duality (`= alpha/30pi` static, ×2 propagating), (b) LoI Eq.19. Was `(3/45)α²`, understated by `1/(2πα)`. |
| Eq.(8) | `P_flip = sin^2(dphi/2)`, `dphi=(2pi/lambda)|dn|z` | `flip_prob_exact` + `retardance_phase` (gap1 driver :140,:119). |
| Eq.(9), abstract, §III.B **(REV-2)** | Ratio `7.5pi/alpha^2 ~ 4.42e5` (propagating; `15pi/α²~8.85e5` static) | `ave.bench.coefficient_ratio_differential_pvlas(geometry="propagating")`; live `4.4247e5`. Was `7.5/α³~1.93e7`. |
| Table I, row 1 (9835 eV, demonstrated) **(REV-2)** | `E=8.68e13`, `A^2=5.90e-7`, `P_ave=5.39e-3`, `P_qed=2.76e-14`, ratio `1.95e11` | scenario driver JSON `scenarios[0]`: `P_ave_exact=5.3883e-3`, `P_qed_exact=2.757e-14`, `ave_over_qed=1.954e11`. |
| Table I, row 2 (8766 eV) **(REV-2)** | `P_ave=4.28e-3`, `P_qed=2.19e-14` | `scenarios[1]`: `4.2822e-3`, `2.190e-14`. |
| Table I, row 3 (12914 eV) **(REV-2)** | `P_ave=9.28e-3`, `P_qed=4.75e-14` | `scenarios[2]`: `9.2781e-3`, `4.754e-14`. |
| Table I, row 4 (1e22 design) **(REV-2)** | `P_ave=4.49e-1`, `P_qed=2.76e-12`, `dphi=1.47 rad` (saturating) | `scenarios[3]`: `P_ave_exact=4.4940e-1`, `P_qed_exact=2.757e-12`, `dphi_ave_rad=1.4694`. |
| Table I, row 5 (1e23 design) **(REV-2)** | `P_ave=7.65e-1`, `P_qed=2.76e-10`, `dphi=14.7 rad` (beyond validity, EXCLUDED, daggered) | `scenarios[4]`: `7.6470e-1`, `2.757e-10`, `dphi_ave_rad=14.6951`. GAP-1 bins FORM-BREAKS-UNRESOLVABLE. |
| §V "seven orders above floor"; abstract | `~2e7` margin vs demonstrated `2.4e-10` | GAP-1 driver `margin_vs_demonstrated_2.4e-10 = 2.266e7` (9835 eV). Floor value = Marx-Schulze `P_DEMONSTRATED_6457 = 2.4e-10` (gap1 :83). |
| Fig.1 / §V "8e-11 floor" | Record polarimeter purity `8e-11` | LoI Sec 4.1 record; scan driver `BEST_XRAY_POLARIMETER_PURITY = 8e-11`. |
| §VI, Eq.(6); abstract; §IV | `delta_n_mu = 0` static-B | `clm-pvlas1`; leaf :13-22 (route scope, side-prediction); GAP-1 `e_vs_b_asymmetry()`. |
| §V "forward prediction / CLEAN-FIELD" | No prior experiment bounds the E-route flip-prob | scan driver `scan_bin = CLEAN-FIELD`; pre-reg §0 gate; `2026-07-03_birefringence-prior-art-exposure-scan_result.md`. |

**Two-floor note (REV-2, citation corrected):** two X-ray polarimeter purity
numbers. The **record `8e-11`** is now correctly cited to **Karbstein2021**
(NJP 23, 095001; the diamond-channel-cut XFEL polarimetry result — the driver's
inline `E_PROBE_NJP_EV` provenance at `birefringence_gap1_hibef_feasibility.py:77,82`
sources it to NJP 2021, NOT Marx2013). The **conservative single-measurement floor
`2.4e-10`** is **Marx2013** (PRL 110, 254801 @6.457 keV; driver `P_DEMONSTRATED_6457`
:83). The paper's kill criterion uses `2.4e-10` (Marx2013); Fig.1 plots `8e-11`
(Karbstein2021), with the caption noting the `2.4e-10` kill floor lies just above.
This corrects the REV-1 mis-citation (8e-11 was wrongly attributed to Marx2013).

## 2. Rounding reconciliation (task brief vs drivers)

The task brief quoted `5.4/4.3/9.3 e-3` and `E_c ~ 1.13e17`; the paper uses the
driver-exact `5.39/4.28/9.28 e-3` (2 sig figs of `P_ave_exact`) and `1.13e17`.
The brief's "5.4/4.3/9.3" are the same numbers rounded to 2 sig figs a different
way; the paper follows the scenario-driver JSON exactly (which matches the frozen
pre-reg §3 table: `5.39/4.28/9.28`). No discrepancy — brief was rounded.

## 3. Reference verification (each checked at draft time; 10 refs after REV-2)

All refs verified via Crossref DOI lookup / arXiv abstract this session:

- **BirefHibefLoI2025** — HPLSE 13, e7 (2025), DOI 10.1017/hpl.2024.70; arXiv:2405.18063. Title + collaboration author list confirmed via arXiv + Crossref.
- **HeisenbergEuler1936** — Z. Phys. 98, 714 (1936), DOI 10.1007/BF01343663. Confirmed.
- **Schwinger1951** — Phys. Rev. 82, 664 (1951), DOI 10.1103/PhysRev.82.664. Confirmed.
- **BornInfeld1934** — Proc. R. Soc. Lond. A 144, 425 (1934), DOI 10.1098/rspa.1934.0059. Confirmed.
- **Karbstein2015** — Phys. Rev. D 92, 071301 (2015), DOI 10.1103/PhysRevD.92.071301; arXiv:1507.01084. Head-on x-ray/optical collision geometry. Confirmed.
- **Ejlli2020** — Phys. Rep. 871, 1-74 (2020), DOI 10.1016/j.physrep.2020.06.001; arXiv:2005.12913. PVLAS final results. Full author list confirmed via Crossref.
- **Marx2013** — Phys. Rev. Lett. 110, 254801 (2013), DOI 10.1103/PhysRevLett.110.254801. Full 13-author list confirmed via Crossref. The pump-OFF X-ray polarimetry demonstration; cited for the `2.4e-10` conservative kill floor ONLY (REV-2 correction: it is NOT the source of the 8e-11 record).
- **Karbstein2021 (REV-2 ADD)** — New J. Phys. 23, 095001 (2021), DOI 10.1088/1367-2630/ac1df4. "Vacuum birefringence at x-ray free-electron lasers." Confirmed via Crossref. TWO roles: the `8e-11` record polarimeter floor source AND the XFEL-birefringence-theory positioning cite.
- **BattestiRizzo2013 (REV-2 ADD)** — Rep. Prog. Phys. 76, 016401 (2013), DOI 10.1088/0034-4885/76/1/016401. "Magnetic and electric properties of a quantum vacuum." Confirmed. Magnetic-null-review positioning.
- **Fouche2016 (REV-2 ADD)** — Phys. Rev. D 93, 093020 (2016), DOI 10.1103/PhysRevD.93.093020. "Limits on nonlinear electrodynamics." Confirmed. NLED-bounds + ALP-distinction cite.

## 4. Discipline tags

- **consistency-vs-emergence:** CONSISTENCY-class throughout. The paper does NOT
  headline the `4.42e5` magnitude (REV-2; was `1.93e7`) as emergence; it ledgers
  `E_c` as calibrated from `alpha, m_e` (§II.B honesty ledger). Matches the
  pre-reg CONSISTENCY tag.
- **chord-vs-echo:** the paper's "discriminating claim" is the FORM (existence of
  a tree-level O(1) differential); the magnitude is explicitly ledgered as
  alpha-rooted for both frameworks (symmetric standard). Matches leaf :43.
- **phase-space-coordinate-check (A46):** PASS. The flip-prob observable is a
  polarization-phase (Poincare/Jones) quantity; both AVE and QED ride the
  identical `dn -> dphi -> flip` chain. No real-space-vs-phase-space mismatch.
- **no-strawman:** QED co-computed through the identical readout chain; only
  `delta_n` differs (driver `hibef_point`).
- **honest exclusion (Rule 11):** the 1e23 design row is a named validity limit
  (`beyond validity`), explicitly NOT part of the registered falsifier (§V).

## 5. FLAGGED FOR GRANT (judgment calls the auditor/Grant owns)

1. **MODEL NAME.** The paper introduces the working name **"saturable vacuum
   electrodynamics (SVE)"** (§I) as a neutral, descriptive label for the
   constitutive model, per the brief's instruction to pick a neutral descriptor
   and flag rather than bikeshed. It appears once by name (§I) and thereafter as
   "the model" / "this model." **Decision needed:** keep "saturable vacuum
   electrodynamics," or substitute ("saturating-vacuum electrodynamics",
   "quarter-arc dielectric vacuum", etc.). Single-point edit (§I) if changed.

2. **AUTHOR / AFFILIATION.** Author block is `G. Lindblom`, email
   `grant6t@gmail.com`, affiliation **"Independent researcher"** (placeholder; no
   affiliation invented, per brief). **Decision needed:** confirm author string,
   email, and whether "Independent researcher" is the intended affiliation line.

3. **VENUE / DOCUMENT CLASS.** Built as REVTeX 4-2 `prd` two-column (5 pages).
   PRD-class is a placeholder choice suited to the NLED/strong-field content.
   **Decision needed:** target venue (PRD Letter, PRL, HPLSE, arXiv-only
   preprint). PRL would need trimming to 4 pages + the abstract-length limit;
   the current draft is comfortably PRD-Letter-length. Trivial class swap.

4. **Two-floor presentation (§1 note above).** The paper cites both `8e-11`
   (record, Fig.1) and `2.4e-10` (Marx demonstrated, kill-criterion floor). This
   is deliberate and both are honest, but if a single floor is preferred for
   simplicity, standardize on `2.4e-10` (the conservative published single-shot
   floor) everywhere. Currently: kill-criterion uses `2.4e-10`, figure line uses
   `8e-11`. Flagged so it is a decision, not a silent inconsistency.

## 6. Build + verify status

- `pdflatex + bibtex + pdflatex x2`: clean, 5 pages, zero undefined refs, zero
  citation warnings, no large overfull boxes.
- `make verify`: GREEN (xi-namespace advisory pre-existing + non-gating).
- src/ change is additive only (`--figure` opt-in export on the scan driver);
  default driver runs and JSON outputs unchanged; ruff-clean.

## 7. Artifact rename + repo build target (2026-07-04)

- The committed PDF is renamed `main.pdf` → `sve_vacuum_birefringence_letter.pdf`
  (Grant directive: the artifact should not be named "main"). PDF metadata
  (`pdftitle`, `pdfauthor`) added via `\hypersetup` — no visual change; hyperref
  was already loaded with the same options.
- New repo target `make paper` (latexmk, `-jobname=sve_vacuum_birefringence_letter`)
  rebuilds it on demand. Deliberately NOT part of `make all`/`make pdf`: this PDF
  is the artifact of record for a pre-registered document (numbers Bitcoin-anchored
  under SHA f34e7559) and is rebuilt only on an explicit `make paper`.
- `make verify` now carries a warn-only staleness check: if `main.tex`/`refs.bib`/
  `figures/` have commits newer than the committed PDF, it prints a rebuild
  reminder (non-gating).
- Rebuilt at this rename: 7 pages, source unchanged from the merged PR #504 state (the
  Appendix-A micro-steps) plus this hypersetup line; content identical, metadata added.

## 8. Letter-v2 (Phase-0 co-author review round, 2026-07-05)

Keith's independent reproduction + Phase-0 review. Five exposition/citation items landed; the fork
memo (`research/2026-07-05_electrostatic-sector-fork-memo_FROZEN.md`; DRAFT at the time of §8, FROZEN
in the Arm-2 round per §9) is a SEPARATE freeze-class doc (Grant-ratify, held before Problem 3). **No
anchored v1 number moved this round.**

**ANCHORED v1 (SHA f34e755998a9, OTS proof on v1 — `claim-prereg-ots/claims_by_hash.md`), preserved
verbatim:** `P_flip = 5.39e-3 / 4.28e-3 / 9.28e-3` (9835/8766/12914 eV, demonstrated pump
1e21 W/cm^2); coefficient ratio `7.5 pi/alpha^2 ~ 4.42e5` (propagating), field-independent; QED
co-prediction `~2.76/2.19/4.75e-14`. These are UNCHANGED by the Phase-0 round.

**Item 1 — FIELD CONVENTION (derived; Table I did NOT move).** The Table I fields ARE the peak carrier
amplitude `E = sqrt(2 I/(c eps0))` (= `8.68e13 V/m` at 1e21 W/cm^2; verified vs
`field_from_intensity_wcm2`). Derivation: the probe crosses ~13 pump carrier cycles, so the accumulated
retardance is carrier-averaged for BOTH legs; the QED `alpha/15pi` coefficient already carries this
average (it is defined on the LoI intensity, reproduces LoI Eq.16 EXACTLY and Eq.19 to 1.1%), so on a
consistent peak-field footing the anchored v1 numbers stand. The Letter now STATES the peak-field
convention explicitly (§III.A + honesty-item (iv)). Full derivation:
`research/2026-07-05_field-convention-carrier-average_note.md`.
  - **[GRANT-ADJUDICATE] flagged exposure (flag-don't-fix):** carrying item 1 to its end surfaces a
    MIXED FOOTING in the anchored ratio — the SVE leg `-1/2(E/E_c)^2` is peak-INSTANTANEOUS while the
    QED `alpha/15pi` is cycle-AVERAGED; a consistent single footing gives `3.75 pi/alpha^2 ~ 2.21e5`,
    HALF the anchored `7.5 pi/alpha^2`. Surfaced with full derivation for Grant; NOT edited. Folded
    into honesty-item (iv) as an α-rooted-convention O(1) shift (order of magnitude + every falsifier
    verdict unchanged). Three adjudication arms in the note §3.

**Item 2 — QED LEG AT THE TRUE CROSSING GEOMETRY (verified; numbers did NOT move).** The driver's
`alpha/15pi` propagating leg IS the head-on (`theta_coll = pi`), 45°-polarization crossing-geometry
value of Karbstein-Gies-Reuter-Zepf 2015 / LoI Eq.16-19 (reproduces Eq.19 to 1.1%). The O(1) geometry
factor is already baked in; the 21.8x = 1/(2 pi alpha) correction (`7.5 pi/alpha^2`) is CONFIRMED, not
regressed. Letter §III.A now states the head-on/45° crossing-geometry provenance + `(1-cos theta)^4`
scaling, citing `Karbstein2015`. Note: `research/2026-07-05_qed-leg-crossing-angle_note.md`.

**Item 3 — DELLIGHT (citation added).** Replaced "below existing interferometric bounds"-class
language with the actual DeLLight number: Sagnac-interferometer common-mode vacuum-index measurement,
QED-level projected sensitivity (refraction angle ~0.13 prad, 5σ in ~1 month, extinction factor
F=0.4e-5). Ref `Robertson2021DeLLight` = Phys. Rev. A 103, 023524 (2021), DOI
10.1103/PhysRevA.103.023524, arXiv:2011.13889 (author list + DOI Crossref/arXiv-verified this session).
Cited in §II.D (common-mode channel) + §V (consistency with bounds).

**Item 4 — ARCHIVAL WORDING (made exact).** §V "Pre-registration" para: "public archival record" ->
explicit OpenTimestamps (SHA-256 of the frozen prediction committed to the Bitcoin blockchain; hash
public, content private until disclosure). No overclaim.

**Item 5 — BORN-INFELD FAMILY (paragraph added).** §II.B now situates SVE's elliptic kernel within the
90-year saturating-field-electrodynamics family: Born-Infeld 1934 engineered the `sqrt(1+F/b^2)` form
to keep electrostatics/self-energy finite; SVE's `sqrt(1-(E/E_c)^2)` is a DISTINCT BRANCH (reversed
sign, softening not stiffening, E-B asymmetric). FAMILY CONTEXT ONLY — no branch-survival or
self-energy claim (that is the electrostatic-sector gauntlet, not yet run). Ref `BornInfeld1934`
(already present).

**Build/verify:** `make paper` clean (7 pages, zero undefined refs/citation warnings, 13 refs resolve
incl. new DeLLight). `make verify` GREEN (staleness warn satisfied by the rebuilt+committed PDF). src/
UNCHANGED this round: a strawman one-leg cycle-average driver edit (a `field_convention` parameter that
halved ONLY the SVE leg's field) was written and caught at compute time — it broke the field-independent
delta_n coefficient ratio, which `coefficient_ratio_differential_pvlas` returns as a field-independent
constant by construction, so a one-leg edit that halves it is provably wrong. Both driver files were
`git checkout`-reverted and the JSON regenerated to byte-identical anchored v1. The full story +
the invariant gate that caught it live in the field-convention note **§4a** (`research/2026-07-05_field-convention-carrier-average_note.md`).
Fresh branch `analysis/letter-v2-phase0` off merged HEAD 3188b052. Grant's five standing decisions
(headline form, SVE name, author, venue, floors) UNTOUCHED.

## 9. Letter-v2 ARM-2 re-freeze — consistent-footing ratio (2026-07-05, Grant-ratified)

**Grant ruling (2026-07-05, verbatim):** *"ARM 2 ratified — the Letter's headline ratio re-freezes on
the consistent footing, WITH the Arm-3 one-sentence decomposition retained where it reads naturally."*

The Phase-0 round (§8) flagged a MIXED FOOTING in the anchored ratio for `[GRANT-ADJUDICATE]`. Grant
picked **Arm 2**: state the discriminating ratio on a SINGLE consistent footing. This is a documented
**v2** of an OTS-anchored document; the v1 value is preserved verbatim below.

**ANCHORED v1 (SHA f34e755998a9, OTS proof — the Bitcoin timestamp covers the v1 CONTENT; this v2 does
NOT re-stamp), preserved verbatim:** discriminating ratio `7.5 pi/alpha^2 ~ 4.42e5` (MIXED footing:
instantaneous SVE kernel `1/2` over cycle-averaged QED `alpha/15pi`); `P_flip = 5.39/4.28/9.28e-3`;
QED co-prediction `~2.76/2.19/4.75e-14`; Table I model/QED `~1.95e11`. **The OTS anchor is on v1.** This
v2 supersedes the QUOTED ratio only; v1's anchored record stands unaltered.

**v2 (Arm-2, this round):**
- **The single footing, stated explicitly:** both printed coefficients are the INSTANTANEOUS
  (peak-field) response. The SVE kernel `-1/2(E/E_c)^2` is instantaneous (Appendix A, algebraic in
  `|E|^2` at the pump); it is paired with the INSTANTANEOUS one-loop coefficient `2 alpha/15pi` (the
  headline `alpha/15pi` of Eq.7 is its `<cos^2>=1/2` cycle average). This is the both-peak-instantaneous
  footing — the ONLY one that holds the SVE model P_flip headline FIXED while making the ratio
  consistent.
- **Discriminating ratio: `3.75 pi/alpha^2 ~ 2.2e5`** (= `15pi/(4 alpha^2)`; exactly HALF v1's
  `7.5 pi/alpha^2`, the difference being the `<cos^2>=1/2` carrier average). Sites swept (two-method):
  abstract, §II.B honesty-item (iv), Eq.9 + surrounding text, §III conclusion, Table I caption. The two
  intentional v1-history mentions (item (iv) "mixed footing doubles to 7.5pi", Eq.9 "a prior draft
  quoted 7.5pi") are RETAINED as the convention history.
- **The x4-geometry x 1/2-carrier decomposition RETAINED** (Grant: "Arm-3 one-sentence decomposition
  retained where it reads naturally"): §III.A carries it (`alpha/30pi -> 2alpha/15pi` head-on geometry
  x4, `-> alpha/15pi` carrier x1/2); item (iv) cross-references it.
- **Table I (v2):** the model P_flip column is UNCHANGED (5.39/4.28/9.28e-3; the SVE headline is the
  footing-invariant quantity). The QED column moves to its INSTANTANEOUS normalization
  `2 alpha/15pi` (`1.10e-13 / 8.76e-14 / 1.90e-13` demonstrated; `1.10e-11` / `1.10e-09` design), and
  the model/QED column to `~4.89e10` = `(3.75pi/alpha^2)^2` — internally consistent with Eq.9. This
  move is FORCED by consistency: keeping the QED column at v1 while re-freezing the ratio would make
  Table I self-contradict Eq.9.
- **FOOTING-INVARIANT quantities verified UNCHANGED:** SVE model P_flip (5.39/4.28/9.28e-3); kill
  criterion (`P_flip < 1e-8`); floor margin (~2.25e7 vs the 2.4e-10 floor); OOM separation (~11,
  log10(4.89e10)=10.7). The kill-criterion NARRATION "~e6 above the QED level" -> "~e5" (the QED
  baseline moved to its instantaneous value; the kill LINE `1e-8` is unchanged).

**Fork memo FROZEN (Grant-ratified 2026-07-05):**
`research/2026-07-05_electrostatic-sector-fork-memo_DRAFT.md` -> `..._FROZEN.md` (git mv; corpus
prereg-freeze convention). Grant ratification recorded verbatim + dated at the memo top; the three
outcome bins + Keith-arm rejection are IMMUTABLE (errata-banner-only). This freeze GATES Problem 3;
the freeze commit lands BEFORE the Arm-2 edits in this PR (commit-time ordering is the proof).

**Build/verify (Arm-2):** `make paper` clean (8 pages — the DeLLight reference now wraps ~3 lines onto
p8; the Arm-2 footing exposition + Table-caption + item-(iv) growth is load-bearing and Grant-ratified,
so 8pp is accepted over cutting ratified physics; no large overfull boxes introduced — only the
pre-existing appendix one at main.tex:~711 remains). `make verify` GREEN. src/ + JSON UNCHANGED
(byte-identical to v1). Fresh branch `analysis/letter-v2-arm2` off merged HEAD a6c8f844 (contains #537).
Grant's five standing decisions UNTOUCHED.
