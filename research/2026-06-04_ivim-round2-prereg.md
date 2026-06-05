# IVIM Round-2 pre-registration — interferometric re-scope (R-A) (2026-06-04)

**Lane:** implementer. **Branch:** `analysis/2026-06-04-ivim-round2-rescope`.
**Authorizing adjudication:** [`research/2026-06-03_ivim-RA-adjudication.md`](2026-06-03_ivim-RA-adjudication.md)
(Grant 2026-06-03: **R-A** — re-scope IVIM bench from 70σ APD photon-counting to an
interferometric scalar-phase precision measurement off the **correct per-node** kernel).

This pre-reg freezes the round-2 question, the operating-point, the observable, the
adjudication criteria, and the corpus-grep BEFORE deriving (per `ave-prereg`).

---

## 0. Disciplines fired (pre-work skill plan)

| Skill | Why | Outcome |
|---|---|---|
| `ave-prereg` | corpus-grep before deriving | §3 inventory completed before any number computed |
| `ave-canonical-source` | no hardcoded substrate numbers | `V_YIELD, E_YIELD, L_NODE(=ℓ_node), Z_0, ALPHA, EPSILON_0` imported from `ave.core.constants` |
| `consistency-vs-emergence` | classify the interferometric observable | §4 — **consistency-class** observable + **manifestation/structural** discriminator |
| `phase-space-coordinate-check` | is the observable phasor/impedance-plane? | §2.4 — scalar phase Δφ is real-scalar; matched-coordinate for an interferometer; the impedance-plane Γ is NOT the readout |
| `ave-walk-back` | leaf-local retire of the photon-counting headline | applied WITHIN `vacuum-impedance-mirror.md` only (deliverable c) |
| `ave-evidence-framing-discipline` | honest magnitude + SNR, no headline inflation | §2.3 honest SNR table |

## 1. The round-2 question (frozen)

