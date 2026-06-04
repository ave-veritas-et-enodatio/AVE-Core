# Double-Slit + Photon-Structure EE Mapping — Orchestration Brief / Pre-reg

**Branch:** `analysis/double-slit-ee-mapping` (off `main`)
**Session type:** Implementor (single-deliverable; KB-only — no engine code, no `.py` touched)
**Discipline applied:** `ave-ee-first-mapping` (Step 6 land+mirror+regime-tag+cross-ref), `consistency-vs-emergence` (classify as translation/consistency), `ave-evidence-framing-discipline` (honest flags carried verbatim), `verify-before-cite` (every anchor grep-confirmed before landing), `ave-canonical-source`, `substrate-native-check` trigger-6 (EE IS substrate-native — no SM leakage in prose), Pure-AVE-corpus rule.
**Status:** _populated incrementally; see commit log._

---

## 1 — Purpose

Consolidate the (now-reconciled) AVE double-slit mechanism and free-photon-vs-self-trapped-electron structure into two new canonical KB leaves plus the cross-cutting circuit translation table, closing the "consolidating leaf pending" flag that `translation-circuit.md:173` carries on the photon E↔B row.

This is a **consistency / translation** consolidation (per `consistency-vs-emergence`): every mapping row is an identification between a substrate primitive (already canonical elsewhere) and its EE component. NONE of it is an emergence test or a new derivation. The leaves originate **no** new claims (`no-claim:` frontmatter) — they reference the owning claims by cross-link.

---

## 2 — Deliverables

1. **`_orchestration/double-slit-ee-mapping.md`** (this file) — brief / pre-reg / audit trail.
2. **`manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/double-slit-ee-mapping.md`** — consolidated double-slit EE/glossary mapping leaf.
3. **`manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md`** — photon's consolidating EE-mapping leaf (the `:173`-flagged pending leaf).
4. **`manuscript/ave-kb/common/translation-tables/translation-circuit.md`** — mirror the new rows into §4/§4.5; flip the `:173` E↔B row's pending-note to point at the new photon-ee-mapping leaf; regime-tag reused symbols.
5. **Cross-ref back-links** from `ohmic-decoherence-born.md` + `photon-identification.md` to the new leaves.

---

## 3 — Corpus state (3-grep synthesis summary)

Three corpus threads converge on the double-slit + photon-structure picture; they had drifted out of sync (the "helical photon" and "bubble" vocabularies were ambiguous across them). The reconciliation below is the corrected canon.

**(a) Photon-identification thread** — `vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`. Canonical: photon = K4 4-port $A_1 \oplus T_2$ decomposition, $A_1$ (longitudinal) dissipates to zero, $T_2$ (transverse microrotation) survives. Free photon is **single-sector** ($T_2$ only): $u = 0$, $\omega \neq 0$, sub-saturation ($\Delta\phi \ll \alpha$), matched at $Z_0 \approx 376.7\,\Omega$ ($\Gamma = 0$), no core. The "electron is a self-trapped photon" — same $T_2$ wave, parameterized only by whether Axiom-4 self-saturation has engaged. The **dual-sector helical photon** ($u \neq 0$ AND $\omega \neq 0$, Doc 105) is **RETRACTED** (`:93`, "Doc 107 correction") as empirically wrong. Owns clm-3npynp, clm-i4p11y, clm-fr3mos.

**(b) Self-trapped-electron / Local-Bubble thread** — `vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md` + `vol1/dynamics/ch3-quantum-signal-dynamics/zero-impedance-boundary.md` + `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:78-79`. At saturation, the **magnetic branch** shorts: Cosserat $\mu_{eff} \to 0$, $Z = \sqrt{\mu_{eff}/\varepsilon_0} \to 0$, $\Gamma \to -1$ (SHORT-circuit). The trapped wave self-creates a spherical $0\,\Omega$ "Local Bubble" ($c_{local} \to 0$, hyper-rigid localized envelope) — the **matter core**, bubble-LIKE but NOT the free photon. The **electric branch** ($\varepsilon_{eff} \to 0$, $Z \to \infty$, $\Gamma \to +1$, open-circuit) is the OTHER, mutually-exclusive Ax-4 branch (dielectric rupture). Owns clm-lv3uw1 (magnetic-branch confinement). EE map (gate-(b) CLOSED 2026-06-04, `translation-circuit.md:240`): a **shorted $\lambda/4$ resonator**.

