# RESULT — Coax-ring secondary route to α: the SCALE-FREE reactance-pair slosh is REAL (phasor-space), but the real-space b/a does NOT close (diverges at the α-free A→1 wall)

**Date:** 2026-06-10
**Branch:** `analysis/2026-06-10-coax-ring-secondary` (worktree off `analysis/2026-06-10-sonic-horizon-closure`). Not pushed/merged.
**Prereg (FROZEN, committed alone first):** [`2026-06-10_coax-ring-secondary_prereg.md`](2026-06-10_coax-ring-secondary_prereg.md) (commit `f14c1166`, before any run artifact).
**Licensed entry:** the §5 gate of the 2026-06-04 α-¼ closure — a discriminating secondary named BEFORE deriving (Grant 2026-06-10, verbatim in the prereg §0).
**Drivers:**
- [`src/scripts/vol_1_foundations/coax_ring_secondary.py`](../src/scripts/vol_1_foundations/coax_ring_secondary.py) — Arm 1 (forward coax) + Arm 2 (FBD re-closure with the A→1 BC). Data: `_output/coax_ring_secondary_results.json`.
- [`src/scripts/vol_1_foundations/coax_ring_scale_invariance.py`](../src/scripts/vol_1_foundations/coax_ring_scale_invariance.py) — Arm 3 (scale-invariance smoke, graft-v2 carrier). Data: `_output/coax_ring_scale_invariance_results.json`.
- [`src/scripts/vol_1_foundations/coax_ring_figures.py`](../src/scripts/vol_1_foundations/coax_ring_figures.py) — figures (data-derived captions).
- Re-used machinery: `electron_mfg_rr_balance.py` (the validated mfg-flow `G(ρ̄)` balance, Arm 2 RE-RUN); `crystal_graft_v2.py`/`crystal_engine.py` + `crystal_graft_v2_run.py::extract_2_3_omega` (the validated own-ω carrier + extractor, Arm 3).
**Figures:** `research/figures/coax_ring_fig{1,2,3}_*.png`.
**Governing discipline:** `ave-apparatus-floor-attribution`. Skills: substrate-native-check, ave-prereg, ave-canonical-source, ave-driver-script-honesty, ave-conserved-vs-pumped, ave-representation-capability-check, verify-before-cite, ave-live-fire-derivation-provenance, consistency-vs-emergence.

---

## 0. VERDICT — MIXED, cleanly localized (the discipline at full strength)

> **The discriminating secondary HOLDS in phasor/reactance coordinates and DIES in real-space radius coordinates — exactly along the corpus's standing coordinate firewall.**
>
> - **Arm 3 = SCALE-FREE.** The (2,3) carrier's own reactance pair (`ω ↔ π_ω`) sloshes with a scale-INVARIANT exchange fraction (`f_exch = 1.05 / 1.00 / 0.99` at r=4/6/8; spread **6.2%** < the worst ledger floor **23.7%**) WHILE the mode frequency scales DOWN with size toward the mass-gap floor (`ω_field = 1.093 → 1.074 → 1.052 → ω_0 = 1.0`). The planted (2,3) reads back at every scale (`is_2_3=True`, rel ≈ 0.73/0.63). Grant's *"how L and C change together in scale but not relative magnitude"* is **CONFIRMED for the winding carrier's reactance pair.**
> - **Arm 1 = RATIO-DERIVED but DIVERGENT.** `b/a` emerges α-FREE from the two floors (dead-input clean), BUT the exact α-free `A→1` wall makes it **DIVERGE** (`b/a → ∞`), and the regularized value **TRACKS the saturation clip `A_cap`** (5.2 → 9.7 → 17.4 → 30.9 → 55.1 as `A_cap`: 0.9→0.99999) — apparatus, not physics. The implied coax `Z/slosh` therefore does NOT reproduce α.
> - **Arm 2 = DIFFERENT.** The FBD radial balance with the α-free `A→1` outer BC gives a **divergent** `R/r` (and an `A_cap`-clip-tracking value, +329% vs 2.27 at `A_cap`=0.99) — NOT the real-space canon ≈2.27. Forcing 2.27 needs a NON-canonical `ρ̄_wall ≈ 0.304` (a FIT, not the A→1 derivation).

