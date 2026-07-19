# F6 mode-count door — Arm B (G0 exterior leave) — prereg FROZEN

**Date:** 2026-07-16  
**Charters:** [`2026-07-15_f6-mode-count-door_CHARTER.md`](2026-07-15_f6-mode-count-door_CHARTER.md) §4/§6; [`2026-07-16_f6-frontier-map_CHARTER.md`](2026-07-16_f6-frontier-map_CHARTER.md) §6 (Tier-0 **G0**; Grant GO 2026-07-16).  
**Prior kills:** rung-2 global V scale-down = **BIAS-MOVED**; Arm A event-gated occupancy = **BIAS-MOVED** (mode-count LIVE).  
**Class:** prereg — **freeze-by-push BEFORE any driver exists** (ave-prereg Step 3.11).  
**Arm status:** **HYPOTHESIS under the discriminator** — not “the plan,” not Re(Z) absorb, not orthogonal cosmology.

> ★ **FROZEN.** §1–§4 locked before RESULT. Do not retune after fire (Rule 11).

---

## §0 Arm identity (hypothesis)

**Name:** Arm B — face-port exterior leave → exterior multi-mode ledger (geometry fork **G0**).

**Intended mechanism (substrate-native language):**
1. **Ports:** on the discrete **box-face** sites of an active `K4Lattice3D` (`pml_thickness=0`), extract a packet of field energy each step when ports are ON.
2. **Exterior credit:** deposit that energy into an **exterior** mode accumulator `b[m]` (M slots), spreading each packet across `N_SPREAD` lowest-occupied slots so exterior occupied-mode-count can rise.
3. **Protected core:** spherical finished-A1 mask — bias≠release / electron-no-drain knives apply; ports do **not** extract from the core.
4. **OFF:** ports disabled — same stepper, closed box (no exterior leave). Periodic wrap at `pml=0` is recirculation, not an exterior ledger.

**Geometry fork:** **G0** — face ports are implementation convenience, **not** a claim of normal-to-frontier (G1) cosmology. No normal-weighted leave in pass criteria. G3 parked.

**Explicitly not this arm:** matched-termination Re(Z) absorb, matched stub, interior dump-R, STZ/plastic loss, PML sponge as T2, interior event-gated V scale-down (Arm A class), electron `radiation_leak` Q-leak, ℏ/FD design constraints, F6=frontier unification, DE lifecycle / `ρ_Λ` claims.

**How mode-count is supposed to enlarge without friction:** irreversibility claim = energy leaves the reactive interior into a **growing set of occupied exterior modes**, not a single scalar damper. FRICTION-RENAMED fires if exterior energy rises **without** exterior occupied-mode-count increase. Pairing amendment: exterior energy↑ alone is generic-consistent and does **not** count toward CHANNEL-BOUNDED.

---

## §1 Hypothesis

Under Arm B ON vs OFF, the frozen `classify()` returns **CHANNEL-BOUNDED** *or* a fail-closed kill (BIAS-MOVED / ELECTRON-DRAIN / DETONATE / FRICTION-RENAMED / NULL / SPONGE-COSTUME). Analytic expectation is **fork-record-both**: face leave may pass the exterior mode-count knife while still failing bias≠release (Arm A lineage), or may CHANNEL-BOUNDED if surface leave separates from core scatter. **No claim that CHANNEL-BOUNDED is expected.** Even CHANNEL-BOUNDED does **not** claim DE lifecycle, crystallization, F6 occupancy chord, or orthogonal geometry.

**Sector declaration (map charter):**  
- MODE: T2 / transverse exterior mode-count (entropic sink bookkeeping), not A1 mass cage.  
- REGIME: boundary leave at face ports; interior reactive Ax3 when OFF.  
- PHASE-STATE: toy box with exterior ledger — **not** cosmic horizon crystallization; **not** BH pre-geodesic.

---

## §2 Bins (mode-count charter §4 + map SPONGE-COSTUME; locked)

