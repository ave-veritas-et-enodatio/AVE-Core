# INTERNAL provenance — saturable-vacuum birefringence Letter

**NOT part of the paper.** This is the audit trail the public Letter deliberately
does not carry (pure-physics rule: the paper cites no private repo, no framework
volumes, no program history). Every quantitative claim in `main.tex` maps here to
its corpus source: canonical claim-id, driver, output JSON, and the merged PR.

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
