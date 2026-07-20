# Scalar-GW Bulk-Channel Far-Field — Derivation (does the A1/√2·c bulk-dilatation channel radiate; multipole-by-multipole; LIGO comparison)

**Date:** 2026-07-20
**Class:** DERIVATION (research-doc; **forms derived, values calibration/astro-imported and tagged; mints no `clm-`, propagates to no KB/tex leaf**). This lane resolves-or-frames **FLAG-1 (D5)** of the deep-space band-map derivation (`research/2026-07-19_deep-space-band-map_derivation.md:236`) — the surfaced sector-identification fork: *does the `√2·c` A1/bulk-dilatation channel radiate as an observable scalar-GW polarisation?*
**Provenance:** Grant-fired 2026-07-20, verbatim `[sic]`: *"5. derive either way?"* — ratifying derive-don't-rule / prove-or-disprove. EITHER outcome is the deliverable; a radiating outcome is a WELCOME kill-class falsifier exposure. Every `[canon]` input below was content-verified in this worktree at HEAD `64f1894d` (verify-before-cite, `grep -F` / direct read).
**Lane fences:** DERIVATION lane only. **No** engine edits; **no** `manuscript/` / `manuscript/ave-kb/` / `.tex` edits. Numeric arithmetic is reproduced by the lane-fenced driver `research/drivers/scalar_gw_bulk_channel.py` (+ `_results.json`); it imports `ave.core.constants.C_0` read-only and touches no engine primitive. KB/tex propagation is OWED-FOLLOW-ONS (§8), fenced to the auditor/cleanup lanes.

---

## §0 — Attribution key + what this doc does / does not do

**Attribution tags** (same discipline as the band-map lane):
- **[canon]** — citation of an existing canonical leaf/const, content-verified at HEAD `64f1894d`.
- **[derived]** — a FORM this lane derives from `[canon]` inputs by standard radiation/multipole algebra. Derivation shown; nothing asserted as new canon.
- **[import]** — an external (LIGO/Virgo, astro) or CODATA value, cited and tagged. Consistency-class per `consistency-vs-emergence`: FORMs may be derivable, but any dimensionful VALUE enters through a calibration or an imported measurement — never headlined as emergence.
- **[FLAG]** — an unforced modeling choice or a corpus contradiction, surfaced per flag-don't-fix (Grant/auditor adjudication), never silently resolved.

**This doc DOES:** write the bulk-channel wave equation from the canon constitutive relations; identify the source a compact binary imposes on the A1/bulk sector; run the multipole expansion (monopole / dipole / quadrupole) as theorems with enumerated assumptions; if a multipole survives, derive the far-field flux FORM, the **dimensionless amplitude ratio vs the shear channel** (the headline, per the α-circularity lesson — the claim must live in a ratio), and compare to the published LIGO extra-polarisation constraints; state plainly whether the prediction is EXCLUDED / CONSTRAINED / UNTOUCHED / NON-RADIATING.

**This doc does NOT:** mint canon; edit any leaf; manufacture a suppression to protect the framework OR a signal for drama (consensus knife both ways); or resolve the load-bearing fork by fiat. Where the derivation hits an unforced choice it **fails closed to UNDETERMINED** and surfaces the fork (§7).

---

## §1 — REGIME / SECTOR / PHASE-STATE header (fired before any radiation algebra)

**MODE.** A compact binary (BBH / BNS) in the inspiral — two orbiting mass-energy concentrations — as a **source** driving the deep vacuum. Contrast column: the observed transverse GW (LIGO/Virgo).

**REGIME.** **Regime I** — deeply linear. `[canon]` `einstein-field-equation.md:90-97`: GW150914/GW170817 sit at `V_GW/V_snap ~ 10^-28`–`10^-29`, "deeply linear," lossless propagation at `c`; the nonlinear II–III regime is reached only in the near-merger zone `r ≲ 10 r_s`. All radiation algebra below is the **cold-linear** far field; saturation (Op14) does not enter the propagation.

**PHASE-STATE.** **Cold-reactive** (lossless-reactive, Axiom 3). `[canon]` `eq_axiom_3.tex:24` (quoted in the deep-space walk-record §4 anchor 1): the medium "stores and returns energy but does not dissipate it," and "any apparent loss must be a boundary-radiation or mode-conversion channel, **never a bulk resistive one**." Far-field **radiation is a legal Ax3 loss channel** (a radiative port), unlike a bulk resistor — so a radiating bulk channel does NOT violate Ax3. That is exactly why this is a live question rather than an Ax3-forbidden one.

