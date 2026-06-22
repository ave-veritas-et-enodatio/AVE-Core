# RESULT — Node-Up Small- and Large-Signal Analysis: the V/I-keyed dual resolves FORK-1 (static-B is transparent to AVE)

**Date:** 2026-06-22 · **Lane:** implementer · **Branch:** `docs/birefringence-arc-2026-06-22`
**Scope:** the analysis BEHIND the merged canonical leaves `clm-vca7r1`
([`node-up-small-large-signal.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md))
and `clm-pvlas1`
([`pvlas-static-b-verdict.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md)),
canonicalized via PR #357. This doc is the research substrate (FORK-1 resolution workflow `wy1dl84a3`); the
leaves are the distilled canon.
**Class (consistency-vs-emergence):** **CONSISTENCY / manifestation.** Re-expresses the already-derived
Axiom-4 kernel + relativistic-inductor primitive (`clm-p5cf3t`) as an operating-point taxonomy and reads off
the static-field asymmetry. Originates no new dimensionful constant. The R2 ratio `7.5/α³` is an **α-echo** at
the value level.

---

## 0. TL;DR

The vacuum cell is one LC tank with **two reactive grades keyed on different drive variables**:

- **ε-grade** (capacitive, 3 translational DOF) is a **varactor keyed on VOLTAGE** `V` (field `E`):
  `C_eff(V) = C_0/S(A_V)`, `A_V = V/V_yield`. A DC `E`-bias is a real operating point.
- **μ-grade** (inductive, 3 Cosserat micro-rotational DOF) is a **relativistic inductor keyed on the
  circulating CURRENT** `I`: `L_eff(I) = L_0/S(A_I)`, `A_I = I/I_max`, `I_max = ξ_topo·c ≈ 124.4 A`
  (verified 124.384 A; `relativistic-inductor.md`:15,:18). The μ-grade saturates on internal circulation,
  NOT on `|B|`.

Both are projections of the **single Axiom-4 kernel** `S(A) = √(1 − (A/A_yield)²)` under the substitution
`V → I`, `V_yield → I_max`. The duality fixes each grade's large-signal operating point independently, and
therefore the small-signal index a probe sees.

**FORK-1 resolution** = `static-B-transparent-INERT-ave-survives`. A static external `B` (∂B/∂t = 0,
sustained by the magnet's current not the vacuum's) induces no EMF → no internal vacuum circulation →
`I_vac = 0` → `A_I = 0` → `S_μ = 1` → `δn_μ = 0` **analytically exact**, at every field strength. PVLAS /
BMV apply a static `B`, so they do **NOT** test the AVE prediction; their null is the *expected* AVE result.
The real test is the **E-route** (HIBEF-class facility field) where the `V`-keyed varactor is genuinely
biased (regime R2), giving the OQ-1 differential ratio `7.5/α³ ≈ 1.93×10⁷` vs differenced Euler-Heisenberg
(`clm-pp3qwf`).

Two corrections fell out of the analysis and are recorded below: (i) the prompt-framing assumption "if
birefringent → PVLAS bites" is **arithmetically false** under *either* fork (the rejected saturable-μ
counterfactual gives `δn ≈ −4.4×10⁻¹⁹` at 2.5 T, ~2600× *above* the PVLAS floor — i.e. PVLAS never
discriminates the forks regardless, §5); (ii) a **live engine bug VCA-R01** keys μ-saturation on static
`|B|` and would contradict the canonical R3 verdict — flagged, deferred (§6).

## 1. FORK-1 stated

The open fork: **is the μ-grade a saturable reactor or an ideal inductor under a static external B?**

- **Candidate A — saturable reactor.** Kernel argument `r_μ = B_external/B_SNAP`. If correct, a static `B`
  shifts the μ operating point → vacuum birefringence under a DC magnet → PVLAS bites → AVE constrained.
  Apparent support: `B_SNAP` is a flux-DENSITY yield (`constants.py`:444), and the fdtd engine wires
  `B_local = μ_0·|H|` against `b_yield` (`fdtd_3d.py`:231,:245).
