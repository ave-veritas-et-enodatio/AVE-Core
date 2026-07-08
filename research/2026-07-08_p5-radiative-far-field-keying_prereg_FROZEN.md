# P5 — RADIATIVE FAR-FIELD KEYING: is one radiative-scoping postulate the unifying key for BOTH EM sectors? — FROZEN PREREG

**Date:** 2026-07-08 · **Lane:** implementer · **Branch:** `analysis/p5-radiative-keying`
**Contention:** P5 of the paper-hardening epic (Grant ruling: "test it"). **Tree base:** `origin/main` @ `5219a0b0`.
**Freeze proof:** this file is committed BEFORE any driver/result exists (git ordering = freeze). No result
number appears below; the routing thresholds and guards are committed in advance.

**Pre-work skills fired (recorded):**
- `substrate-native-check` — the two keying functionals are the Axiom-4 kernel projected onto the ε (capacitive)
  and µ (inductive) sectors; they are evaluated as the DIRECT kernel (not the fdtd engine, which carries the
  live VCA-R01 `|B|`-keying defect — `pvlas-static-b-verdict.md`:55). This is the FREE-EM vacuum grade; the
  bound κ-keyed Cosserat µ (`cosserat_field_3d.py`) is a DIFFERENT engine and is NOT touched.
- `phase-space-coordinate-check` (A46) — the corpus claim lives in phase-space reactance coordinates. The test
  measures IN those coordinates: `A_V = |E|/E_yield` (potential coordinate) and `A_I = |∮H·dℓ|_node/I_max`
  (circulation coordinate). The far-field diagnostic is a SEPARATE real-space energy-flux axis (radiated power),
  used only as the discriminator, never as a keying coordinate.
- `consistency-vs-emergence` — the loading VERDICT (loads vs transparent) is STRUCTURAL (whether the keying
  coordinate is nonzero) and is required to be scale-invariant; the loading MAGNITUDES ride `E_yield` / `I_max`
  which carry `e`, `m_e` → α-echo / CONSISTENCY-class; those magnitudes are firewalled OFF the verdict path.
- `pre-test-physics-check` — one plumber-physical question surfaced to Grant (see §6).

---

## §1 — THE HYPOTHESIS UNDER TEST (Grant-blessed ontology — TESTED, not assumed)

The Letter currently carries the radiative scoping as an explicit POSTULATE (`main.tex`:347 VERBATIM
*"The radiative scoping is at present a postulate: it states that the law is radiative-sector, not yet why"*)
and treats the E-route charge-keying and the B-route circulation-keying as DISTINCT sectors (`main.tex`:356-358).
P5 tests whether one statement absorbs both:

> **RADIATIVE-SCOPING HYPOTHESIS.** The single key for BOTH EM sectors is the field's RADIATIVE / far-field
> character. A held/static **E** (charge-sourced, near-zone) LOADS; a held/static **B** (monopole-free,
> near-zone) is TRANSPARENT; a RADIATION field (pure far-field) is ACTIVE. If true, one radiative-scoping
> statement REPLACES the two sector-keying postulates ("charges exist, monopoles don't"), and PVLAS/BMV
> consistency becomes COMPUTED, not asserted.

The **operational content** that makes this falsifiable: if radiative far-field character is the key, then the
loading of a config must TRACK a **field-intrinsic** far-field diagnostic — a loader must be far-field, a
transparent config must be near-field. If instead a NEAR-ZONE config loads (or a far-field config is
transparent), the far-field diagnostic does NOT explain the loading, and the two sector postulates are NOT
absorbed by a single radiative statement.

---

## §2 — THE TWO CANONICAL KEYING FUNCTIONALS (imported form; direct-kernel, not fdtd)

Both are the one Axiom-4 kernel `S(A)=√(1−A²)` projected onto a sector:

- **ε-grade (capacitive / varactor), potential coordinate.** `S_ε = √(1−A_V²)`, `A_V = |E|/E_yield`
  (`node-up-small-large-signal.md`:104; round-3 `[DERIVED: CHARGE-KEYED]` — keys on the MEAN-SQUARE `⟨A_V²⟩`,
  DC-INCLUDED, `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md`). ε-loading `= ⟨1−S_ε⟩` over
  a cycle.