| Bin | Fire when |
|---|---|
| **CHANNEL-BOUNDED** | ON: exterior `E_bath`↑, exterior occupied modes ↑ (`ΔN_occ ≥ 1`), soft energy ledger within tol, finite, core bias & drain within tol; and (if PML control run) PML-without-ports does **not** score as pass |
| **DETONATE** | NaN/Inf/runaway / soft-ledger blow |
| **BIAS-MOVED** | `\|mean_S_core ON − OFF\| > BIAS_TOL` |
| **ELECTRON-DRAIN** | protected-core energy drop ON vs OFF > `DRAIN_TOL` |
| **NULL** | `E_bath < NULL_FLOOR` under ON (ports never effective) |
| **FRICTION-RENAMED** | `E_bath ≥ NULL_FLOOR` (or field drop) **but** `ΔN_occ < 1` — energy moved without exterior mode-count increase |
| **SPONGE-COSTUME** | Control: `pml_thickness>0` with ports OFF scores as if CHANNEL-BOUNDED (energy “leave” into sponge without exterior `b[m]`) — **fail closed** if that control is misread as pass; driver must report the control as non-pass |

Decision: fail-closed on DETONATE / BIAS-MOVED / ELECTRON-DRAIN / FRICTION-RENAMED / SPONGE-COSTUME. Only CHANNEL-BOUNDED ungates thermometer discussion. NULL = build incomplete.

**Entailed-branch note (ave-prereg 3.10):** FRICTION-RENAMED is **not** entailed-never: a sabotage plant that credits a scalar exterior bath without filling `b[m]` must be able to fire it. Production Arm B always spreads into `b[m]`. SPONGE-COSTUME control is a separate ON/OFF of PML without ports — must not be classified CHANNEL-BOUNDED by the production bins (no exterior modes).

---

## §3 Method

1. Platform: native `K4Lattice3D` (`nonlinear=True`, `op3_bond_reflection=True`, `V_SNAP=1.0`, **`pml_thickness=0`**).
2. Seed: mild protected-core clock blob + unprotected traveling bath (same spirit as Arm A / rung-2).
3. Masks: spherical core radius `CORE_R`; **face** = active sites with any index on `{0, N-1}` (depth-1 shell); ports extract only on `face & ~core`.
4. Each step: `lat.step()`; then if `ports_on` (kappa>0): extract packet on face sites; credit exterior modes.
5. Packet: prefer scaling outgoing `V_ref` (and `V_inc` as needed) on face sites so extracted δ matches soft ledger; `δ_site = min(PACKET * dens_site, dens_site * 0.5)`.
6. Mode credit: add δ spread across `N_SPREAD` lowest `b[m]`; `N_occ = count(b[m] > MODE_FLOOR)`.
7. OFF: `kappa=0` — no extract.
8. Sabotage: `--sabotage-friction` → scalar exterior energy, no `b[m]` fill.
9. Optional control (report-only): `pml_thickness>0`, ports OFF — must **not** CHANNEL-BOUNDED (no exterior modes); documents SPONGE-COSTUME detector liveness.
10. `classify(on, off)` frozen in driver before RESULT.

---

## §4 Tolerances / knobs (frozen — do not retune)

```
TOL_SOFT_LEDGER_FRAC = 0.5
DETONATE_FLOOR = 1e6
BIAS_TOL = 5e-3
DRAIN_TOL = 0.05
NULL_FLOOR = 1e-12
MODE_FLOOR = 1e-15
PACKET = 0.08
N_SPREAD = 4
M_MODES = 64
KAPPA = 1.0          # master ON switch (0 = OFF)
N_STEPS = 150
N = 12
CORE_R = 2.5
SEED = 1
```

**Analytic expectations (numbers):**
- OFF: `E_bath=0`, `ΔN_occ=0`, finite.
- ON: if face dens > 0 and ports fire, `E_bath > NULL_FLOOR` and `ΔN_occ ≥ 1` *by construction of mode credit* unless deposit path is broken.
- Bias/drain: unknown a priori; Arm A failed bias at these core tolerances — Arm B may too.
- CHANNEL-BOUNDED requires all of: exterior bath↑, ΔN_occ≥1, soft ledger, bias OK, drain OK, finite.
- Does **not** claim DE / crystallization / F6 / G1 even on CHANNEL-BOUNDED.

