# Prereg + first-pass result: two-node projection alpha residue

**Status:** FROZEN PREREG before driver run; result appended after execution.
**Branch:** `analysis/2026-06-07-two-node-alpha-projection`.
**Driver:** `src/scripts/vol_1_foundations/two_node_alpha_projection.py`.
**Question from Grant:** alpha as the screened RMS / sigma from the fact that it takes **two nodes** to fully project the electron flux tube's 2D precessing profile.

---

## §0 Target

Test whether the electron's phase-space flux tube has an alpha-scale screened residue that appears only after projection across a canonical adjacent A/B two-node baseline.

Mechanical picture:

- The electron's `(2,3)` identity lives in `(V_inc, V_ref)` phase space, not as a static real-space torus.
- A single K4 node observes only a scalar / partial cut through the precessing 2D profile.
- A canonical adjacent A/B pair may be the minimal projector that reconstructs the full 2D profile over a precession cycle.
- The candidate observable is the screened covariance residue of that two-node projection.
- RMS compares to `sqrt(alpha)`; variance / power / loss fraction compares to `alpha`.

## §1 Corpus constraints

The prior two-node synthesis already states the relevant coordinate discipline:

> "The electron is a flux oscillation between two adjacent K4 nodes (one A-sublattice, one B-sublattice), with the bond length `ell_node` as the load-bearing physical scale. The Golden Torus geometry that gives `alpha^-1 = 137` lives in PHASE SPACE, not real space."

It also identifies the remaining empirical test as extracting `V_inc/V_ref` phasor trajectory on a single A-B bond and checking the phase-space Golden-Torus structure. This test is not that full engine extraction. It is a first-pass projection-operator test: does the *two-node projection idea itself* create an alpha-scale screened residue from alpha-free Golden-Torus geometry?

The canonical alpha leaf also sets the ceiling: the Golden-Torus alpha route is Class B substrate-mechanism manifestation. A stronger result here would require a new substrate primitive: two-node projection completeness deriving the screened residue without importing alpha.

## §2 Preregistered discriminator

Inputs allowed:

- K4 adjacent A/B two-node picture.
- `(2,3)` winding.
- Golden-Torus `R = phi/2`, `r = (phi - 1)/2`, `d = 1` from the existing Class-B corpus.
- Pure projection/covariance algebra.

Inputs forbidden:

- `alpha`, `e`, `epsilon_0`, `hbar`, `Z0`, or CODATA-derived quantities as computational inputs.
- Fitting a phase offset, kernel, or projector angle to make `1/137`.

Outcomes:

| Outcome | Criterion | Interpretation |
|---|---|---|
| A | Adjacent two-node screened variance robustly lands near `alpha`, while one-node and wrong-pair controls fail; RMS lands near `sqrt(alpha)` | New two-node projection route worth auditor review |
| B | Adjacent two-node lands near `sqrt(alpha)` in RMS but variance does not land near `alpha` | Possible amplitude-level residue; not alpha itself |
| C | Adjacent two-node is `O(0.1-1)` or control-dependent | Negative; two-node projection does not explain alpha |
| D | Result depends on arbitrary projector angle / phase offset | Fit artifact; reject |

**Prediction before run:** C. Reason: prior negatives suggest local/real-space shadows and simple projection statistics produce `O(1)` or `O(0.1)` quantities, while alpha lives in the codimensional phase-space mode-count. The two-node hypothesis is worth testing because it is more substrate-native than the one-node shadows, but I expect a simple covariance projector to be too weak to generate `1/137`.

## §3 Substrate-native and coordinate checks

- **Sector:** phase-space diagnostic of the bond LC profile, not real-space shell fitting.
- **Coordinate match:** the profile lives in `(V_inc, V_ref)` coordinates. The script does not compare real-space geometry to phase-space alpha.
- **Generative status:** not an emergence simulation. The `(2,3)` profile is given from canonical corpus geometry. Any positive result would still be a projection-mechanism candidate, not a full electron-genesis closure.
- **Classification:** at best Class B lift candidate unless future K4-TLM extraction derives the profile and projector from dynamics.

Additional skill checks after Grant's "check all skills even if Claude" instruction:

