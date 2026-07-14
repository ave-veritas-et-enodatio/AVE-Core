# F6 tier-1 — global two-reservoir ODE ledger (ρ_latent ↔ T2) — CHARTER

**Date:** 2026-07-13
**Class:** charter (draft the discriminator BEFORE any driver) — modeled on the #662 remanence-charter pattern (`research/2026-07-12_remanence-r10-fixed-n_CHARTER.md`: charter doc + frozen bins + fireable-vs-entailed + fool-modes + Ax3 carve). **Charter first; PR DO-NOT-MERGE; driver only after charter review.**
**Grant GO (Q4):** 2026-07-13 — ρ_latent parameterization licensed as INPUT-ONLY at `clm-s4n33u` solidity 0.45.
**Frozen prereg:** downstream sibling file (`research/2026-07-13_f6-tier1-two-reservoir-ledger_prereg_FROZEN.md`) — **not created in this commit**; freeze-by-push BEFORE any driver, gated on this charter's review.

**Sector header (mandatory).** MODE: global bookkeeping **ODE ledger, NOT a field solve** — no `a(t)` evolver exists in the engine and `solve_backreaction` is static-elliptic (`manuscript/ave-kb/common/engine-capability-map.md:155`); Vol-3 cosmology carries only a **LOCAL first-law with no global state vector / conservation law** (`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:130`), and `ΔE_cryst` from `{ℓ_node,α,G}` is **OPEN** (`:122`). REGIME **(★QUARANTINE — Grant-walked input, §1.4)**: the top-stage cascade port (Machian-horizon termination), at/near the cosmic operating point. PHASE-STATE: a held static store (ρ_latent) draining one-way into the T2 bath across the off-line↔on-line boundary. SECTOR **(★QUARANTINE — Grant-walked input, §1.4)**: this is the **A-class (continuous drainage)** behavior of the **local top port** — a static-sector store transferring into a thermal reservoir; it is **NOT** the A1 dilatation-mass sector and **NOT** a Cosserat-winding claim.

**Register:** AVE substrate + EE (two-reservoir exchange, entropic sink, matched-termination absorption, Ax3-lossless interior). **Not** ΛCDM DE-as-fundamental-Λ, **not** QED zero-point energy, **not** a friction/dissipation loss.