**SECTOR.** The graded vacuum medium carries the four branches of the band-map `[canon]` `research/2026-07-19_deep-space-band-map_derivation.md:52-67`:
1. **EM-transverse** (photon, T₂ shear-EM), `c = √(G/ρ)`;
2. **Mechanical shear / GW** (T₂ shear-G), `c_shear = c` — **the observed GW channel** `[canon]` `einstein-field-equation.md:62-63,:84` ("GW are transverse shear modes"; "low-frequency macroscopic inductive strain-waves");
3. **Bulk-longitudinal / dilatation** (A1 mass), `c_bulk = √2·c` (`clm-uu1qbo`, `K = 2G` magic angle) — **the channel under test**;
4. **gapped Cosserat micro-rotation** (the `(2,3)` winding), Yukawa-screened, irrelevant at GW scale (§4.4 band-map: reach `~ℓ_node`).

**Sector-ownership discipline (do NOT cross-wire).** A1 owns compression/mass/dilatation; T2 owns shear/GW. The observed GW is T2 shear at `c`; the channel under test is the A1/bulk dilatation. The binary's masses ARE the A1-dilatation content (`[canon]` `master-equation.md:20` "A1 dilatation-MASS"; `cosserat-mass-gap.md:149` re-scope "the rest-mass store is the A1 longitudinal DILATATION"). So the source is genuinely an A1 source — the derivation must therefore take the A1/bulk far-field seriously, not dismiss it by sector fiat.

**SUBSTRATE-NATIVE CHECK (fired before the algebra).** K4/Cosserat: the medium is the chiral Laves K4 Cosserat crystal with a genuine independent A1 dilatational DOF (`cosserat-mass-gap.md:38,:120-132` `[canon]`). Op14: enters only as a graded reactance near the masses (Regime I here, not load-bearing). **Phase-space-vs-real-space (A46):** the corpus claim is a *channel-radiation* claim (does the A1 dilatation branch carry a far-field port?) — the matching test coordinate is the **multipole/flux decomposition of the radiated field**, computed in the same channel basis (A1 dilatation vs T2 shear) the corpus uses. This doc measures in that basis, not in a real-space Cartesian strain the corpus never claimed.

---

## §2 — The bulk-channel wave equation and the binary source term

### §2.1 — The A1/bulk field equation [derived from canon constitutive relations]

The displacement field of the linear-elastic vacuum decomposes (Helmholtz) into a curl-free longitudinal part carried by the A1/bulk channel and a divergence-free transverse part carried by the T2/shear channel:
$$\mathbf{u} = \nabla\phi + \nabla\times\boldsymbol\psi,\qquad \theta \equiv \nabla\cdot\mathbf{u} = \nabla^2\phi\ \ (\text{the DILATATION, the A1 observable}).$$

Taking the divergence of the linear elastodynamic equation `ρ ∂²ₜu = (K+G/3)∇(∇·u) + G∇²u + f` isolates the **A1/bulk dilatation wave equation** `[derived]`:
$$\boxed{\ \partial_t^2\,\theta \;-\; c_L^2\,\nabla^2\theta \;=\; \frac{1}{\rho}\,\nabla\!\cdot\!\mathbf{f}\ }\qquad c_L^2=\frac{K+\tfrac{4}{3}G}{\rho}.$$
This is a **scalar (spin-0) wave** with a single "breathing" polarisation — structurally the wave equation of a massless scalar field sourced by `∇·f`. The transverse T2 part obeys the companion equation `∂²ₜψ − c_T²∇²ψ = −(1/ρ)∇×f`, `c_T² = G/ρ`, the observed-GW channel.

**[FLAG-A — the √2·c vs √(10/3)·c speed of the *radiated* longitudinal wave.]** The corpus carries **two distinct longitudinal objects**, and this doc must be explicit about which one is the far-field radiative speed:
- The **A1-scalar bulk-modulus PORT mode** `c_bulk = √(K/ρ) = √2·c` (`clm-uu1qbo`; `constants.py` `V_LONG`, `:775-781` `[canon]`; band-map channel 3). This is the **bulk-modulus impedance quantity** `Z_bulk = ρ c_bulk` (`bulk-impedance-at-saturation-boundary.md` `[canon]`) — a reflection/port speed. It *drops* the `4G/3` shear term.
- The **isotropic-solid P-wave** `c_L = √((K+4/3G)/ρ) = √(10/3)·c ≈ 1.826·c` (`constants.py:778` `[canon]` verbatim: "the full compressional (P) wave is `c_L = √((K + 4G/3)/ρ) = √(10/3)·c ≈ 1.83c`"; and the Rule-12 `c_L`-reconciliation notes `mond-hoop-stress.md:43`, `lc-electrodynamics.md:28` `[canon]`: the √2·c form "omits the `4G/3` shear term and is the dilatational/fluid speed, **NOT the isotropic-solid P-wave**").

