# Accuracy Review — Final Pass (Phase 4b Verification)

**Reviewer:** KB Accuracy Reviewer  
**Date:** 2026-04-03  
**Scope:** Phase 4b fix verification + adversarial sampling of unreviewed vol3 material

---

## Summary

The most significant new finding is a **systemic INVARIANT-S1 violation across 18 leaf documents in vol3**: six directories in the condensed-matter (ch09, ch10, ch11) and applied-physics (ch07, ch12, ch13) subdomains render resultboxes as Markdown headings (`## Resultbox: Title`) rather than the mandated blockquote format (`> **[Resultbox]** *Title*`). This pattern is confined entirely to vol3 and was not caught in prior iterations because those chapters were not sampled. A second new notation error was found in `gw-propagation-lossless.md` (vol3/gravity/ch08): the single instance of `\ell_{\text{node}}` in the source is rendered as roman `l_{\text{node}}` in the KB leaf. The summarybox and exercisebox environments from all vol3 gravity and condensed-matter source chapters (ch01, ch02, ch03, ch08, ch09, ch11) are absent from their KB leaves with no acknowledgment note — the vol3 cosmology chapters have explicit notes about this omission, but the gravity and condensed-matter chapters do not.

All Phase 4b fixes were verified correct. The protected roman ell instance in `trace-reversal-mechanism.md` was not disturbed. The `thermal-softening.md` line 9 fix was applied. The ch02 general-relativity index double-pipe correction was applied.

---

## Fixes Verified (Phase 4b)

### 1. vol3/gravity/ch01-gravity-yield/ — Batch ell normalization (6 files, ~20 instances)

- **`optical-refraction-gravity.md`**: All 9 instances are now `\ell_{node}` (script). Verified against source lines 50, 84, 88, 102, 106, 114, 118, 135, 139. CORRECT.
- **`kinetic-yield-threshold.md`**: Lines 10, 22 now use `\ell_{node}`. Verified against source lines 152, 164. CORRECT.
- **`leaky-cavity-decay.md`**: Lines 10, 12, 14 now use `\ell_{node}`. Verified against source lines 152, 164, 170. CORRECT.
- **`gravitational-coupling-constant.md`**: Lines 6, 11 now use `\ell_{node}`. Verified against source lines 102, 106. CORRECT.
- **`static-nodal-tension.md`**: Line 11 now uses `\ell_{node}`. Verified against source line 170. CORRECT.
- **`index.md`**: Lines 14, 17, 21 now use `\ell_{node}`. CORRECT.
- **`trace-reversal-mechanism.md`** (PROTECTED): Line 10 retains `$1.187 \times l_{node}$` (roman). Source line 26 uses `l_{node}`. PROTECTED INSTANCE UNMODIFIED. CORRECT.

### 2. vol2/particle-physics/ch02-baryon-sector/thermal-softening.md — Line 9 function argument fix

- Line 9 now reads `$S(|\partial_r\phi|,\,\pi/\ell_{node})$` (script ell). Source line 65 uses `\ell_{node}`. CORRECT.
- Line 55 protected roman instance `$1.0 l_{node}$` (three occurrences in sentence). Source line 103 uses `l_{node}`. PROTECTED. CORRECT.

### 3. vol3/gravity/ch02-general-relativity/index.md — Double-pipe correction

- Line 12 now reads `|\mathbf{E}|^2` and `|\mathbf{H}|^2` (single pipes). CORRECT.

---

## New Findings

---

### Finding F1 — CRITICAL

**Issue:** 18 leaf documents in vol3 render `\begin{resultbox}{Title}` as a Markdown heading (`## Resultbox: Title`) rather than the INVARIANT-S1 blockquote format (`> **[Resultbox]** *Title*`). The content of the equations is intact, but the environment type is not machine-distinguishable from a subsection heading. An agent relying on the `[Resultbox]` prefix to identify derived results will not recognize these as resultboxes.

**Location:** The following directories contain the violations (18 total instances):

