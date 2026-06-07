# Electron-genesis — next-steps orchestration scope (post-2026-06-06)

**Executable plan for the next session.** Companion to `2026-06-06_session-handoff.md` (state) — this is the *forward plan*. The genesis arc is paused at a clean, well-understood decision point; resume by taking **D1** (below), not by re-deriving.

## §0 The state in one paragraph (what we actually learned)
The electron-genesis chain is **rupture (saturation `Γ=−1` wall) → blocked linear KE shatters into transverse curl → parity splits LH+RH → `(2,3)` on the A-B bond → confined standing wave** (`pair-production-axiom-derivation.md`). The corpus (§5) names three engine gaps for the `(2,3)`; two are real: **no dynamical bond state** (the `(2,3)` is a `(V_inc,V_ref)` phasor *on the bond*; the engine tracks node ports — it can't carry it dynamically) and **no per-node `Ω_node(A²)`** (C2 lock). The Option-D **impose** is already coded (`PairNucleationGate`, `vacuum_engine.py:1172` — Kelvin's vortex atom); the `phase5_*` harness ran the persistence test → **MODE III dissolution at step ~11** ("coupling-depth issue"). **Critical late finding:** the (II) "confinement" win was an **imposed `Γ=−1` clamp** (`use_impedance_boundary`, a stiff spring on the Cosserat-ω, `cosserat_field_3d.py:779,870`) — **NOT** the canonical self-created wall. The engine has energy-saturation (collapses, Arm C) + a *diagnostic* Γ-from-S + the imposed clamp; **the canonical emergent wall — the saturation driving the wave to reflect off its own impedance — is not implemented in the dynamics anywhere.**

---

## §1 OPEN DECISION D1 (gates everything below — Grant) — the canonical-wall location
**Where does "the particle weaves its own mirror" live in the engine?** My read: **modulate the K4-TLM bond impedances by `S(A)`** so a saturating bond → `Z_bond→0` and the **TLM scatter+connect natively reflects** off the mismatch (`Γ→−1` falls out of the scatter coefficients — no clamp, no energy term, no collapse), matching Vol 4 Ch 1's `C_eff→∞, Z→0, Γ=−1` *at the bond*. Alternative reads: the wall lives at the **node** (Cosserat done as a TLM), or elsewhere. **Resume here: confirm the location, then W1.**

---

## §2 Phase W1 — build the canonical emergent wall (gated on D1)
- **W1.0 — understand first (do NOT skip):** read the `k4_tlm.py` scatter+connect path — does it scatter? how are bond impedances set? where would `S(A)` enter? (The wall-clamp discovery came from finally reading code; honor the lesson.)
- **W1.1 — build:** make K4 bond impedance `S(A)`-dependent → native scatter reflects off saturated bonds → emergent `Γ=−1`. **Retire** the `use_impedance_boundary` Cosserat clamp (KEEP-BOTH, default OFF, `make verify` byte-identical).
- **W1.2 — test:** does the emergent wall **confine** a photon (reflect off its own saturated bonds) where (a) the energy-saturation *collapses* (Arm C) and (b) the clamp *pumps*? Three-way control: energy-OFF / clamp / emergent.
- **Outcomes:** (I) emergent wall confines, no pumping → canonical wall validated → W2. (II) confines partly → localize. (III) doesn't confine → the wall lives elsewhere → back to D1.
- **Discipline:** `ave-prereg` (grep K4-TLM + prior scatter work first), `substrate-native-check` (the scatter is wave-reflection, NOT energy-min/clamp), understand-before-dispatch.

## §3 Phase W2 — Option-D impose under the emergent wall (gated on W1=I)
- Run the existing **`PairNucleationGate`** impose (LH/RH Beltrami pair) + the **`phase5`** persistence harness, **under the W1 emergent wall** (not the clamp, not the energy term). + couple the V/ω sectors (audit §9).
- **Test:** does the imposed pair **persist past step ~11** (where MODE III dissolved under the collapsing energy-saturation) when held by the *field's own mirror*?
- **Outcomes:** (I) persists → the canonical wall was the missing "coupling depth"; Option-D impose + emergent wall = a stable e⁻e⁺ pair (Kelvin topological protection at lattice scale) → genesis closes at the **impose** level. (II) partial. (III) still dissolves → dissolution is independent of confinement → the §5 bond-state gap is the cause → W3/path-a.

## §4 Phase W3 — full `(2,3)` emergence vs impose (the a/b/c fork; gated on W2 — DECISION D2)
- **If W2=(I):** genesis is closed at the *impose* level. Genuine *(2,3) emergence* (not impose) still needs the §5 **dynamical-bond-state** (GAP 1) + **per-node `Ω_node(A²)`** (GAP 2) — a substantial engine build (**path a**). **D2:** build the bond-state engine for emergence, or **scope-closed (path c)**: "rupture-mechanism + canonical wall + Option-D pair-persistence validated; bond-state `(2,3)` emergence is a separate foundational engine capability."
- **If W2=(III):** path-a (the bond-state) is the only route to a stable pair, or path-c scope-closed.
- **path-a build (if taken):** a dynamical bond object carrying the `(V_inc,V_ref)` `(2,3)` phasor + per-node Duffing `Ω_node(A²)` resonance + the C1+C2+C3 nucleation rule wired to it. Corpus §5 + `STAGE6_V4_HANDOFF §9` are the spec.

