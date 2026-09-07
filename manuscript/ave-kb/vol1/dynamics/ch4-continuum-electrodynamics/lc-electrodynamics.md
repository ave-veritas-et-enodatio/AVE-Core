[↑ Ch.4 Continuum Electrodynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-crbl60]
-->

## Section 4.2: Continuum Electrodynamics of the LC Network

### The Dimensionally Exact Mass Density ($\rho_{bulk}$)

Previous classical aether models failed because they incorrectly attempted to map vacuum mass density directly to the magnetic permeability constant ($\mu_0$), violating SI dimensional analysis ($[\text{H/m}] \neq [\text{kg/m}^3]$).

The baseline macroscopic bulk mass density ($\rho_{bulk}$) of the spatial vacuum network is defined as follows. The effective inductive mass of one discrete node is derived from the inductance-mass isomorphism. The permeability $\mu_0$ has dimensions of $[\text{H/m}]$. Under the topo-kinematic isomorphism ($[\Omega] = \xi_{topo}^{-2}[\text{kg/s}]$), inductance maps to mass via $L = \xi_{topo}^{-2} m$. Because the vacuum inductance per unit length is $\mu_0$, the mass of one node spanning $\ell_{node}$ is:

> **[Resultbox]** *Effective Inductive Node Mass*
>
> $$
> m_{node} = \xi_{topo}^2 \mu_0 \ell_{node}
> $$

> **[Resultbox]** *Longitudinal (P) Wave Velocity* 🔴 **[DEMOTED 2026-08-11 — R40-B1; dated demotion note at the end of this file]**
>
> $$
> c_L = \sqrt{\frac{K_{bulk} + \tfrac{4}{3}G_{vac}}{\rho_{node}}}
> $$
>
> *(2026-06-08 c_L reconciliation, Rule 12: prior wording gave $v_{longitudinal} = \sqrt{K_{bulk}/\rho_{node}}$ — the bulk-modulus (dilatational) speed, which omits the $4G/3$ shear term. The isotropic-solid longitudinal P-wave carries the shear term; at $K=2G$ this is $\sqrt{10/3}\,c$ ($\nu=2/7$; canonical vol_2 Ch 7). The $\sqrt{K/\rho}$ bulk-modulus dilatational speed is retained as the distinct bulk quantity.)*

Dividing by the Voronoi geometric volume of a single spatial node ($V_{node} = p_c \ell_{node}^3$, from the packing fraction $p_c = 8\pi\alpha$ derived in Chapter 2):

> **[Resultbox]** *Macroscopic Bulk Mass Density*
>
> $$
> \rho_{bulk} = \frac{m_{node}}{V_{node}} = \frac{\xi_{topo}^2 \mu_0 \ell_{node}}{p_c \ell_{node}^3} = \frac{\xi_{topo}^2 \mu_0}{p_c \ell_{node}^2} \approx 7.91 \times 10^6 \text{ kg/m}^3
> $$