- **µ-grade (inductive / relativistic inductor), circulation coordinate.** `S_µ = √(1−A_I²)`,
  `A_I = |∮H·dℓ|_node/I_max`, `I_max = ξ_topo·c = e·c/ℓ_node` (`relativistic-inductor.md`:15,:18;
  `pvlas-static-b-verdict.md`:30). The node-scale circulation is `∮H·dℓ = (∇×H)·ℓ_node²` (the grid-invariant
  node-perimeter form, `2026-06-25_vca-mu-circulation-observable-derivation.md`:141-155; the per-cell
  normalization factor is OPEN but MOOT for a static null and OFF the verdict path). µ-loading `= ⟨1−S_µ⟩`.

**Anti-tautology construction rule (CRITICAL).** `A_V` and `A_I` are COMPUTED from the sampled field of each
config by the SAME operators for every config — `A_V` from `|E|`, `A_I` from a finite-difference `∇×H` of the
sampled `H`. The static-B null MUST emerge as `∇×H≈0` from the field (reported with a refinement/convergence
residual), NOT be hard-coded. Neither channel is told which config it is looking at.

---

## §3 — THE FOUR FIELD CONFIGURATIONS (three ontology + one discriminating control)

All fields are built analytically on a lattice and sampled in a PML-free interior region away from sources
(top-K density sampling not needed — analytic fields, but source singularities are excluded by a radius mask).
For oscillatory configs the reactance PAIR (C-state `A_V`, L-state `A_I`) is recorded at EVERY phase over a
full cycle and cycle-averaged (Rule-10 reactance-pair tracking — a single-phase snapshot cannot distinguish a
static config from an oscillator caught at peak).

| # | Config | Source | `∂_t` | Field-intrinsic far-field char |
|---|---|---|---|---|
| 1 | **Static E** | point charge (Coulomb `1/r²`), interior sampled | 0 | near-zone: net Poynting = 0 |
| 2 | **Static B** | current loop (magnetic dipole), vacuum sampled | 0 | near-zone: net Poynting = 0 |
| 3 | **Radiation** | traveling plane wave `E∥x̂`, `B∥ŷ`, `B=E/c` | ≠0 | FAR-zone: net Poynting > 0 |
| 4 | **Standing wave (CONTROL)** | two counter-propagating waves | ≠0 | near-field-like: **net Poynting = 0** despite large local `|E|`, `∂_tE` |

**Config 4 is the discriminating control (the "config that CAN report the opposite").** A standing wave has
large local field and large `∂_tE` (so its keying coordinates `A_V`, `A_I` are nonzero — it CAN load) but ZERO
net radiated power (far-field diagnostic = 0). It splits the two hypotheses cleanly:
- radiative-far-field key ⟹ config-4 TRANSPARENT (no radiated power);
- local phase-space-coordinate key ⟹ config-4 LOADS (nonzero `A_V`, `A_I`).

The µ-functional is thereby proven can-report-nonzero (configs 3,4), so the static-B null (config 2) is
INFORMATIVE, not a functional that always returns zero.

---

## §4 — THE FAR-FIELD DIAGNOSTIC (field-intrinsic; the discriminator axis)

Primary: **normalized net radiated power** `F = |⟨S⟩_net| / (⟨u⟩·c)`, `S = E×H` (Poynting),
`u = ½ε₀|E|² + ½|B|²/µ₀` (energy density), cycle- and interior-averaged. `F∈[0,1]`: `F=1` for a pure traveling
wave, `F=0` for a static or standing field. Committed classification: **radiative if `F>0.5`, near-field if
`F<0.5`.** Secondary diagnostics reported for completeness (not routing-critical): the `|E|`-vs-`c|B|` balance
`β=(ε₀|E|²−|B|²/µ₀)/(ε₀|E|²+|B|²/µ₀)` and a near/far zone `kr` parameter.

**Loading classification (committed).** A channel LOADS iff its RMS keying coordinate `√⟨A²⟩ > τ_A = 1e-4`;
TRANSPARENT iff `< 1e-4`. Active configs are driven to `A ~ 0.3–0.7` (deficits `O(1e-2)`), null coordinates
emerge at the discretization floor (`~1e-8` or below); `τ_A=1e-4` sits in the two-decade-plus gap. A config
"loads" (overall) iff EITHER channel loads.

---

## §5 — VERDICT ROUTING (committed in advance)

Let `L_i∈{load,transparent}` be the overall loading of config `i` and `R_i∈{far,near}` its far-field class
(`F>0.5`). Define a **tracking violation** = a config that loads with `R_i=near`, OR a config that is
transparent with `R_i=far`.

- **[RADIATIVE-KEY-CONFIRMED]** — the three ontology configs behave as predicted (1 loads, 2 transparent,
  3 active) AND there are ZERO tracking violations across all four configs (loading ⟺ far-field). ⟹ one
  radiative-scoping postulate absorbs the two; resolves P5 + H1 (H1 count drops by one). Still deliver S_B.
