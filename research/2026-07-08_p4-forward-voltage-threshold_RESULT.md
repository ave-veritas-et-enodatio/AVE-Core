# P4 — forward-voltage conduction threshold circuit + copper constraint — RESULT

**Date:** 2026-07-08 · **Lane:** implementer · **Branch:** `analysis/p4-forward-voltage`
**Frozen prereg:** `research/2026-07-08_p4-forward-voltage-threshold_prereg_FROZEN.md` (freeze commit
`0ada6025`, committed BEFORE any compute — git ordering = freeze proof).
**Driver:** `src/scripts/vol_9_device/p4_forward_voltage_threshold.py` · **Tests:**
`src/tests/test_p4_forward_voltage_threshold.py` (9 green, driver-confirmed via `verify_constants`,
`copper_decrement`, `muonic_loading_with_threshold`, `vf_candidates`).
**Figure (house-WHITE, Vol-9 datasheet register):**
`manuscript/vol_9_vacuum_datasheet/figures/forward_voltage/p4_diac_varactor_circuit.{pdf,png}`.

> **CLASSIFICATION (consistency-vs-emergence): CONSISTENCY / FALSIFICATION-class.** `E_c = E_yield =
> √α·E_crit` is CODATA-derived through `α, m_e`; `δ_Cu ≈ 2.4e-5` is an EXTERNAL empirical input (tagged
> by value only, no attribution). No emergence headline. The verdict is a consistency identity of the
> network topology + the Ax-4 kernel, plus a falsification comparison against an external decrement.

---

## ★ ROUTED BIN: **V_f is FREE** — no canonical scale forces a forward-voltage dead zone.

The make-or-break question routes **[FREE]**. The forward-voltage / minimum-bias-to-conduct threshold
`V_f` is **NOT forced by the substrate**: it must be tuned to survive. Per the A0 "free parameter" flag
(`research/2026-07-05_problem3-muonic-lamb_RESULT.md`:158), **that makes the cutoff a fit / echo**, and I
headline it as such. Two structural facts and one directional fact carry the verdict:

1. **The Ax-4 kernel has NO dead zone.** `S(A)=√(1−A²)` is analytic at the origin and loads `∝ ½A²` from
   `A=0` continuously. A dead zone (flat `ε₀` below `V_f`) is a NEW ingredient the kernel does not
   contain. **`V_f = 0` is the round-3 member; any `V_f > 0` is a departure from the round-3 derivation**
   (driver `eps_eff_over_eps0`; test `test_S1_zero_threshold_recovers_round3_continuous_kernel`).
2. **The lattice dispersion is gapless.** The canonical cold dispersion is the monatomic acoustic sine
   law `ω(q)=(2c/ℓ)|sin(qℓ/2)| → 0` as `q→0` (`graded-network-response.md`:56). There is **no phonon gap**
   to seed a conduction threshold (`dispersion_has_gap` → `is_gapped=False`, `gap_voltage_V=0`;
   `test_C1_dispersion_is_gapless_no_phonon_seeded_Vf`). A forward-voltage gate would need an optical-branch
   gap the corpus-modelled monatomic ladder does not carry.
3. **The only canonical field boundary is a HIGH-field CEILING, not a low-V floor.** The D-turnover
   (`E_C=E_c/2`, actual field `E=E_c/√2`, `A=1/√2`) is where the kernel loses its real lower branch. Using
   it as a dead-zone *floor* is upside-down (a floor suppresses WEAK field; the turnover bounds STRONG
   field). Likewise the A0 protective spatial cutoff (`r < r_cut ≈ 9·ℓ_node`) suppresses the STRONG-field
   near-nucleus region — its bond-voltage image is **~46 V** (a HIGH-field ceiling), not a forward floor.

### The V_f candidate table (driver `vf_candidates`; test `test_vf_candidates_scales`)

| Cand | scale | `V_f` | `A_f=V_f/V_yield` | dead-zone onset? | rescues muonic? | keeps copper? | keeps radiative A²≈6e-7? |
|---|---|---|---|---|---|---|---|
| **C1** | phonon gap | 0 | 0 | **none (gapless)** | — | — | — |
| **C2** | slew `α·V_snap` | 3.73 kV | **√α = 0.0854** | kinetic scale, not an onset | NO (A_char 0.157 > A_f) | yes | yes |
| **C3** | turnover ref `E_c/2` | 21.8 kV | **0.5** | HIGH-field ceiling | yes-but-empties-all | **NO (δ→0)** | **NO (kills it)** |
| **C4** | turnover actual | 30.9 kV | **0.7071** | HIGH-field ceiling | yes-but-empties-all | **NO** | **NO** |
| **C5** | pair gap `V_snap` | 511 kV | 11.7 | real-carrier gap | yes | **NO (δ→0)** | **NO** |
| **C6** | A0 cutoff image | **46 V** | 0.0011 | wrong-sign ceiling image | NO | yes | yes |