**(c) Double-slit / Ohmic-decoherence / Born thread** — `vol1/dynamics/ch3-quantum-signal-dynamics/ohmic-decoherence-born.md`. Mechanism: the topological defect (the particle = electron / self-trapped photon) passes through ONE slit; its continuous transverse inductive wake ($\propto \nabla|\Psi|^2$, ponderomotive) passes through BOTH; the defect deterministically navigates the ponderomotive gradients into the standing-wave troughs (`:11`). Which-path = Ohmic/Joule decoherence: a detector is a resistive mechanical load $Z_{detector}$, extracting $W_{extracted} \propto |\partial_t\mathbf{A}|^2/Z_{detector}$ (`:18,23`), thermalizing the phase wave and attenuating the fringes (`:34`). Born-rule path CLOSED 2026-05-26 (7-step master-equation chain, `:36-61`); screen intensity $= |\partial_t\mathbf{A}|^2 \equiv |\Psi|^2$ (`:31`); scope = AC / sign-symmetric signals only (`:59`). Owns clm-7zuwtm, clm-ldmvwi, clm-zuf7g1.

**Distinctness guard (load-bearing):** the double-slit **ponderomotive wake** ($\propto \nabla|\Psi|^2$, near-field, navigates the particle) is NOT the **thrust dark-wake** ($\tau^{far}_{zx}$, far-field reaction momentum). The $\tau_{zx}$ derivation is an explicit OPEN gap (`dark-wake-bemf-foc-synthesis.md:100`; `translation-circuit.md:139`). Do NOT import $\tau_{zx}$ / Op14-thrust math into the double-slit leaf.

**Cavitation-bubble guard:** the sonoluminescence "cavitation bubble" proper is a DIFFERENT mechanism — saturated Rayleigh-Plesset inertia ($\rho_{eff} = \rho_0/(1-\mathrm{M}^2)^{3/2}$, `sonoluminescence-derivation.md:25-27`), NOT the $\Gamma = -1$ self-created cavity. The two must never merge.

---

## 4 — The reconciled physics (corrected canon)

| Object | Substrate state | Impedance / reflection | Core? | EE component |
|---|---|---|---|---|
| **Free photon** | single-sector $T_2$-only transverse Cosserat shear wave; $u = 0$, $\omega \neq 0$, sub-saturation $\Delta\phi \ll \alpha$ | $Z = Z_0 \approx 376.7\,\Omega$, **matched ($\Gamma = 0$)** | NO core, NO bubble | matched lossless transmission line; carrier × Gaussian envelope (informal) |
| **Electron** | a **self-trapped photon** — same $T_2$ wave at saturation amplitude $\Delta\phi \to \alpha$ | magnetic branch shorts: $\mu_{eff} \to 0$, $Z \to 0$, **$\Gamma = -1$ (SHORT)** | YES — the $\Gamma = -1$ self-created $0\,\Omega$ "Local Bubble" | a **shorted $\lambda/4$ resonator** (the matter core) |
| **"Bubble" / core** | the electron's $\Gamma = -1$ self-created $0\,\Omega$ cavity; $c_{local} \to 0$, hyper-rigid envelope | $0\,\Omega$ boundary, total internal reflection | IS the matter core (bubble-LIKE, self-confined) — NOT the free photon | shorted $\lambda/4$ resonator wall (EE) |

**Mutually-exclusive Ax-4 branches** (`master-equation.md:78-79`, clm-lv3uw1): the magnetic branch ($\mu_{eff} \to 0$, $Z \to 0$, $\Gamma \to -1$, SHORT-circuit, → particle confinement / rest mass) and the electric branch ($\varepsilon_{eff} \to 0$, $Z \to \infty$, $\Gamma \to +1$, open-circuit, → dielectric rupture). The electron is the **magnetic / SHORT / $\Gamma = -1$** branch — do not conflate with the open-circuit branch.

**Double-slit mechanism** (the "particle" = the electron / self-trapped photon): the defect / core threads one slit; the transverse inductive wake ($\propto \nabla|\Psi|^2$, ponderomotive) threads both; deterministic ponderomotive navigation $\mathbf{F} \propto \nabla|\Psi|^2$ steers the defect into the standing-wave troughs (`ohmic-decoherence-born.md:11`). Screen $= |\partial_t\mathbf{A}|^2 \equiv |\Psi|^2$ (`:31`, Born-path CLOSED 2026-05-26, `:36-61`). Scope: AC / sign-symmetric signals only (`:59`).