- **[RADIATIVE-KEY-REFUTED]** — ≥1 tracking violation exists (a near-field config loads, or a far-field
  config is transparent). ⟹ far-field character is NOT the unifying key; keep ε-charge-keying and
  µ-circulation-keying as two independent postulates; H1 count stays (= 3 sector postulates). Still deliver S_B.
- **[RADIATIVE-KEY-MIXED]** — the three ontology configs behave as predicted but the tracking is partial
  (e.g. it holds for the µ-sector but the ε-sector loads in the near-zone). Report the partial + what it
  implies for the postulate count.

**Committed prediction of the anti-tautology check:** the static-B `A_I` and the static-E `A_V` are computed
from the field; whichever way they come out, they are reported verbatim and route the verdict. No adjudication
criterion is dropped post-hoc (Rule 11). If the result falsifies the radiative-scoping ontology, it is
recorded as a clean negative with the mechanism named (Rule 11), and S_B is still delivered.

---

## §6 — FIREWALL, SCALE-INVARIANCE, ANTI-TAUTOLOGY, and the ONE PLUMBER QUESTION

- **Firewall (AST-scan gate).** The `verdict(...)` function and the loading/tracking classifiers take only the
  computed diagnostics (`A_V`, `A_I`, `F`, `β`) as inputs; an AST scan asserts NO token `ALPHA`/`M_E`/`m_e`
  appears anywhere on the verdict-path functions. Field construction and the `A`-normalizations may import
  `E_yield`/`I_max`/`ℓ_node` (which carry `e`,`m_e`) as DIMENSIONAL normalizations only.
- **Scale-invariance guard.** Re-run the full verdict with `E_yield` and `I_max` each rescaled by `{0.1×, 10×}`;
  assert the `{load, transparent}` pattern and the verdict are UNCHANGED (only the magnitudes scale). If any
  rescale flips the verdict, the α-echo magnitude has reached the verdict → FAIL.
- **Anti-tautology gate.** (a) config-2 `A_I` emerges as `∇×H` of the sampled dipole field (residual reported +
  refinement); (b) config-4 (control) MUST be able to report loading (proves the null is not a dead functional);
  (c) neither channel is passed a config label.
- **Energy honesty.** For the wave configs report the cycle energy-balance drift; the fields are analytic
  (no integrator) so drift is the sampling/quadrature residual, reported.
- **ONE PLUMBER-PHYSICAL QUESTION surfaced to Grant (pre-test-physics-check):** *Is the E/B keying asymmetry a
  consequence of the Maxwell SOURCE asymmetry (`∇·E=ρ/ε₀` has charges, `∇·B=0` has no monopoles), or of the
  field's radiative/far-field CHARACTER? These differ observably: the source-asymmetry lets a static-E load
  (a real near-zone charge bias) while a pure far-field-scoping would make static-E transparent like static-B.
  The test measures whether loading tracks a field-intrinsic far-field diagnostic — so it discriminates "source
  asymmetry" from "radiative scoping" directly.*

---

## §7 — THE OWED EQUATION (S_B) — to be written in the RESULT, form committed here

The magnetic-sector functional to lift into a paper-ready equation:
`S_B ≡ S_µ = √(1−A_I²)`, `µ_eff = µ₀/√(1−A_I²)`, `A_I = |∮H·dℓ|_node/I_max`, `I_max = e·c/ℓ_node ≈ 124.4 A`,
parameter-free. The RESULT will show (a) `∂_tB=0 ⟹ ∮H·dℓ=0 ⟹ A_I=0 ⟹ S_µ=1 ⟹ δn_µ=0` (reduces to Letter
Eq (6)); (b) the near-zone `(kr)²` suppression of `A_I` that makes PVLAS/BMV consistent as a COMPUTED limit;
and (c) state whether S_B is a CONSEQUENCE of the radiative-scoping principle or an INDEPENDENT postulate,
routed by the §5 verdict.

## §8 — OUTPUTS

`src/scripts/verify/p5_radiative_far_field_keying.py` (driver + JSON), a house-WHITE figure, a standing test
`src/tests/test_p5_radiative_far_field_keying.py`, and `research/2026-07-08_p5-radiative-far-field-keying_RESULT.md`.
`make verify` green. NO edit to the paper / ledger / canon (result doc only, with a proposed integration note).
NO self-merge — push branch, open PR into main.
