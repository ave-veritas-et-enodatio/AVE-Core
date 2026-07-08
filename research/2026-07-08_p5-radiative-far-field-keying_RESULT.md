# P5 — RADIATIVE FAR-FIELD KEYING: RESULT + the owed magnetic functional S_B

**Date:** 2026-07-08 · **Lane:** implementer · **Branch:** `analysis/p5-radiative-keying`
**Tree base:** `origin/main` @ `5219a0b0`. **FROZEN prereg (gated on):**
`research/2026-07-08_p5-radiative-far-field-keying_prereg_FROZEN.md` (freeze commit `76486a59`,
committed BEFORE the driver — git ordering = freeze proof).
**Driver:** `src/scripts/verify/p5_radiative_far_field_keying.py` (numpy; direct Axiom-4 kernel,
NOT the fdtd engine — the fdtd free-EM µ path carries the live VCA-R01 `|B|`-keying defect,
`pvlas-static-b-verdict.md`:55; constants imported from `ave.core.constants`).
**Figure:** `src/scripts/verify/p5_radiative_far_field_keying_figure.py` (house-WHITE).
**Tests:** `src/tests/test_p5_radiative_far_field_keying.py` (12 fast-core gates).
**JSON:** `src/scripts/verify/_output/p5_radiative_far_field_keying.json`.

## ROUTED VERDICT: **[RADIATIVE-KEY-REFUTED]**

> The field's **radiative / far-field character is NOT the unifying key** for the two EM sectors.
> Loading is **decorrelated** from a field-intrinsic far-field diagnostic: a **static E** (charge,
> near-zone) LOADS the ε-channel with **zero radiated power**, and a **standing wave** LOADS both
> channels with **zero NET radiated power** — two near-zone loaders. Each channel keys on a **LOCAL
> phase-space coordinate** (`A_V=|E|/E_yield` for ε; `A_I=|∮H·dℓ|_node/I_max` for µ), not on the
> field's global radiative character. The three ontology configs still behave exactly as predicted
> (E loads, B transparent, radiation active) — the behaviors are REPRODUCED — but a single far-field
> statement does **not** explain them, so it does **not** absorb the two sector postulates.
> **H1 count stays: the ε-charge-keying and µ-circulation-keying remain two independent postulates.**
> S_B is delivered below regardless.

## THE PER-CONFIG RESULTS (verbatim from the JSON; `TAU_A=1e-4`, `F_FAR=0.5`)

| config | `√⟨A_V²⟩` (ε coord) | `√⟨A_I²⟩` (µ coord) | ε deficit `1−S_ε` | µ deficit `1−S_µ` | `F` (radiated) | `β_EB` | loading | far-field |
|---|---|---|---|---|---|---|---|---|
| **static E** (point charge) | `0.066299` | `0.0` | `2.213e-3` | `0.0` | `0.0` | `+1.000` | **LOAD** (ε) | near |
| **static B** (uniform, solenoid) | `0.0` | `0.0` | `0.0` | `0.0` | `0.0` | `−1.000` | **transparent** | near |
| **radiation** (traveling wave) | `0.212132` | `0.212123` | `2.290e-2` | `2.289e-2` | `1.000` | `0.000` | **LOAD** (ε+µ) | far |
| **standing wave** (CONTROL) | `0.299623` | `0.299610` | `4.750e-2` | `4.750e-2` | `1.17e-18 ≈ 0` | `0.003` | **LOAD** (ε+µ) | near |

**Tracking violations (the refutation, verbatim):**
`static_E: LOADS but near-field (F<0.5)` · `standing: LOADS but near-field (F<0.5)`.
`ontology_configs_ok = True` (E loads, B transparent, radiation active — all as predicted).

**Reading it.** If radiative far-field character were the key, loading would track `F`: loaders at
`F>0.5`, transparent at `F<0.5`. Instead **three of four configs load, and two of those three have
`F=0`** (static-E and the standing-wave control). The only transparent config (static B) ALSO has
`F=0`. So `F` and loading are decorrelated (figure Panel A). The `β_EB` column makes the actual
discriminator plain: loading happens whenever the ε-coordinate `|E|` is present (`β≥0`: static-E,
radiation, standing) and the µ-coordinate `|∮H·dℓ|` is present (radiation, standing) — i.e. keying
is on the **local field/rate coordinates of each sector**, the capacitor/inductor phase-space
coordinates (A46), not on whether the field radiates.

