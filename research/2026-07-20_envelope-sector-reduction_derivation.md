# Envelope-Sector Reduction — the analytic legs (Leg 0 sign / Leg A multiple-scales / Leg B channel-asymmetry)

**Date:** 2026-07-20
**Class:** DERIVATION (analytic legs of the frozen prereg `research/2026-07-20_envelope-sector-reduction_prereg-FROZEN.md`). Forms `[derived]`; values `[canon]`/`[import]`-tagged. Mints no `clm-`; propagates to no leaf; engine byte-untouched.
**Provenance:** Grant-fired 2026-07-20 (`"fire the lane"` `[sic]`). COMMIT 2 (derivation), after the prereg was frozen + pushed ALONE (`e27cc5e0`). The Leg-C driver + the integrated frozen-bin verdict land in later commits. Every `[canon]` cite content-verified two-method at base HEAD `f84b622b`; `[branch @ d17a2248]` for #761.

> **Scope note.** This doc lands the Leg-0/A/B ANALYTIC findings + their bin-leanings. The FINAL frozen-bin verdict — citing only the frozen criteria's outputs — lands in the result doc after Leg C runs. Per the anti-seduction fence, findings here are the frozen criteria's analytic outputs; nothing else.

---

## §0 — the pre-reg's UNDETERMINED forks, and the one fact that dissolves two of them up front

The prereg (§4) named three verdict-controlling forks. The mechanical-constitutive canon (Leg 0) forces the mechanical bulk and shear channels to **grade together** under saturation, which pre-emptively resolves Fork F2 (the emergent-boundary Γ) and Fork F3-ratio (the saturation dependence of the partition). Fork F1 (source vs coefficient) is resolved by the **gaplessness** the #761 lane established. The three legs below carry this out.

---

## §1 — LEG 0: the compression-channel grade under S(A) (sign check) `[canon-read + derived]`

**The kernel and the two mechanical speeds.** Ax4: `S(A) = √(1 − (A/A_yield)²)` ∈ [0,1], monotone-decreasing in `A` (`eq_axiom_4.tex:7` `[canon]`). The substrate's mechanical (rest-mass / group) speed is `c_shear(A) = c₀√S` (`temporal-spatial-lattice-decomposition.md:28` `[canon]`: `√g₀₀ = √S` is the local `c_shear` clock; KB CLAUDE.md Ax4 "two effective speeds"). The compression (P) speed `c_P = √((K+4G/3)/ρ)`; with `K = 2G` (`srs-band-structure.md:116` `[canon]`, GR-imported PR#261) both moduli carry the same overall saturation factor.

**Sign of the grade (derived).** Under the symmetric mechanical saturation `G_eff = G₀S`, `K_eff = K₀S` (both ∝ S; forced by `K=2G` being scale-invariant):
- `c_P(A) = c_{P0}√S` and `c_shear(A) = c_{shear0}√S` — **both DECREASE with A (soften).** The saturated lump is a **slow region** for both mechanical channels → refractive index **UP** → a **converging / focusing** region (a graded-index well), NOT diverging.
- `Z_bulk = ρc_P ∝ √S → 0` and `Z_shear = ρc_shear ∝ √S → 0` as `A → A_yield` (`S → 0`). At the fully-saturated wall **both** mechanical impedances vanish → `Γ_bulk = Γ_shear = −1` (soft / pressure-release), **together** (`lattice-extreme-bh-rationality.md:37` `[canon]`, verbatim: *"the `Γ=−1` reflection is **shear + bulk** (`G_shear→0`, `c_bulk→0`, `Γ_shear=Γ_bulk=−1`) while EM stays matched (`Γ_EM=0`)"*). Only the EM channel stays matched (`Γ_EM=0`); the two MECHANICAL channels are grade-locked.

