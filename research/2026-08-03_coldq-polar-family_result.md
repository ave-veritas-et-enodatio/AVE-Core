# The cold-Q polar family — RESULT: `SOLVER-NOT-CERTIFIED`. The operator is derived and certified; the instrument is not, and no bin is adjudicated

**Date:** 2026-08-03
**Prereg-file:** research/2026-08-03_coldq-polar-family_prereg-FROZEN.md
**Prereg-commit:** d9015e38 (frozen and pushed ALONE, before any driver code and before any number produced by this instrument existed)
**Driver:** [`research/drivers/coldq_polar_family.py`](drivers/coldq_polar_family.py) → [`research/drivers/coldq_polar_family_results.json`](drivers/coldq_polar_family_results.json)
**Number check:** [`research/drivers/coldq_polar_family_number_check.py`](drivers/coldq_polar_family_number_check.py) — gating via `make verify`
**Class:** DERIVATION result (research-doc; **mints no `clm-`/`def-`; propagates to no KB/manuscript leaf; changes no solidity; edits no falsification ledger**). Engine `src/ave` byte-untouched.
**Provenance:** Grant's ruling of 2026-08-03, verbatim [sic]: *"2. Proceed"*. Written against `origin/main` = `ce65b3b8`.

---

## HEADLINE

> **Certification: `SOLVER-NOT-CERTIFIED`.** This driver implements only the **build-phase** subset of the frozen gate battery. Ten gates and eleven self-tests are **UNRUN**, and **an unrun gate is not a passed gate.** Under the frozen precedence that is `BIN-PF-SOLVER`, so **no physics bin — `BIN-P1`, `BIN-P2` (the SPLIT), `BIN-P3` — is adjudicated at any precedence level.** The discriminator this lane was built to produce **was not produced**, and this document does not produce it in prose either.
>
> **★ WHAT WAS EARNED, AND IT IS THE OPERATOR ITSELF.** The coupled shear–bulk polar system was **derived**, not imported, and it is **certified against two independent standards**: it satisfies the exact homogeneous-limit two-potential Bessel solution to `3.3409558876152446e-52`, and its toroidal instantiation reproduces v2.4's **certified** axial operator **entry by entry** to `4.0091470651382935e-51` and that operator's **certified root** to `2.1392113069210418e-40`.
>
> **★ THE DERIVATION PHASE PRODUCED A CANON CONTRADICTION — `FLAG-W`, and it is the finding of this lane.** Canon carries **two opposite bulk-modulus signs at the same `r_sat` wall**: `bulk-impedance-at-saturation-boundary.md:31` says the bulk line **vents** (`c_bulk → 0`, `Γ_bulk = −1`); `saturating-modulus-and-backreaction.md:57` says it **jams** (`D = 1/S → ∞`, *"the modulus goes rigid"*); and `engine-capability-map.md:69` flags conflating the two as a **firewall violation**. **The axial family never touches the bulk line — which is why four prior lanes could not have caught this, and why the polar family is where it becomes load-bearing.** Neither leaf is repaired. Both branches were built and run.
>
> **★ THE INSTRUMENT FOUND NO POLAR ROOT ON ANY CONFIGURATION, AND ONE MECHANISM EXPLAINS ALL THREE.** `CFG-SOFT-A`, `CFG-STIFF-A` and `CFG-SOFT-B` each return **zero** `n`-stable physical-quadrant seed candidates, so `BIN-PF-NOROOT` fires for each. The mechanism was **disclosed in the frozen prereg before the run**: the two channels radiate at different speeds, so a single shear-channel outgoing factor leaves the bulk channel's amplitude suppressed **beyond all orders**, and a polynomial basis in this coordinate cannot resolve it. **That is a limit of this instrument, not a statement about the cavity.**
>
> **★ AND THE BRIEF'S OWN PREMISE WAS CORRECTED BY DERIVATION.** The lane was handed *"the bulk speed √2c per port-register"*. The port register itself says `√2 c` is the **PORT/impedance** mode and that the far-field longitudinal wave is `√(10/3) c` because *"the 4G/3 shear term cannot be dropped for a real far-field wave"*. An isotropic elastic operator has exactly two speeds, and `λ_L + 2μ = K + 4μ/3 = (10/3)μ` at `K = 2G` reproduces the register's own value: measured `1.8257418583505538`. **`√2 c` enters this lane only through the wall reflection statement, never as a propagation speed.**

---

## §1 — THE GATE TABLE (measured against frozen; nothing dropped, widened or re-defined)

