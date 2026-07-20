# RESULT — J(ω) derivation: the z=3 bath spectral density as the yield-fork adjudicator (+ arccos drag-onset)

> **SECTOR HEADER (read first).**
> - **MODE:** derivation + 0D research-driver (explicit-bath GLE, ODE-level). Object = the z=3 srs bath spectral density `J(ω)` for the transverse-bow `S`, and the per-cycle energy ledger at the near-yield crossing. NOT a minimization, NOT continuum-Helmholtz. **Engine byte-UNTOUCHED.**
> - **REGIME / PHASE-STATE:** near-yield crossing, Regime II→III (`k4_tlm.py:308–311`), driven `ωτ≈0.9`; the *bath* is the cold-linear z=3 srs net.
> - **SECTOR:** load `A` = axial A1 dilatation (V-sector); response `S` = transverse **T2** bow. A1 ⊥ T2.
> - **DISCIPLINE:** frozen-then-run (prereg pushed before code, `research/2026-07-20_jomega-derivation_prereg_FROZEN.md`, base HEAD `64f1894d`). Rule-11 (frozen tree governs). Rule-12. Anti-seduction fence BOTH directions. Verify-before-cite. Flag-don't-fix.

**Date:** 2026-07-20 · **Lane:** implementer, J(ω) derivation (yield-fork adjudicator) · **Branch:** `research/jomega-derivation` · **Driver:** `src/scripts/vol_4_engineering/jomega_yield_fork.py` · **Test:** `src/tests/test_jomega_yield_fork.py` (7/7, `engine_sim`).

---

## 0. VERDICT (the frozen tree's output)

The frozen decision tree (prereg §4) lands in bin **(iii) DEGENERATE / UNDETERMINED — but with strong derived structure that reshapes the fork**. It does NOT land cleanly in world (a) or world (b), and that is the honest, anti-seduction result. Precisely:

1. **[DERIVED] World (c) — an axiom-level resistor / rate-independent plastic loss — is DEFINITIVELY EXCLUDED.** The H-ledger shows a lossless (`γ=0`) second-order `S` gives a **FINITE reactive loop** `∮S dr = 0.183` with **EXACTLY zero dissipated work** `W_diss = 0.0`. A finite pinched loop does not require, or imply, a resistor. Every damping-like term is `γ`-transduction that vanishes as the coupling → 0. **This is robust** (coupling-model- and scope-independent) and is the strongest result of this lane.

