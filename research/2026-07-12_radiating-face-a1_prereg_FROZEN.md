# A1 — Radiating face (universe port for local models) — FROZEN prereg

**Freeze discipline.** This prereg is frozen **by push**: it is pushed as its own
commit BEFORE any driver / face-port / test code exists (ave-prereg v1.7 Step 3.11).
Bins below are frozen; **frozen bins enforce, flags don't**.

**Authorization.** Grant 2026-07-12 session: focus the not-built stack on
**A1 radiating-face** — a local solid model that radiates strain into a universe
port accurately (not melt-fluid, not node-mint, not painted envelopes).

**Class.** Engine-completeness / **boundary instrumentation** — NOT a new chord.
No `genesis_v{N}`, no srs v18+, no fourth engine. Rule-14: reuse
`CrystalEngine` / `MasterEquationFDTD` / `NativeCageIMEX` / facade energy gates
(GX3/GX5 pattern).

**α-CLEAN.** No ALPHA import on the verdict path. Cosmic IC may appear only as
**slow projected bias** (optional follow-on); A1 itself is the radiating face.

---

## Sector header (mandatory)

- **SECTOR** = solid-phase mechanical dilatation / shear radiation at a **domain
  face** looking into an exterior port (universe stub). Not electron remanence
  (R10); not node-creation; not melt EOS.
- **Does the engine carry the DOF?** Interior YES (existing solid engines).
  **Matched radiating face keyed to live \(Z(A)\)** — PARTIAL (PML/sponge exists;
  GX5 proves *one* Newmark radiative port is passive on facade). **Universe stub
  returning Machian / \(\Omega_{\rm freeze}\) projections** — NO (A2+, out of
  A1 scope).