- **pre-test-physics-check:** the plumber question was supplied by Grant before branch work: *does two-node projection of the full precessing flux-tube profile expose alpha as screened RMS/sigma?* The corpus does not settle this exact screened-residue version; it only settles that the two-node electron and `(V_inc,V_ref)` phase-space framing are canonical.
- **ave-canonical-source:** `ALPHA_COLD_INV` and `ALPHA_COLD` were verified at `src/ave/core/constants.py` and are imported for comparison only. The script asserts that `ave.core.constants` resolves to the canonical AVE-Core module before writing outputs.
- **ave-canonical-leaf-pull:** the relevant physical class is electron-tank Q / boundary-observable alpha decomposition. The test is scoped below the canonical leaf: it does not replace Op21 mode-counting, Theorem 3.1, or the Golden-Torus Class-B route; it only tests whether a two-node projection supplies a missing residue.
- **ave-discrimination-check:** no positive AVE-distinct claim is promoted. The result is negative; the only surviving positive statement is projection-completeness (`rank=2`), which is linear algebra, not an AVE-distinct alpha derivation.
- **ave-evidence-framing-discipline:** strength language is bounded to the measured first-pass scope: "simple covariance projector" only, not all possible two-node screened mechanisms.

## §4 Driver scope

The script constructs an alpha-free `(2,3)` phase-space Lissajous shadow with Golden-Torus semi-scales and evaluates covariance projectors:

- one-node `x` and `y` scalar cuts;
- adjacent two-node conjugate `x/y` projection;
- wrong-pair controls;
- 3-node and 4-node convergence controls.

The measured quantities are:

- screened variance fraction: smallest covariance eigenvalue divided by total covariance;
- screened RMS fraction: square root of screened variance.

`alpha` is imported only for final comparison ratios.

---

## §5 Result

Executed with:

```bash
MPLCONFIGDIR=.matplotlib-cache PYTHONPATH=src python src/scripts/vol_1_foundations/two_node_alpha_projection.py
```

Output files:

- `src/scripts/vol_1_foundations/_output/two_node_alpha_projection_results.json`
- `src/scripts/vol_1_foundations/_output/two_node_alpha_projection.png`

Summary:

| Projector | Complete? | Screened variance | vs `alpha` | Screened RMS | vs `sqrt(alpha)` |
|---|---:|---:|---:|---:|---:|
| one-node x | no | 0 | 0x | 0 | 0x |
| one-node y | no | 0 | 0x | 0 | 0x |
| adjacent two-node conjugate `x/y` | yes | 0.500000 | 68.52x | 0.707107 | 8.28x |
| wrong same-axis pair | no | 0 | 0x | 0 | 0x |
| wrong 45-degree pair | yes | 0.146447 | 20.07x | 0.382683 | 4.48x |
| three-node 120-degree | yes | 0.500000 | 68.52x | 0.707107 | 8.28x |
| four-node quadrature | yes | 0.500000 | 68.52x | 0.707107 | 8.28x |

## §6 Adjudication

**Outcome C — negative.** The canonical adjacent two-node projection is genuinely a complete 2D projector, but it gives a symmetric two-quadrature covariance residue (`1/2` variance, `1/sqrt(2)` RMS), not an alpha-scale residue. Three-node and four-node complete projectors converge to the same value, so the effect is simply "complete 2D quadrature measurement" rather than a fine-structure constant.

The wrong 45-degree complete pair gives `0.146447 = (1 - 1/sqrt(2))/2`, which is a projector-angle artifact and still 20x alpha. The same-axis pair and one-node cuts are rank-incomplete and therefore cannot carry a transverse screened residue.

Interpretation:

- The two-node idea is correct at the level of **completeness**: one node is rank-1; a conjugate adjacent pair is the minimal rank-2 projector.
- The two-node idea does **not** by itself generate `alpha` or `sqrt(alpha)`.
- Any surviving route must add a substrate-native screening kernel, impedance weighting, or mode-count normalization that is not present in this simple projector. If that added ingredient is just the Golden-Torus mode-count, the route collapses back to the existing Class-B alpha leaf rather than becoming independent.

## §7 Follow-up boundary

The only follow-up worth running is a stricter engine-native extraction:

1. read actual `V_inc/V_ref` time series on a canonical A-B bond from K4-TLM;
2. apply the two-node projector to the measured bond-pair phasor, not to an analytic Lissajous shadow;
3. introduce screening only if it is already present in the engine state (`S(A)`, `Phi_link`, Op14/Op3 impedance), not as a fitted kernel;
4. compare one-node, adjacent pair, wrong-pair, and 3/4-node projectors again.

Until that exists, this branch closes only the **simple covariance projector** version of Grant's hypothesis.
