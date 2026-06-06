# Observable-Battery + Sweep Infrastructure (PREREG, FROZEN)

**Date:** 2026-06-05
**Branch:** `analysis/2026-06-05-observable-battery-infra` (off `analysis/2026-06-05-2-3-winding-extractor`, off `origin/main` `c1d7390f`; worktree `AVE-Core-obs-battery-wt`)
**Status:** PREREG FROZEN — implementor build pending (9-step plan, §6). Session: orchestration (Grant in-session).
**Origin:** Grant directive 2026-06-05 — *"we shouldn't assume any sweep is the sweep; produce everything we can and analyze each simulation; deploy all orchestration skills to map this infrastructure into our existing sims/solvers."* MAP fleet (`wf_631750cd-ab6`) surveyed engines/observers/drivers → this design.

---

## §0 What this is

ONE reusable `ObservableBattery` class in `src/ave/core/` that instruments **every** AVE simulation with the full physical readout, plus a sweep harness that runs the engine over an N-D parameter cube **with no axis pre-judged**. It **composes** the shipped diagnostics (imports + calls; never redefines — KEEP-BOTH); only the genuinely-missing reads are NEW. Every channel carries an honesty tag. This single tool **subsumes** five open threads — the Γ open/short seam, the (2,3) coordinate, the V0 degradation-vs-contamination fork, single-bond-vs-bond-pair, the C↔L reactance state — answering them as a *byproduct* of running instrumented sims.

**Scope-fence:** this is **measurement infrastructure** — it MEASURES, it does not adjudicate. It does NOT run any R·r=¼-selection / α-derivation test (CLOSED, anti-pattern-marked). Forward reads + forward classification only; no fits, no target-matching.

---

## §1 The observable battery — 14 channels, with the AVE-native reading of each

Every channel = a native-state read or a composed reuse. **The "physical reading" column is the interpretation guide** — what the number *means* substrate-natively (Grant 2026-06-05, the flags folded in).

