# Problem 3 — muonic-hydrogen 2S–2P shift from the SVE elliptic kernel: RESULT

**Date:** 2026-07-05 · **Lane:** implementer · **Branch:** `analysis/problem3-muonic-lamb` (stacked on freeze)
**Gated on FREEZE commit:** `4747630bf35e5e5abdd816ca022e8fcb5ba343ca` (fork memo FROZEN, Grant-ratified
2026-07-05; verified on `origin/analysis/letter-v2-arm2` before any shift number).
**METHOD prereg (frozen first):** `research/2026-07-05_problem3-muonic-lamb_METHOD-prereg.md`
**Driver:** `src/scripts/verify/problem3_muonic_lamb_shift.py` · **Gate 0:** `src/scripts/verify/problem3_gate0_recon.py`
**Tests:** `src/tests/test_problem3_muonic_lamb_shift.py`

## ROUTED BIN: **[C-EXCLUDED]** — both arms violate the µeV window by 4–7 orders of magnitude.

The static-E sector of the SVE continuum kernel is EXCLUDED as written for muonic hydrogen. Even scoped
to the lattice pitch `r >> ℓ_node = 386 fm`, the 2S–2P shift exceeds the CREMA window by ~2×10⁴×. Per
the frozen memo §3 [C] ledger, the **AC pump–probe birefringence and the µ-sector circulation-keying
survive** — they are DIFFERENT sectors, untouched by a static-E exclusion.

## Gate 0 — reconnaissance reproduction (DISCLOSED inputs, PASS)

Every frozen-memo §1 number reproduces exactly from `constants.py` under the derived E_c normalization
`E_c = E_YIELD = V_YIELD/L_NODE = √α·(m_e c²)/(e·ℓ_node) = √α·E_crit` (`constants.py:489,500`):

| quantity | this session | frozen memo |
|---|---|---|
| ℓ_node | 386.16 fm | 386.16 |
| E_c | 1.1304e17 V/m | ~1.13e17 |
| r_ns (Z=1/29/92) | 112.86 / 607.79 / 1082.56 fm | 112.9 / 607.8 / 1082.6 |
| A²(muonic-H) | 0.0246 | 0.0246 |
| A²(U91+) | 12.56 | 12.6 |

## The analytic tail (sympy-verified)

Gauss forces `D(r)=e/(4πr²)` exactly ⟹ Coulomb field `E_C(r)=D/ε₀=k/r²`, `k=e/(4πε₀)=1.44e−9 V·m`.
Inverting `E·√(1−(E/E_c)²)=E_C` on the lower branch gives `E/E_c = x + ½x³ + ⅞x⁵ + …`, `x=E_C/E_c`
(field ENHANCED, δV>0). The potential shift tail:

> **δV(r) = k³/(10 E_c² r⁵)  ⟺  δV/V_C = (1/10)·A²(r)**, `A²(r)=(E_C(r)/E_c)²`.

The expected (E/E_snap)²-class tail. Interior structure: LHS `E·√(1−(E/E_c)²)` has maximum `E_c/2` at
`E=E_c/√2` (D-turnover); above `E_C>E_c/2` no real lower branch — the interior, `r<r_turn=r_ns√2=159.6 fm`.

## The shift table — TWO arms × variants × TWO independent code paths (µeV)

muonic reduced mass `μ_red=185.84 m_e` (CODATA 2018 ratio m_μ/m_e=206.7682830, EXTERNAL input),
`a_μ=284.75 fm`, `r_ns=112.86 fm`, `r_turn=159.61 fm`, `ℓ_node=386.16 fm`. Window (primary) = 2.3 µeV
(CREMA 1σ). Full splitting 202.3706 meV = 202371 µeV.

| arm | variant | PATH B (full kernel, µeV) | PATH A (leading tail, µeV) | reconcile | flag |
|---|---|---|---|---|---|
| continuum | C-i (D-cap) | −2.31e7 | 4.04e6 | 1.18 | NA¹ |
| continuum | C-ii (δV-freeze) | +5.65e6 | 4.04e6 | 0.284 | OK |
| continuum | C-iii (excluded) | +1.52e6 | 1.26e6 | 0.172 | OK |
| lattice | L-i (hard ℓ_node) | −4.92e4 | −4.91e4 | 0.0024 | OK |
| lattice | L-ii (soft (qℓ)²) | +6.17e5 | −4.91e4 | 1.08 | NA² |

**Band summary (|shift|):** continuum [1.5e6, 2.3e7] µeV = **7.5×–114× the entire 202 meV splitting**;
lattice-scoped [4.9e4, 6.2e5] µeV = **0.24×–3× the entire splitting**.

¹ C-i (D-cap) interior is dominated by full non-tail cap physics: with D capped at D_max=ε₀E_c/2 inside
r_ns, the reference Coulomb field `E_C=k/r²` diverges, so `E_cap−E_C→−∞` and δV goes large-negative deep
inside. The leading 1/r⁵ tail (PATH A) cannot represent this — the A/B gap is EXPECTED, not a failure.
PATH B is authoritative.
² L-ii (soft form) multiplies the FULL kernel by `1/(1+(ℓ_node/r)²)` extending below r_turn; PATH A's
hard-ℓ_node bound is only a proxy. A/B gap expected; PATH B authoritative.

