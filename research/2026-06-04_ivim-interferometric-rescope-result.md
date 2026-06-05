# IVIM Round-2 result — interferometric re-scope derivation + SNR + inventory (2026-06-04)

**Branch:** `analysis/2026-06-04-ivim-round2-rescope`.
**Pre-reg:** [`research/2026-06-04_ivim-round2-prereg.md`](2026-06-04_ivim-round2-prereg.md).
**Adjudication:** [`research/2026-06-03_ivim-RA-adjudication.md`](2026-06-03_ivim-RA-adjudication.md) (Grant R-A).

## VERDICT (one line)

**DEFENSIBLE-INTERFEROMETRIC-DISCRIMINATOR (structure) — but NOT a near-term tabletop
falsifier (honest SNR ≪ 1).** The structural axes survive parameter-free; the magnitude at
the recommended 100 µm-gap geometry is undetectable (SNR ≈ 2×10⁻² in a 1-day shot-noise
run, time-to-SNR=1 ≈ 7.6 yr; reaching SNR=1 in 1 day needs E ≈ 6.3×10¹² V/m, ABOVE
clean-tip field-emission onset → ruptures the apparatus before the signal is visible).

(Section bodies below.)

## 1. Derivation off the CORRECT per-node kernel

All substrate constants imported from `ave.core.constants` (`ave-canonical-source`,
verified `V_YIELD = √α·V_SNAP` and `E_YIELD = V_YIELD/ℓ_node` self-consistent):

| Constant | Value | Provenance |
|---|---|---|
| `V_YIELD` | 4.36519×10⁴ V | `constants.py:387` = `√α·V_SNAP` |
| `ℓ_node` (`L_NODE`) | 3.86159×10⁻¹³ m | `constants.py:239` = `ℏ/(m_e c)` (reduced Compton) |
| `E_YIELD` | 1.13041×10¹⁷ V/m | `constants.py:398` = `V_YIELD/ℓ_node` (**per-node yield FIELD**) |
| `Z_0` | 376.7303 Ω | `constants.py:98` = `√(μ₀/ε₀)` |
| `α` | 7.2973526×10⁻³ | `constants.py` |

**The chain (leaf-self-consistent):**
1. Kernel (Ax 4, asymmetric ε-only): `ε_eff(A) = ε₀√(1−A²)`, **`A = E_local/E_YIELD`**
   (per-node strain). This is the round-1 correction: NOT `V_apparatus/V_YIELD`.
2. Index from the leaf's own `Z_local = Z₀(1−A²)^{−1/4}` (i.e. `n_eff = c√(μ₀ε_eff)`):
   `n_eff = (1−A²)^{1/4}`, so `δn = n_eff − 1 ≈ −A²/4` (leading, A≪1; A⁴ next).
3. Phase shift: `Δφ = (2π/λ)·δn·L_int`, λ = 532 nm.

**The per-node strain at the leaf's literal operating point** (uniform field, 43.65 kV /
100 µm gap):

```
E_uniform = V_app/d_gap        = 4.36500×10⁸ V/m
A_uniform = E_uniform/E_YIELD  = 3.86143×10⁻⁹      <-- NOT 0.99
```

The leaf's `V_app/V_YIELD = 1.0000` is overstated by `d_gap/ℓ_node = 2.590×10⁸` — exactly
the round-1 factor. `Γ→1` at 43.65 kV is the conflation; the true `A ~ 4×10⁻⁹`.

**Operating-point sweep** (sharp-tip enhancement `E_tip = β·V/R_tip`, β ≈ 1/5 per the
`G_geom ~ 10⁵` sharp-tip-pair figure, `trampoline-framework.md:685`):