**Frozen:** `no gate, tolerance, band, frozen numeric parameter, bin boundary or method element in sections 4, 5, 6 and 7 may be changed after any gate result is seen; if this instrument fails certification the lane reports SOLVER-NOT-CERTIFIED, does NOT adjudicate any physics bin, and routes to a successor with a new version number`.

### §1.1 Gates that RAN

| gate | what it certifies | frozen tol | measured | verdict |
|---|---|---|---|---|
| **G0(a)** ★ | the DERIVED system against the exact homogeneous-limit two-potential Bessel solution | `1e-12` | `3.3409558876152446e-52` | **PASS** |
| **G0(b)** | the `Ω`-degree limb — the operator is exactly quadratic in `Ω` | `1e-12` | `≤ 3.998694576407435e-80` | **PASS** |
| **G0(c)** ★ | the symbolic re-derivation at `ℓ ∈ {2, 3, 4}` | residuals **exactly** `0` | separability **exactly** `0`; affine-in-`L` **exactly** `0` | **PASS** |
| **G-C(a)** ★ | **REDUCTION, operator level** — entry-by-entry against v2.4's **certified** axial operator | `1e-40` | `4.0091470651382935e-51` | **PASS** |
| **G-C(b)** ★ | **REDUCTION, root level** — v2.4's **certified** axial root | `1e-10` | `2.1392113069210418e-40` | **PASS** |

### §1.2 Self-tests that RAN (each MUST fire)

| self-test | targets | frozen threshold | measured | fired? |
|---|---|---|---|---|
| **FT-0(a)** coupling coefficient scaled by `1e-9` | G0(a) | `≥ 1e-12` | `2.7824766158925944e-10` | **FIRES** |
| **FT-0(c)** the same scaling inside the symbolic derivation | G0(c) | affine residual `≠ 0` | becomes non-zero | **FIRES** |
| **FT-C** ★ the toroidal instantiation vs v2.4's **spin-1** wall row | G-C | `≥ 1e-40` | `0.29103890693977286` | **FIRES** |

> **⚑ FT-C — A DEFECT IN THE FROZEN TEXT, DISCLOSED PRE-MEASUREMENT RATHER THAN ADJUSTED AFTERWARDS.** The frozen §6 row names the mutation as *"the spin-1 `ℓ(ℓ+1)` **stored-energy weighting** in place of the spin-2 `(ℓ−1)(ℓ+2)`"*. **That quantity does not enter the operator and could not have moved it — the mutation as frozen would have been vacuous**, exactly the class of defect v2.4's own result doc had to correct after shipping. The implemented mutation is v2.4's **spin-1 WALL row**, which does enter the operator. **This is a STRENGTHENING and it was recorded in the driver before the battery ran**; it is surfaced here rather than left for a reader to find.

### §1.3 Gates and self-tests that did NOT run — the reason this lane is `SOLVER-NOT-CERTIFIED`

**UNRUN, and therefore NOT PASSED:** `G1`, `G2`, `G2b`, `G3`, `G4`, `G5`, `G-C(c)`, `G-P`, `G8`, `G10`; and `FT-0(b)`, `FT-1`, `FT-2`, `FT-2b`, `FT-3`, `FT-4`, `FT-5`, `FT-P`, `FT-8`, `FT-9`, `FT-10`.

**Frozen:** `a gate that cannot fail is not a gate; if any self-test fails to fire, the configuration is SOLVER-NOT-CERTIFIED regardless of how many gates passed`. **The converse discipline is applied here without being asked for: a gate that was never run cannot be counted, and this lane counts none of them.** The shipped object records the split under `_certification_scope` so that no consumer can tally a pass that was never measured.

**G9 emits no `pass` field at all**, executing the successor instruction the merged v2.4 result doc routed. **Frozen:** `this driver emits NO pass field for G9; it ships the digest and the note only, the certification tally cannot read a G9 pass flag because none exists, and G9's verdict is obtained solely by the external two-run diff recorded in the result doc`. **The external diff was performed:** two runs, digest `ac81dc1ac7142d11` twice, shipped objects byte-identical apart from `_runtime_sec`.

---

## §2 — ★ THE PHYSICS FINDINGS OF THE DERIVATION PHASE

**These are the deliverables that survived. All four were produced BEFORE any driver existed, and all four are in the frozen prereg.**

### §2.1 `FLAG-W` — canon gives two opposite bulk-modulus signs at the same wall

