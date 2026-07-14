# ROUTE A — THE COMPOSITE FADDEEV-SKYRME NEUTRON BUILD — RESULT

**Date:** 2026-07-14 · **Branch:** `derivation/route-a-composite-fs` · **PR:** `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`.
**Frozen prereg (gated on):** `research/2026-07-14_route-a-composite-fs_prereg_FROZEN.md` (freeze commit
`1fc0f61f`, committed `2026-07-14T14:23:48Z`, pushed BEFORE any solver code — git ordering = freeze proof).
**New capability:** `faddeev_skyrme.py` `TopologicalHamiltonian1D.solve_composite_trace(d)` (the threaded-`0₁`
term added to the FS energy integral). **Driver:** `src/scripts/vol_2_subatomic/route_a_composite_fs.py` ·
**Tests:** `src/tests/test_route_a_composite_fs.py` (32 passed) + no regression (`test_constants_literals`,
`test_np_mass_split_gate` still green, 80 total).

**One-line result:** **bin (iii) RIGHT-SIGN-WRONG-MAGNITUDE** (both mass-accounting readings) — the composite
FS instrument, built value-blind per the TBD-pin, **COMPUTES a positive split** (`Δm > 0`, neutron heavier,
matching observation), but the magnitude **over-predicts the 2× band by ~15×** (`+38.12 m_e` Reading Y /
`+39.12 m_e` Reading X at the Ax1-floor `d=1.0`, warm κ_FS; target `+2.531 m_e`). **★ The δ_th ablation
does NOT resolve C5 in this instrument:** the 1D shift proxy has no δ_th channel into the threading surplus
except the confinement bound, so the split's δ_th-loading is `+0.042 m_e` (~0.11% of the split), **linear in
δ_th** — a `r_opt=κ/5` bound-drift residual, NOT a substrate adjudication. **C5 stays OPEN** pending an
instrument that retains the quartic linking channel (the genuinely 3D composite build). The `+0.042 m_e` is
banked as the proxy's δ_th-sensitivity characterization. [See the "Review findings + repairs (2026-07-14)"
section for the channel-excision proof.]

---

## INTERPRETATION-DISCIPLINE (read BEFORE the verdict — items 1-2 frozen in the prereg; items 3-4 CORRECTED per the 2026-07-14 review, see the repairs section at the end)

1. **The SIGN and the δ_th-LOADING are the load-bearing observables; the absolute magnitude is the LEAST
   robust.** The 1D radial FS functional is a coarse spherically-symmetric proxy for the composite's true
   3D linking geometry (the `0₁` threading the cage's void is a 3D topological relation the 1D hedgehog
   cannot fully represent). A magnitude miss (bin iii) is a statement about the **instrument's coarseness**,
   NOT a physics falsification of the composite neutron ontology.

2. **A bin-(iii) does NOT falsify the +0.74% bare-topology emergence result.** That result (cold `κ_FS=8π`
   → `1849.70 (+0.7377%)`) stands independently of both δ_th and the neutron construction. Route A touches
   only the split. Nothing about the bare-topology result is affected.