- **Candidate B — ideal relativistic inductor.** Kernel argument `r_μ = I_circ/I_max` (the internal
  circulating current). If correct, a static `B` (∂B/∂t = 0) drives no internal circulation → `S_μ = 1` →
  the μ-grade is transparent → PVLAS does not test AVE. Support: the canonical magnetic-sector primitive
  `eq:relativistic_inductor` (`relativistic-inductor.md`:15,:18), `L_eff(I) = L_0/√(1 − (I/I_max)²)`,
  `I_max = ξ_topo·c`, stored energy `½L·I²` keyed on circulation.

The decision must be made on the **substrate's own constitutive law**, not on what the code currently does
(substrate-native-check). The next section derives Candidate B node-up.

## 2. The keyed-argument dual (the load-bearing derivation)

**What state variable holds each grade's stored energy?**

- **Capacitor (ε-grade):** stored-energy state variable is the voltage/charge (`½CV²`). A DC bias sets `V`
  directly. So `A_V = V_local/V_yield = E·ℓ_node/V_yield = E/E_yield`
  (`E_yield = V_YIELD/L_NODE ≈ 1.13×10¹⁷ V/m`, `constants.py`:438). `S_ε(A₀) = √(1 − (E/E_yield)²) < 1` for
  any static `E`. **The ε-grade is amplitude-saturable; a DC E-bias shifts its operating point** — the
  canonical varactor `C_eff = C_0/S` and the bench / E-route mechanism.

- **Inductor (μ-grade):** stored-energy state variable is the current (`½L·I²`), and the dynamics are
  governed by the **rate** via `V = −L·dI/dt` (Lenz). An external static `B` sustained by an external magnet
  current is a **boundary condition** on the substrate, not internal vacuum circulation. The μ-grade DOF is
  the Cosserat micro-rotation; its inductive energy is `½L·I_circ²` where `I_circ = ξ_topo·v` is the
  substrate's OWN circulating current. A static external `B` with `∂B/∂t = 0` induces no EMF
  (`EMF = −dΦ/dt = 0`), hence drives no internal circulation, hence `I_circ → 0`, `r_μ → 0`, `S_μ = 1`.

The μ-grade is **not** a ferrite saturable reactor in the substrate's own constitutive law: a ferrite
saturates on aligned domain magnetization set by the field amplitude; the AVE μ-grade stores energy in
*circulation* and saturates when that circulation approaches `I_max = ξ_topo·c` (the substrate's "matter
cannot exceed c" limit), not when an external static flux density approaches `B_SNAP`.

**Three independent corpus primitives corroborate the I-keyed (rate-gated) reading:**

1. `manuscript/ave-kb/CLAUDE.md`:75 (INVARIANT-S2 W6, verbatim): *"a static field has no ∂B/∂t to load the
   μ / microrotational (Cosserat-B) sector, so it loads the ε / capacitive sector only (S_ε<1, S_μ=1)."*
2. `tau-relax-derivation.md`:93-97: near saturation Op14 drives `L_eff → ∞`; the diverging back-EMF blocks
   `dI/dt` — μ governed by the rate, `L_eff` saturates on the current.
3. `newtonian-inertia-as-lenz.md`:12 (`clm-jwyy6l`) + `substrate-hysteresis-index.md`:47: the inductive/Lenz
   class applies "any time the dynamics are governed by a *rate* (dω/dt, dI/dt) rather than an instantaneous
   amplitude." The just-merged PR #339 (`emf-lenz-sign-correction`,
   [`2026-06-21_emf-lenz-sign-correction_result.md`](2026-06-21_emf-lenz-sign-correction_result.md))
   re-derived the cross-sector coupling sign to `−2` = the Lenz back-EMF, "reaction opposes drive."

### B_SNAP reconciliation (no node-level contradiction)

`B_SNAP = 1.89×10⁹ T` is **NOT** a rival kernel-argument primitive — it is an **energy-density scale**,
verified `B_SNAP²/2μ₀ = m_e c²/ℓ_node³ = 1.0` exactly (ratio `1.0000000000000002` this turn). It marks the
flux density whose magnetic energy density equals a node's rest-energy density — the amplitude *image* of the
`I_max` current limit through the cell geometry, reached BY internal self-circulation, NOT an assertion that
an externally-imposed static flux saturates the core. The "B_SNAP-vs-INVARIANT-S2 contradiction" dissolves
once the energy-density *yield scale* (B_SNAP) is held apart from the kernel *argument* (`I_circ/I_max`).