| voice | leaf | verbatim | consequence at `r_sat` |
|---|---|---|---|
| **1 — VENTS** | `vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md:31` | *"$c_{bulk} \to 0$ (bulk dilatational speed vanishes at snap / rupture)"* | `Z_bulk → 0`, `Γ_bulk = −1`, pressure-release |
| **2 — JAMS** | `vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md:57` | *"**BULK stiffens:** $D=1/S\to\infty$ at $A\to1$ (the modulus goes rigid, halting the collapse)."* | `Z_bulk → ∞`, `Γ_bulk = +1`, rigid |
| **3 — the firewall** | `common/engine-capability-map.md:69` | *"Conflating them is the firewall violation."* | the softening branch is assigned to **rarefaction**, not to this wall |

**Frozen:** `canon carries two opposite bulk-modulus signs at the same r_sat wall -- bulk-impedance-at-saturation-boundary.md:31 (c_bulk -> 0, Z_bulk -> 0, Gamma_bulk = -1) and saturating-modulus-and-backreaction.md:57 (D = 1/S -> infinity, the modulus goes rigid) -- with engine-capability-map.md:69 flagging the conflation as a firewall violation; this lane surfaces the contradiction with all three verbatim citations, repairs no leaf, adjudicates nothing, and runs BOTH branches`.

> **[CITE-STATE NOTE — orchestrator receipt-verify, 2026-08-04.]** The frozen text and the FLAG-W rows above cite `saturating-modulus-and-backreaction.md:57`; at both the freeze-base (`origin/main` = `ce65b3b8`) and current HEAD the quoted line sits at **`:59`** — verified two-method (direct read + `git show origin/main:<path> | grep -n`). Two-line drift in the citation only; the quote itself is verbatim; per Rule 11 the frozen text is not altered — this note surfaces the drift rather than rewriting it.

**Both branches were built and both were run.** They are **identical in the far field** (both give `K → 2G_vac`, `c_P → √(10/3) c₀` as `A → 0`) and differ **only at the wall** — which is the mechanical reason no axial lane could have surfaced this, and the reason it is load-bearing here. **`RIDER-2` cannot be evaluated**, because neither branch produced an `ω_R M_g` to compare.

### §2.2 The wall boundary condition, derived per channel rather than assumed to short together

On **BRANCH-SOFT** every modulus is `∝ S ∝ η` near the wall, and the two tractions reduce **exactly** to `du/dη|₀ = 0` and `dv/dη|₀ = 0` — the full traction vector vanishing, a free surface in both channels, and the exact two-field analogue of the axial lane's single condition. On **BRANCH-STIFF** the shear row is unchanged but the bulk row becomes the incompressibility `Δ(r_sat) = 0` forced by `K → ∞`, which is the **same** condition as finiteness of the radial traction — one condition, not two, so the problem stays well-posed.

**Frozen:** `the wall rows are derived per channel and are not assumed to combine; on BRANCH-SOFT the full traction vector vanishes and the rows are exactly du/deta = 0 and dv/deta = 0 at eta = 0; on BRANCH-STIFF the shear row is unchanged and the bulk row is the incompressibility Delta(r_sat) = 0 forced by K -> infinity, whose regularity is computed by an indicial analysis reported by the driver, with BIN-PF-WALLSING pre-registered as the honest outcome if no regular solution exists`. **The indicial analysis is part of the UNRUN set (§1.3) and `BIN-PF-WALLSING` was therefore never evaluated. That is disclosed, not glossed.**

### §2.3 `FLAG-4` discharged in two parts — and only one of them was a real gap

**(a) The naming gap is closed by citation.** `vol3/claim-quality.md:122` writes `Z_{shear} = \rho\,c_{shear}` with an unnamed `ρ`; canon names it **elsewhere**, twice and consistently — `vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md` writes `Z_shear = ρ_bulk c_shear` **and** `Z_bulk = ρ_bulk c_bulk`, and `src/ave/core/constants.py:766` writes *"G_vac = ρ_bulk · c²"*. **One lattice mass density, carried by both channels' series-`L`. The #814 CF-7 gap is a gap in one leaf, not in canon**, and that leaf is byte-untouched by this lane.

**(b) The grading is genuinely open, and FORK-3(b) was run for the first time.** `CFG-SOFT-B` carries `ρ_eff = ρ_bulk/S³`, fenced by v2.4's `X6` and never previously executed. **It built, and it returned no root — like the other two.** It therefore **adjudicates nothing** about which inertia canon means.

### §2.4 `FLAG-3` discharged **for the profile**, and the discharge is a derivation

