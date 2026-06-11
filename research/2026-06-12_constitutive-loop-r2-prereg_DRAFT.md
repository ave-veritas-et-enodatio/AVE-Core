# R2 — Constitutive Loop Pre-Registration (DRAFT)

**Status:** `DRAFT-FOR-GRANT-REVIEW` (2026-06-12). **NOT FROZEN.**  
**Tier:** R2 / fundamentality plan §0b — prereg + cRIO ferrite B-H bench **before** any v10 sim.  
**Lane:** implementer. First deliverable is **framing + bench protocol**, not a genesis integrator.  
**Governing diagnosis:** LOOP GAP (`research/2026-06-11_vocab-operator-unification-audit.md` §4c2).

**Skills fired at draft time:** `ave-prereg`, `pre-test-physics-check`, `substrate-native-check`,
`consistency-vs-emergence`, `ave-discrimination-check`, `ave-evidence-framing-discipline`,
`ave-apparatus-floor-attribution`, `verify-before-cite`.

---

## 0. Relationship to v10 Decisions 2 and 4 (read this first)

v10 has two **orthogonal** open calls. R2 informs both; it does not replace Grant's pick.

| | **Decision 2 — loop scope** | **Decision 4 — `chi_shock` / saturation ride** |
|---|---|---|
| **Question** | Does the medium's **constitutive law** include a **closed B–H-style loop** (remanence), or only the **anhysteretic** saturation curve `S(A)=√(1−A²)`? | When the medium **crosses** saturation / a sonic horizon, is energy **irreversibly removed** (`chi_shock>0`), **channel-shuffled** (saturation transfer functions), or **fully elastic** (`chi_shock=0`)? |
| **EE picture** | **Ferrite B–H loop:** after you remove drive (`H→0`), does **`B_r` (remanence)** remain? That is the zero-drive persistence analogue of **mass**. | **Shock at a horizon:** when flow crosses `c→0`, is crossing KE **dumped to heat** (one-way) or **stored/recovered** in another channel? |
| **AVE kernel today** | Canon implements **σ / Op14 only** — instantaneous `S(A)`; SPICE manual: memristor **documented, not implemented**; *"hysteresis loop has **zero enclosed area**"* (`06_spice_verification_manual.tex:127-133`). | Sonic-horizon prereg: `chi_shock` = fraction of crossing KE **dissipated**; `:359` row = **per-channel** saturation transfer (`H_shear/H_EM/H_bulk`). |
| **Genesis symptom** | v6–v9: objects **store** under drive (`Q_react`) but **no architecture retained mass** without a quantizer/lock. Phase-2 Op14 trap is **reactive**, not remanent. | v5 snap / horizon work: **CLIP vs FLASH** — is persistence real physics or apparatus bookkeeping? |
| **Options** | **(a) σ-only** · **(b) σ + rate-gated snap** · ~~(c) defer~~ ✅ Phase-1/2 done | **(a)** `chi_shock=0`, transfer-fn ON · **(b)** `chi_shock>0` sweep · **(c)** defer dark-sector |

**How they differ (one sentence each):**

- **Decision 2** asks whether the vacuum medium has **memory of its magnetization state** when drive is removed — the **ferrite remanence ↔ mass** map.
- **Decision 4** asks whether **energy leaving a port during a crossing event** is **true dissipation** vs **reactive exchange** — the **shock / ledger seam** (CVR framing §4.4).

**Coupling (why both matter for v10):**

- You can have **σ-only + `chi_shock=0`** → saturating but **spring-back**; stores under drive, **no mass** (current engine class).
- You can have **σ + snap + `chi_shock=0`** → loop **geometry** without one-way heat (reversible hysteresis — rare in real ferrite at low f).
- **σ + snap + `chi_shock>0`** → the only package that can show **genesis-with-irreversibility** *and* zero-drive persistence — but it **reopens the loss seam** and needs reactance-pair accounting.

**R2's job:** characterize the **real ferrite B–H loop** on the bench so Grant can pick Decision 2/4 with measured EE anchors, not prose.

### 0b. Three-wave EE mapping — corpus vs R2 gaps (2026-06-12)

Recent work **already tri-channelled** propagation impedance; R2 is **single-channel** (μ / B-sector). This section records what is landed and what R2 still omits — especially **Ω_freeze**.