**No row satisfies the [FORCED] bin** (a genuine dead-zone onset that simultaneously rescues muonic,
keeps copper consistent, AND keeps the radiative weak-field sector loading). The candidates that could
rescue muonic (C3/C4/C5) do so only by making the vacuum transparent to ALL sub-turnover static fields —
which zeroes the copper contribution and kills the very static loading round-3 derived. The candidates
that preserve loading (C2/C6) do not rescue muonic. **V_f is FREE.**

---

## 1 — CIRCUIT MAPPING (formal)

**Equivalent circuit (figure, left panel).** One lossless L–C link cell: **series-L bond**
`L_cell = μ₀ℓ_node = 4.853×10⁻¹⁹ H`, **shunt-C node** `C_cell = ε₀ℓ_node = 3.419×10⁻²⁴ F`, giving
`Z₀ = √(L/C) = 376.73 Ω` and `ω_C = 1/√(LC) = c/ℓ_node = 7.763×10²⁰ rad/s` (driver `cell_reactances`;
`test_cell_reactances_Z0_and_omegaC`). The shunt C is the **T2 varactor** `C(V)=C₀·S(A_V)`,
`A_V=V/V_yield=|E|/E_yield` (`C_diel ∝ ε_eff = ε₀S`, rolls DOWN under load; `CLAUDE.md`:73). The NEW
ingredient — a **DIAC** (back-to-back / anti-series diodes, polarity-symmetric breakover `±V_f`) — gates
the varactor. **Constitutive law (piecewise; driver `eps_eff_over_eps0`):**

$$
\varepsilon_{\rm eff}(E)=\begin{cases}\varepsilon_0 & |E|<E_f\quad(\text{transparent, }C=C_0)\\[2pt]
\varepsilon_0\sqrt{1-(E/E_c)^2} & |E|\ge E_f\quad(\text{loads})\end{cases}
\qquad E_f=\tfrac{V_f}{\ell_{\rm node}},\;A_f=\tfrac{V_f}{V_{\rm yield}}=\tfrac{E_f}{E_c},\;E_c=E_{\rm yield}.
$$

The DIAC fires at breakover, so `ε` **snaps** discontinuously from `ε₀` to `ε₀ S(A_f)` at `|E|=E_f` (right
panel, orange). The `A_f=0` member is round-3's smooth continuous law (blue). **This is the formal
statement of "loads above a forward-voltage threshold."**

---

## 2 — DERIVE V_f: FREE (see routed bin above)

The derivation is the routed bin: gapless dispersion (C1), an analytic no-dead-zone kernel (S1), and only
a high-field ceiling (turnover) as a canonical boundary. **No canonical scale falls out as a forward-voltage
dead-zone onset.** Honestly: `V_f` is a **tuned parameter**, so the "forward-voltage threshold" is an
**echo/fit** at the value level — the same status the A0 result assigned the ~9·ℓ_node ≈ 3.5 pm cutoff.

---

## 3 — CONSTRAINTS WITH THE THRESHOLD

### (a) Copper X-ray decrement — **CONSISTENT** (OUR compute; not any external ~1e-7 estimate)

Volume-average of `A²(r)=(Z_Cu·k/(E_yield r²))²` over the Cu WS cell (Z=29, FCC `a=3.615 Å`,
`R_ws=141.3 pm`), interior-excluded at the Cu turnover `r_turn(Cu)=0.860 pm` (driver `copper_decrement`,
bare-Z = direction-conservative UPPER bound; screening only lowers it):

- `⟨A²⟩ = 1.68×10⁻⁷` → **index decrement `δ_index = ¼⟨A²⟩ = 4.20×10⁻⁸`**, ε-deficit `½⟨A²⟩ = 8.39×10⁻⁸`.
- vs measured `δ_Cu ≈ 2.4×10⁻⁵` (external; known to ~1% → uncertainty band `2.4×10⁻⁷`):
  `δ_AVE/δ_Cu ≈ 1.7×10⁻³` (≈3 orders below), and **`δ_AVE < ` the 1% band** → **[CONSISTENT]**
  (`test_copper_decrement_is_consistent_and_far_below_delta_Cu`). The AVE static-loading contribution
  hides under the measured decrement's known accuracy.
