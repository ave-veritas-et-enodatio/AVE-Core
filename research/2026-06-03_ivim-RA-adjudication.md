# IVIM bench — R-A adjudication + the V_yield per-node/apparatus conflation (2026-06-03)

**Adjudicated by Grant 2026-06-03: R-A.** The IVIM recommended-geometry signal is
WKB-suppressed; the bench is an interferometric (scalar-phase) precision measurement,
not a 70σ APD photon-counter. Ch 12/14/23/28 walk back to the Phase-A′-C′ reality;
the V⁴ law and the 8.38×10¹² AVE-vs-QED coefficient ratio survive; the **magnitude +
detection mode** change.

This doc is the adjudication record + the mapping-audit findings that grounded it.
It also surfaces a **bigger, verified, corpus-wide finding** (§4) that is FLAGGED for
Grant, not fixed here.

---

## 1. The decision context (Camp-A/Camp-B contradiction)

The IVIM corpus contradicts itself on the headline reflectance Γ by 15–30 OOM
(`AVE-Bench-VacuumMirror/docs/analysis/2026-06-03_ivim_adversarial_reverification.md` §2):

- **Camp A** (Ch 01 / Ch 04 / Phase-A′-C′): recommended geometry is WKB-suppressed →
  Γ ~ 10⁻²³…10⁻⁴¹; *"does not produce a detectable signal under linear AC small-signal
  response."* → PVLAS-class interferometer.
- **Camp B** (Ch 12/14/23/28): Γ = 1.94×10⁻¹¹, 70–1025σ APD photon-counting, via an
  N²-Bragg gain on a single-element value computed at R_tip = d_gap = 10 nm.

What survives either way (both re-derived clean, zero free parameter): the **V⁴ scaling**
and the **8.38×10¹² discrimination ratio**. R-A keeps both and moves to the honest readout.

---

## 2. Mapping/coordinate audit (per `phase-space-coordinate-check` + `ave-ee-intuition-summary`)

Five overloaded symbols audited for conflation:

