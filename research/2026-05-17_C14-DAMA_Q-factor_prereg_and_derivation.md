# C14-DAMA Q-Factor (per-event detection probability) — Prereg + Derivation

> **🔴 PAUSED 2026-05-17 night — audit walk-back triggered before derivation execution.**
>
> The pre-derivation discrimination-check ([dispatched agentId a070b9030be6eefd1] in parallel with this prereg) caught three load-bearing issues that block the Q-factor derivation as scoped: (i) Ca Kα at 3.691 keV is a 1% Moseley-law coincidence with α m_e c² = 3.728 keV; (ii) SM cosmic-X-ray-background photoabsorption gives same OOM as DAMA observed rate; (iii) 52-OOM Q-factor closure would require ~22 powers of α from independent axiom invocations with corpus providing one canonical chain.
>
> Q-factor derivation work is PAUSED pending anti-anchor framework + substrate-mode-density foundational work. The Z-independence + CMB-velocity phase-lock + solid-vs-liquid binary gate (genuinely AVE-distinct claims that survive the audit) are documented in source leaf [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) §11. Full walk-back audit trail at [`research/2026-05-17_C14-DAMA_audit_walk-back.md`](2026-05-17_C14-DAMA_audit_walk-back.md).
>
> This document is preserved as historical artifact of the work that triggered the audit. The structural form sections below (§0 prereg framework, §3 required suppression magnitude calculation) remain analytically correct but their physical interpretation is rendered inadmissible by the audit findings (Ca Kα coincidence + CXB OOM match + 22-α-power gap).

**Status:** PAUSED 2026-05-17 night per audit walk-back. ORIGINAL FRAMING (pre-audit): single-parameter closure attempt on the DAMA rate magnitude gap identified at [`research/2026-05-17_C14-DAMA_amplitude_result.md:125-137`](2026-05-17_C14-DAMA_amplitude_result.md).

**Date:** 2026-05-17 night
**Matrix row:** C14-DAMA-MATERIAL (rate magnitude U-D pending)
**Prior chain:** [`research/2026-05-17_C14-DAMA_amplitude_prereg.md`](2026-05-17_C14-DAMA_amplitude_prereg.md) → [`research/2026-05-17_C14-DAMA_amplitude_result.md`](2026-05-17_C14-DAMA_amplitude_result.md) (energy + modulation closed via α-slew) → THIS DOC (rate magnitude)
**Pre-audit corpus-grep:** agentId a3d1372d5d9c02578 — NO prior Q-factor derivation exists; structural ingredients present; gap explicitly named single-parameter target

## §0 — Pre-registered claim before computation

### Derivation target

Derive the dimensionless per-event detection probability $\epsilon_{det}$ (loosely called the "Q-factor" in [`dama-alpha-slew-derivation.md:85-93`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md)) such that

$$R_{DAMA} = R_{intrinsic} \times \epsilon_{det}$$

where $R_{intrinsic}$ is the canonical AVE-substrate intrinsic α-slew event rate in NaI, and $R_{DAMA}$ is the observed integrated rate of $\sim 4.6 \times 10^{-7}$ events/s/kg in the 2-6 keV window.

### Physical picture (mechanical / topological)

1. **Source mechanism**: every atomic electron in NaI is a Cosserat unknot soliton whose ground state undergoes intrinsic α-slew Schwinger oscillation at $\nu_{slew} = \alpha c / (2\pi \ell_{node}) \approx 9.02 \times 10^{17}$ Hz. This is the same physics that produces the electron's anomalous moment $a_e = \alpha/(2\pi)$ — canonical at [`simulate_g2.py`](../src/scripts/vol_2_subatomic/simulate_g2.py).
2. **Detection topology**: the α-slew oscillation modulates the local electron-substrate coupling at amplitude $E_{slew} = \alpha m_e c^2 = 3.728$ keV. **Most** of these modulations average to zero on detection timescales — the unknot returns to its ground state without depositing energy into the K-shell binding. **Rare** events couple coherently to a NaI atomic K-shell electron and deposit the full quantum, producing a 3.728 keV scintillation pulse.
3. **Detection probability per α-slew event**: the rare-coupling probability $\epsilon_{det}$ has structural form set by the cascade of substrate-matter coupling steps. Candidate factors:
   - $\kappa_{crystal} = \rho_{NaI}/\rho_{bulk} \approx 4.63 \times 10^{-4}$ (canonical mass-density coupling per [`research/2026-05-17_C14-DAMA_amplitude_prereg.md:61`](2026-05-17_C14-DAMA_amplitude_prereg.md))
   - $\Phi_A = \alpha^2$ per substrate-matter crossing (canonical lattice porosity per [`optical-refraction-gravity.md:46`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md))
   - $a_e = \alpha/(2\pi)$ per Schwinger-class coupling step (canonical [`dama-alpha-slew-derivation.md:33-42`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md))
   - Coherent baseline enhancement $N_{coh}^2$ for crystalline-lattice coupling