| Config | A = E_local/E_YIELD | δn ≈ −A²/4 | Δφ = (2π/λ)δn·L_int |
|---|---|---|---|
| uniform 43.65 kV / 100 µm (L=100 µm) | 3.861×10⁻⁹ | −3.728×10⁻¹⁸ | −4.40×10⁻¹⁵ rad |
| STM tip R=10 nm @43.65 kV (L≈R=10 nm) | 7.723×10⁻⁶ | −1.491×10⁻¹¹ | −1.76×10⁻¹² rad |
| STM tip R=10 nm @200 kV push (L≈10 nm) | 3.539×10⁻⁵ | −3.130×10⁻¹⁰ | −3.70×10⁻¹¹ rad |

> **FLAG (index-convention discrepancy — flag-don't-fix, NOT resolved here):** the sibling
> leaf `ch12.../vacuum-birefringence-e4.md` and `divergence-test-substrate-map.md:63` write
> `Δn = 1 − √(1−A²) ≈ +A²/2`. This leaf's chain gives `δn ≈ −A²/4`. Both yield E⁴
> intensity-slope, but the **phase coefficient (factor 2) and sign differ by convention**
> (index-via-impedance `n=(1−A²)^{1/4}` vs index-via-permittivity-deficit `n=√(1−A²)·…`).
> Surfaced for a cross-leaf reconciliation pass. Round-2 uses the mirror-leaf's own
> `−A²/4` for the mirror-leaf re-scope (self-consistent within the leaf being edited).
> Magnitude conclusions (SNR ≪ 1) are robust to this factor-2.

Driver: `/tmp/ivim_interferometric_v2.py` (analytic leading term used to avoid float64
catastrophic cancellation on `(1−A²)^{1/4}−1` at A²~10⁻¹⁷; constants imported, not hardcoded).

## 2. Honest interferometric magnitude + SNR

Shot-noise-limited interferometer (the OPTIMISTIC floor): `Δφ_min = 1/√N_ph`,
`N_ph = P·τ·λ/(hc)`, P = 0.5 mW (leaf probe), λ = 532 nm. **Headline config = STM tip
R=10 nm @43.65 kV** (the most favorable *recommended-geometry* point; `Δφ = 1.76×10⁻¹² rad`):

| Integration τ | N_ph | Δφ_min (shot) | **SNR** |
|---|---|---|---|
| 1 s | 1.34×10¹⁵ | 2.73×10⁻⁸ rad | 6.4×10⁻⁵ |
| 1 hr | 4.82×10¹⁸ | 4.56×10⁻¹⁰ rad | 3.9×10⁻³ |
| 1 day | 1.16×10²⁰ | 9.30×10⁻¹¹ rad | 1.9×10⁻² |
| 1 month | 3.47×10²¹ | 1.70×10⁻¹¹ rad | 1.0×10⁻¹ |

- **Time to SNR = 1** (headline config, P = 0.5 mW): `N_ph = 1/Δφ² = 3.23×10²³` →
  **τ ≈ 2.41×10⁸ s ≈ 7.6 yr** of continuous shot-noise-limited integration. (And this
  ignores all real interferometer noise: laser frequency drift, mirror thermal noise,
  vibration — i.e. 7.6 yr is a *floor*, the real time is longer or unreachable.)
- **Field needed for SNR = 1 in a realistic 1-day run** (STM tip, L = 10 nm):
  `A_need = 5.61×10⁻⁵` → `E_need = 6.34×10¹² V/m` → `V_tip ≈ 3.17×10⁵ V`. This field is
  **ABOVE clean-tip field-emission / vacuum-breakdown onset (~few×10¹⁰ V/m)** — the
  electrode emits / the gap arcs long before the probe accumulates a detectable phase.

**Conclusion (honest, `ave-evidence-framing-discipline`):** off the correct per-node kernel,
the interferometric Δφ at the recommended tabletop geometry is **SNR ≪ 1** by 1–2 orders of
magnitude even after a 1-month shot-noise-limited run, and the field that *would* give
SNR ~ 1 ruptures the apparatus first. This is the interferometric-side confirmation of the
same conclusion round-1 reached from the photon-counting side: the recommended IVIM tabletop
apparatus is NOT a near-term falsifier. The PHASE-SLOPE measurement (E² vs E⁴, see §3)
remains the meaningful test, but it requires the facility-class fields already named by the
sibling leaf `vacuum-birefringence-e4.md` (E ~ 10¹⁶ V/m).

## 3. Structural discriminator (what survives) + consistency-class framing

The verdict is DEFENSIBLE-INTERFEROMETRIC-**DISCRIMINATOR** (not RETIRE) because two
parameter-free AVE-vs-QED axes survive independent of magnitude:

1. **Tree-vs-loop scaling (the 8.38×10¹² ratio, traced clean round-1).** AVE `δn ~ −A²/4`
   is a *tree-level* kernel term (geometric saturation of the LC string). QED's vacuum index
   shift is a *loop* (Euler-Heisenberg). The phase-vs-field SLOPE in a log-log fringe sweep
   is the observable: AVE predicts the kernel's E⁴-intensity / E²-phase shape with the AVE
   coefficient; QED predicts the Euler-Heisenberg coefficient. Same functional family at
   low field (see consistency note below), different coefficient by ~10¹² — but the
   *coefficient* is only resolvable once the *signal* is above noise (§2: it is not, at the
   tabletop geometry).
2. **Isotropy vs birefringence (the cleaner structural axis).** The AVE kernel keys off
   `|E|` → isotropic δε → **scalar** phase (same shift for both probe polarizations). QED's
   Euler-Heisenberg vacuum is **birefringent** in a background field (n∥ ≠ n⊥). So the
   *cross-polarized phase difference* `Δφ∥ − Δφ⊥` is **0 in AVE, ≠ 0 in QED** — a
   pattern/SIGN discriminator that does not require resolving the 10¹² coefficient, only
   the presence/absence of birefringence. This is the PVLAS-class axis. (`ave-walk-back`
   note: this is the axis the re-scoped leaf should carry forward, NOT the APD count.)

**Consistency-vs-emergence classification (frozen in pre-reg §4, confirmed):**

| Component | Class | Evidence |
|---|---|---|
| Δφ itself (small-A) | **consistency** | `claim-quality.md:75`: leading correction "formally identical to the Euler-Heisenberg low-field limit; recovers linear Maxwell to arbitrary precision." A quadratic-in-A index shift is NOT AVE-unique. |
| Tree-vs-loop coefficient | **manifestation / structural** | scaling-origin difference, zero free parameter, traced round-1. |
| Isotropy vs birefringence | **manifestation / structural** | polarization-pattern (sign) test, not a coefficient. |

**Headline discipline:** the re-scoped leaf must NOT headline an emergence claim. The
defensible content is: *a parameter-free structural discriminator (tree-vs-loop + isotropy)
whose magnitude is undetectable at the recommended tabletop geometry and which requires
facility-class fields (E ~ 10¹⁶ V/m, per the sibling birefringence leaf) to reach SNR ~ 1.*

## 4. Broader-conflation site inventory (BLOCKED on Grant §4 — flag-don't-fix, do NOT edit)

The per-node-V_yield / apparatus-voltage conflation propagates beyond the IVIM leaf. Per the
RA-adjudication §4, the corpus-wide sites are a **PENDING GRANT DECISION** (tied to the
PONDER-05 consistency-vs-emergence question and the kernel-convergence-narrative). This
session re-scopes ONLY the IVIM-local leaf (deliverable c). The sites below are
**inventoried, not edited** (flag-don't-fix). Definition of conflation: an *apparatus gap
voltage* (~30/35/43 kV across a macroscopic gap) substituted into `(V/V_yield)` as if
`V_apparatus → V_yield`. (Sites that merely quote the kernel *constitutive form*
`S(V)=√(1−(V/V_yield)²)` with `V` = per-node voltage are NOT counted.)

### 4A. CORPUS-WIDE — BLOCKED on Grant §4 (PONDER-05 family + measurement-hierarchy) — 8 sites

| # | File:line | Verbatim conflation | Note |
|---|---|---|---|
| 1 | `vol4/falsification/ch11-experimental-bench/measurement-hierarchy-snr.md:66` | *"detects 27.4% ε_eff collapse at V_DC/V_yield = 0.687 (bench-measurable at ~30 kV bias)"* | named in RA §4. 27.4% collapse needs A=0.687 → E≈7.8×10¹⁶ V/m, unreachable at 30 kV across macroscopic quartz absent G_geom~10⁶. |
| 2 | `common/universal-saturation-kernel-catalog.md:72` | *"V_DC/V_yield = 0.687 (bench-measurable at ~30 kV bias)"* | named in RA §4. Same as #1. |
| 3 | `common/translation-tables/translation-circuit.md:111` | *"PONDER-05 canonical bench tester at V_DC/V_yield = 0.687"* | NOT in RA §4 — newly surfaced. Asserts 0.687 as if reachable. |
| 4 | `common/translation-tables/translation-circuit.md:191` | *"PONDER-05 bench tester at V_DC/V_yield = 0.687"* | NOT in RA §4 — newly surfaced. |
| 5 | `common/translation-tables/translation-circuit.md:481` | *"PONDER-05 at V_DC/V_yield = 0.687"* | NOT in RA §4 — newly surfaced. |
| 6 | `common/op14-local-clock-modulation.md:106` | *"DC-biased quartz at V_DC/V_yield = 0.687 should show … 27.4% slowing"* | named in RA §4 (as the PONDER-05 anchor). The c_eff-modulation forward-claim inherits the same A=0.687 reachability gap. |
| 7 | `common/divergence-test-substrate-map.md:126` | *"30 kV DC bias across quartz cylinder … holds material at 68.7% of V_yield = 43.65 kV"* | NOT in RA §4 — newly surfaced. Explicit apparatus-30 kV ↔ 68.7%-of-V_yield equation. |
| 8 | `common/divergence-test-substrate-map.md:466` (B7-PONDER-05 matrix row) | *"30 kV DC bias holds quartz at 68.7% V_yield"* | NOT in RA §4 — newly surfaced. Matrix-row form of #7. |

> **Inventory count (corpus-wide BLOCKED): 8 sites** (2 named in RA §4 + 6 newly surfaced
> this sweep). The RA §4 "honest/corrected camp" sites (`trampoline-framework.md:439`/`:685`
> Q-G42 G_geom; `claim-quality.md:393`/`:79`; `ybco-phased-array.md:8` INVALIDATED) are NOT
> conflations — they are the *correct* readings and are listed here only as the resolution
> template Grant's §4 call would propagate.
>
> **The load-bearing question (RA §4, unchanged):** PONDER-05's "V_DC/V_yield = 0.687" is
> either (1) vacuum-kernel reading → needs a real resonant-enhancement geometry to reach
> A=0.687 that the "30 kV" framing omits (same conflation as the IVIM leaf), OR (2)
> material reading → "V_yield" is a *quartz-material* saturation voltage and 27.4% is
> quartz's ordinary voltage-coefficient-of-capacitance (Class-II ceramic behavior,
> `translation-circuit.md:481` already analogizes it). **Only Grant + a PONDER-side trace
> can decide.** If reading (2), PONDER-05 is consistency-class, not a forward vacuum
> discriminator, and Q-G42 (the V²-coefficient SIGN test) becomes the one clean forward
> discriminator of the saturation kernel. DO NOT edit sites #1–#8 before that call.

### 4B. IVIM-LOCAL — this branch's authorized scope (re-scoped or flagged-for-IVIM-sweep)

| File:line | Status |
|---|---|
| `vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md` | **RE-SCOPED this branch** (deliverable c). |
| `vol4/claim-quality.md:357,377` clm-5s5b0d (`Γ→1 as V→V_yield`) | flagged for IVIM sweep (RA §6) — NOT edited this branch (kept scope to the leaf per task item 2; claim-quality is a follow-on within the IVIM-local set). |
| `vol4/claim-quality.md:390` (IMD variant *"measurable above ~30% of V_yield (~13 kV)"*) | NOT in RA §6 — newly surfaced IVIM-local site; same conflation (apparatus 13 kV ↔ 30% V_yield). Flag for the IVIM sweep. |
| `cosmological-constant-closure.md:131` (*"Γ_bench = 1.94×10⁻¹¹ at 43.65 kV"*) | flagged for IVIM sweep (RA §6). |
| `ch11-experimental-bench-falsification/index.md:30` (Γ(V) row, `Γ→1 as V→V_yield`) | NOT in RA §6 — newly surfaced; flag for IVIM sweep. |
| `ch11-experimental-bench/advanced-protocols.md:29–37` (Z_local/Γ + *"sweep past 35 kV → APD spike"*) | RA §6 (the AVE-Bench Ch 12/14/23/28 re-freeze sibling). Flag. |
| `common/ave-analytical-toolkit-index.md:192` (Γ(V) toolkit entry) | NOT in RA §6 — newly surfaced; flag for IVIM sweep. |
| `common/divergence-test-substrate-map.md:63` (B1 row) | already uses **correct** `E/E_yield`; only the trailing `Γ(V)→1 as V→43.65 kV` clause is the photon-counting remnant. Flag (low-priority). |

### 4C. INDEX-CONVENTION discrepancy (flag-don't-fix, separate from the V_yield conflation)

`δn ≈ −A²/4` (impedance-mirror leaf chain `n=(1−A²)^{1/4}`) vs `Δn ≈ +A²/2`
(`vacuum-birefringence-e4.md` + `divergence-test-substrate-map.md:63` chain
`Δn=1−√(1−A²)`). Same E⁴ intensity-slope; phase coefficient (×2) and sign differ. Surfaced
for a cross-leaf reconciliation pass (NOT this branch). 2 sites: the e4-leaf + substrate-map:63.

## 5. AVE-Bench-VacuumMirror protocol-doc patch (DOCUMENTED DIFF — do NOT push)

**Scope (per task item 4):** this is a DOCUMENTED patch for the reviewed follow-on sync into
`AVE-Bench-VacuumMirror`. It is NOT pushed to that repo from this branch. It re-freezes the
photon-counting headline (the Ch 12/14/23/28 / `analysis/2026-06-03-ivim-harden` route named
in RA §6) to the interferometric framing with the honest round-2 numbers. The exact target
files in AVE-Bench-VacuumMirror are reachable from that repo's
`docs/analysis/2026-06-03_ivim_adversarial_reverification.md` (Camp-B leaves); the patch
below is expressed against the canonical Camp-B claim text so the sync can apply it
verbatim regardless of which Camp-B leaf hosts the headline.

```diff
--- a/docs/analysis/<camp-B-headline-leaf>.md   (AVE-Bench-VacuumMirror)
+++ b/docs/analysis/<camp-B-headline-leaf>.md
@@ Detection mode / headline @@
-## Detection: single-photon APD back-scatter counting
-Sweep DC gap voltage past 35 kV across the 100 µm gap; the APD registers a
-sudden non-linear spike in back-scattered photons. Predicted Γ_bench = 1.94×10⁻¹¹
-at 43.65 kV, 70–1025σ over the APD dark-count floor.
+## Detection: interferometric scalar-phase (NOT photon-counting)
+The recommended geometry is WKB-suppressed and the per-node strain at the
+apparatus field is A = E_local/E_YIELD ≈ 3.9×10⁻⁹ (uniform 43.65 kV / 100 µm),
+NOT V_apparatus/V_YIELD ≈ 0.99. The detectable observable is the scalar phase
+shift of a probe in a high-finesse cavity / Mach-Zehnder, NOT an APD count:
+
+  δn  = (1−A²)^{1/4} − 1 ≈ −A²/4,   A = E_local/E_YIELD,  E_YIELD = 1.130×10¹⁷ V/m
+  Δφ  = (2π/λ)·δn·L_int           (λ = 532 nm)
+
+Honest magnitude at the recommended geometry (best STM-tip enhancement,
+R_tip = 10 nm, β ≈ 1/5, 43.65 kV):  Δφ ≈ 1.8×10⁻¹² rad.
+
+Honest SNR (shot-noise floor, 0.5 mW probe): SNR ≈ 3.9×10⁻³ (1 hr),
+1.9×10⁻² (1 day), 1.0×10⁻¹ (1 month); time-to-SNR=1 ≈ 7.6 yr. The field
+that would give SNR=1 in 1 day (E ≈ 6.3×10¹² V/m) is ABOVE clean-tip
+field-emission onset, so the apparatus ruptures before the signal is visible.
+
+CONCLUSION: the recommended tabletop apparatus is NOT a near-term falsifier.
+The meaningful test is the E²-vs-E⁴ phase-SLOPE (tree-vs-loop) and the
+isotropy-vs-birefringence pattern, which require facility-class fields
+(E ~ 10¹⁶ V/m, per vacuum-birefringence-e4.md), not 43.65 kV across 100 µm.
@@ What survives @@
-The V⁴ Bragg law and the 8.38×10¹² AVE-vs-QED coefficient ratio give a 70σ APD signal.
+The V⁴ scaling and the 8.38×10¹² AVE-vs-QED coefficient ratio SURVIVE (traced
+clean, zero free parameter) as the STRUCTURAL discriminator — but as a phase-slope
+/ birefringence-pattern discriminator, NOT a photon-count magnitude. The magnitude
+at the recommended geometry is undetectable (SNR ≪ 1 above).
@@ Operating point @@
-The experiment sweeps exactly up to the 43.65 kV V_yield ceiling.
+43.65 kV is NOT a ceiling at the apparatus scale (A ~ 10⁻⁹–10⁻⁵). The real
+ceiling is electrode field-emission / vacuum breakdown. Since the phase ∝ V²,
+push V higher than 43.65 kV until breakdown; do NOT frame 43.65 kV as the
+saturation operating point of the apparatus.
```

> **Patch provenance:** numbers from §1–§2 (driver `/tmp/ivim_interferometric_v2.py`,
> constants imported from `ave.core.constants`). The `<camp-B-headline-leaf>` placeholder is
> resolved at sync time against AVE-Bench-VacuumMirror's Camp-B leaf set
> (`analysis/2026-06-03-ivim-harden`); this result-doc deliberately does not hardcode that
> repo's internal path because this branch does not touch that repo (cross-repo session
> scope: the sync is a reviewed follow-on in a different session).

---

## Appendix — auditor-gate self-check (pre-commit)

- [x] `ave-prereg`: corpus-grep done BEFORE deriving (prereg §3 timestamped before result).
- [x] `ave-canonical-source`: `V_YIELD, E_YIELD, L_NODE, Z_0, ALPHA, EPSILON_0` imported,
      nothing hardcoded; `V_YIELD=√α·V_SNAP` and `E_YIELD=V_YIELD/ℓ_node` verified self-consistent.
- [x] `consistency-vs-emergence`: Δφ classified consistency; discriminators classified
      manifestation/structural; no emergence headline.
- [x] `phase-space-coordinate-check`: scalar phase is real-space-matched; impedance-plane Γ
      is the *derived* quantity, not the readout; documented prereg §2.4.
- [x] `ave-walk-back`: applied WITHIN the leaf only; the broader corpus is inventoried not edited.
- [x] `ave-evidence-framing-discipline`: SNR ≪ 1 stated in verdict, §2, leaf, and patch.
- [x] flag-don't-fix: index-convention discrepancy (§4C) and PONDER-05 reading (§4A) surfaced
      with verbatim file:line, NOT resolved.
- [x] PURE-AVE-CORPUS: no external-context references.