The leaf [`vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md)
derives the kernel `ε_eff(V) = ε₀√(1−(V/V_yield)²)` and then plugs the **apparatus gap
voltage** (43.65 kV across a 100 µm gap) into the **per-node** ratio as if `V→V_yield`,
yielding `Γ→1` (perfect mirror) and a 70σ APD photon-count. Round-1
([RA-adjudication §3](2026-06-03_ivim-RA-adjudication.md)) showed the true per-node strain
at that apparatus field is `A = E_local/E_yield ≈ 3.9×10⁻⁹`, not `V/V_yield ≈ 0.99` — the
headline is overstated by `d_gap/ℓ_node ≈ 2.6×10⁸`.

**Q-IVIM-R2:** *Off the CORRECT per-node kernel `A = E_local/E_YIELD`, what is the
defensible INTERFEROMETRIC observable (scalar phase shift Δφ from the `ε_eff(A)` index
modulation in a high-finesse cavity / Mach-Zehnder readout), and what is its honest
shot-noise-limited SNR at the recommended tabletop geometry?*

## 2. Pre-registered derivation plan + operating point

### 2.1 Kernel → index → phase (the chain, fixed before computing)
- Kernel (leaf canonical, Ax 4): `ε_eff(A) = ε₀√(1−A²)`, **`A = E_local/E_YIELD`** (per-node
  strain, NOT `V_apparatus/V_YIELD`). `μ_local = μ₀` (asymmetric saturation, ε-only).
- Index (consistent with the leaf's `Z_local = Z₀(1−A²)^{−1/4}` chain):
  `n_eff = c√(μ₀ε_eff) = (1−A²)^{1/4}` → `δn = n_eff − 1 ≈ −A²/4` (leading, A≪1).
- Interferometric observable: `Δφ = (2π/λ) · δn · L_int`, λ = 532 nm probe, `L_int` = beam
  path through the high-field region.

> **FLAG (index-convention discrepancy, pre-registered, flag-don't-fix):** the sibling leaf
> [`ch12.../vacuum-birefringence-e4.md`](../manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md)
> and `divergence-test-substrate-map.md:63` write `Δn = 1 − √(1−A²) ≈ +A²/2`. The
> impedance-mirror leaf's own chain gives `δn ≈ −A²/4`. **Same E⁴ intensity-slope; the
> phase coefficient (factor 2) AND sign differ by convention.** This is surfaced for a
> cross-leaf reconciliation pass, NOT resolved here — round-2 reports BOTH and uses the
> mirror-leaf's own `−A²/4` for the mirror-leaf re-scope (self-consistent within the leaf).

### 2.2 Operating point (frozen — per RA §5.2)
- **NOT** "sweep up to V_yield." 43.65 kV is not a ceiling at the apparatus scale.
- Report THREE operating points: (a) uniform 43.65 kV / 100 µm (the leaf's literal
  geometry); (b) STM sharp-tip enhancement R_tip = 10 nm, geometric factor β ≈ 1/5
  (consistent with the Q-G42 `G_geom ~ 10⁵` sharp-tip-pair figure, `trampoline-framework.md:685`);
  (c) push-to-breakdown variant (V > 43.65 kV until field-emission/vacuum-breakdown onset).
- The real ceiling is electrode field-emission / vacuum breakdown (~few×10¹⁰ V/m at a
  clean tip), NOT V_yield.

### 2.3 SNR (frozen)
- Shot-noise-limited interferometer: `Δφ_min = 1/√N_ph`, `N_ph = P·τ·λ/(hc)`, P = 0.5 mW.
- Report SNR at τ ∈ {1 s, 1 hr, 1 day, 1 month} and the integration time to reach SNR = 1.
- Report the field needed for SNR = 1 in a 1-day run, and whether it is below or above
  field-emission onset.

### 2.4 Coordinate discipline (`phase-space-coordinate-check`)
The corpus claim Γ(V) lives in the **impedance plane** (Z_local/Z₀). The READOUT, however,
is a **real scalar phase Δφ** of the transmitted/circulating probe (high-finesse cavity
fringe shift). These ARE matched coordinates for an interferometer: an isotropic δε shifts
the scalar phase velocity → fringe shift; no phasor/Clifford-torus projection is involved.
The impedance-plane Γ is a *derived* reflectance, NOT the measured quantity in the
interferometric re-scope. The candidate STRUCTURAL discriminator (isotropic scalar-phase
vs QED's anisotropic birefringence) is a polarization-pattern test, also real-space-matched.

## 3. Corpus-grep (DONE before deriving — `ave-prereg`)

Conflation = an **apparatus gap voltage** (30/35/43 kV across ~100 µm) substituted into the
per-node ratio `(V/V_yield)` as if `V_apparatus → V_yield`. NOT a conflation: sites that
quote the kernel *constitutive form* `S(V) = √(1−(V/V_yield)²)` where `V` denotes the
per-node voltage (design-rule / symbol-encoding references).

**IVIM-LOCAL (this branch may re-scope — per RA §6):**
- `vacuum-impedance-mirror.md` (the leaf; deliverable c).
- `vol4/claim-quality.md` clm-5s5b0d (:354–377) + the IMD-variant line (:390).
- `cosmological-constant-closure.md:131` (Γ_bench headline).
- `vol4/falsification/ch11-experimental-bench-falsification/index.md:30` (Γ(V) row).
- `vol4/falsification/ch11-experimental-bench/advanced-protocols.md:29–37` (Z_local/Γ + "sweep past 35 kV → APD spike").
- `common/ave-analytical-toolkit-index.md:192` (Γ(V) entry).
- `common/divergence-test-substrate-map.md:63` (B1 row — but already uses correct `E/E_yield`).

**CORPUS-WIDE (BLOCKED on Grant §4 — INVENTORY ONLY, do NOT edit):** see deliverable (b)
result-doc §"broader-conflation inventory". Headed by `measurement-hierarchy-snr.md:66` +
`universal-saturation-kernel-catalog.md:72` (the PONDER-05 `V_DC/V_yield = 0.687 @ ~30 kV`
pair) plus the full PONDER-05/divergence-map propagation.

## 4. Consistency-vs-emergence classification (frozen)

| Component | Class | Justification |
|---|---|---|
| The phase-shift Δφ itself (small-A) | **consistency** | `claim-quality.md:75`: the leading correction is "formally identical to the Euler-Heisenberg low-field limit; recovers linear Maxwell." Δφ at A≪1 is a quadratic-in-A index shift that QED ALSO predicts (different coefficient). Not emergence. |
| Tree-vs-loop coefficient (the 8.38×10¹² ratio) | **manifestation / structural** | AVE Δφ ~ A² is a TREE-level kernel term; QED's is a LOOP (Euler-Heisenberg). The ratio is a structural scaling-origin difference, traced clean in round-1, zero free parameter. |
| Isotropic scalar-phase vs anisotropic birefringence | **manifestation / structural** | AVE kernel keys off `|E|` (isotropic) → scalar phase; QED Euler-Heisenberg vacuum is birefringent in a background field. Pattern discriminator, not a coefficient. |

**Headline rule (`ave-evidence-framing-discipline`):** do NOT headline this as an emergence
result. The defensible content is a *structural discriminator* (tree-vs-loop + isotropy)
whose *magnitude is undetectable at the recommended tabletop geometry* (see result doc SNR).

## 5. Adjudication criteria (frozen BEFORE the result — no post-hoc drops, Rule 11)

- **DEFENSIBLE-INTERFEROMETRIC-DISCRIMINATOR** iff: (i) Δφ derives cleanly off the correct
  per-node `A = E_local/E_YIELD` (no apparatus/per-node conflation), AND (ii) at least one
  structural axis (tree-vs-loop scaling OR isotropy-vs-birefringence) survives as a
  parameter-free AVE-vs-QED distinction, REGARDLESS of magnitude. Magnitude/SNR is reported
  honestly but does NOT gate the *structure* verdict.
- **RETIRE** iff: the per-node kernel does not produce any AVE-distinct interferometric
  signature even in principle (i.e., AVE and QED Δφ are indistinguishable in both scaling
  and pattern). If RETIRE, walk back the leaf to "subsumed by `vacuum-birefringence-e4.md`."
- **Honest-magnitude rider (NOT a verdict gate, an evidence-framing requirement):** the
  re-scoped leaf MUST state the SNR ≪ 1 at the recommended geometry and that the recommended
  tabletop apparatus is NOT a near-term falsifier. Failing to state this = framing violation.

## 6. What survives either verdict (pre-committed)

The **V⁴ scaling** and the **8.38×10¹² discrimination ratio** are traced clean in round-1
(RA §1) with zero free parameters. They are NOT re-litigated here; round-2 only fixes the
*detection mode + magnitude* and the *operating-point framing*.
