# RESULT — Compositeness-Defense engine leg (charge-channel exterior-tail)

**Status:** RUN-COMPLETE. **VERDICT: ENGINE-BLOCKED** (pre-registered expected bin). **Grant's ruling: UNDECIDED-BY-ENGINE, block-localized** (neither confirmed nor broken — the mechanism the ruling posits is exactly the unimplemented/underived piece).
**Prereg (FROZEN):** [`2026-07-03_compositeness-defense_engine-leg_prereg.md`](2026-07-03_compositeness-defense_engine-leg_prereg.md) @ this branch's first commit.
**Docket:** B2. **Parent Gate-0:** `research/2026-07-03_compositeness-defense-gate0_result.md` (merged, PR #471) — composite bin ILL-DEFINED (charge channel) triggered this HELD leg.
**Branch:** `analysis/compositeness-engine-leg` (off `origin/main` @ `ecfb8588`). NO self-merge.
**Driver:** [`src/scripts/vol_2_subatomic/compositeness_engine_leg_validate.py`](../src/scripts/vol_2_subatomic/compositeness_engine_leg_validate.py).
**Results JSON:** `src/scripts/vol_2_subatomic/compositeness_engine_leg_validate_results.json`.
**Classification (`consistency-vs-emergence`):** ENGINE-CAPABILITY finding (WALL-engine per substrate-native-check CP9), NOT a physics verdict. NO chord/emergence/DEFENSE claim minted for the charge channel.

---

## 0. BOTH RESULTS, RECORDED (per Grant's explicit instruction "record both")

### Result 1 — Grant's ruling (the pre-registered leading hypothesis)

**Grant 2026-07-03 (verbatim, coordinator-relayed):** *"I agree, it's most likely a conflation, but let's get the engine to decide and record both results."*

**The ruling:** the Gate-0 Leaf A / Leaf B contradiction is **SECTOR CONFLATION** — Leaf A (`translation-circuit.md:541`, ~ℓ_node/r Coulomb leak) describes the **massless matched EM channel** (Γ_EM=0, gapless ⇒ 1/r); Leaf B (`substrate-perspective-electron.md:109`, exponentially-suppressed hedgehog + 1/r² gravitational survivor) describes the **gapped ω/winding sector** (Yukawa, ξ≈0.548 cells, clm-wcoul2). Both true, different sectors.

### Result 2 — the measured engine verdict

**ENGINE-BLOCKED.** The engine can neither confirm nor break Result 1: the mechanism the ruling posits — the winding sourcing the massless EM channel's 1/r Coulomb field — is **exactly the coupling that no engine implements and that canon leaves underived** (`claim-quality.md:1311`). The engine's honest verdict on the ruling is **UNDECIDED-BY-ENGINE**, block-localized to the missing coupling.

**Why both are recorded and not reconciled to one:** per Grant's instruction and `flag-don't-fix`. The ruling is the leading physical hypothesis (and is plausible — the two sectors DO have the right properties: EM gapless→1/r, ω gapped→Yukawa). The engine simply cannot adjudicate it because the adjudicating mechanism is unbuilt. The ruling is NOT elevated to "confirmed" on the strength of the engine (no positive 1/r-from-winding measurement exists), and NOT demoted to "broken" (no contradicting measurement exists). Recorded as: **ruling = leading hypothesis; engine = cannot-decide, and here is precisely why.**

---

## 1. THE HOST AUDIT (the block, localized by reading the code) — verified @ `ecfb8588`

The measurement requires a coupling path: winding integer 𝓠 = Link(∂Ω,F) ∈ ℤ → EM/u channel source → dynamically-evolved exterior E(r). Three candidate hosts audited (`ave-driver-script-honesty`, read the code paths):

| Host | EM E-field? | Winding? | Winding→E source path? |
|---|---|---|---|
| `crystal_graft_v4` (clm-wcoul2 host) | **NO** — evolves ONLY ω; gapped dispersion (`step():242`, `−ω_gap²·ω` Yukawa mass); no E, no ε, no Maxwell | YES (∇×ω vorticity carrier) | N/A (no E to source) |
| `fdtd_3d` (curl-Maxwell) | YES (Ex/Ey/Ez, `update_electric_field():322`) | NO | **NO** — E updates ONLY from ∇×H (Ampère); no charge-source term (0 grep hits for rho/J/charge/gauss in the E-update); only `inject_soft_source` (hand-placed transverse radiator) |
| `unified_engine` (facade) | LABEL only (`u ↔ E/ε₀` DOF; `characteristic_impedance` is an impedance LABEL; `velocity_channels` are ratios) | YES (reads Q_link via `winding_reader`) | **NO** — `winding_reader` READS the integer; `coupled()` couples A1 cage + ω, NOT ω→u(E); no Q_link→u/E path |

**Exhaustive grep (this session):** `winding|Q_link → E/u/electric/coulomb/rho source` across all `src/ave/**/*.py` returns **EMPTY**. The winding integer is READ (`charge_quantization.compute_Q_link`); it sources no EM field anywhere in code.

**This IS the finding (coordinator item 3, the honest blocked branch):** there is NO implemented mechanism by which the boundary integer sources the massless EM channel — the charge-readout mechanism is underived in code **exactly as it is in canon**. Hand-wiring an ω→E coupling to force a measurement is FORBIDDEN (the code-convenience-coupling failure mode the lattice-derived discipline exists to prevent). The block was NOT worked around.

---

## 2. THE VALIDATE-ON-KNOWN (booked empirically, not by code-read alone) — DRIVER RAN

The one honest measurement available: can the chosen EM host (`fdtd_3d`, the only engine with a genuine dynamically-evolved E-field) reproduce a KNOWN static 1/r Coulomb field from a point charge, before any knot readout counts? Driver `compositeness_engine_leg_validate.py`, N=48, dx=1e-3, linear-only, no PML:

### Sub-test 1 — zero-source control

Zero initial E/H, no source, 200 steps → `max|E| = 0.0` exactly (`stays_zero = True`). The curl-only host has no spurious source; a field appears only if put there. Clean floor.

### Sub-test 2 — would-be static point charge

Planted a perfect Coulomb field as the initial condition (E = q/(4πε₀)·r̂/r², unit q). Measured the planted exterior radial exponent: **p = −2.000** (a perfect 1/r² Coulomb field — the field-exponent; the potential is 1/r). Then evolved 400 steps under the curl-Maxwell update and re-measured:

| Quantity | Planted (t=0) | After 400 steps | Reading |
|---|---|---|---|
| exterior field exponent p (E∼rᵖ) | −2.000 | **−1.957** | drifted OFF the Coulomb −2 |
| mean interior fractional change | — | **14.4%** | the "static" field did not stay static |
| total field energy | 5.76e12 | **5.18e12** (−10%) | the planted field radiated/leaked away — no charge holds it |

**The decisive empirical signature:** a real charge's field is a fixed point (it persists, p stays −2, energy conserved by the charge sourcing it). Here the planted monopole is **NOT a fixed point of the curl-only update** — it drifts (p: −2.000 → −1.957), the interior changes 14.4%, and energy decays 10% as the longitudinal-static field radiates/relaxes with no charge-source to maintain it. **`charge_source_term_present = False`** (verified: 0 grep hits). Gauss's law div E = ρ/ε is not enforced; the static/longitudinal electrostatic sector — the sector the boundary integer would source — is **absent from the EM host.**

### Validate-on-known verdict: **FAIL**

`fdtd_3d` cannot SOURCE a static 1/r Coulomb field from a charge (no charge-source term) and cannot MAINTAIN a planted one (not a fixed point of the curl-only update). Per coordinator item 2 ("No 1/r on the known source → the host can't answer the question → ENGINE-BLOCKED"), the host cannot answer the exterior-tail question. **No knot readout is run** (prereg §3): with no winding→E coupling and no maintained-Coulomb capability, seeding a 0₁ would measure nothing the winding sources.

---

## 3. THE BIN + THE NAMED MISSING PIECE

**BIN: ENGINE-BLOCKED** (pre-registered expected bin, prereg §4).

**The precise missing piece (the next derivation target):** the coupling by which the boundary integer 𝓠 = Link(∂Ω, F) ∈ ℤ **sources the massless EM channel's static 1/r Coulomb field**. This is missing in BOTH code and canon:
- **In code:** no engine has a winding→EM-source path; the EM host (`fdtd_3d`) is a curl-only radiation solver with no charge-source / no electrostatic-longitudinal sector.
- **In canon:** `claim-quality.md:1311` (verbatim): *"WHY topological strain equals ℓ_node/r rather than α·ℓ_node/r from first principles is an open multi-week analytical item"* — the exterior charge-field shape is a flagged open derivation item.

The code-block and the canon-gap are the SAME gap, which is itself the honest finding: **the engine is blocked at exactly the point canon is open.** This is not a tooling failure to route around — it is the empirical confirmation that the charge-channel exterior-field derivation (the F₁ premise) does not exist yet, at either grade.

---

## 4. GRANT'S RULING — CONFIRMED, BROKEN, OR UNDECIDED?

**UNDECIDED-BY-ENGINE, block-localized.** Reported honestly per the reporting spec:

- **Not confirmed:** confirming the conflation ruling numerically would require a positive measurement of a 1/r Coulomb field sourced by the winding in the EM channel (proving Leaf A's "EM channel → 1/r" for the actual winding). No such measurement exists — the coupling is unimplemented.
- **Not broken:** breaking it would require a contradicting measurement (e.g. the winding sources an EM-channel field that is NOT 1/r, or the ω-sector is NOT Yukawa). The ω-sector Yukawa (Leaf B's gapped sector) IS separately confirmed (clm-wcoul2 measured ξ≈0.548 cells directly), which is CONSISTENT with the ruling's Leaf-B assignment — but that is prior work, not this leg, and it does not close the Leaf-A (EM-channel) half.
- **Net:** the ruling stands as the **leading, plausible hypothesis** (the sector properties line up: EM gapless→1/r, ω gapped→Yukawa, and the ω half is independently confirmed). The engine **cannot adjudicate the EM-channel half** because that coupling is the unbuilt/underived piece. The conflation ruling is therefore neither vindicated nor falsified by this leg; it is handed forward with the named derivation target (§3) as the thing that would close it.

**Leaf sector-header corrections: FLAGGED, NOT LANDED** (gating rule, prereg §5). Since the engine is UNDECIDED, the Leaf A/B sector-header corrections (A=EM-channel-1/r, B=ω-channel-Yukawa) are FLAGGED with the ruling + the block for Grant/auditor, NOT landed as confirmed. There is no divergence to flag loudly (the ω half is consistent); there is only non-decision on the EM half.

---

## 5. WHAT UPDATES THE CORPUS (surfaced for the auditor; implementer does NOT land manual entries)

- **Wall-channel updates (DEFENSE-DERIVED, dischargeable NOW, independent of this block — from Gate-0 §8):** landed in this arc as data-file/coverage updates surfaced for the auditor:
  1. Coverage-matrix compositeness row → **"OPEN-GAP NARROWED"** (wall DEFENSE-DERIVED Γ_EM=0; moment CONSISTENCY; charge F₁ ENGINE-BLOCKED at the unbuilt winding→EM coupling).
  2. `boundary-observables-m-q-j.md` → a q²-conditioned no-hair paragraph (the Γ=−1 wall is EM-transparent, Γ_EM=0, so a hard EM probe does not reflect off the body — the naive 7-OOM tension is dissolved at the impedance level).
- **Charge-channel:** NO corpus closure (ENGINE-BLOCKED). The named missing coupling (§3) is surfaced as the next derivation target — a HOW-does-the-boundary-integer-source-the-massless-channel item, which is the same as the `claim-quality.md:1311` open item.
- **Leaf A/B sector-headers:** FLAGGED (not landed), per §4.

Claim minting: NO new charge-channel claim (ENGINE-BLOCKED). The wall-channel DEFENSE (Γ_EM=0 ⇒ EM-transparent-to-hard-probe) remains mint-eligible as CONSISTENCY-class — 6-char id + solidity proposed for the auditor to adjudicate, NOT minted unilaterally.

---

## 6. DISCIPLINE LEDGER

- **`substrate-native-check` (trigger 8 hosting + CP9 + CP10):** CP9 (heuristic-vs-dynamical) was the load-bearing check — the exterior E(r) is NOT dynamically evolved from a winding source in any engine; this is a **WALL-engine capability gap** (fixable by implementing the channel), explicitly NOT a physics floor. Stated as such. CP10 noted: the correct readout (had a coupling existed) is the exterior far-field (boundary), not the ω-bulk-force crystal_graft_v4 measures.
- **`verify-before-cite`:** host code paths + `claim-quality.md:1311` + clm-wcoul2 ξ≈0.548 re-verified @ `ecfb8588`. PR #471 merge state verified (MERGED 2026-07-03T10:53:27Z) before branching.
- **`flag-don't-fix`:** the block is surfaced with the exact missing coupling named + the code/canon gap identified as the SAME gap; NOT worked around, NOT hand-wired.
- **`ave-driver-script-honesty`:** the driver makes NO physics claim beyond the host-capability fact (curl-Maxwell has no charge-source ⇒ no static 1/r Coulomb from a charge), verified by running (control stays_zero=0.0; planted p=−2.000 drifts to −1.957 with 10% energy loss).
- **`consistency-vs-emergence`:** ENGINE-CAPABILITY finding, not a physics verdict. No emergence/chord/DEFENSE claim minted for the charge channel.
- **INVARIANT-N1:** no new substrate noun introduced.
- **Lattice-derived discipline (Grant memory):** the forbidden hand-wired coupling was NOT introduced; the block was booked honestly.
