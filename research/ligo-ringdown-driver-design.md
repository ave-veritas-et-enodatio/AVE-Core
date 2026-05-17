# LIGO Ringdown Driver — Design + Phase-1 Verification

**Branch:** `analysis/ligo-ringdown-driver` (off `research/l3-electron-soliton` at `317faf3`)
**Goal:** Build the executable observer for matrix row **C1-BH-RING** in [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md), currently flagged as "MISSING — no LIGO driver in any repo." Tests AVE's $\omega_R M_g = 18/49 \approx 0.3673$ vs GR's $0.3737$ via re-analysis of public LIGO O1-O2 strain data.

---

## §1 Target — three canonical LIGO events

Per [`manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md) lines 44-48, the AVE prediction has been computed for three LIGO O1-O2 events and compared against LIGO-collaboration published ringdown values:

| Event | $M_{final}$ | $a_*$ (spin) | $f_{AVE}$ (predicted) | $f_{obs}$ (LIGO) | $\Delta f$ | $\tau_{AVE}$ | $\tau_{obs}$ |
|---|---|---|---|---|---|---|---|
| GW150914 | 62.0 $M_\odot$ | 0.67 | 278 Hz | 251 Hz | 10.6% | 3.5 ms | 4.0 ms |
| GW170104 | 48.7 $M_\odot$ | 0.64 | 345 Hz | 312 Hz | 10.5% | 2.7 ms | 3.0 ms |
| GW151226 | 20.8 $M_\odot$ | 0.74 | 884 Hz | 750 Hz | 17.8% | 1.2 ms | 1.4 ms |

**AVE consistently predicts HIGHER ringdown frequencies than LIGO observed by 10.5–17.8%.**

This is the "10–18% from 3 LIGO events" referenced at [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) line 40.

## §2 AVE prediction formula

From [`ave-merger-ringdown-eigenvalue.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md):

**Cold-AVE Schwarzschild eigenvalue** (zero spin):

$$
\omega_R \cdot M_g = \frac{\ell \cdot (1 + \nu_{vac})}{x_{sat}} = \frac{2 \cdot (9/7)}{7} = \frac{18}{49} \approx 0.3673
$$

where $\ell = 2$ (quadrupole mode), $\nu_{vac} = 2/7$ (vacuum Poisson ratio), $x_{sat} = r_{sat}/M_g = 7$ (saturation horizon multiplier per $\varepsilon_{11}(r_{sat}) = 1$).

**Kerr correction** (spinning remnant) — frame-dragging shifts the prograde saturation boundary inward:

$$
f_{ring}(a_*) = f_{ring}(0) \times \frac{r_{ph,\,Schw}}{r_{ph}^+(a_*)}, \quad r_{ph}^+ = \frac{2GM}{c^2}\left(1 + \cos\left[\frac{2}{3}\arccos(-a_*)\right]\right)
$$

with $r_{ph,Schw} = 3GM/c^2$ (Schwarzschild photon sphere).

**For comparison: GR exact** (Schwarzschild $\ell=2, n=0$ QNM) gives $\omega_R M_g = 0.3737$ — AVE is 1.7% below this purely geometric value.

## §3 Phases of driver work

### Phase 1 — Computational verification (this session)

**Scope:** Independently compute the AVE prediction for each of the 3 events from the formula above + Kerr correction. Verify the KB-cited values are internally consistent (no arithmetic drift). Pure numpy/scipy, no LIGO data access required.

**Substrate:** [`src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py`](../src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py) (Phase 1: function `compute_ave_ringdown_prediction(M_msun, a_star)`).

**Acceptance:** computed $f_{AVE}$ values match KB table to within 1% (allowing for rounding in the published table).

**Outcome (2026-05-16):** see Phase-1 run report at bottom of this design doc once driver runs.

### Phase 2 — Raw-strain ringdown fit (next session)