| Channel | $Z$ / speed | Wall $\Gamma$ | Saturation ride (Decision 4) | Memory / hysteresis class | R2 coverage |
|---|---|---|---|---|---|
| **EM** (transverse) | $Z_{\mathrm{EM}}$; $c_{\mathrm{EM}}$ **rises** with $A$ | $\Gamma_{\mathrm{EM}}=0$ (matched / transparent) | $H_{\mathrm{EM}}$ (`dark-sector-response` §3.2) | Lenz / back-EMF freeze blocks $dI/dt$ (`substrate-hysteresis-index` §1) | **Indirect** — ferrite eddy/hysteresis loss only |
| **Shear** (deviatoric / GW) | $Z_{\mathrm{shear}}$; $c_{\mathrm{shear}}$ **freezes** | $\Gamma_{\mathrm{shear}}\to -1$ at saturation | $H_{\mathrm{shear}}$ | Cosserat $\omega$ sector; microrotational phase-lock (`translation-circuit` memristor row) | **Absent** — no GW/shear bench arm |
| **Bulk** (longitudinal) | $Z_{\mathrm{bulk}}$; $c_{\mathrm{bulk}}$ **freezes** at $\bar\rho_{\mathrm{cav}}$ | $\Gamma_{\mathrm{bulk}}\to -1$ at snap | $H_{\mathrm{bulk}}$ | Standing-$V$ wall; **α turns-ratio** secondary (`alpha-boundary-energy` prereg, $Z_{\mathrm{bulk}}$ channel) | **Absent** — R2 does not test longitudinal wall / $\bar\rho_{\mathrm{cav}}$ |

**Ω_freeze (fourth memory class — not ferrite remanence):**

- **What it is:** one-time **cosmic spin lock** at lattice genesis — bond over-bracing $u_0^*$, global chirality $\hat\Omega_{\mathrm{freeze}}$, $\mathcal{J}_{\mathrm{cosmic}}$ (`omega-freeze-cosmic-grain-cascade` §2; `substrate-hysteresis-index` §4).
- **EE map:** polarized-TL bias / chirally-rotated reference frame; Machian $G$ as horizon input impedance (`translation-circuit` rows 16–17).
- **Mechanism link to LOOP:** same **BEMF / $L_{\mathrm{eff}}\to\infty$** family as §1 — blocks $d\omega/dt$ during yield crossing so topology **cannot unwind** (`tau-relax-derivation` §4). **Different time scale** from ferrite $B_r$: cosmic **initial data**, not a cyclic $(H,B)$ loop.
- **Genesis readout:** charge sign / chirality direction inherit from $\Omega_{\mathrm{freeze}}$ (simulation-assumptions audit); Phase-2 Op14 trap is **reactive under drive**, not a replay of cosmic freeze-in.
- **R2 gap:** bench ferrite **cannot** adjudicate Ω_freeze; needs **(i)** α-boundary-energy forward test (R1 sibling), **(ii)** explicit v10 **initial-condition** arm for $\hat\Omega_{\mathrm{freeze}}$, not only constitutive loop.

**What a complete three-wave + Ω_freeze EE map still needs (not in R2 scope alone):**

1. **Per-channel remanence ledger** — if Decision 2(b) lands, tag which channel holds zero-drive state ($B_r$ ↔ shear $\omega$ helicity ↔ bulk standing-$V$), not a single μ map.
2. **Decision 4 `:359` row** — $H_{\mathrm{shear}}/H_{\mathrm{EM}}/H_{\mathrm{bulk}}$ are the **three-wave crossing knobs**; R2 ferrite does not substitute for sim/bench on channel shuffle.
3. **Level 1 vs Level 2** (`tau-relax` §3) — reversible $S(A)$ envelope vs dynamic memristive loop; R2 must state which level the bench probes.
4. **Astrophysical $\Gamma_{\mathrm{bulk}}$ at horizon** — vocab audit §4b still **AMBIGUOUS** in vol3 gravity leaves; Ω_freeze cascade may require explicit bulk-wall assignment.
5. **Cross-sector reactance pair** — Op14 $\rho(\mathcal{H}_{\mathrm{cos}},\Phi_{\mathrm{link}})\approx -0.99$ (`op14-cross-sector-trading`); honest Decision 4 needs **Tellegen pair** accounting, not `chi_shock` alone.
6. **Sonic-horizon closure** — Z_bulk collapse tested **LOCK not FLASH**; persistence without `chi_shock` already falsifies one-way-dissipation-only story.

