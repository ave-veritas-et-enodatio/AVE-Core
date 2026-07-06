[↑ Vol 4 Index](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-5s5b0d, clm-7tynm2, clm-9sujp8, clm-acgyr1, clm-baoa36, clm-bdualb, clm-cltls0, clm-clvchn, clm-cwjd8t, clm-fh6w3y, clm-fofwr1, clm-fuajdb, clm-gv1wu4, clm-gw2wgc, clm-h55fy1, clm-i02mhk, clm-iz3svl, clm-k4d4ph, clm-k9up5c, clm-kl1ern, clm-oiw6cb, clm-om0rtq, clm-p12mem, clm-pp3qwf, clm-pvlas1, clm-qagkgy, clm-qsgl7d, clm-qx9bb8, clm-sve3xc, clm-to41c7, clm-trgqtf, clm-ui3m8a, clm-wcoul2, clm-wzezvt, clm-ydksh6, clm-yr6tu4]
subtree-experiments: [exp-0n5p16, exp-1ddtr0, exp-1up5ww, exp-6kwkx7, exp-71uhr0, exp-742kv5, exp-7jekc6, exp-ct4cts, exp-onqclb, exp-po1a0v, exp-rth12t, exp-v6nzcq]
-->

> ⛔ **Bootstrap.** Leaves are canonical; this index, the volume index, and the entry-point are *derived* summaries and may suggest implications not supported by the leaves. Before forming any claim about results in this subtopic, load [`../claim-quality.md`](../claim-quality.md) (volume scope) and [`../../claim-quality.md`](../../claim-quality.md) (cross-cutting). Treat the summary text and Key Results entries below as routing only — qualifications and conditions live in the cited leaves and the claim-quality documents.

# Falsification

Comprehensive experimental falsification portfolio for the AVE framework. Every prediction exposes a single measurable parameter derived from the axioms — no fitting variables.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Active Sagnac Interferometry phase shift | $\Delta\phi \approx 2.07\,\text{Rad}$ (Tungsten rotor, 200 m fiber, 10k RPM) | Ch.11 |
| Metric mutual inductance ratio | $\Psi = \rho_W/\rho_{Al} \approx 7.15$ | Ch.11 |
| $\sqrt{\alpha}$ yield limit | $V_{yield} = \sqrt{\alpha} \times 511\,\text{kV} = 43.65\,\text{kV}$ | Ch.11 |
| Levitation limit | $m_{max} = 1.846\,\text{g}$ | Ch.11 |
| YBCO phased array | $F_{total} = 24{,}480\,\text{N}$ (2.5 metric tons per m$^2$) | Ch.11 |
| $c^2$ multiplier | $a = 1{,}283\,\text{m/s}^2$ (130 G's) from $\Delta n = 1.42 \times 10^{-17}$ | Ch.11 |
| Vacuum impedance mirror | $\Gamma(V) \to 1$ as $V \to V_{yield}$ (parameter-free prediction) | Ch.11 |
| Macroscopic field limit | $E_{yield} \approx 1.13 \times 10^{17}\,\text{V/m}$ | Ch.12 |
| Maxwell stress thrust scaling | $F \propto V^2 f^2$ | Ch.12 |
| Birefringence discriminator 🔴 | ~~AVE: $E^4$; QED: $E^2$~~ → **COEFFICIENT**: $\delta n_{AVE}/\delta n_{QED}=1/(4 a_{EH}\alpha^3)\sim 10^6$ (both $E^2$-leading) | Ch.12 |
| Forward baryon predictions | $(2,17)$: $2742\,\text{MeV}$; $(2,19)$: $2983\,\text{MeV}$; $(2,21)$: $3199\,\text{MeV}$ | Ch.12 |

> **🔴 Birefringence-row correction (2026-06-04, Rule 12; clm-pp3qwf, commit `ad26d357`).** The struck "AVE: $E^4$; QED: $E^2$" framing was a **false falsifier** ($\sqrt{\varepsilon}$ conflation). Both AVE and QED are **$E^2$-leading** in the refractive-index shift; an $E^2$ slope does NOT falsify AVE. The discriminator is the field-**independent COEFFICIENT** ratio $1/(4 a_{EH}\alpha^3)\sim 10^6$. Canonical leaf: [`ch12-falsifiable-predictions/vacuum-birefringence-e4.md`](ch12-falsifiable-predictions/vacuum-birefringence-e4.md); forward driver `src/scripts/vol_4_engineering/birefringence_coefficient_discriminator.py`.

## Chapters

| Chapter | Contents |
|---|---|
| [Ch.11: Experimental Bench (detailed)](ch11-experimental-bench-falsification/index.md) | 22 leaves: kill-switches, tabletop tests, existing signatures, engineering projects (CLEAVE through TORSION), scale-up architectures, telemetry, advanced protocols |
| [Ch.11: Experimental Bench (consolidated)](ch11-experimental-bench/index.md) | 8 articles: epistemology, null results, Sagnac-RLVE, existing signatures, PCBA protocols, industrial scale-up, zero-parameter derivations, advanced protocols |
| [Ch.12: Falsifiable Predictions](ch12-falsifiable-predictions/index.md) | EE Bench plateau, Sagnac-RLVG telemetry, autoresonant rupture, helicity injection, baryon mass predictions, kill-switches, birefringence |

---
