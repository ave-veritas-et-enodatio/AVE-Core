# SPICE-lane feasibility — inventory findings + pilot evidence

**Date:** 2026-07-03
**Branch:** `analysis/spice-lane-charter` (off `origin/main`, HEAD `a0508e50`)
**Companion charter:** [`_orchestration/2026-07-03_spice-lane-charter.md`](../_orchestration/2026-07-03_spice-lane-charter.md)
**Role:** implementer lane. Planning arc — evidence note, not production code.

This note is the file:line evidence base for the charter. It records
(1) what the SPICE lane already IS, (2) the run-state of every artifact,
(3) the constitutive-drift + sign-inconsistency flags surfaced during
inventory (flag-don't-fix — NOT resolved here), and (4) the bounded-pilot
verdict.

---

## 0. Headline (the one thing that reframes the charter)

**The SPICE lane is NOT greenfield, and the "SPICE" in it has never touched
a SPICE engine.** Everything under the "SPICE" banner today is either (a) a
netlist *emitter* whose output has never been fed to ngspice, or (b) a
*native-Python* ODE/matrix solver wearing the "SPICE" label as a branding
pattern. `spice_cvr_loop.py:303` self-reports `"spice_executed": False`;
the result doc `research/2026-06-13_spice-cvr-constitutive-loop_result.md:7`
states "**Python only**; ngspice transient not executed"; every
ngspice-invoking test is gated behind `@ngspice_required` and skips
(5 skipped, this machine). **No SPICE engine has ever validated an AVE
netlist.** The charter is therefore about *promoting an emit-only lane to a
run-and-cross-check lane*, not about building from zero.

---

## 1. Inventory table (verify-before-cite; every row grepped 2026-07-03)

| Artifact | Path | State | Run? | Rides |
|---|---|---|---|---|
| Netlist compiler | `src/ave/solvers/spice_netlist_compiler.py` | 296 lines; emits `.cir`; imports `C_0, V_YIELD, XI_TOPO` from `ave.core.constants` (:24) | **emit-only** — no `subprocess`/ngspice call anywhere in module | App 6 manual |
| Canonical `.lib` | `src/ave/solvers/spice_models/ave_vacuum_cell.lib` | 169 lines, valid ngspice B-source syntax; 5 subckts (`AVE_VACUUM_CELL`, `_LINEAR`, `_L1`, `AVE_MEMRISTOR_S_STATE`, `AVE_EE_BENCH`) | **never parsed by ngspice** (only via skipped tests) | clm-vjv4zf |
| Transient integrator | `src/ave/solvers/spice_transient.py` | 102 lines; explicit-Euler `a=(-∇V-Rv)/L`; **pure numpy/JAX**, no SPICE | runs (unit) | App 5/6 |
| CVR constitutive loop | `src/ave/solvers/spice_cvr_loop.py` | 340 lines; L0/L1/L2 ODE ladder; `"spice_executed": False` (:303) | runs (Python ODE) | — |
| Vacuum-cell tests | `src/tests/test_spice_vacuum_cell.py` | 207 lines; 5 analytical PASS + 4 ngspice `@ngspice_required` | **4 skip** (ngspice absent) | — |
| CVR-loop tests | `src/tests/test_spice_cvr_loop.py` | 81 lines | runs | — |
| Compiler demo | `.agents/scratch/demo_spice_compiler.py` | 111 lines; "verifies" via **numpy ABCD matrices**, not ngspice | runs | — |
| CVR pre-reg | `research/2026-06-13_spice-cvr-constitutive-loop_prereg.md` | FROZEN 2026-06-13 | — | — |
| CVR result | `research/2026-06-13_spice-cvr-constitutive-loop_result.md` | verdict **DISSIPATIVE-ONLY + IMPOSED-LATCH** (Rule-12 retracted from REMANENT-LOOP); PR #215 OPEN, do-not-merge | — | — |
| App-6 manual | `manuscript/backmatter/06_spice_verification_manual.tex` | 347 lines; positions SPICE as independent verification tool | — | — |
| ch18 subcircuit spec | `manuscript/ave-kb/vol4/simulation/ch18-universal-vacuum-cell/spice-subcircuit.md` | KB leaf | — | clm-vjv4zf |
| ch14 leaky-cavity netlist | `manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/spice-netlist.md` | KB leaf; VSWITCH breakdown | — | clm-c54kdd |
| ch15 autoresonant netlist | `manuscript/ave-kb/vol4/simulation/ch15-autoresonant-breakdown/spice-netlist.md` | KB leaf; PLL behavioral | — | clm-9sujp8 |
| ch16 sagnac netlist | `manuscript/ave-kb/vol4/simulation/ch16-sagnac-inductive-drag/spice-netlist.md` | KB leaf; directional-L B-source | — | clm-cbwd77 |
| ch17 ee-bench netlist | `manuscript/ave-kb/vol4/simulation/ch17-hardware-netlists/ee-bench-netlist.md` | KB leaf; DC sweep | — | clm-vjv4zf |
| vol9 device-circuit-models | `manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md` | 256 lines; §1 cell sectors, §6 graded network | — | clm-kezk9z + |
| chiral circulator vocab | `manuscript/ave-kb/common/vocabulary-register.md:696` (`def-ch1crc`) | STATED pending chiral-crystal engine; NOT adjudicated | — | — |

**clm- IDs riding on the SPICE leaves:** clm-vjv4zf, clm-c54kdd,
clm-9sujp8, clm-cbwd77, clm-kezk9z (grepped across the ch14-18 + vol9
leaves). All are KB-leaf claims describing the netlist *forms*; none
asserts a *run result* (there are no run results to assert).

**Test run-state (this machine, 2026-07-03):**
`pytest test_spice_vacuum_cell.py test_spice_cvr_loop.py` → **14 passed,
5 skipped**. All 5 skips are the ngspice-gated cases.

---

## 2. Flag-don't-fix — inconsistencies surfaced during inventory

Per flag-don't-fix: these are surfaced with both paths + verbatim content.
NOT resolved. They are Grant/auditor adjudication items.

### FLAG-1 — constitutive VALUE drift (V_YIELD three ways)

The Ax4 yield voltage appears at **three different values** across the lane:

- `src/ave/core/constants.py:464` (canonical source): `V_YIELD = 43651.85…`
  (evaluated live: **43651.851844…**)
- `src/ave/solvers/spice_models/ave_vacuum_cell.lib:52,95,113,160`: subckt
  default `V_YLD=43651.9` (rounded — close, but a hardcoded literal)
- `manuscript/ave-kb/…/ch18-universal-vacuum-cell/spice-subcircuit.md:23,78`
  and `manuscript/backmatter/06_spice_verification_manual.tex:159`:
  **`V_YLD=43653.7`** / `43654` — a **DIFFERENT number** (off by ~1.8 V).

The App-6 manual `:167` claims *"No constants are hardcoded in the .lib
file"* — **false**: the `.lib` subckt defaults hardcode `43651.9` and
`124.384`. This is exactly the drift design-question (d) exists to prevent,
already realized in three places. (`I_YMAX`: `.lib`=124.384 vs KB
spec=124.4 — same drift class.)

### FLAG-2 — varactor constitutive-law SIGN inconsistency (RECIPROCAL kernels)

The metric varactor is written with the saturation factor on **opposite
sides of the fraction** in the canonical library vs two KB netlist leaves:

- **Canonical** (`.lib:63`, App-6 `:97`, ch18 `:26`, vol9 §1 table:28):
  `Q = C0 * V / sqrt(1 - (V/V_YLD)^2)`  ⇒  **C_eff = C0 / S(V)**,
  capacitance **diverges** as V→V_yield.
- **ch17 ee-bench** (`ee-bench-netlist.md:36`): `Q = C0 *
  sqrt(1 - (V/V_yield)^2) * V`  ⇒  **C_eff = C0 · S(V)**, capacitance
  **collapses** as V→V_yield.
- **ch15 autoresonant** (`autoresonant-breakdown.../spice-netlist.md:20`):
  same `C_eff = C0 · S(V)` (collapse) form.
- **ch17 prose** (`ee-bench-netlist.md:15`) states
  `C_eff(V) = C0 sqrt(1-(V/V_yield)^2)` — the **collapse** form, matching
  its own netlist but **contradicting** the canonical `.lib` and vol9 §1.

These are **reciprocal** constitutive laws — they predict **opposite signs**
of the plateau (diverge vs collapse). The App-6 worked-example numbers
(`06_spice_verification_manual.tex:228-230`: `C_eff/C0 = 1.155` at
`V/V_yield=0.5`) match the **divergent** `/S(V)` form (1/√0.75 = 1.1547),
confirming the canonical intent is `/S(V)`. The ch15/ch17 leaves are the
outliers. **This is a load-bearing physics contradiction** (which way does
the vacuum capacitance go at yield?) and must be adjudicated before any
ngspice run — a run would silently validate whichever sign the netlist
happens to carry. NOT resolved here.

### FLAG-3 — App-6 "solver-independent" claim vs never-run reality

`06_spice_verification_manual.tex:71-73` asserts agreement between the
Python engine and ngspice "constitutes a cross-platform consistency check."
No such agreement has ever been computed — the ngspice half has never run.
The manual describes an *intended* cross-check as though it were an
*achieved* one. (The 2026-06-15 scope caveat at :19-24 honestly narrows
"derives" to forms-not-values, but does not caveat the un-run SPICE half.)

---

## 3. Pilot evidence

**Script:** `src/scripts/vol_4_engineering/spice_lane_pilot_poisson.py`
**Outputs:** `_output/spice_lane_pilot_poisson.cir` (ngspice-ready netlist),
`_output/spice_lane_pilot_poisson_result.json` (verdict).

**What it does.** ngspice is NOT installed (see §4), so the pilot builds the
*identical* MNA (Modified Nodal Analysis) linear system a SPICE `.OP` would
assemble for a resistor network — `G v = i`, ground row/col deleted — in
pure numpy, and cross-checks it against a structurally independent
graph-Laplacian pinned-Dirichlet solve (the numpy path the srs engine
already uses for Poisson statics). It also emits the equivalent `.cir` so
the ngspice path is runnable the instant ngspice lands.

**Result (24 nodes, 32 edges, 1 mA injection, seed 20260703):**

```
max|v_MNA - v_Laplacian| = 7.550e-15 V
VERDICT = PASS   (threshold 1e-10)
ngspice_executed = False
```

**What this proves.** Test-ladder rung 3 (known-Poisson vs numpy) is
demonstrated end-to-end: the MNA matrix SPICE builds for a resistor network
IS the weighted graph-Laplacian the engine already solves; the two agree to
machine precision. The ground-node row/col deletion is the principled fix
for the singular-Laplacian / closed-graph-neutrality subtlety (design
question (e)/(g)). The statics cross-solve harness (design question (g),
the immediate Stage-1b consumer) is feasible and small.

**What it does NOT prove.** It does not exercise ngspice itself, and it does
not touch the Ax4 nonlinear kernel (that is rung 2, needs the `.lib` fed to
a real B-source engine — blocked on the ngspice install). The MNA stand-in
is *linear resistor* only.

---

## 4. Tooling availability (charter prerequisite)

| Tool | State | Install path |
|---|---|---|
| `ngspice` | **NOT installed** (`which ngspice` → not found) | `brew install ngspice` (Homebrew formula: stable 46, bottled, ~2.6 MB) |
| PySpice | **NOT installed** (`import PySpice` → ModuleNotFoundError) | `pip install PySpice` (wraps libngspice; still needs ngspice) |
| Xyce / LTspice / qucs | not present | — |
| numpy / scipy | present (numpy 2.4.4, scipy 1.15.3) | — |

**No install was performed** (system-state-change discipline). `brew install
ngspice` is flagged as the #1 charter prerequisite in the PR body.

---

## 5. One-line inventory verdict

The SPICE lane is a **well-formed, single-sourced, never-executed netlist
emitter + a Python-native solver mislabeled "SPICE."** It is a *reasonable
and cheap* thing to promote to a real cross-check lane (~2.6 MB dependency,
the MNA math already agrees to 1e-15) — **but only after FLAG-1 (value
drift) and FLAG-2 (varactor sign) are adjudicated**, because a live ngspice
run would otherwise silently certify whichever inconsistent form the netlist
carries. Full phased plan + design answers in the companion charter.