---

## §5 Result

**Fired 2026-07-16** (prereg commit `5bda8777` pushed before driver; classify frozen).

```
VERDICT = BIAS-MOVED
  ON  bath≈5.78  field≈1.79  core≈0.200  N_occ=64  events≈27300
  OFF bath=0     field≈7.68  core≈0.313
  soft_ledger |ΔE_field − bath| ≈ 3.73
  ΔS_core ≈ −0.017  (|ΔS| ≫ BIAS_TOL=5e-3)
  ΔN_occ = 64  (exterior mode-count detector LIVE — not FRICTION-RENAMED)
  geometry = G0
```

**Sabotage (Discriminator 7):** `--sabotage-friction` (scalar exterior bath, no `b[m]` credit) → **FRICTION-RENAMED** as required.

**Sponge control:** `--sponge-control` → `SPONGE-CONTROL-OK (NULL)` — PML without exterior ports does **not** CHANNEL-BOUNDED.

**Honest closure (Rule 11):** Arm B G0 face-port exterior leave enlarges exterior occupied mode-count and books exterior energy, but **fails bias≠release** at the protected-core knife (same kill-shape class as rung-2 / Arm A). Soft ledger also messy. Do **not** retune `PACKET` / `CORE_R` / face mask. This hypothesis arm is **not** CHANNEL-BOUNDED.

**WRONG-OBJECT / CATEGORY-WRONG (2026-07-16 circuit-first repair):** the tested object was an **unsaturated face \(V\)-scale siphon** into exterior `b[m]`, not native K4 port refusal at full yield (\(|\Gamma|\to 1\) mirror; storage→boundary). Bin fire preserved; siphon class closed; does **not** constrain saturated-port wall physics. See [`2026-07-16_f6-circuit-first-door-map_CHARTER.md`](2026-07-16_f6-circuit-first-door-map_CHARTER.md).

**What this does not claim:** DE lifecycle, crystallization, F6 occupancy chord, orthogonal (G1) geometry, `ρ_Λ`, native wall-port behavior.

Thermometer re-fire remains **GATED**. Full `node_creation` mint remains **NO** per frontier map. No Arm C siphon.

---

# Post-freeze amendments (append-only)

> **Freeze rule.** §0–§5 above are the **frozen body** and are byte-untouched. Post-fire adversarial-review corrections are recorded here as dated amendments only (Rule-12 preserve-under-supersession). The banked **BIAS-MOVED** verdict and its `ΔS_core = −0.017146` basis are **unchanged**; these amendments repair *labels and demonstrations*, not the classifier or any bin.

## Amendment A1 — 2026-07-16 — mode-count "LIVE" demoted (twin-64)

Adversarial review confirmed the §5 line "`ΔN_occ = 64` (exterior mode-count detector LIVE — not FRICTION-RENAMED)" over-reads a structural constant as a measurement. **This amendment supersedes that line.**

- **Elevated as the disclosed tell:** §4's own analytic expectation — "`ΔN_occ ≥ 1` *by construction of mode credit* unless deposit path is broken" — is the correct reading. `ΔN_occ ≡ M_MODES` because `_credit_modes` round-robins into the `N_SPREAD` lowest slots of a pre-allocated `M_MODES` array that saturates in ~16 events (27 300 fire). Live-fire: `M_MODES ∈ {16,48,64,128,256} → ΔN_occ = {16,48,64,128,256}`, `E_bath = 5.776694` invariant; `b[m]` is write-only (zero back-reaction).
- **Corrected label (everywhere banked):** "deposit-path intact (`ΔN_occ ≥ 1`; magnitude = the `M_MODES` knob) — a code-flag self-test, **not** a physical mode-count measurement."
- **Twin-64:** Arm A's interior 64 and Arm B's exterior 64 = the same `M_MODES=64` constant printed twice (not two geometries converging).
- **FRICTION-RENAMED** is reachable only by the deliberate `--sabotage-friction` plant (`credit_modes=False`); it is **unreachable by production physics** (any positive δ with the flag on fills the slots). It discriminates the bookkeeping code-path, not a physical irreversibility magnitude.
- **MANDATORY GATE:** no `CHANNEL-BOUNDED` bank or thermometer ungate until the mode-count observable is rebuilt with real bath DOF + back-reaction + a physical control that can fail on physical inputs. The `#711` (Arm A) repair registers the same gate — cross-cite.