- **MODE** = mechanical bulk + shear (strain leave-taking); EM-transverse only as
  a cross-check channel if already exposed — do not conflate \(c_{\rm EM}\) vs
  \(c_{\rm shear}\) (Pitfall #5 / categorization slot refusal).
- **REGIME** = primarily **I–II** (sub-yield matched radiation). Near-yield face
  (\(A\) high at the pad) is a **named stress test**, not the default PASS path.
- **PHASE-STATE** = cold solid lattice embedded in infinite (or cosmically large)
  exterior. Melt / cavitated phases out of scope.
- **Instrument:** prefer closed-box vs open-port comparison on the same seed
  (Rule-14 reuse of facade `energy_gate_lossless_limit` + GX5 passivity idiom).
- **consistency-vs-emergence:** A1 is **FIREABLE instrumentation** +
  CERTIFICATION that PML cells stay out of physics reads (Rule 10). Success is
  **not** emergence of \(m_e\) or cosmic \(G\).

---

## Corpus sweep (STEP-0)

| Prior | Finding |
|---|---|
| `engine-capability-map.md` §6 | Loop / boost / node OPEN; A1 is **orthogonal** (port layer, not electron DOF column) |
| `breathing-soliton-v14-mode-i.md` | PML = numerical absorber, **no physical meaning** |
| `unified-engine-design-doctrine.md` + GX5 | Closed-box energy gate mandatory; sponge-MULTIPLY PML **injected** energy (142× artifact); Newmark radiative port must be **passive** |
| `cosserat_field_3d.use_impedance_boundary` | Moving \(\Gamma\) clamp from live \(S\) — **cavity wall**, not matched radiation to infinity |
| Op14 cosmic-horizon / Machian \(\xi\) | Universe **projections** exist as prose/params; **not** a live exterior stub (A2+) |
| Nucleation viz session 2026-07-12 | Painted \(R(t)\) ≠ tracking; free dynamics disperse; clarified need = **universe port**, not melt |

**VERDICT: authorized-open.** Matched radiating face is genuinely thin/missing as a
**discipline + diagnostic package** on solid engines; pieces exist (PML, GX5) but
are not unified as “local model ↔ universe port.”

---

## Target (one sentence)

Build and gate a **Rule-14 radiating face** so a local solid run can launch a
known strain / shear packet and demonstrate **passive absorption** (no energy
injection at the face) with **reflection residual below a frozen floor**, while
physics observables are read only on the **PML/port-excluded interior**.

---

## Analytic expectations (mandatory numbers)

### Face law (default, Regime I–II)

Exterior reference impedance \(Z_{\rm univ} = Z_0 \equiv 1\) (engine units) for
cold vacuum. Face uses live \(\mu\)-load \(Z_{\rm face}=\sqrt{S(A)}\) on the
boundary shell (same chain as `crystal_engine.gamma_bulk`).

Reflection amplitude at the port (analytic matched limit):

\[
\Gamma_{\rm port} = \frac{Z_{\rm univ}-Z_{\rm face}}{Z_{\rm univ}+Z_{\rm face}}
\quad\Rightarrow\quad
A\to 0,\; S\to 1,\; Z_{\rm face}\to 1 \Rightarrow \Gamma_{\rm port}\to 0.
\]

**Expectation:** in a linear outgoing-pulse run, time-integrated
\(|\Gamma_{\rm port}|\) (or proxy: reflected energy / launched energy) satisfies

\[
\mathcal{R} \equiv \frac{E_{\rm reflected}}{E_{\rm launched}} < 10^{-2}
\]

on the measurement window after the pulse has cleared the interior
(**fireable**; not entailed by mesh install alone).

### Passivity (GX5-class)

With the radiating face ON, total mechanical energy of
(interior + accounted port outflow) must **not increase** beyond numerical floor:

\[
\frac{E_{\rm tot}(t_{\rm end})-E_{\rm tot}(t_0)}{E_{\rm tot}(t_0)} > -\,\varepsilon_{\rm num}
\quad\text{and}\quad
\Delta E_{\rm tot} \le +\varepsilon_{\rm inj}
\]

with \(\varepsilon_{\rm inj} = 10^{-3}\) relative (**PASS** = no sponge-injection
class growth). Sabotage: multiply-damped PML (legacy) or energy-injecting BC
must **trip** the gate (Discriminator 7).

### Closed-box control

Same seed, face OFF / no PML: lossless-limit \(|\Delta H/H| < 10^{-6}\) (or the
landed facade threshold already used by GX3/RUNG-0 — **reuse**, do not invent a
looser number). Certifies the seed is not a numerical bomb before opening the port.

### Near-yield stress (report, not default PASS)

If \(A\) on the face exceeds \(r_1=\sqrt{2\alpha}\), \(\Gamma_{\rm port}\) is
**allowed** to depart from 0; report \(\mathcal{R}(A)\) vs the analytic
\(\Gamma_{\rm port}(Z(A))\). Bin separately — do not fail A1 default on this leg.

### Entailed vs fireable (ave-prereg v1.7)

| Claim | Class |
|---|---|
| PML cells excluded from \(\Gamma_{\min}\)/energy reads | CERTIFICATION / Rule 10 |
| \(\Gamma_{\rm port}\to 0\) when \(A\to 0\) algebraically | ENTAILED by \(Z=\sqrt{S}\) definition |
| \(\mathcal{R}<10^{-2}\) on a live outgoing pulse | **FIREABLE** |
| Face never injects energy (GX5-class) | **FIREABLE** (+ sabotage) |
| Machian \(G\) / \(\Omega_{\rm freeze}\) live projection | **OUT OF SCOPE** (A2+) |

---

## Frozen bins

| bin | criterion | meaning |
|---|---|---|
| **(i) FACE-PASSIVE-MATCHED** | Closed-box control PASS; open-port \(\mathcal{R}<10^{-2}\); passivity gate PASS; sabotage TRIPS | A1 landed for Regime I–II local→universe radiation |
| **(ii) FACE-PASSIVE-MISMATCHED** | Passivity PASS but \(\mathcal{R}\ge 10^{-2}\) | Absorbs but wrong \(Z\) / geometry — retune face, not cosmology |
| **(iii) FACE-INJECTS** | Energy grows beyond \(\varepsilon_{\rm inj}\) with face ON (or sabotage fails to trip) | Forbidden PML/BC class — halt promotion |
| **(iv) CLOSED-BOX-FAIL** | Lossless control fails before port open | Interior integrator/seed issue — not a face verdict |
| **(v) HALT** | Fourth engine / node-mint / melt-fluid scoped as A1 | Forbidden by this prereg |

**Near-yield stress** reports into a sidecar table; it does **not** select (i)–(iv)
unless the default linear leg is contaminated.

---

## Gates (driver PR — later)

1. Closed-box energy control on the chosen Rule-14 carrier.
2. Outgoing pulse + \(\mathcal{R}\) measurement (PML/port-excluded interior).
3. Passivity gate + **sabotage** (injecting BC must fail).
4. Rule 10: no PML cells in physics aggregates.
5. `ClaimClass` tags: face PASS ≠ EMERGENCE / genesis.
6. `make verify` relevant keepers green.

---

## Out of scope (A1)

- Live Machian \(\xi\) / \(\Omega_{\rm freeze}\) exterior stub (**A2**).
- Melt entrainment / node-creation / R10 remanence.
- Painting \(R(t)\) saturation envelopes.
- Equating PML with cosmic \(\Gamma=-1\) horizon.
- Merging #652 X44; graph-growth.

---

## Deliverables

- This FROZEN prereg (this commit, pushed first).
- Orchestration pointer in `_orchestration/` + index line.
- Later: thin driver + result doc on a follow-on commit/PR (freeze claimable only
  via this push ordering).

## Next after (i)

**A2** — universe stub: one-way exterior + slow projected IC (Machian /
\(\Omega_{\rm freeze}\)) feeding constitutive bias; still no full outer mesh
required for the thin charter.