**Scope:** Install PyCBC or GWpy. Fetch public strain data from gw-openscience.org for the 3 events. Identify post-merger window. Fit damped sinusoid to extract observed $f_{obs}, \tau_{obs}$ independently of LIGO collaboration's published values.

**Substrate:** extend the driver with `fit_ringdown_from_strain(event_name)` function.

**Acceptance:**
- Re-fit $f_{obs}$ matches LIGO collaboration's published values (251 / 312 / 750 Hz) to within fit precision (~ few Hz typical)
- Either (a) confirms KB table independently (PASS), or (b) finds discrepancy = surface as load-bearing flag

### Phase 3 — Outcome propagation to C1-BH-RING (next or later session)

**Scope:** Update [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) row C1-BH-RING:
- Move outcome cell from `TBD` → `partial-PASS` (with documented 10-18% offset from LIGO observed) OR `partial-FAIL` (if Phase 2 reveals KB table was computed from different observed values)
- Move substrate cell from `MISSING` → `AVE-Core/src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py`
- Move lifecycle Built/coded from `no` → `code-written + data-collected`

Since this branch is off L3 (not the analysis branch), the C1 row update happens either:
- (a) After this branch merges to L3 and L3 merges back to analysis branch
- (b) Via cherry-pick of the C1-row update commit back to the analysis branch
- (c) After the analysis branch itself merges (then L3 + analysis-branch reunite)

## §4 Branching decision (per Grant 2026-05-16)

This branch is `analysis/ligo-ringdown-driver` off `research/l3-electron-soliton` (NOT off main, NOT off `analysis/divergence-test-substrate-map`).

- **Why not main:** main lacks `ave-merger-ringdown-eigenvalue.md`, `universal-saturation-kernel-catalog.md`, and the C1-BH-RING row context
- **Why not analysis/divergence-test-substrate-map:** that branch was docs-only; LIGO driver is code-bearing; keep separation clean
- **Reintegration path:** when LIGO driver lands a verified outcome, the C1-row update can be cherry-picked back to the analysis branch OR done after both branches merge to L3

## §5 References

- [`manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md) — canonical AVE prediction + 3-event comparison table
- [`manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md) line 78 — names GW150914, GW170104, GW151226 explicitly
- [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) line 40 — "1.7% GR; 10-18% LIGO" canonical claim
- LIGO Open Science Center: https://www.gw-openscience.org (Phase 2 data source)
- LIGO event catalog GWTC-1 (O1-O2 BBH): GW150914, GW151226, GW170104 are all in this catalog

## §6 Phase-1 run report (2026-05-16)

### §6.1 KB self-consistency: PASS

All 3 events match KB-cited AVE prediction to within 0.15%:

```
Event         M (M_sun)    a_*   AVE-cold   AVE-Kerr     KB AVE   AVE-vs-KB
GW150914           62.0   0.67      191.4      277.7      278.0       0.13%
GW170104           48.7   0.64      243.7      344.7      345.0       0.10%
GW151226           20.8   0.74      570.6      883.9      884.0       0.01%
```

KB table is computationally self-consistent. Independent re-derivation from $\omega_R M_g = 18/49$ + the canonical Kerr photon-sphere correction reproduces all three table entries.

### §6.2 AVE-vs-observed: matches KB-cited Δf

```
Event         AVE-Kerr     KB obs   AVE-vs-obs   KB-cited Δf
GW150914         277.7      251.0      +10.62%       10.6%
GW170104         344.7      312.0      +10.47%       10.5%
GW151226         883.9      750.0      +17.86%       17.8%
```

Matches the KB's claimed 10.5-17.8% AVE-above-observed pattern exactly.

### §6.3 SURFACED FINDING — Kerr-correction-formula sensitivity (flag for Phase 2)