## Amendment A2 — 2026-07-16 — E0 baseline bug: "soft ledger messy" was an artifact

Adversarial review confirmed the §5 result lines "soft_ledger ≈ 3.73" and §5 closure "Soft ledger also messy" over-read a **t=0 baseline bug**. **This amendment supersedes those lines.**

- **Bug:** the frozen driver measured `E0 = lat.total_energy()` on the raw **V_inc-only seed** (`3.839`), which is not a valid `V_inc/V_ref` equilibrium. The first `lat.step()` equilibrates and the OFF energy **doubles EXACTLY 2.000000×** (`3.839 → 7.678`, then conserves to machine precision). So `soft = |(E0 − E_f) − E_bath| ≈ E0` identically (measured `0.971·E0`), and the soft sub-gate — a **mandatory** sub-condition of `CHANNEL-BOUNDED` (§2/§4) — was **structurally unreachable**. The §1 hypothesis space ("CHANNEL-BOUNDED *or* a fail-closed kill") had its pass bin foreclosed before any physics ran.
- **Fix (driver, not a knob retune):** book the ledger against the **equilibrated** baseline `E_equil` (post-step-1, pre-transfer; `RunOut.E_field_equil`). Lattice trajectory byte-identical; all frozen tolerances (§4) untouched.
- **Honest re-bank (two-method verified):** `soft = |(E_equil − E_f) − E_bath| = 0.110790` = **1.443 %** of `E_equil = 7.678`; **PASSES** the frozen `0.5·E_equil` tol. OFF ledger ≈ `5.3e-15`. The exterior ledger **closes**.
- **Verdict unchanged:** BIAS-MOVED is decided at `classify()` step 4 (bias), upstream of the soft-ledger DETONATE branch; the WRONG-OBJECT closure does not rest on soft-ledger reachability.
- Same E0 convention flagged to the **#711** (Arm A) repair — same bug class.

## Amendment A3 — 2026-07-16 — co-fire + statistic-honesty corrections

Adversarial-review MINORs (findings 2, 3, 9, 11). No verdict moves (all fail-closed); these correct labels/omissions in §5.

- **ELECTRON-DRAIN co-fired (finding 2):** the shipped run drains the protected core `rel=(off−on)/off = 0.362 ≫ DRAIN_TOL=0.05` (7.2× over). The frozen `classify()` tests **BIAS-MOVED before ELECTRON-DRAIN**, so only BIAS-MOVED is *returned* — but the drain bin genuinely fires and was absent from the §5 check enumeration. Now recorded (result check-table co-fire row) with the frozen-precedence note. Not a false pass.
- **`mean_S_core` is a CONTRAST, not saturation (finding 3):** `_mean_S` normalizes A² by the in-mask **peak**, so the hottest site always reads contrast `S=0`. It is a profile-**shape** contrast, not the Ax-4 `S(A)` vs `V_SNAP`. Measured true core saturation stays `S≥0.99` (`A²_max≈0.021`) everywhere. **BIAS-MOVED gates a profile-shape change**, not an absolute saturation-bias move. Same `_mean_S` in Arm A/#711 — relabel applies there (cross-cite).
- **Soft-ledger row was mis-characterized (finding 11):** the superseded "fail-adjacent … would DETONATE" was, under the shipped seed-`E0` tol, a **1.94× outright FAIL** whose counterfactual bin was **ELECTRON-DRAIN** (checked before soft DETONATE), and the 2.000000× ports-OFF non-conservation is engine-pump-created energy (echoes engine-pumps-at-dt→0). Corrected in the result E0-fix note. (Moot after Amendment A2, recorded for honesty.)
- **Sponge control relabeled (finding 9):** §3.9's "documents SPONGE-COSTUME detector liveness" over-claims. With κ=0, `E_bath≡0` → `classify()` short-circuits to NULL (verified pml∈{0,2,4,6}) before CHANNEL-BOUNDED is reachable, so SPONGE-COSTUME is entailed-never. It is a **standard negative control** verifying the κ-off branch; genuine mode-liveness rests on the separate FRICTION-RENAMED sabotage plant.