**★The frozen-ratio fact (decisive; `[canon]`, PR#521, `clm`-carried).** `electron-bh-isomorphism.md:38` `[canon]` (PR#521 MERGED, quantitative-support / CONSISTENCY): the ABSOLUTE moduli collapse by the overall factor `S` toward zero (`C_44: 0.17661 → 0.02536 → 4×10⁻⁵` as `A→1`), but the **dimensionless RATIOS freeze** (`ν`, Zener, `K/G` are "**homogeneous degree-0 in the bond stiffnesses**, so they depend on `ρ_eff` alone and are unshifted by saturation magnitude"). **Therefore `c_P/c_S` is FROZEN under saturation magnitude — a saturated lump has the SAME `c_P/c_S` ≈ 1.71–1.90 (`srs-band-structure.md:120` `[canon]`, `clm-bnd5rq` 0.8 ok-with-caveats) as the cold vacuum.** The compression/shear far-field partition `κ² = A_ang(c_S/c_P)⁵` does **not** shift with saturation depth.

**Leg-0 output (frozen deliverable).** `dc_P/dA < 0` (softens; index up; converging), `dZ_bulk/dA < 0` (`→0`, `Γ_bulk→−1`), and — the load-bearing one — **the mechanical channels grade together (`Γ_shear=Γ_bulk` at the wall) and the `c_P/c_S` RATIO is saturation-invariant (degree-0)**. This orients Legs A/B and pre-resolves Fork F2 (any emergent-Γ image effect is SYMMETRIC across the two mechanical channels, not a compression-only asymmetry) and Fork F3-ratio (saturation does not change the partition).

---

## §2 — LEG A: multiple-scales reduction, the envelope equation, and the multipole order `[derived]`

### §2.1 — the two-scale ansatz (fast carrier / slow envelope)

The mass is the ENVELOPE of the A1 breather (`master-equation.md:20` `[canon]`). Write the displacement field as a fast node-resonance carrier `ω₀ = ω_e` (Compton-scale, node LC self-frequency) modulated by a slow envelope `A(x,T)`:

$$u(x,t) \;=\; A(x,T)\,e^{-i\omega_0 t}\,\hat e \;+\; \text{c.c.} \;+\; u_{\rm slow}(x,t),\qquad T = \varepsilon t,\ \ \varepsilon = \Omega/\omega_0 \sim 10^{-24}.$$

The carrier `ω₀` sits at the node self-resonance (the top/optical scale) — **NOT** on the gapless acoustic branch. The acoustic P and S branches are the LOW-frequency (`ω → 0` as `k → 0`) gapless modes `u_slow`. Gravitational radiation at `2Ω` lives in `u_slow` (deep-IR acoustic), 24 decades below the carrier.

### §2.2 — the envelope equation and its linear mode content

Substituting into the saturable elastic equation `ρü = ∇·σ[S(|A|)]` and collecting orders (standard multiple-scales / Newell-Whitehead), the carrier envelope obeys an **NLS-class** equation:

$$i\,\partial_T A \;+\; \tfrac12\,\omega_0''(k_0)\,\nabla^2 A \;+\; \gamma\,\mathcal N(|A|^2)\,A \;=\; 0,$$

with `ω₀''(k₀)` the carrier-band curvature and `𝒩` the saturable nonlinearity from `S`. **Linear mode content:**
- **about the cold vacuum (`A=0`):** `i∂_T A + ½ω₀''∇²A = 0` — a **PARABOLIC (Schrödinger-class)** dispersion `ω_env = ½ω₀''k²`, NOT an acoustic `ω = c_env k`. The envelope of the carrier does **not** itself carry a gapless *acoustic* branch; it is a massive/dispersive band centred at `ω₀`. **This is why the envelope's OWN band offers no new low-frequency radiative channel** — the carrier-band content sits at `ω₀ ± nΩ` (node scale), not at `2Ω`.
- **about a saturated lump's tail:** the linearization has (i) a **translational zero mode** (the Goldstone mode of the broken translation symmetry — the lump's center of mass `X`), and (ii) the continuous spectrum. The orbiting lump is this zero mode DRIVEN at `2Ω`.

### §2.3 — ★what the orbiting envelope-lump actually sources (the source/coefficient split, resolved)