- `vol3/condensed-matter/ch09-condensed-matter-superconductivity/` — files: `superconductor-type-classification.md` (line 6), `kuramoto-phase-locking.md` (line 6), `inertial-london-penetration-depth.md` (line 6)
- `vol3/condensed-matter/ch10-material-properties/` — files: `nuclear-hessian.md` (line 6), `inter-element-reflection-coefficient.md` (line 6)
- `vol3/condensed-matter/ch11-thermodynamics/` — files: `vacuum-heat-capacity.md` (line 6), `thermal-softening-correction.md` (lines 6, 12), `effective-dof-g-star.md` (line 6), `casimir-effective-temperature.md` (line 6), `baryon-asymmetry.md` (line 6), `vacuum-nyquist-baseline.md` (line 6), `macroscopic-temperature-lc-noise.md` (line 6)
- `vol3/applied-physics/ch07-stellar-interiors/` — files: `msw-resonance-critical-density.md` (line 6), `neutrino-msw-matter-potential.md` (line 6)
- `vol3/applied-physics/ch12-ideal-gas-law/` — files: `lc-energy-balance-equation.md` (line 6), `ideal-gas-law.md` (line 6)
- `vol3/applied-physics/ch13-geophysics/` — files: `seismic-reflection-coefficient-moho.md` (line 6)

**Source reference:** INVARIANT-S1 (ave-kb/CLAUDE.md) mandates that all `resultbox` environments render as `> **[Resultbox]** *Title*`. The source LaTeX files for all affected chapters use `\begin{resultbox}{Title}` uniformly.

**Avoidance requirement:** Every leaf document in the KB whose source LaTeX contains `\begin{resultbox}{...}` must render that environment as `> **[Resultbox]** *Title*` blockquote per INVARIANT-S1. The form `## Resultbox: Title` (Markdown heading) does not satisfy this invariant and is a Critical distillation error in all 18 instances enumerated above.

---

### Finding F2 — CRITICAL

**Issue:** `gw-propagation-lossless.md` line 28 renders `$V_{GW} = h \cdot c \cdot l_{\text{node}} \cdot 2\pi f$` with **roman ell** (`l_{\text{node}}`). The source (`08_gravitational_waves.tex` line 46) uses **script ell** (`\ell_{\text{node}}`). Vol3 uses script ell per INVARIANT-N2.

**Location:** `/manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md`, line 28

**Source reference:** `vol_3_macroscopic/chapters/08_gravitational_waves.tex` line 46: `$V_{GW} = h \cdot c \cdot \ell_{\text{node}} \cdot 2\pi f`

**Avoidance requirement:** The leaf `gw-propagation-lossless.md` must render the lattice node spacing symbol in the LIGO voltage expression as `\ell_{\text{node}}` (script ell), matching the source. This is the only ell_node instance in ch08.

---

### Finding F3 — CRITICAL

**Issue:** `gw-propagation-lossless.md` renders the Invariant Gravitational Impedance equation (`$Z(r) = \sqrt{\mu_{eff}/\varepsilon_{eff}} \equiv Z_0$`) as a bare display equation (lines 20–22) without the `[Resultbox]` wrapper. The source wraps this equation in `\begin{resultbox}{Invariant Gravitational Impedance}` (source line 17). The dedicated standalone leaf `invariant-gravitational-impedance.md` correctly captures the resultbox, but `gw-propagation-lossless.md`—which presents the same content as context—strips the resultbox marking. An agent reading only `gw-propagation-lossless.md` will not identify this as a named derived result.

**Location:** `/manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md`, lines 20–22

**Source reference:** `vol_3_macroscopic/chapters/08_gravitational_waves.tex` lines 17–22

**Avoidance requirement:** Where a leaf document includes content from a source `\begin{resultbox}` environment, that content must carry the `[Resultbox]` prefix per INVARIANT-S1, even when the resultbox also appears in a dedicated standalone leaf. Stripping the resultbox markup in one leaf while preserving it in another creates inconsistency in how agents identify derived results.

---

### Finding F4 — WARNING

**Issue:** The `\summarybox` and `\exercisebox` environments at the end of vol3 source chapters ch01, ch02, ch03, and ch08 (gravity domain) and ch09, ch11 (condensed-matter domain) are absent from all corresponding KB leaves, with no acknowledgment note in any of those chapter indexes. The vol3 cosmology chapter indexes (ch04, ch05, ch06, ch14, ch15) carry an explicit note: "NOTE: summarybox and exercisebox environments are not extracted as leaves." No such note appears in any gravity or condensed-matter chapter index.

The omitted summarybox content includes synthesis statements that may not appear elsewhere in the KB. Examples:
- ch01 summarybox (source lines 182–189): 4 bullet synthesis of gravity derivation, kinetic yield, particle stability, and heavy fermion decay
- ch08 summarybox (source lines 109–115): 3 bullet synthesis of GW propagation as lossless LC modulation
- ch09 summarybox (source lines 247–253): 3 bullet synthesis of superconductivity as Kuramoto phase-locking
- ch11 summarybox (source lines 327–334): 4 bullet synthesis of temperature as LC noise, entropy as geometric spreading