**R2 amendment (minimal):** keep ferrite as **μ-sector anchor** for Decision 2; add **explicit non-goals** (Ω_freeze, $Z_{\mathrm{bulk}}$ α-wall, per-channel $H_*$) and **pair with** α-boundary-energy prereg + dark-sector §3.2 sim arm before v10 charter execution.

---

## 1. Corpus-grep (ave-prereg Step 1)

| Prior item | Relevance | R2 relation |
|---|---|---|
| `S(A)=√(1−A²)` / Op14 | Anhysteretic saturation | **The GAP** — no enclosed loop area |
| `06_spice_verification_manual.tex:127-133` | Memristor **not implemented**; zero loop area | **Canon anchor** for LOOP GAP |
| `nonlinear-vacuum-capacitance.md` § Vacuum Memristor | Thixotropic `τ_relax`, pinched loop **theory** | Target kernel to implement if bench supports |
| Genesis v6–v9 session record | No mass retention without lock | **Motivating falsifier set** |
| v9 Phase-2 production | P5 FAIL, P6 inconclusive, Op14 reactive trap | **Does not test remanence** — LOOP still open |
| `2026-06-10_crio-ceff-saturation-onset_prereg-draft.md` | cRIO validation ladder, C_eff(V) | **Sibling bench** — varactor/saturation onset; R2 adds **B–H loop** arm |
| `2026-06-10_sonic-horizon-closure_prereg.md` | `chi_shock`, one-way crossing | **Decision 4 sim analogue** — not ferrite |
| `research/2026-06-11_chiral-vacuum-reactor-framing.md` §4–§5 | Lossless layers + v10 charter | Decisions 2+4 defined here |
| `research/2026-06-11_vocab-operator-unification-audit.md` §4a–4d | Three-impedance law + $\Gamma$ assignments | **Landed** — R2 must not re-derive; tri-channel gaps in §0b |
| `research/2026-06-10_field-symbol-registry.md` §3.11 | $Z_{\mathrm{EM}}/Z_{\mathrm{shear}}/Z_{\mathrm{bulk}}$ registry | **Landed** — channel-subscript discipline |
| `research/2026-06-11_alpha-boundary-energy_prereg.md` | $E_{\mathrm{boundary}}/E_{\mathrm{content}}=\alpha$ on $Z_{\mathrm{bulk}}$ | **Sibling R1** — transformer secondary of α; not ferrite |
| `research/2026-06-11_dark-sector-response-characterization.md` §3.2 | $H_{\mathrm{shear}}/H_{\mathrm{EM}}/H_{\mathrm{bulk}}$ | **Decision 4 `:359`** — three-wave saturation ride |
| `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md` | $\Omega_{\mathrm{freeze}}$, $u_0^*$, chirality lock | **§0b** — cosmic memory, not B–H loop |
| `manuscript/ave-kb/common/substrate-hysteresis-index.md` | Five hysteresis classes (§1–§5) | R2 = §5 subset; Ω_freeze = §4 |

**Genuinely open:** whether a **constitutive loop** (remanence) is THE missing kernel piece for mass retention — or whether remanence is an **emergent lattice** property not visible in a lumped ferrite bench.

---

## 2. Physical picture (Step 1.5)

### 2.1 The LOOP GAP (substrate picture)

Picture the vacuum medium as a **saturable reactive core**:

1. **Linear regime** (`A≪1`): small-signal propagation; effectively lossless in-band (CVR §4.2).
2. **Saturation** (`A→1`): Op14 stiffens `z_local`; snap / pair-production analogues fire (Regime IV).
3. **Under drive:** energy piles into **reactive stores** (`Q_react = m_e c² · α` ledger) — genesis v6–v9 **did** make objects.
4. **Drive off:** canon kernel returns along the **same** `S(A)` curve → **no remanence** → object **decays**. That is the nine-architecture record.

**Mass, in this framing, is remanence:** the persistent **`B_r` at `H=0`** in a ferrite — a **closed loop** in the `(H,B)` plane, not a point on the anhysteretic curve.

### 2.2 Ferrite bench as direct EE analogue (Grant 2026-06-11)

| Ferrite observable | AVE analogue | R2 bench gate |
|---|---|---|
| Linear `μ(H)` region | Regime I | Baseline — must see |
| **`B_sat`** knee | Snap / yield | Onset field recorded |
| **`B_r`** at `H=0` | **Mass** (zero-drive persistence) | **Primary discriminator** |
| **`H_c`** | Annihilation / coercivity threshold | Secondary |
| **Loop area ∮H dB** | Latent heat per create/annihilate cycle | Energy accounting |
| Inrush spike | Birth pulse (N4 vent) | Optional transient arm |