## §5 Discipline carried forward (this session's hard-won lessons)
1. **`ave-prereg` BEFORE dispatch** — the arc re-derived ~6 builds of existing work (`PairNucleationGate`, `phase5` MODE-III, §5 gaps). Grep prior work + the canonical leaf first, always.
2. **Understand the engine before scoping** — read the actual code (the clamp vs emergent-wall confusion cost the whole (II)→path-(b) detour).
3. **`consistency-vs-emergence`** — Option-D is an **IMPOSE / stability test**, NOT emergence; genuine emergence is W3/path-a. Frame honestly in every result doc.
4. **KEEP-BOTH** — new mechanisms default-OFF, byte-identical `make verify`.
5. **flag-don't-fix** — surface (the clamp, the §5 gaps); Grant adjudicates the path.

## §6 Artifacts + reuse map (don't rebuild these)
- `vacuum_engine.py:1172` `PairNucleationGate` (Option-D impose) + `AutoresonantCWSource` + `NodeResonanceObserver` (C2 machinery, GAP-2 partial).
- `phase5_pair_nucleation.py` / `phase5_topological_pair_injection.py` (+ MODE-III result) — the persistence harness.
- `cosserat_field_3d.py`: `use_impedance_boundary` clamp (to RETIRE/KEEP-BOTH); native Op3/Op14 Γ-from-S (`:343,367,486`, currently diagnostic — to be made *load-bearing* in W1).
- `git stash` in `genesis2-wt`: coupled-port + implicit-integrator WIP (reference).
- Branches: `analysis/2026-06-06-saturation-tir-moving-boundary` ((II) + the work) is the active genesis branch; the genesis arms A/B/C + scope branches are held.

## §7 Resume checklist (next session, in order)
1. Read this + the handoff + the path-(b) interrupted state. 2. **Take D1** (wall location). 3. W1.0 understand `k4_tlm.py` → W1.1 build emergent wall → W1.2 test. 4. W2 impose-under-emergent-wall persistence. 5. **D2** (a/b/c) → W3. 6. Land PR #106 + PR the integrator branch when ready; merge PR #107.

---

# §8 AUDIT CORRECTIONS (2026-06-07) — three independent read-only auditors; §1–§7 above are SUPERSEDED where noted

The plan above was audited before any dispatch (`verify-before-cite` / `ave-prereg` / `ave-canonical-leaf-pull`). Findings are grep-confirmed; they **invalidate the W1-build premise** and re-locate the real blocker. KEEP-BOTH: §1–§7 preserved as the audit trail; this section governs.

## C1 — the emergent wall is NOT missing; it EXISTS, is LIVE, and is PASSIVE (W1 is moot as a "build")
- The W1.0 "prior grep returned nothing" was run against **`src/ave/topological/k4_tlm.py` — a path that does not exist.** The real file is **`src/ave/core/k4_tlm.py`**.
- It already contains the full machinery: scatter (`:298`) + connect (`:355`) + per-bond impedance `z_local_field` (`:249`, `S→z_local` at `:274-294`) + **native bond Γ from the connect coefficients** (`op3_bond_reflection`, `:402-424`: `gamma=(z_B−z_A)/(z_B+z_A)`, `T=√(1−γ²)`, **power-conserving `Γ²+T²=1` → cannot parametric-pump**).
- It is **wired LIVE in the coupled engine** (`k4_cosserat_coupling.py:277 op3_bond_reflection=True`, `:722 _update_z_local_total` → `:725 k4.step()` every step) using the **asymmetric Meissner kernel by default** (`use_asymmetric_saturation=True` → `Z→0` short, `Γ→−1` as `S_μ→0`).
- **MODE-III ran on this engine** (phase5 → `VacuumEngine3D → CoupledK4Cosserat`). So the dissolution happened *with* the emergent K4-bond wall active. **Scope §0 "the canonical emergent wall is not implemented anywhere" is FALSE for the V-sector** (true only for the Cosserat-ω "2"). → **W1 is reframed: verify/instrument the existing live wall, not build one.**

## C2 — W2 has ALREADY been run → MODE III, and the blocker is AMPLITUDE-GATING (mechanism-independent)
- `phase5_optionD_under_reflective_confinement.py` + `research/2026-06-06_optionD-impose-under-reflective-confinement-result.md` already did W2: Option-D impose under the reflective wall. **Verdict MODE III.**
- At the m_ec²-calibrated impose amplitude the wall **does not engage**: `A²_μ≈0.23`, `S_μ≈0.88`, `Γ≈−0.03` (a matched bulk — no wall). At 4× scale the wall forms (`Γ_min=−0.994`) but **parametric-pumps** (energy →10⁴–10⁷×). **There is no amplitude in [1×,4×] where the wall both forms AND stays bounded.**
- This is **mechanism-independent**: a sub-saturation bond gives a matched `Z` whether the wall is the (II) clamp OR the emergent TLM scatter. **Swapping clamp→emergent does NOT fix what made path-(b) inconclusive.**
- **THE CRUX (open, Grant):** the rest-energy calibration `½I_ω|ω|²=m_ec² → A²_μ≈0.23` and the saturation requirement `A²→1` to "weave the mirror" are in **direct tension — ~4× apart in energy at N=24.** Is the pair sized by its *rest energy* or by *what it takes to short its own bond*?