3. **★ The δ_th ABLATION is CHANNEL-BLIND — it does NOT resolve C5 (RETRACTED per the 2026-07-14 review).**
   The split's δ_th-loading `Δm(warm) − Δm(cold) = +0.042 m_e` (both readings, ~0.11% of the split) is real
   and reproduced — but its near-vanishing is a **structural identity of the 1D shift rendering, not a
   substrate verdict.** δ_th enters the composite functional ONLY through `κ_FS` (`κ_FS = 8π(1−δ_th)`,
   `constants.py:927`), and `self.kappa` appears at exactly two solver sites: the κ²-weighted Skyrme
   (quartic) term (`faddeev_skyrme.py:264`) and the `r_opt_max = κ/5` confinement bound (`:292`). Under the
   spherical `4πr²` measure the Skyrme term's `1/r²` cancels **exactly**, leaving a function of `φ` and
   `dφ/dr` with no explicit `r` — so it is **shift-invariant** under the rigid shift `φ(r)→φ_bare(r−d)` and
   cancels **identically** in `E_comp − E_bare` (live-fire decomposition at the shipped minimizer: kinetic
   d-surplus `+24.1387` (κ-FREE), Skyrme d-surplus `−7e-7`, κ-coupled fraction `−2.8e-8`; bare and composite
   minimizations corner-pinned at the SAME argmin `[4.99017, 1.0]`). δ_th's ONLY surviving path into the
   split is the `r_opt_max = κ/5` **bound drift** (perturbation probe: `δ_th×3 → loading ×3.04`,
   `δ_th×10 → ×10.6` — linear-and-tiny through the bound). So **the 1D shift proxy has no δ_th channel into
   the threading surplus except the confinement bound; loading through that residual is `+0.042 m_e`, linear
   in δ_th — a bound-drift floor, NOT the FS-route (`:77`) loading the δ_th-carrying side of C5 needs.**
   **C5 stays OPEN** pending an instrument that retains the quartic linking channel (the genuinely 3D
   composite build); the `+0.042 m_e` is banked as the proxy's δ_th-sensitivity characterization, NOT as a
   fork resolution. Consequence: the split is a **poor δ_th discriminator by construction** (the loading
   channel is excised), so the bin-(iii) magnitude miss is a **structural/instrument fact, not a δ_th fact.**
   The audit-card provenance findings (R3/R7/R10/R12 on the *level* δ_th) stand exactly where the audit left
   them — the split neither strengthens nor weakens them.

4. **The sign is CANON-FORCED POSITIVE by the C1 rendering selection — a canon-transcription check, NOT a
   stronger confirmation (CORRECTED per the 2026-07-14 review).** The C1 walk selected the shift-outward
   rendering *because* it is the only one of the three candidates that gives the `:25` positive surplus (the
   other two were ruled out for the wrong sign), so `E_comp − E_bare > 0` for all `d > 0` is guaranteed by
   the `4πr²` measure — the frozen bin (ii) WRONG-SIGN was structurally **unfireable** on any admissible
   physical output from C1 onward. Route A's positive split is therefore **consistent-by-construction with**
   (NOT independent of, and NOT a stronger mechanism-level confirmation of) the n–p gate's genuinely δ_th-free
   sign bound (rest mass ≥ 0 + Ax1 strain ≥ 0 + the β-decay-downhill floor `Δm > 1.000 m_e`). The direction
   (outward) and sign (surplus) are corpus-stated at `:25`; the only genuinely computed content is the
   MAGNITUDE (which missed by ~15×).

---

## THE VERDICT

### Magnitude: **bin (iii) RIGHT-SIGN-WRONG-MAGNITUDE** (both readings)

Primary split at the frozen `d = 1.0 ℓ_node` (Ax1 transverse-thickness floor), mapped through the canonical
`/(1−V·p_c)` regenerative feedback:

| κ config | elastic (with feedback) | Reading X (`+1.000 m_e`) | Reading Y (elastic only) | raw ΔI (no-feedback alt) | sign |
|---|---|---|---|---|---|
| **warm** `κ_FS=8π(1−δ_th)` | `+38.1221 m_e` | **`+39.1221 m_e`** | **`+38.1221 m_e`** | `+24.1387` | **+** |
| **cold** `κ_FS=8π` | `+38.0799 m_e` | `+39.0799 m_e` | `+38.0799 m_e` | `+24.1120` | + |

- **Target:** `Δm_CODATA = +2.5310 m_e = 1.293332 MeV`; `2×` band `[1.265, 5.062] m_e`.
- **Warm split (Reading Y):** `+38.12 m_e = 19.48 MeV` → **`15.1×` above the target**, far outside the 2× band.
- **d=0 consistency (built-in check):** `solve_composite_trace(0) == solve_scalar_trace()` exactly, warm and
  cold — the composite capability reduces to the bare proton at zero displacement (the new capability adds
  nothing spurious to the bare path; `test_constants_literals` unchanged).

### Sign: **CANON-FORCED POSITIVE (Δm > 0, neutron heavier) — positive by construction, NOT an independent computation.**

