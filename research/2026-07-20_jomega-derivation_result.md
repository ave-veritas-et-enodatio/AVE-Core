# RESULT — J(ω) derivation: the z=3 bath spectral density as the yield-fork adjudicator (+ arccos drag-onset)

> **SECTOR HEADER (read first).**
> - **MODE:** derivation + 0D research-driver (explicit-bath GLE, ODE-level). Object = the z=3 srs bath spectral density `J(ω)` for the transverse-bow `S`, and the per-cycle energy ledger at the near-yield crossing. NOT a minimization, NOT continuum-Helmholtz. **Engine byte-UNTOUCHED.**
> - **REGIME / PHASE-STATE:** near-yield crossing, Regime II→III (`k4_tlm.py:308–311`), driven `ωτ≈0.9`; the *bath* is the cold-linear z=3 srs net.
> - **SECTOR:** load `A` = axial A1 dilatation (V-sector); response `S` = transverse **T2** bow. A1 ⊥ T2.
> - **DISCIPLINE:** frozen-then-run (prereg pushed before code, `research/2026-07-20_jomega-derivation_prereg_FROZEN.md`, base HEAD `64f1894d`). Rule-11 (frozen tree governs). Rule-12. Anti-seduction fence BOTH directions. Verify-before-cite. Flag-don't-fix.

**Date:** 2026-07-20 · **Lane:** implementer, J(ω) derivation (yield-fork adjudicator) · **Branch:** `research/jomega-derivation` · **Driver:** `src/scripts/vol_4_engineering/jomega_yield_fork.py` · **Test:** `src/tests/test_jomega_yield_fork.py` (7/7, `engine_sim`).

---

## 0. VERDICT (the frozen tree's output)

> **🔴 RE-BANKED 2026-07-20 (post-review repair, wrapper `wf_d07d804e` — 13 confirmed findings, 2 CRITICAL). Rule-12: the superseded verdict text is preserved verbatim in the banners below; the FROZEN prereg is untouched (Rule-11).** The original §0 banked the (c-scope) split as "coupling-scale-robust" with the ∞-lattice "draining to 0–10 %" and "the SCOPE-SPLIT is unambiguous [DERIVED]" — all from an **UNDRIVEN ring-down that is NOT in the frozen prereg** (§4-iv freezes only the DRIVEN protocol) run at a **single coupling scale (0.6)**. This repair (i) **RAN the frozen (a-ledger)/(b-ledger) net-per-cycle-transfer criterion** that was never computed [R-2, driver `frozen_ab_ledger`]; (ii) **added the coupling-scale scan** that was never shipped [R-1, `ringdown_scale_scan`]; (iii) re-banks honestly. The bin-(iii) DEGENERATE landing **SURVIVES**; the quantitative half of the scope-split **collapses into the already-UNDETERMINED coupling fork**.

### 0.1  FROZEN-CRITERION OUTPUT (Rule-11 — this governs the verdict; stated FIRST)

The frozen decision tree (prereg §4) lands in bin **(iii) DEGENERATE / UNDETERMINED**. It does NOT land cleanly in world (a) or world (b) — the honest, anti-seduction result.

**The frozen (a-ledger)/(b-ledger) criterion, run exactly as prereg §4-i,ii,iv specify** [DERIVED, `frozen_ab_ledger`; driven `r=0.7+0.3·sin(0.9t)`, per-mode `E_bath`, net-per-cycle transfer vs `tol=3.53×10⁻³` relative]:

| model / bath | net-per-cycle transfer (rel) | vs `tol=3.53e-3` | returns within window (Poincaré) | (a-ledger) | (b-ledger) |
|---|---|---|---|---|---|
| C1 on-site · finite `N=60` | `+3.2e-1` | **≥ tol** | returns (0.27) | ✗ | ✗ |
| C1 on-site · dense `N=1200` | `+5.4e-1` | **≥ tol** | stays up (0.50) | ✗ | ✗ |
| C2 strain · finite `N=60` | `+7.5e-2` | **≥ tol** | returns (0.35) | ✗ | ✗ |
| C2 strain · dense `N=1200` | `+3.7e-2` | **≥ tol** | stays up (0.58) | ✗ | ✗ |

**Neither (a-ledger) nor (b-ledger) fires.** Under continuous driving the net-per-cycle transfer EXCEEDS `tol` in **every** cell (even the finite/0D bath transfers above the integrator floor per cycle), so (a-ledger)'s `< tol` conjunct fails everywhere; the finite/0D bath RETURNS within the window (Poincaré, return-ratio 0.27–0.35) while the dense bath sits at 0.50–0.58 (NOT a clean monotone drain), so (b-ledger)'s "not-returned" clause is not cleanly satisfied either. **The pre-registered driven instrument does not separate the scopes** — exactly the muddiness `§4` discloses. The transfer MAGNITUDE tracks the undetermined coupling prefactor `ζ` (C2 dense: `5.6e-3` at scale 0.2 → `3.7e-2` at 0.6 → `1.3e-1` at 1.0), i.e. **the frozen tol-gate's quantitative verdict inherits the same indeterminacy as bin (c-magnitude)**. Frozen-tree output: **bin (iii) DEGENERATE**, with (c-magnitude) firing on the coupling-model split (§0.3).