A **freely propagating plane longitudinal wave** in a solid with nonzero shear modulus travels at the P-wave speed `c_L = √(10/3)·c`, because a plane compression shears the medium — the `4G/3` term cannot be dropped for a real far-field wave. **So the far-field radiated A1/bulk-longitudinal wave, if it exists, propagates at `√(10/3)·c`, not the `√2·c` port speed.** The `√2·c` is the correct speed for a *boundary/impedance* statement (Z_bulk, reflection at a saturation wall), which is the context the band-map channel-3 row inherited. This distinction is **already in the corpus** (the c_L-reconciliation Rule-12 notes) but the band-map table labels channel 3 with the port speed `√2·c`; carried here as a deviation to surface (§7), not a fix. **Both speeds are superluminal** — the causality/observability consequence is the same (§6) and is robust to this fork.

### §2.2 — The source a compact binary imposes on the A1/bulk sector [derived]

Each body is a localised A1-dilatation concentration; the binary is **two moving dilatation centres**. The bulk-channel source moments are the moments of the dilatation source density `s(\mathbf{x},t) ≡ (1/ρ)\nabla\cdot\mathbf{f}`, whose volume integral is fixed by the mass-energy content:
$$q(t)=\int s\,d^3x \;\propto\; M_{\rm tot}\quad(\text{total dilatation = total mass-energy}),\qquad d_i(t)=\int s\,x_i\,d^3x \;\propto\; \sum_a M_a x_{a,i},$$
$$Q^{(s)}_{ij}(t)=\int s\,x_i x_j\,d^3x \;\propto\; \sum_a M_a\,x_{a,i}x_{a,j}\quad(\text{the mass second-moment — same tensor that sources T2/GW}).$$
The key structural fact: **because mass = A1-dilatation, the bulk-channel source moments ARE the mass moments** (monopole ∝ M, dipole ∝ Σ M x, quadrupole ∝ Σ M xx). The multipole verdict therefore rides entirely on the conservation laws those moments obey.

---

## §3 — Multipole expansion of the bulk channel (theorems; assumptions enumerated)

For a scalar field `θ` obeying `□θ = s`, the far-field energy flux from the retarded solution is governed, order by order, by the time-derivatives of the source moments of §2.2. The scalar radiated power at multipole order `ℓ` scales as `P_ℓ ∝ (∂_t^{ℓ+1}\,[\text{ℓ-th moment}])²`. The three leading orders:

### §3.1 — MONOPOLE: NON-RADIATING [theorem]

`P_0 ∝ \dot q^2`. With `q ∝ M_tot`:
$$\dot q \;\propto\; \dot M_{\rm tot} \;=\; 0 \quad(\text{mass-energy conservation for a bound binary})\ \Rightarrow\ P_0=0.$$
**Verdict: the bulk monopole does not radiate.** This is the *same theorem class* that kills monopole GW in GR (there via `∂_t M = 0`). A "compression monopole cannot radiate if total compression/mass-energy is conserved" — confirmed, derived not asserted.
**Assumptions (enumerated):** (M1) total mass-energy of the isolated binary is conserved over an orbit — standard, robust. (M2) the bulk-channel monopole moment is the total mass-energy (mass = A1-dilatation) — `[canon]` sector identity, consistency-class.

### §3.2 — DIPOLE: NON-RADIATING [theorem] — AVE-strengthened vs generic scalar-tensor

`P_1 ∝ \ddot d^2`. With `d_i ∝ \sum_a M_a x_{a,i} = M_{\rm tot}\,x_{\rm cm,i}`:
$$\ddot d_i \;\propto\; M_{\rm tot}\,\ddot x_{\rm cm,i} \;=\; \dot P_{\rm tot,i} \;=\; F^{\rm ext}_i \;=\; 0 \quad(\text{momentum conservation; internal forces cancel})\ \Rightarrow\ P_1=0.$$
**Verdict: the bulk dipole does not radiate.** Killed by momentum conservation, exactly as the task's candidate route anticipated.