**Which-path** = Ohmic / Joule decoherence: detector = resistive mechanical load $Z_{det}$, $W_{extracted} \propto |\partial_t\mathbf{A}|^2/Z_{det}$ (`:18,23,34`).

**AVE-distinct falsifiable prediction:** fringe visibility $V$ vs detector impedance $Z_{det}$ is **continuous** (Γ-detune), vs Copenhagen binary (`double_slit_design_space.py:17-20`).

**Carrier + envelope** (real but informal): carrier $\omega$ × Gaussian envelope (`photon_propagation.py:74,77`; `animate_vacuum_phonon_3d.py:63`).

---

## 5 — The mapping table (double-slit component → substrate primitive → EE component)

| Component | Substrate primitive | EE component | Anchor | Status |
|---|---|---|---|---|
| **Free photon** | $T_2$-only transverse Cosserat shear wave; $u=0$, $\omega\neq0$, $\Delta\phi\ll\alpha$ | matched ($\Gamma=0$) lossless transmission line at $Z_0$ | `photon-identification.md:11,24` | ✓-VERIFIED canonical |
| **Carrier** | oscillation frequency $\omega$ of the $T_2$ wave | RF carrier | `photon_propagation.py:74`; `animate_vacuum_phonon_3d.py:63` | informal (visualization choice) |
| **Envelope** | Gaussian amplitude modulation in time/space | bandwidth-limited pulse envelope | `photon_propagation.py:77`; `animate_vacuum_phonon_3d.py:63` | informal |
| **Electron (the "particle")** | self-trapped photon; $T_2$ wave at $\Delta\phi\to\alpha$, magnetic branch shorts | shorted $\lambda/4$ resonator | `photon-identification.md:11`; `translation-circuit.md:240` | ✓ (electron=self-trapped-photon canonical; λ/4 gate-(b) CLOSED) |
| **"Bubble" / core** | $\Gamma=-1$ self-created $0\,\Omega$ Local Bubble; $c_{local}\to0$ | shorted $\lambda/4$ resonator wall ($0\,\Omega$ short) | `resonant-lc-solitons.md:50`; `zero-impedance-boundary.md:51`; `translation-circuit.md:115` | ✓ (Γ=−1 SHORT canonical) |
| **Rest mass** | trapped reactive energy in the $\Gamma=-1$ standing wave | stored reactive energy of the shorted resonator | `master-equation.md:79`; `zero-impedance-boundary.md:51` | ✓ (magnetic-branch confinement, clm-lv3uw1) |
| **Transverse wake** | continuous transverse inductive wake $\propto\nabla|\Psi|^2$ (ponderomotive) | near-field ponderomotive gradient (NOT $\tau^{far}_{zx}$) | `ohmic-decoherence-born.md:11`; distinct from `translation-circuit.md:139` | ✓ (Born-path closed); regime-tagged ≠ dark-wake |
| **Slit wall** | impedance discontinuity / aperture in the lattice | aperture / boundary discontinuity in the line | `ohmic-decoherence-born.md:11` (wake through both slits) | consistency |
| **Detector / observer** | resistive mechanical load coupling to the $\mathbf{A}$-field | resistive load $Z_{det}$ (Joule sink) | `ohmic-decoherence-born.md:18,23` | ✓ (clm-ldmvwi) |
| **Which-path decoherence** | Ohmic thermalization of the phase wave; $W_{extracted}\propto|\partial_t\mathbf{A}|^2/Z_{det}$ | $P = V^2/R$ Joule heating at the load | `ohmic-decoherence-born.md:18,23,34` | ✓ (clm-ldmvwi) |
| **Screen / Born rule** | $P(\text{click}\mid x_n) = |\partial_t\mathbf{A}(x_n)|^2/\int|\partial_t\mathbf{A}|^2 \equiv |\Psi|^2$ | detector capture-work at Joule-integration boundary | `ohmic-decoherence-born.md:31,36-61` | ✓ (Born-path CLOSED 2026-05-26; AC/sign-symmetric scope `:59`) |
| **de-Broglie wave** | transverse standing-wave troughs the defect navigates | standing-wave pattern on the line | `ohmic-decoherence-born.md:11` | consistency |
| **Visibility vs impedance** | $V$ vs $Z_{det}$ CONTINUOUS (Γ-detune) | continuous decoherence vs binary collapse | `double_slit_design_space.py:17-20` | AVE-distinct falsifiable prediction |