### 0.2  Robust derived structure (SURVIVES the repair)

1. **[DERIVED] World (c) — an axiom-level resistor / rate-independent plastic loss — is EXCLUDED** (a re-confirmation of the exclusion already banked on main, `research/2026-07-19_flag-f-s-dynamics-derivation.md:20,223`, preserved through the `#744` re-bank `:237`; **corroborated here, not new**). The informative NEW content is that a lossless (`γ=0`) second-order `S` traces a **FINITE reactive loop** (`∮S dr` finite, existence-grade — O(0.2–1.4), window-dependent, §5/R-5), so **loop-area ≠ dissipation** — a finite pinched loop does not imply a resistor. The `W_diss = 0` at `γ=0` leg is a **definitional identity** (`γ∮v²dt = 0`; cannot fail — the discriminating leg is the finite loop, not the zero-work assert); the real (fireable) energy ledger is the **independent drive-work closure** `W_drive = κ∮S_eq·v dt ≈ W_diss` for `γ>0` (§5, closes to ≤2 %). Coupling-model- and scope-independent (the `γ=0` contrast has no bath).

2. **[DERIVED] The §4.3/§5.3 inconsistency of the flag-F doc is resolved** (§3): `πJ(ω→0)` (Markovian friction constant, slow-limit) and `πJ(ω_drive)` (finite-drive per-cycle transfer) are **different physical objects** (frequency-dependent friction), both legitimate, evaluated at different arguments.

3. **[DERIVED] The load-bearing band-edge correction:** the corpus-adjudicated arccos band top is `π√3·ω_C ≈ 5.44 ω_C`, **NOT the flag-F doc's assumed `ω_C`** — so the crossing (`ωτ≈0.9`) sits at ≈16 % of the band, **deep inside**, where `J(ω_drive) > 0`. This is why the fork is genuinely live (a hybrid), consistent with the flag-F re-bank (F1/F11).

4. **[DERIVED] Loss-location adjudication (§7):** Site 1 (vol_4 ch01:358, "max loss at `f≪1/τ`") is **the world-(c) picture — EXCLUDED**; Site 2 (backmatter:147, "zero-area elastic at `f≪1/τ`") is **CORRECT** there; Site 3 (`#735` Debye peak at `ωτ≈0.9`) is **CORRECT** for the loss peak. Flagged (not fixed) with verbatim citations. **(Kept only insofar as it is INDEPENDENT of the retracted claims** — it rests on the world-(c) exclusion above + `J(f≪1/τ)→0` in BOTH models, §7; confirmed independent.)**

5. **[DERIVED] Batched arccos drag-onset (§9):** `v_p,min/c₀ = 0.80` (srs 3D acoustic) and **exactly `1.0` (1D-chain arccos, dispersionless)** — the cosine-branch `2/π ≈ 0.637` **does NOT survive** the model switch.

### 0.3  POST-HOC CHARACTERIZATION (disclosed protocol provenance; NOT frozen-adjudicated; stated SECOND)

6. **[POST-HOC] The (a)/(b) crossing distinction is a SCOPE + COUPLING-MODEL question, not a clean XOR:**
   - **(c-magnitude) [FROZEN-SUPPORTED]:** the crossing *shape* verdict hinges on the one unforced modeling choice (S→bath coupling): on-site → **Ohmic** `J`, `J_norm(0.9ω_C)=0.31 ≥ 0.1` → world-(b) channel LIVE; strain → **super-Ohmic** `J`, `J_norm(0.9ω_C)=0.036 < 0.1` → world-(a) suppression. UNDETERMINED between them; choice surfaced, not silently picked. (This bin IS grounded in the frozen a-shape/b-shape thresholds.)
   - **(c-scope) [POST-HOC CHARACTERIZATION — the undriven ring-down is NOT in the frozen prereg]:** the ring-down ORDERING — **0D/finite-cell recovery ≥ ∞-lattice/dense recovery — is scale-robust** [R-1 scan, all 10 cells, `ringdown_scale_scan`]. But the DRAIN **MAGNITUDE is coupling-scale-governed, not robust**: the super-Ohmic (C2) ∞-lattice bath recovers **77 % at scale 0.2, 35 % at 0.4** (world-(a) reactive return), reaching the `0–10 %` band only at scale ≥ 0.6. The drain magnitude is set by the **same undetermined coupling prefactor `ζ`** as (c-magnitude) — so the quantitative (c-scope) reading collapses into the (c-magnitude) UNDETERMINED bin.

   > **🔴 RE-BANKED (Rule-12; superseded text preserved verbatim).** The original item 2/§4 banked: *"the **0D few-mode cell** (the actual scope of a single node's yield crossing) **recovers 70–95 % of `E_S`** (world-(a) reactive return, Poincaré recurrence); the **dense/∞-lattice bath drains to 0–10 %** (world-(b) transduction) … Robust to coupling model and coupling scale."* and *"**[DERIVED] The SCOPE-SPLIT is unambiguous.**"* — RETRACTED: the "0–10 %" magnitude and the "coupling-scale-robust" adjective are **live-fire false at weak coupling** (F1/F6/F9); the "unambiguous" grade rested on a detector whose window straddles both Poincaré times **by construction** (F3, §4). Only the ORDERING is scale-robust.