If a **real ferrite** shows **`B_r ≠ 0`** but the canon kernel cannot express it, the LOOP GAP diagnosis is **supported** (consistency-class). If ferrite shows **no remanence** at bench rates, the diagnosis is **weakened** — remanence may need a faster thixotropic channel (`τ_relax`) not accessible on cRIO.

### 2.3 What R2 is NOT

- **Not** a v10 genesis sim (that waits on Decisions 2+4).
- **Not** proof the vacuum **is** a ferrite (discrimination required — §5).
- **Not** a promotion of `ρ̄_cav` or cavitation physics (firewall unchanged).
- **Not** an Ω_freeze or cosmic-chirality adjudication — initial-data lock at genesis (§0b).
- **Not** a complete three-wave impedance map — single μ/B-sector; $Z_{\mathrm{bulk}}$ α-wall and $H_*$ transfer functions are **sibling** preregs / sim arms.

---

## 3. Hypotheses

**H1 (LOOP GAP — primary):** Canon's anhysteretic `S(A)` is **insufficient** for zero-drive mass retention; a **constitutive loop** (memristive / thixotropic / rate-gated snap) is the **missing kernel** class.

**H2 (rate-unified):** The documented but unimplemented **Vacuum Memristor** (`τ_relax = ℓ_node/c`) and **real ferrite domain-wall dynamics** are **one mechanism** at different rate scales — bench sees remanence at **material** `τ`; lattice needs **`f ≪ 1/τ_relax`** for full loop (cRIO is ~16 OOM below crossover per cRIO C_eff draft §3.3).

**H3 (emergence alternative):** Remanence is **not** a kernel patch — it **emerges** only from full lattice lock / quantizer (v6–v7 route). Ferrite bench would still map analogies but **would not** dictate kernel form.

---

## 4. Bench protocol (cRIO ferrite B–H)

**Hardware (inherited from cRIO program):** NI cRIO-9014 + NI-9263 (AO) + NI-9215 (AI); DC–40 kHz band.

**DUT:** ferrite toroid or gapped core (Grant inventory — **part number frozen at execution**, not here).

**Waveform:**

1. **Quasi-static B–H loop:** triangular or controlled ramp `H(t)` at sweep rates `{slow, med, fast}` spanning domain-wall vs quasi-static regime.
2. **Bidirectional major loop:** `H_max → −H_max → H_max`; record `B(H)` via flux sense (secondary winding or Hall, apparatus documented at run).
3. **Remanence read:** ramp `H→0`; measure **`B_r/B_sat`**.
4. **Coercivity read:** ramp `H` from `+B_r` until `B→0`; record **`H_c`**.
5. **Optional:** small-signal permeability `μ_diff(H)` on top of DC bias (links to C_eff sibling prereg).

**Apparatus inventory (CLIP suspects):**

| Knob | Sweep | CLIP signature |
|---|---|---|
| Ramp rate `dH/dt` | 3 decades | `B_r` tracks rate only (no intrinsic loop) |
| Sense geometry / air gap | fixed vs ±20% | knee fields track geometry only |
| Temperature | room vs elevated | all curves collapse to one thermal curve |
| Core material swap | ferrite A vs B | only material-specific if physics |

**Verdict-clearing:** remanence **robust** across rate sweep (same sign, comparable `B_r/B_sat`) → physics; tracks only `dH/dt` → CLIP.

---

## 5. Frozen predictions (pre-execution — thresholds filled at freeze)

| Gate | Criterion | Falsifier |
|---|---|---|
| **R2-L** | Linear region visible: `μ` stable over ≥10% of `H_c` span | No linear region — wrong DUT or apparatus |
| **R2-S** | Saturation knee `B_sat` identifiable (|dB/dH| drops ≥5×) | No knee — protocol fail |
| **R2-R** | **`B_r/B_sat ≥ 0.05`** at quasi-static ramp after major loop | **`B_r ≈ 0`** at slowest sweep → weakens H1 at bench band |
| **R2-C** | **`H_c` finite and repeatable** (±10% run-to-run) | Unstable `H_c` → apparatus |
| **R2-A** | Loop area **> 0** (enclosed ∮H dB) | Zero area → ferrite not showing hysteresis (DUT/rate) |