> 🔴 **Engine-lockstep value re-pin, 2026-08-03 (Rule 12 — the prior printed `\approx 7.92 \times 10^6 \text{ kg/m}^3` is quoted here and preserved, not deleted). THIS IS THE RECEIPT SITE for the corpus-wide re-pin; the ten mirror rows point here.** The printed 3-s.f. value carried a $+0.13\%$ transcription drift against the engine constant. Recomputed two ways, both on `src/ave/core/constants.py`:
> - **banked:** `RHO_BULK` $= 7{,}909{,}692.740007466$ kg/m³
> - **recomputed from this leaf's own formula:** `XI_TOPO**2 * MU_0 / (P_C * L_NODE**2)` $= 7{,}909{,}692.740007466$ kg/m³ — **bit-identical**, so the formula printed above and the engine constant are the same object, and the drift was purely in the transcription.
>
> To 3 significant figures that is $\mathbf{7.91 \times 10^6}$ kg/m³, not $7.92\times10^6$. **No formula, symbol or downstream quantity changes.** Specifically $G_{vac} = \rho_{bulk}c^2$ at `index.md`:21 ($7.12\times10^{23}$ Pa) and the cross-check $v_T = \sqrt{G_{vac}/\rho_{bulk}} = c$ are both unaffected at their printed precision, and `vol4/claim-quality.md`:870/:882 already carried $7.91\times10^6$.
>
> **Ten sites re-pinned in the same commit** (two-method sweep — a literal `7.92` scan **plus** an independent `rho_bulk`-symbol context scan; the second method found four sites the first item list did not name): this leaf `:35`; [`ch4-continuum-electrodynamics/index.md`](index.md):20; [`vol1/dynamics/index.md`](../index.md):25; [`vol1/index.md`](../../index.md):31; [`vol1/claim-quality.md`](../../claim-quality.md):643; [`vol2/appendices/app-c-derivations/index.md`](../../../vol2/appendices/app-c-derivations/index.md):20; [`common/appendices-overview.md`](../../../common/appendices-overview.md):64; `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex`:194; `manuscript/backmatter/01_appendices.tex`:99; `manuscript/vol_0_engineering_compendium/chapters/02_analytical_summaries.tex`:53. *(The three `.tex` coordinates are post-re-pin; on `origin/main` they read `:177` / `:92` / `:44` — the in-place Rule-12 comment blocks displace them. Content anchor for all three: the `\rho_{bulk} = \frac{\xi_{topo}^2 \mu_0}{p_c \ell_{node}^2}` line.)*
>
> 🟠 **SCOPE AMENDMENT 2026-08-03 (Rule 12 — the paragraph above is preserved verbatim and unedited; this note bounds it, it does not replace it).** The sentence above reads, verbatim: *"**Ten sites re-pinned in the same commit** (two-method sweep — a literal `7.92` scan **plus** an independent `rho_bulk`-symbol context scan; the second method found four sites the first item list did not name)"*. As written that reads as a **corpus-complete** claim. It is not, and was not, complete. **What it actually covered: ten `manuscript/` sites, at 3 significant figures, in commit `c5cf9fa3`.** The honest scope of the $\rho_{bulk}$ re-pin, after the 2026-08-03 repair pass, is three tiers:  <!-- rule12-freeze: base=8f6e5c8230fdbba4daaffa165d9bacc954add277 region=above offset=0 lines=23 bytes=3142 sha256=365ade26b602490ebe0e735e8580404a54f5e4150073ada12335ea755a1d2f50 -->
>
> | tier | sites | disposition |
> |---|---|---|
> | **A — `manuscript/`, 3 s.f.** | the ten listed above | re-pinned $7.92\times10^6 \to 7.91\times10^6$ in commit `c5cf9fa3` |
> | **B — `src/`, live engine text** | `src/ave/core/lbm_3d.py`:9 (docstring; cited `RHO_BULK` on the same line while printing a different number) and `src/scripts/vol_4_engineering/simulate_sagnac_kinematic_entrainment.py`:65 **as-found** / `:84` **post-repair** (**a live hard-coded `rho_vacuum = 7.92e6` in an executed code path**, whose adjacent comment also omitted the $\xi_{topo}^2$ numerator; content anchor: the `rho_vacuum =` assignment inside `calculate_ave_sagnac`) | repaired in the 2026-08-03 repair pass — the script now **imports** `RHO_BULK` rather than transcribing it |
> | **C — `manuscript/`, 4 s.f. family** | `vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md` and its by-methodology twin `vol4/falsification/ch11-experimental-bench/sagnac-rlve.md` — both printed $7.916\times10^6$ | re-pinned to $7.910\times10^6$ in the repair pass; **no cascade** ($\kappa_{entrain}$ still $0.00244$) |
>
> **Tier D — historical `research/` documents: recorded, deliberately NOT edited.** These are frozen dated working documents; re-pinning a value inside a dated result would falsify the record of what that document actually computed. **Six files, nine mentions**, enumerated so the record is closed rather than merely bounded: `research/2026-05-17_C13b_bullet_cluster_prereg.md`:76; `research/2026-05-17_C14-DAMA_amplitude_prereg.md`:48; `research/2026-05-17_DAMA-bulk-transfer-function-reframe.md`:76 (all $7.92\times10^6$); `research/2026-05-17_parametric-coupling-kernel-prereg.md`:113; `research/2026-05-17_plumber-physical-audit-matched-LC.md`:27,:34,:37; `research/2026-05-18_flyby-anomaly-anderson-anchor-result.md`:237,:242 (all $7.916\times10^6$).
>
> ★ **One tier-D site carries a live false attribution, flagged not fixed (dated-doc class).** `research/2026-05-18_flyby-anomaly-anderson-anchor-result.md`:237 states verbatim: *"Canonical $\rho_{bulk} = 7.916 \times 10^6$ kg/m³ — substrate-derived as `RHO_BULK = ξ²μ₀/(p_c·ℓ²_node)` at `src/ave/core/constants.py` `RHO_BULK`."* **`constants.py` `RHO_BULK` does not and did not evaluate to $7.916\times10^6$** — it evaluates to $7{,}909{,}692.74$, i.e. $7.910\times10^6$. The sentence attributes a number to a named engine constant that does not produce it, and it already carries a *different* 2026-06-03 provenance correction (`[provenance wording corrected 2026-06-03]`) which repaired the *direction* of the derivation and left the *value* misattribution standing. Per flag-don't-fix and the frozen-document rule this is **recorded here and not edited there**; whether a dated research result may carry an in-place attribution correction is a corpus-posture question, not a mechanical one.
>
> **Two-method re-sweep after the repair pass (whole repo, both methods run independently):** literal `7.92`-with-density-context scan **and** literal `7.916` scan **and** a `rho_bulk`/`RHO_BULK`-symbol context scan. **Final count: 12 corpus sites re-pinned (10 tier-A + 2 tier-C), 2 `src/` sites repaired (tier B), 9 historical `research/` mentions across 6 files recorded-not-edited (tier D), 0 remaining un-dispositioned.** *(The audit that routed this repair named "five" historical `research/` mentions; the re-sweep finds nine across six files. The larger count is reported rather than the routed one — surfaced, not silently reconciled.)*