7. **[ASSERTED — routed to Grant] Grant's reversible-reactive lean at the 0D-cell scope.** The reading "the 0D few-mode cell = the actual scope of a single node's yield crossing" is **asserted, not derived** (F3): the ring-down window (fixed `T = 80·2π/ω_S`) straddles the finite-bath Poincaré time (`t_poin(N=40)=46` ≪ window `503`, ~11 recurrences) and the dense-bath one (`t_poin(N=1500)=1732` ≫ window, 0.29 recurrences) **by construction**, so the finite-recurs/dense-drains direction is a bath-discretization identity the detector cannot contradict. Whether a node embedded in the ∞-srs-lattice physically has a few-mode bath (0D, world-(a) character) or the lattice continuum (∞, world-(b) character) is **the open physical-scope question — routed to Grant**, not settled here. What the driver shows microscopically (Ax3-losslessness) is a **construction input** (the bath is built symplectic/Hamiltonian), not a finding.

**Anti-seduction fence held BOTH directions:** world (a) does not "win"; world (b) does not "win"; world (c) LOSES (corroborated); the fork was ill-posed as an XOR because it conflated scope — but which scope is the *physical* one is not adjudicated here.

**Flag F status:** **PARTIALLY discharged, advanced past OPEN-XOR.** World (c) exclusion corroborated (not new; §0.2); the (a)/(b) crux is named as a scope+coupling distinction, not a dichotomy; the frozen ledger is DEGENERATE and the physical-scope ruling stays Grant's. `I_S` kinetic-term provenance stays OPEN (§8; scope not stretched). **AWAITING GRANT RATIFICATION.**

---

## 1. The load-bearing band-edge correction (the pivot)

