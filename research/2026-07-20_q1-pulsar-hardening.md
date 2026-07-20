# Q1 HARDENING — the pulsar-timing budget + the exact bulk/shear quadrupole flux prefactor

**Date:** 2026-07-20
**Class:** DERIVATION + research-driver (research-doc; **forms derived, values calibration/observation-imported and tagged; mints no `clm-`, propagates to no KB/tex leaf**). Hardens the **Q1** open row of the port register (`research/2026-07-20_port-register_draft.md` §3) and the scalar-GW bulk-channel exposure (`#750`, `research/2026-07-20_scalar-gw-bulk-channel_derivation.md`).
**Provenance:** Grant-fired 2026-07-20 (`"fire the port channel lane and continue it"` `[sic]`). This doc executes two of the #750 owed follow-ons: (§8 item 3) the **exact O(1) prefactor** #750 FLAG-B left bracketed, and the **pulsar-timing budget** (a cleaner kill surface than the LIGO single-event handle #750 used). Numeric arithmetic reproduced by `research/drivers/q1_pulsar_timing_budget.py` (+ `_results.json`), which derives the channel speeds from `ave.core.constants` (K=2G) read-only and touches no engine primitive.
**Lane fences:** DERIVATION lane only. **No** engine edits; **no** `manuscript/` or `manuscript/ave-kb/` `.tex`/`.md` leaf edits; **no** edits to #748/#750/#751 branch files. Every `[canon]` input content-verified two-method at HEAD `64f1894d` (verify-before-cite). Pulsar figures `[import]`-tagged and WebFetch-verified against the source abstracts this session.
**Headline (stated plainly, both ways, no thumb on the scale):** Under **Reading A** (the A1/bulk channel has an independent far-field radiative port), the extra flux fraction `F_bulk/F_shear ≈ 0.03–0.12` is **EXCLUDED at 9–110σ by Hulse-Taylor and by a factor 100–1400× the double-pulsar bound** — a decisive kill across the entire FLAG-A speed × O(1)-coupling range. Under **Reading B** (constrained / reactive-near-field-only), pulsar timing is silent (consistent) — but the corpus **owes a suppression derivation**. **The Q1 ruling is Grant's** (§4).

---

## §0 — REGIME / SECTOR / PHASE-STATE header (fired before any budget algebra)

**MODE.** A non-relativistic compact binary in the inspiral (Hulse-Taylor B1913+16, `v/c ~ 10⁻³`; double pulsar J0737-3039A/B, `v/c ~ 2×10⁻³`) as a **source** driving the deep vacuum. Contrast column: the observed orbital-decay `Ṗ_b`, matched to the GR shear-quadrupole to `[import]`-tagged precision.

**REGIME.** **Regime I** — deeply linear far field (`V_GW/V_snap ~ 10⁻²⁵`, `08_gravitational_waves.tex:60-66` `[canon]`); the lattice "acts as a perfect lossless linear transmission line." Saturation (Op14) does not enter the propagation.

**PHASE-STATE.** **Cold-reactive** (Ax3-lossless-reactive; `eq_axiom_3.tex:24` `[canon]`). Far-field **radiation is a legal Ax3 loss channel** (a radiative port — port-not-valve), so a radiating bulk channel does NOT violate Ax3; that is why Q1 is a live question, not an Ax3-forbidden one.

**SECTOR.** The observed GW = **T2 transverse shear** at `c` (`einstein-field-equation.md:62-63,84` `[canon]`). The channel under test = **A1 bulk dilatation**, radiative speed `√(10/3)·c` (FLAG-A, port register §1). **Sector-ownership discipline:** A1 owns compression/mass/dilatation; T2 owns shear/GW — do NOT cross-wire. The binary's masses ARE the A1-dilatation content (`master-equation.md:20` "A1 dilatation-MASS" `[canon]`), so the source is genuinely an A1 source.

**SUBSTRATE-NATIVE + PHASE-SPACE-COORDINATE CHECK (A46).** The corpus claim is a *channel-radiation* claim (does the A1 branch carry a far-field port?); the matching test coordinate is the **radiated-flux decomposition in the channel basis** (A1 dilatation vs T2 shear), and the **energy budget of the binary's orbital decay** (`Ṗ_b`), measured in that basis. The pulsar test measures `Ṗ_b` (the total radiative energy-loss rate) — the correct matching coordinate for a "which channels carry the radiated power" claim. Not a real-space lattice-Cartesian strain the corpus never claimed.