---

## 6 — Honest-status flags (carry verbatim into the leaves)

- **Photon E↔B row** (`translation-circuit.md:173,233`) is **⚠ partial, gate-(a)-passed 2026-06-04, consolidating leaf PENDING**. The new `photon-ee-mapping.md` leaf IS that pending leaf; on landing it, flip the `:173` note to point at it.
- **R·r = ¼ is NOT canonical** — Class-B, contradicts honest-α (`translation-circuit.md:230`: "the substrate does NOT independently select R·r=1/4"). Do not present it as derived. (clm-0ktpcn Class-B.)
- **Soliton self-lock / autoresonance at $\Gamma = -1$ is underived** (✗ GAP, `translation-circuit.md:202,217`).
- **Helical photon RETRACTED** — `photon-identification.md:93` ("Doc 107 correction"): the dual-sector helical-photon framing is empirically wrong; the canonical photon is single-sector ($T_2$ only). `simulate_double_slit_observer.py:6` still uses the retracted "helical soliton" framing — note as **superseded**, do NOT propagate.
- **Every mapping entry is a consistency / translation identification** (`consistency-vs-emergence`: NOT an emergence test, NOT a new derivation). Both leaves classify themselves as such explicitly and carry `no-claim:` frontmatter.
- **Wake distinctness:** the ponderomotive wake ($\nabla|\Psi|^2$) is regime-tagged distinct from the thrust dark-wake ($\tau^{far}_{zx}$, OPEN gap). Do not import $\tau_{zx}$/Op14 thrust math.
- **Cavitation-bubble distinctness:** sonoluminescence cavitation = saturated Rayleigh-Plesset inertia, a DIFFERENT mechanism from the $\Gamma=-1$ cavity.

---

## 7 — Auditor queue (for the orchestrator audit + merge)

The orchestrator audits this branch and merges. Queue items:

1. **Verify the two new leaves carry `no-claim:` not spurious `claims:`.** Both are consolidation/translation leaves that originate no new derivation (consistency-vs-emergence: translation/consistency class). Confirm neither invents a `clm-` id. They reference owning claims (clm-3npynp/i4p11y/fr3mos, clm-lv3uw1, clm-7zuwtm/ldmvwi/zuf7g1, clm-eemap1) by body cross-link only.
2. **Confirm the `translation-circuit.md:173` E↔B row pending-note now points at `photon-ee-mapping.md`** (was "consolidating canonical leaf pending"). The mirror in §4.5(b) Impedance & transmission family must be updated, not duplicated.
3. **Regime-tag audit on the new §4 double-slit cluster:** the wake row must read "ponderomotive $\nabla|\Psi|^2$ (near-field, NOT $\tau^{far}_{zx}$)" so the symbol reuse vs the existing dark-wake row (`:139`) is disambiguated end-to-end.
4. **Honest-flag fidelity:** confirm the R·r≠¼ Class-B flag, the helical-photon retraction, and the autoresonance-underived ✗ GAP are carried verbatim (not softened) into both leaves.
5. **`make verify` + `verify-md-links` green** on the branch tip (run pre-commit each section; orchestrator re-runs at merge).
6. **Cross-ref back-links present** in `ohmic-decoherence-born.md` (→ double-slit-ee-mapping) and `photon-identification.md` (→ photon-ee-mapping + double-slit-ee-mapping).
7. **Index updates:** `ch3.../index.md` lists the double-slit-ee-mapping leaf; `ch4.../index.md` lists the photon-ee-mapping leaf. No `subtree-claims` hand-edits (both leaves are `no-claim`, so `subtree-claims` is unchanged — verify `make refresh-kb-metadata` is a no-op on claims).

**Corpus-state change to land (auditor lands, implementer surfaces):** the `:173` pending flag closes; if the orchestrator tracks an EE-mapping work-queue entry for "photon E↔B consolidating leaf," mark it DONE.

---

## 8 — Anchor re-verification log (verify-before-cite, all confirmed at branch-creation 2026-06-04)

All anchors below were grep/Read-confirmed against `analysis/double-slit-ee-mapping` HEAD (== `main` tip `947b2c49`) before any leaf content landed. **No anchor failed re-verification.**

