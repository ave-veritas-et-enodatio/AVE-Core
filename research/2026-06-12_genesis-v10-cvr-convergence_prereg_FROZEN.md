# Genesis v10 — CVR Convergence Pre-Registration (FROZEN 2026-06-11)

> **STATUS: FROZEN.** Ratified by Grant session 2026-06-11 ("snap it is; let's go").
> **Charter:** `research/2026-06-11_chiral-vacuum-reactor-framing.md` §5 — all Decisions 1–5 closed.
>
> **Gates satisfied at freeze:**
> 1. v9 Phase-2 production bins landed (P5 FAIL; P6 partial CVR-SET — honest baseline).
> 2. D1 adjudicated B-primary / A-partial; diamond engine + srs instrument.
> 3. Decisions 2b (σ+snap), 4 (equal tri-channel χ + H_* ON), 5 (Ω_freeze IC + ablation).
> 4. CVR-SET failure ladder + P6 thresholds inherited from v9 Phase-2 (no ⟨…⟩ placeholders).

**Tier:** v10 convergence build — first run asking the lattice to **make** the reactor (not host a planted one).  
**Lane:** implementer. Extend v9 Phase-2 platform; do not reopen D1 substrate ruling.

---

## 0. Grant decisions (frozen kernel spec)

| ID | Ruling | v10 implementation |
|---|---|---|
| D1 | B-primary / A-partial | srs cells + diamond control; engine substrate z=4 diamond |
| D2 | **σ + rate-gated snap** | Op14 + Op3 **plus** snap on yield crossing |
| D3 | Phase-1/2 executed | Inherit P6 bins, A1–A4 controls |
| D4 | **χ_EM=χ_shear=χ_bulk=χ** + **H_* ON** | Tri-channel shock equality; saturation ride per channel |
| D5 | **Ω_freeze IC ON** + Ω-free ablation | Cosmic IC from cascade; ablation control required |

---

## 1. Corpus-grep (ave-prereg Step 1)

**Target:** Under **snap + tri-channel dissipation + Ω_freeze IC**, does a **linear precursor**
on srs **self-trap** into **CVR-SET** (formed + set + geometry-handed)?

| Prior item | Relevance | v10 relation |
|---|---|---|
| `chiral_lattice_vector_sat.py` + Phase-2 result | Op14/Op3 reactive trap; partial CVR-SET | **Platform base** — extend, do not replace |
| `unified_genesis_engine.py` snap | `chi_shock`, latent tally, rate-gated crossing | **Snap semantics reference** — port to discrete TLM |
| `sonic_horizon_flow.py` | Scalar `chi_shock` sweep discipline | χ sweep values |
| `omega-freeze-cosmic-grain-cascade.md` §2 | $u_0^*$, $\hat\Omega_{\mathrm{freeze}}$, $\mathcal{J}_{\mathrm{cosmic}}$ | Ω_freeze IC arm |
| `dark-sector-response-characterization.md` §3.2 | $H_{\mathrm{EM}}$, $H_{\mathrm{shear}}$, $H_{\mathrm{bulk}}$ | Channel saturation ride at readout |
| `tau-relax-derivation.md` §3–§4 | Level 2 memristive / BEMF freeze | Rate-gate for snap firing |
| Genesis v6–v9 record | No mass without lock/snap | **Motivating falsifier** — v10 tests snap path |

**Genuinely open:** First **snap-equipped** discrete srs genesis run with Ω_freeze IC.

---

## 2. Physical picture (Step 1.5)

- **Substrate:** periodic srs net (z=3 instrument), scatter+connect vector-TLM.
- **Medium:** Op14 $z_{\mathrm{local}}(A^2)$ + Op3 bond reflection (**σ**). On node
  saturation **crossing** ($A^2$ rising through $A_{\mathrm{yield}}$), **rate-gated snap**
  removes fraction $\chi$ of excess crossing KE **one-way** into latent ledger (per channel,
  **equal** $\chi$). This is the irreversible leg Decision 2b adds.
- **Ω_freeze IC (D5):** At $t=0$, imprint cosmic chirality bias on the lattice state per
  cascade constants ($u_0^*$ from `constants.py` / CODATA chain; $\mathcal{J}_{\mathrm{cosmic}}$
  direction tagged apparatus-floor). **Ω-free ablation:** same run grid with IC arm disabled —
  only κ_chiral geometry; CVR-SET must **not** promote on Ω-free alone if IC is load-bearing.