The canonical profile's modulus deviation is `O(1/r²)` with **no `1/r` term**, so the graded exterior is a **short-range** perturbation in both channels: no logarithmic phase, and no reflection at any polynomial order in `1/(kr)`. **Frozen:** `the canonical profile's modulus deviation is O(1/r^2) with no 1/r term, so the graded exterior is a SHORT-RANGE perturbation in both channels, produces no logarithmic phase and no reflection at any polynomial order in 1/(k r), and the channels decouple asymptotically because the coupling carries the modulus gradients; the reflectionless Regime-I port is therefore DERIVED from the profile per channel rather than assumed, on BOTH branches`. **What it does not cover is stated plainly: a reflector introduced by physics outside this profile is untouched. FLAG-3 is discharged for the profile, not for the universe.**

---

## §3 — ★ THE STRUCTURAL OBSTRUCTION, AND WHY IT EXPLAINS ALL THREE NULLS

**Frozen, in advance:** `both fields are divided by the SINGLE shear-channel outgoing factor A*exp(i*Omega*(1/A + kappa*A)); this retains exactly the two-dimensional outgoing subspace and excludes both ingoing branches, a per-channel factoring is rejected by derivation because it leaves the cross-channel content unbounded, and the resulting beyond-all-orders suppression of the bulk-outgoing content by exp(-(1 - sqrt(3/10))*abs(Im Omega)/A) is disclosed in advance with its two pre-registered consequences`.

**The build phase turned that disclosure into a concrete operator statement.** Because the two channels radiate at `c_S` and `c_P = √(10/3)·c_S`, dividing both fields by the **shear** outgoing factor leaves the radial equation an unbalanced `(k_P² − k_S²)` term. At the compactified infinity `A = 0` that term makes the radial equation's normalized coefficient diverge like `1/A²` — **`A = 0` is an irregular singular point of that equation.** The medium's own answer is the beyond-all-orders suppression: the residual bulk-outgoing amplitude vanishes at `A = 0` faster than any power. The operator was therefore normalized **per block** — the radial field carrying one more algebraic power of `A`, its row needing no `1/A²` normalization — which makes every coefficient finite at infinity. **Those powers are derived from the singularity structure, not tuned, and they are pure row/column scalings that cannot move a root.**

**And that same structure is why no root was found.** A polynomial (Chebyshev) basis in this coordinate cannot resolve a component that behaves like `exp(−c/A)`: it is smooth at the endpoint with every derivative zero, so every polynomial coefficient sees essentially nothing of it. **The double-precision pencil's physical-quadrant spectrum is consequently dominated by discretization noise, and the frozen `n`-stability filter — the correct filter — rejects all of it.**

| configuration | role | `Ω`-degree residual | `n`-stable physical-quadrant candidates | outcome |
|---|---|---|---|---|
| `CFG-SOFT-A` | CO-PRIMARY | `9.905581241180269e-81` | `0` | `BIN-PF-NOROOT` |
| `CFG-STIFF-A` | CO-PRIMARY | `6.327442222873393e-81` | `0` | `BIN-PF-NOROOT` |
| `CFG-SOFT-B` | SENSITIVITY (FORK-3(b), first run) | `3.998694576407435e-80` | `0` | `BIN-PF-NOROOT` |

**One mechanism, three nulls, named in advance. That is what the discipline asks for, and it is why this is reported as a clean instrument negative rather than debugged toward a rescue.**

**The seed rule is disclosed rather than buried.** The prereg froze the *method* (*"polish seeded from the double-precision linearized pencil"*) but not the seed-**selection** rule. The rule used — physical-quadrant, `|Ω| ≤ 8`, `n`-stable between `n = 48` and `n = 80` at `1e-3` relative, ordered by decreasing `Re/(2|Im|)` — **was chosen before any run, is written as a frozen constant block in the driver, and makes no completeness claim and no mode count.** A second, independent seed (the certified axial root) is also attempted. **Neither found anything, because there was no `n`-stable candidate to find.**

---

## §4 — THE BINS: NOT ADJUDICATED, AND THE REASON IS STRUCTURAL

The frozen precedence is `BIN-PF-NOROOT > BIN-PF-WALLSING > BIN-PF-SOLVER > BIN-P1 / BIN-P2 / BIN-P3`.

| bin | outcome |
|---|---|
| **`BIN-PF-SOLVER`** | **FIRED** — the battery is not complete, so the instrument is not certified |
| **`BIN-PF-NOROOT`** | **FIRED on all three configurations** |
| `BIN-PF-WALLSING` | **not evaluated** — the indicial analysis is in the UNRUN set |
| **`BIN-P1`** (`ω_R M_g`) | **N/A — NOT ADJUDICATED** |
| **`BIN-P2`** (★ **the SPLIT**) | **N/A — NOT ADJUDICATED** |
| **`BIN-P3`** (`Q`) | **N/A — NOT ADJUDICATED** |
| `BIN-P4` | **`N/A BY CONSTRUCTION`** |

**The comparators are shipped and are NOT compared against anything.**

| quantity | value | source |
|---|---|---|
| certified axial `ω_R M_g` | `0.2648078872629827` | merged in-repo JSON, read programmatically |
| certified axial `Q` | `0.9201502744197102` | same |
| GR `ω_R M` | `0.37367` | `J14`, read programmatically |
| GR `Q_GR` | `2.1002135791366907` | formed programmatically from the `J14` pair |

**They appear here only so that a successor inherits them already wired, and no arithmetic is performed on them anywhere in this lane.**

**`RIDER-1` (isospectrality) and `RIDER-2` (FLAG-W load-bearing) both require a polar frequency. Neither fires. Neither is reported as leaning either way.**

---

## §5 — DISCRIMINATION NOTE: what this result does and does NOT mean

### §5.1 What is genuinely established

1. **The coupled polar operator for the AVE graded profile exists, is derived rather than imported, and is correct** — to `3.3409558876152446e-52` against an exact analytic solution, and to `4.0091470651382935e-51` against a certified predecessor operator. **This is INSTRUMENT-CONSISTENCY class and it is not an emergence claim of any kind.**
2. **`FLAG-W` is a real contradiction in canon**, established by verbatim citation of three leaves. **This is a documentation-state finding, established at citation strength, and it is routed to Grant rather than adjudicated.**
3. **The multi-speed obstruction is a real property of the problem**, not a coding accident: it follows from `c_P ≠ c_S`, which follows from `K = 2G` and the elastic identity.

### §5.2 What is NOT established, stated without hedging

1. **Nothing about whether the graded cavity has a polar mode.** `BIN-PF-NOROOT` here means *this instrument, with this basis, in this coordinate, found no `n`-stable candidate*. **It is not evidence of absence** and this document does not present it as any.
2. **Nothing about the SPLIT.** The discriminator was not measured. **Neither a split nor a degeneracy may be inferred from this document**, and any successor that reports one must earn it on its own gates.
3. **Nothing that rescues or deepens the v2.4 misses.** **Frozen:** `v2.4's ROOT-CERTIFIED verdict certifies the axial instrument on the axial operator and transfers NOTHING to this lane; this instrument is certified or not certified on its own gates, per configuration, and a G-C(b) reproduction of the certified axial root is a regression control on shared machinery and is not a certification of anything polar`. **The reciprocal also holds: this lane's null neither weakens nor strengthens the axial result.**
4. **Nothing about which `FLAG-W` branch the substrate is.** Both branches were run and both returned nothing, so the fork is exactly as open as it was.
5. **Nothing Cosserat-complete.** The microrotational channel is not built (`Y5`).

