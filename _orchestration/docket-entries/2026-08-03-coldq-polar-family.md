### ENTRY 2026-08-03-coldq-polar-family

**cold-Q POLAR FAMILY — the coupled shear–bulk solve; the isospectrality discriminator**

**Status:** `SOLVER-NOT-CERTIFIED` (BUILD PHASE). **No physics bin adjudicated.**
**Branch:** `research/coldq-polar-family` · **Freeze:** `d9015e38` (prereg pushed ALONE, before any code)
**Prereg:** `research/2026-08-03_coldq-polar-family_prereg-FROZEN.md`
**Result:** `research/2026-08-03_coldq-polar-family_result.md`
**Driver:** `research/drivers/coldq_polar_family.py` → `research/drivers/coldq_polar_family_results.json` (digest `ac81dc1ac7142d11`, two runs identical)
**Fired on:** Grant's ruling 2026-08-03, verbatim [sic] *"2. Proceed"*, plus the FLAG-3/FLAG-4 routing the merged v2.4 result doc carries at `:320`–`:321`.

### What was asked, and what came back

Build the polar (coupled shear+bulk) mode family for the canonical graded profile and measure the **SPLIT** against the certified axial pole — the observable on which AVE would predict a split `ℓ = 2` ringdown spectrum where GR's own isospectrality theorem predicts one line.

**The split was not measured.** The instrument implements only the build-phase gate subset; ten gates and eleven self-tests are UNRUN, and an unrun gate is not a passed gate. Under the frozen precedence that is `BIN-PF-SOLVER` and **no bin is adjudicated**. Separately, the seed search returned **zero** `n`-stable physical-quadrant candidates on **all three** configurations, so `BIN-PF-NOROOT` also fired for each.

### What WAS earned

| gate | measured | tol | verdict |
|---|---|---|---|
| G0(a) homogeneous-limit **Bessel identity** on the DERIVED coupled system | `3.3409558876152446e-52` | `1e-12` | PASS |
| G0(b) `Ω`-degree probe (operator exactly quadratic) | `≤ 3.998694576407435e-80` | `1e-12` | PASS |
| G0(c) symbolic re-derivation at `ℓ ∈ {2,3,4}` | separability + affine-in-`L` **exactly 0** | exact | PASS |
| **G-C(a) OPERATOR IDENTITY vs v2.4's certified axial operator** | `4.0091470651382935e-51` | `1e-40` | PASS |
| **G-C(b) certified axial ROOT reproduced** | `2.1392113069210418e-40` | `1e-10` | PASS |

Self-tests FT-0(a) (`2.7824766158925944e-10`), FT-0(c) and FT-C (`0.29103890693977286`) all FIRE.

### ★ THE FINDING — FLAG-W, routed to Grant

**Canon gives two opposite bulk-modulus signs at the same `r_sat` wall.**

- **VENTS:** `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md:31` — *"$c_{bulk} \to 0$ (bulk dilatational speed vanishes at snap / rupture)"* ⇒ `Z_bulk → 0`, `Γ_bulk = −1`.
- **JAMS:** `manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md:57` — *"**BULK stiffens:** $D=1/S\to\infty$ at $A\to1$ (the modulus goes rigid, halting the collapse)."* ⇒ `Z_bulk → ∞`, `Γ_bulk = +1`.
- **FIREWALL:** `manuscript/ave-kb/common/engine-capability-map.md:69` — *"Conflating them is the firewall violation."*

The two branches are **identical in the far field** and differ **only at the wall**, which is exactly why four prior axial lanes could not have surfaced this: the axial mode never touches the bulk line. **Neither leaf repaired; both branches built and run; nothing adjudicated.**

**Grant's plumber question, owed:** *at the saturation radius, does the vacuum's compression line vent, or does it dead-end?*

### Three more derivation-phase outcomes

- **FLAG-B — the brief's `√2 c` bulk speed is CORRECTED by derivation.** The port register itself calls `√2 c` the PORT/impedance mode and gives `√(10/3) c` as the far-field longitudinal wave; the elastic identity `λ_L + 2μ = K + 4μ/3 = (10/3)μ` at `K = 2G` reproduces it (`1.8257418583505538`). `√2 c` enters only the wall reflection statement.
- **FLAG-4(a) DISCHARGED by two-method citation** — canon carries ONE lattice density `ρ_bulk` for BOTH channels (`three-channel-impedances.md`; `constants.py:766`). The #814 CF-7 gap is a gap in one leaf, not in canon. **FLAG-4(b) (the grading) remains open**; FORK-3(b) `ρ_eff = ρ_bulk/S³` was RUN for the first time (`CFG-SOFT-B`) and returned no root.
- **FLAG-3 DISCHARGED FOR THE PROFILE** — the modulus deviation is `O(1/r²)` with no `1/r` term, so the port is reflectionless **by derivation**, per channel, on both branches. It does not cover a reflector from physics outside this profile.

### ★ The structural obstruction, and the successor requirement

The two channels radiate at `c_S` and `c_P = √(10/3)·c_S`, so a **single** shear-channel outgoing factor leaves the radial equation an unbalanced `(k_P² − k_S²)` term: `A = 0` is an **irregular singular point** of that equation. The medium's answer is a **beyond-all-orders** suppression of the bulk-outgoing amplitude — pre-registered in prereg §2.6 — and a polynomial basis in this coordinate cannot resolve it. **One mechanism explains all three nulls.**

**Routed successor requirement:** an instrument that handles two speeds — **exterior complex scaling**, or a matched two-domain scheme with per-channel outgoing conditions at a finite radius. Note that ECS is also the *"genuinely independent third instrument"* v2.4's own FLAG-10 says is not built: **one build discharges both.**

### Three bugs the gates caught before any physics number existed

1. `sp.diff(S, η)` with `S = η·u` returned `u` instead of `2A/u`, corrupting **every** modulus gradient — i.e. exactly the coupling this lane measures. Caught by G-C against the certified axial operator.
2. A hand-expanded second-derivative-of-a-product formula disagreed with the certified operator by `2η²(iΩ − 2A)/u²`. Hand expansion removed; the chain rule is now symbolic.
3. Float contamination made G0(c)'s exact-zero residuals read `False`.

**Two of the three would have produced a plausible-looking wrong polar frequency.** This is the Rule-10 argument in its strongest form.

### Frozen-text defect, disclosed PRE-measurement

The frozen FT-C row names the spin-1 **stored-energy weighting**, which does not enter the operator and could not have moved it — **the mutation as frozen would have been vacuous.** The implemented mutation is v2.4's spin-1 **WALL row**, which does. Recorded in the driver before the battery ran; the successor should freeze the wall-row form.

### Validation

`make verify` ALL PHYSICS PROTOCOLS PASSED · number check 31 sites / 21 distinct / 20 registered / 11 allow-listed / **0 unregistered**, all 14 registered keys exercised, mutation receipt fires on a single-digit drift · two runs digest-identical · ruff clean · fifth cold-Q Makefile target added as its own recipe · engine `src/ave` byte-untouched · all nine predecessor frozen files byte-untouched and blob-pinned · mints no `clm-`/`def-`; propagates to no leaf.

### Open / routed

1. **FLAG-W → Grant** (the compression-line ruling). Highest value.
2. **Successor instrument** (ECS or two-domain) → discharges FLAG-10 too.
3. FLAG-4(b) grading fork — still open, still unrun in the sense that no root was obtained.
4. FLAG-COS — Cosserat microrotational channel not built.
5. FLAG-5 — substrate-derived low-frequency cutoff, unchanged.