The shift-outward rendering computes `E_comp(d) > E_bare` for all `d > 0` — the spherical `4πr²` measure
weights the displaced winding shell more, so the elastic-expansion surplus is positive by construction of
the canon-forced rendering. **This matches observation** (the neutron IS heavier) and is
**consistent-by-construction with** (NOT a stronger confirmation of) the n–p gate's δ_th-free sign
sub-finding. Bin (ii) WRONG-SIGN was unfireable on admissible `d ≥ 0.5` (all give `Δm > 0` by the
canon-forced C1 sign); it is exercised only via a synthetic plant (`classify_bin(-1.0)`).

### δ_th-loading (C5 stays OPEN — the ablation is channel-blind): **`+0.042 m_e` (≈ 0.022 MeV, ≈ 0.11% of the split)** — a bound-drift residual, not a fork resolution.

| observable | Reading X | Reading Y | no-feedback |
|---|---|---|---|
| `Δm(warm) − Δm(cold)` | `+0.04218 m_e` | `+0.04218 m_e` | `+0.02671` (raw ΔI) |

(The `+1.000 m_e` threaded-electron rest mass is κ-independent, so it cancels in the difference — X and Y
loadings are identical.) **This is the resurrected δ_th second shot, fired — but into a CHANNEL-BLIND
instrument:** the κ²-weighted Skyrme term (the ONLY δ_th-carrying channel, since δ_th enters only via κ) is
shift-invariant under the rendering and cancels **identically** in `E_comp − E_bare`, so the `+0.042 m_e` is
the residual `r_opt = κ/5` bound drift, not a genuine FS-route loading. It is a mischaracterization to say
the difference "de-sensitizes δ_th" by physical near-cancellation — the δ_th-carrying term is *structurally
absent* from the surplus by an exact measure-cancellation identity of the 1D shift ansatz. **C5 is NOT
adjudicated by this proxy — it stays OPEN.**

---

## THE C1–C5 CHOICE LEDGER (as executed — the n–p gate's five missing choices, MADE + justified)

| # | Choice | As executed | Justification / tag |
|---|---|---|---|
| **C1** | FS field ansatz for the composite | Profile-shift-outward: cage `φ=π` on `[0,d]`, `φ=π/(1+((r−d)/r_opt)ⁿ)` on `(d,∞)`; same functional, `c=5` confinement unchanged. `solve_composite_trace(d)`. | **CANON-FORCED** — the only rendering (of inner-exclusion / r_opt-stretch / shift-outward) that gives the `:25` positive surplus; the other two give the wrong sign (ruled out BY the corpus). Held-core `φ=π` on `[0,d]` = disclosed ENGINEERING-CHOICE. |
| **C2** | threading-lock coupling term | Folded into the boundary displacement — NO separate constant. | ENGINEERING-CHOICE (minimal, non-mint); `:25` names a single "elastic-expansion tension" mechanism. |
| **C3** | cage stiffness + displacement `d` | Stiffness = the FS functional's own tension (no new constant); `d = 1.0 ℓ_node` (Ax1 floor). | `d=1.0` from **Ax1** (`:25`); `:54` FLAGS the ℓ_node-expansion premise "not established" → disclosed `d`-sweep `{0.5,1,1.5,2}`, `d=1.0` frozen primary (NOT tuned). |
| **C4** | mass-accounting X vs Y | Reported BOTH; both land bin (iii). | Disclosed FORK (`proton-neutron-mass-split.md:10`); not a tuning choice. |
| **C5** | δ_th softening of composite | **C5-OPEN — NOT adjudicable in this instrument.** Loading `+0.042 m_e` is the `r_opt=κ/5` bound-drift residual; the δ_th-carrying κ²-Skyrme channel is shift-invariant and cancels identically in `E_comp − E_bare`. | The ablation is CHANNEL-BLIND (the `:77` FS-route loading is structurally excised by the 1D shift measure); C5 stays OPEN pending a 3D composite build that retains the quartic linking channel. |

### `d`-sweep (disclosed robustness ONLY — never a selection mechanism)