> **[Resultbox]** *1D String Tension Density (axial stiffness)*
>
> $$
> G_{string} = \frac{T_{EM}}{\ell_{node}} = \frac{m_e c^2}{\ell_{node}^2} \approx 5.49 \times 10^{11} \text{ Pa}
> $$

> **[Resultbox]** *Baseline 3D Vacuum Shear Modulus*
>
> $$
> G_{vac} = \rho_{bulk} \cdot c^2 \approx 7.12 \times 10^{23} \text{ Pa}
> $$
>
> Cross-check: $v_T = \sqrt{G_{vac}/\rho_{bulk}} = c$ (canonical transverse wave speed per [`photon-propagation-baseline.md:16`](photon-propagation-baseline.md), [`k4-port-irrep-decomposition.md:129`](../../operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md), [`de-broglie-standing-wave.md:236-240`](../../../vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)).
> <!-- [2026-07-19 Tier-2.5 anchor repoint, Rule-12 in-place: the k4-port-irrep-decomposition anchor was `:109`; content-verified at HEAD to `:129` — the cited content "$T_2$ (transverse photon): $c=\sqrt{G/\rho}$" is the §6 propagation-speed-split row (line 129). NOTE: the k4 leaf's own LINE-ANCHOR DRIFT inventory listed this cite as `:109`→`:111`, which is ARITHMETIC-only (the +2 D1-block shift) and CONTENT-WRONG — line 111 is the Op3-transduction sentence, not the transverse-speed row. Grepped the quoted content per the #728 lesson; correct target is `:129`. Sibling C13b prereg carried the identical mis-target and is repointed to `:129` too. -->


**Correction note (2026-05-17 audit):** prior leaf revision conflated $G_{string}$ (1D axial stiffness, $T_{EM}/\ell_{node}$) with $G_{vac}$ (3D shear modulus, $\rho_{bulk} \cdot c^2$) and quoted "$G_{vac} \approx 5.48 \times 10^{24}$ Pa" — a 13-order-of-magnitude error. The correct quantities are now separated above per [`../../../vol2/appendices/app-f-solver-toolchain/derived-numerology.md:49-56`](../../../vol2/appendices/app-f-solver-toolchain/derived-numerology.md) which first identified the error. The 3D shear modulus $G_{vac}$ is what governs transverse-wave physics (photons, gravitational waves, bullet-cluster substrate-strain halos); the 1D string tension $G_{string}$ governs longitudinal/axial confinement physics.

### Deriving the Kinematic Mutual Inductance of the Universe ($\nu_{kin}$)

In classical kinetic network theory, the Kinematic Mutual Inductance ($\nu$) of a continuous network medium is defined as the product of its characteristic signal velocity ($v$) and its internal microscopic mean free path ($\lambda$), modulated by a dimensionless geometric momentum diffusion factor ($\kappa$): $\nu = \kappa v \lambda$.

<!-- 🔴 Rule-12 2026-06-21 INVARIANT-N1 𝓜_A→prose retirement: the retired $\mathcal{M}_{A}$ glyph (Amorphous-substrate symbol, retired 2026-06-18 per INVARIANT-N1 — the "A" carried the closed geometry-leak "amorphous") is replaced here by substrate-native prose ("chiral LC network"). Physics unchanged. -->
For the chiral LC network hardware lattice, the absolute internal signal velocity is $c$, and the topological mean free path is exactly the fundamental spatial lattice pitch $\ell_{node}$.

As established in Section 1.3.2, the geometric packing fraction ($p_c$) determines the structural porosity and transverse geometric scattering cross-section of the discrete graph (where $\alpha = p_c/8\pi$). Consequently, the macroscopic momentum diffusion across the lattice inherits this geometric scattering threshold ($\kappa \equiv \alpha$).

> **[Resultbox]** *Kinematic Network Mutual Inductance*
>
> $$
> \nu_{kin}=\alpha c \ell_{node}\approx8.45\times10^{-7}\text{ m}^{2}\text{/s}
> $$

This parameter-free derivation shows that the discrete vacuum medium possesses a macroscopic kinematic network mutual inductance close to that of liquid water.

> **Audit note (2026-05-17)**: a prior `src/ave/core/lbm_3d.py` docstring listed `ν_kin = (1/(4π)) × ℓ_node × c` (factor `1/(4πα) ≈ 10.9×` off the canonical form above). Verified documentation-only bug (no downstream code used the wrong formula; LBM default `nu=0.1` is lattice-units placeholder); docstring corrected to reference the canonical `NU_KIN = α × c × ℓ_node` import path from [`src/ave/core/constants.py`](../../../../../src/ave/core/constants.py).

---

---

### 🔴 Dated demotion note — 2026-08-11 (R40 demotion sweep, batch 1)

**Class: DIES-WITH-THE-PHANTOM.** Status change only — the claim text is **preserved
verbatim** (honesty-lag pattern, Rule 12) and stamped in place; it is **no longer live
canon**. Nothing is deleted.

**Demoted in this file:**

- **`:22`** — *"**[Resultbox]** *Longitudinal (P) Wave Velocity* ... $c_L = \sqrt{(K_{bulk} + \tfrac{4}{3}G_{vac})/\rho_{node}}$"*
  Stamped in place at `:22`.
  **Why it dies (audited row rationale, verbatim):** Standalone P-wave-velocity resultbox (with the Rule-12 note retaining sqrt(K/rho) as 'the distinct bulk quantity' — a second speed claim); no downstream quantity in this leaf consumes it: rho_bulk accounting and the v_T=c cross-check (:72) are untouched.
  **Scope carve (review fix 2026-08-11).** `:72` is **NOT** demoted — it is the TRANSVERSE/shear speed
  identity $v_T=\sqrt{G_{vac}/\rho_{bulk}}=c$, which the bulk carve does not touch. The audited
  rationale carves it verbatim: *"no downstream quantity in this leaf consumes it: rho_bulk accounting
  and the v_T=c cross-check (:72) are untouched."*

**The arc, complete — the framing R40 rules every demotion note carries:**

1. **The kill fired** (#930) — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the #261 K = 2G import** (G-RECON, unchallenged): the compressible
   far-field branch was minted by a GR-imported elastic modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the #935 flat-direction finding: the written
   action conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the RATIFIED bound-sector law — Axiom 5, Substrate DC Bias**
   (BC-SRC clauses **S** / **G** / **Q**), ratified per `_orchestration/docket-entries/2026-08-10-ruling-r43-ratification.md`, as reconciled by `_orchestration/docket-entries/2026-08-10-ruling-r44-r43-reconciliation.md` (R44 — the
   full-scope R43 record is FINAL and authoritative; the partial
   `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` is SUPERSEDED and is **not**
   the resolution). Under the ratified law the A1 / bulk slot is a **bound response** — mechanism
   gloss **back-reaction** — with no independent propagating branch, no port, and zero longitudinal
   characteristic speed. A bulk *wave speed*, a bulk *radiative port*, a bulk *band-branch* and a
   bulk *transit clock* therefore have **no referent**.

**Standing named-open debt (the honest rider).** The ratified axiom does **not** discharge
everything: **THE BIAS PROPAGATION THEOREM** is Axiom 5's standing named-open entry — clause G's
elliptic law is the *static abstraction* of underived finite-speed bias dynamics (`_orchestration/2026-08-10_bias-propagation-brief.md`). Where a
demoted claim's replacement depends on finite-speed bias dynamics, the resolution is the ratified
axiom **with that debt open**, not a closed replacement.

**Records.** R40 ruling `_orchestration/docket-entries/2026-08-10-rulings-r40-r42.md` · verified worklist `research/drivers/r40_sweep_worklist_verified.json` · scope verification `_orchestration/2026-08-10_r40-sweep-scope-verification.md` ·
batch-1 record `_orchestration/2026-08-11_r40-sweep-batch1.md` · vocabulary R50 `_orchestration/docket-entries/2026-08-10-ruling-r50-vocab.md` (canonical: the displacement pattern u₀ around a
deposit is **the bound response**, mechanism gloss **back-reaction**; ε₁₁ is **the bias**;
"dress", "grade"-as-canonical-noun and "halo"-for-the-physics are retired; and the owed theorem is
renamed **THE BIAS PROPAGATION THEOREM**) · vocabulary **R49(b)** `_orchestration/docket-entries/2026-08-10-rulings-r48-r49.md` (*"retardation"
is RETIRED from this role. The canonical term is **propagation delay / finite propagation speed*** —
the retardation retirement is R49(b)'s, NOT R50's; corrected 2026-08-11 at review).