**The single mechanism (Rule 11):** the **real-space radius ratio** `b/a` cannot carry the closure because the α-free `A→1` (full-compression saturation) wall is **asymptotic** — the medium stiffens to `c²→∞` before reaching full compression, so the v=c₀ scale-free profile never reaches the outer wall at finite radius. The **scale-free invariant Grant predicted is real, but it lives in the reactance/phasor coordinates** (the `ω↔π_ω` slosh), **NOT in the real-space radius ratio.** This is precisely the corpus's coordinate firewall (`28_two_node_electron_synthesis.md` §4.2: real-space `R/r≈2.27` and phase-space `R/r=φ²` are *"DIFFERENT QUANTITIES … they needn't match"*) — reinforced here from a new direction.

**Per the frozen synthesis map (prereg §7): Arm-3 SCALE-FREE ∧ Arm-1 RATIO-DERIVED ⇒ the slosh lane EARNS its §5 license** — but the license is for the PHASOR-coordinate quantization derivation (where the scale-free invariant lives), NOT for the real-space b/a route (which is closed, divergent). Next-step note only, §5 below; **not run here.**

This is reported without debugging toward 2.27 or α (Rule 11). The b/a divergence was the pre-registered expectation (prereg §6) and it held.

---

## 1. ARM 1 — the forward coax derivation (RATIO-DERIVED, divergent)

**The two α-free loci (Block 1):**
- inner `a` = the cavitation locus, the EOS `c²=0` root **DERIVED in-script** (`ρ²−ρ−1=0`) = `−0.6180339887 = −1/φ` (exact identity; `c_eff²/c₀²` at the root = 0). `ρ̄_cav=−1/φ` kept **CANDIDATE-CLAIM** (Propulsion `04_superluminal_transit.tex:86,89`; zero KB/`constants.py` hits).
- outer `b` = the `A→1` rupture locus, `ρ̄_wall → +1` (`S=√(1−ρ̄²)→0`; regime boundary `R_III=1.0`, `constants.py:425`). **α-free.**

**The substrate-native coax log-ratio (Block 2/3).** Derived from the K4-TLM radial line, NOT imported: the radial balance `dP/dr = ρ v_θ²/r` with the barotropic EOS `c²=dP/dρ` and the v=c₀ scale-free closure gives `d(ln r) = [c_eff²/c₀² /(1+ρ̄)] dρ̄`, whose integral **IS** the coax log-factor `ln(b/a) = G(ρ̄_b) − G(ρ̄_a)`, `G(ρ̄) = −¼ln(1−ρ̄)+(5/4)ln(1+ρ̄)+½/(1+ρ̄)`. The local bulk impedance `Z_bulk=ρ·c_bulk` vanishes at `a` (c²=0) and diverges at `b` (c²→∞): both ends are `Γ=−1` mirrors ⇒ a closed radial cavity (consistent).

| outer wall | `b/a = R/r` | reading |
|---|---|---|
| exact `A→1` (`ρ̄=1`) | **+∞ (DIVERGES)** | `G(ρ̄→1) ~ −¼ln(1−ρ̄) → +∞` |
| `A_cap=0.9` | 5.24 | tracks clip |
| `A_cap=0.99` | 9.75 | tracks clip |
| `A_cap=0.999` | 17.41 | tracks clip |
| `A_cap=0.9999` | 30.98 | tracks clip |
| `A_cap=0.99999` | 55.09 | tracks clip |

Per `ave-apparatus-floor-attribution`: `b/a` **TRACKS the regularization knob `A_cap`** (monotone, unbounded) ⇒ APPARATUS, not a physical ratio. The implied coax impedance `Z_coax/Z₀ = ln(b/a)/2π → ∞` and the Op21 per-cycle slosh `f_slosh = 1/ln(b/a) → 0` at `A→1`; neither lands near `α⁻¹ = 4π³+π²+π = 137.036`.

**DEAD-INPUT test (Block 5 — circularity-free proof):**
- **(a) inner-floor sweep** `ρ̄_cav ∈ {−0.40,−0.50,−0.618,−0.70,−0.80}` → `b/a` MOVES (4.42 → … distinct values) ⇒ **physics, not tautology.** ✅
- **(b) α-sweep on the canonical A→1 BC** `α ×{0.01, 1, 100}` → `b/a` UNCHANGED (the BCs `ρ̄_cav` and `ρ̄_wall=1` carry NO α) ⇒ **CIRCULARITY-FREE.** ✅
- **(c) the REJECTED `√(2α)` onset BC** `α ×{0.5,1,2} → ρ̄_wall=√(2α)` → `b/a` MOVES with α ⇒ this is **exactly why √(2α) is rejected** as the outer BC (it smuggles α into the ratio meant to predict α). ✅