| Anchor | Verbatim content confirmed | Result |
|---|---|---|
| `photon-identification.md:11` | "The electron is a self-trapped photon"; photon = $T_2$-only, $u=0$, $\omega\neq0$ | ✓ |
| `photon-identification.md:24` | photon row: $u=0$, $\omega\neq0$, no saturation $\Delta\phi\ll\alpha$, linear $Z=Z_0$ | ✓ |
| `photon-identification.md:93` | "Doc 105's dual-sector helical-photon framing … is empirically wrong … canonical photon is single-sector (T₂ only)" | ✓ |
| `translation-circuit.md:115` | $\Gamma=-1$ = SHORT-circuit, magnetic branch $\mu_{eff}\to0$, $Z\to0$; electric branch $\Gamma\to+1$ open, mutually exclusive | ✓ |
| `translation-circuit.md:139` | dark wake = $\tau^{far}_{zx}$ far-field radiated shear stress (the thrust wake) | ✓ |
| `translation-circuit.md:173` | I/Q $(V_{inc},V_{ref})$ photon E↔B row, ⚠, "consolidating canonical leaf pending", gate (a) 2026-06-04 | ✓ |
| `translation-circuit.md:202,217` | autoresonance / soliton self-lock at $\Gamma=-1$ = ✗ GAP, underived | ✓ |
| `translation-circuit.md:230` | "the substrate does NOT independently select R·r=1/4" | ✓ |
| `translation-circuit.md:233` | "(I) Intra-K4, the photon's own E↔B — LINEAR, PRESENT: V_inc/V_ref ↔ Φ_link" | ✓ |
| `translation-circuit.md:240` | shorted $\lambda/4$ resonator, gate-(b) CLOSED 2026-06-04 | ✓ |
| `resonant-lc-solitons.md:50` | "weaves its own perfect topological mirror … 'Local Bubble' … hyper-rigid, localized envelope"; $c_{local}\to0$ | ✓ |
| `zero-impedance-boundary.md:51` | "trapped inside a spherical $0\,\Omega$ impedance boundary of its own geometric creation" | ✓ |
| `sonoluminescence-derivation.md:25-27` | saturated Rayleigh-Plesset: $\rho_{eff}=\rho_0/(1-\mathrm{M}^2)^{3/2}$ | ✓ |
| `master-equation.md:78-79` | two mutually-exclusive Ax-4 branches (electric open $\Gamma\to+1$ / magnetic short $\Gamma\to-1$), clm-lv3uw1 | ✓ |
| `ohmic-decoherence-born.md:11` | defect through Slit A, wake through both, $\mathbf{F}\propto\nabla|\Psi|^2$ navigation | ✓ |
| `ohmic-decoherence-born.md:18,23` | detector = resistive load; $W_{extracted}\propto|\partial_t\mathbf{A}|^2/Z_{detector}$ | ✓ |
| `ohmic-decoherence-born.md:31` | $P(\text{click}\mid x_n)=|\partial_t\mathbf{A}|^2/\int|\partial_t\mathbf{A}|^2\equiv|\Psi|^2$ | ✓ |
| `ohmic-decoherence-born.md:34` | "permanently attenuating the interference gradients" (Ohmic thermalization) | ✓ |
| `ohmic-decoherence-born.md:36-61` | Born-rule master-equation path CLOSED 2026-05-26 (7-step chain) | ✓ |
| `ohmic-decoherence-born.md:59` | scope: "AC signals or sign-symmetric signal ensembles" | ✓ |
| `dark-wake-bemf-foc-synthesis.md:100` | $\tau_{zx}$ "asserted … but NOT yet derived … an explicit open gap" | ✓ |
| `double_slit_design_space.py:17-20` | Copenhagen binary vs AVE continuous decoherence ∝ impedance — testable, falsifiable | ✓ |
| `photon_propagation.py:74,77` | carrier frequency $\omega$ (`:74`); temporal Gaussian envelope (`:77`) | ✓ |
| `animate_vacuum_phonon_3d.py:63` | "A 'photon': Gaussian envelope × sinusoidal carrier frequency" | ✓ |
| `simulate_double_slit_observer.py:6` | "a 'photon' is a helical soliton" — the RETRACTED framing (note as superseded) | ✓ (superseded) |