The flag-F doc §4.2 assumed the z=3 bath band edge is `ω_max ~ c/ℓ_node = 1/τ_relax = ω_C` (so `ωτ_max = 1`) and built its CRITICAL band-edge step (F1/F11) on it. The **corpus-ADJUDICATED** band model (`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/srs-band-structure.md`, `clm-bnd5rq`, gates PASS #604/#607) is the **arccos transmission-line map**:

```
ω_n(k) = ω_link · arccos(μ_n(k)/3),   ω_link = √3·ω_C,   band top = π·ω_link = π√3·ω_C ≈ 5.4414 ω_C  (at H).
```
**[ENGINE-READ / CANONICAL]** In `ωτ_relax` coordinates the bath band spans `[0, 5.44]`. The crossing at `ωτ ≈ 0.9` is at **16.5 % of the band top — deep INSIDE**, not near the edge. `J(ω_drive)` at the crossing is therefore **not band-edge-suppressed**; whether it is *appreciable* is a DOS/coupling question (§2). This corrects the flag-F doc's factor-≈5.4 underestimate.

---

## 2. The J(ω) derivation

**Density of states `g(ω)`** [DERIVED, dense BZ histogram of the arccos band, driver `density_of_states`]: `g(ω) ∝ ω^{1.844}` at low ω — the **3D acoustic Debye** form `g ∝ ω²` (the arccos acoustic branch is linear near Γ, velocity factor `1/√3`; in 3D that gives `g∝ω²`). Band-top van Hove structure; `g` cuts off at `5.44 ω_C`.

**Coupling model — the one unforced choice, both run** (prereg §3, driver `build_J`). `S` modulates `Z_eff = Z_0/√S` (Op14, `k4_tlm.py:315,318,362`), so the bond reflection `Γ_bond=(Z_B−Z_A)/(Z_B+Z_A)` (`k4_tlm.py:440`) couples `S` to the bond waves [ENGINE-READ]. Whether the linearized S→mode coupling is on-site or strain/gradient is **not fixed by the constitutive form alone**:

| model | `c(ω)` | `J(ω) = (π/2)g·c²/(m ω)` | low-ω exponent `s` (measured) | `J_norm(0.9 ω_C)` | class |
|---|---|---|---|---|---|
| **C1 on-site** | const | `∝ g/ω ∝ ω` | **0.844 (Ohmic, s≈1)** | **0.311** (appreciable) | world-(b) channel LIVE |
| **C2 strain** | `∝ω` | `∝ g·ω ∝ ω³` | **2.844 (super-Ohmic, s≈3)** | **0.036** (suppressed) | world-(a) shape |

**[DERIVED]** Both give `J(ω→0)=0` (elastic at DC), a peak at intermediate `ω` (`2.12 ω_C` C1 / `3.33 ω_C` C2), and `J=0` above the band edge. The **crossing shape verdict SPLITS on the coupling model** — the frozen `(c-magnitude)` UNDETERMINED bin, choice surfaced. The S-bow is an *internal transverse deformation* (buckling response), not a rigid translation, so on-site coupling (C1) is not forbidden by translation invariance; both remain physical candidates. **Deriving the absolute `c(ω)` scale (and hence the model) from the full engine constitutive tensor is the owed extension** (§11).

---

## 3. The two Γ objects — the §4.3/§5.3 inconsistency resolved

For the bilinear bath (`H_int = −S·Σ c_j q_j`), the friction is **frequency-dependent**. Two distinct objects, both legitimately `πJ(·)`:

- **Markovian friction CONSTANT** (§4.3's `πJ(ω→0)`): `γ_0 ≡ lim_{ω→0} J(ω)/ω`. The DC friction that would drive the overdamped first-order Eq 2.1. **[DERIVED]** C1 (Ohmic): `J/ω → const` (`γ_0` finite; measured `J/ω` low-ω slope `−0.28 ≈ 0`) ⇒ **Eq 2.1 recoverable in the slow limit** (`ωτ≪1`) with a finite `γ_0`. C2 (super-Ohmic): `J/ω ∝ ω^{1.7} → 0` (`γ_0 = 0`) ⇒ **no DC friction; Eq 2.1 NOT recoverable** as a friction-relaxation (the flag-F R-6 super-Ohmic branch — it *strengthens* world (a) at low frequency).

- **Per-cycle transduction at finite drive** (§5.3's `πJ(ω_drive)`): the energy dissipated into resonant bath modes per cycle at `ω_d` is `ΔE_cycle = π S_0² J(ω_d)`. It requires REAL bath modes at `ω_d`; `J(ω_d)` counts them. **[DERIVED]** Finite in BOTH models at the crossing (`0.31` C1 / `0.036` C2 of peak).

**Resolution:** these are a DC-limit constant vs a finite-frequency per-cycle transfer — different objects because the friction is dispersive. The flag-F doc's error was treating them as one `Γ`. **The crossing verdict uses `J(ω_drive)`; the Eq-2.1-recoverability uses `J(ω→0)`. State both; do not equate.**

---

## 4. The per-cycle GLE energy ledger at the crossing (the thing #744 said was never shown)

Explicit-bath realization (prereg §4-iv): `S` + `N` bath oscillators sampled from the srs arccos DOS, coupled bilinearly with counter-term, symplectic (velocity-Verlet) integration — energy-closed (|dH/H|≈3.3e-4), mode-resolved. Driven `r(t)=0.7+0.3 sin(ω_d t)`, `ω_d=0.9`, `S_eq` byte-locked to `k4_tlm.py:283`.

### 4.1  FROZEN (a-ledger)/(b-ledger) criterion — the pre-registered instrument, RUN [R-2, Rule-11]

The frozen tree §4-i,ii defines the world-(a)/(b) CHARACTER by the **net-per-cycle transfer vs `tol=3.53×10⁻³`** with **per-mode `E_bath`** — this was **never computed** in the original ship (finding F2/F5/F7/F12). Computed now [DERIVED, `frozen_ab_ledger`; net-per-cycle transfer = steady late-window secular slope of `E_bath` per drive cycle, relative to `E_S_peak`; `tol` = the `#735` integrator floor]:

| model / bath | net/cyc (rel) | vs `tol` | Poincaré return | `t_poin` / window | 90 %-modes |
|---|---|---|---|---|---|
| C1 on-site · finite `N=60` | `+3.2e-1` | ≥ tol | returns 0.27 | 69 / 209 | 2 |
| C1 on-site · dense `N=1200` | `+5.4e-1` | ≥ tol | stays 0.50 | 1386 / 209 | 14 |
| C2 strain · finite `N=60` | `+7.5e-2` | ≥ tol | returns 0.35 | 69 / 209 | 1 |
| C2 strain · dense `N=1200` | `+3.7e-2` | ≥ tol | stays 0.58 | 1386 / 209 | 20 |

**Frozen output (Rule-11):** the net-per-cycle transfer is `≥ tol` in every cell, so **(a-ledger) never fires** (its `<tol` conjunct fails even for the finite/0D bath — continuous driving pumps energy above the integrator floor each cycle); the finite bath returns within the window while the dense bath stays up at 0.50 (not a clean monotone drain), so **(b-ledger) does not cleanly fire either**. **Neither fires ⇒ bin (iii) DEGENERATE.** The transfer magnitude is coupling-scale-governed (see §4.3), so the frozen tol-gate's quantitative verdict is the same UNDETERMINED as (c-magnitude). **The pre-registered driven instrument does not separate the scopes** — the muddiness the original ship narrated but never quantified.

### 4.2  Undriven ring-down — POST-HOC CHARACTERIZATION (disclosed; NOT in the frozen prereg)

The original ship's clean split came from an **undriven ring-down** (`gle_ringdown`): displace `S`, let it ring, watch the `E_S` recovered after the initial decay. **This protocol is NOT in the frozen prereg** (§4-iv freezes only the DRIVEN protocol above) and its 0.4/0.2 thresholds were chosen after seeing the data — it is disclosed here as a **post-hoc characterization**, not a frozen adjudication (F5/R-2). At the single scale (0.6) the driver ran:

| model | 0D few-mode bath (`N=40`) | dense / ∞-lattice bath (`N=1500`) |
|---|---|---|
| C1 on-site | recovery **0.698** (recurs) | recovery **0.000** (drains) |
| C2 strain | recovery **0.948** (recurs) | recovery **0.101** (drains) |

**Structural caveat (F3):** the fixed window `T = 80·2π/ω_S = 503` straddles the two Poincaré times **by construction** — `t_poin(N=40)=46` (≈11 recurrences inside the window) vs `t_poin(N=1500)=1732` (0.29 recurrences) — so the finite-recurs/dense-drains DIRECTION is a bath-discretization identity the detector cannot contradict, not a contingent physical result. The microscopic Ax3-losslessness is a **construction input** (symplectic bath), not a finding.

### 4.3  Coupling-scale scan — the honest robustness claim [R-1, post-review extension]

The original ship banked "coupling-scale-robust" and "drains to 0–10 %" from the single scale 0.6. The scan (both models × scales, `ringdown_scale_scan`, `E_S` recovery finite/dense):

| model | 0.2 | 0.4 | 0.6 | 1.0 | 1.5 |
|---|---|---|---|---|---|
| C1 on-site (fin/den) | 0.93 / **0.16** | 0.90 / 0.00 | 0.70 / 0.00 | 0.81 / 0.00 | 0.75 / 0.00 |
| C2 strain (fin/den) | 1.00 / **0.77** | 0.99 / **0.35** | 0.95 / 0.10 | 0.78 / 0.00 | 0.87 / 0.00 |

**[DERIVED] What is robust vs what is not:** the **ORDERING `finite ≥ dense` is scale-robust** (all 10 cells). The **drain MAGNITUDE is NOT**: the super-Ohmic (C2) ∞-lattice bath recovers **77 % (scale 0.2), 35 % (0.4)** — world-(a) reactive return — reaching the `0–10 %` band only at scale ≥ 0.6. The drain magnitude is governed by the **same undetermined coupling-scale prefactor `ζ`** the lane fails-closed on in bin (c-magnitude); so the quantitative half of the (c-scope) split **collapses into the already-UNDETERMINED coupling fork**. Only the ordering survives as a scale-robust claim.

This is the flag-F §6 "0D recurs / ∞-lattice radiates" picture COMPUTED — but the DIRECTION is what is robust; the magnitude and the "0D = physical scope" reading are open (§0.3 item 7, routed to Grant).

---

## 5. First-order Eq 2.1 vs second-order reactive contrast + H-ledger (closes #735 C-3)

`#735` PROTOCOL-COMPLETION §8 / F-B3 SPEC'd but never ran the second-order reactive contrast. Run here on the identical drive [DERIVED, `first_order_loop` / `second_order_loop`]:

- **Loop-area peaks do NOT discriminate.** First-order Eq 2.1: `(r,S)` peak `ωτ=1.049`, `(V,I)` peak `ωτ=0.937` (reproduces `#735`'s `0.911` (V,I) / `~1.00` (r,S)). Second-order reactive: peaks also near `ωτ≈0.94–1.05`. **Both produce finite loops near `ωτ~1`** — the loop area alone cannot tell them apart (confirms `#735` F-B3).

- **★ The finite reactive loop at `γ=0` is the discriminator** [DERIVED, `second_order_loop`; R-4/R-5 re-bank]:

  | `γ` | `∮S dr` (loop area) | `W_diss = γ∮v²dt` | `W_drive = κ∮S_eq·v dt` (independent ledger) | ledger mismatch |
  |---|---|---|---|---|
  | **0.0** | **finite, window-dependent** (§below) | **0.0 (definitional identity)** | — (no steady state at γ=0) | — |
  | 0.05 | 0.390 | 0.518 | 0.509 | 1.7 % |
  | 0.2 | 0.903 | 1.152 | 1.149 | 0.2 % |
  | 0.5 | 0.654 | 0.838 | 0.837 | 0.07 % |

  **The discriminating content is the FINITE loop at `γ=0` — `loop-area ≠ dissipation`.** A lossless second-order `S` traces a finite pinched loop, so a **finite `∮` does NOT imply a resistor** (the world-(c) reading). Two re-banks the review forced:
  - **R-4 / F11 — the `W_diss = 0` leg is a DEFINITIONAL identity, not a ledger measurement.** `W_diss = γ∮v²dt ≡ 0` at `γ=0` for *any* trajectory — it cannot fail (the `#721`-W2 identity class), so it carries no evidential weight. The **real (fireable) energy ledger** is the *independent* drive-work `W_drive = κ∮S_eq·v dt`, which must equal `W_diss` in the driven steady cycle (energy balance: `κ∮SṠ = ∮S̈Ṡ = 0` over a period). It closes to **≤ 2 %** for `γ>0` (table) — this is the actual H-ledger the shipped `γ=0` pin lacked, and it is what the world-(c) exclusion rests on.
  - **R-5 / F10 — `∮S dr` at `γ=0` is EXISTENCE-grade, not value-grade.** The `γ=0` case has **no steady state** (the undamped `ω_S=1` transient beats against `ω_d=0.9`), so the loop area is **finite at every settle window but not converged**: across `n_settle ∈ {40, 80, 160, 320}` it runs `0.18, 0.46, 1.44, 1.28` — an ~8× spread. **Re-banked everywhere as "finite, window-dependent, O(0.2–1.4), with `W_diss ≡ 0` at every window"** — the previously-banked value `∮S dr = 0.183` was one (`n_settle=40`) representative window, not a physical constant.

  > **🔴 RE-BANKED (Rule-12; superseded text preserved verbatim).** The original §5 table banked *"| **0.0** | **0.183 (FINITE)** | **0.0 (EXACTLY ZERO)** |"* and the prose *"a **FINITE reactive loop** `∮S dr = 0.183` with **EXACTLY zero dissipated work**"* — the value-grade `0.183` is a settle-window artifact (R-5) and the "EXACTLY zero" leg is a definitional identity (R-4). The finite-loop *existence* and the world-(c) exclusion survive.

---

## 6. Adjudication per the frozen tree

- **World (c)** (axiom resistor / rate-independent plastic): **EXCLUDED** — corroborated (not new; already banked on main via the `#744` re-bank, §0.2 item 1). Rests on the finite-loop-at-`γ=0` existence + the independent drive-work ledger closure, NOT the definitional `W_diss=0` leg (§5).
- **World (a) vs (b) at the crossing:** the **FROZEN (a-ledger)/(b-ledger) criterion is DEGENERATE** (§4.1, Rule-11) — neither fires; bin (iii). (c-magnitude) fires on the frozen coupling-model shape split (§2). The (c-scope) reading is **POST-HOC characterization** (§4.2–4.3): the ORDERING is scale-robust, the drain MAGNITUDE and the "0D = physical scope" reading are UNDETERMINED (routed to Grant). Grant's lean is **[ASSERTED, not frozen-adjudicated]** at the 0D-cell scope.
- **Consequence for the yield fork:** the fork's original framing ("finite-area memristive loop *vs* zero-area saturating reactance") is not a clean XOR at the crossing — the object is a **finite-area REACTIVE loop** (finite `∮`, `W_diss=0` by construction at `γ=0`) whose ∞-lattice-transduces-vs-0D-recurs CHARACTER depends on the physical bath scope (open) and the coupling scale (UNDETERMINED). The "memristance in Ω / energy dissipated per yield-heal cycle" reading (world c) is dead; the (a)/(b) magnitude is not settled here.

---

## 7. Loss-location adjudication (the three-way contradiction — FLAGGED, not fixed)

Per-cycle loss (the memristive loop-area / dissipated-energy observable) `∝` the S-response Debye/reactive lag `×` `J(ω_d)`. Both factors → 0 as `ω_d→0` (quasi-static reversible; `J(0)=0`, measured `J_norm(0.05ω_C)=0.017` C1 / `0.0` C2) and as `ω_d→∞` (frozen; `J=0` above band edge). The loss **peaks near `ωτ~1`** (the relaxation/response rate), NOT at `f≪1/τ`.

| Site | verbatim (grep-verified at HEAD) | J(ω) verdict |
|---|---|---|
| **Site 1** — `vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:358` | *"At `f ≪ 1/τ_relax`, complete yield and recovery occur within each cycle, producing **maximum hysteresis loss**."* | **WRONG — the world-(c) rate-independent-plastic picture; EXCLUDED.** Under Ax3-lossless z=3 transduction, `J(f≪1/τ)→0` ⇒ loss is **MINIMAL (elastic)** at low f, not maximal. Already fork-open-caveated at `:338–339`. |
| **Site 2** — `backmatter/06_spice_verification_manual.tex:147–148` | *"At any practical SPICE simulation frequency (`f ≪ 7.8×10²⁰ Hz`), the lattice responds purely elastically---the hysteresis loop has **zero enclosed area**."* | **CORRECT in the `f≪1/τ` regime** — `J(0)=0` ⇒ reversible, zero loop. |
| **Site 3** — `#735` Leg B (`research/2026-07-19_yield-fork-discriminators_result.md:19,81`) | (V,I) loop-area **peaks at `ωτ=0.911`, INSIDE `[0.85,0.95]`** | **CORRECT for the loss peak** — the loop-area observable peaks near `ωτ~1` (reproduced here: (V,I) peak `0.937`). |

**Robust conclusion (coupling-model-independent):** loss is **zero at `f≪1/τ`** (Site 2 ✓, Site 1 ✗) and **peaks near `ωτ~1`** (Site 3 ✓). The three-way contradiction resolves as: **Site 1 is the excluded world-(c) branch; Sites 2 and 3 are the two true limits of the same Ax3-lossless reactive/transductive loop.** *(Flagged per flag-don't-fix; no `.tex` edited — the auditor lane owns the manuscript relabel; owed pointer in §11.)*

---

## 8. Memristor phenomenology status + the I_S caveat

- **Memristor phenomenology:** the pinched hysteresis loop is REAL (both first- and second-order produce it, near `ωτ~1`), but it is a **saturable-reactance / parametric-varactor** object with mode-transduction, **not an RC/memristor-with-resistance**. The `M` (Ω) / "energy dissipated per thixotropic yield–heal cycle → heat" reading (`01_vacuum_circuit_analysis.tex:356`) is the **world-(c) branch, EXCLUDED**. The finite loop area is confirmed but does NOT license a resistor (§5).
- **I_S kinetic-term provenance (flag-F R-5) — stays OPEN; scope NOT stretched.** The GLE assumes a bare inertia `m_S ≡ I_S` for `S`. The bath contributes a *reactive added-mass renormalization* (the ω→0 real part of the bath response dresses `m_S` upward), so the *dressed* inertia is bath-supported even if the bare term were small — but the **bare kinetic-term axiom provenance is not derived here** (consistent with flag-F §2.2 R-5: the transverse-shear-wave `c_shear=c√S` argument for `m_S>0` plausibly exists but is not made). Noted, not closed.
- **Ledger convention disclosure (R-6 / F13).** The ring-down `E_S` recovery fractions (§4.2–4.3) use the **bare system energy** `E_S = ½ṗ_S² + ½κ(S−S_eq)²`, EXCLUDING the interaction `−S·Σc_j q_j` and counter-term `½·ct·S²` (the standard Caldeira–Leggett / open-quantum-systems convention for "system energy"). Disclosure: at mid-transit the omitted cross terms reach ~20–27 % of `E_S0`, but the recovery is read at the post-decay `E_S` PEAK, where the bath coordinates `q` return near zero so `−S·Σc_j q_j → 0` (partition ambiguity at the read-instant ≤ ~3 % for C2, ~0 % for C1; the review's finding on this was itself REFUTED on that basis). **Softened bands** (acknowledging the convention): 0D/finite recovery ≈ **70–95 % ± few %**; the split SIGN (0.70 vs 0.00 at scale 0.6) is far outside any partition ambiguity — but see §4.3, the ∞-lattice band is coupling-scale-governed, not `0–10 %`.

---

## 9. Batched task — arccos drag-onset ratio (does 2/π survive?)

Re-derived `v_p,min/c₀` on the corpus-ADJUDICATED arccos map, replacing the cosine-branch `2/π` of `#741` (`research/2026-07-19_deep-space-band-map_derivation.md` §3.3, §5-D4) [DERIVED, `drag_onset_srs` / `drag_onset_chain`]:

| band model | `v_p,min/c₀` | note |
|---|---|---|
| cosine chain (lumped, #741) | **`2/π = 0.6366`** | the value #741 carries (cosine-scoped) |
| **1D-chain arccos** (z=2) | **`1.0000` (EXACTLY)** | `arccos(cos kℓ)=kℓ` ⇒ **perfectly dispersionless**; NO drag onset below `c` |
| **srs 3D acoustic arccos** | **`0.8028`** | per-direction `[0.803, 0.803, 0.805, 0.809, 0.823, 0.882, 0.976]`; min along ⟨100⟩/⟨110⟩ |

**[DERIVED] The cosine-branch `2/π ≈ 0.637` does NOT survive the model switch.** On the substrate-native arccos map the acoustic branch is far more linear: the 1D chain is **exactly dispersionless** (`v_p ≡ c`, no vacuum-Cherenkov threshold below `c` at all), and the 3D srs acoustic branch gives `v_p,min/c₀ = 0.80` — an AVE-distinct, dimensionless, `ℓ_node`-free manifestation, but ≈26 % **higher** than the cosine `2/π`. **Consequence for `#741`:** its D4 discriminator value `2/π` is a cosine-branch artifact; the substrate-native arccos value is `0.80` (srs) / `1.0` (idealized chain). The deep-space NULL is unaffected (deep-space matter is `v~10⁻⁴c ≪` any of these AND bandlimited, `#741` §3.3), but the drag-onset *ratio itself* must be relabeled `0.80`, not `2/π`. **Owed KB-caveat-update pointer (fenced, §11).**

---

## 10. FORM / VALUE + consistency-vs-emergence ledger

| quantity | FORM | VALUE | class |
|---|---|---|---|
| `J(ω)` shape (Ohmic/super-Ohmic, band edge, peak) | **[DERIVED]** | — | **MANIFESTATION** (theorem of arccos band + coupling model) |
| band edge `π√3 ω_C`, `ω_C`, `τ_relax=1/ω_C` | [ENGINE-READ] | calibrated via `ℓ_node≡λ̄_C` | **CALIBRATION / consistency** (NOT headlined as emergent) |
| the two Γ objects (`γ_0`, `πJ(ω_d)`) | **[DERIVED]** | — | manifestation |
| GLE scope-split ORDERING (0D recovery ≥ ∞ recovery) | **[DERIVED]** | scale-robust (R-1 scan, all cells) | manifestation |
| GLE scope-split DRAIN MAGNITUDE (∞-lattice recovery) | [POST-HOC] shape | **[UNDETERMINED]** coupling-scale-governed (§4.3) | — |
| frozen (a-ledger)/(b-ledger) net-per-cycle transfer | **[DERIVED]** | **DEGENERATE** (neither fires; Rule-11, §4.1) | manifestation |
| H-ledger — finite `∮S dr` at `γ=0` (existence) + drive-work closure `W_drive≈W_diss` | **[DERIVED]** | existence-grade (∮ window-dep); closure ≤2 % | manifestation |
| per-cycle transfer *magnitude* `ζ` | [DERIVED] shape | **[UNDETERMINED]** coupling scale | — |
| `v_p,min/c₀ = 0.80` (srs) / `1.0` (chain) | **[DERIVED]** | dimensionless, `ℓ_node`-free | **MANIFESTATION** |

No CODATA / `α` / `Q_TANK` on any verdict path; forward computation only.

> **🔴 RE-BANKED (Rule-12).** The original ledger rows banked *"GLE scope-split (0D recurs / ∞ drains) | [DERIVED] | coupling-scale-robust"* and *"H-ledger (finite loop, `W_diss=0` at `γ=0`) | [DERIVED] | exact"*. Split into the scale-robust ORDERING vs the UNDETERMINED drain-MAGNITUDE (R-1), and the `W_diss=0`-exact leg relabeled definitional-identity + drive-work closure (R-4); the frozen-criterion DEGENERATE row added (R-2).

---

## 11. Flags (flag-don't-fix) + owed follow-ons

**Flags surfaced (routed to Grant / auditor; not fixed here):**
- **FLAG-1 — loss-location three-way contradiction** (§7). Site 1 (vol_4 ch01:358) is the excluded world-(c) picture; Site 2 (backmatter:147) and Site 3 (#735) are the two true limits. **Surfaced with verbatim citations; no `.tex` edited.** Site 1 is already fork-open-caveated (`:338–339`), so this sharpens an open caveat rather than exposing a silent error.
- **FLAG-2 — the (a)/(b) fork is a false XOR.** The fork record (`retention-transition-split.md:61–65`, `2026-07-17` §5) frames it as "finite-area memristive loop *vs* zero-area saturating reactance." This lane derives that the true object is a **finite-area REACTIVE loop** (finite `∮`, `W_diss=0` by construction at `γ=0`) whose transduces-in-∞-lattice-vs-recurs-in-0D-cell CHARACTER depends on the physical bath scope (open) and the coupling scale (UNDETERMINED) — so the XOR is the wrong question, but which branch dominates physically is NOT settled here. **Routed to Grant** (the ruling stays his).
- **FLAG-3 — coupling-model UNDETERMINED.** The crossing shape verdict (Ohmic-b vs super-Ohmic-a) hinges on whether the S→bath coupling is on-site or strain (§2). Deriving it needs the full engine constitutive tensor — not attempted here (fail-closed).
- **FLAG-4 — the physical bath SCOPE is undetermined (F3, routed to Grant).** Whether a node embedded in the ∞-srs-lattice has a few-mode bath (0D, world-(a) reactive-return character) or the lattice continuum (∞, world-(b) transductive character) is not derived — the ring-down detector cannot distinguish them (its window straddles both Poincaré times by construction, §4.2). The "0D cell = the actual scope of a single node's yield crossing" is **ASSERTED**, not argued. **The scope ruling is Grant's.**
- **FLAG-5 — the drain MAGNITUDE inherits the coupling-scale indeterminacy (R-1).** The ∞-lattice ring-down recovery is coupling-scale-governed (77 % at scale 0.2 for C2, §4.3); only the ORDERING (0D ≥ ∞) is scale-robust. The quantitative (c-scope) reading collapses into bin (c-magnitude)'s UNDETERMINED coupling fork.

**Owed follow-ons (FENCED — cleanup/auditor lanes own these trees; NOT executed here):**
1. **`#59` Flag F status update:** "PARTIALLY discharged, advanced past OPEN-XOR — world (c) exclusion corroborated (finite-loop existence + drive-work ledger; NOT new — already on main via `#744`); the frozen (a-ledger)/(b-ledger) criterion is DEGENERATE (§4.1); the (a)/(b) crux is a scope+coupling question, both UNDETERMINED; awaiting Grant ratification." *Auditor lands.*
2. **Loss-location relabel** at `vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:358` (Site 1): the "maximum hysteresis loss at `f≪1/τ`" line is the excluded world-(c) reading; the Ax3-lossless bath gives **minimal (elastic) loss** there. *Auditor lands (the subsection is already Rule-12-caveated).*
3. **`#741` D4 relabel** (`research/2026-07-19_deep-space-band-map_derivation.md` §3.3, §5-D4, §6): the drag-onset ratio is **`0.80` (srs arccos) / `1.0` (chain arccos)**, NOT the cosine-branch `2/π ≈ 0.637`; `srs-band-structure.md` could gain a drag-onset row. *Auditor/cleanup lane; Grant-gated for any KB mint.*
4. **`tau-relax-derivation.md` / `#59` §10 staleness** (already flagged by `#735` §5): note that Eq 2.1's regime of validity is `ωτ≪1` AND requires `γ_0>0` (Ohmic coupling); under super-Ohmic coupling Eq 2.1 is not recoverable at all. *Owed KB follow-on.*

**None of items 1–4 executed here** (Rule-12 / lane fence).

---

*Derived 2026-07-20 by Opus 4.8 (implementer lane) per Grant's J(ω) yield-fork-adjudicator dispatch ("1. fire"). Frozen prereg governed (Rule-11); anti-seduction fence held both directions (world (a) did not win, world (b) did not win, world (c) lost); engine byte-untouched; verify-before-cite at base HEAD `64f1894d`; flag-don't-fix.*

*Re-banked 2026-07-20 (post-review repair, wrapper `wf_d07d804e` — 13 confirmed findings, 2 CRITICAL) per the REPAIR lane. Honest re-banking: R-1 (coupling-scale scan added; "robust"/"0–10 %" retracted, ORDERING-only survives), R-2 (frozen (a-ledger)/(b-ledger) criterion RUN — DEGENERATE, Rule-11; ring-down relabeled POST-HOC), R-3 (cannot-fail detector disclosed; 0D-scope ASSERTED→Grant), R-4 (world-(c) exclusion corroborated-not-new + `W_diss=0` definitional + drive-work ledger added), R-5 (`∮S dr` existence-grade), R-6 (bare-`E_S` ledger convention disclosed). Frozen prereg untouched (Rule-11); superseded text preserved verbatim in the 🔴 banners (Rule-12). Driver + tests extended (`frozen_ab_ledger`, `ringdown_scale_scan`, drive-work closure); 11/11 `engine_sim` green.*