| `d` (ℓ_node) | `Δm` warm, Reading Y (m_e) | Reading X (m_e) |
|---|---|---|
| 0.5 | `+17.455` | `+18.455` |
| **1.0 (primary, Ax1 floor)** | **`+38.122`** | **`+39.122`** |
| 1.5 | `+62.001` | `+63.001` |
| 2.0 | `+89.093` | `+90.093` |

Monotone-increasing in `d` (bigger displacement → bigger surplus). **Every `d ≥ 0.5` over-predicts the 2×
band by ≥ 3.5×**; landing IN band would require sub-floor `d ≈ 0.04–0.15 ℓ_node`. The Ax1 transverse-thickness
floor is a **real-space** length, whereas `d` here (like `r_opt`) lives in the solver's **dimensionless**
ℓ_node Nyquist-cutoff coordinate; per `neutron-identification.md:54` the mapping of the real-space floor onto
that dimensionless coordinate is 🔴 **"not established"** (`D_p ≈ 0.841 fm ≈ 460× smaller than ℓ_node = 386
fm`), so **whether a canon-admissible `d` reaches bin (i) is NOT canon-determined** — at the frozen candidate
`d=1.0` (solver units) the proxy over-predicts ~15×, but bin (i) is not foreclosed. The miss is robust to `d`
**only over the range the flagged Ax1-floor mapping admits**, NOT a selection of `d` (mirrors the C3 ledger's
own `:54`-flag disclosure above).

---

## NO-REFIT / NO-MINT / NO-SEED / NO-BYPASS AUDIT (self-review; the adversarial-review lens re-runs this)

| Rail | Check | Result |
|---|---|---|
| No refit (2) | live `ave.core.constants` consumed set == frozen HEAD JSON sidecar; `PROTON_ELECTRON_RATIO` reproduced from `I_scalar/(1−V·p_c)+1` | PASS (rtol 1e-12) |
| No refit (2) | `run_route_a()` aborts on a source-level `DELTA_THERMAL` refit (`test_run_route_a_aborts_on_refit`) | FIRES |
| New capability | `solve_composite_trace(0) == solve_scalar_trace()` exactly (bare path untouched; `test_constants_literals` green) | PASS |
| Positive surplus | `E_comp > E_bare` (the canon-required sign) | PASS |
| No mint (1) | fabricated `E_elastic` from provenance `invented` rejected on the emit path (`_guarded_split_component`) | FIRES |
| No seed (4) | a component whose VALUE = the answer (1.293 / 2.531 / 939.565 / proton ratio) rejected even with canonical provenance | FIRES (5/5) |
| Ablation-bypass (5) | a single-κ "ablation" (warm==cold), a mislabeled pair, or a mismatched-`d` pair is rejected | FIRES (3/3) |
| d-refit (4) | tuning the primary `d` away from the Ax1-floor `1.0` trips the primary-d guard | FIRES |
| Bin fireable | in-band → (i); wrong-sign → (ii); out-of-band → (iii); non-computable → (iv) (`test_bin_flip_plants`) | FIRES on **synthetic plants only**. ⚠ bin (ii) WRONG-SIGN is UNFIREABLE on admissible physical output (every `d ≥ 0.5` gives `Δm > 0` by the canon-forced C1 sign); the classifier exercises it via `classify_bin(-1.0)`, a hand-planted negative — so this row is classifier mechanics, not instrument-fireability of bin (ii). |
| EFT hygiene | `verify_universe.py`: driver + solver + test PASS, "MATHEMATICALLY PURE" (1250 files) | PASS |

Zero hard-coded physics numbers in the driver; the forbidden-seed set is derived from module CODATA anchors
(auto-tracks). All 32 Route A tests pass; 80 total green (incl. constants-literals + np-gate coordination).

---

## FLAG-DON'T-FIX — surfaced for Grant, NOT resolved here

1. **The `/(1−V·p_c)` feedback question (framing fork).** Whether the elastic surplus rides the full
   regenerative mass-feedback loop (primary, `×1.58`: `Δm ≈ 38 m_e`) or is a linear-response perturbation
   outside it (raw ΔI: `≈ 24 m_e`) is a genuine fork. It is **NOT load-bearing for the bin** (both
   over-predict the 2× band by ≫ 3×), so it did not block the build; both are reported. Surfaced for
   Grant/auditor adjudication of which reading the composite cage's self-consistency actually takes.