## THE MECHANISM THAT EXPLAINS ALL FOUR (Rule 11 — one mechanism, no rescue)

The ε-channel is a **shunt varactor keyed on the static-capable potential coordinate** `|E|`
(round-3 `[DERIVED: CHARGE-KEYED]`, mean-square DC-included) — it loads on ANY field with an
E-component, near-zone or far. The µ-channel is a **series relativistic inductor keyed on the
circulation / rate coordinate** `|∮H·dℓ| = ε₀|∂_tE|` — it loads on ANY field with a nonzero
displacement current (rate), near-zone or far, and gives an **exact zero on a static B** because a
source-free static field carries no circulation. Radiation loads both because it has BOTH `|E|` and
`∂_tE`; a standing wave loads both because it has both LOCALLY while carrying zero NET flux. The
far-field character (`F`) only correlates with loading in the special source-free traveling-vs-static
comparison; it **breaks on the near-zone static-E loader and the zero-net-flux standing wave**.

## S_B — THE OWED MAGNETIC-SECTOR FUNCTIONAL (paper-ready, parameter-free)

$$
\boxed{\;
S_B \;\equiv\; S_\mu(A_I) \;=\; \sqrt{1 - A_I^{\,2}},
\qquad
\mu_{\mathrm{eff}} \;=\; \frac{\mu_0}{\sqrt{1 - A_I^{\,2}}},
\qquad
A_I \;=\; \frac{\bigl|\oint_{\partial\,\mathrm{node}} \mathbf H\cdot d\boldsymbol\ell\bigr|}{I_{\max}}
     \;=\; \frac{\ell_{\mathrm{node}}^{\,2}\,|\nabla\times\mathbf H|}{I_{\max}},
\qquad
I_{\max} = \xi_{\mathrm{topo}}\,c = \frac{e\,c}{\ell_{\mathrm{node}}} \approx 124.4\ \mathrm A.
\;}
$$

By Ampère–Maxwell in a vacuum node, `∮H·dℓ = ε₀ ∂_t∫E·dA` — the **displacement current** — so the
kernel argument is the field's **circulation / rate**, not its magnitude. Parameter-free:
`I_max = e·c/ℓ_node` is closed two independent ways (the V→I dual of the varactor, and the rest-energy
map `½L₀I_max² = ½m₀c²`, `relativistic-inductor.md`:18,:28). Verbatim canonical form:
`relativistic-inductor.md`:15 (`L_eff(I)=L_0/√(1−(I/I_max)²)`), `pvlas-static-b-verdict.md`:30.

**Limit (a) — static B reduces to Letter Eq (6) exactly.**
`∂_t\mathbf B = 0 ⟹ ∮H·dℓ = 0 ⟹ A_I = 0 ⟹ S_B = 1 ⟹ µ_eff = µ₀ ⟹ δn_µ = 0`
(driver: `static_B` gives `√⟨A_I²⟩ = 0.0` exactly for a source-free uniform B — the µ-null EMERGES
from `∇×H` of the sampled field, and a non-uniform dipole B converges to it as `O(h²)`, ratio 4.03
per halving; `test_p5_radiative_far_field_keying.py::test_dipole_null_converges_O_h2`). This is
Letter Eq (6), `main.tex`:370-373, reproduced parameter-free at ANY field strength.

**Limit (b) — near-zone `(kr)²` suppression makes PVLAS/BMV consistency COMPUTED.**
For an oscillating magnetic source the vacuum circulation is the displacement current
`∮H·dℓ = ε₀∂_tE`, and the near-zone induced `E` is itself one time-derivative of the quasistatic
potential (`E = −∂_t A`). Two time-derivatives ⟹ `A_I ∝ ω² ∝ (kr)²` at fixed `r` (driver computes
each `∂_t` explicitly; loglog slope `= 2.000`):

| `kr` | `A_I` | `S_µ` | `δn_µ` |
|---|---|---|---|
| `1e-3` | `3.00e-5` | `1.0000000000` | `−2.25e-10` |
| `1e-2` | `3.00e-3` | `0.9999955` | `−2.25e-6` |
| `1e-1` | `3.00e-1` | `0.9539` | `−2.33e-2` |