**AVE-distinct strengthening (consensus knife the *favourable* way — a genuine consistency success, not manufactured).** In generic scalar-tensor gravity (Brans-Dicke), dipole scalar radiation is `P_1 ∝ (s_1 - s_2)^2` where `s_a` are the bodies' *sensitivities* (fractional gravitational binding energy); for self-gravitating compact objects `s_NS ~ 0.2`, `s_BH ~ 0.5`, so `s_1 ≠ s_2` **revives** dipole radiation for asymmetric systems (NS-BH, NS-WD) — the dominant scalar-tensor observable. In AVE the bulk channel couples to the **A1-dilatation charge = inertial mass, exactly and universally** (no separate "scalar charge," no sensitivity): `d_i ∝ M_a x_{a,i}` with the *same* `M_a` that appears in `\ddot x_{cm}`, so the cancellation is exact **even for compact objects**. **AVE therefore predicts NO scalar dipole radiation, cleanly, with no compact-object revival** — consistent with the tight pulsar-binary dipole bounds (e.g. PSR J1738+0333) that constrain scalar-tensor. This is a point *in AVE's favour*.
**Assumption (enumerated, load-bearing):** (D1) the A1-dilatation charge that sources the bulk far-field equals the inertial/gravitating mass *including gravitational binding energy* (strong-equivalence-exact). This is the `[canon]` "mass = A1 dilatation" identity — **consistency-class, NOT driver-validated** (`cosserat-mass-gap.md:151` `[canon]`: "No driver discriminates A1-mass from T2-mass"). If (D1) failed (a sensitivity-like split between bulk-charge and inertial mass), dipole would revive — flagged, not assumed away.

### §3.3 — QUADRUPOLE: RADIATIVE [derived] — the exposure

