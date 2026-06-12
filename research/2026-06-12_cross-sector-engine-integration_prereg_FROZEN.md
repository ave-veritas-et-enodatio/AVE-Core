# Cross-sector engine integration — pre-registration (FROZEN 2026-06-12)

> **STATUS: FROZEN** — Grant session proceed directive 2026-06-12.
> **Module:** `src/ave/core/cross_sector_coupling.py`
> **Coupled hook:** `CoupledK4Cosserat.use_trilinear_converter` + `EngineConfig.use_trilinear_converter`
> **Drivers:** `cross_sector_gap1_closure.py`, `reflection_genesis_23_converter_replay.py`

**Tier:** engine-completeness — closes genesis-23 GAP-1 (bulk $V\equiv 0$ from transverse-only).
**Lane:** implementor.

---

## 0. A44 adjudication (frozen rationale)

**Question:** Is transverse→longitudinal SOURCE conversion canonical or a new postulate?

**Ruling (Grant 2026-06-09, `crystal_engine.py` header):** **Axiom consequence** — I4₁32 non-centrosymmetry gyrotropic coupling. Rendered as conserved Hamiltonian:

$$H_{\mathrm{couple}} = \tilde\kappa \int g_{\mathrm{wall}}(A)\, V\, [\mathbf w \cdot (\nabla\times\boldsymbol\omega)] \,\mathrm d^3 r, \quad \tilde\kappa = \frac{pq}{p+q} = \frac65$$

Functional derivatives give **f_V**, **f_ω**, optional **f_w** (photon depletion arm = detonation contrast only).

**Not:** genesis-24 one-way EMF pump (falsified).

---

## 1. Corpus-grep

| Prior | Relation |
|:---|:---|
| genesis-23 result | GAP-1: $\max|V_{\mathrm{inc}}|=0$ without source |
| `crystal_engine.py` ADD-2 | Gyrotropic 2-branch variant |
| `crystal_graft_v4.py` | Trilinear 3-branch with photon director = **w** |
| `k4_cosserat_coupling.py` W_refl | Impedance modulation — **not** bootstrap source |
| `op14-cross-sector-trading.md` | Reactive trading after saturation — sibling |

**Open at freeze:** genesis-23 photon-only replay with converter ON (this prereg §6).

---

## 2. Primary falsifier — GAP-1

| Metric | PASS |
|:---|:---|
| $V_{\mathrm{inc}}(t{=}0)$ | $\approx 0$ |
| $V_{\mathrm{inc}}(t_{\mathrm{end}})$ with converter ON | $> 10^{-6}$ |
| Ablation (converter OFF) | $V_{\mathrm{inc}}(\mathrm{end}) \ll$ ON arm |
| $|L|$, $H_{\mathrm{total}}$ | Bounded (no genesis-24 detonation) |

---

## 3. Implementation spec

### 3.1 `cross_sector_coupling.py`

- `trilinear_buckle_forces`, `gyrotropic_converter_forces`
- `combined_strain_amplitude(V_sq, A_cos_sq)` for **g_wall**
- `scale_cosserat_to_front` for front localization at $A\approx R_{II}$
- `KAPPA_TILDE = 6/5` (α-free)

### 3.2 Engine flags

| Flag | Default | Role |
|:---|:---:|:---|
| `use_trilinear_converter` | False | Master switch |
| `converter_mode` | `trilinear` | `trilinear` or `gyrotropic` |
| `disable_cosserat_lc_force` | True (drivers) | Avoid A28 double-count |
| `freeze_converter_wall()` | post-seed | Bilinear H_couple |

### 3.3 Step order

1. `_update_z_local_total` → 2. `k4.step()` → 3. `V_inc += f_V·dt²` → 4. Cosserat substeps + **f_ω**

---

## 4. Hypotheses

**H1:** Combined-A **g_wall** lets converter fire with K4 $V\approx 0$ when Cosserat strain peaks near $A\approx R_{II}$.

**H2:** Trilinear mode energizes $V_{\mathrm{inc}}$ without pump detonation (`photon_deplete=False`).

**H3:** Converter OFF ablation nulls GAP-1 closure.

---

## 5. Out of scope

- (2,3) self-assembly LANDED verdict
- Discrete srs genesis v11
- R2 ferrite bench

---

## 6. Deliverables

| Artifact | Path |
|:---|:---|
| Core module | `src/ave/core/cross_sector_coupling.py` |
| Coupled + VacuumEngine hook | `k4_cosserat_coupling.py`, `vacuum_engine.py` |
| Tests | `src/tests/test_cross_sector_coupling.py` |
| GAP-1 driver | `cross_sector_gap1_closure.py` |
| Genesis-23 replay | `reflection_genesis_23_converter_replay.py` |
| Result | `research/2026-06-12_cross-sector-engine-integration_result.md` |