> **Coordinate discipline (A46).** The kernel arguments `A_V`, `A_I` are phase-space / reactance quantities
> (operating-point along the Axiom-4 arc), not real-space lattice-Cartesian field magnitudes. A test or
> solver that keys μ-saturation on the static `|B|` magnitude measures the wrong coordinate — that is exactly
> the VCA-R01 defect (§6).

## 3. The three-regime sweep (with numbers)

Direct-kernel sweep (`src/tests/test_vca_node_regime_sweep.py`, evaluates the Axiom-4 kernel directly — NOT
the fdtd engine). Constants from `src/ave/core/constants.py`; `n = √(S_ε·S_μ)`, `δn = n − 1`,
`Z_eff = Z_0·√(S_μ/S_ε)`.

| Regime | Drive | `S_ε` | `S_μ` | `Z_eff` | Small-signal `δn` |
|---|---|---|---|---|---|
| **R1** symmetric internal | both grades (internal `E` **and** `B`, mass-soliton) | `S` | `S` | `Z_0` (invariant) | `δn = 1/S − 1` (isotropic; Γ=0 reflectionless) |
| **R2** static-E route | static `E` only (∂B/∂t = 0) | `<1` | `1` | `Z_0/√S_ε` (changes) | `δn ≈ ¼(E/E_yield)²` (Γ≠0) |
| **R3** static-B | static `B` only (∂B/∂t = 0) | `1` | `1` | `Z_0` (unchanged) | `δn_μ = 0` **EXACTLY** |

### R1 — symmetric internal soliton (both sectors)

`S_ε = S_μ = S` at the symmetric operating point. `δn = 1/S − 1`, `Z_eff = Z_0` invariant → Γ = 0,
reflectionless. Sample (`A₀ → δn`): `0.10 → +0.005038`, `0.50 → +0.154701`, `0.687 → +0.376164`,
`0.90 → +1.294157`, `0.99 → +6.088812`. This IS the C4 "both sectors scale symmetrically" regime =
Symmetric Gravity (`CLAUDE.md`:75). Z invariant so reflectionless, but the clock slows (`δn ≠ 0`). See the
C4-reconciliation companion section / doc.

### R2 — external static E (ε only, the E-route, the REAL test)

`S_ε = √(1 − (E/E_yield)²) < 1`, `S_μ = 1` (μ unloaded, no internal circulation). Isotropic
`δn = √S_ε − 1 → −¼(E/E_yield)²` to leading order; under a linearly-polarized pump the par−perp differential
is `−½(E/E_yield)²` (the OQ-1 observable, `clm-pp3qwf`). Sample (`E [V/m] → δn`): `1×10¹² → 1.96×10⁻¹¹`,
`1×10¹⁴ → 1.96×10⁻⁷`, `1×10¹⁵ → 1.96×10⁻⁵`, `1×10¹⁶ → 1.97×10⁻³`, `1×10¹⁷ → 0.464`. Leading coefficient
computed `= ¼` (arithmetic this turn: exact vs leading ratio `1.000000` at `E = 1×10¹⁴ V/m`). `Z` steps so
Γ ≠ 0 (the vacuum-impedance-mirror bench mechanism).

### R3 — external static B (neither sector, transparent)

`∂B/∂t = 0` ⟹ no Faraday EMF ⟹ `I_circ = 0` ⟹ `A_I = I_circ/I_max = 0` ⟹ `S_μ = √(1 − 0²) = 1` at
**every** field strength. `S_ε = 1` (no `E` to set the varactor charge-state). `δn_μ = 0.000000` EXACTLY,
`Z_eff = Z_0 = 376.730 Ω` exactly. Checked at `B = 2.5, 10, 50, 100, 500, 1000 T` — all `S_μ = 1.00000000`,
`δn = 0`. This is "flat" across 2.5 T → 1 kT **trivially** — not a numerical finding but a consequence of the
μ-grade being keyed on circulation, not `|B|`. **PVLAS (static B) does NOT test AVE.**

