[↑ Ch.12 Falsifiable Predictions](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-acgyr1]
-->

# Chiral Mechanical & Acoustic Gyrotropy on srs-z3 — a Geometry-Fixed, Parity-Odd, Below-Bound Forward Statement

<!-- claim-quality: clm-acgyr1 -->

> **Consistency-vs-emergence tag — read first.** This leaf is **CONSISTENCY / FORM-class**.
> Its AVE-distinct content is the **existence + PARITY + geometry-fixedness** of a chiral
> `k`-linear gyrotropy that the ratified chiral **srs-z3** carrier PERMITS and the historical
> centrosymmetric **diamond** carrier structurally **FORBIDS**. The **magnitude is an ECHO** and
> is **negligible** at accessible scales (`δ_chiral ≈ 1.7×10⁻⁹·(qℓ_node)` at optical, `~11 OOM`
> below current LIV/SME bounds) — this is **NOT a near-term falsifier**. It is surfaced honestly
> as a genuine carrier-native prediction the diamond could not host, living far below bounds.
> α-CLEAN (dimensionless ratios only; no CODATA input, no SI substitution).

The two srs-z3 elastic-tensor arcs of 2026-07-04 (PRs #508, #515) each measured, in independent
sectors, the same underlying object: a **chiral cross-coupling permitted by the non-centrosymmetric
`I4₁32` point group `432`** and forbidden by the centrosymmetric diamond point group `m3̄m`. This
leaf documents it as one consistency-class forward statement with two faces.

## §1 — The mechanical face (couple-stress / static elastic tensor, PR #508)

The 48×48 chiral micropolar Bloch eigensolve on the srs-z3 net (`src/ave/core/micropolar_bloch.py`)
finds a **nonzero chiral translation↔rotation cross-coupling pseudo-tensor `B`**:

| Property | Value / statement |
|---|---|
| `B` on srs (right, 432) | `B_signed ≈ −5.995×10⁻³` (invariant up to `~2.3×10⁻²` over `ρ∈[0.5,10]`) — nonzero |
| Enantiomorph parity | `B_signed(left) = +5.995×10⁻³` — exact sign flip (`M_tr(left)=−M_tr(right)`, `R+L=0` to `2.8×10⁻¹⁶`) — **parity-odd** |
| Diamond null-control (`m3̄m`) | `B ≈ 7.0×10⁻¹⁹` — machine null; **centrosymmetry FORBIDS** the piezo-class pseudo-tensor |
| Channel | rides the **`σ^A` asymmetric-stress / lever-arm** channel (`B_σA ≈ 1.05×10⁻¹`) — the couple-stress `κ_rot`/`μ` channel is `~30 OOM` smaller (`B_μ ≈ 5.4×10⁻³³`) |
| Provenance | **geometry-fixed** — the lever arm is set by the Poisson-disk node radius + bond length; the couple-stress `γ` by canon (`ℓ_c²=γ/G=6`). **NO new stiffness knob.** |

The chirality is **non-local**: the single srs node is coplanar (the trivalent star has
`det(bond dirs) = 0`); the handedness lives in how consecutive bond-planes rotate along the `4₁`
screw axis (girth-10 helical connectivity). `B` emerged from the FULL lattice sum and vanished
identically on diamond. It is the **mechanical sibling of the A44 EM gyrotropic converter**
(`src/ave/core/cross_sector_coupling.py:5-10`, an "Axiom-1 non-centrosymmetry consequence"),
realized as the `σ^A` lever-arm channel.

## §2 — The photon / acoustic face (Bloch dispersion, PR #515)

The Lorentz-on-srs 24×24 translational-sector Bloch eigensolve
(`src/scripts/vol_4_engineering/lorentz_on_srs.py`) reads the **`k`-linear rotatory
(acoustic-activity) term** — the k-space dispersion face of the same pseudo-tensor:

| Lattice | `B_signed` (k-linear rotatory) | Reading |
|---|---|---|
| srs (right, 432) | `−4.30×10⁻⁴` | nonzero — 432 permits acoustic activity (one of the 15 gyrotropic classes) |
| srs (left, 432) | `+4.30×10⁻⁴` | exact sign flip (parity-odd, resid `5.6×10⁻¹³`; `detect_symmetry_forced_zero` harness) |
| diamond (`m3̄m`) | `+4.8×10⁻³⁷` | machine null — centrosymmetry forbids it |

**Honest magnitude at physical scale (not waved):**

| Scale | `qℓ_node` | `δ_chiral ∼ |B_signed|·(qℓ_node)` |
|---|---|---|
| optical (633 nm) | `3.83×10⁻⁶` | **`1.65×10⁻⁹`** |
| X-ray (1 Å) | `2.43×10⁻²` | `1.04×10⁻⁵` |

The chiral term is **`k`-LINEAR** (vs the even-in-`k` quartic anisotropy `clm-k4d4ph` /
`clm-yr6tu4`), so it dominates the quartic at long wavelength — but its coefficient is tiny:
`δ_chiral(optical) ≈ 1.7×10⁻⁹` is `~11 OOM` below the `~10⁻¹⁹`–`10⁻²⁰` SME cavity bounds. **Negligible
at optical/X-ray scales, quantified.**

## §3 — What is AVE-distinct, and what is not

- **AVE-distinct (FORM/parity):** a vacuum optical-activity / acoustic-gyrotropy that the
  centrosymmetric diamond instrument structurally **cannot host** but the ratified chiral srs-z3
  carrier does — parity-odd (enantiomorph sign-flip), geometry-fixed (zero new knobs). This is a
  genuine carrier-native forward statement, distinct from BOTH the parity-EVEN quartic
  (`clm-k4d4ph` / `clm-yr6tu4`) and the field-INDUCED birefringence coefficient (`clm-pp3qwf`).
- **DISTINCT from the reciprocal optical-activity leaf (`clm-fofwr1`).** That leaf's `±75.46°`/unit
  is a lossless RECIPROCAL-Faraday gyrator keyed on ring-WRITHE with an `ETA_ROT_PER_WRITHE`
  engineering decree (magnitude NOT bankable, `~40 OOM` over bound). THIS leaf is a `k`-linear
  gyrotropic-dispersion pseudo-tensor sourced by the lattice point group, geometry-fixed, `~11 OOM`
  below bound. Different mechanism, different (much smaller) size.
- **NOT AVE-distinct (magnitude):** the coefficient is an ECHO (a lattice-geometry number), and the
  physical `δ_chiral` sits `~11 OOM` below current bounds — **not a near-term test.**
- **`mass = A1` untouched** (PR#260 / #311 ECHO-final). This is a photon/mechanical-sector
  gyrotropy, orthogonal to the mass sector.

## §4 — Relation to the SME / Letter context (KB-side; the Letter is NOT edited here)

The corpus's standing forward-Lorentz surface (`the-abandoned-interior.md` §"named open
falsifiable surface"; the SME/Kostelecký bookkeeping) lists an owed channel-by-channel campaign
against Hughes–Drever / vacuum-birefringence / GRB / SME bounds. This chiral `k`-linear term is a
**parity-ODD SME operator** (distinct from the parity-even cubic quartic), predicted `~11 OOM`
below the parity-odd cavity bounds — i.e. it maps onto an SME coefficient that current experiments
already bound far above the AVE value. **It is a CONSISTENCY entry on that surface, not a chord.**
Whether it earns an explicit line in the standalone birefringence Letter is a **Grant/auditor
framing call, deferred** — this KB leaf is the context; the Letter is not edited by the arc that
surfaced this.

> **Leaf references:** [chiral-mechanical-gyrotropy](chiral-mechanical-gyrotropy.md).

## Cross-references

- Register: `vol4/claim-quality.md` (`clm-acgyr1`)
- Mechanical face: `research/2026-07-04_srs-chiral-micropolar_result.md` §2a, §3, §7 (PR #508); module `src/ave/core/micropolar_bloch.py`
- Photon face: `research/2026-07-04_lorentz-on-srs_result.md` §2 readout (3), §4 (PR #515); driver `src/scripts/vol_4_engineering/lorentz_on_srs.py`
- Circuit sibling (EM face, magnitude pending): `def-ch1crc` (`common/vocabulary-register.md`)
- Parity-EVEN companions (distinct): `clm-k4d4ph`, `clm-yr6tu4` (quartic anisotropy)
- Reciprocal optical-activity (distinct mechanism): `clm-fofwr1` ([field-free-optical-activity](field-free-optical-activity.md))
- SME / owed-campaign context: `common/the-abandoned-interior.md`
