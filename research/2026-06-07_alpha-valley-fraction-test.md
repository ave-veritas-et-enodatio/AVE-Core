# α as the valley/shadow fraction of the K4 multi-neighbor rotor envelope — real-space vs phase-space

**Date:** 2026-06-07 · **Branch:** `analysis/2026-06-07-alpha-valley-fraction` (off `main`)
**Lane:** implementer · **Session type:** implementor (single deliverable)
**Status:** §0–§5 are the **FROZEN PREREG** (frozen before any driver run). §6+ are post-run results.
**Base:** Grant's electron-synthesis mechanism for the dark-wake α-localization (PR #119,
`research/2026-06-07_darkwake-feedback-alpha-test.md`) — which localized α's origin OFF the
parametric loss/gain ratio (that carries only the `4π`) and ONTO the multipole / Golden-Torus geometry.

---

## §0 Frame (Grant, electron-synthesis epic)

PR #119 (the α-free dark-wake loss) showed the parametric loss carries **only the `4π`** of
`137 = 4π³ + π² + π`; α is **NOT** in the parametric loss/gain ratio. The α-free emergence
candidate was localized to the **multipole / Golden-Torus geometry** on the separate
`(V_inc, V_ref)` phase-space axis.

**Grant's mechanism for that geometry.** The electron's time-averaged rotor envelope — the
spinning B-loop around the host K4 node — is **spherical from the host alone**. But
**multi-neighbor coupling at larger radii** (the K4 neighbor shells) **bulges** it into a
multipole: bulges toward each neighbor node, **valleys between**.

**HYPOTHESIS under test.** α = the **inverse shadow** = the **valley/gap fraction**:
one valley per `~137` bulges; `α = 1/137 = 1/(mode count)`; `α⁻¹ = 4π³ + π² + π` is the
mode/bulge count (`Q_vol + Q_surf + Q_line`). This would unify α = the valley = the leak (1/Q)
= the packing gap (`p_c = 8πα`).

**LOAD-BEARING CAVEAT (the test's whole point).** α lives in **PHASE-SPACE** (the Golden Torus
on the Clifford torus in `(V_inc, V_ref)`); the real-space envelope is the **SHADOW/projection**,
and real-space projections do **NOT** preserve phase-space ratios (canonical: `R/r = φ²` in
phase-space, ≠ in real-space — `ch8-alpha-golden-torus.md`). So the real-space valley fraction
**need NOT** equal the phase-space `1/137`. **The test must resolve WHICH FRAME carries α.**

**The deliverable is the honest classification + the localization**, not a hit. Per the task:
pure K4 geometry (α-free) AND `1/137` → first geometric α-emergence; α-encoded → CIRCULAR (the
A47 `p_c=8πα` / theorem-3-1 Path-A failure mode); **α-free but ≠ 1/137 → report the NUMBER + the
FRAME (localization is as valuable as a hit).** Do NOT report a near-miss as a hit.

---

## §1 Substrate-native re-walk (`substrate-native-check`)

**CP1 — what the rotor envelope IS.** The electron is the `0₁` unknot soliton at a host K4 node;
its time-averaged magnetic-rotor (Cosserat-B, microrotational sector, Ax 1) envelope is, from the
host node alone, **spherically symmetric** (a monopole `E₀(r̂) = 1`). This is the real-space,
field-space (NOT `(V_inc,V_ref)` phase-space) object.

**CP2 — the K4 multi-neighbor coupling (the bulge source), ALPHA-FREE.** The diamond/K4 lattice
(`k4_tlm.py:10,107,212,378`): A-sublattice = all-even coords, B = all-odd = A+(1,1,1); each node
has **4 tetrahedral nearest neighbors** along the canonical port vectors `(1,1,1),(1,-1,-1),
(-1,1,-1),(-1,-1,1)` (`k4_tlm.py:378-383`), then 12 second-shell, etc. The neighbor-shell
positions are **pure lattice geometry** — `ℓ_node`-quantized, no α. The rotor's envelope bulges
toward each neighbor with which it couples, valleys between. Two α-free modeling inputs:
- **shell positions + multiplicities** (n̂, R_s) — exact lattice geometry, no knob;
- **coupling falloff w(R_s)** and **angular kernel g(r̂·n̂)** — modeling choices; both α-free, but
  KNOBS → swept (sensitivity, §6.4) so the verdict is robust to them, per the PR #119 template.

