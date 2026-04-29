# 90 — Round 11 (vi) Stride 3: Discrete Beltrami Eigenmode on Chair-Ring + 1-Step K4 Neighborhood

**Status:** implementer-drafted, 2026-04-29. Stride 3 analytical work per [doc 89 §7.4](89_round_11_vi_stride_2_topological_mismatch.md#74--updated-stride-3-plan) updated plan (post-Grant-pushback corrections).

**Scope:** numerical solution of the discrete Beltrami eigenvalue problem ∇×A = k·A on the chair-ring + 1-step K4 neighborhood (18 nodes, 54 DOF). Output: eigenvalue spectrum + top ring-localized eigenvector for v9 IC construction.

**Verdict:** discrete spectrum's most ring-localized mode at **k_disc ≈ 1.56 in 1/ℓ_node units (84% ring localization)** — substantively different from continuum (1,1) prediction k_cont ≈ 6.36. The 4× gap confirms the discretization-density issue from doc 89 §7.3. Closest discrete mode to Compton frequency k=1 is at k=0.84 (16% below), but that mode has lower ring localization. **No discrete eigenmode lies exactly at Compton frequency at the chair-ring scale.**

---

## §1 — Setup

### §1.1 — Subgraph

Chair-ring + 1-step K4 neighborhood: 18 K4-active nodes total.

| Index | Sublattice | Position | Role |
|---|---|---|---|
| 0 | A | (0, 0, 0) | ring |
| 1 | B | (1, 1, 1) | ring |
| 2 | A | (0, 2, 2) | ring |
| 3 | B | (-1, 3, 1) | ring |
| 4 | A | (-2, 2, 0) | ring |
| 5 | B | (-1, 1, -1) | ring |
| 6 | B | (1, -1, -1) | 1-step neighbor of n=0 (port 1) |
| 7 | B | (-1, -1, 1) | 1-step neighbor of n=0 (port 3) |
| 8 | A | (2, 0, 2) | 1-step neighbor of n=1 (port 2) |
| 9 | A | (2, 2, 0) | 1-step neighbor of n=1 (port 3) |
| 10 | B | (1, 3, 3) | 1-step neighbor of n=2 (port 0) |
| 11 | B | (-1, 1, 3) | 1-step neighbor of n=2 (port 3) |
| 12 | A | (-2, 4, 2) | 1-step neighbor of n=3 (port 1) |
| 13 | A | (0, 4, 0) | 1-step neighbor of n=3 (port 3) |
| 14 | B | (-3, 3, -1) | 1-step neighbor of n=4 (port 2) |
| 15 | B | (-3, 1, 1) | 1-step neighbor of n=4 (port 3) |
| 16 | A | (-2, 0, -2) | 1-step neighbor of n=5 (port 0) |
| 17 | A | (0, 2, -2) | 1-step neighbor of n=5 (port 3) |

Total bonds in subgraph: 18 (6 ring-ring chair-ring bonds + 12 ring-out-of-ring poloidal bonds).

### §1.2 — Discrete curl operator

For tetrahedral 4-port K4 nodes, derived analytically using `Σ ê_i ⊗ ê_i = (4/3)·I`:

```
(∇×A)_n = (3/4) Σ_i ê_i × (A_neighbor_i - A_n) / bond_length
```

where:
- ê_i are the 4 K4 port unit vectors at node n (with sign flip for B-sites)
- bond_length = √3·ℓ_node (tetrahedral diagonal)
- A_neighbor_i = 0 if neighbor is outside the 18-node subgraph (Dirichlet boundary)

Verification in continuum limit:
- Σ_i ê_i^a ê_i^b = (4/3)·δ_ab for tetrahedral 4 ports → recovers continuum ∇×A
- (3/4) factor inverts the (4/3) sum normalization

### §1.3 — Eigenvalue problem

`M·A = k·A` where M is the (3×N_total)·(3×N_total) curl matrix. For 18 nodes: M is 54×54.

Numerical findings:
- M is **symmetric** (verified via `np.allclose(M, M.T)`)
- Eigenvalues are real (consistent with symmetric M and standard ∇× being formally Hermitian under L² inner product with Dirichlet boundary)
- 7.4% nonzero (sparse)
- 54 eigenvalues found

---

## §2 — Eigenvalue spectrum

### §2.1 — Top 20 eigenvalues (sorted by magnitude)

In 1/bond_length units (multiply by √3 ≈ 1.732 to convert to 1/ℓ_node units):

| Rank | λ (signed) | \|λ\| | k in 1/ℓ_node units |
|---|---|---|---|
| 0 | +0.9001 | 0.9001 | 1.559 |
| 1 | -0.9001 | 0.9001 | 1.559 |
| 2 | +0.9001 | 0.9001 | 1.559 |
| 3 | -0.9001 | 0.9001 | 1.559 |
| 4-7 | ±0.8595 | 0.8595 | 1.489 |
| 8-11 | ±0.8090 | 0.8090 | 1.401 |
| 12-15 | ±0.7409 | 0.7409 | 1.283 |
| 16-19 | ±0.4865 | 0.4865 | 0.843 |

**Eigenvalue spectrum top: 0.9001 in 1/bond_length units = 1.559 in 1/ℓ_node units.**

Multiple modes are degenerate (4× at each magnitude) — consistent with chiral symmetry of the chair-ring + K4 neighborhood (CW/CCW × 2 polarization directions per ±k).

### §2.2 — Comparison to continuum (1,1) Beltrami prediction

**Continuum prediction at corpus geometry (R=ℓ_node, r=ℓ_node/(2π)):**
```
k_cont² = (1/r)² + (1/R)² = (2π)² + 1² ≈ 40.5
k_cont = √(40.5) ≈ 6.36 in 1/ℓ_node units
```

**Discrete spectrum max: 1.56 in 1/ℓ_node units.**

**Ratio: continuum / discrete = 6.36 / 1.56 ≈ 4.07.**

The continuum (1,1) prediction is **4× above** the highest discrete eigenvalue. There is NO discrete eigenmode at k=6.36; the chair-ring + 1-step K4 spectrum tops out at k=1.56.

This is consistent with the doc 89 §7.3 sub-Nyquist finding: chair-ring at K4 sampling density cannot represent the (1,1) Beltrami mode in the continuum sense. The discrete spectrum's modes are physically distinct objects from the continuum (1,1) mode at corpus geometry.

### §2.3 — Comparison to Compton frequency

**Compton frequency k_C = 1 in 1/ℓ_node units.**

**Closest discrete eigenvalues to k_C:**
- |λ|=0.4865 → k=0.843 in 1/ℓ_node units (16% below k_C)
- |λ|=0.7409 → k=1.283 in 1/ℓ_node units (28% above k_C)
- |λ|=0.8090 → k=1.401 in 1/ℓ_node units (40% above k_C)

**No discrete eigenvalue is exactly at k=1.**

This matters for the framework's claim "trapped photon at Compton frequency = Beltrami eigenmode." If the curl-operator eigenvalue must equal the dispersion wavenumber (free-wave dispersion ω=k·c), then the Compton-frequency Beltrami eigenmode doesn't exist on the chair-ring + 1-step K4 substrate. Either:

- (a) The framework's "Beltrami at Compton frequency" identification is wrong (per doc 88 §2.5: dispersion vs curl-eigenvalue distinction)
- (b) The chair-ring + 1-step K4 substrate is too coarse (per doc 89 §7.3 sub-Nyquist)
- (c) The corpus electron lives at a different mode (k=1.56 most localized, NOT k=1)

---

## §3 — Top ring-localized eigenmode (for v9 IC)

### §3.1 — Mode selection

Most ring-localized mode: **λ = +0.9001, ring_localization = 0.842, k = 1.559 in 1/ℓ_node units.**

This mode has the highest fraction of |A|² localized at the 6 chair-ring nodes vs the full 18-node subgraph. 4-fold degenerate (±0.9001 × 2 chiral copies). Picking one representative.

### §3.2 — Eigenvector A_0 structure

**At ring nodes (real part):**

| n | sublattice | position | A_0 (3D vector) | \|A_0\| |
|---|---|---|---|---|
| 0 | A | (0, 0, 0) | (+0.000, -0.035, -0.207) | 0.210 |
| 1 | B | (1, 1, 1) | (-0.026, -0.029, -0.182) | 0.186 |
| 2 | A | (0, 2, 2) | (+0.157, +0.316, +0.080) | 0.362 |
| 3 | B | (-1, 3, 1) | (-0.365, +0.112, +0.301) | 0.486 |
| 4 | A | (-2, 2, 0) | (+0.115, -0.364, +0.317) | 0.496 |
| 5 | B | (-1, 1, -1) | (+0.330, +0.183, +0.086) | 0.387 |

**At out-of-ring 1-step neighbors:** |A_0| ranges 0.075 to 0.179 (smaller than ring magnitudes).

**Mean amplitudes:**
- Ring: 0.355
- Out-of-ring: 0.108
- Ring/out-of-ring ratio: 3.27

### §3.3 — Substantive structural observations

1. **Non-uniform ring amplitudes.** |A_0| varies from 0.19 to 0.50 across the 6 ring nodes — factor 2.6× variation. Specifically n=3 and n=4 have ~2.5× the amplitude of n=0 and n=1. This is **not** the v6/v7/v8 IC's uniform amplitude with cos/sin spatial PHASE pattern. The discrete eigenmode has a specific spatial AMPLITUDE structure that doesn't match the traveling-wave IC class.

2. **Non-zero out-of-ring contribution.** ~16% of energy at 12 out-of-ring 1-step neighbors. v6/v7/v8 IC zeroed these. The proper eigenmode has small but non-zero poloidal extension into the K4 neighborhood.

3. **Spatial localization with sub-lattice "tube"**: ring 84%, 1-step neighbors 16%, total at chair-ring + 1-step neighborhood 100%. The eigenmode IS spatially localized but extends one lattice spacing into the surrounding K4.

4. **Chiral degeneracy 4×.** Eigenvalues come in pairs ±0.9001 with each having 2 degenerate eigenvectors. This corresponds to 2 chiralities (CW/CCW around the ring) × 2 polarization directions per chirality. v9 IC must pick one specific eigenvector (electron, not positron, with one polarization handedness).

---

## §4 — v9 IC specification (per Stride 3 output)

### §4.1 — IC structure

For each of the 18 nodes (6 ring + 12 out-of-ring 1-step), set V_inc + Phi_link + Cosserat ω per the eigenvector A_0 spatial pattern.

**At each node n:**
- A_0(n) is a specific 3D vector from the eigenmode (per §3.2)
- V_inc[node n, port p] = projection of -∂A_0/∂t onto port direction × bond_length normalization
- Phi_link[A_site_n, port p] = projection of A_0(midpoint of bond_p) onto bond direction × bond_length
- Cosserat ω[node n] = k · A_0(n) (Beltrami: B = ∇×A = k·A, parallel to A)

### §4.2 — Time-phase choice

Per doc 86 §3.4 + doc 87 §3.4: Phase A IC (V_inc=0) is engine-incompatible. Use **Phase B**: V_inc at peak (E=peak), Phi_link=0 (zero crossing of ∫E dt), Cosserat ω=0 (B=zero crossing).

For Phase B at IC time:
- V_inc[node, port] = ω·A_0·port_dir·bond_length (E = -∂A/∂t at peak; ω is time-domain rest-mass frequency)
- Phi_link = 0 (start of integration)
- Cosserat ω = 0 (B at zero crossing)

Engine evolves: at later time T/4, E reaches zero crossing while A and B reach peak.

### §4.3 — Eigenvalue identification: which k for the corpus electron?

**Three candidates from the discrete spectrum:**

(a) **Most ring-localized: k = 1.56 in 1/ℓ_node units.** Mass would be 1.56·m_e — NOT corpus electron mass. Could be an excited state or non-physical mode.

(b) **Closest to Compton: k = 0.84 in 1/ℓ_node units.** Mass 0.84·m_e — also not corpus electron, but close. Lower ring localization (~67%).

(c) **Compton frequency exactly: k = 1 — DOES NOT EXIST in discrete spectrum.** No eigenmode at k=1.

**Open question:** which eigenvalue identifies the corpus electron at K4 chair-ring scale? If the framework requires Compton frequency exactly, the discrete spectrum doesn't host the corpus electron. If the framework allows the curl eigenvalue to differ from Compton (per dispersion-vs-curl-eigenvalue distinction in doc 88 §2.5), one of (a) or (b) is the candidate.

This is a Rule 16 plumber-physics question for Grant adjudication.

---

## §5 — Resolution candidate adjudication (per doc 88 §2.4 + doc 89 §2)

Stride 3 results adjudicate the candidates:

**(1) Continuum formula doesn't apply to discrete K4** — **CONFIRMED EMPIRICALLY.** Continuum k_cont = 6.36 NOT in discrete spectrum. The 4× gap is too large to be just a small discretization correction. Either (1,1) Beltrami doesn't transfer to K4 chair-ring at all, or transfers to a fundamentally different mode at lower k.

**(2) Corpus electron isn't (1,1)** — **POSSIBLE.** The discrete spectrum has multiple candidate modes (k = 0.84 to 1.56). The corpus electron at K4 scale might correspond to one of these (NOT the continuum (1,1) projection).

**(3) Dispersion vs curl eigenvalue distinction** — **STRONG.** No discrete eigenmode at Compton frequency k=1. If framework requires k_curl = ω/c, no Beltrami mode exists at K4 chair-ring scale. If framework allows them to differ, the corpus electron lives at one of the discrete eigenvalues with rest mass coming from total stored energy independent of curl k.

**(4) R, r values aren't ~(1, 1/(2π))** — **STRONG.** The continuum (1,1) at R/r=2π isn't where the discrete chair-ring lives. Effective R/r at K4 sampling is determined by the discrete eigenvalue, not by continuum-inferred R, r values.

**(5) Beltrami isn't load-bearing in (p,q) sense** — **CONFIRMED.** Vol 1 Ch 3:402's "Beltrami on chiral K4 graph" is the canonical statement. The discrete K4 chair-ring + 1-step neighborhood DOES have Beltrami eigenmodes (real eigenvalues of symmetric ∇× operator), but they're discrete-graph eigenmodes, not continuum (p,q) torus eigenmodes.

---

## §6 — Open questions for Grant + auditor adjudication (Rule 16)

**Q1 — Which discrete eigenvalue identifies the corpus electron?**
Three candidates: k=1.56 (most ring-localized), k=0.84 (closest to Compton), or k=1 (doesn't exist exactly in discrete spectrum). The framework's "trapped photon at Compton frequency" identification needs reconciliation with the discrete spectrum.

**Q2 — Is the discrete-eigenmode rest mass = ℏ·k·c, or determined by total stored energy independent of k?**
For free EM waves: rest mass would scale linearly with k. For trapped Beltrami eigenmodes: rest mass might equal m_e·c² regardless of k (set by IC amplitude and saturation), with k determining the spatial mode structure only. This is the dispersion-vs-curl-eigenvalue distinction from doc 88 §2.5.

**Q3 — v9 IC at k=1.56 (most ring-localized) — should it be tested even if k ≠ Compton?**
Stride 3 found the discrete eigenmode is at a non-Compton-frequency k. If v9 tests this mode and the trapped state forms with persistence + localization + Beltrami parallelism, what does it mean? Confirms (1,1)-class Beltrami at non-Compton k, OR confirms the framework needs reframing on the Compton-frequency claim.

**Q4 — Is the framework's substrate-native scale m_e·c² actually equal to ℏ·c·k_eigenvector, or independent of k?**
This is the deepest physics question. If k_eigenvector = k_Compton is required for corpus identification, the chair-ring at K4 doesn't host the corpus electron (no k=1 mode). If k can be different (mass from other source), v9 at k=1.56 is a valid test.

---

## §7 — Stride 4 plan (deferred)

Per "appropriate strides to maintain rigor": Stride 3 outputs the eigenmode + v9 IC spec. Stride 4 = v9 driver implementation + run.

1. **Pause for Grant adjudication on Q1-Q4 above** OR proceed with provisional Q1=k=1.56 reading.

2. **Implement v9 driver** using the §4.1 IC spec on the chair-ring + 1-step K4 neighborhood.

3. **Run v9 at T=0** with the corrected Phase B IC + non-Compton k value.

4. **Adjudicate per doc 86 §7.4 4-criterion gate** (persistence + ring localization + Beltrami parallelism + loop flux).

5. **If Mode I:** Beltrami trapped state at corpus-canonical scale empirically confirmed (at the discrete eigenmode k value, not continuum (1,1)). doc 83/85/86/87 amendments documenting the result + framework refinement on Compton frequency identification.

6. **If Mode II/III:** Round 11 (vi) doesn't close cleanly even with corrected IC. Move to secondary candidates ((i) finer-than-K4 substrate, (ii) multi-loop, (iii) topology variant).

---

## §8 — Compliance check

**Manuscript-canonical:**
- [Vol 1 Ch 3:402](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex#L402) Beltrami standing wave on chiral K4 graph ✓
- All v6/v7/v8 manuscript citations carry forward

**Synthesis (this stride):**
- Discrete curl operator derivation: standard finite-difference discretization on tetrahedral K4
- 18-node subgraph + Dirichlet boundary: implementer choice for tractable analytical work
- Eigenvalue identification (which k = corpus electron): pending Grant adjudication per Q1-Q4

**Numerical verification:**
- Discrete curl matrix M: symmetric ✓ (standard ∇× behavior under L² inner product with Dirichlet BC)
- Sparse: 7.4% nonzero ✓
- 54 real eigenvalues found ✓
- 4-fold degeneracy at top eigenvalue 0.9001 ✓ (consistent with chiral symmetry)

---

## §9 — References

- [Doc 87](87_path_alpha_v8_round_11_ignition.md), [Doc 88](88_round_11_vi_stride_1_a43_v14.md), [Doc 89](89_round_11_vi_stride_2_topological_mismatch.md) — Round 11 (vi) Strides 1-2
- Driver: [`r10_round_11_vi_chair_ring_eigenmode.py`](../../src/scripts/vol_1_foundations/r10_round_11_vi_chair_ring_eigenmode.py)
- Result: [`r10_round_11_vi_chair_ring_eigenmode_results.json`](../../src/scripts/vol_1_foundations/r10_round_11_vi_chair_ring_eigenmode_results.json)
- [`COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) Rule 14, Rule 16, A40, A43 v2
