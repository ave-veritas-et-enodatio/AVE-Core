# C1 — Cosmic-Rotation Knee: Alignment-Strength ∝ Moment-of-Inertia, Reynolds-Style Threshold — Pre-Registration

**Date:** 2026-06-05
**Branch:** `analysis/c1-cosmic-rotation-knee` off `origin/main` at `33b23192`
**Chord-hunt:** C1 (the genuine new-physics discriminating test from the 2026-06-05 gravity-sector arc)
**Brief:** `_orchestration/2026-06-05_follow-up-session-briefs.md` §C1 (on PR #94)
**Physical thread:** `project_cosmic_rotation_soliton_coupling_thread` memory (2026-06-05, exploratory, uncommitted)

---

## 0. One-paragraph pre-registration (per `ave-prereg`)

**What I expect.** The soliton-lattice-coupling-operator's missing functional form is **coupling ∝ moment-of-inertia / knot-content $I_s$**, and the alignment between a bound soliton's spin axis and the cosmic $\hat{\Omega}_{\text{freeze}}$ axis is governed by a **Reynolds-style dimensionless coupling-number** with a critical threshold (a "knee"). Below the knee, alignment washes out (soliton reflects cosmic torque, frozen/lossless, mismatched impedance); above it, alignment locks in (soliton absorbs cosmic torque, lossy/matched, coherent). I expect the dimensionless number to be the canonical **regenerative coupling-number $Q\cdot\delta$** (parametric-coupling-kernel §6, onset at $Q\cdot\delta \geq 2$) with $\delta \propto I_s \propto$ crossing-number $c$, and equivalently the **Op17 power-transmission coefficient $T^2 = 1-\Gamma^2$** (matched → absorbs → aligns).

**Why.** Three canonical anchors assemble it: (1) **$\mathcal{J} = \hat{\Omega}\cdot I$** at every $\Gamma=-1$ surface (`12_cosmological_characteristics.tex:68` verbatim; `boundary-observables-m-q-j.md:21`) makes angular-momentum coupling to the cosmic spin proportional to a soliton's moment of inertia $I_s$. (2) **$K_{\text{MUTUAL}} \propto$ crossing number $c$** (`12_the_millennium_prizes.tex:421` verbatim) makes the inductive coupling proportional to knot-content; mass↔inductance ($L = \xi^{-2}m$, `translation-circuit.md:24`) and $\mathcal{M}$↔inertia (`boundary-observables-m-q-j.md:19`) tie $I_s$ to the inductive/knot sector. (3) **$Q = \alpha^{-1}$** sets the electron's per-cycle loss fraction (grip = loss = $1/Q$); the regenerative onset $Q\cdot\delta\geq2$ (`parametric-coupling-kernel.md:22,209`) is the canonical Reynolds-analog knee, and scalar-gravity is already shown "15 OOM short of $Q\cdot\delta\geq2$" (`parametric-coupling-kernel.md:284`) — the weak-coupling/reflection regime.

**What would discriminate.** A galaxy-spin-axis alignment-strength that **rises with galaxy mass / moment-of-inertia** and shows a **threshold (knee)** would be AVE-distinct ONLY if isotropic-ΛCDM+systematics, Bianchi-anisotropy, and MOND do not predict the same mass-scaling. The load-bearing gate is Phase 4 `ave-discrimination-check`: a monotone alignment∝mass correlation that ΛCDM+selection-effects also predict is an **echo, not a chord**. The chord requires the *specific functional form* (knee location set by $Q\cdot\delta\sim2$ with $\delta\propto I_s$) to be confirmed AND to be a form the alternatives do not produce.

---

## 1. Corpus state (Phase 0 inventory)

### 1.1 What exists

| Corpus item | Status | Relevance to C1 |
|---|---|---|
| `_orchestration/theoretical/soliton-lattice-coupling-operator.md` | Epic; Session 1 (scoping) CLOSED, Session 2 (planetary scoring) DONE; Sessions 3-5 QUEUED/conditional | Operator $\hat{\mathcal{O}}_{\text{soliton}}$ defined as a SKETCH; integrated functional form **explicitly undetermined** (line 27: "until the operator is derived ... the prediction is the operator's coherent output ... with the operator's output undetermined") |
| `research/2026-05-20_soliton-coupling-operator-session2-planetary-scoring.md` | Result; 14-15/16 planetary class matches | Defines $A_{\text{spin}}^{(p)} = L_p\kappa_{\text{cosmic}}g_{\text{class}}/A_{\text{spin,sat}}$ — but for alignment **ANGLE** (obliquity branch selection), NOT alignment **STRENGTH-vs-$I_s$ with a knee** |
| `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md` | Canonical leaf | $\Omega_{\text{freeze}} = \mathcal{J}_{\text{cosmic}}/I_{\text{cosmic}}$ (line 32); §4 nested-cascade is **PROVISIONAL, not derived** (line 156); Observable 3 (LSS spin) "Same axis" |
| `manuscript/ave-kb/common/boundary-observables-m-q-j.md` | Canonical leaf | $\mathcal{J} = \text{Wind}(\partial\Omega)$, ME projection = rotation; $\mathcal{M}$ = strain integral ↔ inductance $L$ ↔ inertia (kg); J=Ω·I structure |
| `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md` | Canonical leaf | $\kappa_{\text{quality}}=1$ for $Q\cdot\delta_C\geq2$; $=(Q\delta_C/2)^2$ sub-regenerative (lines 22, 209, 225); scalar-gravity 15 OOM short of threshold (line 284) — **the canonical Reynolds-analog knee** |
| `manuscript/ave-kb/common/operators.md:57` | Canonical | Op17 $T^2 = 1-\Gamma^2$ power transmission |
| `manuscript/ave-kb/common/translation-tables/translation-circuit.md` | Canonical leaf | $R=\xi^{-2}\eta$ (grip=loss, line 24); microrotation PRIMARY (electron) → vorticity DERIVED (galaxy); galactic rotation = fluid/MHD emergent (lines 273-301) |
| C5 SDSS DR17 result `research/2026-05-19_c5-sdss-spin-orientation-result.md` | Marginal-D | LSS spin axis (l=129°, b=79°), σ=6.83°; CMB-LSS = 36.75° = 5.33σ from zero. Measures axis DIRECTION, NOT alignment-strength-vs-mass |
| C5 Shamir cross-catalog `research/2026-05-19_c5-shamir-2022-cross-catalog-result.md` | A (weak) | Methodology-dependent; Shamir DESI axis 3.77° from CMB (low precision); discrimination verdict: "consistent with both AVE-distinct AND null at precision available" |

### 1.2 What does NOT exist (the C1 gap)

- **No derivation of the I_s-coupling functional form.** The operator epic line 27 states the operator output is undetermined; Session 2's $A$-form is for obliquity-angle branch selection, not alignment-strength.
- **No knee derivation.** The $Q\cdot\delta$ Reynolds-analog appears only in the uncommitted memory thread (`project_cosmic_rotation_soliton_coupling_thread`, 2026-06-05, exploratory). Grant's Fork #2 there is RESOLVED ("the knee is no different than ... Reynolds number ... a dimensionless-ratio regime boundary") but the numerator/denominator of the ratio is flagged as the "soliton-lattice-coupling-operator Session 2 derivation (scoped, never run)."
- **No alignment-strength-vs-mass data test.** C5 measured axis DIRECTION and its tightness, never the alignment-strength as a function of galaxy mass / moment of inertia.

### 1.3 No contradicting prior negative

The C5 work is on a **different observable axis** (where is the cosmic axis; how tight is the dipole), and explicitly does not bear on the strength-vs-$I_s$-with-knee prediction. There is no prior corpus negative that closes the C1 strength-scaling axis. **C1 is genuinely open.** This satisfies the `ave-prereg` "genuinely open, here's the diagnostic" outcome.

### 1.4 Substrate-native check (per `substrate-native-check` trigger 6, prose-derivation of a scaling law)

| Checkpoint | C1 status |
|---|---|
| K4 / Cosserat | Coupling is Cosserat microrotation ↔ couple-stress (mutual inductance), NOT a Lagrangian energy-basin. The "alignment" is impedance matching, not gradient descent to a potential minimum. ✅ |
| Op14 saturation | Frame-drag asymmetry is the prograde-vs-retrograde Op14 saturation profile (`frame-dragging-impedance-convolution.md:24`), not a continuum-Helmholtz field. ✅ |
| Phase-space vs real-space | The alignment observable (axis direction) is real-space angular (galactic coordinates); the COUPLING-NUMBER is a dimensionless impedance/Reynolds ratio, scale-invariant per Ax 2. The data test must measure alignment-strength in matching coordinates (angular dispersion vs $I_s$), see §3. ✅ |
| EE-native, no SM default | Reynolds-analog $Q\cdot\delta$ + Op17 $T^2=1-\Gamma^2$ are EE-native (regenerative oscillator + transmission line), NOT MOND-style modified-inertia or Bianchi metric anisotropy. The grip=loss=$1/Q$ axis is the substrate-native framing. ✅ |

---

## 2. The prediction, sharpened to a falsifiable form

**P1 (coupling-number form):** the soliton-cosmic alignment coupling is set by a dimensionless number $\Pi_s$ that increases with the soliton's moment-of-inertia / knot-content $I_s$.

**P2 (knee):** there is a critical $\Pi_{\text{crit}}$ (canonically $Q\cdot\delta = 2$) below which alignment-strength → 0 (reflection / frozen / lossless) and above which alignment-strength → ceiling (absorption / matched / coherent).

**P3 (data signature):** galaxy-spin-axis alignment-strength (1 − angular dispersion about the cosmic axis, or equivalently the dipole-magnitude SNR) should be a **rising sigmoid in $\log I_{\text{gal}}$** with a knee, NOT flat and NOT a power law without threshold.

**P4 (electron anchor / sanity):** the electron ($Q=\alpha^{-1}$, $\delta\to0$, single $0_1$ unknot) sits FAR below the knee ($Q\cdot\delta\ll2$) → reflects cosmic torque → no measurable spin-axis alignment with $\hat{\Omega}_{\text{freeze}}$. This is consistent (electron spins are isotropic) and is the lossless-pivot end of the scaling.

---

## 3. Data-test design (Phase 3) — scoping and observable

### 3.1 The matched-coordinate observable (per `phase-space-coordinate-check`)

The prediction is about **alignment-STRENGTH as a function of $I_s$**, so the test must bin galaxies by a moment-of-inertia proxy and measure alignment-strength per bin:

- **$I_s$ proxy:** $I_{\text{gal}} \sim M_{\text{gal}} R_{\text{gal}}^2$. Stellar mass $M_*$ (from luminosity / mass-to-light) and disk scale-radius $R_d$ are both available in SDSS-class catalogs. A cruder single-variable proxy is absolute magnitude $M_r$ (luminosity ∝ mass). Best available proxy: $I \propto M_* \cdot R_d^2$ with $M_*$ from the MPA-JHU or NSA stellar-mass catalog and $R_d$ from the photometric profile.
- **Alignment-strength per bin:** the Longo cos-γ axial-dipole magnitude $|A| = |\frac{1}{N}\sum_i \chi_i \hat{n}_i|$ (C5 estimator) computed PER mass-bin, normalized by the randomization-null σ per bin (to control for differing N). Equivalently, the angular dispersion of per-galaxy spin vectors about the best-fit / fixed cosmic axis.
- **Knee signature:** plot alignment-strength SNR vs $\log I_{\text{gal}}$. AVE predicts a rising sigmoid with a knee; ΛCDM-isotropic predicts flat (zero) at all $I$; a generic systematic predicts monotone-without-threshold.

### 3.2 Data accessibility (per `ave-driver-script-honesty` — scope, do not fabricate)

- The C5 SDSS DR17 driver already ingests `data/sdss_dr17/GalaxyZoo1_DR_table2.csv.gz` (667,944 galaxies, chirality votes). **This is in-repo and was used for C5.**
- GZ1 Table 2 carries chirality + position but **NOT stellar mass or scale radius**. The mass proxy requires a cross-match to a photometric/stellar-mass catalog (NSA / MPA-JHU / SDSS `petroMag_r` + redshift for absolute magnitude).
- **Cheapest viable first-pass:** if GZ1 Table 2 carries an apparent-magnitude column and redshift (or a cross-matched `petroMag` + `z`), absolute magnitude $M_r$ is a luminosity (≈ mass) proxy and a coarse $I$-ordering is achievable IN-REPO without re-fetch. Disk-radius-weighted $I \propto M R^2$ requires the photometric profile cross-match.
- **Decision rule (gated):** Phase 3 first checks the in-repo GZ1 columns. IF a usable mass/luminosity proxy is present → run the binned alignment-strength driver. IF NOT → **scope precisely** (catalog = NSA v1_0_1 cross-matched to GZ1 on objID; observable = $|A|$/σ per $\log(M_* R_d^2)$ bin; cut = same δ_clear=0.4 + NVOTE≥10 as C5; expected signal = rising-sigmoid knee) and report as a scoped-not-run test. **Do NOT fabricate alignment-vs-mass numbers.**

### 3.3 What "pass" / "fail" / "scoped" mean

- **PASS (chord candidate):** alignment-strength rises with $I$ and shows a knee; the knee survives Phase 4 discrimination.
- **FAIL (honest negative, Rule 11):** alignment-strength is flat in $I$, OR rises monotonically without a knee (favoring a generic systematic / selection effect over the AVE Reynolds-knee form).
- **SCOPED:** in-repo columns insufficient; precise catalog/observable/cut/expected-signal recorded for a follow-up live-fire session.

---

## 4. Adjudication table (frozen before derivation/test)

| Outcome | Phase 1-2 derivation | Phase 3 data | Phase 4 discrimination | Verdict |
|---|---|---|---|---|
| **CHORD** | I_s-coupling + knee derived from canonical anchors with no new free param | Knee detected, alignment∝I_s | AVE-distinct (alternatives do NOT predict the knee form) | Genuine discriminating prediction; promote to foreword-candidate queue (auditor lands) |
| **ECHO** | Derivation OK | Correlation present | ΛCDM+systematics / Bianchi / MOND ALSO predict it | Real but not discriminating; record, do not headline (per `ave-discrimination-check`) |
| **NEGATIVE** | Derivation OK | Flat or no-knee | n/a | Honest negative (Rule 11); the strength-scaling prediction is falsified; close branch |
| **SCOPED** | Derivation OK | Data not in-repo | Conditional | Precise data-test scope recorded; no empirical verdict claimed |
| **DERIVATION-BLOCKED** | A canonical anchor does not assemble as expected | n/a | n/a | Surface the gap to Grant (missing-axiom-vs-engine-bug discipline); do NOT draft a new axiom |

---

## 5. Skill discipline (this prereg)

- `ave-prereg` — corpus-grep before deriving (§1); outcome = "genuinely open, here's the diagnostic" (§1.2-1.4).
- `ave-canonical-leaf-pull` — enumerated the Q-factor / mutual-inductance / boundary-observable / saturation-kernel class leaves (§1.1) before deriving.
- `substrate-native-check` trigger 6 — prose-derivation substrate-walk (§1.4) before the scaling-law derivation in the result doc.
- `verify-before-cite` — all load-bearing citations re-grepped verbatim at execution time (logged in result doc §6).
- `consistency-vs-emergence` — Class tagging deferred to result doc; the alignment observable is Class E (operating-point projection of $\hat{\Omega}_{\text{freeze}}$) but the **knee-form prediction** is a candidate emergence-class structural prediction IF it uses no CODATA-back-substituted input.
- `ave-discrimination-check` — the LOAD-BEARING gate, executed in result doc Phase 4.
- `ave-evidence-framing-discipline` — chord-vs-echo strength language.
- Pure-AVE-corpus rule — no external-context references.

---

*Prereg frozen 2026-06-05 before Phase 1 derivation. Result doc executes against this frozen prereg.*
