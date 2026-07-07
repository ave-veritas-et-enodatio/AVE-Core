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

## 10. Electrostatic-sector scope + exclusion ledger entry (2026-07-05, Grant go)

**Grant go (2026-07-05):** the flagship must carry its own sector's adjudication — the Letter states
the electrostatic-sector exclusion in its OWN standalone terms (corpus-independent), with the muonic
result phrased self-contained and the CREMA measurement cited properly. **No anchored v1 number moved
this round;** this round adds a sector boundary the model *acquired in public*, ledger open.

**The merged canon this round surfaces into the flagship (each verified verbatim this session):**
- **Static-E [C-EXCLUDED]** (Problem 3, merged #539/#540, claim `clm-sve3xc`;
  `research/2026-07-05_problem3-muonic-lamb_RESULT.md`): the CONTINUUM static-E constitutive law
  `eps_eff = eps0 sqrt(1-(E/E_c)^2)` is EXCLUDED at atomic scales by muonic hydrogen,
  **non-perturbatively**. Both arms violate the CREMA 2.3 µeV window by 4–7 OOM: continuum
  `[1.5e6, 2.3e7]` µeV = 7.5×–114× the full 202.37 meV Lamb interval; lattice-scoped (`r >> ell_node`)
  still `[4.9e4, 6.2e5]` µeV (smallest variant ~2e4× the window). U91+ continuum arm is genuinely
  INCOMPUTABLE (`A^2 = 12.6 > 1`, no real solution). The protective cutoff would need `~9·ell_node ≈
  3.5 pm` — an independent free parameter (the ~300 fm floor estimate is REFUTED, ~12× too small). The
  Letter states this in standalone terms: the constitutive law as written cannot extend to strong static
  atomic fields, the induced level shift exceeding the *entire* measured splitting.