**Arm 1 BIN = RATIO-DERIVED** (α-free, fixed by the two floors) **— sub-record: the derived ratio DIVERGES and tracks `A_cap` (apparatus); the static coax profile does NOT yield a finite α-relevant slosh.**

---

## 2. ARM 2 — the FBD re-closure with the A→1 outer BC (DIFFERENT)

Re-ran the validated mfg-flow `G(ρ̄)` balance (`electron_mfg_rr_balance.py::rr_const_v`) — which left `R/r` **UNDERDETERMINED** because `ρ̄_wall` was free — now with the outer BC fixed at the **α-free `A→1` locus** (Grant's "local saturation," the input the mfg-flow doc left open).

- `R/r` at exact `A→1`: **+∞ (DIVERGES)**.
- Regularized: `R/r = 5.24 / 9.75 / 17.41 / 30.98 / 55.09` at `A_cap = 0.9 … 0.99999` (identical to Arm 1 — the coax framing and the FBD framing are the SAME annulus).
- **Comparison to the REAL-SPACE canon ≈2.27** (`28_..._synthesis.md` §5.3; **NOT** phase-space `φ²=2.618`): residual at `A_cap=0.99` = **+329%**; not within the frozen ±10% tol at any clip; diverges at the exact wall.
- **Fit-tell (ave-live-fire Step 4):** `R/r = 2.27` requires `ρ̄_wall ≈ 0.304` — NOT a canonical density and NOT the `A→1` rupture locus (`ρ̄=1`). Forcing 2.27 is **FITTED**, not the A→1 derivation. (Note: `0.304 ≈ (φ−1)/2` the Golden-Torus **phasor** minor semi-axis — but using a phasor semi-axis as a real-space density would be a coordinate mismatch + coincidence-magnet; NOT pursued, per the fence.)

**Arm 2 BIN = DIFFERENT** (the α-free A→1 outer BC gives a divergent / `A_cap`-clip-tracking `R/r`, not 2.27).

---

## 3. ARM 3 — the scale-invariance smoke (SCALE-FREE; the discriminating result)

Engine: `CrystalGraftV2` (the validated own-ω carrier). Observable (`ave-representation-capability-check` — named DOF pair): the (2,3) carrier's **own reactance pair** — `L-state = ½|π_ω|²` (ω-momentum kinetic), `C-state = ½(c_ω²|∇ω|² + ω_0²|ω|²)` (ω-field potential). This is the reactance-pair-tracking the empirical-driver discipline demands (record BOTH `ω` and `π_ω` every step). Pure size scaling: R = 2r, r ∈ {4, 6, 8}, N scaled to match margins.

**Apparatus gates (skill A — all cleared):**
- **known-null** (amp=0): no winding → no slosh (false-positive floor = 0). ✅
- **known-positive extractor at EACH scale** (the de-novo r≈1.1 poloidal floor avoided by construction): the planted (2,3) reads back at r=4/6/8 — `(w_tor,w_pol)=(2,3)`, rel `(0.73,0.62)/(0.734,0.629)/(0.744,0.629)`, `is_2_3=True`. The extractor resolves (2,3) at all three scales. ✅
- **free-evolution ledger floor**: the ω-tank total-energy drift = **23.7% / 12.3% / 7.1%** at r=4/6/8 (decreasing with resolution — coarse N=38 at r=4 is the worst). This is the instrument floor the invariance must clear. ✅ (stated next to the number)
- **grid-resolution sweep (r=6, N=44/50/62)**: `f_exch = 1.0001/0.9986/0.9986`, `ω_field = 1.078/1.074/1.074` — converged at N≥50. ✅

**The scale sweep:**

| r | N | f_exch (C↔L slosh) | ω_field | ⟨L⟩/⟨C⟩ | ledger floor (drift) | cycles |
|---|---|---|---|---|---|---|
| 4 | 38 | 1.0519 | 1.0929 | 1.288 | 23.7% | 6 |
| 6 | 50 | 0.9986 | 1.0741 | 1.134 | 12.3% | 5 |
| 8 | 62 | 0.9888 | 1.0524 | 1.076 | 7.1% | 5 |

- **f_exch INVARIANT**: spread **6.2%** < worst ledger floor **23.7%** ⇒ the exchange fraction is scale-invariant within the instrument floor. ✅
- **ω SCALES with size** (product-set): `1.093 → 1.074 → 1.052`, monotone DOWN toward the mass-gap floor `ω_0 = 1.0` — exactly the LC prediction `ω = √(c_ω²k² + ω_0²) → ω_0` as `k~1/r → 0`. ✅
- **⟨L⟩/⟨C⟩ virial ratio** relaxes `1.29 → 1.08` toward equipartition (the gradient term yielding to the mass-gap term as size grows) — consistent with, not contradicting, the LC reading.

**Secondary — the literal cross-sector u↔ω (V↔ω via the buckle):** `H_couple/E_ω = 5.36×10⁻⁶` — far below the ledger floor. In this geometry (central breather wall vs the planted-(2,3) torus shell) the buckle barely fires, so the cross-sector channel is **UNRESOLVED** (geometry-limited). The CARRIER reactance pair (`ω↔π_ω`) is the resolved DOF pair — and the right one for the winding (representation-capability-check).

**Arm 3 BIN = SCALE-FREE** (exchange fraction invariant within the ledger floor; ω scales as LC predicts).

**Honest caveat (ave-evidence-framing):** `f_exch ≈ 1.0` is the **generic full-slosh value** of any clean LC oscillator, so its scale-invariance alone is *necessary-not-sufficient*. The LOAD-BEARING scale-free content is (a) the planted (2,3) reads back AND sloshes coherently at all three scales, and (b) `ω_field` scales toward the mass-gap floor as LC predicts. Treat Arm 3 as a **positive consistency** result for the coax/LC reading, not a sharp falsification of the torus-knot-only reading.

---

## 4. consistency-vs-emergence + conserved-vs-pumped classification

- **Class:** Arm 1/2 are **consistency/identity** (the EOS `c²=0` root is a parameter-free identity; the b/a is α-free but divergent). Arm 3 is a **manifestation/consistency** smoke (does the validated carrier's reactance pair behave scale-freely?). **None is graded emergence** — no dimensionless observable is computed from primitives without the candidate inputs.
- **conserved-vs-pumped:** the (2,3) winding is a conserved topological invariant — **energize+LOCK**, never pumped. The slosh is the `C↔L` exchange at fixed |winding| (the (2,3) reads back unchanged at every scale). No accumulation channel; no pump. ✅
- **phase-space-coordinate-check:** the `b/a`/`R/r` are REAL-SPACE radius ratios (compared to the 2.27 real-space canon, never φ²); the (2,3) winding is phase-space (read by the extractor in the ω Clifford torus); the slosh is a real-energy ledger. The three coordinate systems were kept disjoint throughout. The KEY finding sits ON this firewall: real-space b/a diverges, phasor reactance-pair slosh is scale-free.

---

## 5. SYNTHESIS + the §5-license next-step note (NOT run here)

Per the frozen synthesis map (prereg §7): **Arm-3 SCALE-FREE ∧ Arm-1 RATIO-DERIVED ⇒ the slosh lane EARNS its §5 license.** The map condition is met. But the result LOCALIZES the license precisely:

- The **real-space radius-ratio route** to 2.27/α (Arm 1 + Arm 2) is **CLOSED (divergent)**: the α-free `A→1` outer wall is asymptotic, so `b/a → ∞` and the only way to land on 2.27 is a fitted non-canonical wall. **Do not pursue a real-space b/a = 2.27 derivation.**
- The **scale-free invariant** Grant's secondary requires **IS real (Arm 3)** — but it lives in the **reactance/phasor coordinates** (the `ω↔π_ω` slosh fraction invariant + ω scaling toward the mass-gap floor). 

**Next-step note (design only, not run):** the phasor-native quantization derivation the §5 license permits should be designed **in the reactance/phasor coordinates** (the bond-LC `V_inc↔Φ_link` / `ω↔π_ω` pair, where the scale-free invariant lives), targeting the PHASE-space `φ²` Golden-Torus quantity — **NOT** as a real-space radius ratio (which this run showed diverges). It must keep the same coordinate firewall (real-space ↔ phasor-space are different quantities) and remain α-free on input. This is a candidate design, not a committed claim.

**What this convergence run did NOT do** (and must not be read as doing): it did NOT re-derive α (still ch8 Class-B), did NOT promote `ρ̄_cav=−1/φ` (still CANDIDATE-CLAIM), did NOT reopen the ¼-selection (CHALLENGE-CLOSED), did NOT touch the fenced material (mirror-vs-ring `(½)²`, real-space face counting, phasor↔real-space area bijection).

---

## 6. DERIVED / VERIFIED / BLOCKED (honest split)

**DERIVED / canonical-anchored:**
- the cavitation root `ρ̄_cav=−1/φ` as the EOS `c²=0` root (parameter-free identity; CANDIDATE-CLAIM EOS).
- the substrate-native coax log-factor `ln(b/a)=G(ρ̄_b)−G(ρ̄_a)` from the radial balance (same as the mfg-flow §4 `G`, re-used).
- the real-space canon `R/r≈2.27` (L3 doc 28 §5.3) and phase-space `φ²` (constants.py:200-201) as DISTINCT quantities — imported comparison-only.

**NUMERICALLY VERIFIED (this run; native units; ratios/fractions dimensionless):**
- Arm 1: `b/a` α-free, divergent at A→1, `A_cap`-clip-tracking (5.2→55.1); dead-input clean (inner moves, α flat, rejected √(2α) BC α-dependent).
- Arm 2: `R/r` at A→1 divergent / +329% vs 2.27; the 2.27-forcing wall ρ̄≈0.304 is non-canonical (fitted).
- Arm 3: (2,3) reads back at r=4/6/8 (is_2_3=True); f_exch invariant (6.2% < 23.7% floor); ω scales 1.093→1.052 toward ω_0; grid-converged at N≥50; cross-sector V↔ω floor-limited (5.36e-6).

**BLOCKED / out of scope:**
- absolute units (native c₀ / lattice units; the verdict is dimensionless: ratios, fractions, scalings).
- the literal cross-sector u↔ω (V↔ω) exchange — geometry-limited (buckle non-overlap); would need a co-located breather+winding config (a separate design, Rule 12 — not refilled here).
- the phasor-native quantization derivation the §5 license permits — DESIGN-only note (§5); not run.

---

## 7. Corpus-state deltas to QUEUE (auditor lands; implementer surfaces only)

1. **NEW result (consistency-class, convergence):** the discriminating secondary of the α-¼ §5 gate — Grant's *"L and C change together in scale but not relative magnitude"* — is **CONFIRMED in phasor/reactance coordinates** (Arm 3 SCALE-FREE: the (2,3) carrier's `ω↔π_ω` slosh fraction is scale-invariant while ω scales toward the mass-gap floor) and **REFUTED in real-space radius coordinates** (Arm 1/2: the α-free `A→1` outer BC gives a DIVERGENT b/a, not 2.27). The slosh lane earns the §5 license **for a PHASOR-coordinate quantization derivation only** (next-step note §5).
2. **REINFORCES the coordinate firewall** (`28_two_node_electron_synthesis.md` §4.2; `ch8-alpha-golden-torus.md`): real-space radius ratios and the phasor `φ²` are different quantities — now shown from the coax direction (real-space b/a diverges; the scale-free invariant lives in phasor space).
3. **FLAG — `ρ̄_cav=−1/φ` remains CANDIDATE-CLAIM** (zero KB/constants hits); this run does not promote it. It uses it only as a parameter-free EOS root + an α-free inner BC.
4. **FLAG (flag-don't-fix) — the b/a divergence is the single mechanism:** the α-free A→1 (full compression) wall is asymptotic (`c²→∞`), so no finite real-space b/a exists for the v=c₀ profile. Any future "coax b/a = 2.27" hypothesis must specify a DIFFERENT (finite, α-free, canonical) outer locus — the A→1 saturation wall is not it. Surfaced verbatim, not reframed.
5. **FLAG — representation nuance:** the literal cross-sector u↔ω (V↔ω) is UNRESOLVED here (buckle geometry-limited, `H_couple/E_ω=5.4e-6`); the resolved + correct DOF pair for the winding is the carrier's own reactance pair `ω↔π_ω`. A co-located breather+winding config would be needed to resolve the cross-sector channel (separate design).