2. **The 1D-radial-proxy limitation (build honesty).** The composite `6₂³ ∪ 0₁` is two LINKED tubes — a
   3D topological relation. The 1D radial hedgehog solver represents a single spherically-symmetric defect;
   the shift-outward `d` is a **proxy** for the true 3D linking energy. The corpus TBD-pin (`:54`/`:77`)
   itself commits to a 1D-solver-shaped computation ("same shape as proton … in units of m_e c²"), so this
   is the corpus's own scope — but the ~15× magnitude overshoot is consistent with the proxy being
   geometrically coarse (the spherical measure over-weights the displaced shell vs a true axial threading).
   A faithful magnitude would need a genuinely 3D composite FS solve (a separate, larger build). This is
   surfaced as the honest ceiling on the magnitude claim, NOT a debug-toward-rescue.

3. **Mass-accounting ambiguity (Reading X vs Y).** Inherited from the n–p gate; `proton-neutron-mass-split.md:10`
   attributes the whole surplus to elastic tension with no separate electron-rest-mass accounting. The
   verdict (bin iii, sign +, δ_th-robust) is robust to both readings; flagged for Grant, not decided.

---

## COORDINATION — the n–p gate's corpus-state detector

The n–p gate wired `corpus_has_derived_neutron_mass` + `test_detector_fires_if_derived_neutron_mass_appears`
to **announce exactly this event** (`2026-07-13_np-mass-split-gate_RESULT.md:100`, Route A charter). **As
built, Route A is a standalone driver (DO-NOT-MERGE, value-blind); it does NOT canonize a
`NEUTRON_ELECTRON_RATIO`/`M_N_MEV_AVE` into `ave.core.constants`** (canonization is a corpus-state change
requiring Grant adjudication of this result). So the **live detector remains clean by design** — the n–p
gate's `magnitude_computability_leg` does not raise, and its 41 tests stay green. The n–p gate test file
carries a **dated note (2026-07-14)** recording that Route A now exists as the derivation the detector was
designed to announce, and that canonization (which would flip the detector) awaits Grant's ruling.

---

## BOTTOM LINE

The corpus's own TBD-pin, built value-blind, **fires the discriminator the audit card wanted** — and what
stands is a bin (iii) RIGHT-SIGN(-by-construction)-WRONG-MAGNITUDE deliverable across the three frozen
observables (NOT a clean three-observable substrate verdict): (1) **SIGN** — canon-forced positive by the
C1 rendering selection, matching observation, **consistent-by-construction with** (not a stronger
confirmation of) the n–p gate's δ_th-free sign; (2) **MAGNITUDE** — bin (iii),
`+38 m_e` (≈ 15× the target) at the frozen `d=1.0`, the 1D-radial proxy over-predicts the elastic tension
(an instrument-coarseness fact, robust to the feedback fork; robust to `d` only over the range the
`:54`-flagged Ax1-floor mapping admits — sub-floor `d` is NOT canon-excluded, so bin (i) is not foreclosed);
(3) **δ_th-LOADING** — `+0.042 m_e` (~0.11% of the split) is a `r_opt=κ/5` bound-drift residual, NOT a fork
resolution: the δ_th-carrying κ²-Skyrme channel is shift-invariant and cancels identically in the
difference, so **C5 stays OPEN** (the ablation is CHANNEL-BLIND). The loading being tiny is preordained by
the ansatz, so the magnitude miss is NOT a δ_th verdict; the level-δ_th provenance findings (R3/R7/R10/R12)
stand untouched. The +0.74% bare-topology result stands untouched. Route A converts the n–p gate's bin-(iv)
"FORK-OPEN, unbuilt" into a built result with an honestly-railed bin-(iii) magnitude deliverable:
**sign canon-forced-positive (by construction), δ_th-loading measured (but channel-blind → C5 stays OPEN),
magnitude honestly missed by the coarse 1D proxy.**