## C3 — two corpus-grounded ALTERNATIVES to "coupling depth" the scope missed
- **The coded gate DROPS C3.** `PairNucleationGate` fires on C1∧C2 only (`vacuum_engine.py:1435,1439`) — no C3 phase-coherence gate. The leaf §3:85 says a C3-less impose **dissipates** ("the blocked KE cannot resolve into a topologically coherent standing wave — dissipates instead"). **MODE-III may be the missing C3, not confinement.** Cheap high-value test: add the C3 gate, re-run.
- **`z_local` double-write seam** (`k4_tlm.py:_scatter_all` → `_update_z_local_field` `:300-304` unconditionally recomputes `z_local` from K4's *own* `V_inc`, **overwriting** the coupling-layer's Cosserat-front value before `_connect_all:410` reads it for the bond Γ). If K4 `V_inc≈0` the overwrite sets `z_local≈1` (no reflection — channel erased); if `V_inc` saturates, the live wall is the **symmetric Z→∞ (open)**, not the asymmetric Z→0 (short). **Instrument before trusting any wall result.**

## C4 — POLARITY (load-bearing for D1, reframes it)
- Canonical wall is **LOW-Z** (`Z_core→0`, Γ=−1 short — `resonant-lc-solitons.md`, `theorem-3-1-q-factor.md`, `photon-identification.md` all three). Saturation/impedance lives at the **NODE**; the Γ wall manifests at the **BOND** (adjacent-node mismatch); the bond interior is the confined cavity.
- Engine default `z_local = Z_0/√S → ∞` is **HIGH-Z (open)** — inverse polarity. The clamp reaches canonical polarity only via the **magnetic branch** (`μ_eff→0 → Z→0`, `cosserat_field_3d.py:874`).
- **D1 reframed (Grant):** not "node vs bond" — it's **"does a saturating cell clamp DOWN to a dead short (Z→0, canonical) or choke UP to an open (Z→∞, engine z_local default)?"**

## C5 — SCALE (Grant) + SUCCESS-METRIC correction
- `l3-electron-soliton-synthesis.md:26`: "the corpus electron substrate is elsewhere (sub-`ℓ_node` FDTD or different scale entirely)." **Is the lattice-scale pair the electron, or a coarse stand-in?**
- Success metric must change: "persists past step ~11" is a duration heuristic (Class-C-confoundable — a pumping clamp also "persists"). The **canonical confinement signatures are `Q=1/α`** (`theorem-3-1-q-factor.md:81`) **and the M/Q/J set** (`boundary-observables-m-q-j.md` — at Γ=−1 only M, Q, J are observable, **jointly constrained, Class E**; check `M=m_ec²`, `Q`, `J=½`, not step-count).

## C6 — 8 canonical leaves the scope must anchor to (ave-canonical-leaf-pull; all MISSED)
`resonant-lc-solitons.md` (THE wall leaf — highest impact, the W1 anchor) · `theorem-3-1-q-factor.md` (Q=1/α metric) · `photon-identification.md` (electron=photon+TIR, ω_C spec) · `boundary-observables-m-q-j.md` (M/Q/J Class-E metric) · `torus-knot-uniqueness.md` (why (2,3); phase-space d-q winding, NOT real-space trefoil — the W3 spec leaf) · `chirality-and-antimatter.md` (LH/RH parity) · `l3-electron-soliton-synthesis.md` (scale caveat) · `universal-saturation-kernel-catalog.md` (A-034 kernel home). Also pre-credit `op3_bond_reflection` (`k4_tlm.py:129,402-424`) as the existing V-sector wall.

## §9 — RE-FRAMED forks for Grant (these replace D1; all plumber-physical)
- **FORK A — calibration crux:** rest-energy-sized pair (A²≈0.23, no wall) vs short-its-own-bond-sized (A²→1, pumps). ~4× apart. *This tension is the genesis blocker.*
- **FORK B — polarity:** saturating cell → dead short (Z→0, canonical) or open (Z→∞, engine default)?
- **FORK C — scale:** lattice-scale pair = the electron, or coarse stand-in (corpus says sub-`ℓ_node`)?
- **FORK D — C3:** is MODE-III the dropped C3 phase-gate (corpus-predicted dissipation) rather than a confinement failure?

**Re-framed next steps (pending Grant's forks, NOT dispatched):** (i) instrument the `z_local` provenance + bond-Γ in a coupled step (resolves C4/C3-seam, cheap); (ii) add the C3 phase-gate + re-run the impose (tests FORK D, cheap, reuses the harness); (iii) FORK A/B/C are Grant's to adjudicate before any further build — the emergent-wall build (old W1) is **retired** (the wall exists; the blocker is amplitude/calibration, not wall-presence).