| # | Channel | Read (native state) | Physical reading (AVE-native) | Reuse / tag |
|---|---|---|---|---|
| 1 | **Γ reflection coef (HEADLINE)** | rebuild per directed A→B bond from the **persistent** `z_local_field` (engine never stores in-flight Γ): `Γ=(z_B−z_A)/(z_B+z_A)`; report Γ_max/min, **Γ_at_max_A2_bond**, Γ-vs-A² scatter | **The reflecting boundary IS matter.** Cold vacuum is uniform `Z₀` → Γ=0 (transparent). Γ≠0 only where saturation bends `S(A)`. `sign(Γ_at_max_A2)` = the soliton wall's boundary condition: **+1 = antinode (OPEN, Z→∞, mass-closure)** vs **−1 = node (SHORT, primer)** — which sets the standing-wave ladder → mass/α. Only meaningful with Op14 nonlinear ON. | `universal_reflection` (universal_operators:118); `z_local_field` native · *native-read* |
| 2 | **Power split R²/T²** | `R²=Γ²`, `T²=1−Γ²` per bond | Whether energy is fully reflected (`T²→0` = trapped) regardless of OPEN/SHORT *sign* — the magnitude vs sign question | `universal_power_transmission` · *native-read* |
| 3 | **Capacitive reactance X_C** | `|V_inc|/(ω·|Phi_link|)` per port | The C-state (voltage store) vs L-state amplitude ratio. **ω must be the soliton's Compton/LC self-frequency `ω_C=c/ℓ_node` (l3:68), not the drive** — v1 uses drive-ω (tagged); a formed electron rings at ω_C | NEW `_reactances` · *engineering-input (ω)* |
| 4 | **Inductive reactance X_L** | `ω·|Phi_link|/|V_inc|`; report **X_L/X_C** | L-state (flux store). `X_L/X_C→1` = LC-matched standing mode (the bond-pair resonance). Same ω caveat as #3 | NEW `_reactances` · *engineering-input (ω)* |
| 5 | **Real↔phase angle Θ_RP** | angle between real-space n̂ (Cosserat ω→unit) and phase-space C↔L/U(1)-fibre phase | Eigenmode-vs-trajectory discriminator: **n̂ locked in quadrature to the C↔L fibre = phase-coherent eigenmode**; angle drifts = dissipative trajectory. Distinct real vs phase axes (phase-space-coordinate-check) | reuse `field_direction_nhat`+`fibre_phase_cell`+`knot_tangent_port_weights` (r10) · *native-read* |
| 6 | **(2,3) winding** | `extract_2_3_spatial` full-field walk: w1_base(n̂ "2"), w2_fibre(C↔L "3"), c; + modal_count/n_walks confidence | The soliton's **topological charge W** — conserved (mass-closure: can't un-knot without unwinding W; protection 2m_e c²). It does NOT fade gradually → on a 91%-bound state the winding is *there*; a weak read = thermal dressing, not lost charge (the V0 fork → contamination side). Confidence fields make a weak read visible | reuse `extract_2_3_spatial` (r10, clean-validated) · *native-read + confidence* |
| 7 | **7-mode energy split** | 3 translational/C (`½ρu̇ᵢ²`) + 3 rotational/L (`½I_ω ω̇ᵢ²`) + 1 volumetric (`½λ(∇·u)²`); + `E_K4` | The energy partition across the substrate's 7 micropolar DOF — the C-sector (3 trans + volumetric) vs L-sector (3 rot) balance, mechanically | reuse `kinetic_energy` (cosserat:1504) split per-axis; div-u NEW · *native-read* |
| 8 | **Energy budget + retention** | E_K4, E_cos, T_cos, E_coupling, H_total; `retention=H(t)/H(t_drive_off)` | Conservation-vs-dissipation: retention→1 = bound standing wave (mass = trapped reactance); →0 = dispersal | compose `EnergyBudgetObserver._capture` (vacuum_engine:667) · *composed* |
| 9 | **Boundary invariants M, Q, J** | on `A=√(V_inc²)`: M (∫(n−1)dV), Q, J | The three things visible outside a Γ-wall (A-026). **M rigorous (mass = integrated strain, geometry).** **Q, J are TOPOLOGICAL** (Axiom 2 [Q]≡[L]: charge IS the winding; J = (2,3) angular momentum) — the proxies (component-count, MOI-anisotropy) are geometric stand-ins, NOT the linking/winding. Read Q/J as proxy until fed from #6/#11 | `compute_all_invariants` (boundary_invariants:268) · *M native-read; **Q/J first-pass-proxy (mandatory tag)*** |
| 10 | **Beltrami helicity** | `h=ω·(∇×ω)/(...)` (Cosserat) + `h_K4` (TLM bipartite) | The chirality signature — the handedness frozen at genesis, carried by the soliton | reuse `_beltrami_helicity`/`get_helicity_density` · *native-read* |
| 11 | **Hopf charge + centroids + R/r** | Q_hopf (Chern-Simons), centroids, shell R_major/r_minor; R/r | Topological sector (→6 for (2,3) electron, 0 vacuum); R/r vs φ² golden-torus aspect; centroids = where matter sits. Feeds the rigorous Q/J | compose `TopologyObserver._capture`+`extract_shell_radii` · *native-read* |
| 12 | **Saturation / regime** | A²_max (Pythagorean K4+Cos), sat_frac, per-regime cell counts, S_field_min | Where on the Axiom-4 kernel the substrate sits — **how close to making a boundary** (A²→1 = the wall forms = matter) | compose `RegimeClassifierObserver._capture` · *native-read* |
| 13 | **Per-site charge density ρ_Q** | pre-integration Chern-Simons/Beltrami integrand per site | Virtual-soliton / pair-nucleation precursor map — where the substrate is *about to* seed topology | NEW `_charge_density` (reuse Q_hopf kernel) · *native-read* |
| 14 | **Spectral dispersion** | FFT of accumulated probe series → v_phase, v_group, f_BZ | Does the soliton ring at ω_C? phase/group velocity, Brillouin-edge — the substrate's dispersion. POST-RUN only | `universal_spectral_analysis` · *native-read (DSP)* |