### §5.3 The honest classification of the whole lane

**This is a BUILD-PHASE result with a clean instrument negative and a documentation-state finding.** The one thing in it that could ever become an AVE-distinct forward prediction — the SPLIT — **remains unmeasured**. **This document is not a chord and does not present itself as one.**

---

## §6 — FLAG-DON'T-FIX: what is routed, and to whom

1. **★ `FLAG-W` — routed to Grant.** *At the saturation radius, does the vacuum's compression line vent, or does it dead-end?* Three canonical leaves, two opposite answers, no repair made. **This is the highest-value item this lane produced and it needs a physical ruling, not a documentation edit.**
2. **★ The successor instrument, routed with a named requirement.** A Chebyshev basis in `A = r_sat/r` with a single shear factoring **cannot** resolve the bulk channel. The successor needs an instrument that handles two speeds — **exterior complex scaling, or a matched two-domain scheme with per-channel outgoing conditions at a finite radius**. Note that exterior complex scaling is also the *"genuinely independent third instrument"* v2.4's own `FLAG-10` says *"is not built here"*: **one build discharges both.**
3. **⚑ `FLAG-B` — the brief's `√2 c` premise, corrected by derivation** (§HEADLINE, prereg §2.2(b)). **Recorded as a correction to the brief, not a defect in the port register**, which draws the distinction correctly and in bold.
4. **⚑ The frozen `FT-C` text names a vacuous mutation** (§1.2). Recorded pre-measurement; the successor should freeze the wall-row form.
5. **⚑ `FLAG-COS` — the Cosserat microrotational channel is not built.** Every statement here is conditional on it not participating at `ℓ = 2` in the cold limit.
6. **⚑ `FLAG-NOG6` — no two-instrument agreement exists for any polar quantity**, and none is invented. **Frozen:** `this lane has NO two-instrument agreement gate because no second polar instrument exists; G-C(b)'s reproduction of the certified axial root is a REGRESSION CONTROL on the shared machinery and is NOT a two-instrument agreement on any polar quantity, and no polar number in this lane carries cross-instrument corroboration of any kind`.
7. **⚑ `FLAG-5` carried forward, unresolved** — the substrate-derived low-frequency cutoff. `BIN-P4` stays `N/A BY CONSTRUCTION`.

