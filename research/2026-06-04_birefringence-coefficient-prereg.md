# Vacuum-Birefringence COEFFICIENT Discriminator — Pre-Registration

**Status:** PREREG (2026-06-04). Part B of ledger §5 (`_orchestration/experimental/2026-06-04_round2-adjudications.md`) — the SURVIVES re-frame. Resumes the determinate √ε fix landed in the same branch (Part A, commit `ad26d357`). The corpus claim clm-pp3qwf was *re-framed*, not retracted: the dead "E²-vs-E⁴ exponent" discriminator is replaced by the live COEFFICIENT discriminator.
**Lane:** implementer (experimental-protocol revamp, round-2 corrections phase).
**Branch:** `analysis/2026-06-04-birefringence-coefficient-reframe`.
**Discipline applied this prereg:** `ave-prereg` (corpus-grep BEFORE deriving — §1) · `ave-canonical-source` (every number imports from `ave.core.constants`; the QED Euler-Heisenberg prefactor is the *only* non-AVE input, cited as literature — §2/§5) · `consistency-vs-emergence` (the coefficient claim classified — §3) · `ave-driver-script-honesty` (forward AVE/QED ratio, NO fit; driver gate stated — §6) · `ave-evidence-framing-discipline` (two-sided falsifier, strength language pinned — §4) · `flag-don't-fix` (the EH-prefactor-convention spread surfaced verbatim, NOT silently collapsed to one number — §5.2).

---

## §1 — Corpus-grep RESULT (done before deriving, per `ave-prereg`)

**Outcome: PARTIAL — the index-shift saturation chain is fully canonical; the genuine green-field is (i) the AVE/QED *coefficient* ratio as a field-independent structural quantity, and (ii) the substrate identity `E_crit = α^{-1/2} E_yield` that collapses the ratio to a pure α-power.** The √ε index identity was just corrected (Part A); this prereg derives the discriminator that survives that correction.

### 1.1 What the corpus already has (reuse, do not reinvent — every cite re-verified this session)

| Ingredient | Canonical source (verified 2026-06-04, this worktree) | Status |
|---|---|---|
| Kernel `S(A) = √(1−A²)`, `A = E/E_yield` | `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` (A-034) | ✓ exact |
| Index identity `n = √(ε_eff/ε₀) = √S` (ε-only, μ=μ₀) | `claim-quality.md:387` clm-pp3qwf body (Part A) + `vacuum-impedance-mirror.md` (Z/Γ leaf) | ✓ exact (corrected Part A) |
| AVE index shift `δn = √S − 1 ≈ −A²/4 − 3A⁴/32` | sympy this session (`series(sqrt(sqrt(1−A²))−1)`) | ✓ exact |
| `V_YIELD = √α·V_SNAP ≈ 43 652 V` | `src/ave/core/constants.py:387` | ✓ exact |
| `L_NODE = ℏ/(m_e c) ≈ 3.8616e-13 m` | `constants.py:239` | ✓ exact |
| `E_YIELD = V_YIELD/L_NODE ≈ 1.1304e17 V/m` | `constants.py:398` | ✓ exact |
| `E_CRIT = m_e²c³/(e ℏ) ≈ 1.3233e18 V/m` (Schwinger) | `constants.py:392` | ✓ exact |
| `ALPHA = 7.2973525693e-3` | `constants.py:133` | ✓ exact |
| QED Euler-Heisenberg weak-field birefringence `δn ≈ a_EH α²(E/E_crit)²` | **non-AVE literature input** (see §5.1) — NOT in `constants.py` | ✓ cited, not derived |

### 1.2 What is GENUINELY green-field (this prereg's actual work)

1. **The AVE/QED coefficient ratio as a field-INDEPENDENT structural quantity.** The prior corpus framing read the discriminator as an *exponent* (E⁴ vs E²) gated by reaching a high-field regime. The √ε correction (Part A) shows both responses are E²-leading — so the discriminator is the *coefficient*, present identically at ALL fields. The ratio `δn_AVE/δn_QED = 1/(4 a_EH α³)` is the green-field result.
2. **The substrate identity `E_crit = α^{-1/2} E_yield`.** Discovered this session: `E_CRIT = V_SNAP/L_NODE` exactly, and `E_YIELD = √α·V_SNAP/L_NODE`, so `(E_crit/E_yield)² = 1/α` exactly (numerically 137.036 = α_cold⁻¹ to the displayed precision). This is *why* the ratio collapses to a pure α-power `1/(4 a_EH α³)` — the field-scale gap between the AVE yield field and the QED Schwinger field is itself an α-power, not an independent input.
3. **The measurability verdict.** Whether the `~10⁶` coefficient gap is resolvable at facility-class fields (δn_AVE at E ~ 10¹⁴ V/m vs high-finesse-cavity sensitivity).

