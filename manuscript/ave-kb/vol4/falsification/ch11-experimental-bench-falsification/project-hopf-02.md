[↑ Ch.11: Experimental Bench Falsification](../index.md)

<!-- kb-frontmatter
kind: leaf
exp-id: exp-1up5ww
status: pending
strengthens:
  - clm-wzezvt: 1.0
path-stable: "canonical HOPF-02 VNA experiment leaf; matrix A1-HOPF (HOPF-02a fab-ready, $123 BOM)"
-->

## Project HOPF-02: The S-Parameter VNA Falsification

> ↗ See also: [`AVE-HOPF/.agents/HANDOFF.md`](../../../../../../AVE-HOPF/.agents/HANDOFF.md) — canonical hardware-state holder (HOPF-02a fab-ready, $123 BOM)
>
> ↗ See also: [`_orchestration/experimental/a1-hopf/exp-a1-hopf.md`](../../../../../_orchestration/experimental/a1-hopf/exp-a1-hopf.md) — AVE-Core orchestration sub-epic for HOPF-02a fab + measurement
>
> ↗ See also: [Torus Knot Baryon Predictions](../ch12-falsifiable-predictions/torus-knot-baryon-predictions.md) — $(2,q)$ family canonical (refreshed against PDG 2024 + J^P 2026-05-18); cross-scale corroboration target

### Namespace clarification (per AVE-HOPF 2026-05-06 reconciliation)

The HOPF project line was split into three distinct namespaces:

| Namespace | Scope | Status |
|---|---|---|
| **HOPF-01** | Original pilot board (pre-2026-02-26) | **SUPERSEDED** — confound: classical multi-antenna mutual coupling between adjacent antennas on shared fixture per Grant termination experiment (AVE-HOPF commit `bd39c6d`). Per-board scored breakaway in HOPF-02 eliminates this confound. |
| **HOPF-02** | S-parameter VNA enantiomer differential (THIS leaf) | **READY FOR FAB**: HOPF-02a 5-board panel ~$123 BOM; HOPF-02b cavity-extension ~$278 BOM (gated on HOPF-02a measurement). |
| **HOPF-03** | Topological Refraction Snell Parallax (spatial-domain) | DEFERRED — separate sub-epic if pursued post HOPF-02a/b. |

### The Hypothesis

As established in Chapter 5, the physical vacuum is an **LC Resonant Network**, possessing fundamental inductance (chirality). A standard flat PCB spiral inductor or toroid generates a perfectly symmetric vector potential ($\mathbf{A}$) and magnetic field ($\mathbf{B}$) where $\mathbf{A} \cdot \mathbf{B} = 0$. It possesses zero kinetic helicity.

However, a **Hopf Coil** (a $(p,q)$ Torus Knot) forces $\mathbf{A} \parallel \mathbf{B}$. By winding a custom 6-layer PCBA where the inductive traces wrap diagonally around a toroidal core region, the inductor actively injects helicity into the vacuum, physically meshing with the network's intrinsic inductance.

**Canonical AVE-distinct prediction** (per [`AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21`](../../../../../../AVE-HOPF/docs/SESSION_STATE_2026-05-05.md)):

$$
\Delta f / f = \alpha \cdot \frac{pq}{p+q}
$$

| $(p,q)$ | Topological identification (per FI-13 RESOLVED 2026-05-18) | Predicted shift |
|---|---|---|
| $(2,3)$ | Electron trefoil (lepton family canonical per Vol 2 Ch 6) | $-11.91$ MHz |
| $(2,5)$ | Proton cinquefoil (baryon family canonical per Vol 2 Ch 2 + [`torus-knot-baryon-predictions.md`](../ch12-falsifiable-predictions/torus-knot-baryon-predictions.md)) | $-7.92$ MHz |
| $(3,5)$ | Higher-winding test mode | $-55.29$ MHz |

**SNR margin**: 60-400× NEC2 predictions per HOPF-02a PCBA design + measurement protocol.

### The Test Protocol

Design a single PCBA containing both a standard Toroid and a Hopf Coil, mathematically matched to identical classical DC inductances. Connect both to a Vector Network Analyzer (VNA) and sweep from 10 MHz to 100 MHz.

**Test methodology** (per [`AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md`](../../../../../../AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md) Phase F-G; full ave-prereg-format VNA measurement protocol to be drafted at `AVE-Core/research/2026-MM-DD_a1-hopf-hopf-02a-prereg.md` per Phase 2 gate):
1. Wind L-handed + R-handed enantiomer pair on 3D-printed mandrels per [`AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md`](../../../../../../AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md)
2. Solder SMA connectors per per-board scored breakaway (eliminates HOPF-01 multi-antenna coupling confound)
3. Measure S₁₁ for both enantiomers; record differential

### Falsification Criteria

If the vacuum is classical and linear, both coils will display identical impedance curves. However, the AVE framework strictly predicts an **Anomalous Chiral Impedance Match**. Because the Hopf coil couples perfectly to the chiral LC metric, it acts as a topological antenna, minimizing reactive VAR reflections and exhibiting an anomalously deep $S_{11}$ notch at the predicted $\Delta f$ shifts above.

**Standard EE counterfactual**: free-space wire helices have NO chirality-dependent resonance shift. Mirror-image helices have IDENTICAL $S_{11}$. No chirality dependence in classical Maxwell.

### A1 cascade impact (per Matrix 1 cascade column)

A1-HOPF tests the $(2,q)$ family at EE scale. The same $(2,q)$ classification underlies:

- **C8-BARYON-LADDER** (FULL PASS at $-0.002\%$ proton, 6/6 $J^P$, PDG 2024 anchor 2026-05-18) — hadronic-scale validation
- **C3-MUON-DELTA** (PASS-conditional $+502 \times 10^{-11}$ forward, +4.59σ above Fermilab e+e-; driver canonical 2026-05-19) — lepton-g-2-scale validation
- **C10-MUON-LIFE** ($(2,3)$+Cosserat lepton ladder canonical per FI-13 RESOLVED)

A1-HOPF passing at EE scale → cross-scale corroboration of $(2,q)$ topological classification. A1-HOPF failing at EE scale → cascade-impact requires structural revision of $(2,q)$ classification despite C8 hadronic-scale confirmation.

### Outcome adjudication (Phase 3 of sub-epic [`exp-a1-hopf.md`](../../../../../_orchestration/experimental/a1-hopf/exp-a1-hopf.md))

| Outcome | Interpretation |
|---|---|
| **A**: Δf matches AVE prediction within NEC2-class precision | $(2,q)$ family confirmed at EE scale; cross-scale corroboration of C8 + C3 + C10 |
| **B**: Δf detected but magnitude differs from prediction | Partial — confirms chiral-coupling exists; magnitude requires structural revision (Cosserat coefficient or $(p,q)$ selection rule) |
| **C**: No Δf detected within NEC2 SNR | A1 family falsified at EE scale → cascade-impact on C8 + C3 + C10 |
| **D**: Confound (e.g., classical multi-antenna coupling à la HOPF-01) | Re-design needed; escalate to HOPF-02b cavity variant (~$278 BOM) |

### Engineering substrate

| Asset | Location |
|---|---|
| KiCad PCB | [`AVE-HOPF/hardware/hopf_02a.kicad_pcb`](../../../../../../AVE-HOPF/hardware/hopf_02a.kicad_pcb) |
| Gerbers + drill files | [`AVE-HOPF/hardware/Gerbers_hopf_02a/`](../../../../../../AVE-HOPF/hardware/Gerbers_hopf_02a/) (15 files; Phase B export commit `86d1a00`) |
| BOM (~$123) | [`AVE-HOPF/hardware/hopf_02a_BOM.md`](../../../../../../AVE-HOPF/hardware/hopf_02a_BOM.md) |
| JLCPCB ordering | [`AVE-HOPF/hardware/hopf_02a_ORDERING.md`](../../../../../../AVE-HOPF/hardware/hopf_02a_ORDERING.md) (250×185 mm panel + 4 v-score lines + ±0.1 mm drill tol) |
| Test procedure | extract Phase F-G from [`AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md`](../../../../../../AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md); full ave-prereg-format pre-reg drafts at Phase 2 gate |
| Assembly guide | [`AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md`](../../../../../../AVE-HOPF/hardware/hopf_02_ASSEMBLY_GUIDE.md) (376 lines; 3D-print mandrel + wire-winding + Phase F-G measurement) |
| DRC report | [`AVE-HOPF/hardware/hopf_02a_DRC.rpt`](../../../../../../AVE-HOPF/hardware/hopf_02a_DRC.rpt) (251 violations are `lib_footprint_issues` warnings for local HOPF02 footprint library; no copper/drill clearance issues per Phase B verification) |
| Python KiCad emitter | [`AVE-HOPF/hardware/hopf_02_generate_kicad_pcb.py`](../../../../../../AVE-HOPF/hardware/hopf_02_generate_kicad_pcb.py) (canonical fab path) |
| NEC2 prediction | [`AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21`](../../../../../../AVE-HOPF/docs/SESSION_STATE_2026-05-05.md) |
| 89 fast tests passing | HOPF-02 geometry validation (SMA convention, z-values, hole counts, L↔R mirror exactness) |
| Canonical state | [`AVE-HOPF/.agents/HANDOFF.md`](../../../../../../AVE-HOPF/.agents/HANDOFF.md) |

### Status (2026-05-20 EOD per `exp-a1-hopf-repo-audit.md`)

**HOPF-02a DESIGN-COMPLETE; PHASE 0a artifact-generation pending**. Per AVE-HOPF HANDOFF.md: *"Next gate: physical fab order for HOPF-02a (user action; design package complete; Python KiCad emitter is the canonical fab path)."*

Per the Phase A repo audit at [`_orchestration/experimental/a1-hopf/exp-a1-hopf-repo-audit.md`](../../../../../_orchestration/experimental/a1-hopf/exp-a1-hopf-repo-audit.md), three blockers remain before JLCPCB submission:

1. **🔴 BLOCKER-1** (5 min): Export HOPF-02a Gerbers + drill files from `hopf_02a.kicad_pcb` via `kicad-cli pcb export gerbers/drill`. Currently `AVE-HOPF/hardware/Gerbers/` contains HOPF-01 Gerbers only.
2. **🔴 BLOCKER-2** (15 min): Draft `AVE-HOPF/hardware/hopf_02a_ORDERING.md` with v-score spec. Current `ORDERING.md` is titled "HOPF-01 JLCPCB Ordering Guide" with 160×120 mm dimensions; HOPF-02a needs 250×185 mm panel with 4 v-score lines.
3. **🔴 BLOCKER-3** (~1 hour, Phase 2 gate only): Draft `ave-prereg`-format pre-registration for VNA measurement. NOT blocking for Phase 0 fab; blocks Phase 2 bench-fire.

Per audit Axis 1 ATTN-2: the root cause of citation drift between AVE-Core canonical leaves and AVE-HOPF hardware artifacts is the AVE-HOPF `hardware/` directory mixing HOPF-01 and HOPF-02a files at the same hierarchy level. ~30 min reorganization recommended (R1.1).

Sub-epic tracking: [`_orchestration/experimental/a1-hopf/exp-a1-hopf.md`](../../../../../_orchestration/experimental/a1-hopf/exp-a1-hopf.md) Phase 0a + 0b.

---