**Outcome bins:**

| Bin | Label | Rule |
|---|---|---|
| **BIN-LOOP** | Loop confirmed | R2-R + R2-A pass; material shows remanence |
| **BIN-RATE** | Rate-limited | R2-R fail at slow sweeps but pass at fast → thixotropic crossover story (H2) |
| **BIN-NULL** | No loop at bench | All sweeps `B_r≈0` → H1 weakened; emergence path (H3) live |
| **BIN-CLIP** | Apparatus | R2-R tracks knob only |

---

## 6. Discrimination (`ave-discrimination-check`)

| Claim element | SM / standard physics | AVE-distinct? |
|---|---|---|
| Ferrite has hysteresis | **Yes** — standard ferromagnetism | **No** — bench confirms material, not vacuum |
| `(1−A²)^(±1/2)` saturation *shape* | Standard saturating media exist | **Partial** — C_eff arm (sibling prereg) |
| **Remanence ↔ mass mapping** | SM mass not from B–H loops | **Yes** — interpretive bridge; **hypothesis-class** |
| Loop required for genesis | Not SM | **AVE-specific** — falsified if BIN-NULL + future lattice lock works |

**Honest closure:** BIN-LOOP **supports** implementing Decision **2(b)** in sim; it does **not** confirm vacuum is ferrite. BIN-NULL does **not** kill AVE — it redirects to **lock/quantizer** or **`τ_relax`** channel.

---

## 7. Kill conditions

1. **BIN-CLIP** on all primary gates → protocol redesign, no kernel claim.
2. Claiming **BIN-LOOP ⇒ CVR-SET** without v10 sim → **Rule 11 violation**.
3. Using bench `B_r` as **numerical fit** to `m_e` without independent chain → **fit-as-prediction** (driver honesty).

---

## 8. Links to v10 Decisions (post-bench Grant calls)

| Bench outcome | Suggested Decision 2 read | Suggested Decision 4 read |
|---|---|---|
| **BIN-LOOP** | Lean **(b) σ + rate-gated snap** for v10 integrator | Start **(a) `chi_shock=0`** + transfer-fn ON; add **(b)** only if ledger armed |
| **BIN-RATE** | **(b)** with explicit `τ_relax` / thixotropic ODE | **(a)** — reversible exchange first |
| **BIN-NULL** | Stay **(a) σ-only** longer; pursue **lock/quantizer** | **(a)** or **(c)** defer dark-sector |

---

## 9. Implementor deliverables (after freeze)

| Artifact | Path |
|---|---|
| Bench driver / worksheet | `research/2026-06-12_constitutive-loop-r2_bench-protocol.md` (at freeze) |
| Result doc | `research/2026-06-12_constitutive-loop-r2_result.md` |
| Optional sim follow-on | Memristive Op14 extension spec (Phase-2b), **gated** on BIN-LOOP |

**Branch (proposed):** `analysis/2026-06-12-constitutive-loop-r2` off `main`.

**Do not:** merge kernel into `k4_tlm.py` on bench prereg alone; freeze v10 Decisions 2+4 without Grant.

---

## 10. Freeze gates (Grant)

1. Adjudicate: is LOOP GAP **THE** missing piece? (fundamentality plan §0b)
2. Pick ferrite DUT + sense geometry
3. Schedule cRIO bench time (pairs with C_eff prereg if desired)
4. Ratify R2-R threshold `B_r/B_sat ≥ 5%` or revise

---

## Cross-refs

- Three-impedance law: `research/2026-06-11_vocab-operator-unification-audit.md` §4a–4d
- Ω_freeze cascade: `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md`
- Hysteresis taxonomy: `manuscript/ave-kb/common/substrate-hysteresis-index.md`
- α boundary-energy (R1 sibling): `research/2026-06-11_alpha-boundary-energy_prereg.md`
- Dark-sector $H_*$: `research/2026-06-11_dark-sector-response-characterization.md` §3.2
- LOOP GAP: `research/2026-06-11_vocab-operator-unification-audit.md` §4c2
- v10 charter: `research/2026-06-11_chiral-vacuum-reactor-framing.md` §5.2 Decisions 2+4
- cRIO ladder: `research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md`
- D1 ruling: `research/2026-06-12_lattice-d1-adjudication-memo.md` (v10 uses diamond + srs instrument)
- Fundamentality R2: `research/2026-06-11_next-step-fundamentality-plan.md` §0b