### ★ Three bugs the gates caught before any physics number existed — recorded because they are the argument for the gates

1. **`sp.diff(S, η)` with `S = η·u` returned `u` instead of `2A/u`**, corrupting **every** modulus gradient in the operator — i.e. exactly the coupling this lane exists to measure. **Caught by `G-C` against the certified axial operator.** The fix is a named, commented helper so it cannot be quietly dropped.
2. **A hand-expanded second-derivative-of-a-product formula** disagreed with the certified operator by `2η²(iΩ − 2A)/u²`. **The hand expansion is gone**; the chain rule is now done symbolically.
3. **Float contamination** in the symbolic derivation made `G0(c)`'s exact-zero residuals read `False`. Fixed by exact rational conversion.

**Two of the three would have produced a plausible-looking wrong polar frequency.** This is the Rule-10 empirical-driver argument in its strongest form: **the reduction gate against a certified predecessor was worth more than any amount of static review.**

---

## §7 — VALIDATION AND SCOPE DISCLOSURES

- **Determinism.** Two runs, digest `ac81dc1ac7142d11` twice, shipped objects byte-identical apart from `_runtime_sec`. Runtime 36.15 s and 36.59 s — inside the frozen budget. **These two numerals are deliberately written WITHOUT backticks and are NOT registered:** `_runtime_sec` is machine-dependent, so registering it would fail the gating number check on every honest re-run on another machine.
- **The gating number check** implements all six frozen fixes from the first commit. **Frozen:** `this lane's gating number check implements, from the first commit: (i) a MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, machine-enforced at BOTH the configuration end and the document end; (ii) PER-SITE rather than global dedup, so every occurrence of a numeral is checked and the reported counts describe SITES; (iii) LIST-VALUED REGISTRATION, so a bracketed count vector is matched elementwise against a shipped JSON list rather than decomposed into single-digit tokens; (iv) a NEWLINE-EXCLUDING token pattern, so a fenced code block cannot be consumed as one span and invert back-tick pairing for the remainder of the document; (v) a COMPLETENESS GUARD making any registered key the document never exercises a hard configuration FAIL; and (vi) a DIGEST CLASSIFIER, so run digests are checked against the shipped JSON as tokens in their own class rather than skipped by a numeral regex that never matched them`.
- **Engine fence.** `src/ave` byte-untouched; `ave.core.constants` imported read-only.
- **Predecessor fence.** All nine predecessor files blob-pinned in prereg §P.4 are **byte-untouched**. v2.4's driver is **imported read-only** by `G-C(a)` as a comparison object and is not edited.
- **Scope, unchanged:** `ℓ = 2` is an input; `ν_vac`, `K = 2G` and the `7` in `r_sat` are GR-imported and untouched; spin is out of scope; the Cosserat microrotational channel is not built; **no completeness or overtone statement of any kind is made for either family.**

---

> **Result provenance.** Resolves the BUILD phase of `research/2026-08-03_coldq-polar-family_prereg-FROZEN.md` (commit `d9015e38`, COMMIT 1 of this lane, pushed ALONE before any driver code existed and before any number produced by this instrument existed). All numbers above are read from the shipped `research/drivers/coldq_polar_family_results.json` and are machine-verified against it by `research/drivers/coldq_polar_family_number_check.py`, wired into `make verify`. Two full driver runs produced identical digests. Mints no `clm-`/`def-`; propagates to no leaf; engine byte-untouched; falsification ledger untouched. Companion: the docket fragment `_orchestration/docket-entries/2026-08-03-coldq-polar-family.md`.