**Location:** 
- `vol3/gravity/ch01-gravity-yield/index.md` — no note; source summarybox at lines 182–189, exercisebox at 191–196
- `vol3/gravity/ch02-general-relativity/index.md` — no note; source summarybox at lines 151–158, exercisebox at 160–165
- `vol3/gravity/ch03-macroscopic-relativity/index.md` — no note; source summarybox at lines 182–189, exercisebox at 191–196
- `vol3/gravity/ch08-gravitational-waves/index.md` — no note; source summarybox at lines 109–115, exercisebox at 117–122
- `vol3/condensed-matter/ch09-condensed-matter-superconductivity/index.md` — no note; source summarybox at lines 247–253, exercisebox at 255–260
- `vol3/condensed-matter/ch11-thermodynamics/index.md` — no note; source summarybox at lines 327–334, exercisebox at 336–341

**Source reference:** `vol_3_macroscopic/chapters/01_gravity_and_yield.tex` lines 182–196; `02_general_relativity_and_gravity.tex` lines 151–165; `03_macroscopic_relativity.tex` lines 182–196; `08_gravitational_waves.tex` lines 109–122; `09_condensed_matter_superconductivity.tex` lines 247–260; `11_thermodynamics_and_entropy.tex` lines 327–341

**Avoidance requirement:** Either (a) the summarybox and exercisebox content must be present in the corresponding KB leaves with proper `[Summarybox]` and `[Exercisebox]` INVARIANT-S1 markup, or (b) each affected chapter index must carry the same explicit omission note that the vol3 cosmology indexes carry ("NOTE: summarybox and exercisebox environments are not extracted as leaves"). The inconsistency between cosmology (noted) and gravity/condensed-matter (silent) is itself a navigational hazard — an agent reading a gravity chapter index has no signal that chapter-end synthesis content exists in the source but is not here.

---

## Confirmed Clean

The following items were explicitly verified as accurate in this pass:

1. **All 6 files in vol3/gravity/ch01-gravity-yield/ with Phase 4b ell fixes**: Script ell confirmed against source at all corrected instances. Roman ell at protected instance (source line 26) preserved.

2. **vol2/ch02-baryon-sector/thermal-softening.md Phase 4b fix**: Line 9 script ell confirmed. Lines 55, 73, 86 ell variants match source exactly (line 55 roman matching source line 103; lines 73 and 86 script matching source lines 121 and 131).

3. **vol3/gravity/ch02-general-relativity/index.md Phase 4b fix**: Single-pipe `|\mathbf{E}|^2` and `|\mathbf{H}|^2` confirmed.

4. **vol3/condensed-matter/ch09 and ch11 ell notation**: Source uses script ell throughout; KB leaves match. No roman ell contamination.

5. **vol3/gravity/ch03-macroscopic-relativity/**: No ell_node instances — chapter scope (GM/c²r-level quantities) does not require node spacing notation. Correct.

6. **vol3/gravity/ch08-gravitational-waves/ ell notation** (excluding Finding F2): No other ell_node instances in ch08 KB leaves. The single source instance was in the one leaf with the error (F2 above).

7. **vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md**: Script ell used throughout, matches source `15_black_hole_orbital_resonance.tex` lines 8, 39, 41.

8. **vol3/condensed-matter/ch09 remaining-ch09-results.md and ch11 ch11-remaining-resultboxes.md**: Pure navigation manifests with no mathematical content. All listed resultboxes map to named KB leaves. No unverified content.

9. **`[Result]` vs `[Resultbox]` pattern**: No instances of `**[Result]**` remain in any KB volume. Prior finding fully resolved.

10. **INVARIANT-S1 heading violations confined to vol3**: No `## Resultbox:` heading format violations exist in vol1, vol2, vol4, vol5, vol6, vol7, or vol8.

---

## Out of Scope

- vol1, vol2 (non-ch02), vol4, vol5, vol6, vol7, vol8: Not re-reviewed in this pass. Prior iterations cover these. Only vol2/ch02-baryon-sector/thermal-softening.md was spot-checked per Phase 4b scope.
- vol3/applied-physics/ ch07, ch12, ch13 content accuracy (equations, math): Only the INVARIANT-S1 format issue (F1) was identified; leaf math content was not read side-by-side against source. These chapters are not yet fully sampled for leaf fidelity.
- vol3/gravity/ch03 and ch08 full leaf fidelity: Only ell_node notation and resultbox format were checked; prose fidelity was not reviewed sentence-by-sentence.
- vol3/condensed-matter/ch10 leaf math content: Only INVARIANT-S1 format was checked; chapter not previously sampled for equation accuracy.