- **Seed (CP8):** Bare linear transverse packet, zero injected helicity, direction only.
- **Reads:** Interior + phase-resolved; reactance pairs `V_{\mathrm{inc}}/\omega` and
  $\Phi_{\mathrm{link}}/\dot\omega$ over window; per-channel $H_*$ diagnostics at saturation.
- **Γ / ledger:** Snap + χ are **one-way**; must not count reactive exchange as genesis.
  Tag `E_{\mathrm{diss,snap}}` vs `Q_{\mathrm{react}}$ separately.

---

## 3. Platform specification (implementor MUST document)

Extend `chiral_lattice_vector_sat.py` → **`chiral_lattice_v10.py`** (or sibling module).

### 3.1 Inherited from v9 Phase-2 (unchanged)

- Op14: $S=\sqrt{1-A^2}$, $z_{\mathrm{local}}=1/\sqrt{S}$.
- Op3 @ CONNECT bond mixing when $z_{\mathrm{local}}$ varies spatially.
- P6 launch: `launch_linear_packet`; `κ_chiral = 0`; four-cell srs × direction grid.
- Charge proxy: window-weighted `ring_writhe` (v9 frozen v1).

### 3.2 NEW — rate-gated snap (Decision 2b)

On each node per step, after Op14 amplitude update:

1. **Yield surface:** $A_{\mathrm{yield}} = \sqrt{2\alpha}$ (three-regime knee; import `ALPHA`
   from `ave.core.constants`).
2. **Crossing detect:** node newly above yield: $A^2_{t} \geq A_{\mathrm{yield}}^2$ and
   $A^2_{t-1} < A_{\mathrm{yield}}^2$.
3. **Rate gate:** snap fires only if $|dA^2/dt| \geq \dot A^2_{\min}$ OR crossing persists
   longer than $\tau_{\mathrm{relax}}$ (use $\tau_{\mathrm{relax}} = \ell_{\mathrm{node}}/c_0$
   from `L_NODE`, `C_0` — apparatus-floor tagged).
4. **Latent release:** on fire, remove fraction $\chi$ of local excess KE above yield reference
   from **each channel equally** ($\chi_{\mathrm{EM}}=\chi_{\mathrm{shear}}=\chi_{\mathrm{bulk}}=\chi$).
   Increment `E_diss_snap` ledger; do not return to field without explicit heal knob (default heal OFF).
5. **Ablations:** `snap=OFF` recovers v9 Phase-2 reactive class for matched comparison.

### 3.3 NEW — tri-channel χ + H_* (Decision 4)

- **χ sweep (production):** $\chi \in \{0, 0.25, 0.5, 1.0\}$ — **same value** on all three channels.
- **H_* at readout:** report $H_{\mathrm{EM}}=(1-A^2)^{-1/2}$, $H_{\mathrm{shear}}=(1-A^2)^{1/4}$,
  $H_{\mathrm{bulk}}$ per dark-sector §3.2 at peak-$A$ sites (diagnostic; not fit targets).
- **Scalar fallback:** if implementor v1 uses single `chi_shock` internally, enforce
  $\chi_{\mathrm{EM}}=\chi_{\mathrm{shear}}=\chi_{\mathrm{bulk}}$ at API boundary.

### 3.4 NEW — Ω_freeze IC + ablation (Decision 5)

- **IC ON (default production):** apply cosmic chirality bias at init — document exact field
  imprint in result doc (must cite cascade leaf; no hard-coded α fit).
- **Ω-free ablation cell:** `omega_freeze_ic=False` on otherwise identical srs-R:+z cell.
- **Promotion rule:** CVR-SET on IC ON **without** Ω-free showing SET-ACHIRAL or DISPERSES
  does **not** alone prove IC is load-bearing; report both.

### 3.5 Diagnostics (required)

- `max(A²)`, yield-crossing count, `E_diss_snap` total, χ used.
- Reactance-pair traces (last 100 steps of drive-off window).
- `max(|Γ|)` on bonds; Op3/Op14/snap/IC ablation flags per run.

---

## 4. Hypotheses

**H10 (snap enables set leg):** Rate-gated snap + equal χ **increases** drive-off retention
vs v9 Phase-2 reactive class on ≥1 srs cell (matched-baseline ≥2× improvement target inherited).

**H11 (Ω_freeze IC):** Canonical IC ON **biases** chirality concordance (P6-C) vs Ω-free ablation
without injecting CP (consistency-class on IC; not SM-distinct alone).

**H12 (CVR-SET):** Conjunction P6-L + P6-C + P6-D on srs with snap+IC — **emergence-class**
primary claim. Falsified by BIN-D, BIN-T, or SET-ACHIRAL on all production cells.

---

## 5. Frozen predictions (inherit v9 P6 + v10 extensions)

### P6 — genesis-by-precursor (PRIMARY — thresholds unchanged from v9 Phase-2)

| Criterion | Threshold |
|---|---|
| **P6-A** | amp `{0.25, 0.5, 1.0}` |
| **P6-S** | ≥800 steps; plateau last 100 |
| **P6-L** | $r_{\mathrm{rms}}$ change <5% over last 100 steps |
| **P6-C** | $\mathrm{sign}(\Delta\theta)$ tracks $\mathrm{sign}(\mathrm{writhe}\times\mathrm{dir})$; diamond ≤5% srs |
| **P6-D** | Drive-off ≥200 steps; $E_{\mathrm{loc}} \geq 50\%$ peak; $r_{\mathrm{rms}}$ not doubling |
| **P6-G** | L≥10 srs production; L=8 smoke tagged SMOKE-ONLY |

**Outcome bins:** CVR-SET / TRANSIENT / DISPERSES / SET-ACHIRAL — same assignment rules as v9.

**Matched baseline:** srs snap+IC ON must exceed **≥2×** energy retention vs (diamond, Op14-OFF,
Op3-OFF, snap-OFF, Ω-free) on same amp envelope.

### P6-χ — snap sweep gate (v10 NEW)

| Gate | Criterion |
|---|---|
| **P6-χ-MONO** | For fixed cell, $E_{\mathrm{diss,snap}}$ non-decreasing with χ (0→1) |
| **P6-χ-RET** | Best srs cell $e_{\mathrm{driveoff}}$ at χ=0.5 or 1.0 ≥ v9 Phase-2 best (0.514) |

Failure of P6-χ-RET weakens H10 but does not auto-void CVR-SET if another χ lands BIN-G.

---

## 6. Controls (v9 + v10)

| Control | Purpose |
|---|---|
| srs-R / srs-L × ±z | A2 four-cell |
| Diamond | Achiral null |
| `κ_chiral = 0` | Geometry-only chirality |
| Op14 OFF / Op3 OFF | Matched baseline |
| **snap OFF** | v9 reactive class comparison |
| **Ω-free IC** | D5 ablation |
| **χ=0** | Elastic crossing control (no one-way dissipation) |

---

## 7. Discrimination (`ave-discrimination-check`)

| Element | SM | AVE-distinct? |
|---|---|---|
| Ferrite-like hysteresis | SM ferromagnetism | N/A — discrete snap, not B-H bench |
| Snap + χ dissipation | Standard shock physics exists | **Partial** — interpretive mass bridge |
| Ω_freeze IC | Not SM | **Framing** — cosmic initial data |
| CVR-SET promotion | Not SM genesis | **AVE-specific** — requires full bin + baselines |

**No CVR-SET promotion** without matched-baseline 2× and Ω-free ablation reported.

---

## 8. Kill conditions

1. CVR-SET claimed with snap OFF only (mislabeled v9 rerun).
2. χ_EM ≠ χ_shear ≠ χ_bulk without tagged apparatus ablation.
3. Fit `B_r` or $m_e$ from snap ledger to target mass (driver honesty).
4. P5-pass + BIN-D reported as genesis (Rule 11).

---

## 9. Implementor deliverables

| Artifact | Path |
|---|---|
| Module | `src/ave/core/chiral_lattice_v10.py` |
| Tests | `src/tests/test_chiral_lattice_v10.py` (smoke ≤3 min) |
| Driver | `src/scripts/vol_1_foundations/chiral_lattice_v10_genesis.py` (`--smoke`) |
| Result | `research/2026-06-12_genesis-v10-cvr-convergence_result.md` |
| JSON | `assets/sim_outputs/genesis_v10_cvr_convergence.json` (gitignored) |

**Branch:** `analysis/2026-06-12-genesis-v10-cvr-implementor` off `main` (after PR #206 merge).

**Do not:** merge to main; edit orchestration on implementor branch; claim CVR-SET in driver prints.

---

## Cross-refs

- Charter: `research/2026-06-11_chiral-vacuum-reactor-framing.md` §5
- v9 Phase-2 FROZEN: `research/2026-06-12_genesis-v9-phase2-prereg_FROZEN.md`
- v9 Phase-2 result: `research/2026-06-12_genesis-v9-phase2_result.md`
- R2 FROZEN: `research/2026-06-12_constitutive-loop-r2-prereg_FROZEN.md`
- D1 memo: `research/2026-06-12_lattice-d1-adjudication-memo.md`