The far-field radiation at `2Ω` is NOT the carrier-band content (that sits at `ω₀`, gapped, adiabatically suppressed by `ε = Ω/ω₀ ~ 10⁻²⁴`). It is the **ponderomotive back-reaction of the carrier intensity `|A|²` onto the low-frequency acoustic field `u_slow`**. `|A(x,T)|²` IS the mass-energy density (`master-equation.md:20`: the breather's trapped compression energy = the rest mass); its DC part digs the static well (the near-field / halo, port-register P9), and its orbital modulation sources `u_slow`:

$$\rho\,\ddot u_{\rm slow} - \nabla\!\cdot\!\sigma[u_{\rm slow}] \;=\; -\nabla\!\cdot\!T^{\rm pond}[\,|A|^2\,],\qquad T^{\rm pond}_{ij} \;\sim\; \partial_i A^*\partial_j A + (\text{trace}).$$

**Fork F1 resolved (source vs coefficient).** Whether one calls `|A|²` a *source* on the RHS (picture a) or a slowly-moving *coefficient* well the envelope rides (picture b), the object that reaches the far field at `2Ω` is the SAME: the ponderomotive stress `T^{pond}[|A|²]` of the orbiting mass-density, whose second moment is the **mass quadrupole** `Q_ij ∝ ∫x_i x_j |A|² d³x`. **The hoped-for adiabatic suppression (picture b, `exp(−ω₀/Ω)`) protects only the CARRIER band** (the internal breather at `ω₀`, which IS gapped). **It does NOT protect the acoustic channels, which are GAPLESS** (the P-branch reaches DC — #761 Leg A, `clm-bnd5rq` 0.8; the S-branch likewise). A gapless channel offers no adiabatic gap: the orbiting envelope radiates **power-law** into it at `2Ω`. *The #761 gaplessness result is exactly what defeats the envelope framing's suppression hope.* `[derived]`

### §2.4 — ★the multipole order of the compression coupling (Fork F3, resolved by `mass = A1-dilatation`)

The compression channel is sourced by the dilatation moments of the mass. Because `mass = A1-dilatation` (`master-equation.md:20` `[canon]`), the compression multipole moments ARE the mass multipole moments — and the SAME conservation laws that kill low-order GR radiation kill them here:

| Order | Compression moment | Conservation | Radiates? |
|---|---|---|---|
| Monopole `ℓ=0` | `∫∇·u ∝ M` (total mass) | `Ṁ = 0` | **NO** |
| Dipole `ℓ=1` | `∫x_i(∇·u) ∝ M X_{cm,i}` (`= mass dipole`, since `θ ∝ ρ_mass`) | `Ẍ_cm = 0` (momentum cons., isolated) | **NO** |
| Quadrupole `ℓ=2` | `∫x_i x_j(∇·u) = Q_ij` (rotating mass 2nd-moment) | `⃛Q^{TL} ≠ 0` | **YES** |

**The dipole-kill is exact PRECISELY because `mass = A1-dilatation`:** the dilatation dipole `∫x θ` equals the mass dipole `M X_cm`, whose second derivative is the total force `= 0`. So the compression channel starts at **quadrupole order — the SAME order as the shear (GW) channel** — with the SAME source `Q_ij` rotating at `2Ω` (`⃛Q^{TL} ≠ 0`, the tracelessness rescue is dead, `[branch:#761 @ d17a2248]` §2 / q1 §1). Fork F3 resolves to **same multipole order → no `(Ω/ω_ref)^{2Δℓ}` suppression** (`Δℓ = 0`). `[derived]`

### §2.5 — Leg-A output

The compression-envelope radiation at `2Ω` is the mass-quadrupole ponderomotive coupling into the **gapless** P-branch, at the **same multipole order** as shear, with a partition RATIO **frozen** under saturation (Leg 0). Combining: `κ_env² = A_ang(c_S/c_P)⁵ = (2/3)(c_S/c_P)⁵` — the q1 value, unshifted by the envelope reframe. `[derived]`

---

## §3 — LEG B: channel asymmetry + the consistency gate `[derived]`

**Is the observed GW carrier-shear or envelope-texture shear?** The same ponderomotive coupling sources the S-branch: the traceless part of `T^{pond}[|A|²]` at `2Ω` drives the transverse displacement `∇×u_slow` — the observed GW, the mass quadrupole radiating shear exactly as in GR (the standard Peters-Mathews channel; `08_gravitational_waves.tex` `[canon]`, the corpus's HT reproduction). The shear is a **gapless** acoustic branch → radiates power-law at `2Ω` → **the observed GW survives at the GR rate. Consistency gate: PASS for shear.** `[derived]`

**Is the derived structure ASYMMETRIC or SYMMETRIC?** SYMMETRIC. The two mechanical channels are grade-locked (Leg 0, `lattice-extreme-bh-rationality.md:37`: `Γ_shear = Γ_bulk` at the wall) and the `c_P/c_S` ratio is saturation-invariant (`electron-bh-isomorphism.md:38`, degree-0). **Fork F2 (image-cancellation) resolved:** whatever the emergent saturated shell does to the compression far field it does IDENTICALLY to the shear far field (same `Γ=−1`, same `√S` grade) — so any image-cancellation is symmetric across the two channels and **cannot** suppress compression WITHOUT equally suppressing shear. The only genuinely asymmetric channel is EM (`Γ_EM=0`), which gravity does not use (sector-ownership: mass = A1, GW = T2 shear; both mechanical). `[derived]`

**★The consistency gate forecloses BIN 2 (the decisive Leg-B finding).** BIN 2 needs a mechanism that suppresses compression to `κ_env² ≤ κ_max²` WHILE leaving shear at the GR rate. But every candidate suppression is **channel-symmetric** on the mechanical sector:
- an adiabatic gap would gap BOTH acoustic branches (both are gapless — neither is gapped);
- the emergent `Γ=−1` shell reflects BOTH (`shear + bulk`, canon `:37`);
- the `√S` softening grades BOTH (ratio frozen).

So any mechanism that silences compression silences shear too → **BIN 3, not BIN 2.** The consistency gate (frozen: a mechanism that silences both fails into BIN 3) is therefore not merely un-passed — it is **structurally unreachable** for compression-only suppression. This is the envelope-level analog of #761's "the make-or-break is structurally BLOCKED": there is no channel-asymmetric structure in the mechanical sector for a suppression to live in. `[derived]`

---

## §4 — Leg synthesis (analytic bin-lean; final verdict in the result doc after Leg C)

| Leg | Analytic finding | Fork resolved | Bin-lean |
|---|---|---|---|
| **0 — sign** | both `c_P`, `c_shear` soften ∝√S; `Γ_shear=Γ_bulk=−1` together at the wall; `c_P/c_S` ratio FROZEN (degree-0) | F2 (symmetric), F3-ratio (saturation-invariant) | → BIN 1 / forecloses BIN-2-via-F2 |
| **A — reduction** | carrier band parabolic at `ω₀` (gapped, adiabatically suppressed); orbital-band radiation = mass-quadrupole ponderomotive coupling into the **gapless** P-branch; `Δℓ=0` (compression starts at quadrupole, `mass=A1-dilatation` kills monopole+dipole) | F1 (gaplessness defeats adiabatic hope), F3-order (`Δℓ=0`) | → BIN 1: `κ_env² = (2/3)(c_S/c_P)⁵` ≈ q1 value |
| **B — asymmetry** | shear radiates at GR rate (gapless, survives); structure SYMMETRIC (mechanical channels grade-locked); consistency gate forecloses compression-only suppression → BIN 3 not BIN 2 | F2 (symmetric) | → BIN 1; BIN 2 structurally unreachable; shear-survival ⇒ NOT BIN 3 |

**Analytic lean: BIN 1 (ENVELOPE-RADIATES), with the mechanism NAMED —** the envelope reframe fails to rescue Reading B for two derived reasons: (i) the compression radiation channel is **gapless**, so the adiabatic scale-separation (`Ω/ω₀ ~ 10⁻²⁴`) suppresses only the carrier band, never the orbital-band acoustic radiation; (ii) the mechanical bulk and shear channels are **grade-locked** (`K=2G`, `Γ_shear=Γ_bulk`, ratio degree-0), so no channel-asymmetric structure exists for a compression-only suppression to live in — any suppression silences the observed GW too (BIN 3), which the observation forbids. The expected coupling is `κ_env² = (2/3)(c_S/c_P)⁵ ≈ 0.033 ≫ κ_max² = 1.3×10⁻⁴` (`≈ 250×` the double-pulsar bound). **Leg C (the driver) tests the coefficient-coupling half empirically** — does a SATURATED (Op14-ON) translated texture radiate compression at the same partition as the cold breathing source, confirming the saturation-invariance of Leg 0? The frozen-bin verdict integrates Leg C in the result doc.

---

> **Derivation-legs provenance.** Fired by Grant 2026-07-20 (`"fire the lane"` `[sic]`). COMMIT 2 after the prereg froze + pushed ALONE (`e27cc5e0`). Forms `[derived]` by multiple-scales + multipole/conservation algebra; the load-bearing constitutive facts are `[canon]` (`eq_axiom_4.tex:7`, `temporal-spatial-lattice-decomposition.md:28`, `lattice-extreme-bh-rationality.md:37`, `electron-bh-isomorphism.md:38`/PR#521, `srs-band-structure.md:116,120`, `master-equation.md:20`) all content-verified two-method at base `f84b622b`; #761 cited `[branch @ d17a2248]`. Mints no `clm-`; propagates to no leaf; engine byte-untouched; port-register untouched. The FINAL frozen-bin verdict lands in `research/2026-07-20_envelope-sector-reduction_result.md` after Leg C. Companion: the frozen prereg (`_prereg-FROZEN.md`), `[branch:#761 @ d17a2248]`, the q1 hardening, the port register Q1 row.