When I apply AVE's **simplified Kerr photon-sphere correction formula** ($f_{ring}(a_*) = f_{ring}(0) \times r_{ph,Schw} / r_{ph}^+(a_*)$) to GR's cold eigenvalue ($\omega_R M_g = 0.3737$ instead of $18/49$), I get **GR-Kerr predictions ALSO 12-20% above LIGO observed**:

```
Event         AVE-Kerr     GR-Kerr     KB obs   AVE-above-obs  GR-above-obs
GW150914         277.7       282.5      251.0       +10.62%       +12.55%
GW170104         344.7       350.6      312.0       +10.47%       +12.37%
GW151226         883.9       899.2      750.0       +17.86%       +19.89%
```

**This is interesting and worth Phase 2 investigation.** Standard GR Kerr QNM (via full Leaver-method calculation) generally matches LIGO observed ringdown frequencies within ~5%. My GR-Kerr column being ALSO 12-20% above observed suggests:

(a) **AVE's simplified Kerr formula** (photon-sphere geometry only) **over-corrects for spin** compared to full GR Leaver-method QNM. The "10-18% off LIGO" pattern may largely be an artifact of the AVE Kerr-correction formula, not unique to the AVE cold eigenvalue choice ($18/49$ vs $0.3737$).

(b) The **AVE-vs-GR comparison at zero spin** (1.7%) is the clean apples-to-apples discriminator. **Kerr-corrected comparisons need full Leaver-QNM on the GR side to be fair.**

**Phase 2 action items:**
1. Install PyCBC or lalsimulation to access full Kerr QNM (via Leaver continued-fraction method or fitting formulas from Berti, Cardoso, & Will 2006)
2. Re-compute GR-Kerr column using full Kerr QNM (not AVE simplified)
3. If GR-Kerr-full matches LIGO observed within ~5%, the 10-18% offset isolates to **AVE's choice of Kerr-correction formula**, not the cold eigenvalue. KB framing should clarify this.
4. If GR-Kerr-full ALSO predicts 10-20% above LIGO (matching my simplified GR-Kerr column), then the 10-18% offset is a real LIGO ↔ both-theories discrepancy that needs alternative explanation (mass/spin estimation systematics? Detection-bias in published f_obs? Non-fundamental ringdown mode?)

This finding does NOT change the KB's 1.7% AVE-vs-GR-cold claim (verified PASS). It does suggest the **"10-18% from 3 LIGO events" framing needs a methodological footnote** about which GR Kerr-correction method is the reference.

### §6.4 Phase-1 outcome summary

- **KB AVE prediction table: VERIFIED** as computationally self-consistent (PASS)
- **KB-cited AVE-vs-observed Δf: REPRODUCED** exactly (10.6, 10.5, 17.8 %)
- **AVE-vs-GR cold eigenvalue: VERIFIED** at 1.7% as claimed
- **Phase 2 flag:** AVE's simplified Kerr correction over-corrects vs full GR Leaver-QNM; the 10-18% offset may be Kerr-formula-sensitive rather than uniquely AVE-distinct. Need full Kerr QNM for fair comparison.

### §6.5 Status of matrix row C1-BH-RING after Phase 1

The C1 row's `Outcome` cell can move from `TBD` to `partial-PASS` with caveat:
- AVE prediction matches the KB table self-consistently (PASS)
- AVE prediction is 10-18% above LIGO observed using AVE's Kerr correction (CONFIRMED)
- Whether this is uniquely AVE-distinct vs Kerr-formula-sensitive: **PENDING PHASE 2**

The C1 row's `Substrate` cell can move from `MISSING` to `src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py` (this driver).

The C1 row's `Comparison source` cell can resolve `TBD pin which 3 events` → **GW150914, GW170104, GW151226** (now explicit per `ave-bh-horizon-area-theorem.md:78` + `ave-merger-ringdown-eigenvalue.md:46-48`).

C1 row update happens when this branch merges back to L3 (or via cherry-pick to `analysis/divergence-test-substrate-map`).