---

## §2 Reading the results — the four AVE-native principles (the per-sim analysis is built on these)

1. **Matter only exists at saturation.** Γ≠0, a boundary, a soliton, a "short/open" question — all require the nonlinear regime. On a linear-vacuum run (`op3/nonlinear` OFF), Γ≈0 reads **"no-reflection / linear-vacuum,"** NOT "matched." The metadata records the flags so this is never misread. *Matter is what the substrate makes when it strains itself to saturation.*
2. **Γ's sign at the saturated wall = the electron's boundary condition.** `+1` = antinode/OPEN (stiff wall, Z→∞, mass-closure); `−1` = node/SHORT (clamped, primer). It sets the standing-wave ladder → the (2,3) closure, the Q-factor, the mass, α. The battery reports the sign with verbatim numbers as **evidence**; which boundary condition the substrate truly imposes is the corpus seam, **Grant's adjudication** (flag-don't-fix).
3. **The (2,3) is a conserved topological charge.** It cannot fade gradually (unwinding costs 2m_e c² — a pair-creation event). So a 91%-bound state *has* the winding; a weak extractor read is **thermal dressing around a conserved core**, not lost charge. The degradation-vs-contamination fork is therefore **topologically tilted toward "tool, not physics."** The confidence fields (#6) surface a weak read honestly.
4. **Charge and spin are topology; mass is integrated geometry; reactances live at the Compton ring.** M = ∫strain → rigorous. Q/J = the winding/linking (Axiom 2) → proxy until counted from the real winding (#6/#11). X_C/X_L are frequency-dependent and the right frequency is the soliton's own `ω_C=c/ℓ_node`, not the drive (measure it; convergence to ω_C is itself an electron-check).

---

## §3 Integration (library discipline — `ave-module-library-discipline`)

- **Module:** `src/ave/core/observable_battery.py` — `ObservableBattery` class + `ObservableReport` dataclass + a thin `BatteryObserver(Observer)` wrapper. In `core/` (engine-agnostic); lazy try/except imports of the topological readers so a pure-FDTD run doesn't require the Cosserat/JAX stack.
- **Hook (two modes, off `vacuum_engine.py:1851`):** (1) **per-step** `BatteryObserver._capture` → `battery.sample_cheap(engine)` (O(N) scalar channels only — Γ reductions, reactances, E7, budget, regime, helicity, Q_hopf), cadence-filtered; (2) **post-run** `battery.extract_full(engine)` runs the expensive field-walks ONCE on the converged state (#6 (2,3) shell-walk, #9 M/Q/J, #11 R/r, #13 ρ_Q, #14 FFT). Mirrors the shipped cheap-scalar-history / heavy-topology-once pattern.
- **Non-VacuumEngine3D engines** (MasterEquationFDTD etc. — no observer hook): the harness wraps their `run()` loop; the report marks N/A channels (Γ undefined for a scalar field) so a missing read isn't a null result.
- **KEEP-BOTH:** composes shipped diagnostics (`universal_reflection`, `compute_all_invariants`, the three Observers' `_capture` bodies, `_beltrami_helicity`, `extract_2_3_spatial`, …) by import; redefines none. Existing bespoke sweeps untouched.
- Constants strictly from `ave.core.constants` (`ave-canonical-source`).

---

## §4 Sweep harness (`src/ave/core/observable_sweep.py`) — no axis privileged

`SweepSpec{name, parameter_grid: dict[str,list], cadence, output_dir}` → `expand_grid` = `itertools.product` over the declared axes (amplitude, n_periods, N, arm, chirality, seed, temperature, op14_mode — **driver declares which it varies; none privileged**). `run_one_config` builds the engine, attaches `BatteryObserver`, runs, `extract_full` → `ObservableReport`. **Per config:** `sim_{id}.json` (full battery + config + per-sim analysis + metadata incl. honesty tags + flags) + a columnar `{name}_results.npz` (rows=configs, cols=all scalar channels) for cube-slicing + `{name}_manifest.json`. **Per-sim analysis = forward classification** (OPEN/SHORT via `sign(Γ_at_max_A2)`; eigenmode/trajectory via Θ_RP + retention; (2,3)-hosted via `is_2_3`; LC-matched via `X_L/X_C`; regime) — every verdict a forward read off native state, all thresholds honesty-tagged. *Which axis discriminates is read OFF the cube, not decided up front.*

---

## §5 Honesty tags + discipline

Every channel carries `source ∈ {native-read, composed-diagnostic, first-pass-proxy, engineering-input}`. Mandatory: Q/J = `first-pass-proxy`; reactance ω = `engineering-input`. Discipline: `phase-space-coordinate-check` (real vs phase axes tagged per channel), `ave-driver-script-honesty` (forward reads, no fits/targets), `ave-canonical-source` (zero hardcoded literals), `consistency-vs-emergence` (instrumentation, not emergence/α-claim), `substrate-native-check` CP8 (characterize, don't plant), `ave-evidence-framing` (proxy never read as rigorous).

---

## §6 Build plan (9 steps — skeleton-first, live-fire-gated)

1. Skeleton + dataclasses (`ObservableReport`, honesty-tag enum, empty `ObservableBattery` shell); constants imported. Commit.
2. **Γ channel FIRST (headline).** `_reflection` from persistent `z_local_field` + `universal_reflection`; reduce to Γ_at_max_A2 + bins; R²/T². **Live-fire on a tiny `VacuumEngine3D(N=24, imposed (2,3))` and PRINT `sign(Γ_at_max_A2)` to confirm the OPEN/SHORT read fires.** Commit. ← **first orchestrator checkpoint**
3. Reactances (X_C/X_L, ω=config tagged) + 7-mode energy + budget/retention. Commit.
4. Composed shipped diagnostics (regime, Q_hopf, centroids, M/Q/J with V_YIELD, helicity, R/r); tag M-rigorous vs Q/J-proxy. Commit.
5. Heavy full-field reads in `extract_full` only ((2,3) `extract_2_3_spatial`, Θ_RP, ρ_Q, dispersion FFT). Commit.
6. `BatteryObserver` + per-sim-analysis verdict block (forward classifications, threshold tags) + FDTD-scalar branch. Commit.
7. Sweep harness (`observable_sweep.py`: SweepSpec, expand_grid, run_one_config, run_sweep → per-sim json + npz + manifest). Commit.
8. **Aggregator + batch-end live-fire:** `aggregate_sweep` + `render_sweep_summary` (Γ-sign matrix, Θ_RP heatmap, (2,3) grid, E7 bars, retention curves). Run a real small cube (amplitude × arm × n_periods, N=32, ~8–16 sims) end-to-end; confirm every channel populates + OPEN/SHORT resolves per-sim + all artifacts write. Commit. ← **validate-what-you-did gate**
9. Reuse + honesty audit (zero hardcoded literals; no shipped diagnostic redefined; every channel tagged); closure-roadmap note. Commit.

**Deliverables:** the two modules, the live-fire small-cube run + summary, the result doc, brief updated; reviewed PR to `main`.

---

## §7 What it settles (the payoff)

Running any instrumented sim now reports, honestly: **Γ-sign** (the open/short seam, evidence for Grant) · **Θ_RP + (2,3) + confidence** (the coordinate + the V0 fork, topologically tilted) · **X_L/X_C** (the C↔L state) · **shell-walk + R/r** (single-bond vs bond-pair) · **M/Q/J, energy, regime, helicity, dispersion**. Five threads, one tool — and every future AVE sim inherits the full readout.
