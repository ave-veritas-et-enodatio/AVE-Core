# FROZEN PREREG ADDENDUM — Compositeness-Defense engine leg (charge-channel exterior-tail)

**Docket:** B2 (COMPOSITENESS-DEFENSE arc). Sibling to the Gate-0 prereg (merged, PR #471).
**Lane:** research / engine driver (bounded). HOLD canonization. NO self-merge — push + report.
**Branch:** `analysis/compositeness-engine-leg` (off `origin/main` @ `ecfb8588`, post PR #471 merge).
**Prereg status:** FROZEN at first commit. Bins + Grant's pre-registered expected reading do not move post-freeze.
**Parent Gate-0:** `research/2026-07-03_compositeness-defense-gate0_result.md` (merged) — composite bin ILL-DEFINED (charge channel), which triggers this HELD engine leg per Gate-0 prereg §7.

**Disciplines:** `substrate-native-check` (driver walk §0; trigger 8 hosting + CP9 heuristic-vs-dynamical + CP10 boundary-not-bulk) · `pre-test-physics-check` (fork-to-computable, decided by Grant's ruling §1) · `verify-before-cite` · `flag-don't-fix` · `consistency-vs-emergence` · `ave-driver-script-honesty` · INVARIANT-N1.

---

## 1. GRANT'S RULING (pre-registered as the EXPECTED reading — recorded per Grant's explicit instruction)

**Grant 2026-07-03 (verbatim, coordinator-relayed):** *"I agree, it's most likely a conflation, but let's get the engine to decide and record both results."*

**The pre-registered expected reading (Grant's conflation hypothesis):** the Gate-0 Leaf A / Leaf B contradiction (result §2.3) is **SECTOR CONFLATION** —
- **Leaf A** (`translation-circuit.md:541`, "~ℓ_node/r Coulomb leak") describes the **MASSLESS MATCHED EM channel** (Γ_EM = 0, gapless ⇒ 1/r far field).
- **Leaf B** (`substrate-perspective-electron.md:109`, "exponentially-suppressed hedgehog" + 1/r² gravitational survivor) describes the **GAPPED ω / winding sector** (whose Yukawa screening clm-wcoul2 measured directly: ξ ≈ 0.548 cells, `claim-quality.md:1624`).
- **Both true, different sectors.** No leaf is wrong; they describe different channels and were cross-read as if they described one.

**BOTH results get recorded regardless of agreement** (Grant's explicit instruction): the RULING with its rationale (this §1) AND the measured engine verdict (result doc). Leaf sector-header corrections are **GATED on the engine outcome** — landed in this arc IF confirmed; divergence flagged loudly IF broken.

**This is a fork-to-computable** (pre-test-physics-check trigger 9): the engine decides, not fiat. The measurement is the exterior EM-channel E(r) of a seeded charge.

---

## 0. SUBSTRATE-NATIVE WALK (driver — before code)

Per `substrate-native-check` trigger 8 (hosting/measurement test).

- **CP1/CP2 — sector.** Measurement target: the exterior EM-transverse (matched, gapless) E-field sourced by a boundary-integer winding. The winding lives in the **gapped-ω Cosserat sector**; the EM E-field lives in the **curl-Maxwell (fdtd) sector**. These are DIFFERENT engines.
- **CP9 — heuristic vs dynamical (DECISIVE).** For a valid measurement, exterior E(r) must be **dynamically evolved by the engine from the winding source**. This requires a coupling code path: winding integer 𝓠 = Link(∂Ω,F) → EM/u channel source → E-field. **Host audit (this session, §2) finds NO such coupling path exists in any engine.** Per CP9 this is a **WALL-engine capability gap** (fixable by implementing the dynamical channel), NOT a physics floor — stated as such.
- **CP10 — boundary-not-bulk.** Had a coupling existed, the readout is the exterior E-field far-field profile (a boundary/radiation observable), NOT a bulk force. (crystal_graft_v4 measures the ω-normal-stress bulk force T^{xx}_ω, which is the WRONG observable for the EM-channel question — it is the gapped-ω force clm-wcoul2 already measured.)

**Walk verdict:** the measurement, as posed, requires a winding→EM-source coupling that no engine implements. The driver's job reduces to (a) the honest validate-on-known (can the chosen EM host even represent a static 1/r Coulomb field?) and (b) booking the block with the precise missing piece named.

---

## 2. HOST AUDIT (verified this session @ `ecfb8588`) — the winding→EM-source coupling does NOT exist

Three candidate hosts audited by reading the code paths (`ave-driver-script-honesty`):

| Host | EM E-field? | Winding? | Winding→E source path? |
|---|---|---|---|
| `crystal_graft_v4` (clm-wcoul2 host) | **NO** — evolves ONLY the ω sector; gapped dispersion (`step():242`, `−ω_gap²·ω` Yukawa mass term); no E, no ε, no Maxwell | YES (∇×ω vorticity carrier) | N/A (no E to source) |
| `fdtd_3d` (curl-Maxwell) | YES (Ex/Ey/Ez, `update_electric_field():322`) | NO | **NO** — E updates ONLY from ∇×H (Ampère); no charge-source term (no ρ, no J in the E-update); only `inject_soft_source` (a hand-placed additive transverse radiator) |
| `unified_engine` (facade) | LABEL only (`u ↔ E/ε₀` DOF, `characteristic_impedance` is an impedance LABEL, `velocity_channels` are ratios) | YES (reads Q_link via `winding_reader`) | **NO** — `winding_reader` READS the integer; `coupled()` couples A1 cage + ω, NOT ω→u(E); no Q_link→u/E path |

**Exhaustive grep (this session):** `git grep winding|Q_link → E/u/electric/coulomb/rho source` across all of `src/ave/**/*.py` returns **EMPTY** for any source path. The winding integer is READ (charge_quantization.compute_Q_link) but sources no EM field anywhere in code.

**This is the honest blocked branch (coordinator item 3, Grant discipline):** there is NO implemented mechanism by which the boundary integer sources the massless EM channel. The charge-readout mechanism is underived in code **exactly as it is in canon** (the `claim-quality.md:1311` open item: "WHY topological strain equals ℓ_node/r rather than α·ℓ_node/r from first principles is an open multi-week analytical item"). **Hand-wiring an ω→E coupling to force a measurement is FORBIDDEN** (the code-convenience-coupling failure mode the lattice-derived discipline exists to prevent).

---

## 3. THE DRIVER (validate-on-known only; NO knot readout, because the coupling is absent)

Per coordinator item 2 (validate-on-known FIRST) + item 3 (honest blocked branch). The driver does the ONE honest measurement available:

**Validate-on-known:** in the chosen EM host (`fdtd_3d`, the only engine with a genuine dynamically-evolved E-field), seed a KNOWN would-be static point charge and test whether the host reproduces the exact 1/r Coulomb field at r ≫ source. Two sub-tests:
1. **Zero-source control:** zero initial E/H, no source, N steps → E stays 0 (curl-only, no charge-source). Confirms there is no spurious field.
2. **Would-be-charge test:** attempt to establish a static monopole E-field (the only available mechanism is `inject_soft_source`, a transverse radiator, or a hand-set initial Ex/Ey/Ez divergence). Evolve N steps. Fit the resulting E(r) exterior profile. Test: is it a static 1/r monopole (Coulomb) or a radiating transverse pulse / decayed-to-zero?

**Expected (pre-registered):** `fdtd_3d` is curl-Maxwell with no charge-source term, so it CANNOT source a static 1/r Coulomb monopole from a charge — a would-be point charge has no representation; any injected field radiates away transversely (Gauss's law / longitudinal-static sector is absent). **Validate-on-known FAILS on the known source ⇒ the host cannot answer the question ⇒ ENGINE-BLOCKED** with that specific finding (coordinator item 2: "No 1/r on the known source → the host can't answer → ENGINE-BLOCKED").

**NO knot readout is run** — per item 3, since no winding→EM coupling exists, seeding a 0₁ and "measuring its E-field" would measure nothing the winding sources (or, worse, would require hand-wiring the very coupling that is forbidden). The block is booked at the validate-on-known stage.

---

## 4. FROZEN BINS

Per Gate-0 prereg §7 (the HELD engine leg's own bins), refined by the host audit:

- **[TAIL-EXACT-COULOMB]** — the seeded-charge exterior E is 1/r to tolerance ⇒ reading (a), F₁≡1, DEFENSE-DERIVED end-to-end. **(Requires the validate-on-known to PASS first — it does not, per §2/§3.)**
- **[TAIL-DEPARTS]** — a resolved ℓ_node-scale departure from 1/r ⇒ reading (b), extract F₁(q²) + bounds table (EXPOSURE-CONFIRMED path). **(Requires validate-on-known PASS + a winding→E coupling — neither holds.)**
- **[GAMMA-EM-NONZERO]** — the matched-channel premise fails in-engine (Γ_EM(q) ≠ 0). **(Not reachable; no EM-channel wall interaction is implemented.)**
- **[ENGINE-BLOCKED]** — the engine has no implemented winding→EM-source coupling (charge-readout mechanism underived in code, matching canon's open item). **THE PRE-REGISTERED EXPECTED BIN** given the host audit. Books with the precise missing piece named: the coupling by which 𝓠 = Link(∂Ω,F) ∈ ℤ sources the massless EM channel's static 1/r field. This becomes the next derivation target.

**On Grant's ruling:** the engine leg is EXPECTED to land ENGINE-BLOCKED, which means **the engine can neither confirm nor break the conflation ruling numerically** — because the EM-channel charge readout is not implemented. This IS the recorded engine result (Grant: "record both"): the ruling stands as the leading hypothesis (§1), and the engine's verdict is "cannot decide — the mechanism the ruling posits (winding sources the massless EM channel) is exactly the unimplemented/underived piece." The ruling is NOT confirmed (no positive 1/r-from-winding measurement) and NOT broken (no contradicting measurement); it is **UNDECIDED-BY-ENGINE, block-localized**. Leaf sector-header corrections are therefore FLAGGED (not landed) per the gating rule.

---

## 5. DELIVERABLES + CORPUS UPDATES

- Prereg addendum (this doc, frozen).
- Driver: `src/scripts/vol_2_particle_physics/compositeness_engine_leg_validate.py` (zero-source control + would-be-charge validate-on-known).
- Result doc: `research/2026-07-03_compositeness-defense_engine-leg_result.md` — records BOTH (Grant's ruling + the measured/blocked verdict), committed-verdict gates, the named missing coupling.
- **Wall-channel corpus updates (dischargeable NOW regardless of the engine block, per Gate-0 §8):** the coverage-matrix compositeness row → "OPEN-GAP NARROWED"; `boundary-observables-m-q-j.md` → q²-conditioned no-hair paragraph (Γ_EM=0 ⇒ EM-transparent-to-hard-probe). These are DEFENSE-DERIVED and independent of the charge-channel block. **Surfaced for the auditor to LAND** (implementer surfaces, auditor lands — lane discipline); NOT the manual entry itself.
- **Leaf sector-header corrections (GATED — FLAGGED not landed):** since the engine is UNDECIDED-BY-ENGINE, the Leaf A/B sector-header corrections (labeling A=EM-channel, B=ω-channel) are FLAGGED with the ruling + the block, NOT landed as confirmed. Divergence would be flagged loudly; here there is no divergence, only non-decision.