PVLAS (Hz-modulated / DC 2.5 T) and BMV (ms pulse) sit at `kr → 0` on the optical probe timescale, so
`A_I → 0 ⟹ S_B → 1 ⟹ δn_µ → 0`: their nulls are the **computed** magnetic-sector prediction, not an
asserted side-condition. (The absolute `A_I` magnitude rides `I_max` and so is an α-echo at the value
level, `consistency-vs-emergence`; the `(kr)²` SCALING and the `δn_µ→0` limit are α-clean.)

**Is S_B a consequence of the radiative-scoping principle, or independent?** Given the [REFUTED]
verdict: **S_B is an INDEPENDENT sector postulate, not a consequence of a single radiative-scoping
principle.** Its `∂_t`-keying makes radiation the strong-loading limit for the µ-sector, but the SAME
principle does NOT cover the ε-sector, which loads on a **static** (near-zone, `∂_t=0`) charge field.
So S_B keys on **rate** (a µ-sector-specific fact: "no monopole ⟹ B has no static operating-point
bias, only circulation"), while the ε-sector keys on **potential** (a static-capable coordinate). The
far-field character is a *consequence* of S_B's rate-keying, not its cause.

## POSTULATE COUNT / H1 — TWO REMAIN, GROUNDED IN THE SOURCE ASYMMETRY (surfaced, not decreed)

The radiative-far-field statement does NOT collapse the two keys into one, so **H1 count stays at the
two sector postulates** (ε charge-keyed on `|E|`; µ circulation-keyed on `∮H·dℓ`). What the test DOES
show is that both keys share a common physical GROUNDING that is **not** "radiative character": the
**Maxwell source asymmetry** — `∇·E = ρ/ε₀` has real charge sources (so a static E is a genuine
operating-point bias for the potential-keyed capacitor), while `∇·B = 0` has no monopole (so a static
B supplies no bias to the rate-keyed inductor; only circulation `∂_tB≠0` does). This "charges exist,
monopoles don't" is a real, single physical fact — but it is a statement about SOURCES, not about
FAR-FIELD/RADIATIVE character, and it does not make static-E transparent (it loads). Whether "the two
keys reduce to the one source-asymmetry fact" counts as a genuine H1 reduction is a **framing call for
Grant** (it is a grounding, not a keying-variable unification) — surfaced, not decreed (lane
discipline: this is not a draft of the Letter's postulate ledger).

## THE ONE PLUMBER-PHYSICAL QUESTION (pre-test-physics-check; surfaced to Grant)

*Is the E/B keying asymmetry a consequence of the Maxwell SOURCE asymmetry (`∇·E=ρ/ε₀` has charges,
`∇·B=0` has no monopoles), or of the field's radiative / far-field CHARACTER?* The test answers it
observably: loading tracks the **local sector coordinate** (`|E|`, `∮H·dℓ`), NOT the far-field
diagnostic `F` — so it is the **source asymmetry**, not radiative scoping. Recommendation for the
Letter: replace "radiative scoping (postulate)" for the µ-sector with the **source-asymmetry**
grounding ("`∇·B=0` ⟹ no static magnetic operating-point ⟹ circulation-keyed"), which IS computed
here, and keep the ε-sector charge-keying (round-3) as the separate potential-sector fact. This is a
proposed reframe for Grant/auditor to land — NOT edited into the paper here.

## GATE STATUSES (all green)

- **Firewall (AST-scan):** `clean=True`. No `ALPHA`/`M_E`/`m_e` token in the verdict-path functions
  `classify_loading`, `classify_farfield`, `verdict` (`firewall_ast_scan`, asserted in `main()` and
  `test_firewall_no_alpha_me_on_verdict_path`).
- **Scale-invariance:** `scale_invariant=True`. Rescaling `E_yield` and `I_max` by `{0.1×, 10×}`
  leaves the `{load,transparent}` pattern and the `RADIATIVE-KEY-REFUTED` route unchanged — the
  α-echo magnitude never reaches the verdict.
- **Anti-tautology:** `informative_null=True`. The static-B µ-null EMERGES (`√⟨A_I²⟩=0.0` computed
  from `∇×H`, gap `>299` decades to the active configs; non-uniform dipole converges `O(h²)`), and
  the standing-wave CONTROL can report loading (proving the µ-functional is not a dead zero). No
  channel is passed a config label; both nulls and both loads come from the same operators.
- **Energy honesty:** analytic fields (no integrator); the standing-wave net Poynting is
  `1.17e-18 ≈ 0` (quadrature residual), the traveling-wave `F=1.000`.

## CONSISTENCY-VS-EMERGENCE CLASSIFICATION

- The **[REFUTED] verdict** is EMERGENCE-clean: it is a structural (loads-vs-transparent) decorrelation
  that is scale-invariant (α-echo firewalled off the verdict path).
- The **S_B FORM** (`√(1−A_I²)`, the `∂_t`/circulation kernel argument, the `(kr)²` near-zone law) is a
  MANIFESTATION of Axiom 4 + Ampère–Maxwell — α-clean.
- The **S_B MAGNITUDE** (`A_I` absolute value via `I_max = e·c/ℓ_node`) is CONSISTENCY-class /
  α-echo-at-value — not headlined.

## DISCIPLINE

- **Rule 11 (honest closure):** the radiative-scoping ontology is recorded as a clean NEGATIVE with a
  single mechanism named (loading keys on local sector coordinates, not global far-field character);
  no adjudication criterion was dropped post-hoc — the routing thresholds and the tracking-violation
  definition were frozen in the prereg (`76486a59`) before the run. S_B is delivered regardless (the
  prereg committed it on both branches).
- **Rule 12 (substitution-not-retraction):** nothing is retracted; the Letter's "radiative scoping is
  at present a postulate" (`main.tex`:347) is CONFIRMED as a postulate that does NOT unify the sectors,
  and a substitute grounding (source asymmetry) is SURFACED for Grant, not refilled into the slot here.
- **flag-don't-fix:** the Letter's own text already says (`main.tex`:347-352) the E-route dynamical
  scoping routes "have each been tested and excluded; the static-field response is instead derived to
  be charge-keyed" — this result is CONSISTENT with that admission and quantifies it (static-E loads
  with `F=0`). No paper/canon edit made.
- **phase-space-coordinate-check (A46):** the test measures IN the sector reactance coordinates
  (`A_V` potential, `A_I` circulation); the far-field `F` is a separate real-space energy-flux axis
  used only as the discriminator — never as a keying coordinate.

## PROPOSED INTEGRATION NOTE (NOT applied — for Grant/auditor to land)

1. **Letter §"magnetic sector":** the paper can now state S_B explicitly (the boxed equation above) and
   present Eq (6) as its `∂_tB=0` endpoint, with the `(kr)²` near-zone table as the COMPUTED PVLAS/BMV
   consistency (replacing the asserted side-condition). Cite the driver + this result doc.
2. **Letter §"radiative scoping (postulate)":** the µ-sector's scoping is better stated as the
   **source-asymmetry** grounding (`∇·B=0`), which this test computes; the ε-sector stays charge-keyed
   (round-3). The count stays two sector keys, now with a shared physical grounding — a framing call
   for Grant.
3. **`pvlas-static-b-verdict.md`:** a candidate additive note — "the static-B null and the near-zone
   `(kr)²` suppression are the same S_B (`A_I∝∂_t`); PVLAS/BMV sit at `kr→0`, transparency computed."
   Surfaced for the auditor lane; NOT written into canon here.

## CORPUS-STATE UPDATE (surfaced to the auditor lane — NOT landed; NO edit to `manuscript/ave-kb/**`)

- The auditor lane lands these. Empirical finding surfaced: **radiative far-field character is NOT the
  unifying EM keying principle** (P5 [REFUTED]); the two sector keys (ε: `|E|`, µ: `∮H·dℓ`) are grounded
  in the **Maxwell source asymmetry**, not radiative scoping. S_B is delivered as an explicit
  parameter-free equation with its Eq (6) static limit and its `(kr)²` near-zone limit. No supersession
  of any leaf is staged; `main.tex`:347's "postulate" wording is confirmed and a substitute grounding
  is surfaced for Grant to adjudicate.