- **Rescue round 1 [CONSTRAINT-KILLED]** (merged #542;
  `research/2026-07-05_em-saturation-keying-functional_RESULT.md`): the LOCAL-Poynting transport-keying
  scoping mechanism (`S_E = sqrt(1 - c_T · <E×H>/S_yield)`) FAILS on the PHYSICAL atom — the proton
  magnetic moment sources a permanent static, divergence-free `E×H` circulation (hidden-momentum class)
  that engages the local functional at **1278× the 2.3 µeV window** (−2939 µeV @ `r_cut=0.5 a_μ`). As
  recorded at #542 merge, the net-flux (closed-surface) round-2 candidate was named OPEN. **Subsequent
  (post-draft, Grant-walked, recorded in the round-2 arc's prereg addendum): the net-flux candidate is
  DEAD** — closed-surface net flux = `dU/dt = 0` for every steady state, including the pump (Poynting
  degeneracy), so it cannot distinguish the pump from the held atom. The scoping mechanism therefore
  remains OPEN and is stated **candidate-agnostically** in the Letter (see the fix note below); the
  Letter names no specific open candidate, so it needs no edit as the round-2 derivation iterates.

**The edit (surgical — 8pp referee-facing Letter, one logical fix per commit):**
- **Item 1 — SCOPE paragraph (§II.B, `main.tex`):** a "Sector scope, stated explicitly" paragraph after
  the Family-context lineage. The constitutive law is asserted for the RADIATIVE pump-probe sector only
  (`A^2~6e-7`, time-varying); the static-field sector was tested against muonic-H under a pre-registered
  outcome fork BEFORE any external submission; the continuum static extension is EXCLUDED
  non-perturbatively (the induced level shift exceeds the entire measured 202.3706(23) meV interval,
  `\cite{Antognini2013}`; inside a high-Z ion the kernel has no real solution). The radiative scoping is
  a POSTULATE: one candidate mechanism (local `E×H` transport keying) tested and excluded (the physical
  atom's bound magnetic moment engages it); the scoping mechanism remains under derivation, stated
  **candidate-agnostically** (the Letter names no specific open candidate — see the fix note below). The
  B-sector circulation keying [Eq. (6)] is a separate sector, unaffected.
- **Item 2 — HONESTY LEDGER item (v) (§II.B, `main.tex`):** claimed (implicitly universal constitutive
  law) / ruled (static sector dead) / survives (the AC falsifier unchanged — `P_flip` and the kill
  criterion are radiative-sector quantities) / open (the scoping mechanism). Keith's Outcome-B posture
  executed: the model acquired its sector boundary in public, ledger open.
- **Item 3 — sentence sweep (two-method: grep `static|constitutive|universal|electrostatic|D(E)` + §II
  end-to-end read).** ONE static-E-sector consistency sentence scoped: §V "Consistency with existing
  bounds" — the preferred-frame-boost sentence scoped to WEAK macroscopic static fields only
  (`A^2~7e-23`), explicitly NOT a claim into the strong near-nucleus atomic static sector (separately
  excluded). Self-focusing (propagating Kerr) + GW-interferometer (circulating cavity fields) + DeLLight
  (optically-induced common-mode) rows verified RADIATIVE-sector (labelled propagating-field bounds); no
  scoping needed. All other `static` occurrences are the magnetic-sector static-B transparency (a
  separate sector, already correctly scoped).
- **Item 4 — KB seam (`manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`):**
  the leaf headlined `7.5pi/alpha^2 ~ 4.42e5` (v1 mixed footing); reconciled to the consistent-footing
  `3.75pi/alpha^2 ~ 2.2e5` (Letter v2 Arm-2, §9) via a KEEP-BOTH FOOTING RE-FREEZE note — the
  `7.5pi/alpha^2` preserved as v1 convention history, the `x4`-geometry `x1/2`-carrier decomposition
  shown, provenance §9/§10 cited. No OOM / falsifier verdict moves.
- **Item 5 — this §10 entry.**
- **Item 6 — II.B lineage-clause removal (`main.tex`, commit `abd1438f`):** the Family-context lineage
  paragraph previously deferred the static sector inline — "*the behaviour of the elliptic branch in the
  static electrostatic sector, and any comparison of self-energy properties across branches, is outside
  the scope of this Letter*" (stood at `origin/main` `main.tex:270`). That clause was narrowed to "*any
  comparison of self-energy properties across branches is outside the scope of this Letter*" (now
  `main.tex:290–292`): the static-electrostatic deferral is superseded by the [C-EXCLUDED] Sector-scope
  paragraph (Item 1) + honesty-ledger item (v) (Item 2), which state the exclusion non-perturbatively
  rather than deferring it. Content-correct but itemized nowhere at draft time — logged here.

**refs.bib:** `Antognini2013` added — Antognini et al., Science 339, 417–420 (2013), DOI
`10.1126/science.1230016` (the CREMA muonic-H 2S–2P measurement; extracted `2P_1/2−2S_1/2` Lamb interval
`202.3706(23) meV`). DOI + full author list + volume/page Crossref-verified this session. The Letter is
STANDALONE: it cites its own pre-registered mechanism ("a pre-registered atomic-sector test") and this
external CREMA measurement; no private-repo cite.

**Discipline tags.**
- **consistency-vs-emergence:** the exclusion is FALSIFICATION/CONSISTENCY-class (the SVE `E_c` is
  CODATA-derived through `alpha`, `m_e` per honesty-item (iii)); no emergence claimed. Matches
  `clm-sve3xc` solidity 0.80.
- **honest closure (Rule 11):** the static-E extension was routed against FROZEN bins with no post-hoc
  criterion drops; both arms violate; a single mechanism (`1/r^5` near-nucleus enhancement surviving the
  `ell_node` cutoff) explains both. The Letter records the falsification, scopes the branch, ledger open.
- **flag-don't-fix:** the leaf-vs-flagship footing staleness (KB `7.5pi/alpha^2` vs Letter
  `3.75pi/alpha^2`) surfaced + reconciled KEEP-BOTH (not silently overwritten). The leaf body
  (`7.5/alpha^3`) is left under the existing header-supersession chain; NOT rewritten this round.