**Reconcile status:** the three tail-representable variants (C-ii, C-iii, L-i) reconcile WITHIN the
derived tolerance 0.40 (leading-tail truncation at the saturation edge x=E_C/E_c=½). The
ReconcileGate **positive control** (pure 1/r⁵, known coefficient) fires at rel=2.8e-15 — the gate is
LIVE, not a tautology. The two code paths share no code (A = exponential-integral closed forms; B =
transcendental root-find of the full kernel + adaptive quadrature).

## Sign of the lattice-scoped shift (real physics, not a bug)

L-i is NEGATIVE (−4.9e4 µeV) because scoping the cutoff OUT to ℓ_node=386 fm ≈ 1.36 a_μ removes the
entire near-nucleus region where 2S penetration dominates. In the remaining outer region (r>386 fm) the
2P density exceeds the 2S density (2S has its node at r=2a and dips), so ⟨2P|δV|2P⟩ > ⟨2S|δV|2S⟩ and the
differential flips sign. The MAGNITUDE is what routes; it is still ~2×10⁴× the window.

## Routing per the FROZEN bins (verbatim, §3)

- **[A-CONSISTENT]** requires the continuum arm to clear "even without any regime scoping" — it does
  NOT (band 7.5×–114× the full splitting). **[A] excluded.**
- **[B-AVE]** requires continuum-violates AND lattice-scoped-clears — the continuum violates, but the
  lattice-scoped arm ALSO violates (band 0.24×–3× the full splitting, smallest variant ~2×10⁴× the
  2.3 µeV window). **[B] excluded.**
- **[C-EXCLUDED]** — both arms violate. **ROUTED [C].**

## Knife checks (armed)

- **Edge-landing:** smallest |shift| (L-i, 4.92e4 µeV) is ~2×10⁴× the primary window and ~5×10³× the
  loose 10 µeV edge. NO arm sits near an edge — the verdict is not edge-poised. Robust.
- **½ / ¼ over-determination:** the routing numbers carry no ½/¼ coincidence. The derived tail
  coefficient 1/10 and field series (½, ⅞) are sympy-derived, not fitted. The D-turnover at E_c/2 (the
  "½") is a genuine elliptic-kernel feature, not a coincidence tell.
- **0.78 consonance (reported, NOT leaned on):** the memo's data-derived ~300 fm floor vs ℓ_node=386 fm
  (ratio 0.78). The lattice-scoped arm scoped AT the exact ℓ_node still violates by ~2×10⁴×. The
  consonance does NOT rescue the window — if anything it SHARPENS [C]: the cutoff scale is right and it
  still fails, so the failure is not a wrong-cutoff artifact. Reported as a flag, not a finding.

## SECONDARY — U91+ 1s (continuum arm INCOMPUTABLE, reported result)

U91+ (Z=92, electronic hydrogen-like) 1s Bohr `a=575.19 fm` sits INSIDE the no-solution radius
`r_ns(Z=92)=1082.56 fm` (575 < 1083). **72.5% of the 1s density and 90% inside r_turn** sit where the
continuum elliptic kernel has NO real solution (E_C>E_c over the bulk of the orbit). The continuum arm
is genuinely INCOMPUTABLE for U91+ — a reportable result, not a failure. It corroborates [C]: the
continuum static-E law does not merely violate windows at high Z, it has no solution at all. (The
lattice-scoped arm would compute but is not needed for the muonic-H adjudicator; the incomputability is
the informative content.) vs the 460.2±4.6 eV Lamb measurement (Gumberidze et al.): no continuum-arm
number is bookable.

## What dies, what survives (frozen memo §3 [C] ledger, applied)

- **Dies:** the continuum static-E constitutive law `ε_eff=ε₀√(1−(E/E_c)²)` as a UNIVERSAL claim down to
  atomic scales. It cannot be the vacuum's response to arbitrary static fields down to atomic scales.
- **Survives (separate sectors):** (i) the pump–probe AC birefringence of the Letter (deep-cold,
  weak-field A²~6e−7, dynamic ε-varactor read at optical/X-ray — NOT the atomic static-DC sector; its
  ~1e−3 HIBEF flip-prob falsifier is untouched); (ii) the µ-sector circulation-keying (`clm-pvlas1`,
  keyed on ∂_t B, not static flux). A [C] verdict excludes the continuum static-E extrapolation, NOT the
  registered birefringence prediction and NOT the magnetic-sector side-prediction.

## Discipline

- Consistency-vs-emergence: this is a **falsification/consistency-class** result — the SVE kernel
  (whose E_c is CODATA-derived through α, m_e per the Letter honesty ledger (iii)) is compared to a
  measured splitting; no emergence claimed. The verdict is [C-EXCLUDED] for the static-E extrapolation.
- Honest closure (Rule 11): pre-registered predictions were routed against the FROZEN bins with no
  post-hoc criterion drops. The continuum arm decisively violates; the lattice-scoped arm ALSO violates;
  a single mechanism (the 1/r⁵ near-nucleus enhancement surviving even the ℓ_node cutoff) explains both.
  Branch closed [C].
- Two independent code paths + live ReconcileGate (positive control fires); no self-verifying gate;
  gates the CONSUMED observable (the 2S−2P shift).
- Canonical constants only; muon mass declared as external CODATA input.