**CP3 — AVE-native objective.** NOT energy-basin minimization. The envelope is the time-averaged
saturation-amplitude `A²(r̂)` / rotor density field; the "valley fraction" is the geometric
gap-vs-bulge ratio of that field over the unit sphere (real-space) and over the Clifford torus
(phase-space). The leak/1/Q reading (Ax 3 minimum-reflection): valleys = where the envelope
under-fills = the gap the substrate leaks through.

**CP4 — PHASE-SPACE vs REAL-SPACE (the load-bearing fork; `phase-space-coordinate-check`, §2).**
The literal K4 envelope is **real-space** (a function on the unit sphere `S²` of lattice
directions). The corpus α lives on the **Clifford torus** `T² ⊂ S³ ⊂ ℂ²` in `(V_inc,V_ref)`
phase-space. The projection real-space → phase-space does NOT preserve ratios (`R/r=φ²` only in
phase-space). The driver measures the valley fraction in **both** frames and reports which (if
either) carries `1/137`.

**CP5 — constants discipline (`ave-canonical-source`).** `ALPHA` and `ALPHA_COLD_INV` imported
**for COMPARISON ONLY**; never an input to the envelope or the valley fraction. `PHI`,
`R_GOLDEN_TORUS`, `R_GOLDEN_TORUS_MINOR`, `RR_GOLDEN_TORUS` are the phase-space Golden-Torus
geometry (φ-derived, α-free) — used only in the phase-space frame, flagged in the input-trace.

**CP6 — sampling discipline (Rule 10).** No PML / lattice-extraction here — this is an analytic
envelope over direction-space + a torus, not a time-domain field dump. Shells are exact-geometry;
sphere sampling is a Fibonacci-sphere quadrature (uniform-measure), torus sampling is a uniform
`(u,v)` grid with the phase-space area element.

**Walk verdict.** The envelope is a substrate-native real-space rotor-density field built from
α-free K4 neighbor-shell geometry + an α-free coupling kernel; the valley fraction is a geometric
ratio measured in two coordinate frames. The α-classification (§3) is well-posed: trace every
input to the valley fraction in each frame.

---

## §2 Phase-space coordinate check (`phase-space-coordinate-check`)

- **Corpus claim under test:** `α⁻¹ = 4π³+π²+π` is a `(V_inc,V_ref)` **phase-space** Clifford-torus
  mode-count (`ch8-alpha-golden-torus.md` §"Topological self-impedance shape factors";
  `derive_alpha_from_golden_torus.py:33-53`: `Λ_vol=16π³(R·r)`, `Λ_surf=4π²(R·r)`, `Λ_line=π·d`,
  on `T²⊂S³⊂ℂ²` at `R·r=1/4`, `d=1`). Coordinates: **phase-space**.
- **Grant's envelope under test:** the literal K4 multi-neighbor rotor envelope is **real-space**
  (a field on `S²` of lattice directions). Coordinates: **real-space**.