- **The threshold does not change this** (`copper_decrement(A_f=0.2)` still CONSISTENT): copper's
  decrement is dominated by the strong near-core shell (just outside `r_turn`), well above any modest
  `V_f`; a dead zone removes only the negligible weak far-tail. (A `V_f` large enough to matter for copper
  — `A_f ≳ 0.5` — would zero it entirely, killing round-3's static loading.)

> **Our independent number (`~1×10⁻⁷` for the ε-deficit, `~4×10⁻⁸` for the index) lands near the known
> ~1e-7 estimate the task told me not to adopt — a corroboration by an independent WS-cell compute, NOT an
> import.** The direction (`≪ δ_Cu`) is robust across the interior-excluded and screened variants.

### (b) Muonic-with-threshold — **[C-EXCLUDED] STANDS** (the dead zone does not rescue it)

The muonic-H overshoot is dominated by the SUB-PITCH band `[r_turn, ℓ_node]` (103% of the C-iii shift,
A0 round-3 band-split). A forward-voltage dead zone at `A_f` removes only the FAR tail (`A(r)<A_f ⟺ r>r_f`):

- at `A_f=0.05`: surviving loading fraction **0.979** → proxy shift `4.8×10⁴ µeV` ≈ A0's L-i anchor
  (`4.92×10⁴ µeV`, `research/2026-07-05_problem3-muonic-lamb_RESULT.md`:80), **`~2×10⁴×` the 2.3 µeV
  window → [C-STANDS]** (`test_muonic_C_stands_for_subturnover_threshold`).
- the dead zone only empties the real-branch loading at `A_f ≥ ½` (the turnover) — a HIGH-field ceiling
  used upside-down as a floor, which also zeroes copper and the radiative sector. **No `A_f` rescues
  muonic while preserving static loading elsewhere.**

**[C-EXCLUDED] stands.** The threshold reframe does not revive the static continuum extension.

### (c) Delbrück / γ fence — **YES, dispersion fences them**

The sine-law dispersion has a hard band edge `ℏω_max = 2ℏω_C = 1.022 MeV` at `q=π/ℓ` (driver
`delbruck_fence`). The response scale `ℏω_C = m_e c² = 511 keV = e·V_snap` (the pair-production gap).
Delbrück scattering and γ pair-attenuation (`≳ 1 MeV`) live ABOVE the band edge, in the **real-carrier
(pair-production, V_snap) sector**, not on the reactive T2 line. The reactive kernel's predictions do not
extend above `ω_C`; dispersion fences them out.

---

## FLAGS (flag-don't-fix — surfaced with file paths + verbatim, NOT silently resolved)

- **⚑ S1 — a nonzero `V_f` CONTRADICTS the merged round-3 result.** Round-3
  (`research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md`, `[DERIVED: CHARGE-KEYED]`, #547)
  derives that a held static field loads **continuously from `A=0`** at leading order `½A²` (verbatim
  crux, RESULT:69: *"⟨1 − S(A_V)⟩ = ½⟨A_V²⟩ … keeps the DC baseline `a_0²`"* — nonzero for ANY `a_0>0`).
  The DIAC-gated law is FLAT (`ε₀`, unloaded) for `|E|<E_f`. **A nonzero dead zone is not derivable from
  round-3 — it is a departure that would say static fields below `V_f` do NOT load, contradicting round-3's
  `½A²`-from-zero.** Round-3 is exactly the `V_f=0` member. Surfaced for Grant: the forward-voltage
  threshold and round-3 cannot both be canonical at `V_f>0`; round-3 stands as the derived result, `V_f>0`
  is an added free postulate.
- **⚑ S2 — the "9·ℓ_node cutoff ↔ V_f" identity fails DIRECTIONALLY.** A0's protective cutoff SUPPRESSES
  loading for `r < r_cut` (**strong** field / large bond voltage — a HIGH-field ceiling). A forward-voltage
  dead zone suppresses loading for `|V| < V_f` (**weak** field — a LOW-field floor). These act on OPPOSITE
  field regions (driver: `C6_A0_cutoff_image` A_f=0.0011 ceiling vs a floor). So the spatial cutoff and the
  forward-voltage threshold are not the same knob; the reframe does not carry the A0 cutoff's protective
  content. (The genuine, FORCED substrate cutoff is the **UV/spatial** one at `ℓ_node` — the reduced
  Compton wavelength `ℏ/mc`, canonical; the *voltage-threshold* framing of it is what is free.)

---

## RECONCILIATION — the three statements ARE consistent (via SCOPE, not a voltage dead zone)

The threshold clause makes the three consistent through a **field-strength / regime scope**, which is the
FORCED content (`ℓ_node` UV cutoff), NOT the free `V_f`:

1. **Disclaimer (`main.tex:330–331`):** not a universal static-field constitutive law extending to strong
   near-nucleus atomic fields. ✓ — muonic-H (`A²` up to `½`, a STRONG field) proves it is not universal.
2. **Charge-keyed (round-3, §II.B):** a held field loads at the **lattice scale**, in the weak-field
   regime the Letter registers (`A²≈6e-7`, radiative pump). ✓ — copper (`A²~1e-7`, `δ_AVE~4e-8 ≪ δ_Cu`)
   confirms weak static loading is real and consistent with experiment.
3. **Muonic `[C-EXCLUDED]`:** the STRONG-field continuum extension is dead. ✓ — stands even with the
   `ℓ_node` UV cutoff (A0 L-i) and with any sub-turnover dead zone.

**The unifying clause:** *the vacuum loads at the lattice scale in the weak/radiative regime; the continuum
extrapolation to strong sub-lattice atomic fields is excluded (cut off below the node pitch `ℓ_node`). The
cut is a UV/discreteness scope at `ℓ_node` (forced = `ℏ/mc`); a literal forward-voltage dead-zone `V_f` is
a free parameter and is not required by — indeed departs from — the round-3 derivation.*

---

## PROPOSED PAPER-SENTENCE REWRITE (for the orchestrator/Grant to integrate — NOT edited here)

> **DISCIPLINE NOTE:** I did NOT edit `main.tex` or the ledger. Text below is a proposal only. Two options
> are offered because the honest answer (V_f FREE) differs from a literal "forward-voltage threshold"
> headline; Grant/orchestrator pick the framing.

**(A) The `main.tex:330–331` disclaimer — minimal, keeps the honest scope (RECOMMENDED):**
- CURRENT (330–331): *"read at optical/X-ray frequencies. We do \emph{not} assert it as a universal
  static-field constitutive law extending to strong, near-nucleus atomic fields."*
- PROPOSED: *"read at optical/X-ray frequencies. The law loads at the lattice scale in this weak-field,
  radiative regime, but we do \emph{not} extend it as a universal continuum static-field constitutive law
  to strong, near-nucleus atomic fields below one node pitch: the continuum form is cut off at the lattice
  pitch \(\ell_{\rm node}\) (the reduced Compton scale), and its extrapolation to strong atomic fields is
  excluded (Sec.~\ref{sec:model})."*

**(B) The §II.B charge-keyed sentences (`main.tex:280–281` and `:351–352`) — align "loads" with the
lattice-scale scope:**
- CURRENT (351–352): *"the static-field response is instead derived to be charge-keyed, so that a held
  field is a real operating-point bias and does load."*
- PROPOSED: *"the static-field response is instead derived to be charge-keyed: a held field is a real
  operating-point bias and does load at the lattice scale, in the weak-field regime. The continuum
  extrapolation of this loading to strong sub-lattice atomic fields is what the muonic-hydrogen test
  excludes; a lattice-pitch cutoff at \(\ell_{\rm node}\) scopes the loading to the lattice scale but does
  not by itself rescue the strong-field static sector."*

> **If Grant insists on the "forward-voltage threshold" language in print,** it must be tagged as a free
> (fitted) scale, not derived — e.g. append: *"(any dead-zone forward-voltage threshold below which the
> link stays transparent is a free parameter, not fixed by the substrate; the derived content is the
> lattice-pitch cutoff)."* Omitting that tag would present a fit as a derivation.

---

## DISCIPLINE LEDGER

- **ave-canonical-source:** every number from `ave.core.constants`; `verify_constants()` COMPUTES 7 cross-
  checks (all pass), including `V_yield=√α·V_snap`, `E_yield=V_yield/ℓ_node`, `ℏω_C=e·V_snap`. No hardcoding.
  `δ_Cu`, `m_μ/m_e`, and the Cu FCC lattice constant are the ONLY external inputs, tagged in-code.
- **pre-register:** prereg frozen at `0ada6025` BEFORE compute (git ordering).
- **Rule 11 honest closure:** routed against the frozen bins; **V_f = FREE headlined**, no post-hoc rescue.
  A single mechanism (the kernel loads `∝A²` from zero, gapless lattice, only a high-field ceiling)
  explains why no forced dead zone exists.
- **Rule 12 substitution-not-retraction:** round-3 preserved as the `V_f=0` member; this is a NEW
  (DIAC-gated generalization) derivation with its own prereg + verification chain, not a refill of the
  round-3 slot.
- **flag-don't-fix:** S1 (round-3 contradiction) and S2 (direction) surfaced with paths + verbatim; not
  resolved. The muonic `[C-EXCLUDED]` is CONFIRMED, not walked back.
- **phase-space coordinate check (A46):** the claim is `A=|E|/E_yield` (amplitude ratio); copper/muonic
  measure `A²(r)` in the same coordinate. No phase-space↔real-space mismatch.
- **pure-AVE-corpus:** no external attribution in any tracked file; `δ_Cu` by value only.
- **NO self-merge:** branch pushed, PR `[REVIEW: pending-orchestrator]`, DO-NOT-MERGE.
