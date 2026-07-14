# F6 tier-1 — two-reservoir ODE ledger DRIVER — FROZEN PRE-REGISTRATION

**Date:** 2026-07-13
**Class:** frozen prereg (freeze-by-push BEFORE any driver code) — the sibling of `research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md` (merged PR #666). This file pins what the charter (§5 step 2) left to the driver prereg: numeric tolerances, the `D[A,B]` implementation details, the input-history battery (physical + decorrelated), the run grid, the k coupling-scan range, the a-priori expectation restated, and the four charter audits as machine gates.
**Binding upstream:** the CHARTER's §1.6 ledger spec, its frozen bins (§4.5), its fool-mode detectors (§4.3), and its a-priori posture (§4.7) are the frozen physics. **This prereg does NOT change any charter formula or bin.** It pins only the driver-level free choices the charter delegated.
**Freeze discipline:** frozen PRE-RUN, by push, before any driver code exists. No dropped criteria post-hoc (Rule 11). Sabotage plants act on the **evolved ledger trajectory**, not on arithmetic.

**Sector header (mandatory, inherited from CHARTER §0 header).** MODE: global bookkeeping **ODE ledger, NOT a field solve** (no `a(t)` evolver; `solve_backreaction` is static-elliptic, `manuscript/ave-kb/common/engine-capability-map.md:155`). REGIME **(★QUARANTINE — Grant-walked input, CHARTER §1.4)**: the top-stage cascade port at/near the cosmic operating point. PHASE-STATE: a held static store (ρ_latent) draining one-way into the T2 bath. SECTOR **(★QUARANTINE — Grant-walked input, CHARTER §1.4)**: the **A-class continuous-drainage** behavior of the LOCAL top port — a static-sector store transferring into a thermal reservoir; **NOT** A1 dilatation-mass, **NOT** a Cosserat-winding claim.

**Register:** AVE substrate + EE (two-reservoir exchange, entropic sink, matched-termination absorption, Ax3-lossless interior). **Not** ΛCDM Λ-as-fundamental, **not** QED zero-point, **not** a friction/dissipation loss.

**Consistency-vs-emergence class = CONSISTENCY (ceiling).** The slaving coupling `k` is a FREE parameter, **not** derived from `{ℓ_node, α, G}` (CHARTER §4.4). A bin (i) PASS certifies CONSERVATION + FORM only — **never** Ax3-legality (cited premise, deferred to tier-2, CHARTER §iii) and **never** EMERGENCE. No magnitude matching anywhere (the 10^122 trap is rejected canon, `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:8,58-62`).

---

## 0 · What this prereg freezes (index)

1. State vector + transfer laws + observable (verbatim from CHARTER §1.6) — §1.
2. Dimensionless reduction + why the verdict is scale-free (the no-magnitude guarantee) — §2.
3. Input-history battery: PHYSICAL + two DECORRELATED constructions (imported, provenance-stamped, NOT evolved) — §3.
4. Numeric tolerances `tol_cons`, `tol_form`, provenance criterion — §4.
5. `D[A,B]` implementation: integration grid, window `[t₀,t₁]`, norm discretization — §5.
6. k coupling-scan range + fiducial — §6.
7. Run grid — §7.
8. A-priori expectation restated + PRE-REGISTERED CHARTER-TENSION FLAG (flag-don't-fix) — §8.
9. Four charter audits as machine gates, each with a trajectory-acting sabotage plant — §9.
10. Frozen adjudication (bins) + freeze statement — §10.

---

## 1 · State, transfer laws, observable (frozen — verbatim from CHARTER §1.6)

**State (two scalars).** `ρ_latent(t)` (source store) and `E_T2(t)` (bath). Nothing else — no `a(t)`, no field, no A1/muon/bias state (those are tier-2, CHARTER §4.2).

**Conservation + transfer.** One-way exchange:

    dρ_latent/dt = −Γ(t),   dE_T2/dt = +Γ(t),   Γ(t) ≥ 0,

so `ρ_latent(t) + E_T2(t) = const` (the `tol_cons` ledger).

**Three transfer laws (the actuator).**

| Law | Formula | Reading |
|---|---|---|
| **ON (chord)** | `Γ_ON(t) = k · n_B(t) · ρ_latent(t)`, `n_B ∝ n_matter` | reading-i (`dQ/dt ∝ n_matter`), ABSENT-INVENTED |
| **ARM-FRONTIER (OFF)** | `Γ_FRONTIER(t) = 3H(t) · ρ_latent(t)` | reading-ii (frontier default) |
| **ARM-Λ (OFF)** | `Γ_Λ(t) = 0` | bare cosmological constant |

**DE-form observable.** `ρ_DE(t) ≡ ρ_latent(t)`. Work with the normalized shape over the window `[t₀,t₁]`:

    ρ̂_DE(t) = ρ_DE(t) / ρ_DE(t₀).

**Form-separation residual** between arms `A`, `B`:

    D[A,B] = ‖ ρ̂_DE^A(t) − ρ̂_DE^B(t) ‖_{L²([t₀,t₁])} / √(t₁ − t₀)

— a dimensionless RMS shape difference over the window. `tol_form` is the threshold on `D`.

**Two named ablation arms (do not conflate).**
- **ARM-Λ** (`Γ_Λ=0`): observable `D[ON, Λ]` — chord-vs-bare-constant.
- **ARM-FRONTIER** (`Γ_FRONTIER=3H·ρ_latent`): observable `D[ON, FRONTIER]` — chord-vs-frontier. This is the **primary discriminator** (CHARTER §4.6).

---

## 2 · Dimensionless reduction + the no-magnitude guarantee (frozen)

The observable is a **normalized shape** ratio, and the ODE `dρ/dt = −Γ` with `Γ ∝ ρ` is linear in `ρ`. Therefore the whole ledger reduces to a scale-free form. Introduce dimensionless time `τ = t/t_ref` with the canonical time anchor `t_ref = 1/H_INFINITY` (imported from `src/ave/core/constants.py::H_INFINITY`). Writing `ρ̂ = ρ/ρ(t₀)` and `Ê_T2 = E_T2/ρ(t₀)`:

    dρ̂/dτ = −ĝ(τ)·ρ̂,   dÊ_T2/dτ = +ĝ(τ)·ρ̂,

with dimensionless drain coefficients (derivation in §3):

- `ĝ_Λ(τ) = 0`
- `ĝ_FRONTIER(τ) = 3 H(τ) t_ref`  (the matter-era anchor gives `= 2/τ`, see §3)
- `ĝ_ON(τ) = κ · n̂_B(τ)`, where **κ ≡ k · n_B(t₀) · t_ref** is the dimensionless slaving coupling and `n̂_B(τ) = n_B(τ)/n_B(t₀)` is the normalized B-occupancy profile.

**No-magnitude guarantee (MAGNITUDE-TUNE audit, §9.3).** Because `dρ̂/dτ` depends only on `ĝ(τ)` (not on the absolute store value), the normalized shape `ρ̂(τ)` — and hence every `D[·,·]` — is **invariant under any rescale of the input `ρ_latent(t₀)`**. The verdict path never reads a magnitude. This scale-invariance is the machine-checkable form of "no magnitude match to ρ_Λ" (stronger than byte-identity; both are asserted in §9.3). `H_INFINITY` is imported to anchor the physical time units of the reported window (`H(t₀) = (2/3)·H_INFINITY`); the D verdict is scale-free and does not depend on its numeric value.

**Input store value.** `RHO_LATENT_INPUT = 1.0` — the input-only ρ_latent in **normalized store-units**, a declared engineering-choice normalization (CHARTER §4.4: ρ_latent is SYMBOLIC-ONLY / input-only at `clm-s4n33u`, solidity 0.45, "don't build deeper"). It is a pure normalization, **not** a physics magnitude, and the verdict is invariant to it (scale-invariance above). No CODATA / ρ_Λ value is imported or targeted.

---

## 3 · Input-history battery (frozen — imported, provenance-stamped, NOT evolved)

A no-`a(t)` ledger cannot solve for the cosmic drivers, so it **imports** `H(τ)` and `n_matter(τ) ∝ n_B(τ)` as fixed time series. Provenance is first-class: these are IMPORTED matter-era analytic profiles, NOT evolved by any engine. Three histories:

### 3.1 PHYSICAL (correlated — the FRW lock; "the degeneracy lives here" per CHARTER §1.6)

Matter era, both drivers functions of one scale-factor parameter:

- `a(τ) = τ^(2/3)`  (matter-era scale factor)
- `H(t) = 2/(3t)` ⇒ `H(τ) = 2/(3 t_ref τ)`, so `ĝ_FRONTIER(τ) = 3 H(τ) t_ref = 2/τ`
- `n_matter(τ) = τ^(−2) ∝ a^(−3)` (normalized to 1 at τ₀), so `n̂_B(τ) = τ^(−2)`

Note the lock: `H ∝ a^(−3/2)` while `n_matter ∝ a^(−3)`, i.e. `n_matter ∝ H²`. The two drivers are locked to `a` but scale with **different powers** of `a` (this is load-bearing for the §8 flag).

### 3.2 DECORR_H_FROZEN (H frozen constant, n_matter falls) — decorrelation construction 1

Breaks the lock: expansion frozen at its τ₀ value, matter still falling.

- `H(τ) = H(τ₀) = 2/(3 t_ref)` ⇒ `ĝ_FRONTIER(τ) = 2` (constant)
- `n̂_B(τ) = τ^(−2)` (falls as physical)

### 3.3 DECORR_N_FROZEN (n_matter frozen, H falls) — decorrelation construction 2

Breaks the lock: matter occupancy frozen, expansion still falling.

- `H(τ) = 2/(3 t_ref τ)` ⇒ `ĝ_FRONTIER(τ) = 2/τ` (falls as physical)
- `n̂_B(τ) = 1` (constant)

**Both decorrelated constructions are MANDATORY arms** (CHARTER §1.6/§4.6: the decorrelated run is the only tier-1 degeneracy-breaker; two constructions are pinned per the driver brief).

### 3.4 Frozen closed-form solutions (integrator validation targets)

The linear ODE integrates in closed form; the driver's integrator is validated against these (RESULT will report max deviation):

| History | `ρ̂_ON(τ)` | `ρ̂_FRONTIER(τ)` | `ρ̂_Λ(τ)` |
|---|---|---|---|
| PHYSICAL | `exp(−κ(1 − 1/τ))` → plateau `exp(−κ)` | `τ^(−2)`  (∝ a^(−3)) | `1` |
| DECORR_H_FROZEN | `exp(−κ(1 − 1/τ))` | `exp(−2(τ−1))` | `1` |
| DECORR_N_FROZEN | `exp(−κ(τ−1))` | `τ^(−2)` | `1` |

These match CHARTER §1.6 and §4.7 signature tables (ON is Λ-like plateau on PHYSICAL/DECORR_H_FROZEN; FRONTIER is matter-tracking `∝a⁻³` on PHYSICAL/DECORR_N_FROZEN).

---

## 4 · Numeric tolerances (frozen)

| Symbol | Value | Meaning / justification (pinned on principle, NOT verdict-tuned) |
|---|---|---|
| `tol_cons` | `1e-8` | Max relative conservation residual `max_τ |ρ̂(τ)+Ê_T2(τ) − 1|` over the run. Comfortably above the RK45 drift floor (`rtol=1e-11`, so drift ≪ 1e-9) and far below any physically-meaningful energy leak. A non-conserving (energy-destroying) transfer trips it. |
| `tol_form` | `1e-2` | Threshold on `D`. Principle: **1% RMS shape agreement ⇒ the two forms are the "same form" (degenerate).** `ρ̂` ranges over ~[0.01, 1] (order-1), so `D ≤ 1e-2` means the shapes agree to 1% RMS across the window. Chosen on the "same-shape-to-1%" principle, pre-committed, **not** back-solved from any D value (no D is computed before this push). |
| provenance criterion | exact-equality + scale-invariance | (a) `ρ_latent(t₀)` used in every run equals the frozen `RHO_LATENT_INPUT` by exact float equality; (b) every `D[·,·]` is invariant to machine precision under an arbitrary rescale of `ρ_latent(t₀)` (the no-magnitude guarantee, §2). No value in the verdict path is adjusted toward ρ_Λ. |

Tier-2 tolerances (`tol_bias`, `tol_A1`, `tol_μ`) are **NOT** pinned here — the three §4.2 sector detectors are DEFERRED to tier-2 (their state does not exist in the two-scalar ledger).

**Sensitivity panel (NON-FROZEN, reported for transparency only).** The RESULT will additionally tabulate every `D` against a ladder of candidate thresholds `{1e-3, 1e-2, 1e-1, 3e-1}` so the reader can see exactly where each history crosses degenerate↔separable. **The FROZEN verdict uses `tol_form = 1e-2` only;** the ladder is a landscape aid, not an adjudication knob (no post-hoc threshold selection — Rule 11).

---

## 5 · `D[A,B]` implementation (frozen)

- **Time variable:** dimensionless `τ = t/t_ref`, `t_ref = 1/H_INFINITY`.
- **Window `[t₀,t₁]`:** `[τ₀,τ₁] = [1, 10]` — one decade of matter-era cosmic time. Scale factor `a ∝ τ^(2/3)` grows by `10^(2/3) ≈ 4.64×` across the window. Physically-motivated dynamic range (chosen for expansion coverage, NOT for any D outcome). In physical units the window is `[t_ref, 10 t_ref]` with `H(t₀) = (2/3) H_INFINITY`.
- **ODE integrator:** `scipy.integrate.solve_ivp`, method `RK45`, `rtol=1e-11`, `atol=1e-13`, `dense_output=True`, integrating the joint 2-vector `[ρ̂, Ê_T2]` (so conservation is a genuine integrator check, not booked by construction).
- **Norm discretization:** evaluate `ρ̂(τ)` on a uniform grid of `N_GRID = 2001` points over `[τ₀,τ₁]` via the dense solution, then

      D[A,B] = √( ∫_{τ₀}^{τ₁} (ρ̂^A − ρ̂^B)² dτ / (τ₁ − τ₀) )

  with the integral by the trapezoidal rule (`numpy.trapezoid`) on the 2001-point grid. Because the window scale `t_ref` cancels in the normalized `ρ̂` and the `/(τ₁−τ₀)` normalization, `D` is dimensionless and scale-free.

---

## 6 · k coupling-scan range (frozen)

`k` (hence `κ`) is a **FREE parameter, not derived from `{ℓ_node, α, G}`** (CHARTER §4.4). The scan is a **robustness map, not a fit** — no `κ` is selected to hit a verdict.

- **Fiducial:** `κ_fid = 2.0` — the value matching the frontier drain's initial slope at τ₀ (`ĝ_ON(τ₀)=κ = ĝ_FRONTIER(τ₀)=2`). This is the **most-generous-to-degeneracy** fiducial (the chord is set to look maximally like frontier at the window start), so a separation seen at `κ_fid` is not an artifact of an adversarial κ choice.
- **Scan:** `κ ∈ {0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0}` (weak → strong drainage), applied to the ON arm only. Reported: `D[ON,FRONTIER]` and `D[ON,Λ]` per history per κ.
- **Degeneracy metric:** `min_κ D[ON,FRONTIER]` per history (the best-case chord-mimics-frontier over the scanned range). If even the best κ separates (`min_κ D[ON,FRONTIER] > tol_form`), the chord is separable on that history.

---

## 7 · Run grid (frozen)

Full battery = {ON, ARM-FRONTIER, ARM-Λ} × {PHYSICAL, DECORR_H_FROZEN, DECORR_N_FROZEN} × κ-scan (κ affects the ON arm only). Reported per (history, κ): `D[ON,FRONTIER]`, `D[ON,Λ]`, conservation residual, bounded-norm status. Plus the four §9 audit gates (honest-law PASS + plant-trips), each on the evolved trajectory.

---

## 8 · A-priori expectation (restated) + PRE-REGISTERED CHARTER-TENSION FLAG

### 8.1 A-priori expectation (restated verbatim-in-substance from CHARTER §4.7, banked per Rule 11)

- On **PHYSICAL** input histories, **bin (iii) FORM-DEGENERATE is the EXPECTED tier-1 outcome** — `D[ON,FRONTIER] ≤ tol_form` (the homogeneous global ledger is the wrong instrument; the chord's real home is the DESI/Euclid **spatial** cross-correlation, `dark-energy-latent-heat-definition.md:159`).
- **Bin (i) is reachable ONLY through the DECORRELATED arm** — the single tier-1 lever that breaks the `H↔n_matter` lock; the chord fires only if the decorrelated run lifts `D[ON,FRONTIER] > tol_form`.
- Bin (iii) on physical is **banked, not rescued**; a bin (i) PASS certifies conservation + FORM only (not Ax3-legality, not emergence).

### 8.2 ★PRE-REGISTERED FLAG (flag-don't-fix) — analytic tension in the charter's degeneracy premise

**Surfaced BEFORE running the driver, so the verdict cannot be accused of post-hoc rationalization.**

The charter's §4.3 SLAVING-DEGENERACY detector, bin (iii), and §4.7 a-priori all assert `D[ON,FRONTIER] ≤ tol_form` **on physical histories** (degenerate). But the charter's OWN §1.6 and §4.7 signature tables state the two forms are **INVERTED and different**: ON is `exp(−κ(1−1/τ))` (Λ-like plateau), FRONTIER is `τ⁻² ∝ a⁻³` (matter-tracking). Different functional forms ⇒ `D[ON,FRONTIER] > 0` on physical, and (for a meaningful window) plausibly `> tol_form`.

**Mechanism of the tension (load-bearing):** on the physical FRW lock, `n_matter ∝ a⁻³` and `H ∝ a^(−3/2)` scale with **different powers of a** (`n_matter ∝ H²`). So no constant `κ` makes `ĝ_ON = κ·a⁻³` proportional to `ĝ_FRONTIER = 2/τ ∝ a^(−3/2)` across the window — the FRW lock does **not** collapse ON onto FRONTIER. The "degeneracy" the charter conceptually intends is an **ATTRIBUTION degeneracy** about the *observable statement* "DE tracks matter" (which the NON-chord FRONTIER carries, §4.7 inversion), **not** a `D[ON,FRONTIER]` shape-coincidence. The frozen operational metric `D[ON,FRONTIER]` may therefore **not** operationalize the intended degeneracy.

**Pre-committed disposition:** the driver implements `D[ON,FRONTIER]` EXACTLY as frozen (§1/§5) and adjudicates on the ACTUAL numbers per the frozen bins (§10). If `D[ON,FRONTIER]_physical > tol_form`, the charter's "physical degeneracy" a-priori is **not borne out** and I SURFACE the conflict (verbatim charter §4.3/§4.7 + empirical D-table) for Grant/auditor adjudication — I do **NOT** reshape the driver, retune `tol_form`, or edit the charter to force degeneracy. This flag is registered as a possible outcome, not a prediction that overrides the frozen bins.

---

## 9 · Four charter audits as machine gates (frozen — each with a trajectory-acting sabotage plant)

Each gate is implemented as a test that PASSES on the honest law and is TRIPPED by a sabotage plant. **Plants act on the evolved ledger trajectory** (a modified transfer/booking law evolved through the same ODE), not on arithmetic.

### 9.1 IMPOSED-LEAK — conservation / destination booking equality (CHARTER §iii, §4.3)
- **Gate:** `max_τ |ρ̂(τ) + Ê_T2(τ) − 1| ≤ tol_cons` (source loss = bath gain).
- **Plant (trajectory):** a leaky booking `dÊ_T2/dτ = +η·ĝ·ρ̂` with `η < 1` (destination gains less than the source loses ⇒ energy vanishes). Evolved through the ODE, the conservation residual grows past `tol_cons` ⇒ **trips → bin (ii) IMPOSED-LEAK.**
- **REACH LIMIT (CHARTER §iii, recorded):** an honestly-booked *conserving* friction term (`dρ̂=−γρ̂`, `dÊ_T2=+γρ̂`) conserves and is **NOT** caught — entropic-vs-dissipative is inexpressible in two scalars and is a **cited premise, deferred to tier-2.**

### 9.2 TRILINEAR-PUMP — bounded-norm audit (CHARTER §v, §4.3)
- **Gate:** the evolved trajectory is bounded and non-runaway: `ρ̂(τ)` is monotone non-increasing (`dρ̂/dτ ≤ 0`, drain-only) AND `max_τ (ρ̂+Ê_T2) ≤ 1 + tol_cons` AND all states finite.
- **Plant (trajectory):** a v4-style indefinite-Hamiltonian pump `dρ̂/dτ = −ĝρ̂ + c·ρ̂·Ê_T2`, `dÊ_T2/dτ = +ĝρ̂ + c·ρ̂·Ê_T2` (a product of two co-growing amplitudes feeding total norm; `d(ρ̂+Ê_T2)/dτ = 2c ρ̂ Ê_T2 > 0`). Evolved, the total norm runs away (exceeds `1+tol_cons` / diverges) ⇒ **trips.** The honest transfer term is a bounded reservoir-exchange rate, never a product of growing amplitudes.

### 9.3 MAGNITUDE-TUNE — input-provenance audit (CHARTER §4.3, §4.4)
- **Gate:** (a) `ρ_latent(t₀)` in every run equals `RHO_LATENT_INPUT` by exact float equality; (b) every `D[·,·]` is invariant to machine precision (`≤ 1e-12`) under an arbitrary rescale of `ρ_latent(t₀)` (the no-magnitude guarantee, §2).
- **Plant (trajectory):** a magnitude-dependent "verdict" that compares the **un-normalized** `ρ_DE(τ₁)` against a fabricated ρ_Λ magnitude target (a 10^122-style tune). Evolved with two different input scales, the plant's score **changes** (it reads magnitude) while the honest scale-invariant `D` does not ⇒ the plant is caught by the invariance assertion ⇒ **trips.** No adjustment toward ρ_Λ is ever in the verdict path.

### 9.4 DIODE-RESURRECTION — mechanism-class audit (CHARTER §iv, §4.3)
- **Gate:** the effective rate reconstructed from the evolved trajectory, `g_eff(τ) = −(dρ̂/dτ)/ρ̂`, must equal the DECLARED smooth law `ĝ(τ)` (continuous, no `V_f` dead-zone, no `sign(rate)` asymmetry) within reconstruction error (relative deviation `≤ 1e-3` off the endpoints). One of the three licensed mechanisms only (CHARTER §vi).
- **Plant (trajectory):** a diode dead-zone law `ĝ = κ·n̂_B` while `ρ̂ > ρ_f`, else `0` (a forward-voltage-style threshold). Evolved, `ρ̂` decays until it hits `ρ_f` then freezes; the reconstructed `g_eff(τ)` **jumps** from `κ·n̂_B` to `0` at the crossing (a discontinuity absent from the declared smooth law) ⇒ **trips.** V_f is FREE / has no substrate scale (dead four ways, CHARTER §iv).

---

## 10 · Frozen adjudication (bins) + freeze statement

**Frozen bins (verbatim-in-substance from CHARTER §4.5):**

- **(i) LEDGER-CONSISTENT.** Conserves (`≤ tol_cons`) + structural gates pass (TRILINEAR-PUMP bounded-norm, DIODE-RESURRECTION mechanism-class) + the chord's DE-form is separable from the frontier default on the **DECORRELATED** run (`D[ON,FRONTIER] > tol_form`). Certifies **conservation + FORM only** — NOT Ax3-entropic legality (cited premise, tier-2), NOT the three §4.2 sector constraints (tier-2), NOT emergence (`κ` free).
- **(ii) LEDGER-VIOLATES-CONSERVATION.** Total drifts beyond `tol_cons` — FAIL (bin IMPOSED-LEAK). Catches only energy-DESTROYING (non-conserving) transfers; an honestly-booked conserving dissipative term is NOT caught (§9.1 reach limit).
- **(iii) FORM-DEGENERATE.** Runs and conserves, but `D[ON,FRONTIER] ≤ tol_form` on physical **and** the decorrelated run does not lift it — the form is degenerate; F6's chord does not resolve at tier-1. **A LEGITIMATE outcome that CLOSES the tier-1 interior branch** (Rule 11 honest closure), with the degeneracy mechanism named precisely as the exact `3H` continuity identity (`dρ/dt=−3Hρ ⇒ ρ_DE∝a⁻³`).

**Freeze statement.**
- Bins + tolerances frozen PRE-RUN, by push, before any driver code (this file).
- No dropped criteria post-hoc. The complete tier-1 adjudication set = three bins + tier-1 fireable set (conservation/destination audit, two ablation arms on physical+decorrelated, input-provenance audit, two structural transfer-law audits). The three §4.2 hard detectors are DEFERRED to tier-2 (not dropped).
- The **ARM-FRONTIER + DECORRELATED** comparison is the primary discriminator (CHARTER §4.6); both ablation arms and all three histories run in the battery.
- No debug-toward-rescue: a bin (ii)/(iii) landing is recorded, mechanism named, branch closed. A sudden bin (i) PASS appearing only after re-shaping the transfer term is a red flag — re-run the §9 detectors before banking.
- Substitution-not-retraction (Rule 12): a later falsification preserves this body and adds a dated 🔴 header; the slot is not silently refilled.

**Deliverable order (freeze-by-push, binding):** this prereg is committed + PUSHED before any driver code. Driver + tests + RESULT land in a subsequent commit on the same branch.

---

## 11 · References (charter + home-leaf anchors)

- `research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md` — the binding charter (§1.6 ledger spec, §4.3 fool-modes, §4.5 bins, §4.7 a-priori). Merged PR #666.
- `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:84-86` (Ax3-legal one-way T2 transfer, `dS>0`, "NOT a friction loss"); `:122,136` (`clm-s4n33u` ρ_latent input-only, solidity 0.45); `:128` (`reading-i` ABSENT-INVENTED); `:143` (reading-ii frontier default); `:159` (forward observable = DESI/Euclid spatial cross-correlation).
- `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:8,58-62` — the 10^122 magnitude path rejected canon.
- `manuscript/ave-kb/common/engine-capability-map.md:155` — `solve_backreaction` static-elliptic, no `a(t)` evolver.
- `src/ave/core/constants.py::H_INFINITY` — canonical Hubble-scale anchor (`t_ref = 1/H_INFINITY`).