4. **Substrate length scale**: $\lambda_{slew} = 2\pi \ell_{node}/\alpha \approx 3.32 \times 10^{-10}$ m (atomic, NOT nuclear; corpus correction at [`research/2026-05-17_C14-DAMA_amplitude_result.md:127`](2026-05-17_C14-DAMA_amplitude_result.md))
5. **Coupling endpoint**: NaI K-shell binding for ionization or atomic-electron-recoil for elastic scattering (energy deposit ≥ 2 keV per DAMA's lower-edge threshold)

### Expected structural form

The natural AVE-substrate form for $\epsilon_{det}$ is

$$\epsilon_{det} = \kappa_{crystal} \times (\text{coupling-cascade suppression})$$

The coupling-cascade suppression is expected to take the form $\alpha^N$, $(\alpha/(2\pi))^N$, $\Phi_A^N$, or some combination, with $N$ set by the topological-count of substrate-matter crossings in the detection chain. **The prediction is that $N$ has a structural meaning, NOT an arbitrary fit parameter.**

### Pre-registered prediction: required suppression magnitude

Required $\epsilon_{det} = R_{DAMA} / R_{intrinsic}$. Both sides are computed independently from canonical AVE quantities; their ratio is the suppression magnitude that any structural derivation must reproduce.

### Discriminating outcomes

- **Outcome A (full closure)**: natural single AVE-structural form (e.g., $\kappa_{crystal} \times \alpha^N$ for one integer $N$ ≤ ~25 with topological interpretation) matches required $\epsilon_{det}$ within factor 10. Promotes C14 rate magnitude from U-D to U-C. Foreword-promotion candidate.
- **Outcome B (structural form correct, fit factor pending)**: structural form matches within factor 100-1000; some additional geometric factor needed but mechanism right. Partial closure; matrix update reflects structural-form-correct.
- **Outcome C (form right, magnitude off by ≥3 OOM)**: structural assembly is in the right family but missing a foundational factor; reopens as multi-session work item.
- **Outcome D (no natural AVE form matches)**: substrate-mode density at α-slew quantum is not yet established in the corpus at the precision needed; rate magnitude gap remains open; honest scope-statement.

### Pre-registered falsifier

If no AVE-natural structural form matches the required suppression within factor 1000, the α-slew detection mechanism for DAMA is in trouble — energy + modulation match (already corpus-closed) loses its rate-magnitude scaffolding. This would NOT walk back the energy + modulation closures (which stand on their own foreword-bullet derivation), but it would demote the rate-magnitude prediction to "framework incomplete" rather than "single-parameter target."

### Honest-scope flag pre-registered

The corpus's prior framing of "single Q-factor closure" at [`dama-alpha-slew-derivation.md:85-93`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) and [`research/2026-05-17_C14-DAMA_amplitude_result.md:125-137`](2026-05-17_C14-DAMA_amplitude_result.md) used "Q-factor" loosely. **This derivation explicitly distinguishes two physically-different "Q"s** that the prior framing conflated:
- **Resonance bandwidth Q** ($\sim 1$ to $10^4$): sets the spectral width of the α-slew absorption line. Determines modulation amplitude.
- **Per-event detection probability $\epsilon_{det}$** ($\sim 10^{-51}$): the dimensionless probability that a substrate α-slew event deposits its full quantum into the detector. Determines rate magnitude.

The corpus walked back the conflation in this derivation; the rate-magnitude gap is on $\epsilon_{det}$, NOT on bandwidth Q.

## §1 — Intrinsic α-slew event rate in NaI ($R_{intrinsic}$)

Computed in [`src/scripts/vol_3_macroscopic/derive_dama_q_factor.py`](../src/scripts/vol_3_macroscopic/derive_dama_q_factor.py) Step 1.

The intrinsic α-slew rate is sourced by every atomic electron in the detector:

$$R_{intrinsic} = N_e^{(kg)} \times \nu_{slew}$$

where $N_e^{(kg)}$ is the electron number density per kg of NaI, computed from molar mass (149.89 g/mol) and total electronic charge $Z_{Na} + Z_I = 11 + 53 = 64$ per molecule.

## §2 — DAMA observed rate ($R_{DAMA}$)

DAMA/LIBRA Phase-2 reports $\sim 0.01$ cpd/kg/keV at 2-6 keV single-hit. Total integrated rate in window: $\sim 0.04$ cpd/kg = $4.6 \times 10^{-7}$ events/s/kg. (Counts both modulating + non-modulating components in the cosine fit; AVE prediction targets the total rate, not just the modulating amplitude.)

## §3 — Required suppression $\epsilon_{det}^{required}$

Computed as $R_{DAMA} / R_{intrinsic}$ in script Step 2.

## §4 — Natural AVE-structural candidates for $\epsilon_{det}$

Script Step 3 enumerates and scores each:

1. $\kappa_{crystal} \times \alpha^N$ for $N \in [10, 30]$
2. $\kappa_{crystal} \times (\alpha/(2\pi))^N$ for $N \in [10, 25]$
3. $\kappa_{crystal} \times \Phi_A^N$ where $\Phi_A = \alpha^2$
4. $\kappa_{crystal} \times (a_e)^N$ where $a_e = \alpha/(2\pi)$
5. Combinations: $\kappa_{crystal}^p \times \alpha^N$

For each candidate, report:
- Best-fit integer exponent $N$
- $\epsilon_{det}^{candidate}$ vs $\epsilon_{det}^{required}$ ratio (factor)
- Whether the exponent has plausible topological / geometric meaning

## §5 — Numerical result

*[To be filled by script output — see §6 below for harness.]*

## §6 — Script harness

```
$ uv run src/scripts/vol_3_macroscopic/derive_dama_q_factor.py
```

Script reports each candidate's $\epsilon_{det}$ and ratio to required; identifies best structural form; lands honest gap-statement.

## §7 — Adjudication

*[To be filled after script output.]*

## §8 — Cross-references

- **Prior chain (this session)**: [`research/2026-05-17_C14-DAMA_amplitude_prereg.md`](2026-05-17_C14-DAMA_amplitude_prereg.md) → [`research/2026-05-17_C14-DAMA_amplitude_result.md`](2026-05-17_C14-DAMA_amplitude_result.md) (energy + modulation closure) → this doc (rate magnitude)
- **Canonical α-slew leaf**: [`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md) §6
- **Canonical operators**: Op2 (Saturation), Op14 (Z_eff), Op21 (Q ~ 1/ln(Z₁/Z₀)), Op22 (Avalanche M=1/S²) per [`operators.md`](../manuscript/ave-kb/common/operators.md)
- **Canonical lattice porosity** Φ_A = α²: [`optical-refraction-gravity.md:46`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)
- **Canonical κ_crystal template**: [`sagnac-rlve.md:14-26`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md)
- **Mutual coupling Borromean topology**: [`mutual-coupling-constant.md`](../manuscript/ave-kb/vol6/framework/computational-mass-defect/mutual-coupling-constant.md) — uses cinquefoil (2,5) topology with 5 crossings × π/2 phase per crossing
- **Matrix row**: [`divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) C14-DAMA-MATERIAL

## §9 — Lane attribution

Prereg + derivation work landed on `analysis/divergence-test-substrate-map` branch. Pre-audit corpus-grep dispatched agentId a3d1372d5d9c02578 (output integrated into §0). ave-discrimination-check audit dispatched in parallel to keep AVE-distinct content honestly framed. Continues 7-audit-cycle thread on α-slew substrate framing.
