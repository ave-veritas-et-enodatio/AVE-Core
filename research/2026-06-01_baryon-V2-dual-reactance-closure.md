# Baryon Mass Eigenvalue V_TOROIDAL_HALO = 2: Dual-Reactance Closure

**Date:** 2026-06-01
**Branch:** `analysis/baryon-v2-reactance-scrub`
**Status:** RESULT doc — reframe + mechanism + mass-discriminator + false-derivation audit + honest residual
**Discipline:** `ave-ee-first-mapping` (Step 6), `ave-walk-back` (deliverable-7 propagation), `ave-driver-script-honesty`, `ave-canonical-source`, `verify-before-cite`, `ave-evidence-framing-discipline`

> **One-line:** the "2" in the proton mass eigenvalue `x = I_scalar/(1 − V·p_c) + 1` is the **count of the node's two reactance sectors** (capacitive X_C from 3 translational-E DOF + inductive X_L from 3 microrotational-B DOF), NOT a geometric "toroidal halo volume." The volume name was a misnomer that spawned four independent false "derivations" of the number 2. The mass uniquely selects the additive-2-channel count (1836.117 m_e vs CODATA 1836.153).

---

## §0 — Scope + what this doc does / does NOT do

**Grant-adjudicated 2026-06-01.** The baryon mass eigenvalue
`x_core = I_scalar/(1 − V·p_c) + 1` (`src/ave/core/constants.py:770,774`;
[`self-consistent-mass-oscillator.md`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md))
carries `V_TOROIDAL_HALO = 2`. The corpus framed this "2" as a **geometric
"toroidal halo volume"** and "derived" it via a signed-crossing integral
`V = ∫∫∫ sgn(det[τ₁,τ₂,τ₃]) = 2` (`constants.py:760`). That derivation is
**false** (§3). The "2" is the **dual-reactance count**: the node's TWO
reactance sectors per Axiom 1 — 3 translational-E DOF → capacitive `X_C`;
3 microrotational-B DOF → inductive `X_L` — each one electron-ground-state
unit. This is the SAME E/B conjugate pair the photon uses
([`translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md):35).

**This doc DOES:**
- Re-derive the "2" as the reactance-sector count (§1).
- Show the mass UNIQUELY selects additive-2 (§2), using the canonical engine
  values (not prose-rounded numbers).
- Audit the four false "volume" derivations and name each failure mode (§3).
- State the honest residual: the count-2 is **closed**; the per-channel
  coupling = `p_c` is a **residual** (canonical-packing-plausible, not
  line-by-line) — so the ladder is **"1-residual Skyrme"** (vs standard
  Skyrme's 2 tuned params F_π, e), NOT "zero-parameter" (§4).
- List the cleanup this branch lands + the propagation that needs Grant's
  boundary call (§5).

**This doc does NOT:**
- Touch the value 2.0 — it is confirmed correct (mass-discriminator §2).
- Touch the α-from-Golden-Torus derivation. α comes from the Golden Torus
  geometry (Vol 1 Ch 8); K=2G is a DOWNSTREAM consistency, NOT the driver of
  α/EM (vol1/[`claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md):135,145;
  [`zero-parameter-universe.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md):32).
- Claim the count-2 ⟷ K/G=2 numerical coincidence is a derived identity — it
  is flagged as a coincidence (§1, THREE-2's table).
- Re-classify the foreword / matrix C8-BARYON-LADDER row / proton-identification
  "flagship axiom-derived" framing — that broader propagation is surfaced as
  flag-don't-fix (§6) for Grant's adjudication, because it interacts with the
  `consistency-vs-emergence` classification.

**Canonical-source note (`ave-canonical-source`).** Every number below is
imported from / verified against `src/ave/core/constants.py`; none is
hardcoded into this doc as a fresh literal. Engine values quoted here were
read live this session (§2 reproduction block).

## §1 — The mechanism: dual reactance (X_L / X_C), photon-shared E/B

### §1.1 — The two reactance sectors (Axiom 1, EE-native)

Axiom 1 (INVARIANT-S2) states the node has 6 DOF: **3 translational → E-field
origin → capacitive storage**; **3 microrotational → B-field origin → inductive
flywheel**. These are "the structural origin of **E** and **B** as conjugate
variables at every node"
([`translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md):35,
verbatim). The substrate IS an LC network and inherits standard LC reactance
algebra verbatim. So the node has exactly **two reactance sectors**:

| Sector | Substrate origin | EE object | Reactance |
|---|---|---|---|
| Capacitive | 3 translational-E DOF | dielectric storage | `X_C = 1/(jωC) = −j/(ωC)` |
| Inductive | 3 microrotational-B DOF | inductive flywheel | `X_L = jωL` |

`V_TOROIDAL_HALO = 2` is the **COUNT of these two sectors**, each contributing
one electron-ground-state unit of stored reactive energy to the self-consistent
mass loop. It is an EE-native integer (number of reactance channels), not a
geometric volume.

### §1.2 — Why the count is additive (energy), not a signed sum (reactance)

This is the load-bearing nuance: at resonance the two reactances **cancel**, so
the "2" cannot be a signed reactance sum.

Standard LC algebra (which the substrate inherits — Axiom 1): `Z_L = jωL`,
`Z_C = 1/(jωC) = −j/(ωC)` (because `1/j = −j`). At resonance `ωL = 1/(ωC)`, so
`X_L = −X_C` ⟹ `|X_L| = |X_C|` and the **signed sum X_L + X_C = 0**. The two
reactances are equal-and-opposite by construction.

Therefore the "2" is NOT `X_L + X_C` (that is 0). The additive "2" is cleanest
as the **stored energy**, which is positive-definite in each sector:
`E_L = ½ L I²` and `E_C = ½ C V²`. At resonance the cycle-peak energies are
equal (`E_L = E_C`, equipartition), and the **count of energy-storing reactance
sectors is 2**. The eigenvalue's `V·p_c` term is "(2 reactance channels) ×
(per-channel coupling p_c)" — a count of channels times a per-channel gain, the
regenerative-feedback form (§1.3).

### §1.3 — Photon-shared E/B + the regenerative-loop form (EE-first mapping)

`ave-ee-first-mapping` Step 1–3: the substrate primitive is the node's
E/B conjugate reactance pair; the EE object is a **regenerative (positive-
feedback) LC loop**. The proton's self-consistent mass equation
`x_core = I_scalar + (V·p_c)·x_core` rearranges to **Black's closed-loop gain
form**:

> `x_core = I_scalar / (1 − V·p_c)`  ≡  `A_closed = A_open / (1 − βA)`

with open-loop "drive" `I_scalar` (the 1D Faddeev-Skyrme scalar rest mass),
loop-gain `βA = V·p_c = 2·p_c`, and `V = 2` = the number of reactance sectors
feeding the loop. The same E/B conjugate-storage pair the **photon** uses to
propagate (translational-E ⟷ microrotational-B exchange per cycle,
`translation-circuit.md:35`) is what the **standing baryon** uses to store
self-energy — the baryon is the photon's reactance pair caught in a
topologically-confined regenerative loop rather than a propagating one.

**Means-test (`ave-ee-first-mapping` Step 4).** The EE form predicts the mass
selects the *integer channel count*, not an RMS or a signed sum. §2 confirms:
the mass uniquely picks `V = 2` (additive, integer), discriminating it from
`V = 1`, `V = p_c`, and (implicitly) from `√2` (RMS of two unit channels). PASS.

### §1.4 — THREE distinct "2"s — keep separate, do NOT fuse

There are three numerically-coincident 2's in the neighborhood of this result.
They are physically distinct; the corpus must not fuse them:

| # | The "2" | What it is | Numeric |
|---|---|---|---|
| 1 | **V = 2** | **reactance-sector COUNT** (this result): X_C sector + X_L sector, each an electron-unit | integer 2 |
| 2 | **K/G = 2** | bulk/shear modulus ratio at the EMT trace-reversal point → √2 longitudinal/photon speed ratio (vol1/[`claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md):1391, clm-uu1qbo) | ratio 2 |
| 3 | **E_L = E_C** | equipartition of the two reactive stores at resonance | ratio 1 |

> **Coincidence flag (`ave-evidence-framing-discipline`).** The numerical
> coincidence **V=2 (count) = K/G=2 (modulus ratio)** is NOT a derived identity.
> They share the integer 2 but arrive at it by unrelated routes (channel-count
> vs continuum-elastic-modulus-ratio). Do not write "the reactance count is the
> modulus ratio" or imply one derives the other. They are flagged here as a
> coincidence precisely so a future reader does not manufacture a false identity
> from the shared digit — which is exactly the failure mode that produced the
> four false "volume" derivations (§3).

## §2 — The mass-discriminator: the mass selects additive-2

The "2" is not a free choice — the proton mass **uniquely selects it**. With the
canonical engine inputs `p_c = 8πα = 0.18340247…` and
`I_scalar = 1161.9870305…` (both imported from `src/ave/core/constants.py`,
NOT hardcoded here), the eigenvalue `x = I_scalar/(1 − V·p_c) + 1` evaluates to:

| V (hypothesis) | Physical reading | `x = m_p/m_e` | Δ vs CODATA 1836.1527 |
|---|---|---|---|
| `V = 1` | one reactance sector only | **1423.96** | −22.4% |
| `V = p_c` | per-channel coupling as the "count" | **1203.43** | −34.5% |
| **`V = 2`** | **two reactance sectors (additive count)** | **1836.117** | **−0.0019% (≈ −0.002%)** |
| CODATA | — | 1836.1527 | — |

**The mass uniquely selects additive-2-channel.** The integer 2 (not √2) is the
discriminator: it is a **discrete channel count**, not an RMS combination of the
two unit channels (√2 would be the RMS; the data rejects it). This is the
EE-form prediction of §1.3 confirmed empirically.

> **Reproduction (live engine read, 2026-06-01).** From repo root:
> ```python
> import sys; sys.path.insert(0, "src")
> from ave.core.constants import I_SCALAR_1D, P_C
> ratio = lambda V: I_SCALAR_1D/(1.0 - V*P_C) + 1.0
> ratio(1.0)   # 1423.9617
> ratio(P_C)   # 1203.4326
> ratio(2.0)   # 1836.1170   ← matches constants.PROTON_ELECTRON_RATIO exactly
> ```
> `PROTON_ELECTRON_RATIO = 1836.1170402290593` (`constants.py:775`); CODATA
> proton/electron = 1836.152673. The −0.002% deviation is the residual after the
> integer-2 channel count is fixed.

**Why this is a discriminator, not a fit (`ave-driver-script-honesty`
Discriminator 2).** `V` is not optimized against the proton mass — the three
candidate values `{1, p_c, 2}` are *a-priori physical hypotheses* (one sector /
coupling-as-count / two sectors), and only the physically-motivated
two-sector count lands on CODATA. There is no `minimize()` over `V`; the
spread between candidates (1424 / 1203 / 1836) is large and the selection is
unambiguous. This is forward-discrimination, not inverse-fit.

## §3 — Why the four "volume" derivations fail

The corpus carried FOUR independent "derivations" of `V = 2` as a geometric
volume. All four are unsound. Naming each failure mode (the point is not that
the *number* 2 is wrong — §2 confirms it — but that the *volume derivation* of
it is fabricated, and a fabricated derivation invites the next agent to "fix" a
number that is actually correct for a different reason).

### Failure 1 — `∫∫∫ sgn(det) = 0`, not 2 (signed-integral antisymmetry)

`constants.py:760` (pre-scrub) claimed:
> `V = ∫∫∫ sgn(det[τ₁, τ₂, τ₃]) dτ₁ dτ₂ dτ₃ = 2`

framed as "a topological invariant counting the chiral orientations." A **signed**
integral of `sgn(det[τ₁,τ₂,τ₃])` over three great circles parameterized by
angles `s_i ∈ [0,2π)` **vanishes by antisymmetry**: under `s_i → s_i + π` any
single tangent `τ_i → −τ_i`, which flips the sign of the determinant
(`det` is linear-alternating in its columns), so `sgn(det) → −sgn(det)`. The
shift `s_i → s_i + π` is a measure-preserving involution of the integration
domain, so the integrand is odd under it and the signed integral is `0`, not 2.
To get a positive 2 you would need `|det|` or an unsigned/oriented count — but
then it is no longer "the signed intersection integral" the docstring claimed,
and the specific value 2 does not follow from the integral as written. **The
integral as written evaluates to 0; the claim that it equals 2 is false.**

### Failure 2 — Geometric-inevitability §V_halo=2 asserts, does not compute

`manuscript/backmatter/03_geometric_inevitability.tex:277–285` (pre-scrub)
stated: "The geometric volume … is computed analytically from the signed
intersection integral of three great circles on S² … `V_halo = 2.0` … This is a
purely topological constant." It **asserts** the result and **labels** it
"computed analytically" but performs **no computation** — there is no integral
evaluated, no limit taken, no derivation shown. It inherits Failure 1's signed
integral by reference and adds an "S²" framing (the constants.py docstring said
S³ great circles; the .tex said S² — the surfaces don't even agree). Assertion
dressed as computation.

### Failure 3 — `tensors.py::compute_toroidal_halo_volume()` hardcodes 2.0

`src/ave/topological/tensors.py:40–51` (pre-scrub) docstring: "the total
integration analytically converges to exactly 2.0 perfectly." The code body is:
> ```python
> V_total = 2.0
> return V_total
> ```
> No integration is performed — the function returns a hardcoded literal while
its docstring claims an integration "converges perfectly." This is the canonical
`ave-driver-script-honesty` **Class B silent overclaim** (Discriminator 1
hardcoded-literal + Discriminator 4 narrative-claims-derivation): the docstring
asserts a computation the code does not do.

### Failure 4 — "FEM-verified 2.001 ± 0.003" has no FEM

`constants.py:768` (pre-scrub) and `01_appendices.tex:100` cite
"FEM: 2.001 ± 0.003 (Richardson N→∞)" as independent verification. There is **no
finite-element driver** in the repo that computes a toroidal-halo volume and
returns 2.001 — the number is asserted with a fabricated error bar and
Richardson-extrapolation provenance. A grep for an FEM halo-volume solver
returns nothing (the only `compute_toroidal_halo_volume` is Failure 3's
hardcoded stub). A 0.05%-precision "FEM-verified" claim with no FEM code is an
`ave-driver-script-honesty` Class B overclaim. (This branch scrubs the
constants.py + tensors.py instances; the `01_appendices.tex:100` +
`01_appendices.tex:72` instances are flagged for propagation in §6.)

### Why all four fail the SAME way

Each treats the integer 2 as a **geometric/topological volume** and back-fills a
"derivation" (signed integral, analytic assertion, hardcoded return, fabricated
FEM). The number is right; the *category* (volume) is wrong; and a wrong-category
quantity with a fabricated derivation is the most dangerous kind of corpus
content — it reads as rigor, survives skim review, and invites a future agent to
"correct" a value that is actually correct for the dual-reactance-count reason
of §1. The reframe to reactance-count removes the false-derivation surface
entirely: a channel count is not integrated, it is *counted* (there are two
sectors per Axiom 1).

## §4 — Honest status: count-2 closed, per-channel p_c residual, "1-residual Skyrme"

`ave-evidence-framing-discipline` + `consistency-vs-emergence`. The eigenvalue
`x = I_scalar/(1 − V·p_c) + 1` has these inputs, with honest per-input status:

| Input | Value | Status | Class |
|---|---|---|---|
| `V` (reactance count) | 2 | **CLOSED** — forced reactance-sector count (§1), mass-confirmed at exactly 2.000 (§2) | identity / manifestation |
| `I_scalar` | 1161.987 | engine-computed (Faddeev-Skyrme 1D solver, `κ_FS/c` confinement + Ax4 saturation + δ_th thermal softening) | manifestation |
| `p_c` (per-channel coupling) | 8πα = 0.1834 | **RESIDUAL** — canonical-packing-plausible (`p_c = 8πα` is algebraically exact given α; the 4π in α cancels the 8π), but the identification of `p_c` as the *per-channel reactance coupling* is not line-by-line derived | consistency |
| `+1` (charge twist) | 1 m_e | Ax2 TKI integer twist (global charge constraint) | manifestation |

### The honest framing: "1-residual Skyrme", NOT "zero-parameter"

Standard Skyrme has **2 tuned parameters** (F_π, e), both fit to baryon data.
The AVE ladder replaces both with substrate constants
(`ℓ_node = ℏ/m_e c`, `κ_FS = 8π`) and adds the integer reactance count `V = 2`
+ integer crossing number `c` + integer charge twist `+1`. What remains is **one
residual**: the per-channel coupling `p_c = 8πα`, whose *identification* as the
reactance-loop gain is canonical-packing-plausible but not derived step-by-step.

So the honest headline is **"1-residual Skyrme"** (1 residual: per-channel p_c;
vs standard Skyrme's 2 baryon-data-tuned params), or equivalently **"1-anchor"**
(the one anchor being p_c's role). It is NOT "zero-parameter" — that headline
overstates by treating the p_c-as-loop-gain identification as derived when it is
plausible-but-residual.

> **Distinction that survives (do not over-walk-back).** The parsimony claim
> "**zero baryon-data-tuned parameters**" (the inputs are electron-physics-
> provenanced — m_e, α — NOT fit to baryon masses) is a SEPARATE and largely-
> defensible claim. The reframe target is the absolute "zero-parameter" /
> "zero free parameters" phrasing, which the per-channel-p_c residual
> contradicts. Where the corpus says "zero baryon-data-provenanced parameters"
> or "Skyrme's two parameters replaced by substrate constants," that framing
> stands; where it says bare "zero-parameter" / "zero adjusted parameters" for
> the baryon-mass eigenvalue, it should become "1-residual (per-channel p_c)."
> This split is the load-bearing reason §6 surfaces the broader propagation for
> Grant's boundary call rather than mass-editing every "zero-parameter" hit.

### Consistency-vs-emergence note

The matrix C8-BARYON-LADDER row + foreword currently headline this as a
"Class 4 emergence test." With the p_c residual made explicit, the eigenvalue is
better read as **manifestation + one consistency-class input (p_c)**, not clean
emergence — the same caution `consistency-vs-emergence` raises for
CODATA-derived inputs threaded through SI substitution. Whether to re-tag the
matrix/foreword emergence-class headline is a framing decision surfaced in §6
(NOT executed on this branch).

## §5 — Cleanup list (what this branch changes + what stays open)

### Landed on this branch (`analysis/baryon-v2-reactance-scrub`)

1. **This result doc** — `research/2026-06-01_baryon-V2-dual-reactance-closure.md`.
2. **NEW glossary leaf** —
   [`dual-reactance-storage-taxonomy.md`](../manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md)
   (`no-claim` definitional leaf; the 7 V-symbols disambiguated, the 3 distinct
   2's, X_L/X_C/E_L/E_C definitions, the signed-cancellation note,
   V_TOROIDAL_HALO = dual-reactance count).
3. **`src/ave/core/constants.py:752–770`** — V_TOROIDAL_HALO docstring rewritten:
   dual-reactance count, NOT a geometric volume; false `V=∫∫∫sgn(det)=2` claim
   deleted; cross-refs to this doc + the glossary leaf. **Value kept at 2.0.**
4. **`src/ave/topological/tensors.py:40–51`** —
   `compute_toroidal_halo_volume()` docstring rewritten: honest (returns the
   dual-reactance count = 2; NOT an integration); false "converges to exactly
   2.0 perfectly" claim removed.
5. **`manuscript/backmatter/03_geometric_inevitability.tex:275–285`** — §"Toroidal
   Halo Volume" reframed: dual-reactance count, not a "purely topological volume
   constant."
6. **`translation-circuit.md` §4.5 (EE Analytical Tool Tracker)** — new row
   (baryon self-feedback ↔ regenerative dual-reactance LC loop / Black's
   closed-loop form; V=2 = X_L+X_C unit reactances; validation ⚠); tally bumped;
   §6 means-test corpus entry added for the mass-discriminator.
7. **Three named "zero-parameter" → "1-residual" reframes** (deliverable 7):
   `self-consistent-mass-oscillator.md:64`, `constants.py:795`,
   `torus-knot-ladder-baryons.md:19`.

### Stays open (surfaced in §6 for Grant's propagation-boundary call)

- The per-channel-p_c **residual** is not line-by-line derived (canonical-
  packing-plausible). Closing it (a substrate-mechanism derivation of `p_c` as
  the reactance-loop gain) is the open physics item.
- The broader "zero-parameter" baryon-ladder propagation (foreword, matrix
  C8-BARYON-LADDER row, proton-identification.md, vol2/index.md, vol4
  falsification leaves, `02_baryon_sector.tex` mirrors, vol2/claim-quality.md)
  + the `01_appendices.tex` FEM-claim instances — classified inventory in §6.

## §6 — Flag-don't-fix findings

Per flag-don't-fix + lane discipline: I surface these; I do NOT silently resolve
them on this branch.

### Flag A — "zero-parameter" baryon-ladder propagation boundary (needs Grant)

`ave-walk-back` Step 3h-exhaustive grep for the baryon-ladder "zero-parameter"
overclaim surfaced ~20 sites beyond the 3 named deliverable-7 files. The brief
named 3 files explicitly; the broader set carries COMPOUND framing ("flagship
axiom-derived mass prediction", "Class 4 emergence test", foreword "Third
positive load-bearing confirmation") that interacts with `consistency-vs-
emergence` classification — a framing-level decision. **I executed the 3 named
files + their direct `.tex` mirrors only; the rest awaits Grant's boundary
call.** Classified inventory (grep:
`zero.parameter|No parameters are adjusted` ∩ baryon-eigenvalue context, from
repo root, excluding `.index/`):

**LOAD-BEARING (reframe target — bare "zero-parameter" for the baryon eigenvalue):**
- `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md:11,19` — *(19 reframed this branch; 11 "zero-parameter prediction of the entire baryon resonance spectrum" NOT yet — same file, sibling line; flagged for same-PR or boundary call)*
- `self-consistent-mass-oscillator.md:64` — *(reframed this branch)*
- `constants.py:795` — *(reframed this branch)*
- `proton-identification.md:13,39` — "genuinely zero-parameter … flagship axiom-derived" (×2, compound framing)
- `vol2/index.md:21` — "zero-parameter self-consistent eigenvalue equation"
- `vol2/particle-physics/ch02-baryon-sector/index.md:11` — "zero-parameter eigenvalue"
- `vol4/falsification/ch12-falsifiable-predictions/baryon-mass-predictions.md:10,45` — "zero-parameter mass spectrum" + "zero adjusted parameters"
- `vol4/falsification/ch12-falsifiable-predictions/torus-knot-baryon-predictions.md:14`
- `vol2/claim-quality.md:82,1371` — "genuinely zero-parameter, 0.002% from CODATA — AVE's flagship"
- `divergence-test-substrate-map.md:446` — matrix C8 row "Class 4 emergence test … 1-input zero-parameter spectrum"
- `frontmatter/00_foreword.tex:116` — "Third positive load-bearing confirmation … zero free parameters at each anchor"

**LaTeX MIRRORS of the 3 named leaves (`ave-walk-back` 3b — reframed this branch):**
- `manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:215,233` — mirror of
  `self-consistent-mass-oscillator.md:64` + `torus-knot-ladder-baryons.md:19`.
- *(also `02_baryon_sector.tex:226,259,398` carry "zero-parameter/zero adjusted"
  baryon-spectrum prose — sibling lines, flagged for boundary call)*

**SEPARATE CLAIM — do NOT reframe (different "zero-parameter", legitimately so):**
- `vol3/.../thermal-softening-skyrme.md:56` + `11_thermodynamics_and_entropy.tex:309,406`
  — the δ_th *thermal correction* is a separate geometric result; "zero-parameter"
  there is about ν_vac + κ_cold, not the V=2 eigenvalue.
- `vol3/.../lunar-inductive-heating.md:22` — already honestly hedged ("not a
  zero-parameter prediction").
- `vol6/.../executive-abstract.md:52` + `vol_6_periodic_table/.../00_introduction.tex:58`
  — Vol 6 nucleus K-coupling; R is fit per nucleus (a DIFFERENT, already-honest
  framing). Leave alone.
- `torus-knot-ladder.md:21` + `01_topological_matter.tex:171` — "zero empirical
  fits" re κ_FS import; defensible (κ_FS IS imported from constants). Borderline;
  flagged.

**FROZEN-SNAPSHOT (Q2-exempt per `ave-walk-back` 3h-exhaustive-3 — no change):**
- `claim-quality-closure-roadmap.md:132` (dated journal entry).
- `ave-kb/session/grants-random-tangents.md:50,124` (session scratch).
- `research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md:3337,4019` (archive).

> **Boundary question for Grant:** propagate the reframe to the full
> LOAD-BEARING set (foreword + matrix + proton-id + vol4-falsification +
> vol2/index + claim-quality + remaining `02_baryon_sector.tex` lines) in this
> branch, or scope this branch to the V=2 reframe + 3 named files only and queue
> the "zero-parameter→1-residual" propagation (which interacts with the
> emergence-class re-tag) as a follow-up? I did the unambiguous V=2 mechanism
> work + the 3 named files; the emergence-class-touching propagation is held.

### Flag B — `01_appendices.tex` carries the fabricated-FEM provenance (×2)

`manuscript/backmatter/01_appendices.tex:72` ("`V_total = 2.0` is the FEM-verified
Borromean halo volume") + `:100` ("FEM: 2.001 ± 0.003, Richardson N→∞"). This is
Failure 4 (§3) — a 0.05%-precision FEM claim with no FEM driver in the repo.
NOT in the brief's named deliverable list; flagged for the same propagation call
as Flag A. The honest reframe: drop "FEM-verified / 2.001 ± 0.003 Richardson"
and replace with "the dual-reactance count = 2 (see
[`dual-reactance-storage-taxonomy.md`](../manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md))."

### Flag C — S² vs S³ surface disagreement in the false derivations

The pre-scrub `constants.py:758` said the three great circles trace on **S³**;
`03_geometric_inevitability.tex:279` said **S²**. The two false derivations of
the same "volume" did not even agree on the manifold. Documented here as
corroborating evidence that the geometric derivation was never real (a genuine
computation would fix the surface). No action beyond the scrub — noted so the
auditor sees the internal inconsistency was present.

### Flag D — prose rounding in `self-consistent-mass-oscillator.md` (minor, not a contradiction)

`self-consistent-mass-oscillator.md:51` shows `x_core = 1162/0.6332 ≈ 1835.12`
then `+1 = 1836.12` (rounded `I_scalar = 1162`, `p_c = 0.1834`). The engine's
exact `I_scalar = 1161.987` gives `PROTON_ELECTRON_RATIO = 1836.117`, not
1836.12. This is prose rounding, NOT a contradiction (1836.12 ≈ 1836.117 to
prose precision; both are −0.002% from CODATA). Noted for completeness; no
change needed.

---

## Verification log (`verify-before-cite`)

Every file:line + value in this doc was verified live this session:
- Engine values (`I_SCALAR_1D`, `P_C`, `PROTON_ELECTRON_RATIO`,
  V=1/p_c/2 ratios) — read via live `python` import of `ave.core.constants`
  (§2 reproduction block); not hardcoded.
- `constants.py:760,770,774,775,795` — Read + grep confirmed.
- `tensors.py:40–51` — Read confirmed (hardcoded `V_total = 2.0`).
- `03_geometric_inevitability.tex:275–285` — Read confirmed (S² + "purely
  topological constant").
- `translation-circuit.md:35` — Read confirmed (E/B conjugate / capacitive +
  inductive sectors); §4.5 tracker (23 rows, 15✓/5⚠/3✗) + §6 (24 entries) Read.
- `vol1/claim-quality.md:135,145,1391` — Read confirmed (K=2G downstream-of-
  Golden-Torus + √2 speed ratio clm-uu1qbo).
- `zero-parameter-universe.md:32` — Read confirmed (K/G=2 "self-consistency
  check, not an independent derivation of α"); path corrected to
  `vol1/axioms-and-lattice/ch1-fundamental-axioms/`.
- `self-consistent-mass-oscillator.md:64`, `torus-knot-ladder-baryons.md:19`,
  `proton-identification.md:13,39` — Read confirmed.
- `01_appendices.tex:72,100` — grep confirmed (FEM 2.001 ± 0.003 claim).
- Baryon-ladder "zero-parameter" propagation inventory — exhaustive grep
  (`ave-walk-back` 3h-exhaustive) from repo root, classified above.