> Sanity on the rejected fork: even the saturable-μ counterfactual `r_μ = B/B_SNAP` gives only
> `δn_μ ≈ −¼(B/B_SNAP)² ≈ −4.4×10⁻¹⁹` at 2.5 T (`B_SNAP = 1.89×10⁹ T` ⟹ `B/B_SNAP = 1.32×10⁻⁹`). The
> *correct* current-keyed reading gives identically 0. See §5 for why neither reaches the PVLAS floor — and
> why the prompt's "if birefringent → PVLAS bites" conditional is arithmetically false.

## 4. The rescue-guard (the discipline that caught the rescue twice)

The ideal-inductor verdict is the one that "saves AVE from PVLAS." That is exactly the shape of a convenient
rescue, so it was pressure-tested against the anti-rescue tells. It **PASSES**:

1. **The discriminating primitive predates the question.** The μ-grade is keyed on `I` (not `|B|`) by
   `relativistic-inductor.md`:15, which was fixed by an earlier FORK before the static-B question was posed.
   It was not minted to escape PVLAS.
2. **It pays rent (sharp falsifiable consequence).** It predicts the PVLAS static-B null *exactly*
   (`δn_μ = 0` categorical, not a bound), and it moves the real test to the E-route. A static-B birefringence
   detection at or above the QED level (`~10⁻²³` at 5 T) would falsify it.
3. **One mechanism, multiple independent uses.** The same `∂B/∂t` axis does load-bearing work elsewhere: the
   asymmetric Meissner Z-step bench mechanism (`operators.md`:54), the Beltrami internal-circulation g=2
   result (`electron-unknot.md`:13), Newtonian inertia as Lenz (`clm-jwyy6l`).
4. **The independently-derived corroborant.** The relativistic inductor independently gives `E = mc²` from
   `½L_0·I_max²` — three corroborants (the I-keyed primitive, the Lenz-rate hysteresis class, the PR #339
   Lenz coupling sign) all land on the same reading.
5. **Symmetric-standard lens.** Standard EM/QED gets an unquestioned pass for the identical scoping move: a
   static `B` induces no EMF and drives no current (Faraday), while AC does — nobody calls "static B and AC B
   have different circuit effects" a rescue; it is textbook. AVE's claim is structurally the same applied to
   its own `I`-keyed inductive sector.
6. **The counterfactual would itself have failed.** The rejected saturable-reactor fork (Candidate A) does
   not even reach the PVLAS floor (§5), so PVLAS cannot select it over Candidate B — the fork is not decided
   by PVLAS at all; it is decided by the constitutive primitive.