- **MISMATCH is the hypothesis.** The test does NOT assume they match; it MEASURES the valley
  fraction in each frame separately and reports which carries `1/137`. Comparing a real-space
  valley fraction directly against the phase-space `137` would be exactly the A46 uninformative
  comparison — so the driver also **projects the real envelope onto the Clifford torus** and
  measures the valley fraction in the phase-space measure (the honest shadow→phase-space of
  Grant's envelope), and separately reports the corpus's own Clifford-torus mode-count (which
  uses `R·r=1/4`, NOT Grant's envelope) as the reference `137`.

---

## §3 Consistency-vs-emergence pre-classification (`consistency-vs-emergence`) — THE HEADLINE, pre-registered

**Step 1 — target:** the valley/gap fraction `f_valley` of the K4 multi-neighbor rotor envelope,
in real-space and in phase-space, compared to `α = 1/137.036` (COMPARISON ONLY; α never an input).

**Step 2 — trace EVERY input to `f_valley`** (the make-or-break; pre-registered before the run):

| Input | Value / form | Class | α / `e,ε₀,ℏ,Z₀ⁱ,c` present? |
|---|---|---|---|
| K4 neighbor-shell positions `n̂, R_s` | exact diamond-lattice geometry (`k4_tlm.py:378`) | Axiom-1 geometry | **NO** |
| shell multiplicities (4, 12, …) | exact lattice coordination | Axiom-1 geometry | **NO** |
| coupling falloff `w(R_s)` | `R_s^{-p}`, `p∈{1,2,3}` swept | Modeling choice (α-free knob) | **NO** |
| angular kernel `g(r̂·n̂)` | normalized peaked kernel, sharpness swept | Modeling choice (α-free knob) | **NO** |
| sphere / torus quadrature | Fibonacci-sphere / uniform `(u,v)` | Numerical | **NO** |
| **phase-space frame only:** `R=φ/2, r=(φ-1)/2, R·r=1/4` | Golden-Torus geometry (φ, α-free) | **Class B named identification** (corpus) | **NO** (φ-derived) — but the named `R·r=1/4` is the corpus's *not-independently-selected* input |

**Pre-registered classifications (fixed before the run — the run measures, cannot move them):**

- **EMERGENCE (`f_valley = 1/137` from α-free real-space K4 geometry):** the first geometric
  α-emergence. **Pre-registered as NOT expected**, because (i) `R/r=φ²` holds only in phase-space,
  so a real-space projection has no reason to carry the phase-space `137`; (ii) the corpus `137`
  is dominated by `4π³` (a 3-cycle *phase-volume* mode-count), which a 2-sphere real-space
  envelope does not host; (iii) PR #119 + the biquaternion G2-fail already localized α to the
  phase-space Clifford-torus construction, not a real-space field.
- **NEAR-MISS-LOCALIZATION (`f_valley` α-free but ≠ 1/137):** the K4 real-space valley fraction is
  an `O(0.1–1)` geometric number set by the coordination + kernel (a knob pinned to `O(1)`, not
  `137`). **Pre-registered as EXPECTED for the real-space frame.** Report the NUMBER + the FRAME.
  This LOCALIZES α to the phase-space Clifford-torus mode-count (the corpus route), NOT Grant's
  real-space envelope — confirming the canonical "real-space does not preserve phase-space ratios"
  caveat. A clean localization, reported as plainly as a hit.
- **CIRCULAR (`f_valley = 1/137` only with α or `R·r→4π²α` fed in):** if reaching `137` requires
  the α-encoded unit-bridge (`ch8` flags the kinematic bridge forces `R·r→4π²α`, α-in→α-out) or
  α itself — that is the A47 `p_c=8πα` / theorem-3-1 Path-A consistency identity, **not** an
  emergence. An α-encoded computation must NOT masquerade as deriving α.

**Pre-registered prediction (mine):**
1. **Real-space frame:** `f_valley` is α-FREE and `O(0.1–1)`, NOT `1/137`. NEAR-MISS-LOCALIZATION.
   The effective angular-mode count of the K4 envelope (Grant's "bulge count") is `O(10)`, not
   `~137`, for physical falloff `p∈{2,3}` and a few shells.
2. **Phase-space frame:** projecting Grant's *real* envelope onto the Clifford torus gives an
   `O(1)` valley fraction too — the projection does NOT manufacture `137`. The corpus's own
   Clifford-torus mode-count gives `1/137` **but only via the named `R·r=1/4`** (Class B), a
   DIFFERENT construction from Grant's envelope (it is the phase-space mode-count, not a shadow of
   the real-space K4 field). So **the phase-space carries α via the corpus's `R·r=1/4`
   identification, not via a projection of Grant's real-space envelope.**
3. **WHICH FRAME carries α:** PHASE-SPACE (the Clifford-torus mode-count with `R·r=1/4`), NOT the
   real-space K4 envelope. Confirms PR #119 + biquaternion G2-fail.
4. **Corpus route vs Grant's envelope:** DIFFERENT. Corpus = phase-space Clifford-torus mode-count
   on `T²⊂S³⊂ℂ²`; Grant's envelope = real-space K4 multi-neighbor bulge field on `S²`. Not the
   same construction.

**Falsifier (of the NEAR-MISS call):** if the α-free real-space `f_valley` (or the projected
phase-space `f_valley` of Grant's *own* envelope) lands `1/137 ± a few %` AND is robust to the
falloff/kernel sweep, the NEAR-MISS pre-registration is WRONG and this is EMERGENCE. Conversely
if `f_valley` is `O(1)` and knob-dependent, EMERGENCE is refused and NEAR-MISS-LOCALIZATION holds.

---

## §4 PREREG block (`ave-prereg`) — frozen

```
PREREG (target: build the K4 multi-neighbor time-averaged rotor envelope ALPHA-FREE; extract the
        valley/gap fraction in BOTH real-space and phase-space (Clifford-torus); test whether either
        frame gives 1/137; trace every input for the circularity guard; classify
        emergence / near-miss-localization / circular).

Corpus state: the Golden-Torus α⁻¹=4π³+π²+π is a PHASE-SPACE Clifford-torus mode-count
  (ch8-alpha-golden-torus.md; derive_alpha_from_golden_torus.py), Class B substrate-mechanism
  manifestation (named R·r=1/4 identification, NOT independently selected; the kinematic unit-bridge
  forces R·r→4π²α = α-encoded, ch8 §gating-clause). PR #119 (darkwake) localized α OFF the parametric
  loss (carries only 4π) ONTO this multipole/Golden-Torus geometry. The biquaternion G2-fail
  (2026-06-06) confirmed the grades give the {3D,2D,1D} skeleton but generate NONE of the π-powers —
  those are Golden-Torus angular geometry, not algebra. NOT YET DONE: whether Grant's REAL-SPACE
  multi-neighbor envelope (a NEW route) gives 1/137, or whether α stays in the phase-space frame.
  This driver does that.

Prior work cited (verify-before-cite):
  - manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md (phase-space Clifford-torus mode-count; R·r=1/4 Class B)
  - src/scripts/vol_1_foundations/derive_alpha_from_golden_torus.py:33-53 (Λ_vol/surf/line formulae)
  - research/2026-06-07_darkwake-feedback-alpha-test.md §6.1,§7 (α localized to the multipole, not the loss)
  - research/2026-06-06_biquaternion-node-algebra-result.md §6 (G2 fail: grades give skeleton, not π-powers)
  - src/ave/core/k4_tlm.py:212,378-383 (A/B sublattice; 4 tetrahedral port vectors)
  - src/ave/core/constants.py (ALPHA, ALPHA_COLD_INV, PHI, RR_GOLDEN_TORUS; COMPARISON ONLY)

Dimensional analysis (Step 3.5):
  - α⁻¹ = 137.036 = 4π³(124.025) + π²(9.870) + π(3.142). DOMINATED by the 3-cycle phase-VOLUME 4π³.
  - A real-space envelope on S² hosts a SURFACE (2D) mode count, not a 3-cycle phase volume.
  - To have ~137 angular modes a real envelope needs SH bandwidth l_max~11 (Σ(2l+1)₀¹¹=144);
    K4 nearest-neighbor (tetrahedral) is l=3 → Σ(2l+1)₀³=16. Few shells ≠ 137 modes.
  - Real-space valley contrast for 4 tetrahedral bulges: O(0.1-1), NOT 0.0073=1/137.

Discriminating outcomes:
  - NEAR-MISS (expected): real-space f_valley α-free, O(0.1-1), knob-pinned to O(1) not 137 →
    localizes α to the phase-space Clifford-torus mode-count (R·r=1/4), NOT Grant's real-space envelope.
  - EMERGENCE (the prize): α-free real-space (or projected) f_valley = 1/137.0 to <few %, robust to the
    falloff/kernel sweep → FIRST geometric α-emergence. (No geometric reason; pre-registered unlikely.)
  - CIRCULAR: 137 reachable only with α / R·r→4π²α fed in → A47 p_c=8πα consistency identity, not emergence.

My prediction: NEAR-MISS-LOCALIZATION (real-space frame) + α carried by the PHASE-SPACE Clifford-torus
  mode-count (corpus route, via the named R·r=1/4), which is a DIFFERENT construction from Grant's
  real-space envelope. Confirms PR #119 + biquaternion G2-fail. Not the first geometric α-emergence.

Falsifier: α-free f_valley = 1/137 ± few %, robust to sweep ⟹ NEAR-MISS pre-reg WRONG, EMERGENCE.
```

**`pre-test-physics-check`:** the one plumber-physical question the walk surfaces for Grant —
*is the rotor-envelope bulge the NEAR-field mutual-coupling (B-loop overlap, `1/R³` dipole falloff)
or the FAR-field radiated shear (`1/R²`)?* PR #119's `dark-back-reaction-taxonomy` split says the
NEAR-field reactive piece is the mass and the FAR-field radiation is the loss; the time-averaged
*rotor envelope* (a static-average B-density bulge) is the **near-field reactive** species → `1/R³`
is the physically-canonical falloff, with `1/R²` and `1/R` swept as the robustness band. Surfaced as
the §6.4 sweep, not blocked (the classification is made robust to it).

---

## §5 Driver design (`alpha_valley_fraction.py`)

*(frozen design; results in §6+)*

1. **`k4_neighbor_shells(n_shells)`** — enumerate the diamond/K4 lattice around a host A-site;
   group lattice points by distance into shells; return `(R_s, multiplicity_s, unit_dirs_s)`.
   Pure geometry, emits the shell table (the α-free input).
2. **`rotor_envelope(dirs, shells, p, kernel_sharpness, polarity)`** — `E(r̂) = 1 + Σ_s w(R_s)
   Σ_{n̂∈s} g(r̂·n̂)`, `w=R_s^{-p}`, `g` a normalized peaked angular kernel; bulges toward neighbors.
3. **`valley_fraction_realspace(E)`** — Fibonacci-sphere quadrature; report contrast
   `(max-min)/max`, min/max, below-mean solid-angle fraction.
4. **`effective_mode_count(E)`** — SH power-spectrum effective angular-mode count (Grant's "bulge
   count"); compare to `137`.
5. **`valley_fraction_phasespace(E)`** — project the SAME real envelope onto the Golden/Clifford
   torus `T²⊂S³⊂ℂ²` (Hopf map; `R·r` area element, `R/r=φ²`); valley fraction in the phase-space
   measure (the honest shadow→phase-space of Grant's envelope).
6. **Corpus reference** — `1/(4π³+π²+π)` and the mode-count `137.036` via `derive_alpha_from_
   golden_torus.golden_torus_multipole()` (uses `R·r=1/4`; NOT Grant's envelope) — the reference.
7. **★ α-classification** — `f_valley` (both frames, both Grant's-envelope and corpus-reference) vs
   `α`; full input-trace; emergence / near-miss-localization / circular.
8. **Sensitivity** — sweep `p∈{1,2,3}`, kernel sharpness, n_shells; show `f_valley` stays geometry-
   pinned `O(1)` and never `1/137` without α.

**Outputs:** `alpha_valley_fraction_results.json` + `alpha_valley_fraction_map.png`.
**Discipline:** `ave-canonical-source` (ALPHA/ALPHA_COLD_INV/PHI imported; COMPARISON ONLY) ·
`consistency-vs-emergence` (§3 trace fixed pre-run) · `substrate-native-check` (§1) ·
`phase-space-coordinate-check` (§2) · KEEP-BOTH (new driver, no engine mutation).