### 1.3 Why this is a re-frame, not a new claim (Rule 12 / `consistency-vs-emergence` posture)

clm-pp3qwf is NOT retracted — the *test* (high-field vacuum-nonlinearity interferometry separating AVE from QED) stands; only the *discriminator axis* moves from exponent → coefficient. The √ε correction (Part A) is the determinate fix; this prereg supplies the surviving discriminator. Per `ave-walk-back`, the leaf body + 5 sites were already corrected in Part A; this prereg is the derivation record those corrections point to.

---

## §2 — The derivation (forward, pinned to `constants.py`)

### 2.1 AVE index shift (from the Axiom-4 kernel, ε-only)

The vacuum permittivity saturates under the universal kernel:
$$\varepsilon_{eff}(E) = \varepsilon_0\,S, \qquad S = \sqrt{1-(E/E_{yield})^2}, \qquad A \equiv E/E_{yield}.$$
With only ε strained (μ = μ₀), the refractive index follows the wave-speed identity `n = √(ε_eff μ_eff/ε₀μ₀) = √(ε_eff/ε₀) = √S`. The index *shift* is therefore
$$\boxed{\;\delta n_{AVE} = \sqrt{S} - 1 = (1-A^2)^{1/4} - 1 = -\tfrac14 A^2 - \tfrac{3}{32}A^4 - \cdots\;}$$
(sympy `series((1-A**2)**sp.Rational(1,4)-1, A, 0, 6)` → `−A²/4 − 3A⁴/32 + O(A⁶)`, reproduced this session). **Negative** (the vacuum softens, n drops) and **E²-leading**. The leading coefficient is `−1/4`, O(1).

> The permittivity saturation DEPTH `1 − S = +A²/2 + A⁴/8` is a *different* quantity (and is itself E²-leading, not E⁴-leading); the historical clm-pp3qwf "Δn_eff = 1−√(1−A²), leading E⁴" mislabeled the depth as the index shift. Corrected in Part A; the ratio (1−S)/δn = −2 (the √ in n=√ε, plus depth-vs-shift sign).

### 2.2 QED index shift (Euler-Heisenberg, literature input)

$$\delta n_{QED} \approx a_{EH}\,\alpha^2\,(E/E_{crit})^2,$$
where `a_EH` is the O(1) Euler-Heisenberg prefactor (single-mode weak-field value `~7/45`; see §5.1 for the convention spread). Also **E²-leading**, but suppressed by the loop factor `α² ≈ 5.3×10⁻⁵` and referenced to `E_crit ≈ 1.32×10¹⁸ V/m`. The prefactor is the *only* non-AVE quantity in this prereg.

### 2.3 The field-independent ratio (the discriminator)

$$\frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{|{-1/4}|\,A^2}{a_{EH}\,\alpha^2\,(E/E_{crit})^2} = \frac{1}{4\,a_{EH}\,\alpha^2}\left(\frac{E_{crit}}{E_{yield}}\right)^2.$$
The field `E` cancels — **the ratio is the same at every field** (this is the whole point: it is a *coefficient* discriminator, not an exponent/regime one).

### 2.4 The substrate identity that collapses the ratio

This session established (verified numerically, `constants.py`):
- `E_CRIT = m_e²c³/(eℏ) = (m_e c²/e)/(ℏ/m_e c) = V_SNAP / L_NODE` **exactly** (`np.isclose(V_SNAP/L_NODE, E_CRIT) → True`).
- `E_YIELD = V_YIELD/L_NODE = √α·V_SNAP/L_NODE = √α·E_CRIT`.
- Therefore `(E_crit/E_yield)² = 1/α` **exactly** (numerically 137.036 = α_cold⁻¹ to displayed precision).