> **★CORRECTION NOTE (2026-07-13 — post-driver; body NOT rewritten, KEEP-BOTH).** The tier-1 driver
> executed (PR #674, `research/2026-07-13_f6-tier1-ledger-driver_result.md`) and **falsified this
> charter's a-priori expectation.** Two things are now on record:
>
> - **The §4.3/§4.7 "bin (iii) FORM-DEGENERATE expected on physical histories" posture was
>   internally inconsistent with this charter's own §1.6/§4.7 form table** (confirmed by the #674
>   review + driver). The signature table (§4.7) already had ON `∝ a⁻³`-shutoff-plateau (Λ-like)
>   vs FRONTIER `∝ a⁻³` (matter-tracking) as **different powers of $a$** — on the FRW lock
>   `n_matter ∝ a⁻³` and `H ∝ a^(−3/2)`, so **no constant $\kappa$** collapses ON onto FRONTIER,
>   and the physical run is therefore **not degenerate**. The bin-(iii)-expected posture
>   contradicted the very table it was written beside.
> - **The a-priori was FALSIFIED by the driver.** Superseded expectation, quoted verbatim from
>   §4.7: *"on **physical** input histories, **bin (iii) FORM-DEGENERATE is the EXPECTED tier-1
>   outcome**"* and *"**Bin (i) can fire ONLY through the DECORRELATED-history arm**"*. Empirically
>   the chord was **separable on PHYSICAL too** (`min_κ D[ON,FRONTIER] = 0.088 ≫ tol_form = 0.01`;
>   decorrelation did not cross a threshold) → **bin (i) LEDGER-CONSISTENT** by the frozen §4.5 bins.
>
> **§5.4 adjudicated BOTH by Grant (2026-07-13, in-chat):** (i) **FORM-EXISTENCE BANKED** — the
> occupancy-slaved chord is a real, distinct dynamical form (`D[ON,Λ] ≈ 0.895` at frontier-best-mimic;
> CONSISTENCY-class, κ free ⇒ no emergence); AND (ii) **WRONG-INSTRUMENT CLOSURE BANKED** — the
> chord is homogeneously invisible at late epochs (converges onto Λ past window-start τ₀≈300), so
> its discriminating home is the **spatial** cross-correlation channel, not this homogeneous ledger.
> The frozen bins were **not** dropped or retuned (Rule 11); the a-priori falsification was surfaced
> with verbatim charter content, not debugged away (flag-don't-fix). This note corrects the posture;
> the charter body below is preserved byte-unchanged.

---

## 0 · One-paragraph charter

F6 is the **irreversible ε→T2 depletion** primitive — the **DE-tracks-matter chord**, the one ΛCDM-distinct thing AVE could carry and the make-or-break the corpus has never built (`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:139,144,146`: F6 = the one ΛCDM-distinct chord, UNBUILT; the `reading-i dQ/dt∝n_matter` chord is ABSENT-INVENTED at `:128`; the one attempt `photon_deplete=True` detonates). **Tier 1 is a GLOBAL TWO-RESERVOIR ODE LEDGER** (ρ_latent ↔ T2 bath): does a one-way, Ax3-legal, conservation-respecting transfer whose rate is **slaved to lower-stage occupancy** produce a DE component that **tracks matter in FORM** — and is that form distinguishable from a bare cosmological constant in the ledger's own observable? **No `a(t)` field solve** — tier 1 books reservoir exchange, nothing more. The scope is **existence + FORM only** (no magnitude matching; the naive ρ_latent value is ~120 OOM over ρ_Λ and that path is rejected canon). **TIER-2** (one X40-class discrete-click demo) is a **separate follow-on gated on this charter's review.**

---

## 1 · Physical picture (substrate)

### 1.1 What the medium is doing — the two reservoirs

The vacuum is a saturable Cosserat–LC lattice that is **continuously crystallizing** at the cosmic frontier. Crystallization has a **latent heat**: finishing a region of substrate into ordered matter releases a held store, ρ_latent — the static sector's fuel (`dark-energy-latent-heat-definition.md:64`: "DE free-store / latent heat | ε | the 'fuel'; consumed at the frontier"). Two reservoirs bracket the process:

- **ρ_latent** — the **source**: the static sector's held store (the latent heat of ongoing crystallization). Numerically SYMBOLIC-ONLY / ABSENT in the corpus; enters here as a Grant-GO'd **input parameter** at `clm-s4n33u` solidity 0.45, build_status "input-only, don't build deeper" (`dark-energy-latent-heat-definition.md:122,136`).
- **the T2 bath** — the **destination**: the huge thermal reservoir (the CMB photon gas is its entropic sink, `dark-energy-latent-heat-definition.md:67`). **Irreversibility comes from its mode-count, not from a nonlinearity** — the reconvergence probability into the source is effectively zero, so an energy-conserving transfer INTO T2 has `dS>0` and is Ax3-COMPLIANT (`dark-energy-latent-heat-definition.md:84-86`, verbatim: "an **energy-conserving one-way TRANSFER** into the huge T2 reservoir ($dS>0$), NOT a friction loss, so it is Ax3-COMPLIANT").

Tier-1 books **exactly this exchange and nothing else**. There is no `a(t)`, no field, no spatial solve: two scalars ρ_latent(t) and E_T2(t), a transfer rate Γ, and a conservation ledger `ρ_latent + E_T2 = const`.

### 1.2 What "DE-tracks-matter" means here

ΛCDM's Λ is a constant: the dark-energy density does not know how much matter exists. **AVE's F6 chord is that the drainage rate is slaved to how much matter has clicked in** — `reading-i`, `dQ/dt ∝ n_matter`, which the corpus tags **ABSENT-INVENTED** (`dark-energy-latent-heat-definition.md:128`). The *frontier* form (`reading-ii`, `Γ = 3H·ρ_latent`) is the corpus default and is FORCED-in-form / ASSERTED-in-rate (`:121,142`); it is **not** the chord. The chord is specifically the **inter-stage slaving**: lower-stage matter occupancy setting the top-port drainage rate, a coupling **no canon site derives** (the Machian integral is spatial, produces G, and moves no energy).

Tier-1's question is deliberately narrow: **does a matter-slaved, Ax3-legal, conservation-respecting drainage produce a DE component whose FORM tracks matter, and is that form distinguishable from a constant in the ledger's own observable?** Nothing about magnitude.

### 1.3 The walked architecture (ruling-grade inputs — Grant-walked 2026-07-13)

These four elements are recorded as **ruling-grade inputs** (the walked map), not canon derivations:

| Element | Identity |
|---|---|
| **Source** | **ρ_latent** — the static sector's held store (latent heat of ongoing crystallization). |
| **Destination** | **the T2 bath** — the huge thermal reservoir; irreversibility from its mode-count, not a nonlinearity. |
| **Transducer / locus** | **the mass envelope** — where the transfer is physically effected. |
| **Door** | **the off-line ↔ on-line boundary** — the gate the transfer passes through. |

### 1.4 Cascade address ★QUARANTINE — Grant-walked RULING-GRADE INPUT, not canon

> **★QUARANTINE TAG.** The following cascade address is a **Grant-walked ruling-grade INPUT (2026-07-13)**, NOT a canon-derived result. It is the physical picture the tier-1 ledger is built to test; it must not be cited elsewhere as established corpus physics. Treat every clause below as premise-under-test.

**F6 = the A-class (continuous drainage) behavior of the LOCAL top port** — the Machian-horizon termination. Canon already prices that port as a **distributed transmission-line input impedance at the Hubble-horizon termination** (`manuscript/ave-kb/common/translation-tables/translation-circuit.md:126`, Machian-G ↔ TL-input-impedance row; re-confirmed at `:335,:410`). **F6 is the claim that the Re(Z) at that termination is nonzero and one-way** — the port has a real, irreversible drainage channel, not a purely reactive/lossless one.

- **The FRW `3H·ρ_latent` rate reads as the matched termination's absorption rate** — the top-stage loaded Q ~ O(1) (matched), which is exactly where the cascade's far end already sits.
- **DE-TRACKS-MATTER = the top port's A-rate slaved to the lower stages' B-occupancy** — how much clicked-in matter loads the envelope sets the top port's drainage rate. **That inter-stage slaving IS the chord**, and it is **precisely what no canon site derives** (the Machian integral is spatial, produces G, and moves no energy; no inter-stage energy coupling exists in canon).

### 1.5 Channel tag (do not conflate)

| Channel | Role |
|---|---|
| Static-sector store ρ_latent → T2 (A-class drainage, LOCAL top port) | **THIS ledger's transfer axis** |
| A1 dilatation-mass tank | Owns rest-mass; **NOT** the F6 drainage source (SECTOR⊥). A finished electron is a LOSSLESS tank, paid latent heat ONCE (`dark-energy-latent-heat-definition.md:65`) — it must not appear as a drain in the ledger (see `electron-no-drain` detector, §4.2). |
| Cosserat-winding (2,3) charge | Owns charge/spin; **NOT** an energy source for the top port. |

This discriminator is **static-sector / top-port** tagged. The A1 and Cosserat sectors appear only as **constraints** (the three hard detectors, §4.2, DEFERRED to tier-2 — see §4.2), never as the transfer source.

### 1.6 Tier-1 ledger specification (state · transfer laws · ablation arms · observable · inputs)

*This section pins the actuator, the observable, and the imported inputs so the driver has **no post-charter freedom** (repairs the primary-discriminator gaps: the OFF-state was defined three inconsistent ways and the comparison observable had no formula). The Ax3 mechanism-class the transfer carries is addressed in the Ax3 carve §(iii)/(vii); the a-priori expectation and the **form-inversion** the signatures below imply are owned in §4.7.*

**State (two scalars).** `ρ_latent(t)` (source store) and `E_T2(t)` (bath). Nothing else — no `a(t)`, no field, and no A1 / muon / bias state (those are DEFERRED to tier-2, §4.2).

**Conservation + transfer.** One-way exchange:
\[
\frac{d\rho_{\text{latent}}}{dt} = -\Gamma(t), \qquad \frac{dE_{T2}}{dt} = +\Gamma(t), \qquad \Gamma(t)\ge 0,
\]
so `ρ_latent(t) + E_T2(t) = const` (the `tol_cons` ledger). The transfer rate `Γ` is the entire physics content.

**Imported input histories (provenance is first-class).** A no-`a(t)` ledger cannot solve for the cosmic drivers, so it **imports** two time series, and their provenance is part of the battery:
- `H(t)` — the Hubble rate (canonical `H_∞` scale imported from `src/ave/core/constants.py` semantics; profile declared in the FROZEN prereg).
- `n_matter(t) ∝ n_B(t)` — the lower-stage B-occupancy (clicked-in matter; engineering-choice profile declared in the FROZEN prereg).
- **PHYSICAL (correlated) run** — `H(t)` and `n_matter(t)` obey the standard FRW lock (both functions of one scale-factor parameter `a`; matter era `H = 2/3t`, `n_matter ∝ a⁻³`). **The degeneracy lives here.**
- **DECORRELATED run** — `H(t)` and `n_matter(t)` supplied as INDEPENDENT series that break the `a(t)` lock. **This is the ONLY degeneracy-breaker available at tier-1** — it isolates whether `Γ` responds to `n_matter` (chord) or to expansion (frontier). It is a mandatory arm of the battery, not optional.

**DE-form observable (the formula `tol_form` applies to).** The un-expelled store IS the dark-energy density: `ρ_DE(t) ≡ ρ_latent(t)` (de Sitter asymptote `ρ_latent → ρ_Λ`, `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:66`). Scope is FORM not magnitude (§4.4), so work with the **normalized shape** over a fixed window `[t₀, t₁]`:
\[
\hat\rho_{\text{DE}}(t) = \rho_{\text{DE}}(t)\,/\,\rho_{\text{DE}}(t_0).
\]
The **form-separation residual** between two arms `A`, `B`:
\[
D[A,B] = \big\lVert\, \hat\rho_{\text{DE}}^{A}(t) - \hat\rho_{\text{DE}}^{B}(t) \,\big\rVert_{L^2([t_0,t_1])}\; /\; \sqrt{t_1 - t_0}
\]
— a dimensionless RMS shape difference over the window; **`tol_form` is the threshold on `D`.** This single quantity is what every FORM verdict reads; it did not exist in the pre-repair charter.

**Three transfer laws (the actuator).**

| Law | Formula | Reading | `ρ_DE` signature (physical, matter era) |
|---|---|---|---|
| **ON (chord)** | `Γ_ON(t) = k · n_B(t) · ρ_latent(t)`, `n_B ∝ n_matter` | reading-i (`dQ/dt ∝ n_matter`) | as `n_B ∝ a⁻³ → 0`, drain shuts off ⇒ `ρ_DE` relaxes to a **residual constant → Λ-like** at late `t` |
| **ARM-FRONTIER (OFF)** | `Γ_FRONTIER(t) = 3H(t) · ρ_latent(t)` | reading-ii (frontier default) | `dρ/dt = −3Hρ ⇒ ρ_DE ∝ a⁻³` — **tracks matter in exact continuity form** |
| **ARM-Λ (OFF)** | `Γ_Λ(t) = 0` | bare cosmological constant | `ρ_DE = const` — **Λ** |

**Two named ablation arms — different experiments (do not conflate).**
- **ARM-Λ** — OFF-state `Γ_Λ = 0`. Observable: `D[ON, Λ]`. Tests **chord-vs-Λ** (is the chord's DE-form distinguishable from a bare cosmological constant?).
- **ARM-FRONTIER** — OFF-state `Γ_FRONTIER = 3H·ρ_latent` (B-coupling removed, frontier rate retained). Observable: `D[ON, FRONTIER]`. Tests **chord-vs-frontier** (reading-i vs reading-ii).

These are **not** the same ablation: `D[ON, Λ]` and `D[ON, FRONTIER]` can give opposite verdicts (the pre-repair charter conflated them, so a driver could pass one criterion while failing the other).

**★Correction (KEEP-BOTH, Rule-12).** The pre-repair charter defined the OFF-state as *"the drainage rate goes constant ⇒ the DE form must collapse to a constant ⇒ indistinguishable from Λ"* (superseded wording — §2.1 beats 4–5, the §2.2 mermaid, and the §4.1 ablation row). That is mathematically wrong: a constant nonzero rate `Γ₀` gives `dρ/dt = −Γ₀ ⇒ ρ_DE(t) = ρ_DE(t₀) − Γ₀t` — a **LINEAR decay**, which is neither constant nor Λ (a bare Λ drains nothing). The bare-Λ reference is **`Γ_Λ = 0`**, not a constant rate. The superseded wording is preserved in git and quoted here.

---

## Ax3 reconciliation (mandatory carve)

*(This carve governs the whole discriminator. The transfer must be **entropic / event-gated, NEVER dissipative**. All cites below re-verified at this PR's base d0037d8f with LaTeX-aware greps.)*

### (i) The Ax3 constraint + the licensed class

Sub-yield, the substrate is **lossless / reactive** (Axiom 3). A legitimate F6 transfer is therefore **not free to be a friction loss**. It must be **either**:

- **(a) an entropic one-way transfer** made irreversible by the T2 reservoir's mode-count — energy conserved, `dS>0`, NOT a friction loss (`dark-energy-latent-heat-definition.md:84-86`, verbatim above). Irreversibility from **reservoir mode-count, not nonlinearity**; **OR**
- **(b) an event-gated discrete minting** — one-way at a click, energy-conserving, X40-class (`research/2026-07-10_x40-ring-closure-transient_result.md:18-20,161`: `f_E=1/10` trapped, flux linkage Λ banks WHOLE, drift `2.2e-16`, minted only at the discrete ring-completion event).

Both are Ax3-COMPLIANT **precisely because neither imports sub-yield dissipation.** The tier-1 ledger's transfer term Γ must be one of these two; any continuous sub-yield loss term is the retired Ax3 leak (§(ii)–(iii)).

### (ii) The amorphous-retirement precedent (address it explicitly)

The **plastic / STZ sub-yield dissipation route FAILED Ax3 and stays RETIRED.** Verbatim, `manuscript/ave-kb/common/substrate-native-terminology.md:62`:

> "✗ 'thixotropic STZ / liquefies / plastic' *as the load-bearing mechanism* — in the lossless sub-yield regime that imports dissipation, which would radiate, contradicting the result."

F6's drainage must **not reconstruct that retired leak under a cosmological name.** Any tier-1 ledger term that is a **continuous sub-yield loss** is the retired Ax3 leak re-imported — regardless of the label "dark energy" pasted on it. (The corpus's own loop taxonomy is the reason: the enclosed hysteresis loop `∮S dr` is **dissipated energy per cycle** and lives at/above yield as a Level-2 memristive channel, `manuscript/ave-kb/common/substrate-hysteresis-index.md:24-25`; sub-yield it must be lossless.)

### (iii) ★NEW FOOL-MODE — the re-imported Ax3 leak

A **LEDGER-CONSISTENT PASS achieved via a continuous sub-yield dissipative transfer** = the retired leak re-imported. It must be classed **IMPOSED-LEAK, not F6-CANDIDATE.**

**Detector — conservation / destination audit (NOT an entropic-legality certifier).** The audit checks one thing: the destination reservoir's energy rises by exactly what the source loses, to `tol_cons` (`ρ_latent` loss = `E_T2` gain). It catches only a transfer that makes energy **vanish** (a non-conserving, energy-destroying term). Verdict for a non-conserving term: **bin IMPOSED-LEAK / bin (ii).**

**★The Ax3 knife the audit does NOT resolve (finding-corrected).** Conservation does **not** establish entropic-ness. An honestly-booked friction/damping term
\[
\frac{d\rho_{\text{latent}}}{dt} = -\gamma\,\rho_{\text{latent}}, \qquad \frac{dE_{T2}}{dt} = +\gamma\,\rho_{\text{latent}}
\]
**conserves exactly** (`d(ρ_latent+E_T2)/dt = 0`), **passes the `tol_cons` audit**, and with `γ = 3H` is functionally identical to the corpus default `Γ = 3H·ρ_latent` (§1.2). It is the retired STZ-class dissipative leak (§(ii)) wearing a conserving ledger. So the earlier "friction ⇒ non-conserving" equation was **false**: a booked friction deposits its heat into the bath and conserves. The licensed entropic-vs-dissipative distinction — §(i) "irreversibility from **mode-count**, not nonlinearity" — **requires modes**, and the tier-1 state is **two scalars** (`ρ_latent`, `E_T2`, §1.6): there are no modes in the state space, so **entropic-vs-dissipative is not an operational property of any tier-1 observable.**

**Consequence — the transfer's Ax3 class is a CITED PREMISE at tier-1, not a ledger verdict.** At tier-1 the transfer's entropic-not-friction character is **inherited from the home-leaf premise** (`dark-energy-latent-heat-definition.md:84-86`, which establishes it by a *physical* argument about the T2 destination reservoir's mode-count, "reconvergence probability effectively zero" — not by any ledger computation) and is discharged, if ever, only at a **mode-carrying tier-2 / engine-level test.** Therefore a **bin (i) PASS certifies CONSERVATION + FORM only; it does NOT certify Ax3-entropic-legality** (see the bin (i) definition, §4.5, which is worded to prevent that over-read). The conservation/destination audit still composes with the FORM tests as a first gate (a non-conserving term is caught before any FORM verdict is read), but it must not be advertised as proving the transfer entropic.

### (iv) The DIODE / RECTIFIER class is DEAD — four deaths (do not resurrect a valve)

A one-way *valve* (ideal diode / rectifier / ratchet) is the intuitive way to get irreversibility. It is **dead four ways** in the corpus. The tier-1 ledger must get its arrow from **where the energy goes** (reservoir mode-count) or **a click** (X40), **never** from a valve:

1. **The Ax4 kernel is even-in-A and cannot rectify.** `S(A)=√(1−A²)` is instantaneous, even, memoryless — identical 2nd-order momentum for symmetric and asymmetric drive (`research/2026-06-08_rrad-l-rectification_result.md:67-73`). **⚠ HONESTY SCOPE:** the *direct RUN* null there is **regime-scoped** by the doc's own Rule-12 header (sub-yield-linear shear = a regime where the effect cannot exist, a wrong-regime artifact, `:14,:18`); the mechanism finding (even-in-A ⇒ no rectification) stands as a fact about the kernel, and the **regime-independent** bulk-channel closure ("no `sign(dρ̄/dt)` memory ⇒ cannot rectify a symmetric cyclic drive") is **dead-by-derivation on UNMERGED branch `5969bda1`** (cited by branch+commit, not a HEAD path). Carry both: the kernel cannot rectify, and the load-bearing bulk closure is off-main.

2. **Any true rectifying loop is Level-2 memristive = dissipative.** `manuscript/ave-kb/common/substrate-hysteresis-index.md:96`: "**any** rectification / latching / path-memory requires the **Level-2 (memristive)** dynamics, which the smooth √(1−A²) kernel does not implement on its own"; the enclosed loop `∮S dr` is dissipated energy per cycle (`:24-25`). So "lossless + rectifier" is a **contradiction in the corpus's own loop taxonomy** — a rectifier is exactly the retired Ax3 leak of §(ii).

3. **The diode threshold V_f is FREE, not forced.** `research/2026-07-08_p4-forward-voltage-threshold_RESULT.md:19,26,52-56`: "V_f is FREE — no canonical scale forces a forward-voltage dead zone"; the Ax4 kernel is analytic at the origin and loads `∝½A²` continuously (`:26`), the lattice dispersion is gapless (`:30-33`), and **no candidate row satisfies the FORCED bin** (`:52-56`). A diode's defining feature — a forward-voltage dead zone — has no substrate scale.

4. **Chirality-ratchet-as-arrow is REFUTED — do not reopen.** `dark-energy-latent-heat-definition.md:89-90,99-100`, verbatim: "Chirality is a PARITY selector, not the arrow — and 'chirality-ratchet as arrow' is REFUTED"; "**No future reader should re-introduce the chirality-ratchet as the cosmological arrow.**" An ideal-diode / directed-ratchet framing of the drainage risks re-opening this retracted slot.

### (v) The v4 detonation (do not repeat it)

Any **continuous trilinear-potential transfer is the v4 detonation.** `src/ave/core/crystal_graft_v4.py:159-167` (verbatim comment; **⚠ line-drift flag:** the brief cited `:160-166`, the verbatim block spans **:159-167** at this HEAD): the full trilinear `H=κ̃∫gV[w·∇×ω]` is "an **INDEFINITE Hamiltonian** (linear in each field, unbounded below) so the discrete dynamics **PUMP / DETONATE**." The **v5 spec** is the antidote: **bounded, norm-preserving, source-depletion-not-reaction** (`research/2026-06-10_bemf-feedback-smoke_result.md`, §8 `:94`, verbatim: "a **norm-preserving (bounded) photon→ω helicity-transfer** coupling — an orthogonal field-space rotation … rather than a trilinear potential" and "**The missing primitive is depletion, not reaction.**"; the all-caps "SOURCE DEPLETION, NOT REACTION" phrasing is the doc's Rule-12 header at `:10,:12`, cited separately — not part of the §8 body). **Tier-1's ledger must not smuggle a trilinear pump back in through the ODE** — the transfer term must be a bounded reservoir-exchange rate, never a product of three growing amplitudes.

### (vi) Licensed mechanisms only (use ONE of these three)

1. **Entropic mode-count transfer** (arrow-of-time class) — energy-conserving one-way transfer into T2, `dS>0`, Ax3-compliant (`dark-energy-latent-heat-definition.md:84-86`). Irreversibility from reservoir mode-count.
2. **X40-class discrete topological minting** — one-way at the click, energy-conserving, consistency-class (`research/2026-07-10_x40-ring-closure-transient_result.md:18-20,161`; Λ banked whole, drift `2.2e-16`).
3. **The skew-Hermitian circulator** — orthogonal field-space rotation, conserves + transfers, but **magnitude imposed** (`src/ave/core/cross_sector_coupling.py:137-141`: "one-way circulation needs the 3-port loop, magnitude imposed"; PR #321). *Use only with the imposed-magnitude caveat explicit — an imposed magnitude is an echo, not a chord.*

---

## 2 · Circuit picture (EE mapping)

### 2.1 Five-beat intuition summary

1. **Substrate:** The crystallization frontier releases latent heat ρ_latent. It must go somewhere; the only Ax3-legal destination is an **entropic transfer into T2's modes** (`dS>0`, conserved, not friction). The interior stays lossless; the arrow lives at the reservoir.

2. **EE mapping (★QUARANTINE — cascade address is a Grant-walked ruling-grade input, §1.4):** A charged **DC store** (ρ_latent) feeds a **lossless transmission line** (the interior, at `Z_0`) that is **terminated at the Hubble horizon**. Canon prices that termination as the **Machian-G input impedance** (`translation-circuit.md:126`); **that Re(Z)≠0, one-way reading — and the matter-occupancy gating below — are the walked premise-under-test, not established canon.** **F6 = the claim that `Re(Z)` at that termination is nonzero and one-way** — a *matched termination into a huge cold bath*, not a lossy element in the pipe. The drainage rate is a **controlled source gated by lower-stage matter occupancy** — the slaving is the chord.

3. **Prediction & why the form:** The observable is the **form-separation residual** `D[A,B]` (§1.6) between the chord arm (reading-i, `dQ/dt∝n_matter`, ABSENT-INVENTED `dark-energy-latent-heat-definition.md:128`) and each OFF arm. The discriminator is **form-SEPARATION between arms, not tracks-matter-vs-constant** — because the frontier default (reading-ii, `Γ=3H·ρ_latent`) already drives `ρ_DE ∝ a⁻³`, i.e. it **tracks matter for free with zero inter-stage coupling** (§1.6 signature table; owned in §4.7). **No magnitude** — the naive ρ_latent value is ~120 OOM over ρ_Λ and that path is rejected canon (`cosmological-constant-closure.md:8,58-62`: naive mode-count "still gives a too-large naive answer"; DE reframed as latent heat, not zero-point energy).

4. **Discriminator:**
   - *form-shared?* Two OFF arms, two different experiments (§1.6): **ARM-Λ** (`Γ_Λ=0`, `D[ON,Λ]`, chord-vs-Λ) and **ARM-FRONTIER** (`Γ_FRONTIER=3H·ρ_latent`, `D[ON,FRONTIER]`, chord-vs-frontier). The chord fires only if `D[ON,FRONTIER] > tol_form` on the **DECORRELATED** input-history run (the frontier default already matter-tracks on the physical run, so the physical run is expected degenerate — §4.7). If `D` stays below `tol_form` even under decorrelation, that is bin (iii) FORM-DEGENERATE.
   - *already constrained?* The corpus already tags `reading-i` **ABSENT-INVENTED** — this is a **forward existence-of-FORM test**, not a new realized-result claim.
   - *injected?* ρ_latent is **input-only** (`clm-s4n33u`, solidity 0.45); it must **not** be tuned to hit ρ_Λ. The verdict path reads FORM, never magnitude.

5. **Intuition hook:** **It's a matched termination into a huge cold bath, not a resistor burning power in the pipe.** A dump resistor inside the line would be the retired STZ leak (IMPOSED-LEAK); a matched termination transfers the power *out* into the reservoir's mode-count, and the pipe stays lossless (Ax3). And the drainage isn't a **diode** (dead four ways) — it's a **controlled source keyed on how much matter has clicked in**. Take that control away and you get one of two *different* references (§1.6): a frozen store (`Γ_Λ=0`, bare Λ) or the frontier drain (`3H·ρ_latent`, which itself dilutes as `a⁻³`) — **not** "a constant matched rate," which would drain the store linearly to zero (the finding-corrected point).

### 2.2 Circuit schematic (plumber)

```mermaid
flowchart LR
  subgraph source ["Static-sector store"]
    RHO["rho_latent charged DC store<br/>(clm-s4n33u, INPUT-ONLY)"]
  end

  subgraph line ["Interior — LOSSLESS (Ax3)"]
    TL["Transmission line at Z_0<br/>reactive, no interior loss"]
    RHO --> TL
  end

  subgraph term ["Hubble-horizon termination"]
    ZT["Machian-G input impedance<br/>F6: Re(Z) nonzero + ONE-WAY"]
    TL --> ZT
  end

  subgraph bath ["T2 bath — entropic sink"]
    T2["huge mode-count reservoir<br/>dS>0, energy CONSERVED into it"]
    ZT -->|matched absorption 3H.rho_latent| T2
  end

  subgraph slave ["THE CHORD — inter-stage slaving"]
    BOCC["lower-stage B-occupancy<br/>(clicked-in matter)"]
    BOCC -.->|gates the A-rate| ZT
  end

  subgraph ablate ["Ablation arms (§1.6) + fool-detectors"]
    ARMF["ARM-FRONTIER: Gamma=3H.rho (rho_DE ~ a^-3, tracks matter)"]
    ARML["ARM-Lambda: Gamma=0 (rho_DE=const, bare Lambda)"]
    LEAK["interior dump-R => IMPOSED-LEAK"]
    ARMF -.->|D[ON,FRONTIER]| ZT
    ARML -.->|D[ON,Lambda]| ZT
    LEAK -.->|non-conserving transfer = retired Ax3 leak| TL
  end
```

### 2.3 What the circuit is *not*

- **Not a lossy interior resistor.** A dump-R inside the line is the retired STZ/plastic sub-yield leak (`substrate-native-terminology.md:62`) → bin IMPOSED-LEAK.
- **Not a diode / rectifier valve.** Dead four ways (§(iv)); the arrow comes from mode-count or a click, never a valve.
- **Not a trilinear pump.** `H=κ̃∫gV[w·∇×ω]` detonates (`crystal_graft_v4.py:159-167`); the transfer term is a bounded reservoir-exchange rate, not a product of three growing amplitudes.
- **Not an `a(t)` Friedmann field solve.** No field, no scale factor — two scalars and a conservation ledger (`engine-capability-map.md:155`: `solve_backreaction` static-elliptic, no `a(t)`).
- **Not a magnitude match to ρ_Λ.** The 10^122 path is rejected canon (`cosmological-constant-closure.md:8,58-62`).

---

## 3 · Map (where this sits in the program)

```mermaid
flowchart TB
  subgraph landed ["LANDED (reversible sibling)"]
    BR["#86 two-way back-reaction<br/>solve_backreaction, static-elliptic<br/>REVERSIBLE self-gravitation"]
  end

  subgraph proofs ["Existence proofs the ledger reuses"]
    X40["X40 ring-closure<br/>one-way at click + Lambda conserved (2.2e-16)"]
    ARROW["arrow-of-time T2 sink<br/>entropic one-way transfer dS>0"]
  end

  subgraph graves ["Closed / dead (do not resurrect)"]
    V4["v4 trilinear = DETONATION"]
    DIODE["diode/rectifier class<br/>dead 4 ways"]
    STZ["plastic/STZ sub-yield loss<br/>RETIRED (fails Ax3)"]
    RATCHET["chirality-ratchet arrow<br/>REFUTED, do-not-reopen"]
  end

  subgraph this ["THIS CHARTER — F6 tier-1"]
    T1["two-reservoir ODE ledger<br/>rho_latent <-> T2, slaved rate<br/>EXISTENCE + FORM only"]
  end

  subgraph next ["Gated follow-ons"]
    PREREG["FROZEN prereg (bins+tol)<br/>freeze-by-push before driver"]
    DRIVER["tier-1 driver (ODE ledger)"]
    T2DEMO["TIER-2: one X40-class<br/>discrete-click demo"]
  end

  BR -->|F6 = the IRREVERSIBLE sibling| T1
  X40 -->|licensed mechanism (b)| T1
  ARROW -->|licensed mechanism (a)| T1
  V4 -.->|must not smuggle in| T1
  DIODE -.->|must not resurrect| T1
  STZ -.->|IMPOSED-LEAK fool-mode| T1
  RATCHET -.->|risks reopening| T1
  T1 --> PREREG --> DRIVER --> T2DEMO
```

| Neighbor | Relation |
|---|---|
| **#86 two-way back-reaction** (LANDED 2026-06-29) | The **reversible** self-gravitation loop; F6 is its **irreversible** sibling — the DE-tracks-matter chord (`engine-capability-map.md:152,155`). |
| **X40 ring-closure minting** | Existence proof that one-way-at-an-event coexists with exact conservation (Λ drift `2.2e-16`) — licensed mechanism (b); the tier-2 demo carrier. |
| **arrow-of-time T2 sink** | The entropic one-way transfer (`dS>0`) — licensed mechanism (a); the tier-1 default. |
| **DE lifecycle leaf** (`dark-energy-latent-heat-definition.md`) | Home leaf: `reading-i` (chord, ABSENT-INVENTED) vs `reading-ii` (frontier, default). This charter does **not** edit it (KB-leaf edits gated). |
| **v4/v5 graft** | Detonation vs bounded spec — the fork the ledger's transfer term must land on the v5 side of. |
| **TIER-2 (X40 demo)** | Separate follow-on, gated on this charter's review — not in scope here. |

---

## 4 · Analysis (what would discriminate; what would fake)

### 4.1 Fireable content vs entailed content

| Content | Class |
|---|---|
| Reservoir conservation (`ρ_latent + E_T2` invariant to machine precision) | Partly **ENTAILED** (ledger construction) — **do not bank as the chord** |
| The top-port A-rate **slaved to lower-stage B-occupancy** (`Γ_ON = k·n_B·ρ_latent`, §1.6) | **FIREABLE** — *this is the chord* |
| DE-form separation `D[ON, FRONTIER]` on the **decorrelated** input-history run (§1.6) | **FIREABLE** — the only tier-1 chord-carrier (§4.7) |
| ARM-Λ (`Γ_Λ=0`): `D[ON, Λ]`, chord-vs-bare-constant | **FIREABLE ablation** (distinct experiment from ARM-FRONTIER — §1.6) |
| ARM-FRONTIER (`Γ_FRONTIER=3H·ρ_latent`): `D[ON, FRONTIER]`, chord-vs-frontier | **FIREABLE ablation** — degenerate on physical inputs, informative only decorrelated (§4.7) |
| ρ_latent magnitude vs ρ_Λ | **OUT OF SCOPE** — not measured, not fit (§4.4) |

### 4.2 Hard constraints — three named detectors, all ★DEFERRED to tier-2

> **★DEFERRED-to-tier-2 (finding-corrected).** All three hard-constraint detectors below consume state the **two-scalar tier-1 ledger does not carry**: `bias_invariance` needs an R-A operating-point bias parameter, `electron_store_conservation` needs an A1-tank energy `E_A1(t)`, `muon_channel_separability` needs a muon decay-rate channel — **none exists in the `{ρ_latent, E_T2}` state (§1.6).** They are therefore **DEFERRED to the tier-2 (mode/sector-carrying) gate set** and are **struck from bin (i)'s firing condition** (§4.5). We do **NOT** invent tier-1 proxies: a hand-wired flat `E_A1` with no coupling written to it would be flat by construction, making the gate consume its own construction (it could never fire) — that is a fake gate, not a constraint. The definitions below stand as the **tier-2 specification**, recorded now so tier-2 inherits them verbatim.

**The tier-1 fireable set (say it plainly).** With the three hard detectors deferred, tier-1 fires on exactly: **(1) the conservation / destination equality audit** (`tol_cons`, §(iii)); **(2) the two ablation arms** ARM-Λ and ARM-FRONTIER with the form-separation observable `D[·,·]` run on PHYSICAL **and** DECORRELATED histories (`tol_form`, §1.6/§4.7); **(3) the input-provenance audit** (ρ_latent byte-identical to the frozen input, no magnitude tune). The structural transfer-law checks (TRILINEAR-PUMP bounded-norm, DIODE-RESURRECTION mechanism-class, §4.3) also run at tier-1. Everything else — Ax3-entropic certification (§(iii)) and the three sector-ownership guards below — is tier-2.

**Tier-2 detector specification (deferred; each fires on a specific computed quantity when the sector state exists):**

- **`bias_invariance` detector — (bias ≠ release).** The R-A operating-point **bias must be untouched by the release mechanism**; the drainage cannot move the bias point. **Computed quantity:** the operating-point bias parameter recorded with the release channel **ON vs OFF**; `|Δbias|/bias` must be `≤ tol_bias`. A nonzero shift ⇒ the drainage is riding the bias, not a clean top-port A-channel ⇒ **FAIL**.
- **`electron_store_conservation` detector — (electron-no-drain).** The port **must not drain its own transducer** (electron stability). **Computed quantity:** the A1-tank energy time-series `E_A1(t)` while top-port drainage is active — it must be flat (`|dE_A1/dt| ≤ tol_A1`, `Q→∞` preserved). A finished electron paid its latent heat ONCE and is a lossless tank (`dark-energy-latent-heat-definition.md:65`); if `E_A1` decays, the ledger is draining the electron ⇒ **FAIL**.
- **`muon_channel_separability` detector — (muon fence).** The muon **loads T2 but does not decay by that channel**. **Computed quantity:** the muon's booked decay rate with the T2-loading term **ON vs OFF** — it must be invariant (`|Δτ_μ⁻¹| ≤ tol_μ`). If loading the bath changes the muon lifetime in the ledger, the T2-loading channel and the decay channel are cross-wired ⇒ **FAIL**. (T2 loading is separable from the muon's actual decay route.)

### 4.3 Fool-modes — each with a named detector

| Fool-mode | What it fakes | Named detector (computed quantity that fires it) |
|---|---|---|
| **IMPOSED-LEAK** (§iii) | a non-conserving, energy-destroying transfer | **Conservation / destination audit** — `ρ_latent` loss must equal `E_T2` gain to `tol_cons`; a term that makes energy **vanish** fires. **⚠ REACH LIMIT (§iii):** an honestly-booked friction term (`dρ=−γρ`, `dE_T2=+γρ`) conserves and is **NOT** caught here — entropic-vs-dissipative is inexpressible in two scalars and is a cited premise, deferred to tier-2. |
| **TRILINEAR-PUMP** (v4) | transfer via an indefinite-Hamiltonian pump | **Bounded-norm audit** — total ledger energy must not show an unbounded/monotone runaway excursion (the `H_bel`/`H_photon` detonation signature, `crystal_graft_v4.py:159-167`); the transfer term must be a bounded reservoir-exchange rate, never a product of three co-growing amplitudes. |
| **MAGNITUDE-TUNE** (10^122 trap) | a "match" to ρ_Λ | **Input-provenance audit** — the `ρ_latent` value in the run must be **byte-identical** to the frozen input (`clm-s4n33u`); any adjustment toward ρ_Λ in the verdict path fires. The 10^122 path is rejected canon (`cosmological-constant-closure.md:8,58-62`). |
| **SLAVING-DEGENERACY** (→ bin iii) | "tracking" that is carried by the frontier default with zero inter-stage coupling | **ARM-FRONTIER + decorrelated run** (§1.6) — the frontier default `Γ_FRONTIER=3H·ρ_latent` integrates to `ρ_DE ∝ a⁻³`, the **exact matter-continuity form** (not soft co-monotonicity — §4.7), so on the PHYSICAL (`H`↔`n_matter` locked) run `D[ON, FRONTIER] ≤ tol_form` is **expected**. Fire the chord only if the DECORRELATED run lifts `D[ON, FRONTIER] > tol_form`; if it does not, ⇒ **bin FORM-DEGENERATE**. |
| **DIODE-RESURRECTION** | one-way-ness via a valve | **Mechanism-class audit** — the transfer term must be one of the three licensed mechanisms (§vi); any `V_f`-like dead-zone threshold, rectifying nonlinearity, or `sign(rate)`-dependent asymmetry fires (dead four ways, §(iv)). |

### 4.4 Scope lock (CC-honest, binding)

- **Existence + FORM of DE-tracks-matter ONLY.** Tier-1 asks whether a matter-slaved, Ax3-legal, conservation-respecting drainage produces a DE component whose **form** tracks matter — nothing about its **magnitude**.
- **NO magnitude matching.** The naive `ρ_latent` value is ~120 OOM over ρ_Λ; the **10^122 trap is rejected canon** (`cosmological-constant-closure.md:8,58-62`). The charter must **not** attempt to match the ρ_latent magnitude to ρ_Λ.
- **ρ_latent = Grant-GO'd 2026-07-13, INPUT-ONLY.** It enters at `clm-s4n33u`, solidity 0.45, build_status "input-only, don't build deeper" (`dark-energy-latent-heat-definition.md:122,136`). Use it as an input parameter; do **not** deepen the ρ_latent / ΔE_cryst derivation.
- **Consistency-vs-emergence class = CONSISTENCY (ceiling).** Tier-1's DE-tracks-matter FORM, *if it exists*, is at best a **CONSISTENCY / MANIFESTATION**-class demonstration — the ledger is *constructed* to book the transfer, so a form appearing is not EMERGENCE. Per the home leaf's own tag (`dark-energy-latent-heat-definition.md:113`), the AVE-distinct content is the DEFINITION / MECHANISM; the ρ_Λ value is ECHO / CONSISTENCY. The chord only becomes fireable-real if the slaving coupling `k` + response are **derived from `{ℓ_node, α, G}`** (F6 gate 3, `:156`) — which tier-1 does **NOT** do (ρ_latent is input-only). **Refuse any EMERGENCE headline from tier-1.**
- **ave-canonical-source discipline.** Any numerical constant the downstream driver references (`H`, `G`, tolerances) **imports from `src/ave/core/constants.py` semantics** or is declared an engineering-choice in the FROZEN prereg — **no hardcoded value is presented as canonical in this charter.** The only physics numbers named here are cited to their canonical source (`ρ_latent` SYMBOLIC-ONLY input; `Γ=3H·ρ_latent` form; `10^122` framing at `cosmological-constant-closure.md:8`).

### 4.5 Frozen bins (tier-1) — freeze PRE-RUN, by push, before any driver

- **(i) LEDGER-CONSISTENT.** The two-reservoir ledger conserves (`ρ_latent + E_T2` invariant to `tol_cons`); the transfer passes the FORM-level structural gates (TRILINEAR-PUMP bounded-norm audit, DIODE-RESURRECTION mechanism-class audit, §4.3); and the chord's DE-form is separable from the frontier default (`D[ON, FRONTIER] > tol_form` on the DECORRELATED run, §1.6/§4.7) — so **the DE-tracks-matter FORM exists as a tier-1 CONSISTENCY-class demonstration.** **★What bin (i) does NOT certify (finding-corrected):** it certifies **conservation + FORM only.** It does **NOT** certify that the transfer is Ax3-entropic (that class is inexpressible in two scalars and is carried as a cited premise, §(iii), deferred to tier-2); and it does **NOT** discharge the three §4.2 sector-ownership constraints (DEFERRED to tier-2, §4.2). A bin (i) PASS is thus a CONSISTENCY result about FORM, never an Ax3-legality or sector-safety certificate.
- **(ii) LEDGER-VIOLATES-CONSERVATION.** The ledger fails to conserve (`ρ_latent + E_T2` total drifts beyond `tol_cons`) — **FAIL** (bin **IMPOSED-LEAK**, §(iii): the transfer destroys energy). **★Reach caveat (finding-corrected):** an honestly-booked *conserving* dissipative term (`dρ=−γρ`, `dE_T2=+γρ`) is **NOT** caught by this bin — it conserves and passes `tol_cons`. Whether such a conserving transfer is the licensed entropic arrow or the retired friction leak is **not decidable in a two-scalar ledger** (§(iii) Ax3 knife); that discrimination is a cited premise, deferred to a mode-carrying tier-2 test. This bin therefore catches only energy-destroying (non-conserving) transfers, not conserving-but-dissipative ones.
- **(iii) FORM-DEGENERATE.** The ledger runs and conserves, but the chord's DE-form is **not separable from the frontier default** on physical histories and the decorrelated run does not lift it (`D[ON, FRONTIER] ≤ tol_form` — §1.6/§4.7) — the form is degenerate; F6's chord does not resolve at tier-1. **★This is a LEGITIMATE outcome that CLOSES the interior program — a real negative on the FORM question, NOT an instrument gap and NOT a failure to be rescued.** Per Rule 11 honest closure: if the ledger lands here, record the falsification, name the degeneracy mechanism **precisely** — it is **not** soft co-monotonicity but the **exact `3H` continuity-operator identity**: `dρ/dt = −3Hρ ⇒ ρ_DE ∝ a⁻³`, the `w=0` matter-density form itself, so the NON-chord frontier default IS matter-tracking with zero inter-stage coupling (§4.7) — and close the tier-1 interior branch. The chord, if it lives anywhere, then lives only in the tier-2 discrete demo or the forward observable (DESI/Euclid DE-vs-matter *spatial* cross-correlation, `dark-energy-latent-heat-definition.md:159`), not in the homogeneous interior ledger.

### 4.6 Freeze discipline statement

- **Bins frozen PRE-RUN by push** in the downstream FROZEN prereg — before any driver exists.
- **No dropped criteria post-hoc.** The complete **tier-1** adjudication set is the three bins + the tier-1 fireable set (§4.2: conservation/destination audit, the two ablation arms on physical+decorrelated histories, input-provenance audit, and the two structural transfer-law audits). None is dropped to convert a ❌ to a ✅ (Rule 11). The three §4.2 hard detectors are **DEFERRED to tier-2** (not dropped — struck from bin (i) because their state does not exist at tier-1, §4.2).
- **The ARM-FRONTIER + DECORRELATED comparison is the primary discriminator** for the chord vs bin (iii); both ablation arms (ARM-Λ, ARM-FRONTIER) and both history provenances (physical, decorrelated) must run in every battery (§1.6/§4.7).
- **No debug-toward-rescue.** If the ledger lands in bin (ii) or (iii), that is the discipline working at full strength: record the negative, name the mechanism, close the branch. A sudden bin (i) PASS that appears only after the transfer term is re-shaped is a red flag for a smuggled leak or pump — re-run the §4.3 detectors before banking.
- **Substitution-not-retraction (Rule 12).** If a later result falsifies a premise of this charter, the charter body is preserved and a dated 🔴 header is added; the slot is not silently refilled.

### 4.7 A-priori expectation + the form-inversion (posture — banked, not softened)

**The frontier default already tracks matter — exactly, not softly.** With `Γ_FRONTIER = 3H·ρ_latent`, `dρ/dt = −3Hρ` integrates to `ρ_DE ∝ a⁻³` in **any** era — the matter-density continuity law itself (`3H` is the `w=0` continuity operator). So the frontier default (reading-ii, the corpus-realized form, `dark-energy-latent-heat-definition.md:143`) produces DE-tracks-matter **in exact functional form with ZERO inter-stage coupling.** "DE-form tracks matter" is therefore carried by the **non-chord** default; observing it does **not** fire the chord.

**The signatures are INVERTED relative to the naive framing (own it).** Under physical histories (matter era):

| Arm | Transfer | `ρ_DE` form | Naively expected | **Actually** |
|---|---|---|---|---|
| ARM-FRONTIER (reading-ii, NON-chord) | `3H·ρ_latent` | `∝ a⁻³` | "Λ-constant" | **tracks matter** |
| ON (reading-i, the chord) | `k·n_B·ρ_latent`, `n_B ∝ a⁻³` | drain shuts off → residual constant | "tracks matter" | **Λ-like** |

The pre-repair charter had this **backwards** (chord = tracks-matter, OFF = Λ-constant). The truth is the reverse: the chord trends **Λ-like**, the default **tracks matter**. So "tracks-matter-vs-constant" is the **wrong discriminator axis**; the right one is **functional-form separation** between two matter-correlated declines — and on physical histories (`H`↔`n_matter` locked) that separation cannot be attributed to inter-stage slaving, because either driver explains it.

**A-priori expectation (posture change, banked per Rule 11):** on **physical** input histories, **bin (iii) FORM-DEGENERATE is the EXPECTED tier-1 outcome** — the homogeneous global ledger is the wrong instrument for a chord whose real home is the DESI/Euclid **spatial** cross-correlation (`dark-energy-latent-heat-definition.md:159`), which tier-1 (no `a(t)`, no spatial channel) cannot host. **Bin (i) can fire ONLY through the DECORRELATED-history arm** — the single tier-1 lever that breaks the `H`↔`n_matter` lock and isolates whether `Γ` responds to matter or to expansion. The charter does **not** present bin (i) as neutrally reachable; degeneracy (or the form-inversion) is what we expect, and that expectation is banked, not a rescue-to-be-debugged-away.

**★KEEP-BOTH (Rule 12).** The superseded framing — *"the chord tracks matter; slaving OFF ⇒ the DE form collapses to a constant, indistinguishable from Λ"* (pre-repair §2.1 beats 4–5, §4.1 ablation row, bin (iii) "co-monotone" mechanism) — is preserved in git and quoted here. It was inverted (the default tracks matter; the chord is Λ-like) and its degeneracy mechanism was understated (the exact `3H` continuity identity, not soft co-monotonicity).

---

## 5 · Deliverables and sequencing

| Step | Artifact | Status |
|---|---|---|
| 0 | Grant GO (Q4) — ρ_latent parameterization INPUT-ONLY at `clm-s4n33u` (0.45) | 2026-07-13 ✓ |
| 1 | **This CHARTER** (picture · walked architecture · cascade · constraints · licensed mechanisms · Ax3 carve · scope · bins) | This file — reviewed **before** any driver |
| 2 | **FROZEN prereg** — carries, verbatim from §1.6, the **DEFINITIONS** (not only tolerances): the state vector; the three transfer laws `Γ_ON` / `Γ_FRONTIER` / `Γ_Λ`; the two named ablation arms (ARM-Λ, ARM-FRONTIER) and which `D[·,·]` each reads; the DE-form observable `ρ_DE ≡ ρ_latent` + normalized-shape `D[A,B]` formula + window `[t₀,t₁]`; the input-history provenance (PHYSICAL vs mandatory DECORRELATED runs) — **plus** tolerances `tol_cons`, `tol_form` (`tol_bias`, `tol_A1`, `tol_μ` are tier-2, §4.2). | Sibling file — freeze-by-push **BEFORE any driver**; **NOT in this commit** |
| 3 | **Tier-1 driver** (the two-reservoir ODE ledger) | **NOT in this commit** — gated on charter + prereg review |
| 4 | **TIER-2** (one X40-class discrete-click demo) | Separate follow-on — gated on this charter's review |

**Deliverable lock (this PR).** ONE charter doc. **No driver code, no engine edits, no KB-leaf edits.** The frozen prereg (step 2), the tier-1 driver (step 3), and tier-2 (step 4) are all gated on Grant's charter review.

**Rails.**
- **Freeze-by-push** — the FROZEN prereg's bins + tolerances are frozen by push before any driver exists; sabotage plants act on the **evolved tier-1 ledger observables** (the `tol_cons` conservation residual and the `D[·,·]` form-separation observable on both history provenances), not on the input. (The three §4.2 sector-detector time-series are tier-2, not part of the tier-1 sabotage surface.)
- **Adversarial review** via a `scriptPath` wrapper that inlines ARGS and calls `workflow({scriptPath: '.claude/workflows/ave-adversarial-pr-review.js'}, ARGS)` (the named-workflow args path silently drops args).
- **DO-NOT-MERGE** — only Grant merges. This charter is a discriminator draft, not a result.

---

## 6 · References (grep-verified anchors — 2026-07-13, at base d0037d8f)

All file:line anchors below were **re-verified at this PR's base `d0037d8f`** with LaTeX-aware content greps (not carried on trust from the upstream grounding card, which was verified at a different HEAD). Two anchors drifted or need a scope caveat — flagged inline.

**Charter pattern**
- `research/2026-07-12_remanence-r10-fixed-n_CHARTER.md` — the #662 charter pattern this doc is modeled on (charter + frozen bins + fireable-vs-entailed + fool-modes + Ax3 carve).

**Home leaf + scope**
- `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:84-86` (Ax3-legal one-way T2 transfer, `dS>0`, "NOT a friction loss, so it is Ax3-COMPLIANT"); `:89-90,99-100` (chirality-ratchet-as-arrow REFUTED, "No future reader should re-introduce" it); `:122,136` (`clm-s4n33u` ρ_latent solidity 0.45, input-only, "don't build deeper"); `:128` (`reading-i dQ/dt∝n_matter` = ABSENT-INVENTED; `photon_deplete=True` detonates); `:139,144,146` (F6 = the one ΛCDM-distinct chord, UNBUILT); `:153-158` (the five make-or-break gates); `:159` (forward observable = DESI/Euclid DE-vs-matter cross-correlation); `:64,65,67` (reservoir roles: ρ_latent fuel / A1 lossless tank paid once / T2 CMB entropic sink); `:113` (consistency-vs-emergence tag).
- `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:8,58-62` — 10^122 framing; naive mode-count "still gives a too-large naive answer"; DE reframed as latent heat, not zero-point energy (magnitude path rejected).

**Cascade address (★QUARANTINE — Grant-walked ruling-grade input)**
- `manuscript/ave-kb/common/translation-tables/translation-circuit.md:126` (Machian-G = distributed transmission-line input impedance at Hubble-horizon termination; re-confirmed `:335,:410`).

**Engine state (sector header)**
- `manuscript/ave-kb/common/engine-capability-map.md:155` — "F6 = ABSENT-INVENTED; `solve_backreaction` is static-elliptic, no `a(t)` evolver" (this anchor covers the static-elliptic / no-`a(t)` clauses ONLY); `:152` (F6 = the irreversible DE-tracks-matter sibling of the reversible #86 loop); `:145` (#86 two-way back-reaction PRESENT/LANDED 2026-06-29).
- `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:130` — "Total state vector + global conservation law | **ABSENT** | only LOCAL first-law + ∂_tρ_n=0 anywhere in Vol-3 cosmology" (the first-law / no-global-state clause's true home — re-anchored off `engine-capability-map.md:155`, which contains neither token); `:122` (`ΔE_cryst` from `{ℓ_node,α,G}` = OPEN).

**Licensed mechanisms**
- `research/2026-07-10_x40-ring-closure-transient_result.md:18-20,161` — X40 discrete minting: `f_E=1/10` trapped, flux linkage Λ banked whole, drift `2.2e-16`, minted at the discrete ring-completion event.
- `src/ave/core/cross_sector_coupling.py:137-141` — skew-Hermitian 3-port circulator: "one-way circulation needs the 3-port loop, **magnitude imposed**" (PR #321).

**Diode class dead four ways + v4/v5**
- `research/2026-06-08_rrad-l-rectification_result.md:67-73` — Ax4 kernel even-in-A ⇒ identical 2nd-order momentum for symmetric/asymmetric drive. **⚠ SCOPE FLAG:** the direct RUN null is regime-scoped by the doc's own Rule-12 header (`:14,:18`, sub-yield-linear shear = wrong regime); the regime-independent bulk-channel closure is **dead-by-derivation on UNMERGED branch `5969bda1`** (cite-by-branch, off main).
- `manuscript/ave-kb/common/substrate-hysteresis-index.md:24-25` (Level-1 reversible/memoryless vs Level-2 memristive `∮S dr` = dissipated energy/cycle); `:96` ("**any** rectification/latching/path-memory requires the Level-2 dynamics, which the smooth √(1−A²) kernel does not implement").
- `research/2026-07-08_p4-forward-voltage-threshold_RESULT.md:19,26,30-33,52-56` — "V_f is FREE — no canonical scale forces a forward-voltage dead zone"; kernel analytic at origin, dispersion gapless, no FORCED-bin row.
- `manuscript/ave-kb/common/substrate-native-terminology.md:62` — plastic/STZ sub-yield dissipation "imports dissipation, which would radiate, contradicting the result" (amorphous-retirement precedent; FAILs Ax3).
- `src/ave/core/crystal_graft_v4.py:159-167` — trilinear `H=κ̃∫gV[w·∇×ω]` = INDEFINITE Hamiltonian, unbounded below, PUMP/DETONATE. **⚠ LINE-DRIFT FLAG:** the brief cited `:160-166`; the verbatim comment block spans `:159-167` at this HEAD (core detonation lines `:160-162`).
- `research/2026-06-10_bemf-feedback-smoke_result.md` §8 `:94` — v5 spec, verbatim: "a **norm-preserving (bounded) photon→ω helicity-transfer** coupling — an orthogonal field-space rotation … rather than a trilinear potential" and "**The missing primitive is depletion, not reaction.**" **⚠ SPLICE FLAG (finding-corrected):** the all-caps "SOURCE DEPLETION, NOT REACTION" phrasing lives in the doc's Rule-12 header at `:10,:12`, OUTSIDE the §8 body — cite it separately, not as a `:92-94` verbatim.
