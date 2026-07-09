# FROZEN PREREG — Electron g-factor from the (2,3) c-speed self-orbit (analytic + sympy)

**Arc:** electron-as-chiral-self-orbit (Grant-walked 2026-07-08). First test of the push.
**Lane:** research / analytic + symbolic derivation (bounded). HOLD canonization. NO self-merge — push + report.
**Branch:** `analysis/electron-g2-selforbit` (off `origin/main` @ `0341caba`, post PR #582).
**Prereg status:** FROZEN at first commit. Claim + discriminator + firewall + verdict-routing do not move post-freeze.
**Companion result doc (gated):** `research/2026-07-08_electron-g2-selforbit_result.md` (written AFTER this freezes, after the script runs).
**Companion script (gated):** `src/scripts/vol_2_particle_physics/electron_g2_selforbit.py` (sympy symbolic g + numeric + firewall AST-check + naive control).

**Disciplines applied (declared up front):**
`substrate-native-check` (walk §0) · `pre-test-physics-check` (ontology gut-check, question surfaced §1.4) · `phase-space-coordinate-check` (§0 CP4 — the (2,3) is a phase-space winding; μ,S are real-space) · `consistency-vs-emergence` (bin §5) · `verify-before-cite` (every file:line re-verified against `origin/main` @ `0341caba` this session) · `flag-don't-fix` (§6 surfaces a corpus direction-of-the-2 ambiguity, does NOT resolve it) · `ave-canonical-source` (constants imported; MUST cancel in g — firewall §4) · `ave-prereg`.

---

## 0. SUBSTRATE-NATIVE WALK (before any numerical code)

Per `substrate-native-check`. SM/QED defaults that would leak in if unwalked: a Dirac-spinor postulate that hands g=2 for free; a point-charge with a hand-set zitterbewegung radius ƛ_C/2 and frequency 2ω_C; a Lagrangian/energy-basin electron. Walked out below.

- **CP1/CP2 — sector.** Two DIFFERENT substrate objects carry the two inputs to g, and they must not be cross-wired (sector-ownership discipline, `master-equation.md:20`; [[feedback_sector_ownership_a1_t2_crosswiring]]):
  - **μ (magnetic moment)** rides the **CHARGE** = the T2 Cosserat **(2,3) winding** (`electron-identification.md:61`, Ax2 TKI [Q]≡[L]; the integer topological winding of the 0₁ flux loop). μ is a current×area of the charge circulation.
  - **S (spin angular momentum)** rides the **MASS** = the **A1 dilatation** (the 0₁ unknot body, `master-equation.md:20`). S = ∫ r×p over the mass circulation.
  - These are the "two homonymous 3s": A1 dilatation-MASS ⊥ Cosserat (2,3) WINDING-charge. NEVER cross-wire.
- **CP3 — AVE-native objective.** g is defined mechanically: g ≡ 2m·μ/(q·S), the ratio of the charge-circulation magnetic moment to the mass-circulation angular momentum. NOT read off a Dirac equation, NOT an energy minimization.
- **CP4 — phase-space vs real-space (`phase-space-coordinate-check`).** The (2,3) is the **phase-space** (Clifford-torus, T²⊂S³⊂ℂ²) winding label (`ch8-alpha-golden-torus.md:31`, `electron-identification.md` clm-uatcql): "2 windings on the d-axis, 3 windings on the q-axis" in (V_inc, V_ref). The real-space body is the **0₁ unknot** at loop radius ƛ_C = ℓ_node. μ and S are **real-space** quantities. The bridge the test must make explicit: the phase-space poloidal winding number (the "2" of the (2,3) d-axis) sets how many charge-circulations occur per single real-space mass loop — a phase-space→real-space rate map, flagged as the load-bearing modeling identification (§6).
- **CP-regime.** MODE = bound self-trapped soliton (electron), REGIME = Ax4-saturated (Γ=−1 TIR cavity), PHASE-STATE = DC persistent chiral circulation at the c-ceiling (ω_C·ƛ_C = c). A g measured on a cold/linear cage would be a wrong-regime artifact.

**Walk verdict:** g lives in the ratio of a real-space charge-current-loop (T2/(2,3)) to a real-space mass angular-momentum (A1), with the (2,3) phase-space winding number entering only as the charge-vs-mass circulation-rate (cover-degree) map. No Dirac postulate; no hand-set ƛ_C/2 or 2ω_C.

---

## 1. THE CLAIM (one paragraph) + THE ONTOLOGY FORK

**Claim under test.** The electron is a DC persistent chiral circulation at c: charge = the (2,3) T2 winding, mass = the A1 dilatation, both circulating at radius ƛ_C = ℓ_node at speed c (ω_C·ƛ_C = c). Computing g = 2m·μ/(q·S) from the ACTUAL (2,3)+A1 geometry — μ from the charge/(2,3) current circulation, S from the mass/A1 circulation — the physical constants (m_e, e, ħ, c, ƛ_C) MUST cancel algebraically, leaving g as a pure dimensionless GEOMETRIC number. **Hypothesis: the (2,3)/A1 relative geometry FORCES g=2**, and the factor of 2 is a NAMED geometric feature (the (2,3) poloidal double-wrap / K4 bipartite 2-sublattice double-cover / spin-½ 4π), NOT hand-inserted.

### 1.1 The three candidate homes for the factor of 2 (fork, resolved by the computation)
- **(A)** The **"2" of the (2,3) winding** (poloidal / d-axis double-wrap): the charge circulates twice per single mass loop.
- **(B)** The **K4 bipartite double-cover** (2 sublattices → 4π → spin-½ → S carries ħ/2 not ħ; canonical `l3-electron-soliton-synthesis.md:103-105`, `theorem-3-1-q-factor.md:78`, `finkelstein-misner-spin-half-derivation.md` clm-salw2h).
- **(C)** The **c-speed / Virial** constraint.
Corpus states (A)=(B) are "the same geometric content viewed at two abstraction layers, NOT two independent factors" (`ch8-alpha-golden-torus.md:73`, `l3:103-105`). The test names which of (A)/(B)/(C) does the work in the μ/S ratio.

### 1.4 pre-test-physics-check — plumber-physical question surfaced to Grant (at dispatch)
*Does the charge-current circulation rate equal the (2,3) POLOIDAL (d-axis, "2") winding rate, while the A1 mass tracks the single real-space backbone loop ("1")?* This assignment is the load-bearing identification: if charge rides the "2" and mass rides the "1", g=2; if both ride the same loop, g=1 (naive). The corpus double-cover (B) supports charge-vs-mass = 2:1, but the ASSIGNMENT is a modeling choice, surfaced not silently made. (Recorded; not resolved by fiat — the computation reports g under the canonical assignment AND the naive controls.)

---

## 2. THE COMPUTATION (sympy, symbolic + numeric)

All quantities symbolic (e, m_e, c, ƛ_C, ħ as free SYMBOLS — NOT numeric constants — for the firewall). Numeric evaluation imports `ave.core.constants` ONLY at the final report line, and ONLY to confirm the pure-number g is invariant under substitution (an anti-firewall cross-check, not an input to g).

1. **Naive c-orbit control (single object, single cover).** Point charge e AND mass m_e co-circulating on ONE loop of radius ƛ_C at speed c.
   - S_naive = m_e·c·ƛ_C. μ_naive = ½·e·c·ƛ_C. g = 2m_e·μ/(e·S) → **predict g=1**.
2. **General (p,q) torus-knot co-circulation control.** Charge AND mass co-circulate on the SAME (p,q) torus knot (p toroidal, q poloidal) at speed c. Compute μ_z = (I/2)∮(x dy − y dx) and S_z = ∮(x v_y − y v_x) dm over the ACTUAL knot path. **Predict g=1 for ALL (p,q)** — i.e., winding topology ALONE does not lift g when charge and mass are the same circulating object (the p enclosed-area factor cancels against the p angular-momentum factor). This is the sharp negative control: it proves the (2,3) knot per se is insufficient; the SECTOR SPLIT must do the work.
3. **AVE electron (A1⊥T2 split).** μ = μ_B from the charge single-2π-current-loop (double-cover-immune: I=e/T, A=πƛ_C² regardless of cover). S = ħ/2 from the mass/A1 spin observable being a 4π double-cover spinor (spin-½). g = 2m_e·μ/(e·S). Report symbolic g and the named source of the ×2.
4. **Cover-degree generalization.** Parameterize S = S_naive/N_cover, μ = μ_naive. Show g = N_cover EXACTLY (m_e, e, c, ƛ_C, ħ all cancel). N_cover=1 (single cover) → g=1; N_cover=2 (double cover, the (2,3) "2") → g=2. This makes "WHERE the factor comes from" a single symbol: g = N_cover.

---

## 3. DISCRIMINATOR (g=2 vs g=1) — pre-registered

| Path | Prediction | Reads |
|---|---|---|
| Naive c-orbit (single cover) | **g = 1** | control — the geometry does NOT lift it |
| (p,q) co-circulation, any p,q | **g = 1** | winding-topology-alone insufficient (sharp negative control) |
| A1⊥T2 split, N_cover=2 | **g = 2** | the double-cover / (2,3) poloidal "2" lifts it |
| A1⊥T2 split, N_cover=3 (wrong assignment: charge rides the "3") | g = 3 | falsifies the identification; would be reported plainly |

**The test has teeth:** g=1 is the generic classical answer (naive AND full (p,q) co-circulation both give it); g=2 requires the specific charge(single-cover)/mass(double-cover) asymmetry that the (2,3)/A1 structure supplies.

---

## 4. ANTI-TAUTOLOGY / FIREWALL (pre-registered, machine-checked)

- **g is a FORM not a value.** AST-firewall the g-computation cell: assert NO `M_E`/`ALPHA`/`m_e`/`HBAR` numeric token from `ave.core.constants` reaches the symbolic g expression. The script parses the g-expression's free symbols and asserts they are the abstract SymPy symbols only; it then simplifies g and asserts every physical symbol (e, m_e, c, ƛ_C, ħ) CANCELS, leaving a pure Rational.
- **No hand-inserted zitter.** ƛ_C/2 radius and 2ω_C frequency are NOT inputs. The "2" enters ONLY as the integer cover degree N_cover of the spin observable (a topological winding number, dimensionless), never as a plugged physical scale.
- **Numeric cross-check is a CONFIRMATION not an input:** after g is derived as a pure Rational symbolically, substituting the CODATA constants must leave g unchanged (it is constant in them). If g changed under substitution → firewall DIRTY → FAIL.

---

## 5. VERDICT ROUTING (pre-registered — do not move post-freeze)

- **[G2-FORCED]** ⟺ g=2 (leading geometric order) AND the (2,3)/A1 split provides the lift (naive control g=1 AND (p,q) co-circulation g=1) AND firewall clean (constants cancel; no M_E/ALPHA on path). Content: a genuine substrate MECHANISM for g=2 (the charge/single-cover vs mass/double-cover asymmetry), peer-with-Dirac at VALUE level — the AVE result is the FORCED FORM, not a distinct value.
- **[G2-NOT-FORCED]** ⟺ g=1, OR the ×2 must be hand-inserted (not a named topological integer), OR firewall dirty. Report plainly: the self-orbit does not force g=2.
- **[G-OTHER]** ⟺ some other clean number (e.g. g=3 if the assignment routes charge to the "3") — report it as a different geometric prediction.

## 6. flag-don't-fix (surfaced, NOT resolved)
The corpus text at `l3-electron-soliton-synthesis.md:103-105` reads "observable frequency = 2 × medium frequency" AND "m_e (observable) = m_Cosserat (medium)/2" — the DIRECTION of the factor-of-2 (which circulation is the fast one) has an apparent internal tension when read against E∝ω. This is FLAGGED for Grant, not silently resolved. The g-computation is presented for BOTH the canonical assignment (charge=double-cover-fast → g=2) and the naive controls, so the verdict is robust to the direction-read: the SIZE of the factor (2) is fixed by the bipartite cover integer either way; only the physical narration of "which is fast" carries the ambiguity.

## 7. HONEST SCOPE (pre-committed)
g=2 is peer-with-Dirac AT THE VALUE LEVEL (Dirac's equation also gives 2; the classical zitterbewegung construction also gives 2). If [G2-FORCED] lands, the AVE-relevant result is g=2 as a FORCED FORM from the (2,3)+A1 double-cover geometry — a mechanism for WHY g=2 — NOT an AVE-distinct value. Do NOT headline g=2 as an emergence-class distinct-value chord.