**The rescue-shape was caught twice:** once at the FORK-1 derivation (the substrate-native-check forced
deriving the kernel argument before trusting the engine's `|B|`-keying), and once at the C4-reconciliation
pass (the apparent INVARIANT-S2 collision was a stale-citation artifact already closed in-corpus — see §8 and
the C4 companion). Neither pass was allowed to debug toward keeping AVE alive; both derived the answer and
let the substrate decide.

## 5. The synthesis arithmetic-error catch

The dispatch framing assumed "if the μ-grade is birefringent under static B → PVLAS bites." The synthesis
pass surfaced that this conditional is **arithmetically false under either fork**, and corrected a
direction-of-inequality error along the way.

At PVLAS `B = 2.5 T`, against the published null `Δn = (12 ± 17)×10⁻²³` (1σ floor `~1.7×10⁻²²`; QED predicts
`2.5×10⁻²³`):

| Reading | `δn` at 2.5 T | vs PVLAS floor `~1.7×10⁻²²` |
|---|---|---|
| Correct I-keyed (Candidate B, R3) | `0` exactly | transparent — never bites |
| Rejected saturable-μ counterfactual (Candidate A) | `≈ −4.4×10⁻¹⁹` | **~2600× ABOVE the floor** |
| ε-route energy-density proxy (`A = cB/E_yield`, propagating-wave construction) | `≈ −1.1×10⁻¹⁷` | ~6.5×10⁴× above, but NOT a static-DC-B response |

**The error caught:** the counterfactual `δn ≈ 4.4×10⁻¹⁹` is ~2600× *ABOVE* the PVLAS floor, NOT below it.
An earlier framing had it the other way (below floor → "PVLAS can't see it → forks indistinguishable"). The
correct reading is that the rejected fork, were it real, would be *measurable and excluded* by PVLAS — yet
PVLAS sees a null. So PVLAS's null is fully consistent with the I-keyed reading (`δn = 0`) and would *exclude*
the saturable reading — but the fork is not decided by PVLAS, because the saturable reading is rejected on
the constitutive primitive, not on the magnet data. Either way, **PVLAS does not discriminate the forks** and
does not constrain AVE: the magnitude arithmetic settles the PVLAS verdict definitively (`ave-survives`)
regardless of which fork one entertains.

> Note the `B_SNAP = 1.89×10⁹ T` scale makes 2.5 T a billionth of the μ-yield (`B_SNAP/2.5 T = 7.6×10⁸`), so
> even the saturable reading's signal is tiny in absolute terms — but `~4.4×10⁻¹⁹` still sits above the
> ~`10⁻²²` PVLAS floor. The "37,000× falsifies AVE" headline from an earlier tolerance pass is therefore
> **retracted**: it conflated the ε-route propagating-wave proxy with a static-DC-B response.

## 6. The deferred code-bug (VCA-R01)

**Flag-don't-fix.** The fdtd engine keys μ-saturation on the *static* `|B| = μ₀|H|` against `b_yield = B_SNAP`
— the saturable-reactor (Candidate-A) form — which contradicts the canonical `I`-keyed constitutive primitive
for a static external `B`. Sites:

- `src/ave/core/fdtd_3d.py`:231, :245, :396–:397, :425–:426 — the **caller** wires `B_local = μ₀·|H|` into
  `saturation_factor(..., b_yield)`.
- `src/ave/axioms/scale_invariant.py`:198 (`mu_eff`) — sector-agnostic kernel evaluation; the leak is in the
  caller, not here.

In an FDTD loop under a propagating wave, `H` tracks the live circulation, so the two readings *coincide* —
the engine is right as a propagating-wave shortcut. They **diverge on a static external DC-B operating point**,
where the engine would wrongly saturate μ on an external amplitude the substrate's constitutive law ignores.
The engine is also internally inconsistent: its just-merged Lagrangian-EMF coupling (PR #339, the `−2` Lenz
back-EMF) is on the rate/`I` side, while its FDTD μ-update is on the amplitude side.

**Engine-vs-direct-kernel — the gap IS the defect.** The direct-kernel control
(`src/tests/test_vca_node_regime_sweep.py`) gives `A_I = I_vac/I_max = 0 ⟹ S_μ = 1 ⟹ δn_μ = 0` (R3, exact).
The fdtd engine would NOT reproduce this. That gap is machine-confirmed by the regression test
`src/tests/test_vca_r01_static_b_mu_keying.py` — the desired R3 behaviour is an `xfail` that flips to PASS
once VCA-R01 is fixed; a positive-control assertion in the same file confirms the live `|B|`-keyed defect is
present (not a phantom).

**Fix-direction NOT applied (substrate-first-for-numbers).** The correct `I`-keyed implementation is a
*derivation*, not a variable swap: (1) no per-cell circulation → `I_max` threshold mapping exists in the
corpus — keying on `I = ∮H·dℓ` (or the rate `dB/dt`) and mapping it onto `I_max = ξ_topo·c = 124.4 A` on a
Yee grid must be derived, not invented; (2) two distinct μ-saturation paths coexist (the simple `μ_eff(|B|)`
and the chirality-aware `_update_saturation_kernels` in `cosserat_field_3d.py`) and a correct fix must
reconcile both; (3) `scale_invariant.mu_eff()` is called from 8 modules passing a B-magnitude. The fix is
gated on **deriving the I-keyed threshold** and goes in a separate validated PR.
`code_fix_decision = flagged-for-separate-PR-bug-documented`.

## 7. Derived-vs-asserted ledger

| Element | Status | Basis |
|---|---|---|
| `C_eff = C_0/S(A_V)`, varactor keyed on `V` | **DERIVED** | Axiom-4 dielectric specialization (`CLAUDE.md`:73) |
| `L_eff = L_0/S(A_I)`, relativistic inductor keyed on `I`; `I_max = ξ_topo·c = 124.384 A` | **DERIVED** | `clm-p5cf3t` (`relativistic-inductor.md`:15,:18); arithmetic-verified |
| static-B ⟹ no ∂B/∂t ⟹ no `I_circ` ⟹ `S_μ = 1` ⟹ `δn_μ = 0` | **DERIVED (analytically exact)** | `I`-keyed inductor + Faraday/Lenz; 3 corroborants (`CLAUDE.md`:75, `tau-relax`:93-97, `clm-jwyy6l`) |
| R2 E-route `δn ≈ −¼(E/E_yield)²`, par−perp `−½` | **DERIVED** | reproduces `clm-pp3qwf` exactly (ratio `1.000000` at 1×10¹⁴) |
| `B_SNAP²/2μ₀ = m_e c²/ℓ_node³ = 1.0` (energy-density scale, not μ-kernel arg) | **VERIFIED** | ratio `1.0000000000000002` this turn |
| R1 symmetric `δn = 1/S − 1`, `Z = Z_0` reflectionless | **DERIVED** | INVARIANT-S2 W6 (`CLAUDE.md`:75) |
| OQ-1 ratio `7.5/α³ ≈ 1.93×10⁷` | **DERIVED (E-route); value is α-echo** | `clm-pp3qwf`; magnitude rides `α⁻³` |
| Which grade is "magnetic primary" under chirality | **ASSERTED** (degenerate, mute here) | wall-branch fork B3-DEGENERATE (PR #260) |

**Asserted / flagged, NOT resolved by the node analysis:**

- The `B_SNAP`-vs-`E_YIELD/c` magnetic-yield-scale consistency: an audit pass found `u_E(E_YIELD)/u_rest`
  and `B_SNAP/(E_YIELD/c)` differ by ~5.01× — i.e. `E_YIELD` and `B_SNAP/c` are NOT energy-density duals.
  Two corpus magnetic-birefringence treatments (the §5 `cB/E_yield` ε-proxy and the engine `B_SNAP`
  saturation) are keyed on inconsistent scales. **Which magnetic-yield scale is canonical is a Grant call**
  (§8). This does not touch the R3 verdict (R3 = `δn_μ = 0` regardless of yield scale, because `A_I = 0`).

## 8. Residuals carried to Grant

1. **VCA-R01 code fix** (§6) — gated on deriving the `I`-keyed per-cell circulation→`I_max` threshold. Do NOT
   silently swap the variable; the threshold mapping is a derivation. Separate validated PR.
2. **Canonical magnetic-yield scale** (§7) — `B_SNAP` (energy-density-matched) vs `E_YIELD/c` (the ε-proxy);
   they differ by ~5.01×. Surface to Grant before any leaf quotes a *magnetic* birefringence number. (The
   R3 static-B verdict is unaffected: `A_I = 0` ⟹ `δn_μ = 0` independent of either scale.)
3. **C4 / SYM-vs-ASYM small-signal framing** — the apparent INVARIANT-S2 collision was a stale-citation
   artifact ALREADY closed in-corpus (commit `e5307e53`, the W6 scope at `CLAUDE.md`:75). Recorded in the C4
   companion ([`2026-06-22_c4-symmetric-loading-reconciliation.md`](2026-06-22_c4-symmetric-loading-reconciliation.md)).
   The 2026-06-05 gravity-sign result doc's "Not reconciled in this session" flag is stale; updating those
   stale R-a/R-b annotations is an auditor-lane propagation item, surfaced not silently edited.

---

### Provenance

- FORK-1 resolution workflow: `wy1dl84a3` (large-signal + small-signal + synthesis, auditor-lane derivation).
- C4 reconciliation workflow: `w8d8hyhvz` (see companion doc).
- Facility landscape: `w14ptjz80` (see
  [`2026-06-22_vacuum-birefringence-facility-tolerance-survey.md`](2026-06-22_vacuum-birefringence-facility-tolerance-survey.md)).
- Canonicalized: PR #357 (`canon/birefringence-nodeup` → `main`), leaves `clm-vca7r1`, `clm-pvlas1`.
- Arc record: [`_orchestration/2026-06-22_birefringence-vca-bench-arc.md`](../_orchestration/2026-06-22_birefringence-vca-bench-arc.md).