## Amendment A4 — 2026-07-16 — "unsaturated" now MEASURED (port-state probe)

Adversarial-review MINOR (finding 6): the "unsaturated face" regime descriptor was **asserted, not measured** — no port-state observable existed in the driver. Fixed.

- **Probe added (driver):** face-port state observable `port_A2_max`, `port_S_floor`, `port_Gamma_rms_max` (phase-space / impedance-plane, referenced to `V_SNAP`; report-only, not a `classify()` input). Lattice trajectory byte-identical (survivors unchanged).
- **Measured (two-method; review expected unsaturated to CONFIRM — it does):** face `A²_max = 0.0236` (`max|V_inc| = 0.154` vs `V_SNAP = 1.0`), `S_floor = 0.988` — **deep sub-yield / unsaturated everywhere in the run**, never near the wall (`S→0`). No STOP condition. The `Γ_rms ≈ 1.07` is the **closed-box cavity boundary** reflection of the G0 face-convenience geometry at sub-yield, **not** a saturation-driven `|Γ|→1` mirror — `S≈0.99` rules out a saturation wall, which is the WRONG-OBJECT point.
- **Class closure restated on its surviving leg:** independent of the (now-measured) regime label, the closure rests on the **Step-4 entailment** — a fiat `V_ref/V_inc` scale into a **write-only** `b[m]` ledger is a costume in **ANY** regime (reflection ≠ ε→T2 leave). The measured sub-yield port-state is **corroboration**, not the load-bearing argument.

---

## Post-freeze correction-note — 2026-07-18 — Platform line `nonlinear=True` is a no-op (costume; FACT-1-unconditional)

**Append-only, dated; §3 method body byte-untouched (label corrected for the record, not the frozen plant).** Routed from the F6 bath-meter nonlinear-revalidation lane (`2026-07-17_f6-meter-nonlinear-reval_result.md` R-2; charter `2026-07-16_f6-bath-meter_CHARTER.md` §B1 FACT-1 / R-2) and landed here.

- **§3.1's `Platform: … nonlinear=True` is a no-op in `K4Lattice3D` — dead code.** Per PR #721 review **FACT-1-unconditional**, the `nonlinear` flag has **zero dynamical consequence**: the K4 4-port scattering matrix `build_scattering_matrix(z)` (`src/ave/core/k4_tlm.py:64`) reduces to `S[i,j] = 2y/(N·y) − δ = 0.5 − δ` for `N=4` — **z-independent** — so the nonlinear branch reproduces the linear scatter exactly (the reviewer's op3-OFF twin was bit-identical too, `~1e-15`). The flag is a no-op **regardless of `op3_bond_reflection`** (the `pml_thickness=0` co-pin is orthogonal to this note).
- **What the plant actually was: weakly-nonlinear-via-op3 only.** The amplitude-dependent kernel `S(A)=√(1−A²) → z_local=(1−A²)^(−1/4)` flows through **op3's bond Γ** (ON here), not the flag; at the mild seed its amplitude dependence is second-order / negligible (measured face `A²_max = 0.0236`, A4). The plant is **weakly-nonlinear-via-op3**, not a genuinely Op14-saturated lattice.
- **The Arm B verdict is UNAFFECTED.** **BIAS-MOVED** (with the WRONG-OBJECT closure) rests on the protected-core bias step / the Step-4 entailment (reflection ≠ ε→T2 leave, A4), computed on the trajectory itself; the **bias knife did not consume the `nonlinear` flag**, so the no-op does not touch the verdict. Nothing is re-run or retuned.
- **Correction:** the frozen §3 platform label is **costume for `nonlinear=True`** to the same degree the meter lane's was pre-relabel. Recorded for the register; the frozen body is unchanged.