2. **[DERIVED] The (a)/(b) crossing distinction is NOT a clean XOR — it is a SCOPE + COUPLING-MODEL split** (bins (c-scope) AND (c-magnitude) both fire):
   - **(c-magnitude):** the crossing *shape* verdict hinges on the one unforced modeling choice (S→bath coupling): on-site coupling → **Ohmic** `J`, `J_norm(0.9ω_C)=0.31 ≥ 0.1` → world-(b) channel LIVE; strain coupling → **super-Ohmic** `J`, `J_norm(0.9ω_C)=0.036 < 0.1` → world-(a) suppression. UNDETERMINED between them; the coupling choice is surfaced, not silently picked.
   - **(c-scope):** the GLE ring-down ledger SCOPE-SPLITS — the **0D few-mode cell** (the actual scope of a single node's yield crossing) **recovers 70–95 % of `E_S`** (world-(a) reactive return, Poincaré recurrence); the **dense/∞-lattice bath drains to 0–10 %** (world-(b) transduction). Both are Ax3-lossless microscopically.

3. **[DERIVED] Grant's reversible-reactive lean is SUPPORTED — at the 0D-cell scope and at the microscopic (Ax3-lossless) level — but NOT as a strict "world (a) wins at the crossing" claim.** World (b) is the correct *coarse-grained ∞-lattice* description; its "loss" is Op3 mode-transduction (RULING-21), never a resistor. **Anti-seduction fence held:** world (a) does not "win"; world (b) does not "win"; world (c) LOSES; the fork was ill-posed as an XOR because it conflated scope.

4. **[DERIVED] The §4.3/§5.3 inconsistency of the flag-F doc is resolved** (§3 below): `πJ(ω→0)` (Markovian friction constant, slow-limit) and `πJ(ω_drive)` (finite-drive per-cycle transfer) are **different physical objects** (frequency-dependent friction), both legitimate, evaluated at different arguments.

5. **[DERIVED] The load-bearing band-edge correction:** the corpus-adjudicated arccos band top is `π√3·ω_C ≈ 5.44 ω_C`, **NOT the flag-F doc's assumed `ω_C`** — so the crossing (`ωτ≈0.9`) sits at ≈16 % of the band, **deep inside**, where `J(ω_drive) > 0`. This is why the fork is genuinely live (a hybrid), consistent with the flag-F re-bank (F1/F11).

6. **[DERIVED] Loss-location adjudication (§7):** Site 1 (vol_4 ch01:358, "max loss at `f≪1/τ`") is **the world-(c) picture — EXCLUDED**; Site 2 (backmatter:147, "zero-area elastic at `f≪1/τ`") is **CORRECT** there; Site 3 (`#735` Debye peak at `ωτ≈0.9`) is **CORRECT** for the loss peak. Flagged (not fixed) with verbatim citations.

7. **[DERIVED] Batched arccos drag-onset (§9):** `v_p,min/c₀ = 0.80` (srs 3D acoustic) and **exactly `1.0` (1D-chain arccos, dispersionless)** — the cosine-branch `2/π ≈ 0.637` **does NOT survive** the model switch.

**Flag F status:** **PARTIALLY discharged, advanced past OPEN-XOR.** World (c) excluded (new, robust); the (a)/(b) crux is now named as a scope+coupling distinction, not a dichotomy; the fork RULING stays Grant's. `I_S` kinetic-term provenance stays OPEN (§8; scope not stretched). **AWAITING GRANT RATIFICATION.**

---

## 1. The load-bearing band-edge correction (the pivot)

The flag-F doc §4.2 assumed the z=3 bath band edge is `ω_max ~ c/ℓ_node = 1/τ_relax = ω_C` (so `ωτ_max = 1`) and built its CRITICAL band-edge step (F1/F11) on it. The **corpus-ADJUDICATED** band model (`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md`, `clm-bnd5rq`, gates PASS #604/#607) is the **arccos transmission-line map**:

```
ω_n(k) = ω_link · arccos(μ_n(k)/3),   ω_link = √3·ω_C,   band top = π·ω_link = π√3·ω_C ≈ 5.4414 ω_C  (at H).
```
**[ENGINE-READ / CANONICAL]** In `ωτ_relax` coordinates the bath band spans `[0, 5.44]`. The crossing at `ωτ ≈ 0.9` is at **16.5 % of the band top — deep INSIDE**, not near the edge. `J(ω_drive)` at the crossing is therefore **not band-edge-suppressed**; whether it is *appreciable* is a DOS/coupling question (§2). This corrects the flag-F doc's factor-≈5.4 underestimate.

---

## 2. The J(ω) derivation

**Density of states `g(ω)`** [DERIVED, dense BZ histogram of the arccos band, driver `density_of_states`]: `g(ω) ∝ ω^{1.844}` at low ω — the **3D acoustic Debye** form `g ∝ ω²` (the arccos acoustic branch is linear near Γ, velocity factor `1/√3`; in 3D that gives `g∝ω²`). Band-top van Hove structure; `g` cuts off at `5.44 ω_C`.

**Coupling model — the one unforced choice, both run** (prereg §3, driver `build_J`). `S` modulates `Z_eff = Z_0/√S` (Op14, `k4_tlm.py:315,318,362`), so the bond reflection `Γ_bond=(Z_B−Z_A)/(Z_B+Z_A)` (`k4_tlm.py:440`) couples `S` to the bond waves [ENGINE-READ]. Whether the linearized S→mode coupling is on-site or strain/gradient is **not fixed by the constitutive form alone**:

| model | `c(ω)` | `J(ω) = (π/2)g·c²/(m ω)` | low-ω exponent `s` (measured) | `J_norm(0.9 ω_C)` | class |
|---|---|---|---|---|---|
| **C1 on-site** | const | `∝ g/ω ∝ ω` | **0.844 (Ohmic, s≈1)** | **0.311** (appreciable) | world-(b) channel LIVE |
| **C2 strain** | `∝ω` | `∝ g·ω ∝ ω³` | **2.844 (super-Ohmic, s≈3)** | **0.036** (suppressed) | world-(a) shape |

**[DERIVED]** Both give `J(ω→0)=0` (elastic at DC), a peak at intermediate `ω` (`2.12 ω_C` C1 / `3.33 ω_C` C2), and `J=0` above the band edge. The **crossing shape verdict SPLITS on the coupling model** — the frozen `(c-magnitude)` UNDETERMINED bin, choice surfaced. The S-bow is an *internal transverse deformation* (buckling response), not a rigid translation, so on-site coupling (C1) is not forbidden by translation invariance; both remain physical candidates. **Deriving the absolute `c(ω)` scale (and hence the model) from the full engine constitutive tensor is the owed extension** (§11).

---

## 3. The two Γ objects — the §4.3/§5.3 inconsistency resolved

For the bilinear bath (`H_int = −S·Σ c_j q_j`), the friction is **frequency-dependent**. Two distinct objects, both legitimately `πJ(·)`:

- **Markovian friction CONSTANT** (§4.3's `πJ(ω→0)`): `γ_0 ≡ lim_{ω→0} J(ω)/ω`. The DC friction that would drive the overdamped first-order Eq 2.1. **[DERIVED]** C1 (Ohmic): `J/ω → const` (`γ_0` finite; measured `J/ω` low-ω slope `−0.28 ≈ 0`) ⇒ **Eq 2.1 recoverable in the slow limit** (`ωτ≪1`) with a finite `γ_0`. C2 (super-Ohmic): `J/ω ∝ ω^{1.7} → 0` (`γ_0 = 0`) ⇒ **no DC friction; Eq 2.1 NOT recoverable** as a friction-relaxation (the flag-F R-6 super-Ohmic branch — it *strengthens* world (a) at low frequency).

- **Per-cycle transduction at finite drive** (§5.3's `πJ(ω_drive)`): the energy dissipated into resonant bath modes per cycle at `ω_d` is `ΔE_cycle = π S_0² J(ω_d)`. It requires REAL bath modes at `ω_d`; `J(ω_d)` counts them. **[DERIVED]** Finite in BOTH models at the crossing (`0.31` C1 / `0.036` C2 of peak).

**Resolution:** these are a DC-limit constant vs a finite-frequency per-cycle transfer — different objects because the friction is dispersive. The flag-F doc's error was treating them as one `Γ`. **The crossing verdict uses `J(ω_drive)`; the Eq-2.1-recoverability uses `J(ω→0)`. State both; do not equate.**

---

## 4. The per-cycle GLE energy ledger at the crossing (the thing #744 said was never shown)

Explicit-bath realization (prereg §4-iv): `S` + `N` bath oscillators sampled from the srs arccos DOS, coupled bilinearly with counter-term, symplectic (velocity-Verlet) integration — energy-exactly-closed, mode-resolved. Driven `r(t)=0.7+0.3 sin(ω_d t)`, `ω_d=0.9`, `S_eq` byte-locked to `k4_tlm.py:283`.

**Driven ledger** [DERIVED, `gle_ledger`]: `E_bath(t)` return-ratio (tail-min/peak; `~1`=drain, `«1`=recurrence): finite `N=60` returns to `0.27–0.35`; dense `N=1200` stays `0.50–0.58`. The trend is right but continuous driving muddies it — so the **clean discriminator is the undriven ring-down**:

**Ring-down ledger** [DERIVED, `gle_ringdown`, fixed physical window, coupling-scale-robust]: displace `S`, let it ring, watch the fraction of `E_S` recovered after the initial decay:

| model | 0D few-mode bath (`N=40`) | dense / ∞-lattice bath (`N=1500`) |
|---|---|---|
| C1 on-site | recovery **0.698** (world-a return) | recovery **0.000** (world-b drain) |
| C2 strain | recovery **0.948** (world-a return) | recovery **0.101** (world-b drain) |

**[DERIVED] The SCOPE-SPLIT is unambiguous:** the 0D single-cell bath (few `z=3` neighbour modes) **recurs — the energy returns to `S`** (Poincaré-bounded, world-(a) reactive); the ∞-lattice continuum bath **drains — the energy is carried off and does NOT return within the window** (world-(b) transduction). This is exactly the flag-F §6 "0D recurs / ∞-lattice radiates" ledger, now COMPUTED. Both are Ax3-lossless microscopically (the drain is Op3 mode-transduction to the radiation boundary, not a bulk resistor). Robust to coupling model and coupling scale.

---

## 5. First-order Eq 2.1 vs second-order reactive contrast + H-ledger (closes #735 C-3)

`#735` PROTOCOL-COMPLETION §8 / F-B3 SPEC'd but never ran the second-order reactive contrast. Run here on the identical drive [DERIVED, `first_order_loop` / `second_order_loop`]:

- **Loop-area peaks do NOT discriminate.** First-order Eq 2.1: `(r,S)` peak `ωτ=1.049`, `(V,I)` peak `ωτ=0.937` (reproduces `#735`'s `0.911` (V,I) / `~1.00` (r,S)). Second-order reactive: peaks also near `ωτ≈0.94–1.05`. **Both produce finite loops near `ωτ~1`** — the loop area alone cannot tell them apart (confirms `#735` F-B3).

- **★ The H-ledger IS the discriminator** [DERIVED, `second_order_loop` W_diss]:

  | `γ` | `∮S dr` (loop area) | `W_diss` per cycle |
  |---|---|---|
  | **0.0** | **0.183 (FINITE)** | **0.0 (EXACTLY ZERO)** |
  | 0.05 | 0.390 | 0.518 |
  | 0.2 | 0.903 | 1.152 |
  | 0.5 | 0.654 | 0.838 |

  **A lossless (`γ=0`) second-order `S` has a finite reactive loop area and ZERO dissipation.** As `γ→0`, `W_diss→0` while `∮S dr` stays O(0.2–0.9). **The finite pinched loop is a reactive area, not a dissipated-work loop, unless an explicit `γ` (transduction coupling) is turned on.** This is the substrate-native content of Grant's lean and the direct refutation of the "finite `∮` ⇒ resistor" identity (world-(c) reading). *(Note: the `γ=0` case is not a clean steady state — the undamped transient at `ω_S=1` persists and beats against `ω_d=0.9` — but `W_diss=0` is exact regardless, since there is no dissipation term; the `γ→0` limit of the damped runs shows `W_diss→0` continuously.)*

---

## 6. Adjudication per the frozen tree

- **World (c)** (axiom resistor / rate-independent plastic): **EXCLUDED [DERIVED]** (§5 H-ledger; robust).
- **World (a) vs (b) at the crossing:** **UNDETERMINED as an XOR [DERIVED]** — bins (c-magnitude) (coupling-model split, §2) AND (c-scope) (0D-reactive vs ∞-lattice-transductive, §4) both fire. The distinction is a **scope + coupling question**, not a dichotomy. Grant's lean SUPPORTED at 0D-cell scope + microscopically; world (b) is the coarse-grained ∞-lattice description.
- **Consequence for the yield fork:** the fork's original framing ("finite-area memristive loop *vs* zero-area saturating reactance") is a FALSE DICHOTOMY at the crossing — the true object is a **finite-area REACTIVE loop that transduces (not dissipates) in the ∞-lattice and recurs (reactive) in the 0D cell**, Ax3-lossless throughout. The "memristance in Ω / energy dissipated per yield-heal cycle" reading (world c) is dead.

---

## 7. Loss-location adjudication (the three-way contradiction — FLAGGED, not fixed)

Per-cycle loss (the memristive loop-area / dissipated-energy observable) `∝` the S-response Debye/reactive lag `×` `J(ω_d)`. Both factors → 0 as `ω_d→0` (quasi-static reversible; `J(0)=0`, measured `J_norm(0.05ω_C)=0.017` C1 / `0.0` C2) and as `ω_d→∞` (frozen; `J=0` above band edge). The loss **peaks near `ωτ~1`** (the relaxation/response rate), NOT at `f≪1/τ`.

| Site | verbatim (grep-verified at HEAD) | J(ω) verdict |
|---|---|---|
| **Site 1** — `vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:358` | *"At `f ≪ 1/τ_relax`, complete yield and recovery occur within each cycle, producing **maximum hysteresis loss**."* | **WRONG — the world-(c) rate-independent-plastic picture; EXCLUDED.** Under Ax3-lossless z=3 transduction, `J(f≪1/τ)→0` ⇒ loss is **MINIMAL (elastic)** at low f, not maximal. Already fork-open-caveated at `:338–339`. |
| **Site 2** — `backmatter/06_spice_verification_manual.tex:147–148` | *"At any practical SPICE simulation frequency (`f ≪ 7.8×10²⁰ Hz`), the lattice responds purely elastically---the hysteresis loop has **zero enclosed area**."* | **CORRECT in the `f≪1/τ` regime** — `J(0)=0` ⇒ reversible, zero loop. |
| **Site 3** — `#735` Leg B (`research/2026-07-19_yield-fork-discriminators_result.md:19,81`) | (V,I) loop-area **peaks at `ωτ=0.911`, INSIDE `[0.85,0.95]`** | **CORRECT for the loss peak** — the loop-area observable peaks near `ωτ~1` (reproduced here: (V,I) peak `0.937`). |

**Robust conclusion (coupling-model-independent):** loss is **zero at `f≪1/τ`** (Site 2 ✓, Site 1 ✗) and **peaks near `ωτ~1`** (Site 3 ✓). The three-way contradiction resolves as: **Site 1 is the excluded world-(c) branch; Sites 2 and 3 are the two true limits of the same Ax3-lossless reactive/transductive loop.** *(Flagged per flag-don't-fix; no `.tex` edited — the auditor lane owns the manuscript relabel; owed pointer in §11.)*

---

## 8. Memristor phenomenology status + the I_S caveat

- **Memristor phenomenology:** the pinched hysteresis loop is REAL (both first- and second-order produce it, near `ωτ~1`), but it is a **saturable-reactance / parametric-varactor** object with mode-transduction, **not an RC/memristor-with-resistance**. The `M` (Ω) / "energy dissipated per thixotropic yield–heal cycle → heat" reading (`01_vacuum_circuit_analysis.tex:356`) is the **world-(c) branch, EXCLUDED**. The finite loop area is confirmed but does NOT license a resistor (§5).
- **I_S kinetic-term provenance (flag-F R-5) — stays OPEN; scope NOT stretched.** The GLE assumes a bare inertia `m_S ≡ I_S` for `S`. The bath contributes a *reactive added-mass renormalization* (the ω→0 real part of the bath response dresses `m_S` upward), so the *dressed* inertia is bath-supported even if the bare term were small — but the **bare kinetic-term axiom provenance is not derived here** (consistent with flag-F §2.2 R-5: the transverse-shear-wave `c_shear=c√S` argument for `m_S>0` plausibly exists but is not made). Noted, not closed.

---

## 9. Batched task — arccos drag-onset ratio (does 2/π survive?)

Re-derived `v_p,min/c₀` on the corpus-ADJUDICATED arccos map, replacing the cosine-branch `2/π` of `#741` (`research/2026-07-19_deep-space-band-map_derivation.md` §3.3, §5-D4) [DERIVED, `drag_onset_srs` / `drag_onset_chain`]:

| band model | `v_p,min/c₀` | note |
|---|---|---|
| cosine chain (lumped, #741) | **`2/π = 0.6366`** | the value #741 carries (cosine-scoped) |
| **1D-chain arccos** (z=2) | **`1.0000` (EXACTLY)** | `arccos(cos kℓ)=kℓ` ⇒ **perfectly dispersionless**; NO drag onset below `c` |
| **srs 3D acoustic arccos** | **`0.8028`** | per-direction `[0.803, 0.803, 0.805, 0.809, 0.823, 0.882, 0.976]`; min along ⟨100⟩/⟨110⟩ |

**[DERIVED] The cosine-branch `2/π ≈ 0.637` does NOT survive the model switch.** On the substrate-native arccos map the acoustic branch is far more linear: the 1D chain is **exactly dispersionless** (`v_p ≡ c`, no vacuum-Cherenkov threshold below `c` at all), and the 3D srs acoustic branch gives `v_p,min/c₀ = 0.80` — an AVE-distinct, dimensionless, `ℓ_node`-free manifestation, but ≈26 % **higher** than the cosine `2/π`. **Consequence for `#741`:** its D4 discriminator value `2/π` is a cosine-branch artifact; the substrate-native arccos value is `0.80` (srs) / `1.0` (idealized chain). The deep-space NULL is unaffected (deep-space matter is `v~10⁻⁴c ≪` any of these AND bandlimited, `#741` §3.3), but the drag-onset *ratio itself* must be relabeled `0.80`, not `2/π`. **Owed KB-caveat-update pointer (fenced, §11).**

---

## 10. FORM / VALUE + consistency-vs-emergence ledger

| quantity | FORM | VALUE | class |
|---|---|---|---|
| `J(ω)` shape (Ohmic/super-Ohmic, band edge, peak) | **[DERIVED]** | — | **MANIFESTATION** (theorem of arccos band + coupling model) |
| band edge `π√3 ω_C`, `ω_C`, `τ_relax=1/ω_C` | [ENGINE-READ] | calibrated via `ℓ_node≡λ̄_C` | **CALIBRATION / consistency** (NOT headlined as emergent) |
| the two Γ objects (`γ_0`, `πJ(ω_d)`) | **[DERIVED]** | — | manifestation |
| GLE scope-split (0D recurs / ∞ drains) | **[DERIVED]** | coupling-scale-robust | manifestation |
| H-ledger (finite loop, `W_diss=0` at `γ=0`) | **[DERIVED]** | exact | manifestation |
| per-cycle transfer *magnitude* `ζ` | [DERIVED] shape | **[UNDETERMINED]** coupling scale | — |
| `v_p,min/c₀ = 0.80` (srs) / `1.0` (chain) | **[DERIVED]** | dimensionless, `ℓ_node`-free | **MANIFESTATION** |

No CODATA / `α` / `Q_TANK` on any verdict path; forward computation only.

---

## 11. Flags (flag-don't-fix) + owed follow-ons

**Flags surfaced (routed to Grant / auditor; not fixed here):**
- **FLAG-1 — loss-location three-way contradiction** (§7). Site 1 (vol_4 ch01:358) is the excluded world-(c) picture; Site 2 (backmatter:147) and Site 3 (#735) are the two true limits. **Surfaced with verbatim citations; no `.tex` edited.** Site 1 is already fork-open-caveated (`:338–339`), so this sharpens an open caveat rather than exposing a silent error.
- **FLAG-2 — the (a)/(b) fork is a false XOR.** The fork record (`retention-transition-split.md:61–65`, `2026-07-17` §5) frames it as "finite-area memristive loop *vs* zero-area saturating reactance." This lane derives that the true object is a **finite-area REACTIVE loop** (finite `∮`, zero `W_diss`) that transduces in the ∞-lattice and recurs in the 0D cell — so both fork branches are partially right and the XOR is the wrong question. **Routed to Grant** (the ruling stays his).
- **FLAG-3 — coupling-model UNDETERMINED.** The crossing shape verdict (Ohmic-b vs super-Ohmic-a) hinges on whether the S→bath coupling is on-site or strain (§2). Deriving it needs the full engine constitutive tensor — not attempted here (fail-closed).

**Owed follow-ons (FENCED — cleanup/auditor lanes own these trees; NOT executed here):**
1. **`#59` Flag F status update:** "PARTIALLY discharged, advanced past OPEN-XOR — world (c) excluded (H-ledger); the (a)/(b) crux is a scope+coupling distinction, not a dichotomy; awaiting Grant ratification." *Auditor lands.*
2. **Loss-location relabel** at `vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:358` (Site 1): the "maximum hysteresis loss at `f≪1/τ`" line is the excluded world-(c) reading; the Ax3-lossless bath gives **minimal (elastic) loss** there. *Auditor lands (the subsection is already Rule-12-caveated).*
3. **`#741` D4 relabel** (`research/2026-07-19_deep-space-band-map_derivation.md` §3.3, §5-D4, §6): the drag-onset ratio is **`0.80` (srs arccos) / `1.0` (chain arccos)**, NOT the cosine-branch `2/π ≈ 0.637`; `srs-band-structure.md` could gain a drag-onset row. *Auditor/cleanup lane; Grant-gated for any KB mint.*
4. **`tau-relax-derivation.md` / `#59` §10 staleness** (already flagged by `#735` §5): note that Eq 2.1's regime of validity is `ωτ≪1` AND requires `γ_0>0` (Ohmic coupling); under super-Ohmic coupling Eq 2.1 is not recoverable at all. *Owed KB follow-on.*

**None of items 1–4 executed here** (Rule-12 / lane fence).

---

*Derived 2026-07-20 by Opus 4.8 (implementer lane) per Grant's J(ω) yield-fork-adjudicator dispatch ("1. fire"). Frozen prereg governed (Rule-11); anti-seduction fence held both directions (world (a) did not win, world (b) did not win, world (c) lost); engine byte-untouched; verify-before-cite at base HEAD `64f1894d`; flag-don't-fix.*