| Symbol | Canonical meaning | IVIM usage | Verdict |
|---|---|---|---|
| **Γ** | Γ=−1 saturation/TIR boundary (node's own wave fully reflects at A→1) | optical reflectance \|r\|² of the probe laser off the bias ε-step | **Symbol collision, math clean.** Gap sits at A~10⁻⁴, nowhere near Γ=−1. |
| **A** | per-node saturation amplitude = E_local/E_yield (A_field convention, `vol4/claim-quality.md:1114`) | `analytical_gamma_v_sweep.py:59` = E_local·ℓ_node/V_YIELD | **CLEAN** — geometry-aware, canonical. |
| **V_yield** | **per-node** yield: 43.65 kV across one ℓ_node → E_yield = 1.13×10¹⁷ V/m | swept as the **gap** voltage ceiling | **Math clean in the script; FRAMING CONFLATED in the leaf — see §3.** |
| **WKB / Bragg / impedance** | three distinct effects in direct tension via d_gap | all present | clean but the tension is the load-bearing R-A argument. |
| **interferometric / PVLAS** | scalar phase (isotropic δε) vs birefringence (anisotropic δε) | "PVLAS-class interferometric phase" | **Genuine conflation — pin readout (see §5).** |

**The geometric over-constraint (the real R-A argument):** you cannot have R_tip ≪ d_gap
(field-model valid) AND d_gap ≪ λ (no per-element WKB suppression) with R_tip ≥ ~1 nm.
The script's own validity flags confirm: d_gap=1µm → field-model OK but exp(−k₀d_gap)=exp(−12.6)
WKB-killed; d_gap=10nm → no WKB suppression but R_tip=d_gap field-model invalid. Camp B
lives in the validity hole. This is independent of every symbol conflation, so it makes R-A
unambiguous.

---

## 3. Root cause — the canonical leaf conflates per-node V_yield with the gap voltage

`vol4/falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md` plugs the
**applied gap voltage** directly into the **per-node** kernel:

- :38 `ε_eff(V) = ε₀√(1−(V/V_yield)²)`, :57 *"as the experimental gap voltage V → 43,650 V …
  Z_local → ∞"*, :71 *"Γ → 1 (perfect reflection)"*, :77 *"sweeps exactly up to this limit,"*
  :84-85 *"100 µm gap … 35–43 kV sweep."*

At 43 kV across 100 µm the gap field is ~4.3×10⁸ V/m, so the **actual per-node strain is
A = E/E_yield ≈ 3.8×10⁻⁹**, not V/V_yield ≈ 0.99. The "Γ→1 perfect mirror at 43 kV" is
overstated by ~(d_gap/ℓ_node) ≈ 2.6×10⁸. **This leaf is the source of the Camp-A/Camp-B
contradiction:** Camp B inherited the leaf's V/V_yield; Camp A (and the script, :59) used the
correct E_local/E_yield. Q-G42 is the only node that recognized V_yield is per-node.

---

## 4. ⚑ BIGGER FINDING (verified, FLAGGED for Grant — NOT fixed here)

The per-node/apparatus conflation is **corpus-split**, not IVIM-local:

- **Honest/corrected camp:** `trampoline-framework.md:439` (V_yield^apparatus = E_yield/G_geom,
  per Q-G42); `vol4/claim-quality.md:393` (*"far beyond current laboratory capability without
  resonant local enhancement"*); `vol4/claim-quality.md:79` (asymptotic, not literal);
  `ybco-phased-array.md:8` INVALIDATED for the per-node-as-apparatus misuse.
- **Conflated/uncorrected camp:** `vacuum-impedance-mirror.md` (§3); `measurement-hierarchy-snr.md:66`
  + `universal-saturation-kernel-catalog.md:72` (*"bench-measurable at ~30 kV bias"*, no G_geom caveat).

**The PONDER-05 consistency-vs-emergence question (load-bearing, NOT settled):** PONDER-05 is
**DC-biased quartz** (`op14-local-clock-modulation.md:106`, `vol9/ch5-ac-electrical-characteristics:35`)
at "V_DC/V_yield = 0.687" → 27.4% ε-collapse. A 27.4% collapse needs A=0.687, i.e. local field
0.687×E_yield ≈ 7.8×10¹⁶ V/m — unreachable at 30 kV across macroscopic quartz absent G_geom ~ 10⁶.
Two readings, and only Grant + a PONDER-side trace can decide:
  1. **Vacuum-kernel reading (emergence):** the quartz is the apparatus; the vacuum's ε collapses —
     but then it needs a real resonant-enhancement geometry to reach A=0.687, which the "30 kV"
     framing omits. Same conflation as §3.
  2. **Material reading (consistency-class):** "V_DC/V_yield" uses a *quartz-material* saturation
     voltage, and the 27.4% C-collapse is quartz's ordinary voltage-coefficient-of-capacitance
     (every Class-II ceramic does this — `translation-circuit.md:456`). If so, PONDER-05 is a
     standard material effect *analogized* to the substrate kernel, NOT a forward vacuum
     discriminator.

**Impact on the kernel-convergence narrative** (`_orchestration/…revamp…md` §10, "three transducers
of one kernel"): if R-A holds (IVIM → unreachable photon-count, now interferometric) and PONDER-05
is reading 2, then two of the three transducers are consistency-class / unreachable-as-framed, and
**Q-G42 (the V²-coefficient SIGN test) is the one clean forward discriminator** of the saturation
kernel. That is a material deflation of the convergence story and must be Grant-adjudicated before
any corpus surgery.

**The mechanical-grain "fourth transducer" (Grant 2026-06-03, scoped under `ave-prereg`):** Grant's
instinct — that the quartz *crystalline structure / grain* couples the piezo effect to the
lattice/vacuum mechanically, distinct from the dead DC-field channel — was scoped. Outcome at
[`research/2026-06-03_piezo-mechanical-fourth-transducer-prereg.md`](2026-06-03_piezo-mechanical-fourth-transducer-prereg.md):
**green-field but blocked.** The mechanical channel exists *only* in the LOCKED (finite-strain
Lagrangian) reading of the substrate — which is Grant's own unresolved doc-109 trampoline question
(`research/_archive/L3_electron_soliton/109_elastic_substrate_finite_strain_investigation.md`,
canonical engine = SLIDING/Eulerian → a mechanical strain couples to the kernel only via the piezo
E-field it generates = the dead field channel). Even granting LOCKED, A_mech ~ ν_vac·ε_mech ~ 10⁻⁶
(δε/ε ~ 10⁻¹³…10⁻⁸ near fracture) — ~10⁵× the field channel but still ≪ 0.687; grain-dependence
(κ_quality) is the only discriminator and its materials-map is open; the natural locked coefficient
(κ_entrain) is categorically excluded from the reactive kernel. **Not a rescue; ~~gated on the
foundational locked-vs-sliding fork, not a bench choice~~ → CORRECTED 2026-06-03 (full doc-109 read,
Rule 12): RULED OUT, not gated — the fork was reframed (doc 109 §13 boundary-envelope, impedance-only,
Grant-confirmed) AND closed at v14 Mode I (doc 113; Master Equation FDTD hosts the breathing soliton,
K4-TLM cannot). The geometric-locked channel was reframed-against + empirically unneeded. Q-G42 stays
the one clean discriminator.**

> **DEPENDENT (2026-07-02, KEEP-BOTH cross-ref).** The Cleave-01 plate-displacement coupling is a
> DEPENDENT of this sliding-vs-locked fork — but via a DIFFERENT channel than the piezo E-field
> "RULED OUT, not gated" above. Doc-109's closure is scoped to the piezo E-field transducer; the
> Cleave **registry-pump** reading (screw-registry spectral flow / boundary linking) is a separate
> channel. Grant ruled (b) 2026-07-02 — reopen the sliding-vs-locked question *for the registry-pump
> reading specifically* and let the **engine** adjudicate (which reading reproduces the OA anchor).
> The engine returned **NULL-DERIVED** ($C_{slide}=C_{lock}=0$, operator-derived construction). This
> is NOT a reconciliation of the two channels (flag-don't-fix — different transducers):
> [`research/2026-07-02_cleave-coupling-derivation_adjudication.md`](2026-07-02_cleave-coupling-derivation_adjudication.md) §f.

---

## 5. The R-A re-freeze plan (queued, not executed)

1. **Detection mode → interferometric** (scalar phase Δφ at STM geometry), not APD photon-counting.
2. **Operating point → breakdown-limited, not V_yield.** At the apparatus scale 43.65 kV is not a
   ceiling (A~10⁻⁹–10⁻⁵); the real ceiling is electrode field-emission/vacuum breakdown. Since
   Γ ∝ V⁴, push V higher than 43.65 kV until breakdown. Kill the "sweeps up to V_yield" framing.
3. **Pin the readout (new discriminator candidate):** is δε isotropic (→ scalar phase, interferometer)
   or anisotropic (→ birefringence, PVLAS-style)? The kernel keys off |E| (isotropic → interferometer).
   QED's Euler-Heisenberg vacuum IS birefringent in a background field — so the **birefringence
   pattern vs QED is a candidate structural discriminator** (pattern, not 12-OOM coefficient).
4. **Notation hygiene:** keep "Γ" = optical reflectance distinct from Γ=−1 in the leaf.

## 6. Propagation queue (BLOCKED on §4 adjudication for the corpus-wide sites)

IVIM-local (proceed once R-A re-freeze authorized):
- `vacuum-impedance-mirror.md` — leaf re-scope (V/V_yield → E_local/E_yield; Γ→1 claim; detection mode).
- `vol4/claim-quality.md` clm-5s5b0d — Γ(V) entry re-scope.
- `cosmological-constant-closure.md:127` — Γ_bench headline (drop/flag the 1.94×10⁻¹¹-at-43.65kV route).
- closure-roadmap §0.5 — new IVIM walk-back entry (Type: detection-mode re-scope + per-node correction).
- AVE-Bench-VacuumMirror `analysis/2026-06-03-ivim-harden` — leaf re-freeze (Ch 12/14/23/28).
- NOTE: no IVIM row in `divergence-test-substrate-map.md` (claim lives in vol4/claim-quality, clm-5s5b0d).

Corpus-wide (BLOCKED on Grant's §4 call):
- `measurement-hierarchy-snr.md:66` + `universal-saturation-kernel-catalog.md:72` — G_geom caveat.
- PONDER-05 consistency-vs-emergence resolution + the kernel-convergence-narrative re-scope (epic §10).

## 7. Recurring-hazard note

Per-node-V_yield-as-apparatus-voltage has now bitten **3×** this session (Q-G42 caught it; IVIM leaf +
PONDER-05 framing did not). Candidate for a canonical note or a skill (`substrate-native-check`-adjacent:
"normalize the kernel argument by E_yield = V_yield/ℓ_node at the LOCAL field, never V_apparatus/V_yield").