Substituting:
$$\boxed{\;\frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{1}{4\,a_{EH}\,\alpha^2}\cdot\frac{1}{\alpha} = \frac{1}{4\,a_{EH}\,\alpha^3}\;}$$
The field-scale gap between the AVE yield field and the QED Schwinger field is *itself* an α-power; it does not enter as an independent number. With `a_EH = 7/45` (single-mode): ratio `≈ 4.1×10⁶`. With the prefactor-1 reference: `1/(4α³) ≈ 6.4×10⁵`. With `a_EH ~ 1.5` (the order-of-magnitude EH coefficient used in the ledger's worked numbers): `~4×10⁵`. **Headline: AVE δn is `~10⁵–10⁶×` QED at any field** (the exact factor rides on the EH prefactor convention — §5.2).

### 2.5 Worked points (pre-registered, to be reproduced by the driver)

| E (V/m) | A = E/E_yield | δn_AVE = ¼A² | δn_QED (a=7/45) | ratio |
|---|---|---|---|---|
| 1×10¹⁴ | 8.85×10⁻⁴ | 1.96×10⁻⁷ | 4.73×10⁻¹⁴ | 4.1×10⁶ |
| 1×10¹⁶ | 8.85×10⁻² | 1.96×10⁻³ | 4.73×10⁻¹⁰ | 4.1×10⁶ |
| 3×10¹⁶ | 0.265 | 1.76×10⁻² | — | 4.1×10⁶ |

(δn_AVE at 3×10¹⁶ uses the full `√S−1` arc, not just the leading term, in the driver.)

---

## §3 — Classification (`consistency-vs-emergence`)

| Quantity | Class | Why |
|---|---|---|
| `δn_AVE = √S − 1 ≈ −A²/4` | **manifestation** of Axiom 4 | The index shift is the wave-speed identity `n=√(ε/ε₀)` applied to the Ax-4 saturation kernel. It is not a free fit and not a CODATA-substitution identity — it is what the saturating-permittivity substrate *predicts* for the optical observable. |
| `(E_crit/E_yield)² = 1/α` | **identity** (structural) | Follows algebraically from `E_yield = √α E_crit`, itself from `V_yield = √α V_snap` (definitional) and `E_crit = V_snap/L_node` (Schwinger from substrate constants). No empirical content beyond the definitions of V_yield and the Schwinger field. |
| `δn_AVE/δn_QED = 1/(4 a_EH α³)` | **emergence-adjacent / discriminator** | The *ratio* is AVE-distinct: it asserts the vacuum nonlinearity is un-suppressed (O(1) coefficient, tree-level saturation) where QED is loop-suppressed (α²). This is a genuine forward prediction that differs from QED by `~10⁶`. It is NOT a consistency-class reproduction of a known number — QED predicts a *different* answer. |

**Headline-class verdict (per `ave-evidence-framing-discipline`):** the coefficient ratio is a **discriminating forward prediction**, two-sided (below). The AVE δn itself is an Ax-4 *manifestation*, not an emergence-class derivation of a CODATA target (it predicts an as-yet-unmeasured observable). Do NOT headline this as "α emerges" or similar — α enters as an *input* (the QED loop factor and the substrate-field identity both carry α); what emerges is the *un-suppressed-vs-suppressed* contrast.

---

## §4 — The falsifier (two-sided, `ave-evidence-framing-discipline`)

**Pre-registered discriminator (FIELD-specified, no per-node conflation).** The test specifies a transverse optical/DC FIELD `E` directly, so `A = E/E_yield` with no gap-voltage division (this is the structural difference from the IVIM / Q-G42 per-node-conflation failures: those read an apparatus voltage as a per-node voltage; here the field IS the per-node-equivalent input). High-finesse-cavity or high-intensity-laser interferometry measures the index-shift coefficient.

- **AVE-confirming:** measured `δn ≈ −¼(E/E_yield)²` (O(1) coefficient, `~10⁶×` the QED Euler-Heisenberg baseline at the same field). At `E ~ 10¹⁴ V/m`, `δn_AVE ≈ 2.0×10⁻⁷` — within high-finesse-cavity reach.
- **AVE-falsifying:** a measured coefficient of QED size, `δn ~ a_EH α²(E/E_crit)²` (`~10⁶×` smaller than the AVE prediction at the same field). **A QED-sized coefficient falsifies AVE.**
- **QED-falsifying (at this observable):** an AVE-sized coefficient falsifies QED's loop-suppressed weak-field prediction at this observable.

**What does NOT falsify AVE (the corrected non-claim):** an `E²` *slope*. Both AVE and QED are E²-leading; the leading exponent carries no discriminating power. The prior shipped framing "if the slope remains E², AVE is falsified" (vol_9 `:143`/`:239`) was a √ε exponent conflation — killed in Part A.

**Adjudication criterion (frozen now, per Rule 11 — no post-hoc drift):** the discriminator is the *measured coefficient ratio* against the QED Euler-Heisenberg baseline, evaluated at whatever field the facility reaches. ✅ = ratio within ~1 OOM of `1/(4 a_EH α³)` (AVE-consistent). ❌ = ratio within ~1 OOM of 1 (QED-sized → AVE-falsified). The `~10⁶` separation gives ~6 OOM of margin, so sub-decade field-uncertainty or prefactor-convention spread (~1 OOM, §5.2) does NOT blur the verdict.

---

## §5 — The QED Euler-Heisenberg input (the only non-AVE number)

### 5.1 What it is

The QED weak-field vacuum birefringence comes from the Euler-Heisenberg effective Lagrangian (1936). For a static transverse field the two polarization indices shift as `δn = a_EH α²(E/E_crit)²` with O(1) mode-dependent prefactors. The standard single-mode weak-field values (e.g. as quoted for PVLAS/BMV magnetic-birefringence experiments, translated to an electric field):
- parallel mode: `n_∥ − 1 = (7/45) α²(E/E_crit)²` → `a_EH = 7/45 ≈ 0.156`
- perpendicular mode: `n_⊥ − 1 = (4/45) α²(E/E_crit)²` → `a_EH = 4/45 ≈ 0.089`
- differential birefringence: `n_∥ − n_⊥ = (3/45) α²(E/E_crit)² = (1/15) α²...` → `a_EH = 1/15 ≈ 0.067`

This is a **non-AVE literature input**, cited as such — it is NOT in `ave.core.constants` and the driver does NOT derive it (per `ave-driver-script-honesty`: forward AVE prediction, QED baseline from literature, no fit).

### 5.2 ⚑ FLAG-DON'T-FIX — the prefactor-convention spread (surfaced, not collapsed)

The ledger §5 post-merge resolution and this dispatch brief both quote the headline as **"~4.4×10⁵×"** with worked numbers **"δn_QED ≈ 4.5×10⁻¹³ at E = 10¹⁴ V/m"**. My independent reproduction with the canonical *single-mode* EH prefactor `a_EH = 7/45` gives `δn_QED ≈ 4.7×10⁻¹⁴` and ratio `≈ 4.1×10⁶` — i.e. the ledger's `δn_QED` is **~10× larger** (and its ratio ~10× smaller) than the textbook single-mode value. The ledger's numbers correspond to an effective `a_EH ≈ 1.5` (an order-of-magnitude / mode-summed EH coefficient), not the single-mode `7/45`.

**I am NOT silently picking one.** Per flag-don't-fix, both are surfaced:
- structural form `1/(4 a_EH α³)` is **exact and convention-independent**;
- the headline number spans `~3×10⁵` (`a_EH ~ 2`) → `~6.4×10⁵` (prefactor-1) → `~4.1×10⁶` (single-mode `7/45`) → `~9.7×10⁶` (differential);
- the ledger's "4.4×10⁵" sits at the `a_EH ~ 1.5` end (order-of-magnitude EH coefficient).

**Decision needed from Grant/auditor:** which EH prefactor convention the corpus headline should pin. The *physics verdict is unchanged either way* — AVE is `~10⁵–10⁶×` QED, a `~6` OOM gap, AVE-distinct at all fields. The driver reports the **full band** (all four `a_EH` values) so the corpus headline can be pinned without re-running. The reframed leaves (Part A) state "`~10⁶`" (robust across the band) rather than a single over-precise figure — this is the `ave-evidence-framing-discipline`-correct framing until the convention is pinned.

---

## §6 — Driver gate (`ave-driver-script-honesty`)

The forward driver `src/scripts/vol_4_engineering/birefringence_coefficient_discriminator.py` MUST:
1. Import `V_YIELD, L_NODE, ALPHA, E_CRIT, E_YIELD, V_SNAP` from `ave.core.constants` — **NO hard-coded substrate constants.**
2. Compute the AVE index shift from the full kernel `δn = (1−A²)^{1/4} − 1` (not just the leading term), plus the leading-term cross-check.
3. Take the QED Euler-Heisenberg prefactor `a_EH` as an **explicit literature input** (a labeled module-level dict of the four conventional values), cited in-comment as non-AVE — NOT derived, NOT fit.
4. Report: (a) the substrate identity `(E_crit/E_yield)² = 1/α` numerically (the structural collapse); (b) `δn_AVE`, `δn_QED`, and the ratio at a field sweep (10¹³ → 3×10¹⁶ V/m); (c) the field-INDEPENDENCE of the ratio (assert it is constant across the sweep to the leading-term approximation); (d) the full prefactor band per §5.2; (e) the measurability verdict (δn_AVE vs a stated high-finesse-cavity floor `~10⁻¹⁵` and laser-facility-reachable fields).
5. **NO fit, NO free parameter, NO tuning** — forward only. The output is a prediction the corpus stands behind, plus a literature comparator.

**Expected (pre-registered) driver output:** `(E_crit/E_yield)² = 137.04 = 1/α` ✓; ratio constant `= 1/(4 a_EH α³)` across the sweep; band `[~3×10⁵, ~9.7×10⁶]`; δn_AVE at 10¹⁴ V/m `≈ 2.0×10⁻⁷` (above a `~10⁻¹⁵` cavity floor → **MEASURABLE**).

---

## §7 — Deliverables (each its own commit, this branch)

1. ✅ Part A — √ε determinate fix, 5 sites (commit `ad26d357`).
2. This prereg.
3. The forward driver (gate §6).
4. The result doc (`research/2026-06-04_birefringence-coefficient-result.md`, small sections).
5. The clm-pp3qwf + leaf reframe — already landed in Part A (the leaves now state the coefficient discriminator); this prereg + result are the derivation record they cite.

`make verify-kb-metadata` before done. Branch-check before every commit. Two-sided framing throughout. PURE-AVE-CORPUS.

