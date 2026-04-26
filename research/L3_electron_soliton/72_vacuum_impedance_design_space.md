# 72 — AVE design-space articulation: vacuum impedance + bound-state eigenmode analysis

**Status:** 2026-04-25. Precursor to R7.1 pre-registration. Per Grant directive ("I'm open as long as you understand the design/solution space that ave dictates" + "What's the smith chart for the vacuum? is it 3D?"), articulates the AVE-native conceptual stack for bound-state analysis BEFORE any further pre-registration drafting.

Three pre-registration retractions in this session ([doc 71_ §11](71_multi_seed_eigenmode_sweep.md#L11) v1 geometry bug → §12 v2 retracted draft → §13 multi-seed pre-reg pending audit flags) traced to depth-of-understanding gaps. This doc closes those gaps by walking the corpus end-to-end before the next pred attempt.

**Read after:** [doc 03_ §4.3](03_existence_proof.md#L143) (topological quantization is input not output), [doc 67_ §17-§26](67_lc_coupling_reciprocity_audit.md#L1282) (Helmholtz / acoustic-cavity framing + F17-K v2-v2 dual-descent results), [doc 70_ §7](70_phase5_resume_methodology.md#L7), [doc 71_ §13](71_multi_seed_eigenmode_sweep.md#L13) (current frozen pre-reg). Cross-repo: [AVE-HOPF `chiral_antenna_q_analysis.py:644-668`](../../../AVE-HOPF/scripts/chiral_antenna_q_analysis.py#L644), [AVE-VirtualMedia `generate_reflection_profile.py`](../../../AVE-VirtualMedia/scripts/generate_reflection_profile.py), [AVE-Protein `protein_fold.py:260-326`](../../../AVE-Protein/src/ave_protein/regime_2_nonlinear/protein_fold.py#L260) (TDI canonical).

---

## 1. The four AVE-native concepts that govern bound-state analysis

The retracted basin audit conflated two of these and ignored a third. Naming them directly to prevent the next round of conflation:

### 1.1 Wave eigenmode (Helmholtz / TLM-scattering — NOT Hessian-of-W)

The K4-TLM lattice runs **wave propagation**, not energy minimization. From [COLLABORATION_NOTES.md:65](../../.agents/handoffs/COLLABORATION_NOTES.md#L65) (2026-04-20 second observation):

> "What is the actual computation the lattice is running? continuous wave topology? ... The lattice runs K4-TLM wave propagation (`src/ave/core/k4_tlm.py`). The electron is a standing-wave eigenmode of that dynamics. No minimization is the computation; the TLM evolution IS the computation."

The bound-state mathematical object is therefore an **eigenmode of the wave operator**, not a stationary point of an energy functional. In Helmholtz form per [doc 67_ §23.1-§23.4](67_lc_coupling_reciprocity_audit.md#L1282):

```
∇·(z(x)·∇V) + k²V = 0     where  z(x) = z(A²(ω(x)))  via Op14
```

with eigenvalues `ω² = λ` solving for the spectrum at fixed cavity geometry. **Critical implementation consequence**: V_inc is the eigenvector OUTPUT of the eigsolve, not a seed INPUT. The Cosserat ω configuration sets the cavity geometry and `z(x)` profile; the wave solver returns resonant frequencies + mode shapes.

This collapses [doc 71_ §14.2 Flag A](71_multi_seed_eigenmode_sweep.md#L14)'s "K4 amplitude zero at seed" concern entirely. The Hessian-of-W framing required a seed for V_inc to break the cross-block degeneracy; the Helmholtz wave-equation formulation never asks for one.

### 1.2 Impedance match (S₁₁ minimum — NOT energy minimum)

The bound-state physical condition is **`Γ ≈ -1` at the cavity wall** (total internal reflection for the inward-traveling wave) or equivalently **`S₁₁ ≈ 0` at the port** (no leakage out). This is the AVE EE-native criterion, distinct from energy stationarity.

[Doc 67_ §17-§26](67_lc_coupling_reciprocity_audit.md#L17) established this empirically: F17-K Phase 5c-v2-v2 dual-descent ran **two parallel objectives** — Cosserat-energy and `|S₁₁|²` — from the same Golden Torus seed at N=80. Results per [§24 line 1370-1372](67_lc_coupling_reciprocity_audit.md#L1370):

| Objective | Final R/r | Status |
|---|---|---|
| Cosserat-energy descent | 4.08 (later refined to 3.40 with tanh-reparam) | converged but ≠ φ² |
| `\|S₁₁\|²` descent | 2.73 (later 1.03 with saturation pin) | converged but ≠ φ² |
| Corpus claim | φ² = 2.62 | — |

The two objectives are NOT equivalent. They have different stationary states. Neither hits corpus GT. **The bound state is at neither energy-minimum nor S₁₁-minimum alone** — it's at the intersection where the wave equation has an eigenmode AND boundary impedance match holds AND topology is preserved.

### 1.3 Topological quantization (input via ansatz — NOT dynamical attractor)

[Doc 03_ §4.3](03_existence_proof.md#L143) verbatim:

> "R·r = 1/4: topologically quantized, NOT dynamically derived... Both d = 1 and R − r = 1/2 are genuine dynamical derivations; R·r = 1/4 is a topological identity that the Lagrangian must be *consistent with* but does not by itself produce. It follows from the requirement that the toroidal shell area match the spin-1/2 half-cover quantum π² of the SU(2) field — a quantization condition forced by the SU(2) → SO(3) double-cover structure that is *input* to the Lagrangian, not *output* of its energy functional."

So R/r=φ² (or equivalently R·r=1/4 + R−r=1/2) is **selected by ansatz initialization, not derived by gradient flow**. F17-K v2-v2's failure to converge to GT under either objective is the corpus prediction holding empirically — neither objective KNOWS about topological quantization, so neither lands at the topologically-quantized point.

This is also why R7.1's three-mode falsification is asymmetric: mode (II) (eigenmode at F17K endpoint, not GT) is most disruptive because it would mean the engine's Helmholtz spectrum disagrees with the corpus topological-quantization claim. Mode (I) is the corpus-vindicating outcome; mode (III) is the "framework-level rework" outcome.

### 1.4 AVE basin = S₁₁ minimum, NOT W minimum

"Basin finding" is **protein-folding lingo** — [AVE-Protein `protein_fold.py:260-326`](../../../AVE-Protein/src/ave_protein/regime_2_nonlinear/protein_fold.py#L260) is the canonical TDI implementation, applied to **2D Ramachandran (φ, ψ) dihedral space** with multi-basin spectral weights. Protein basins are real attractors of the energy landscape (folded conformations).

The AVE-canonical analog at vacuum level is **S₁₁ minimization** (impedance-match descent), already implemented in F17-K's [`coupled_s11_eigenmode.py`](../../src/scripts/vol_1_foundations/coupled_s11_eigenmode.py). My retracted v1 [P_basin_audit_GT_stationarity](71_multi_seed_eigenmode_sweep.md#L11) imported the protein-folding "basin" terminology AND framed it on Cosserat **W functional** (energy landscape). Two errors compounded:

1. Protein-side basin is gradient-descent on energy → at vacuum level the analog is gradient-descent on **S₁₁** (impedance-match), not on W. F17-K v2-v2's coupled-S₁₁ descent IS the AVE-native basin finding for the (2,3) electron at coupled scale, and it already converged at R/r=1.03.
2. Even if vacuum-side basin meant W-minimum, the bound state is a **wave eigenmode** (concept §1.1), not a basin minimum. Bound states can exist at non-extrema of W if they're standing-wave resonances of the wave operator.

The basin audit asked the wrong question on two axes simultaneously. Reframing both axes makes the question moot.

---

## 2. The Smith chart for the vacuum — yes, 3D (with 4D flagged for later)

Standard EE Smith chart: `Γ = (Z − Z₀)/(Z + Z₀)` plotted in the complex plane at one frequency. **2D because impedance is complex (real + imaginary); the chart parameterizes resonance/match conditions for a transmission line at fixed ω.**

For the vacuum, `Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω` ([`Z_0` in `src/ave/core/constants.py`](../../src/ave/core/constants.py)). [AVE-HOPF `chiral_antenna_q_analysis.py:644-668`](../../../AVE-HOPF/scripts/chiral_antenna_q_analysis.py#L644) implements the standard 2D Smith chart for the vacuum already — at 50Ω test-instrument reference, normalizing torus-knot antenna impedances `Z_norm = R_total / 50` and plotting the resulting Γ for each (p,q) family. It's a single-frequency snapshot per (p,q) point; the standard 2D form.

### 2.1 Three natural 3D extensions

**Extension A — `(Re(Γ), Im(Γ), ω)`: frequency-trajectory chart.** Sweep ω at fixed cavity geometry (R, r); the impedance trajectory traces a curve in the 3D volume. Bound-state resonance is where the curve intersects `Γ = -1` (TIR cavity-wall condition). At that ω, the cavity supports a standing wave with no leakage. **This is the most direct generalization and what R7.1 should map.**

**Extension B — `(Re(Γ), Im(Γ), A²)`: saturation-trajectory chart.** Sweep `A²` (combined K4+Cosserat amplitude squared) at fixed (geometry, ω); trajectory traces regime transitions. Maps to [AVE-VirtualMedia `generate_reflection_profile.py`](../../../AVE-VirtualMedia/scripts/generate_reflection_profile.py)'s three-regime convention (Regime I passband Γ≈0 / Regime II transition / Regime III stopband Γ→1) but in the full 2D Γ plane rather than 1D magnitude. This is Op2 saturation behavior visible.

**Extension C — `(R, r, ω)` volume with 2D resonance surface.** Equivalent to Extension A but swept over geometry rather than tracing trajectory at one geometry. The resonance surface is the 2D submanifold where the cavity supports an eigenmode at frequency ω. Bound states at corpus claim are points where the surface intersects the `ω = ω_Compton` plane. Generalizes cleaner across non-(2,3) bound states (proton, electron, neutrino) because each has a different (R, r, ω_C) — same surface, different reading.

A and C are interchangeable parametrizations; A is more EE-natural (impedance trajectory), C is more physics-natural (resonance hypersurface). R7.1 implementation can use either or both.

### 2.2 4D extension flagged for later

Phase 4 asymmetric saturation per [`cosserat_field_3d.py:312-499`](../../src/ave/topological/cosserat_field_3d.py#L312) splits saturation into two tracks (`S_μ`, `S_ε`) biased by Beltrami helicity `h_local = ω·(∇×ω) / (|ω|·|∇×ω|)`. Under helicity bias the impedance differentiates by chirality:

```
Z_LH(ω) ≠ Z_RH(ω)     ⟹     Γ_LH(ω) ≠ Γ_RH(ω)
```

The 4D Smith chart adds **chirality h_local as a fourth axis**, splitting the resonance surface into LH and RH sheets. This becomes load-bearing for parity-violation analysis and for the chiral-pair-injection R7.2 work, but is **not load-bearing for R7.1's bound-state-existence question**. Defer to post-R7.1.

### 2.3 What this resolves about R7.1

The 3D Smith chart Extension A formulation is:
- At each cavity geometry (R, r), sweep ω across the band of interest
- Build Helmholtz operator at each (R, r, ω) sample
- Compute `Γ(ω)` at the cavity boundary (impedance match condition)
- Trace trajectory in 3D `(Re(Γ), Im(Γ), ω)` plot
- Find ω where trajectory crosses `Γ = -1` ⟹ resonance frequency at this geometry
- Compare to ω_Compton across multiple seeds (GT, F17K endpoints, vacuum control)

This dispenses with two of the audit flags entirely:
- **Flag A (V_inc seed)** — Helmholtz is operator-level; no V_inc seed needed.
- **Flag B (shape correlation)** — replaced by direct topological-crossing-count on the eigenvector V at resonance frequency. The eigenvector IS the standing-wave shape; `extract_crossing_count(V)` should return 3 for the (2,3) electron mode, regardless of how it differs from doc 34_ X4a's pre-coupling reference.

---

## 3. How R7.1 maps to this design space

The frozen pre-registration [`P_phase6_eigensolver_multiseed`](../../manuscript/predictions.yaml) per [doc 71_ §13.4](71_multi_seed_eigenmode_sweep.md#L13) framed R7.1 as "linearize coupled K4+Cosserat dynamics around each seed ansatz, build sparse generalized-eigenvalue Jacobian, eigsh at sigma=ω_C²." That framing is **Hessian-of-W eigsolve** — concept §1.1 says use Helmholtz wave-eigenmode instead.

### 3.1 The block Helmholtz formulation on joint `(V, ω)`

Per audit pushback on hybrid coupled modes: the bound electron is described in [doc 66_ §17.2](66_single_electron_first_pivot.md) as a **three-storage-mode hybrid** (ε strain → C, κ curvature → L, V pressure → C) — coupled across K4 and Cosserat sectors on equal footing. A single-sector V Helmholtz formulation treats Cosserat ω as a static cavity backdrop and misses Cosserat-sector eigenmodes the same way Hessian-of-W missed pure-Cosserat modes. The AVE-native operator must be **block Helmholtz on the joint `(V, ω)` state vector**:

```
                                       state    block-mass     state
  ┌  K_V       C_Vω  ┐ ┌V┐       ┌  M_V      0    ┐ ┌V┐
  │                  │ │ │ = ω²  │                │ │ │
  └  C_ωV     K_ω   ┘ └ω┘       └    0     M_ω  ┘ └ω┘
```

- `K_V`: K4-TLM wave operator on V, with Op14-modulated impedance `z(x; R, r) = z(A²(ω_seed(x; R, r)))` set by Cosserat ansatz.
- `K_ω`: Cosserat sector wave/elastic operator on ω, set by constitutive moduli (G, K, ρ_inertia) per [`cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py).
- `C_Vω, C_ωV`: cross-coupling blocks encoding Op14 K4↔Cosserat coupling explicitly. Generically nonzero where ω ≠ 0 AND V ≠ 0.
- `M_V, M_ω`: block-diagonal mass matrices (identity for Cosserat, impedance-weighted for K4).

`ω_seed(x; R, r)` is the (2,3) hedgehog ansatz from `initialize_electron_2_3_sector(R, r, amplitude_scale=0.3464)`. This sets the cavity geometry simultaneously for K_V (via z_local) and K_ω (via the seeded ω configuration that enters the Cosserat operator linearization).

Generalized block eigenvalue problem:
```
A · ψ = λ · B · ψ        where ψ = (V, ω)ᵀ,  λ = ω_n²
```

Using `scipy.sparse.linalg.eigsh(A, M=B, k=10, sigma=ω_Compton², which='LM')` returns the 10 eigenvalues nearest ω_Compton² and their eigenvectors. Matrix dimension at N=32 is ≈ `(4 + 3) · N³ = 7 · 32³ = 229,376` (4 K4-port amplitudes per node + 3 ω components per node), or `12 · N³ ≈ 393K` if including u-displacements; both tractable for sparse `eigsh`.

**Per geometry (R, r), the solver returns a discrete spectrum {ω_n(R, r)} with hybrid `(V_n, ω_n)` mode shapes.**

#### 3.1.1 Behavior at V=0 seed (load-bearing footnote per audit feedback)

Important caveat for the implementer: at a seed where V_inc = V_ref = 0 (the natural starting point — the seed only sets ω), **the cross-coupling blocks `C_Vω, C_ωV` vanish** because Op14 z_local is multiplicative in V (the term that couples Cosserat ω to V dynamics has factors of ∇V or V which are zero at V=0). The block matrix decouples:

```
  ┌  K_V(ω_seed)    0     ┐                    ┌  M_V    0   ┐
  │                       │ ψ  =  ω²           │             │ ψ
  └      0       K_ω      ┘                    └   0    M_ω  ┘
```

This is the **desired behavior** at V=0 seed: the eigsolve returns BOTH sector candidates simultaneously in one run.

- **V-block eigenmodes** at frequencies set by Cosserat-ω-modulated impedance — the "K4 wave on Cosserat cavity backdrop" framing per [doc 67_ §23.4](67_lc_coupling_reciprocity_audit.md#L1282).
- **ω-block eigenmodes** at frequencies set by Cosserat constitutive moduli (G, K, ρ_inertia) — the "Cosserat-sector bound state" framing per doc 66_ §17.2 three-storage-mode reading.

The three-mode falsification still works at V=0 seed; an additional sub-reading per eigenmode tells you **which sector** the bound state lives in (V-dominant / ω-dominant / mixed, where "mixed" at V=0 means near-degenerate eigenvalues across blocks rather than genuine cross-coupling).

**What block Helmholtz at V=0 seed CANNOT find:** genuinely hybrid `(V, ω)` eigenmodes that **require V ≠ 0 ∧ ω ≠ 0 simultaneously to exist as resonances** — i.e., modes where the Op14 cross-coupling is the load-bearing physics, not just a perturbation. Those would require V≠0 ∧ ω≠0 seeding (e.g., quadrature seed via [`tlm_electron_soliton_eigenmode.py:initialize_quadrature_2_3_eigenmode`](../../src/scripts/vol_1_foundations) at small V_amp). That investigation is a Round 8 question if R7.1 returns mode (III) at V=0 AND the Cosserat-only eigsolve returns the closest-to-ω_Compton candidate.

Block Helmholtz at V=0 thus answers a **strict superset** of what single-sector V Helmholtz answers (it returns the V-block AND the ω-block in one run), but not the full coupled-mode question. The fresh-session implementer should not expect block Helmholtz at V=0 to magically conjure hybrid modes — it exposes both sectors but doesn't probe their parametric coupling.

### 3.2 What the multi-seed sweep becomes

Original framing (doc 71_ §13): three discrete seeds, eigsolve at each, check if any returns eigenmode at ω_Compton.

Helmholtz framing: same three discrete seeds, BUT each seed's eigsolve returns a full local spectrum, AND the natural follow-up is sweeping (R, r) around each seed to map the resonance surface locally. So R7.1 has two layers:

- **Layer 1 (frozen pre-reg compatible):** discrete-seed eigsolve at GT_corpus, F17K_cos, F17K_s11, vacuum_control. Returns `{ω_n}` per seed. Three-mode falsification reads off whether any seed has ω_n = ω_Compton.
- **Layer 2 (extension, optional):** local (R, r) sweep around each discrete seed (e.g., ±10% in 5×5 grid). Returns `ω_n(R, r)` over a small patch. Reveals resonance-surface topology near each seed: is GT a saddle of the surface? A peak? A flat plateau?

Layer 1 is sufficient for the three-mode falsification. Layer 2 adds bandwidth/sensitivity diagnostics. **The pre-registration should commit to Layer 1 and treat Layer 2 as informational**, matching the earlier pattern of "headline pred is binary; informational diagnostics are reported separately."

### 3.3 Topological verification of the eigenmode

Original §13.4 used "shape correlation > 0.85 against doc 34_ X4a profile." Per Flag B that's over-strict because X4a is pre-coupling. Helmholtz framing replaces it with **topological crossing-count**:

```
c_eigvec = extract_crossing_count(V_n)        # winding number of mode shape
```

For the (2,3) electron eigenmode, `c_eigvec = 3`. For non-(2,3) modes (e.g., a (1,1) mode that lives in the same spectrum), `c_eigvec ≠ 3`. The crossing-count is topologically invariant under continuous deformation, so it's robust against coupling-induced shape distortion.

PASS criterion becomes: "eigenmode at ω_Compton ± α·ω_C with `c_eigvec = 3` and Q-factor extracted from boundary impedance within 5% of 1/α." Three orthogonal criteria, all directly observable from the eigsolve output.

**Two-tier addition per audit Q4:** keep shape correlation against doc 34_ X4a profile as **informational diagnostic** (>0.60 threshold for "matches X4a in spirit") alongside the binary `c_eigvec = 3` PASS criterion. Reasoning: `c_eigvec = 3` is necessary but not sufficient for "the (2,3) electron mode in the corpus-claimed sense" — other c=3 modes could coexist (different (p,q) combinations sharing winding, or near-degenerate mixing modes). Shape correlation surfaces "passes c=3 but suspicious" outcomes for adjudication rather than passing silently.

### 3.4 Sector-energy split diagnostic (per audit Q1)

For each eigenmode at ω_Compton (binary PASS), compute the energy partition between K4 V-sector and Cosserat ω-sector:

```
E_V = ψᴴ · M_V · ψ_V         # V-block energy
E_ω = ψᴴ · M_ω · ψ_ω         # ω-block energy
fraction_V = E_V / (E_V + E_ω)
fraction_ω = E_ω / (E_V + E_ω)
```

Three readings (informational, not PASS criterion):
- `fraction_V > 0.7`: V-dominant mode (K4 wave on Cosserat cavity backdrop). Helmholtz framing was correct; the bound state lives primarily in the K4 sector.
- `0.3 < fraction_V < 0.7`: hybrid mode (genuine V-ω co-evolution at this eigenvalue). At V=0 seed this likely means near-degenerate eigenvalues across V and ω blocks rather than true cross-coupling; the V≠0 follow-up sweep would confirm.
- `fraction_V < 0.3`: ω-dominant mode (Cosserat-sector bound state). The "where does the bound state live" question per doc 66_ §17.2 lands in the Cosserat sector.

This diagnostic IS the Q1 sector-energy split. Block Helmholtz on (V, ω) joint at V=0 seed produces this for free — no extra eigsolve, just energy partition of the returned eigenvector.

---

## 4. What's already in the corpus — reuse, don't reinvent

Layered by directness of reuse:

### 4.1 Direct code reuse (no modifications)

- [`cosserat_field_3d.py:initialize_electron_2_3_sector`](../../src/ave/topological/cosserat_field_3d.py#L777) — A26-corrected (2,3) hedgehog seeder. Sets cavity geometry. Used as-is.
- [`cosserat_field_3d.py:extract_shell_radii`](../../src/ave/topological/cosserat_field_3d.py#L1435) — (R, r) extraction from histogram of |ω|. Used for verification.
- [`cosserat_field_3d.py:extract_crossing_count`](../../src/ave/topological/cosserat_field_3d.py#L1468) — topological winding number. Used for `c_eigvec` check.
- [`vacuum_engine.py:VacuumEngine3D.from_args`](../../src/ave/topological/vacuum_engine.py#L1616) — A28+self-terms config. Used for Op14 z_local computation.
- [`universal_operators.py:universal_reflection`](../../src/ave/core/universal_operators.py) — Γ = (Z₂−Z₁)/(Z₂+Z₁). Used for Smith chart trajectory + cavity-wall check.
- [`coupled_s11_eigenmode.py`](../../src/scripts/vol_1_foundations/coupled_s11_eigenmode.py) F17-K methodology — S₁₁ at the eigenmode is automatic post-eigsolve cross-check. Already-converged endpoints (R/r=3.40, R/r=1.03) are the F17-K seed coordinates for layer-1 sweep.
- [AVE-VirtualMedia `generate_reflection_profile.py`](../../../AVE-VirtualMedia/scripts/generate_reflection_profile.py) — three-regime Γ visualization convention. Color/styling reused for 3D Smith chart consistency.

### 4.2 Code with small extensions

- [`k4_greens_function.py`](../../src/scripts/vol_1_foundations/k4_greens_function.py) — sparse K4 Laplacian (`scipy.sparse.lil_matrix` + `spsolve`). Currently solves `ΔG = δ` for Green's function. Extension: replace `spsolve` call site with `eigsh(H, sigma=ω_C², k=10)` for eigenmode mode. ~30 LOC delta, same Laplacian assembly.
- [AVE-HOPF `chiral_antenna_q_analysis.py:644-668`](../../../AVE-HOPF/scripts/chiral_antenna_q_analysis.py#L644) — 2D Smith chart plotting at fixed ω. Extension: animate over ω axis OR stack as 3D matplotlib `Axes3D` line plot. ~50 LOC delta.

### 4.3 Prose-only frameworks (now operationalized)

- [Doc 67_ §23.1-§23.4](67_lc_coupling_reciprocity_audit.md#L1282) — acoustic-cavity / Helmholtz framing. Present as methodology sketch; this doc 72_ + R7.1 implementation operationalize it.
- [Doc 03_ §4.3](03_existence_proof.md#L143) — topological quantization claim. Already validated empirically by F17-K v2-v2 and v3 (i); R7.1 will further test by checking if eigenmode at ω_Compton requires the topological-quantization geometry.
- [AVE-Propulsion `04_chiral_impedance_matching.tex`](../../../AVE-Propulsion/manuscript/vol_propulsion/chapters/04_chiral_impedance_matching.tex) — chiral impedance matching framework. Cross-repo prose, code stub only. Deferred to 4D Smith chart work.

### 4.4 Cross-repo concept loans (terminology hygiene)

- "Basin" comes from AVE-Protein / Ramachandran. **Not used in this doc except to disclaim.** vacuum-side analog is S₁₁-min (concept §1.4).
- "Smith chart" is direct EE loan, well-grounded. Use freely with explicit Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω specified.
- "TIR" (total internal reflection) is direct EE/optics loan, well-grounded. Bound-state condition Γ = -1 at cavity wall is the AVE statement of TIR.
- "Standing-wave eigenmode" is direct wave-physics loan, well-grounded.
- "Hessian-of-W" / "stationary point of W" / "energy minimum" — **avoid for vacuum bound states**. These are SM/QM-style concepts; the AVE substrate runs wave propagation, not energy minimization (concept §1.1).

---

## 5. What's genuinely new code for R7.1 (~290 LOC, single fresh-session)

Estimate before doc 72_ (per [§R7.1](.agents/handoffs/STAGE6_V4_HANDOFF.md#L885)): ~300 LOC for sparse Hessian + eigsh + boundary impedance Q + shape comparison.

Estimate after doc 72_ updates per audit accepted feedback: ~290 LOC. Block Helmholtz on (V, ω) joint adds ω-block assembly (~30 LOC vs single-sector V) but saves elsewhere (no jacrev autodiff, topological crossing-count reuses existing function). Net + Q1 energy-split diagnostic + Q4 shape correlation informational + Helmholtz-operator integrity check.

| Component | LOC est. | Reuses |
|---|---|---|
| `build_block_helmholtz_operator(engine, R, r)` — assemble sparse `(A, B)` matrices for (V, ω) joint | ~110 | `k4_greens_function.py` K4 Laplacian + `cosserat_field_3d.py` ω operator structure + `vacuum_engine.py` Op14 z_local |
| `eigensolve_block(A, B, omega_target, k=10)` — generalized `eigsh(A, M=B, sigma=ω_C²)` wrapper | ~30 | scipy.sparse.linalg |
| `extract_Q_from_boundary(V_n, omega_n, engine)` — Q-factor from boundary impedance | ~50 | `universal_reflection`, `extract_shell_radii` |
| `verify_topology(V_n, omega_n)` — c_eigvec check via `extract_crossing_count` (binary PASS) | ~10 | direct call |
| `compute_shape_correlation(V_n, omega_n)` — informational X4a-profile shape correlation (Q4 two-tier) | ~20 | doc 34_ X4a reference profile loader |
| `compute_sector_energy_split(psi, M_V, M_ω)` — V-sector / ω-sector energy fractions (Q1 diagnostic) | ~10 | numpy |
| `verify_operator_integrity(A, B)` — sanity check on block structure, BC enforcement, Hermiticity | ~10 | numpy/scipy |
| `multi_seed_sweep(seed_list)` — orchestrator | ~30 | itertools |
| `plot_3d_smith_chart(seeds, omega_grid)` — Extension A visualization | ~50 | matplotlib + AVE-HOPF Smith chart code |

Total ~290 LOC. Single fresh-session scope.

---

## 6. Pre-registration drafting + reframe-counting commitment

### 6.1 Commitment language (Rule 10 anchor — present in BOTH this doc and r8.8 manual entry)

**This is reframe 3 of R7.1 in one session arc:** single-seed Hessian (r8.5 forecast) → multi-seed Hessian (r8.7, frozen as `P_phase6_eigensolver_multiseed` at commit `c69e79c`) → multi-seed block Helmholtz on (V, ω) joint (this doc, proposed as `P_phase6_helmholtz_eigenmode_sweep`). Each reframe was substantive and corrected a real upstream error caught by audit or self-audit. None has been run.

**The fresh-session run committed against the v2 pred is committed to operator choice.** Per [COLLABORATION_NOTES Rule 10](.agents/handoffs/COLLABORATION_NOTES.md): *"empirical drivers catch what static analysis + preregistration misses; data first, methodology adjustments after."* If the run hits unexpected behavior, the discipline says: produce empirical data first, analyze the data, then methodology revisions if needed — not pre-emptive reframe 4.

**The ONLY pre-emptive operator-change condition before run:** catastrophic methodology error surfaced by audit or external review. "Catastrophic" means: a load-bearing physics error in the operator construction itself that would invalidate any result regardless of what data the run produces. Anything less than that goes through the empirical-data-first pipeline.

This commitment is the Rule 10 anchor for R7.1 and lands in both this doc 72_ §6 AND in the r8.8 manual entry §13.5l so the fresh-session implementer hits it twice.

### 6.2 Pre-registration `P_phase6_helmholtz_eigenmode_sweep` (replaces `P_phase6_eigensolver_multiseed`)

Specific changes from current frozen pred:

1. **Methodology field** — change from "linearize coupled K4+Cosserat dynamics around each seed ansatz, build sparse generalized-eigenvalue Jacobian" to "build block Helmholtz operator on joint (V, ω) state per §3.1, with Op14-modulated impedance set by Cosserat ω-seed; eigsh on the generalized block eigenvalue problem at sigma=ω_Compton²." (Hessian-of-W approach retired per concept §1.1.)
2. **Seed treatment** — same four seeds (GT_corpus, F17K_cos, F17K_s11, vacuum_control), reframed as "cavity-geometry-defining ansatz" not "linearization seed." V=0 at seed; block Helmholtz at V=0 decouples per §3.1.1, returning V-block AND ω-block eigenmodes simultaneously.
3. **PASS criteria** — `(ω, Q, c_eigvec)` binary tier; **shape correlation > 0.60 informational tier** (Q4 two-tier per audit). Topological crossing-count `c_eigvec = 3` replaces shape correlation as binary criterion; shape correlation retained as informational.
4. **Sector-energy split diagnostic** — Q1 sub-diagnostic per §3.4. Reports V-fraction / ω-fraction per eigenmode found at ω_Compton. Informational, not PASS.
5. **Three-mode resolution** — same as `P_phase6_eigensolver_multiseed`, with new sub-reading on "which sector did the eigenmode come from" (V-dominant / hybrid / ω-dominant).
6. **Lattice geometry** — N=32, R_anchor=10 retained.
7. **Optional Layer 2 informational** — local (R, r) sweep around each discrete seed for resonance-surface topology. Not part of headline PASS.

### 6.3 Why this pred should not retract

Stated honestly to set expectations:

- Concept §1.1 (block Helmholtz, not Hessian) eliminates the Flag A class of issue and the hybrid-coupled-mode pushback that Flag A set up.
- Concept §1.4 (no W-basin language) eliminates the Rule-6/8 framing class of issue.
- Concept §2.1 (3D Smith chart Extension A) gives the AVE-native visualization for the multi-seed sweep.
- Concept §1.2 (S₁₁ cross-check at the eigenmode) makes F17-K v2-v2 result confirmatory data.
- §3.1.1 V=0 footnote lands the "block Helmholtz answers a strict superset, not the hybrid coupled question" caveat *in the methodology doc* so the fresh-session implementer doesn't expect more from V=0 eigsolve than it can deliver.

The v2 pred's failure modes are now concrete and bounded: empirical (mode I/II/III readings) rather than methodology (operator-choice error). Per §6.1 commitment, post-run methodology iteration is allowed; pre-run isn't.

---

## 7. Connection to broader Stage 6 / Round 7

If R7.1 lands cleanly under this design space:
- **Mode (I) result** → corpus GT vindicated; R7.2 ((2,3)/Hopf injection per G-13) runs at GT cavity geometry; Round 7 closes.
- **Mode (II) result** → engine basin at F17-K endpoint; corpus geometry derivation revisited (likely surfaces a coupled-vs-Cosserat-only discrepancy in [doc 34_ §9.4](34_x4_constrained_s11.md) X4a/X4b); Round 7 closes after corpus revision.
- **Mode (III) result** → no eigenmode at ω_Compton at any tested geometry; Round 8 architectural rework. Likely first question: is the bound state in the K4 V-sector, the Cosserat ω-sector, or coupled across both? Helmholtz framing makes this explicitly answerable via per-sector eigenmode amplitude analysis.

R7.2 (topological pair injection per [doc 70_ §7.6](70_phase5_resume_methodology.md)) is unaffected by this design-space reframe — its question is about whether (2,3) torus-knot or Hopf fibration injection profile persists under Cosserat self-dynamics, regardless of where in (R, r) the pair is placed. R7.2 still needs `P_phase5_topological_injection` pre-registration. Can run in parallel with R7.1.

The 4D Smith chart extension (chirality axis) becomes load-bearing for any parity-violation work and for the chiral-pair-injection refinement of R7.2. Deferred to post-R7.1.

---

## 8. Sign-off resolution (closed via audit + Grant directives 2026-04-25)

All five original sign-off questions resolved via audit feedback. Resolution recorded here for the audit trail; this doc 72_ now lands as the active design-space reference for R7.1 v2 pre-registration.

| Question | Resolution |
|---|---|
| Q1 Helmholtz vs Hessian-of-W | **Closed: block Helmholtz on (V, ω) joint** per §3.1. Hessian-of-W retired. Audit pushback on hybrid coupled modes addressed by block formulation; Q1 energy-split diagnostic per §3.4 reads off "which sector" the eigenmode came from. §3.1.1 footnote documents V=0 decoupling and what block Helmholtz can / cannot find. |
| Q2 Retire "basin" for vacuum | **Closed: yes.** Terminology in this doc and v2 pred uses "resonance surface" / "S₁₁-min" / "Helmholtz eigenmode" / "topological-quantization point." [COLLABORATION_NOTES Rule 6](.agents/handoffs/COLLABORATION_NOTES.md) gains a strengthening line on wave-substrate vs minimization-substrate language (per audit suggestion: framed as Rule 6 instance, not new rule). |
| Q3 3D Smith chart Extension A primary | **Closed: yes.** `(Re(Γ), Im(Γ), ω)` is the EE-natural extension; TIR-at-Γ=-1 directly readable. Extensions B (A² saturation-trajectory) and C ((R, r) geometry-trajectory) retained as supplementary diagnostics. AVE-HOPF Smith chart code reuse path clean. |
| Q4 Topological crossing-count vs shape correlation | **Closed: two-tier.** `c_eigvec = 3` binary PASS criterion; shape correlation > 0.60 informational diagnostic. Cheap insurance against "passes c=3 but suspicious shape" outcomes (degenerate mixing, alternative (p,q) modes sharing winding). Per §3.3 + §3.4. |
| Q5 ~250 LOC scope | **Closed: ~290 LOC** with Q1 energy-split diagnostic (~10 LOC) + Q4 shape correlation informational (~20 LOC) + Helmholtz operator integrity check (~10 LOC) added. Single fresh-session. Per §5. |

**Methodology meta-concern (audit, not in original Q's):** addressed in §6.1 with explicit reframe-3 commitment language. Implementer hits the commitment in both this doc and the r8.8 manual entry §13.5l.

The frozen pre-reg `P_phase6_eigensolver_multiseed` (commit `c69e79c`) retracts per Rule 12 in the same commit unit as this doc 72_'s landing — replaced by `P_phase6_helmholtz_eigenmode_sweep` with §6.2 specifications.

---

## 9. §6.1 catastrophic-error carve-out invocation (on-record, 2026-04-25)

**Reframe-3 framing (this doc §1-§8) is RETRACTED.** Per §6.1 catastrophic-error carve-out, with explicit Grant approval on-record.

### 9.1 Trigger

Self-audit during reframe-3 driver smoke test, triggered by Grant pulse-check ("are you being an AVE engineer?", 2026-04-25). Identified that the V-block operator constructed in `r7_helmholtz_eigenmode_sweep.py` (commit `675141e`) is a **continuum-limit graph Laplacian approximation**, NOT the discrete K4-TLM scatter+connect transmission operator that K4-TLM actually implements at finite N.

### 9.2 §6.1 carve-out criteria — met

Per [§6.1 commitment language](#61-commitment-language-rule-10-anchor--present-in-both-this-doc-and-r88-manual-entry): catastrophic methodology error = "load-bearing physics error in operator construction itself that would invalidate any result regardless of what data the run produces."

Met because at N=32 the continuum-vs-discrete corrections are O((10/32)²) ≈ 10%, which is ~14× the PASS tolerance (α ≈ 0.7%). Mode (III) under graph Laplacian could be misread as "Round 8 architectural rework" when actual cause is "continuum approximation finds modes that don't lift to K4-TLM scatter+connect." See [doc 73_ §1.2](73_discrete_k4_tlm_lctank_operator.md) for full reasoning.

### 9.3 Grant approval

> *Grant 2026-04-25: "confirmed 6.1"*

First §6.1 invocation in Round 7. On-record per auditor recommendation so future audits can verify the carve-out is not becoming a routine escape valve from Rule 10's "data first, methodology after" commitment.

### 9.4 Successor doc

[Doc 73_](73_discrete_k4_tlm_lctank_operator.md) articulates the discrete K4-TLM scatter+connect operator + Cosserat (u, ω) LC-tank Hessian-of-W operator + Op14 cross-coupling at full mathematical detail per auditor's 4-part spec. No new pre-registration in this doc 72_ or doc 73_; pred follows after doc 73_ §1-§5 sign-off.

### 9.5 What stays valid in doc 72_

Doc 72_ §1.1-§1.4 (four AVE-native concepts: wave eigenmode / impedance match / topological quantization / S₁₁-min not W-min) are correct. The conceptual layer was right; the operator-syntax layer (§3.1's `∇·(z(x)·∇V) + k²V = 0` continuum form) was wrong. Doc 73_ keeps the §1.1-§1.4 conceptual framework and replaces the §3.1 operator construction with a discrete K4-TLM scatter+connect formulation.

§2 (3D Smith chart for the vacuum, Extension A `(Re(Γ), Im(Γ), ω)`) also stays valid as the AVE-native visualization for R7.1, just with the discrete-operator interpretation: Γ is computed via `S(z_local)` boundary impedance match, ω is read off the eigenvalue phase `arg(λ) = ω·dt`, and resonance surface in (R, r, ω) volume is mapped via discrete eigsolve rather than continuum eigsolve.

### 9.6 Reframe-5 escalation discipline

Per [doc 73_ §6.1](73_discrete_k4_tlm_lctank_operator.md): a SECOND §6.1 invocation in Round 7 must be paired with formal verification / independent operator-math review before any further code. The first invocation (this one, doc 73_) lands the discrete-operator math at the correct layer; reframe 5 if it surfaces would require heavier scaffolding.

---

*§9 added 2026-04-25 — §6.1 catastrophic-error carve-out invocation on-record per Grant approval. Reframe-3's V-block continuum-Laplacian approximation identified as load-bearing physics error in operator construction. Successor: doc 73_. §1.1-§1.4 conceptual framework retained; §3.1 operator-syntax layer superseded by discrete K4-TLM scatter+connect formulation in doc 73_.*

---

*Doc 72_ written 2026-04-25 — design-space articulation precursor to R7.1 pre-registration. Closes the depth-of-understanding gap that produced three pre-reg retractions earlier in this session. §1 names the four AVE-native concepts (wave eigenmode / impedance match / topological quantization / S₁₁-min not W-min). §2 articulates the 3D Smith chart for the vacuum (three natural extensions; Extension A `(Re(Γ), Im(Γ), ω)` recommended for R7.1; 4D chirality flagged for later). §3 maps R7.1 to Helmholtz wave-eigenmode framing (RETRACTED §9; superseded by doc 73_ discrete K4-TLM operator). §4 inventories corpus tools to reuse. §5 estimates ~250 LOC for fresh-session implementation. §6 defers next pre-registration pending §1-§5 sign-off. §8 collects sign-off questions for Grant. §9 records §6.1 catastrophic-error carve-out invocation on-record per Grant approval. Cross-repo references: AVE-HOPF Smith chart (chiral_antenna_q_analysis.py:644), AVE-VirtualMedia three-regime Γ (generate_reflection_profile.py), AVE-Protein TDI canonical (protein_fold.py:260-326).*