- **phase-space-coordinate-check:** N/A / PASS — the muonic-H test measures a level-shift (energy), the
  matching coordinate for a constitutive-law level-shift prediction; no real-space-vs-phase-space
  mismatch.
- **verify-before-cite:** every exclusion magnitude (both arms' bands, the `~9·ell_node` protective
  cutoff, U91+ incomputability, the 1278× local-Poynting overshoot) live-read from the merged #539/#540/#542
  docs this session; the CREMA value + Antognini DOI Crossref-verified; the `3.75pi/alpha^2` arithmetic
  re-checked (`15pi/(4 alpha^2)`).

**Build/verify (scope round):** `make paper` clean (8 pages, zero undefined refs/citation warnings, 16
refs resolve incl. new `Antognini2013`; only the pre-existing appendix overfull box at `main.tex:~741`
remains — my paragraphs introduced no large overfull box). `make verify` GREEN. src/ + JSON UNCHANGED
(byte-identical to v1; no driver touched). Fresh branch `analysis/letter-electrostatic-exclusion` off
merged HEAD `fc6a2379` (contains #542). Grant's five standing decisions UNTOUCHED.

**FIX NOTE (2026-07-05, post-draft, one commit) — candidate-agnostic scoping-mechanism wording.** The
draft's scope paragraph (item 1) and honesty-ledger item (v) (item 2) both named "a net-flux
(closed-surface) formulation under derivation" as the open scoping candidate. That candidate is now
**DEAD** (Grant-walked; recorded in the round-2 arc's prereg addendum): closed-surface net flux =
`dU/dt = 0` for every steady state including the pump (Poynting degeneracy), so a net-flux key cannot
distinguish the pump from the held atom. The Letter must not name a killed candidate — and should not
name whichever candidate is currently live either, so it needs no edit each time the derivation iterates.
Both sentences re-worded to the **candidate-agnostic** form: *"…has itself been tested and excluded; the
scoping mechanism remains under derivation."* The honest state is **mechanism-open**. This changes no
number, no falsifier verdict, no anchored value; it is a physical-picture-accuracy wording fix only.
`make paper` clean (8pp, zero undefined refs/citation warnings, 16 refs); `make verify` GREEN.

**SCOPING-SENTENCE REFRESH (2026-07-06, post rounds 2/3 merged — one commit) — "remains under derivation"
retired; open question re-scoped to the lattice-scale regime boundary.** When the FIX NOTE above was
written, the honest state of the dynamical scoping was *mechanism-open* ("remains under derivation"). Two
dynamical scoping routes have since been tested and **excluded by derivation**, and the open question has
narrowed from "the mechanism" to a sector/scale **class** — so both "remains under derivation" clauses are
now stale and are retired.
- **What the two merged rounds derived (each read verbatim this session):**
  - **Round 2 (net-flux candidate KILLED at STEP 0; the round's own routed bin is [SELECTED-NOT-DERIVED], resolved by round 3)** (merged **PR #546**; `research/2026-07-05_em-keying-round2-worked-cell_RESULT.md`):
    the net-flux (closed-surface) candidate the FIX NOTE already flagged DEAD is confirmed dead by sympy at
    STEP 0 — `∮_∂V S·dA = ∫∇·(E×H) = −∫∂_t u`, and `⟨∂_t u⟩_cycle = 0` for every steady state including the
    pump (Poynting degeneracy), so a net-flux key cannot distinguish the pump from the held atom.
  - **Round 3 [DERIVED: CHARGE-KEYED]** (merged **PR #547**; `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md`,
    claim routing bin, prereg FROZEN `..._prereg_FROZEN.md`): the ε-response is derived to key on the
    **mean-square** of the instantaneous amplitude at leading (2nd) order — `⟨1−S_ε⟩ = ½⟨A_V²⟩`, DC baseline
    retained — so a held field is a **real operating-point bias and loads**. The excursion/variance member
    (H2) is **DERIVED-AGAINST**: M0/M1/M2/M3 + a lattice-level zero-mode/rigidity check all fail to deliver a
    lossless DC-block (K4 shear stiffness `k_s>0`, no floppy zero-mode across the full counted band).
  - **Robust-to-pitch-cutoff (the [B-AVE] band-split, `em_keying_round3_comparison.py::band_split_C_iii`, pinned
    by `test_C_iii_band_split_dominant_subpitch_band_STANDING_PIN`):** ~**103.2%** of the muonic overshoot
    magnitude comes from the sub-pitch band `[159.6, 386.2] fm` (below one node pitch), yet the **super-pitch
    remainder alone** nets `~4.9×10⁴ µeV ≈ 2×10⁴×` the 2.3 µeV CREMA window — so `[C-EXCLUDED]` **stands on the
    super-pitch band alone**; a lattice-pitch cutoff does not rescue the static sector. What is genuinely open
    is confined to the lattice-scale regime boundary (the **[B-AVE] arm**: whether the sub-pitch continuum
    integral is the right lattice-scale accounting).
- **The edit (surgical — two clauses, `main.tex`):**
  - **Honesty-ledger item (v) (§II.B "What is open"):** the "a first candidate scoping (local power-transport
    keying) has been tested and excluded, and the scoping mechanism remains under derivation" clause →
    candidate-agnostic + class-named: the dynamical scoping routes proposed have **each been tested and
    excluded by derivation**; the static-sector response is **derived charge-keyed** (a held field is a real
    operating-point bias, so it loads); what remains open is **confined to the lattice-scale regime boundary**,
    and the exclusion is **robust to it** (a lattice-pitch cutoff alone does not rescue the static sector).
  - **Sector-scope paragraph (§II.B):** the "One candidate scoping mechanism — a response keyed on the local
    power transport (E×H) … — has itself been tested and excluded, because a physical atom's bound magnetic
    moment sources a static, divergence-free E×H circulation …; the scoping mechanism remains under derivation"
    passage → the same candidate-agnostic + lattice-scale-class form. The named E×H (power-transport) candidate
    is REMOVED per the standing wording rule (must not name a killed candidate).
- **Standing wording rule honored (FIX NOTE above, verbatim):** the Letter names **no** killed candidate and
  **no** currently-live candidate; the **lattice-scale regime boundary is a sector/scale CLASS, not a
  candidate**, so naming the class is permitted and needs no edit as the [B-AVE] derivation iterates. §V and
  honesty-ledger item (v) checked for consistency with the new wording (two-method: grep
  `scoping|regime boundary|lattice-scale|charge-keyed|operating-point|under derivation` + §II/§V read); §V's
  magnetic-route/static-B and preferred-frame-boost sentences are a disjoint sector, **still true, left
  unchanged**. STANDALONE discipline preserved: no new `\cite` (the scope paragraph still cites only
  `Antognini2013` + internal `\eqref`/`\ref`); no private-repo cite.
- **Anchored invariants grep-confirmed UNCHANGED:** `P_flip` triplet `5.39/4.28/9.28e-3`; kill criterion
  `P_flip < 1e-8` at `≥1e18 W/cm²`; ratio `3.75π/α²`; pump `A²≃5.9e-7` (and `6e-7`/`5.90e-7`). No number, no
  falsifier verdict, no anchored value moves; src/ + JSON UNTOUCHED (no driver read or edited in the Letter dir).
- **Discipline:** *Rule 11 honest closure* — the two dynamical routes are recorded excluded-by-derivation with
  no post-hoc criterion drops; *substitution-not-retraction* — round-2's open member is RESOLVED by the round-3
  derivation (its own prereg + verification chain), not refilled; *flag-don't-fix* — the leaf `node-up:217`
  (*"loads ε and shifts n"*) is CONFIRMED by the charge-keyed derivation, surfaced to the auditor lane, not
  silently overwritten. `make paper` clean (8pp, zero undefined refs/citation warnings, 16 refs resolve;
  only the three pre-existing overfull boxes remain — the Table I alignment ~8.9pt plus two appendix
  displays ~21.9pt/~6.6pt — the scope-paragraph edits introduced none);
  `make verify` GREEN. Fresh branch `analysis/letter-scoping-sentence-refresh` off merged HEAD `b0615b5e`
  (contains #547). Grant's five standing decisions UNTOUCHED.

## 11. Two physics-wording corrections — last Letter edit before external contact (2026-07-06, Grant-fired Task #16)

**Grant go (2026-07-06):** two convention/physics-accuracy corrections to the referee-facing Letter, ONE PR
(`analysis/letter-bi-corrections`), two commits (one logical fix each). No anchored number moved; both are
physical-picture-accuracy fixes, and FIX 2 STRENGTHENS the E-route discriminator (it makes the pump-on
measurement a three-way separator). Branch off `origin/main` `cb38c9b9`.

**FIX 1 (commit `4ff9e20c`) — convention-independent response-exponent B-I contrast (§ "Family context", `main.tex`).**
- **What was wrong:** the sentence displaying `L ∝ √(1+F/b²)` read *"the sign under the root is reversed, so the
  response softens…"* (stood at `main.tex:294–295`). It is true against the covariant display but reads FALSE the
  moment a reader substitutes the pure-E form: `√(1+F/b²) = √(1−E²/b²)` for pure E (since `F ∝ −2E²`), so the
  *interior* sign is a display convention, not a physical difference. This exact trap already fired once when the
  sentence was lifted into a KB leaf.
- **What changed:** migrated to the **response-exponent** framing, mirroring the merged KB precedent
  `manuscript/ave-kb/common/historical-precedents.md:39` (verified verbatim this session). The two theories put the
  root on **opposite sides of the response**: **B-I stiffens** — `D = E/√(1−(E/b)²)`, root in the *denominator*
  (exponent `−½`), diverges as `E→b`; **this model softens** — `ε = ε₀√(1−(E/E_c)²)`, root in the *numerator*
  (exponent `+½`), `ε→0` at the ceiling `E_c`. The covariant display `√(1+F/b²)` is KEPT and explicitly reconciled
  to the electric form in-text (`√(1+F/b²)=√(1−E²/b²)`), so the contrast lives at response level where it is
  convention-independent. Letter register (tight, no KB jargon).

**FIX 2 (commit — see PR) — the Born–Infeld static-B birefringence error (four sites + two new refs), `main.tex` + `refs.bib`.**
- **What was wrong:** the Letter claimed static-B transparency separates the model *"from QED and from
  Born–Infeld-type electrodynamics, both of which predict a nonzero static-B birefringence"* (`main.tex:351–352`),
  justified at `:587–589` by *"Born–Infeld-type… likewise predicts symmetric electric and magnetic responses"* (a
  non-sequitur), with the same wrong echo in the intro at `:96–98` and `:108–110`. **Exact Born–Infeld is the
  celebrated ZERO-birefringence exception:** the unique nonlinear electrodynamics (besides Maxwell) in which both
  photon polarizations share one effective light cone in ANY constant background, so exact B-I predicts **zero**
  static-B birefringence too.
- **The corrected physics (this STRENGTHENS the Letter, written soberly):** (a) static-B transparency separates the
  model **and exact B-I** from QED — the existing PVLAS/BMV nulls remain consistent for both; (b) the **E-route is the
  three-way discriminator** — this model predicts a large tree-level signal (`3.75π/α²` above QED), QED predicts its
  small one-loop signal, and exact B-I predicts exactly zero, so the pump-on measurement separates all three in one
  shot; (c) generic Born–Infeld-**TYPE** family members generically DO birefringe (the zero-birefringence property is
  the **exact 1934 theory's uniqueness**), so family statements and exact-theory statements are kept distinct.
- **Four sites swept (full `grep Born|Infeld|birefring` across `main.tex`, before + after):**
  1. `main.tex:~96–98` (intro, count-2 signature) — reworked: exact B-I shares the transparency; the tree-level
     E-route coefficient is what separates the model from exact B-I.
  2. `main.tex:~108–110` (intro, "distinct on two counts") — reworked: tree-level `O(1)` coefficient (vs QED's loop
     **and** vs exact B-I's zero); transparency is vs QED (exact B-I transparent too).
  3. `main.tex:~351–352` ("most sharply separates") — reworked: separates from QED; exact B-I shares the transparency
     (uniqueness cite); the E-route coefficient separates the model from exact B-I.
  4. `main.tex:~587–589` (signature §, the non-sequitur) — reworked: QED birefringes; exact B-I is the
     zero-birefringence theory (same PVLAS/BMV nulls); generic B-I-**type** members birefringe; the pump-on E-route
     separates all three (model / QED / exact B-I) at once.
  - Abstract (`:42–59`) + Conclusion (`:730–746`) checked: they state the *model's* zero static-B prediction and
    PVLAS/BMV consistency and name no B-I static-B claim — no wrong-claim echo, left untouched.
- **New refs (verified before adding — `refs.bib`):**
  - `Boillat1970` — **Crossref-verified in full** (DOI `10.1063/1.1665231`): G. Boillat, *Nonlinear Electrodynamics:
    Lagrangians and Equations of Motion*, J. Math. Phys. **11**(3), 941–951 (1970). This is the celebrated
    single-light-cone / zero-birefringence uniqueness result — the load-bearing citation.
  - `Plebanski1970` — **INSPIRE-HEP-confirmed** (recid 1103928): J. Plebański, *Lectures on Non-Linear
    Electrodynamics*, 1970. Author + exact title + 1970 date confirmed; **no DOI** and the *"NORDITA, Copenhagen"*
    imprint is the conventional literature attribution (INSPIRE carries `imprints: None`), rendered as a lecture-notes
    `@misc` with a `note:` and NOT asserting a database-confirmed publisher/page. **FLAG for Grant:** if a referee
    wants a fully database-grounded imprint, either keep Boillat as sole primary (it alone establishes the
    uniqueness) or supply the confirmed NORDITA report identifier — see the verify tier note below.

**Anchored invariants grep-confirmed UNCHANGED (before + after both fixes):** `P_flip` triplet `5.39/4.28/9.28e-3`
(3 hits); kill criterion `P_flip < 1e-8` at `≥1e18 W/cm²` (1 + 4 hits); ratio `3.75π/α²` (7 hits); pump
`A²≃5.9e-7`/`6e-7`/`5.90e-7` (4 hits); purity floor `2.4e-10` (5 hits); `δn_μ=0` static-B equation untouched. No
number, no falsifier verdict, no anchored value moves; `src/` + JSON UNTOUCHED (no driver read or edited).

**Discipline tags.**
- **verify-before-cite:** the KB response-exponent precedent (`historical-precedents.md:39`) read verbatim this
  session; both new bib entries verified against an authoritative database BEFORE adding (Boillat = Crossref full;
  Plebański = INSPIRE author/title/year; the un-confirmable NORDITA imprint flagged, not asserted as verified).
- **flag-don't-fix:** the Plebański imprint is NOT database-confirmable at the publisher-field level — surfaced as a
  FLAG for Grant rather than silently rendered as verified.
- **standalone citation discipline:** the two new refs are external empirical/theory sources (Boillat, Plebański) —
  permitted in these passages; no private-repo cite, no killed/live scoping candidate named.
- **consistency-vs-emergence:** N/A — a wording/physics-accuracy correction to a comparison with prior art; no AVE
  claim class changes.

**Build/verify:** `make paper` clean — **9 pages** (was 8; the two added references push the bibliography onto a 9th
page — body content did not balloon a page, the spill is the reference list renumbering with `[5]`/`[6]`), zero
undefined refs / zero citation warnings, both new refs resolve in the `.bbl` (Boillat with DOI, Plebański 1970).
Only the three pre-existing overfull boxes remain (Table I alignment ~8.9pt + two appendix displays ~21.9pt/~6.6pt,
line numbers reflowed by the page break); the corrections introduced none. `make verify` GREEN. Fresh branch
`analysis/letter-bi-corrections` off `origin/main` `cb38c9b9`. Grant's five standing decisions UNTOUCHED.