`P_2 ∝ (\dddot Q^{(s)}_{ij})^2`. With `Q^{(s)}_{ij} ∝ \sum_a M_a x_{a,i} x_{a,j}` = the mass second-moment: for a circular binary the trace `\sum_a M_a r_a^2` is constant, but the traceless part **rotates at `2Ω`**, so
$$\dddot Q^{(s),\rm TL}_{ij} \neq 0 \quad\Rightarrow\quad \boxed{\,P_2 \neq 0\ \text{— the bulk channel RADIATES at quadrupole order.}\,}$$
**The bulk channel is NOT non-radiating.** Monopole and dipole are killed by conservation laws; the quadrupole source moment is the *same nonzero rotating mass quadrupole* that sources the observed T2/shear GW, so there is no conservation law left to kill it. The candidate "monopole-killed-leaves-quadrupole" route of the task closes **radiative**, not suppressed — the WELCOME kill-class exposure.
**Assumptions (enumerated):** (Q1) the A1/bulk channel is an **independent far-field radiative DOF** of the medium (an elastic solid's longitudinal channel is a real propagating mode, distinct from the transverse channel). **This is the load-bearing unforced choice** — see §7; if the A1 longitudinal is instead *constrained* (as in GR, where the longitudinal/scalar metric parts are pure-gauge and do not radiate) or *reactive-near-field-only*, the quadrupole port is closed and P₂→0. (Q2) the mass quadrupole couples to the dilatation channel with an O(1) (not parametrically small) strength — true for an elastic medium with `K = 2G` (no large suppression parameter), the crux of §4.

---

## §4 — Far-field flux and the headline dimensionless ratio (bulk vs shear)

The quadrupole survives (§3.3), so the deliverable is the **dimensionless ratio of the bulk-channel amplitude to the shear-channel (observed-GW) amplitude** — the α-circularity lesson: the claim must live in a ratio, not an absolute (all dimensionful VALUES are imported).

### §4.1 — The speed suppression [derived, calibration-free]

Both channels are sourced by the **same** rotating mass quadrupole `Q_ij` (§2.2), so in the ratio the source moment cancels and the radiated-power ratio is set by the channel speeds and the O(1) coupling/tensor-structure factor. For a fixed quadrupole source moment the scalar radiated power scales as `1/c_channel^5` (the standard multipole flux scaling), giving a **calibration-free lower-bound suppression** (driver: `research/drivers/scalar_gw_bulk_channel.py`):
$$\frac{P_{\rm bulk}}{P_{\rm shear}}\Big|_{\rm speed} = \left(\frac{c_{\rm shear}}{c_{\rm long}}\right)^{5} = \begin{cases} 2^{-5/2} \approx 0.177 & (c_{\rm long}=\sqrt2\,c,\ \text{port speed})\\[4pt] (3/10)^{5/2}\approx 0.049 & (c_{\rm long}=\sqrt{10/3}\,c,\ \text{P-wave, the physical radiative speed per FLAG-A})\end{cases}$$
Amplitude-level (`h ∝ √P`, equal-coupling bracket): `h_bulk/h_shear|_speed = (c_shear/c_long)^{5/2}` = **0.42** (√2·c) or **0.22** (√(10/3)·c).

### §4.2 — The coupling factor is O(1) — there is no large suppression parameter [derived, the crux]

The speed factor alone leaves `h_bulk/h_shear ~ 0.2`–`0.4`. The remaining factor is the **coupling of the mass quadrupole to the dilatation channel relative to the shear channel**. In an isotropic elastic medium this ratio is O(1), governed by `K/G`:
- `K = 2G` at the magic angle (`[canon]`) — the two moduli are the *same order*. There is **no** analog of the Brans-Dicke `1/(2ω_BD+3)` large-denominator suppression (`ω_BD > 4×10^4`, Cassini `[import]` Bertotti-Iess-Tortora 2003) that makes viable scalar-tensor scalar radiation negligible. AVE's bulk-to-shear coupling is not parametrically small.
- **Worse for suppression:** since mass *is* the A1-dilatation (`[canon]` sector identity), the mass quadrupole is most naturally an A1/dilatation source of *at least* comparable strength to its shear projection. The sector-ownership logic pushes the coupling **up**, not down.

**Headline (consensus knife applied both ways):** under the elastic-medium reading with an O(1) coupling, `h_bulk/h_shear ~ 0.2`–`0.4` — a **LARGE scalar admixture**, comparable-order to the observed tensor GW, NOT the tiny `~1/ω_BD` of viable scalar-tensor gravity. This is the exposure. The only way it becomes small is a corpus-absent mechanism that decouples the mass quadrupole from the A1 radiative port (see §7 fork). Fabricating such a mechanism to protect the framework is exactly the move the discipline forbids; it is surfaced as the fork, not asserted.

**[FLAG-B — the O(1) angular/tensor-structure factor is not pinned.]** The exact bulk/shear power ratio requires the angular-pattern integrals of a rotating quadrupole projected onto the longitudinal vs transverse radiation patterns (the elastodynamic P-vs-S partition of a quadrupole source). This lane derives the **speed scaling** (robust) and the **O(1)-not-small coupling** (robust from `K=2G`) but does NOT pin the exact numerical prefactor — it is bracketed at O(1), and the headline (`~0.2`–`0.4`, large) is robust to that bracket. A precise prefactor is a satellite-driver follow-on (§8).

---

## §5 — Comparison to published LIGO/Virgo extra-polarisation constraints

Three independent observational handles bear on a large scalar-quadrupole admixture. Each is stated with its `[import]` tagged and its strength honestly bounded.

### §5.1 — Direct polarisation-content tests

`[import]` Abbott et al. (LVC), *Tests of General Relativity with GW170817*, PRL **123**, 011102 (2019) / arXiv:1811.00364: using the sky location from the EM counterpart and the three-detector (LIGO-Hanford/Livingston + Virgo) network, **pure-scalar and pure-vector** polarisation hypotheses are strongly disfavoured relative to **pure-tensor** — log Bayes factors of order **O(20)** (odds `~10^20`) favouring tensor. *(Exact Bayes-factor value not re-verified against the source in this lane; the qualitative "pure-scalar strongly excluded" is the robust import; the precise figure is an owed check.)*
- **What it constrains:** AVE does **not** predict pure-scalar; it predicts tensor **plus** a scalar admixture (§4). Current 2–3-detector networks cannot fully resolve a mixed 5-polarisation content for a transient CBC, so the **admixture-amplitude** bound is weaker than the pure-hypothesis bound. Verdict on this handle alone: **CONSTRAINED** (pure-scalar excluded; a `~0.2`–`0.4` admixture is in tension but not decisively resolved by GW170817's network).

### §5.2 — Inspiral energy-balance / phasing

The observed inspiral chirp matches the GR tensor-quadrupole energy-loss rate. An extra radiative channel at the **same (0PN, quadrupole) order** carrying `P_bulk/P_shear ~ 0.05`–`0.18` rescales the total flux by that factor.
- **Honest caveat (against a naive kill):** a *same-order* scalar quadrupole is **partially degenerate** with the chirp mass for a single event (an overall flux rescaling reabsorbs into inferred masses) — unlike a `−1PN` dipole term, which is why dipole is the well-bounded scalar-tensor observable and a 0PN scalar quadrupole is *not* cleanly excluded by one event's phasing. The degeneracy is broken across events with different mass ratios and by the polarisation content (§5.1). Verdict on this handle: **CONSTRAINED, degeneracy-limited** — not a clean single-event kill.

### §5.3 — Superluminal propagation (the decisive handle if the channel radiates) — see §6

The radiated longitudinal wave travels at `√(10/3)·c ≈ 1.83·c` (FLAG-A). GW170817 established `[import]` `|c_GW − c_EM|/c ≲ 10^{-15}` (Abbott et al. 2017, multi-messenger; tensor channel) and a `~1.7 s` GW–GRB delay over `~40 Mpc`. A **superluminal** scalar channel carrying an O(0.1) energy fraction is a qualitatively different propagation signature from the tensor mode observed at `c` — it is the sharpest tension (§6).

### §5.4 — LIGO-comparison verdict

| Reading of the fork (§7) | Predicted `h_bulk/h_shear` | LIGO status |
|---|---|---|
| **A1/bulk is an independent radiative DOF, O(1) coupling** | `~0.2`–`0.4` (large) | **CONSTRAINED → leaning EXCLUDED** (polarisation content §5.1 + superluminal §6); not a single clean single-event kill (§5.2 degeneracy), but multi-handle tension |
| **A1/bulk radiative but coupling somehow ≪1** | ≪ 0.1 | UNTOUCHED — but needs a corpus-absent small-coupling mechanism (fork) |
| **A1/bulk NON-radiating (constrained/near-field-only)** | 0 | UNTOUCHED — but needs a corpus-absent suppression theorem (fork) |

**The elastic-medium default (row 1) is a kill-class exposure.** Escaping to rows 2–3 requires new physics the corpus does not currently carry.

---

## §6 — The √2·c coexistence note (causality / observability — surface, don't bury)

The task requires the two-speed tension be addressed honestly: a propagating bulk mode faster than the EM/shear speed.

**What canon says about coexistence.** The "three speeds, do not fuse" table (`cosserat-mass-gap.md:116-132` `[canon]`) asserts the A1/bulk `√2·c`, the T2/shear `c`, the T2/curvature `√2·c`, and the P-wave `√(10/3)·c` **coexist as distinct-sector modes** — the shared digits are magic-angle coincidences, "NOT an identity." The observed GW is deliberately kept on the T2/shear channel at **exactly `c`** (`einstein-field-equation.md:84`, `:97`), which is what makes AVE consistent with GW170817's `|c_GW−c_EM|/c ≲ 10^{-15}` `[import]` **for the tensor mode**. Coexistence per se is not a contradiction: the lattice has a preferred frame (emergent-Lorentz with a substrate rest frame), so a mode faster-than-`c` is not a logical inconsistency *within* AVE.

**Where the conflict actually bites — radiative vs reactive.** The tension is created *only if the superluminal channel RADIATES to the far field*:
- The band-map showed deep-space slow matter is doubly protected from the `√2·c` channel (sub-threshold + evanescent-for-the-gapped-branch); but a **compact binary is a strong, fast, quadrupolar source**, not slow matter — none of those protections apply. If the A1 channel has a radiative port (§3.3 Q1), the binary drives it.
- A radiated `√(10/3)·c ≈ 1.83·c` scalar burst carrying an O(0.1) energy fraction would **outrun the tensor GW/EM front by ~`4.5×10^7`–`5.9×10^7` yr** over GW170817's `~40 Mpc` (driver: `research/drivers/scalar_gw_bulk_channel.py`; `38 Myr` at `√2·c`, `59 Myr` at `√(10/3)·c`). It would not be a *time-associated* precursor we could tag to GW170817 (we cannot look 50 Myr back on one event); the real observable consequence is (a) a **standing population** of superluminal scalar bursts decoupled from their EM/tensor counterparts, and (b) the **energy budget**: `~5`–`18%` of a binary's radiated energy leaving in a channel that LIGO's tensor-tuned pipeline does not see would perturb the inferred source energetics/distance (GW170817's GW distance agrees with the NGC 4993 host distance at the `~10`–`20%` level `[import]`, bounding an anomalous flux fraction at that scale).

**Net coexistence verdict.** Coexistence of the *static/reactive* `√2·c` bulk **port** (impedance, reflection at saturation walls) with the observed `c` shear GW is **consistent** — this is the corpus's established position and it is fine. What is NOT established, and what this lane exposes, is whether the same bulk sector has a **far-field radiative port**; if it does, the superluminal radiated wave (`√(10/3)·c`) is the sharpest observational tension. The two-speed coexistence is safe for reactance, contested for radiation.

---

## §7 — VERDICT (multipole-by-multipole) + the fork (fail-closed) + ledger + flags

### §7.1 — Multipole-by-multipole verdict

| Order | Bulk-channel verdict | Mechanism | Robustness |
|---|---|---|---|
| **Monopole** | **NON-RADIATING** | `\dot M_{\rm tot}=0` (mass-energy conservation) | theorem, robust (same class as GR monopole kill) |
| **Dipole** | **NON-RADIATING** | `\ddot d = \dot P_{\rm tot}=0` (momentum conservation); AVE-**strengthened** — scalar-charge = inertial-mass exactly ⇒ no compact-object revival (unlike Brans-Dicke) | theorem, robust; assumption D1 (mass=A1-dilatation SEP-exact) is consistency-class |
| **Quadrupole** | **RADIATIVE** | same nonzero rotating mass quadrupole as T2/GW; no conservation law left to kill it | derived; **conditional on Q1** (A1 is an independent radiative DOF) |

### §7.2 — HEADLINE

**The bulk channel is NOT the non-radiating outcome.** Monopole and dipole are cleanly killed by conservation laws (the dipole-kill is a genuine AVE consistency *success* vs scalar-tensor). But the **quadrupole radiates**, and with an O(1) coupling (`K=2G`, no large suppression parameter) the predicted scalar admixture is **`h_bulk/h_shear ~ 0.2`–`0.4` — large**. Against the LIGO handles this is **CONSTRAINED, leaning EXCLUDED** (§5.4 row 1): pure-scalar is already excluded (`~10^20` Bayes, GW170817), a large admixture is in tension with polarisation content, and the superluminal `√(10/3)·c` propagation is the sharpest conflict.

**Fail-closed status: UNDETERMINED-leaning-EXCLUDED.** The verdict is pinned to one **unforced choice** (assumption Q1): *does the A1/bulk-dilatation sector have an independent far-field radiative port?*
- **Reading A (independent elastic radiative DOF):** large scalar-GW admixture ⇒ **kill-class**, EXCLUDED/CONSTRAINED. This is the elastic-medium *default*.
- **Reading B (constrained/near-field-reactive-only, as GR's longitudinal metric parts are pure-gauge):** no scalar-GW ⇒ **UNTOUCHED** — but then the corpus **owes a mechanism** for why a mode that propagates freely at `√(10/3)·c` in its linear passband does not radiate from a strong quadrupolar source.

Neither reading is forced by current canon ⇒ **fork surfaced, not decreed** (per the discipline). The physics ruling — is the A1/bulk radiative port real? — is a **Grant/auditor sector-ownership adjudication**, exactly the question FLAG-1 (band-map D5) named. This lane sharpens it from "unstated" to "the choice carries a kill-class consequence in Reading A."

### §7.3 — Calibration-vs-derived ledger (`consistency-vs-emergence` tags)

| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| monopole/dipole kill | `[derived]` (conservation theorems) | — | manifestation (theorem of conservation) |
| dipole no-revival (SEP-exact) | `[derived]` given D1 | — | consistency (rides on mass=A1-dilatation, not driver-validated) |
| `P_bulk/P_shear|_speed = (c_s/c_long)^5` | `[derived]` multipole flux scaling | `0.177` (√2) / `0.049` (√10/3), dimensionless | manifestation (calibration-free) |
| `K=2G` ⇒ O(1) coupling (no `1/ω_BD`) | `[derived]` from `[canon]` `K=2G` | — | consistency (`K=2G` is GR-imported) |
| `h_bulk/h_shear ~ 0.2`–`0.4` | `[derived]` speed × O(1) coupling | dimensionless, O(1)-bracketed | **the headline ratio** (robust to FLAG-B bracket) |
| precursor lead `38`–`59 Myr` (GW170817) | `[derived]` `(D/c)(1−c/c_long)` | `D≈40 Mpc` `[import]` | consistency (astro-imported distance) |
| LIGO pure-scalar Bayes `~10^20` | — | `[import]` Abbott 2019 (exact figure owed) | import |

**Headline discipline:** the only calibration-free content is the speed suppression (`2^{-5/2}`, `(3/10)^{5/2}`) and the O(1)-coupling argument. No emergence-class claim is headlined; the ratio is the deliverable and it rides on the fork (Q1), not on a hidden calibration.

### §7.4 — Deviations + contradictions (flag-don't-fix)

- **FLAG-A (carried, band-map channel-3 speed label).** The band-map table (`research/2026-07-19_deep-space-band-map_derivation.md:58`) labels the bulk channel `√2·c`. That is the **port/impedance** speed (`Z_bulk=ρc_bulk`, `constants.py` `V_LONG`); the **far-field radiative** longitudinal wave is the P-wave `√(10/3)·c` (`constants.py:778`; c_L-reconciliation Rule-12 notes `mond-hoop-stress.md:43`, `lc-electrodynamics.md:28`, all `[canon]`). Radiation should use `√(10/3)·c`; reflection/port uses `√2·c`. Surfaced, not fixed — the band-map/KB leaves are not edited by this lane (DERIVATION fence). **Both are superluminal**, so §6's conclusion is robust to the fork.
- **FLAG-B (O(1) prefactor unpinned).** The exact bulk/shear power ratio needs the elastodynamic P-vs-S angular-partition integral of a rotating quadrupole. Bracketed O(1); satellite-driver follow-on. Does not move the headline (large vs tiny).
- **Contradiction surfaced (Q1, the load-bearing fork).** The corpus simultaneously (i) treats A1/bulk as a **real propagating channel** with its own speed and impedance (band-map, three-speeds table, `Z_bulk`), and (ii) reproduces GR — in which the scalar/longitudinal gravitational sector is **pure-gauge and non-radiating**. If (i) is taken at face value for the far field, Reading A follows and the framework faces the GW-polarisation kill. If (ii) governs the radiative sector, Reading B follows and A1/bulk is reactive-only for gravity. **These are in tension for the radiative case; the corpus has not stated which governs.** Flagged for Grant/auditor — not reframed to match either side.

---

## §8 — OWED-FOLLOW-ONS (fenced this session; not executed here)

Per substitution-not-retraction (Rule 12 / A47 v11b) and the DERIVATION-lane fence, this doc mints nothing and edits no leaf. The owed items:

1. **FLAG-1 (band-map D5) resolution = a Grant/auditor sector-ownership ruling** on assumption **Q1**: does the A1/bulk-dilatation sector have an independent far-field radiative port (Reading A), or is it constrained/reactive-only for gravity (Reading B)? This lane provides the material — the ruling carries a **kill-class consequence in Reading A** (large scalar-GW admixture, EXCLUDED/CONSTRAINED). *Grant-gated physics ruling first; then auditor lane lands any leaf.*
2. **FLAG-A speed-label reconciliation** in the band-map channel-3 row (`√2·c` port vs `√(10/3)·c` radiative P-wave). *Auditor lane; not edited here.*
3. **FLAG-B exact-prefactor driver** — a satellite driver computing the elastodynamic P-vs-S angular-partition of a rotating mass quadrupole, to pin the O(1) factor and turn `h_bulk/h_shear ~ 0.2`–`0.4` into a sharp number for a decisive LIGO comparison. *Satellite / number-generating lane.*
4. **Exact LIGO Bayes-factor verification** — re-verify the pure-scalar/pure-vector rejection figures against Abbott et al. 2019 (§5.1) before any leaf headlines a numeric bound. *Owed cite-check.*

**None of items 1–4 are executed here.** The FLAG-1 slot stays **open** (not refilled with an asserted resolution); this derivation is a new lane with its own verification chain that *frames* the fork with its quantitative consequence, and leaves the ruling to Grant.

---

> **Derivation-doc provenance.** Fired by Grant 2026-07-20 (`"5. derive either way?"` `[sic]`). All `[canon]` citations content-verified at HEAD `64f1894d` (verify-before-cite). FORMs `[derived]` by standard multipole/elastodynamic-radiation algebra from `[canon]` inputs; dimensionful VALUEs `[import]`-tagged (CODATA `c`, GW170817 distance/bounds, LIGO polarisation Bayes factors). Arithmetic reproduced by `research/drivers/scalar_gw_bulk_channel.py` (+ `_results.json`), which imports `ave.core.constants.C_0` read-only. Mints no `clm-`; propagates to no leaf; owed follow-ons fenced to §8. Verdict: **monopole/dipole NON-RADIATING (theorems); quadrupole RADIATIVE; headline `h_bulk/h_shear ~ 0.2`–`0.4` ⇒ CONSTRAINED-leaning-EXCLUDED in the independent-radiative-DOF reading; fail-closed UNDETERMINED on the Q1 fork.** Companion: the band-map derivation (`research/2026-07-19_deep-space-band-map_derivation.md`, FLAG-1/D5) and the docket continuation (`_orchestration/2026-07-10_rulings-docket.md`, ENTRY 27).