---

## §1 — The exact bulk/shear quadrupole flux prefactor (the #750 owed FLAG-B follow-on)

#750 derived the calibration-free **speed suppression** `(c_shear/c_long)^5` and argued the coupling is O(1) (`K=2G`, no `1/ω_BD`), but left the exact angular/tensor-structure prefactor **bracketed at O(1)** (its FLAG-B). This section pins it.

### §1.1 — Setup: both channels sourced by the SAME rotating mass quadrupole `[derived]`

Both the bulk (A1, longitudinal/P) and shear (T2, transverse/S — the observed GW) channels are driven by the **same** rotating mass quadrupole `Q_ij` of the binary (port register §1; #750 §2.2 — because mass = A1-dilatation, the bulk source moments ARE the mass moments). In the far field of an isotropic elastic medium a moment-tensor source `M_ij ∝ Q̈_ij` radiates both a longitudinal (P) and a transverse (S) wave (standard elastodynamics; Aki-Richards far-field moment-tensor radiation):

$$u^P_i \;\propto\; \frac{\gamma_i\,\gamma_p\,\gamma_q}{\rho\,c_L^3}\,\dot M_{pq},\qquad u^S_i \;\propto\; \frac{(\delta_{ip}-\gamma_i\gamma_p)\,\gamma_q}{\rho\,c_T^3}\,\dot M_{pq},$$

with `γ_i` the radial direction cosines, `c_L` the longitudinal (P) speed, `c_T` the transverse (S) speed. The radiated power is `P = ∮ ρ c ⟨u̇²⟩ r² dΩ`.

### §1.2 — The angular partition `[derived, calibration-free]`

Carrying the flux integral (the `1/(ρ² c^6)` amplitude × `ρ c` flux × `r²` cancels to `1/(ρ c^5)` × an angular integral of the traceless symmetric `M`):

$$P_{\rm long} \;=\; \frac{\langle|\ddot M|^2\rangle}{\rho\,c_L^5}\cdot\underbrace{\oint |\gamma_p\gamma_q \hat M_{pq}|^2\,d\Omega}_{=\,(8\pi/15)\,|M|^2},\qquad P_{\rm shear} \;=\; \frac{\langle|\ddot M|^2\rangle}{\rho\,c_T^5}\cdot\underbrace{\oint |(\delta-\gamma\gamma)\!\cdot\!(\gamma\!\cdot\!\hat M)|^2\,d\Omega}_{=\,(4\pi/5)\,|M|^2}.$$

The two angular integrals are standard results for a traceless symmetric `M` (using `∮γ_iγ_jγ_kγ_l dΩ/4π = (1/15)(δδ+δδ+δδ)`):
- **Longitudinal (P):** `∮|γ_pγ_q M_pq|² dΩ = (8π/15)|M|²` (the `l=2` radial projection).
- **Transverse (S):** `∮|(δ-γγ)·(γ·M)|² dΩ = (1/3 − 2/15)·4π|M|² = (4π/5)|M|²`.

The **angular-partition factor** is their ratio:

$$\boxed{\ \mathcal{A}_{\rm ang} \;\equiv\; \frac{(8\pi/15)}{(4\pi/5)} \;=\; \frac{2}{3}\ }\qquad\text{(derived, dimensionless, calibration-free).}$$

### §1.3 — The headline dimensionless flux ratio `[derived]`

Combining the angular partition with the speed suppression, and taking the **equal-coupling** default (the same moment tensor `M` sources both channels — the natural elastic-medium reading, #750 §4.2: `K=2G` ⇒ no large suppression parameter):

$$\boxed{\ \frac{F_{\rm bulk}}{F_{\rm shear}} \;=\; \mathcal{A}_{\rm ang}\cdot\left(\frac{c_{\rm shear}}{c_{\rm long}}\right)^{5} \;=\; \frac{2}{3}\left(\frac{c}{c_{\rm long}}\right)^{5}\ }$$

evaluated at the two FLAG-A speeds (driver `q1_pulsar_timing_budget.py`, speeds derived from `constants.py` K=2G):

| `c_long` (FLAG-A) | `(c_shear/c_long)^5` | `F_bulk/F_shear = (2/3)·(…)` |
|---|---|---|
| **`√2·c`** (A1 port/impedance speed; `V_LONG`) | `2^{-5/2} = 0.1768` | **`0.1179`** |
| **`√(10/3)·c`** (radiative P-wave; the physical far-field speed per FLAG-A) | `(3/10)^{5/2} = 0.0493` | **`0.0329`** |

**Honest O(1) bracket (consensus knife both ways).** `A_ang = 2/3` is the P/S angular partition for the *elastic vector S-wave* comparison; if the observed GW is treated as a *spin-2 TT* mode the exact factor shifts but stays O(1), and the coupling ratio `κ_L/κ_T` (equal in the elastic default) could plausibly range `[0.5, 2]²`. Bracketing `A_ang·κ² ∈ [0.3, 1.0]`:

$$\frac{F_{\rm bulk}}{F_{\rm shear}} \;\in\; [\,0.0148,\ 0.1768\,]\qquad(\text{min: }A=0.3,\,\sqrt{10/3}\,c;\ \text{max: }A=1.0,\,\sqrt2\,c).$$

**The headline is robust to the bracket: `F_bulk/F_shear` is O(0.01–0.2) — a LARGE, same-order admixture, not the `~1/ω_BD` tiny of viable scalar-tensor gravity.** The exposure survives the honest prefactor pinning.

**Ledger tag (`consistency-vs-emergence`):** `A_ang = 2/3` is **[derived]**, MANIFESTATION-class (a theorem of the isotropic-elastic P/S angular integral). The speed factor is **[derived]**, calibration-free. The equal-coupling default rides on the `K=2G` sector identity, which is **GR-imported** (`constants.py:385`, PR#261) — CONSISTENCY-class, not emergence. No emergence-class claim is headlined; the deliverable is the dimensionless ratio.

---

## §2 — The pulsar-timing budget (a cleaner kill than the LIGO single event)

### §2.1 — Why pulsar timing is the sharp handle `[derived]`

#750 §5.2 flagged that a **single LIGO event's** phasing only weakly constrains a *same-order (0PN)* scalar quadrupole, because the overall flux rescaling is **partially degenerate with the chirp mass** (an extra 0PN channel reabsorbs into the inferred masses). **Pulsar timing breaks exactly this degeneracy:**

- In a binary pulsar the **masses are measured INDEPENDENTLY** from the *conservative* post-Keplerian (PK) parameters — periastron advance `ω̇`, Einstein delay `γ`, Shapiro `r` & `s` — and (in the double pulsar) the mass ratio `R` from timing both pulsars. These are **near-field / conservative-sector** effects.
- The **radiative** PK parameter `Ṗ_b` (orbital decay) is then an **over-determined consistency check**: `Ṗ_b^GR` is *predicted* from the independently-pinned masses and compared to the observed decay.
- An anomalous **radiative** channel therefore shows up as a `Ṗ_b` that disagrees with the mass values pinned by the conservative parameters — **NOT absorbable into a chirp-mass rescaling.** This is precisely why pulsar timing is the well-bounded scalar-tensor observable and why it is the right hardening surface for Q1.

**Both readings agree on the conservative sector.** The corpus already claims GR-consistency for periastron advance (the ponderomotive `n_scalar` derivation, structurally identical to GR — `claim-quality-closure-roadmap.md:204` `[canon]`; `anomalous-perihelion-advance.md` `[canon]`). Under Reading B the near-field (DM-halo-like reactance, port register P9) shapes the conservative dynamics and is GR-matched; under Reading A the conservative sector is unchanged. So the **only** discriminator is the *radiative* budget `Ṗ_b`.

### §2.2 — The two imported budgets `[import]`

| System | Observed `Ṗ_b` vs GR shear-quadrupole | Fractional precision | Source `[import]` (WebFetch-verified 2026-07-20) |
|---|---|---|---|
| **Hulse-Taylor B1913+16** | `0.9983 ± 0.0016` (obs/GR, Galactic-corrected) | `δ_HT ≈ 0.0016` (1σ) | Weisberg & Huang 2016, ApJ **829**, 55 (arXiv:1606.02744), abstract verbatim |
| **Double pulsar J0737-3039A/B** | GR quadrupolar-GW prediction validated at `1.3×10⁻⁴` (95% conf.) | `δ_DP ≈ 1.3×10⁻⁴` (frac. bound) | Kramer et al. 2021, PRX **11**, 041050 (arXiv:2112.06795), abstract verbatim |

**Corpus cross-check (consistency reproduction).** The corpus's own Hulse-Taylor treatment (`08_gravitational_waves.tex:73-83` `[canon]`) models B1913+16 as a macro-LC orbital tank and **reproduces the observed decay to `~2%`** — but it explicitly **carries over the Peters-Mathews `(v/c)^5` quadrupole scaling from the standard (shear) radiation formula** ("a consistency reproduction rather than an independent first-principles derivation"). So the corpus's `Ṗ_b = −2.402×10⁻¹² s/s` IS the GR shear-quadrupole. **NB the corpus's `~2%` is the circuit-model's *reproduction accuracy*, NOT the observational precision** — the tight constraint on an *extra* channel is the `δ_HT ≈ 0.16%` (Weisberg-Huang) / `δ_DP ≈ 1.3×10⁻⁴` (Kramer) observational agreement, imported above.

### §2.3 — The exclusion significance under Reading A `[derived]`

Under Reading A the bulk quadrupole radiates ON TOP of the shear quadrupole, so `Ṗ_b^AVE = Ṗ_b^GR·(1 + F_bulk/F_shear)`. The observed `Ṗ_b` matches the GR shear-quadrupole to the fractional precision `δ`, so an extra fraction `F` is in tension at `F/δ` (driver `q1_pulsar_timing_budget.py`):

| `F_bulk/F_shear` | Hulse-Taylor `F/δ_HT` | Double pulsar `F/δ_DP` |
|---|---|---|
| `0.0148` (min bracket: `A=0.3`, `√(10/3)·c`) | **9.2σ** | **114×** the bound |
| `0.0329` (headline, P-wave `√(10/3)·c`, `A=2/3`) | **20.5σ** | **253×** the bound |
| `0.1179` (headline, port `√2·c`, `A=2/3`) | **73.7σ** | **907×** the bound |
| `0.1768` (max bracket: `A=1.0`, `√2·c`) | **110.5σ** | **1360×** the bound |

$$\boxed{\ \textbf{Reading A ([radiative bulk port + O(1) coupling]) is EXCLUDED at }9\text{–}110\sigma\text{ (Hulse-Taylor) and by }100\text{–}1400\times\text{ the double-pulsar bound}\ (\gtrsim 200\sigma\text{-equiv.}).\ }$$

**Stated plainly (Rule 11 honesty, no thumb on the scale):** the exclusion is DECISIVE across the *entire* plausible range — the smallest defensible admixture (`A=0.3`, the more-suppressed `√(10/3)·c` speed) still exceeds the double-pulsar bound by 114× and the Hulse-Taylor precision by 9σ. There is **no corner of the FLAG-A speed × O(1)-coupling grid where Reading A survives pulsar timing.** If Reading A is the physics, this is a **clean kill-class result to bank.**

### §2.4 — ★The load-bearing corpus contradiction this exposes (flag-don't-fix)

The manuscript **already carries** the Q1 fork as an unresolved contradiction, verbatim in `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex`:
- **Step-3 of the Hulse-Taylor `P_real` derivation:** *"real power radiates radially outwards into the **bulk lattice network**"* — attributing the orbital-decay radiated power to the **bulk / longitudinal** channel.
- **The same chapter's summary + KB canon:** GW propagate *"exclusively as lossless, trace-free, **transverse** impedance modulations"*; the KB assigns GW to the **transverse shear** channel (`gw-propagation-lossless.md`, `three-channel-impedances.md` "Shear / GW" row).
- The manuscript's own **`warningbox`** flags this as *"unresolved channel attribution"* and notes it was independently surfaced by the vacuum-impedance-probe Phase-A result and the 2026-07-03 longitudinal-energy-budget audit.

**This IS Q1 surfacing inside the existing manuscript.** If the HT decay is *bulk* (as step-3 says) AND the GW is *shear* (as the summary + KB say), the two channels **double-count** the same orbital-decay energy — which pulsar timing (matched to a single quadrupole channel) forbids. The register's Q1 fork is not a new hypothetical; it is the resolution of a contradiction the corpus has been carrying. **Flagged for Grant/auditor; NOT reframed to match either side** (fence: `08_gravitational_waves.tex` not edited by this lane).

*Review-repair W1 (2026-07-20) — the lightest reading, added so the ruling is not pre-framed:* step-2 of the same chapter (`:78`) pins the decay wave's propagation at **`c₀` — the SHEAR speed**, which is internal textual evidence that step-3's "bulk lattice network" may be **loose prose for "the surrounding medium"** (a shear emission), not the A1 bulk channel. Under that reading the warningbox resolves by a **standalone wording fix** (step-3 → "shear") with **no physics fork**, and Q1 remains a separate theoretical question. The adjudication menu is therefore THREE-way: (a) genuine bulk-channel double-count → resolves with the Q1 ruling; (b) loose prose → one-line wording fix, Q1 unaffected; (c) hold. One-sentence question for Grant: *is step-3's "bulk lattice network" the A1 channel, or just the medium?*

---

## §3 — The Reading-B obligation, sharpened: candidate suppression mechanisms

If Grant rules **Reading B** (the bulk sector is constrained / reactive-near-field-only for gravity), pulsar timing is silent and the framework survives — **but the corpus then owes a derivation** for why a mode that propagates freely at `√(10/3)·c` in its linear passband does not radiate from a strong quadrupolar source. This section **enumerates the candidates and what each derivation would need to show — it does NOT pick one** (per the discipline; the ruling is Grant's, §4).

**★First, a FALSE rescue to rule out up front (consensus knife against the framework).** The band-map **Cherenkov/Mach drag-onset threshold** (`v_crit = 0.80 c_ch` srs arccos / `2/π` cosine; port register P6) does **NOT** save Reading B. That threshold is for a **STEADY-drift source dragging a near-field** (deep-space matter, `v ≪ v_crit`, doubly protected). A binary is an **accelerated multipole** radiating at `2Ω`; for a *gapless* channel (channels 1-3 all propagate to DC) an oscillating quadrupole emits a propagating wave at `k = 2Ω/c_ch` with **no velocity threshold**. HT/J0737 are sub-Cherenkov (`v~10⁻³c`) yet radiate copious *shear* GW for exactly this reason — so the same non-threshold logic drives the *bulk* channel under Reading A. Invoking `v_crit` to close the Q1 port would be an inapplicable-threshold rescue; it is ruled out here so it cannot be reached for later. (This is #750 §6's "none of those protections apply" made explicit.)

**Candidate B1 — Constraint / gauge-like slaving of the longitudinal sector (the GR mechanism).**
- *Statement:* In GR the longitudinal/scalar metric parts are **pure-gauge** (fixed by the Hamiltonian & momentum constraints / diffeomorphism invariance); only the 2 TT polarizations propagate. If the A1/bulk sector is similarly **constrained** — slaved to the instantaneous matter distribution by an *elliptic* (Poisson-like, near-zone) equation rather than a *hyperbolic* (retarded, radiative) one — it has no independent far-field radiative DOF.
- *What a derivation must show:* that for gravitating sources the A1 dilatation obeys a **constraint** `∇²φ = source` (instantaneous potential) rather than `□φ = source` (radiative wave) — i.e., the "√2·c channel" is the near-zone gravitational potential, not a propagating d'Alembertian mode.
- *The tension it must resolve:* this **directly contradicts** the band-map's treatment of channel 3 as a *gapless propagating acoustic branch* (port register §1). The derivation must reconcile "propagating channel in the band structure" with "constrained/non-radiating for gravity" — perhaps via the FLAG-A split (the `√2·c` port mode is the constrained near-field potential; the `√(10/3)·c` radiative mode is what must be shown absent/decoupled).

**Candidate B2 — Incompressibility / dilatational source-term vanishing.**
- *Statement:* The bulk channel is sourced by `∇·f`. If the effective vacuum is **incompressible at the radiative scale** (`∇·u → 0`), or if the mass-quadrupole's *radiative* dilatation projection `∇·f` vanishes, the channel isn't driven.
- *What a derivation must show:* that a compact binary's stress source has vanishing (or strongly suppressed) **radiative** dilatational projection at quadrupole order — e.g., the mass concentrations couple to the far field purely through *shear* (transverse) stress.
- *The tension it must resolve:* this **fights the sector identity "mass = A1-dilatation"** (#750 §3.2). If mass IS dilatation, the *near-field* source is manifestly dilatational (that is the halo, P9). The derivation must show the *far-field radiative* coupling of the mass quadrupole to the dilatation channel vanishes **even though** the static/near-field dilatation is the mass — a non-trivial separation of near-field storage from far-field radiation. (FLAG-A gives the structural handle: near-field = `√2·c` reactive; far-field radiative = `√(10/3)·c`, which is what must vanish.)

**Candidate B3 — The DM-near-field-coherence single-structure argument (the task's framing).**
- *Statement:* Whatever closes the binary's radiative bulk port must be the **same structure** that leaves the halo reactive. The DM halo IS the bulk channel's reactive near-field (added-mass; port register P9). If the bulk channel is reactive-near-field-only **universally** — the same reason the halo doesn't drain — then the binary also sees only reactive near-field, no radiative port.
- *What a derivation must show:* a **single mechanism** that (a) gives the halo its added-mass reactance (rotation curves, no loss) AND (b) forbids the binary's quadrupole from opening a radiative bulk port. **The FLAG-A split makes this *cleaner* than a single-structure requirement:** the halo uses the `√2·c` *port/impedance* mode (established reactive; P9), while the radiative question is about the *separate* `√(10/3)·c` P-wave. So B3 reduces to B1/B2 restricted to the radiative mode — "the `√2·c` reactive port shapes the halo; show the `√(10/3)·c` radiative P-wave is constrained/decoupled." The single-structure obligation is *already partly discharged* by the two modes being structurally distinct.

**Candidate B4 — Gapping / stopband of the radiative bulk sector.**
- *Statement:* If the **radiative** bulk mode is actually *gapped* (like the Cosserat channel 4, `m_ω ~ c/ℓ_node`) rather than gapless, then below the gap there is no propagating mode and the coupling is **evanescent** (reactive near-field, decay `~ℓ_node`). The binary's `2Ω` is astronomically far below any lattice-scale gap ⇒ reactive-only.
- *What a derivation must show:* that the far-field radiative bulk mode (the `√(10/3)·c` P-wave) is **gapped or otherwise non-propagating** for gravitating sources, even though the reactive `√2·c` port mode is gapless — i.e., the two FLAG-A modes have **different band structures**.
- *The tension it must resolve:* the band-map explicitly classifies channel 3 (bulk) as **gapless** (propagates to DC, port register §1). B4 requires re-deriving the radiative bulk mode as gapped — the strongest departure from current canon of the four, but the one that would most cleanly explain the null.

**Cross-cutting note.** B1-B4 are not mutually exclusive; B1 (constraint) is the GR-analog and the most conservative (it is *how GR itself* avoids scalar GW), and B3/B2/B4 are increasingly substrate-specific mechanisms for the same end. **All four must survive the FLAG-A observation that the halo (√2·c reactive) and the radiative port (√(10/3)·c) are already distinct modes** — which is why the register carries FLAG-A as a column, not a footnote. **This lane picks none; it hands Grant the menu with each derivation's obligation named** (§4).

---

## §4 — Q1 ADJUDICATION PACKAGE FOR GRANT (walk-brief)

**The question (one line).** Does the A1/bulk-dilatation sector have an **independent far-field radiative port** for a gravitating quadrupole source (Reading A), or is it **constrained / reactive-near-field-only** for gravity (Reading B)?

**The hardened numbers on the table.**
- Under **Reading A**, the derived extra flux is `F_bulk/F_shear = (2/3)·(c_shear/c_long)^5 ≈ 0.033` (radiative `√(10/3)·c`) to `0.118` (port `√2·c`), bracket `[0.015, 0.177]` over the O(1) coupling.
- Pulsar timing **excludes** that at **9–110σ (Hulse-Taylor)** and **100–1400× the double-pulsar bound**. No corner survives.
- The FLAG-A speed split is confirmed in canon (`constants.py:770-781`); the halo (`√2·c` reactive, P9) and the radiative port (`√(10/3)·c`) are **already distinct modes**.
- The manuscript **already carries the fork as an unresolved contradiction** (`08_gravitational_waves.tex` warningbox: HT decay attributed to *bulk* vs GW-canon *shear*).

**The options (bulleted; decision is yours):**
- **Rule A (bulk radiates).** Bank a **clean kill-class result**: AVE's elastic-medium default predicts a large scalar-GW admixture that pulsar timing excludes at ≫100σ. This would be a **falsification of the naive elastic-bulk-radiates reading** — a genuine, bankable negative (Rule 11 honest closure). *Consequence:* the corpus must either abandon the independent-bulk-radiative-DOF reading or accept a falsified prediction. The `08_gravitational_waves.tex` step-3 "radiates into the bulk lattice" wording would be **wrong** and owe a correction to *shear*.
- **Rule B (bulk constrained / reactive-only).** The framework survives (pulsar timing silent), but you **open a suppression-derivation lane** owing one of B1-B4 (§3) — most naturally **B1** (GR-like constraint slaving) restricted via FLAG-A to the `√(10/3)·c` radiative mode. *Consequence:* the band-map channel-3 "gapless propagating" treatment must be reconciled with "non-radiating for gravity," and the `08_gravitational_waves.tex` step-3 wording still owes a correction (the decay is *shear*, the bulk is reactive-near-field).
- **Defer (fork stays open).** Keep the register Q1 row OPEN; the exposure is documented and the branch-state cites (#750/#751) merge first. *Consequence:* the manuscript contradiction (warningbox) stays live; no bank either way.

**Implementer recommendation (surfaced, not decreed).** The numbers point hard: Reading A is excluded ≫100σ, so either (a) Reading B is the physics and a B1-style constraint derivation is owed, or (b) Reading A is banked as a falsified prediction. **Both are legitimate honest-closure outcomes.** The one move the discipline forbids is debugging toward a rescue via the inapplicable Cherenkov threshold (ruled out, §3). **Your call, Grant** — this lane hands you the hardened fork, not a verdict.

---

## §5 — Calibration-vs-derived ledger + OWED-FOLLOW-ONS

### §5.1 — Ledger (`consistency-vs-emergence` tags)

| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| `A_ang = 2/3` (P/S angular partition) | `[derived]` (elastic angular integrals) | dimensionless | **MANIFESTATION** (theorem) |
| `(c_shear/c_long)^5` speed factor | `[derived]` (multipole flux scaling) | `0.177` (√2) / `0.049` (√10/3) | manifestation (calibration-free) |
| `F_bulk/F_shear ≈ 0.03–0.12` | `[derived]` `= (2/3)·(c_s/c_L)^5` | dimensionless, O(1)-bracketed | **the headline ratio** |
| speeds `√2·c`, `√(10/3)·c` | `[derived]` from `K=2G` | — | consistency (`K=2G` GR-imported) |
| HT `Ṗ_b` agreement `0.9983±0.0016` | — | `[import]` Weisberg-Huang 2016 | import (verified) |
| J0737 `Ṗ_b` bound `1.3×10⁻⁴` | — | `[import]` Kramer 2021 | import (verified) |
| exclusion `9–110σ` / `100–1400×` | `[derived]` `= F/δ` | — | manifestation (given imports) |

### §5.2 — OWED-FOLLOW-ONS (fenced; not executed here)

Per substitution-not-retraction (Rule 12) and the DERIVATION-lane fence, this doc mints nothing and edits no leaf. Owed:
1. **The Q1 ruling itself** — a Grant sector-ownership adjudication (§4). *Grant-gated; then auditor lands any leaf.*
2. **The `08_gravitational_waves.tex` warningbox resolution** — the channel-attribution contradiction (HT decay bulk-vs-shear) resolves *with* the Q1 ruling. *Auditor lane; not edited here.*
3. **Exact double-pulsar figure re-verification** — the `1.3×10⁻⁴` is a 95%-conf bound; the most recent intrinsic-`Ṗ_b` analysis may be tighter (`~6×10⁻⁵`). Either way the exclusion is unchanged; the exact figure is an owed cite-check before any leaf headlines it. *(Same discipline #750 applied to the LIGO Bayes factor.)*
4. **The FLAG-A band-map channel-3 speed-label reconciliation** (`√2·c` port vs `√(10/3)·c` radiative) — auditor lane, per the port register §4.
5. **If Reading B is ruled:** the B1-B4 suppression-derivation lane (§3) — a new lane with its own version number and verification chain (Rule 12: the Q1 slot is not refilled with an asserted resolution).

**None of items 1-5 are executed here.** The Q1 slot stays **open**; this doc *frames and hardens* the fork with its quantitative pulsar-timing consequence and leaves the ruling to Grant.

---

> **Hardening-doc provenance.** Fired by Grant 2026-07-20 (`"fire the port channel lane and continue it"` `[sic]`). All `[canon]` citations content-verified two-method at HEAD `64f1894d`; pulsar figures `[import]`-tagged and WebFetch-verified against source abstracts this session. FORMs `[derived]` by standard elastodynamic-radiation + multipole algebra; dimensionful VALUEs `[import]`-tagged. Arithmetic reproduced by `research/drivers/q1_pulsar_timing_budget.py` (+ `_results.json`), which derives channel speeds from `ave.core.constants` (K=2G) read-only. Mints no `clm-`; propagates to no leaf; owed follow-ons fenced to §5.2. Verdict: **Reading A EXCLUDED at 9–110σ (HT) / 100–1400× (J0737) — kill-class if ruled; Reading B survives but owes a B1-B4 suppression derivation; the Q1 ruling is Grant's.** Companion: the port register (`research/2026-07-20_port-register_draft.md`, Q1 row §3), #750 scalar-GW derivation, and the docket continuation (ENTRY 27).

---
## §6 — External anchor internalized (2026-07-20, Grant-directed): the seismology cross-validation + what it proves

**The receipt (previously review-ephemera; landed here).** The review's independent verification showed the same two angular integrals + the `1/c⁵` scaling reproduce the canonical seismological result for an isotropic (Poisson) elastic solid: `E_S/E_P = (I_S/I_P)·(V_p/V_s)⁵ = (3/2)·(√3)⁵ ≈ 23.4` (Aki & Richards, standard elastodynamics — `[import]`, external anchor). Our `A_ang = 2/3` is the inverse partition `I_P/I_S` of the identical integrals. An exact, non-AVE, textbook agreement — means-test PASS at value level, not order-of-magnitude.

**★What the anchor PROVES about Reading B (the sharpened obligation).** `E_S/E_P ≈ 23.4` means the P/bulk channel of a generic isotropic elastic solid **RADIATES** — weaker than shear, but copiously (every earthquake's P-arrival). Therefore **Reading B's suppression cannot come from generic elasticity**: a rock radiates bulk waves from a rotating quadrupole; the vacuum, per the pulsar exclusion (§2), must not. Whatever closes the vacuum's bulk port must be a structure the vacuum has and a rock lacks. Consequences for the §3 menu: **B2 (incompressibility / source-vanishing) must be DERIVED, not assumed** — real elastic solids are compressible and radiate; **B1 (constraint/gauge slaving)** and **B4 (gapped radiative bulk sector)** are precisely the non-generic structure class required. The mechanism lane's target, one sentence: *find the AVE-specific structure that makes the vacuum's bulk sector different from a rock's.*

**Routed follow-ons added (auditor lands; Grant-gated where noted):** (i) translation-table row per the EE-first-mapping landing discipline — "vacuum A1/T2 radiation partition ↔ seismological P/S partition (Aki-Richards; means-test PASS exact)" — rides the register canon-promotion; (ii) skill-candidate watch-list entry: seismology as a standing external-anchor toolkit for substrate elastodynamics (mode conversion at Γ walls; Rayleigh/boundary waves ↔ boundary-localized modes; evanescent head waves) — posture-B gated, watch-not-mint.
