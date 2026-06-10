# Novel-Objects Report — Engine-Created, Canon-Unnamed Objects (for Grant's independent review)

> **NOT NORMATIVE. REVIEW-PENDING.** This is the side-report companion to
> `research/2026-06-10_field-symbol-registry.md`. It lists every object the 2026-06-09..10 arc and its
> engines **created** that canon has **not** named or blessed. **None of these are canon. None enter the
> registry's normative table** except where the registry explicitly carries them as branch-tagged
> engine-constructs (descriptive, `[branch UNMERGED]`) or as future `⟂PROPOSED` rows after Grant's
> review. The point of separating this report is exactly so engine-constructs are never silently
> promoted into the normative table as if canonical (`ave-evidence-framing-discipline`).
>
> **Each entry:** what it is | where it arose (run/doc) | why canon may need it | proposed symbol+name |
> **status** ∈ {engine-construct, candidate-physics, hypothesis}. Status is a claim-class tag, not a
> verdict — Grant adjudicates promotion.
>
> **Verification note (`verify-before-cite`):** branch anchors were verified via git objects this
> session and are tagged with their branch (all UNMERGED). One object (the v6 exchange quantum $\delta L$)
> has **no committed anchor anywhere** — flagged UNVERIFIABLE (N6).

---

## A. Engine-constructs (bookkeeping the integrator needs; not yet claimed as physics)

### N1 — the latent tally: `latent_ledger` + `paid_ledger`
- **What it is:** per-cell snap stored-energy tally (`latent_ledger`, "held-out per cell") plus a
  payback ledger (`paid_ledger`, "paid-back per cell"); a snapped cell may re-enter the normal state
  only when `paid_ledger ≥ latent_ledger`. Hysteresis implemented **by bookkeeping**, with no new EOS.
- **Where it arose:** `src/ave/core/unified_genesis_engine.py:145-146` (commit 5e6485a8);
  D1 definition `2026-06-10_genesis-v5-seeded-snap_prereg.md:72-74`. [branch v5, UNMERGED]
- **Why canon may need it:** it is the state variable that makes the snap irreversible without inventing
  a new constitutive law — a candidate substrate-native model of latent heat of the local freeze.
- **Proposed symbol+name:** $\mathcal{L}_{cell}$ / $\mathcal{P}_{cell}$ — "latent tally / paid tally".
- **Status:** engine-construct.

### N2 — the burst detector + FLASH burst (D6)
- **What it is:** `LongitudinalBurstDetector`, an instrument reading impulsive latent release in the bulk
  EOS ledger; calibrated known-null floor $F_{0d}=3.84\times10^{-5}$ (cleared by 3–6 OOM); the detected
  event is the "FLASH burst".
- **Where it arose:** `src/ave/core/longitudinal_burst_detector.py`; `2026-06-10_genesis-v5-seeded-snap_result.md:92,98-101`. [branch v5, UNMERGED]
- **Why canon may need it:** a calibrated observable (with a known-null floor, per the
  apparatus-floor-attribution discipline) for the D6 birth/vent detection class — the bulk-ledger analog
  of an S11 ring-down probe.
- **Proposed symbol+name:** the **D6 longitudinal-burst observable** (keep the detector name; the event =
  "FLASH burst").
- **Status:** engine-construct (detector observable).

### N3 — the snap state machine + snapped-cell material state
- **What it is:** a per-cell `normal ↔ snapped` state machine; on crossing the floor the bulk impedance
  $Z_{bulk}=\rho c \to 0$ so $\Gamma \to -1$ and the cell becomes a **boundary-class** (sonic-horizon)
  reflector. The "snapped" value is a per-cell **material state**, not a field value.
- **Where it arose:** `unified_genesis_engine.py:291-293` (commit 5e6485a8); `2026-06-10_genesis-v5-seeded-snap_prereg.md:47,64,72-74`. [branch v5, UNMERGED]
- **Why canon may need it:** matter genesis in the engine is mediated by this discrete state; if it is
  physical it is a new substrate phase label (a two-state-per-cell order field).
- **Proposed symbol+name:** $\sigma_{cell}\in\{0,1\}$ — "snap state"; the snapped state = the
  boundary-class reflector cell.
- **Status:** engine-construct → candidate-physics (the SNAP-channel verdict is UNRESOLVED /
  construction-dependent, `v5 result:195-222`).

---

## B. Candidate-physics (engine-created objects that may name real substrate physics)

### N4 — the vent / birth pulse
- **What it is:** an impulsive **longitudinal** pulse emitted at snap events ("not a wake") — the
  one-way energy delivery snap → seed (`vent_into_seed` / `E_vent_to_seed` / `E_vent_radiated`). The
  proposed D6 detection class is built to catch it.
- **Where it arose:** engine `unified_genesis_engine.py:279-280` (the `_vent_to_seed` call);
  `2026-06-10_genesis-v5-seeded-snap_prereg.md:78,94,152`; one-way vent snap→seed `v5 result:124`. [branch v5, UNMERGED]
- **Why canon may need it:** if matter genesis radiates a distinct impulsive bulk signature (vs the
  motion-trail dark wake), that is a new emission species with its own detection class.
- **Proposed symbol+name:** the **birth pulse** (event class), $\delta V_{vent}$ (impulsive bulk-longitudinal emission).
- **Status:** candidate-physics (flagged GAP-C cross-sector instantiation in the engine).

### N5 — the pocket / void: the FOURTH object (firewall)
- **What it is:** a snapped-cell density void — a **substrate-bulk-density tensile-failure pocket**
  ($c_{bulk}^2\le0$ region of the volumetric $K$ modulus); SNAP-LOCKED, persists under forced de-spin,
  $\rho_{core}=-0.618$ clamped at the candidate floor. Explicitly firewalled: **NOT** Rayleigh-Plesset,
  **NOT** photon-bubble, **NOT** the shear-sector $\Gamma=-1$ EE cavity.
- **Where it arose:** firewall `2026-06-10_sonic-horizon-closure_prereg.md:34-36`; void persistence
  `2026-06-10_genesis-v5-seeded-snap_result.md:22-23,107-108`. [branches sonichorizon + v5, UNMERGED]
- **Why canon may need it:** it is named as a genuinely distinct ("fourth") object — a new bulk-sector
  defect with its own constitutive identity, not a re-label of an existing cavity.
- **Proposed symbol+name:** the **bulk tensile-failure pocket** (the fourth object), $\mathcal{V}_{pocket}$.
- **Status:** candidate-physics (SNAP-channel verdict UNRESOLVED / construction-dependent, `v5 result:195-222`).

### N6 — motion-lock (and snap-lock) as named mechanism classes
- **What it is:** **motion-lock** — the physical angular momentum $L_{bulk}$ is conserved drive-off in
  ALL arms (incl. no-snap, ratio 0.9945) and is $\nu_{art}$-**invariant**: a persistent-current mechanism,
  "real physics, not a viscosity artifact". **snap-lock** — the density void persists under forced
  de-spin (requires the latent-tally D1). Distinct from $|L_\omega|$, which tracks the `lock_eta`
  apparatus knob (a clip, not physics).
- **Where it arose:** `2026-06-10_genesis-v5-seeded-snap_result.md:25,64,73,171-172,195,225-230`. [branch v5, UNMERGED]
- **Why canon may need it:** the genuine v5 positive — a substrate-native persistent-current /
  conserved-circulation mechanism that survives the apparatus-floor controls.
- **Proposed symbol+name:** **motion-lock** (conserved-$L_{bulk}$ persistence) and **snap-lock** (void
  persistence) as named mechanism classes.
- **Status:** candidate-physics. (The "~8 OOM" $L_{bulk}/|L_\omega|$ energy-weight figure is **UNVERIFIED**
  — do not attach it; see registry §6.3.)

### N7 — the electron self-spectrum $f_0$ (S11 small-signal bulk probe)
- **What it is:** an S11 lock-in ring-down probe that recovers known resonators to $f_0$ within 0.2%, Q
  within 5% (validated instrument), then finds the UNKNOWN electron has **no single high-Q resonance** —
  two weak dispersive peaks ($f\approx0.026,0.057$, contrast 1.1–1.5× floor, $Q_{fit}=0.73$ overdamped,
  MULTI-MODE). The 2-peak structure is flagged as a possible breather-ringdown coincidence.
- **Where it arose:** `src/ave/core/s11_probe.py`; `2026-06-10_electron-s11-sweep_result.md:14,58-65`. [branch edatasheet, UNMERGED]
- **Why canon may need it:** a validated small-signal observable + a clean **negative** (the electron is
  not a simple single-tank resonator on the $\omega$ readout) — a datasheet-grade self-spectrum result.
- **Proposed symbol+name:** the **electron self-spectrum** $f_0$ (S11 multi-mode); keep the probe name.
- **Status:** candidate-physics (engine observable; the negative is the result, the 2-peak read is open).

### N8 — the twin-pocket RH/LH split
- **What it is:** the snapped pocket splits into two sub-pockets by the rotation column's vorticity sense
  — but the split is **GEOMETRIC, not chiral**: RH=2608 / LH=1040 cells **byte-identical** across MAIN,
  C-achiral, AND C-opposite-helicity arms.
- **Where it arose:** `2026-06-10_genesis-v5-seeded-snap_result.md:107-108`. [branch v5, UNMERGED]
- **Why canon may need it:** a control result — it tells canon the pocket asymmetry is NOT the charge/
  helicity signature one might reach for; a discriminator that rules out a chiral reading.
- **Proposed symbol+name:** the **geometric twin-pocket split** (explicitly not a chiral observable).
- **Status:** candidate-physics (a negative/control observable).

### N9 — the transducer + the exchange quantum $\delta L$ (v6)
- **What it is:** the **transducer** = "a real photon-helicity → bulk-circulation/$\omega$ coupling
  channel" (the §F handedness-coupling channel), named the load-bearing primitive for the v6 T2/T5 tests.
  The **$\delta L$** = the transducer's exchange quantum (v6).
- **Where it arose:** the transducer channel is anchored at `2026-06-10_genesis-v5-seeded-snap_result.md:277,285`
  [branch v5, UNMERGED]. **$\delta L$ has NO committed anchor anywhere** — the v6 branch tip (93da170e/
  fa4420c6) carries zero v6-specific commits; $\delta L$ exists only in the running `/tmp/ave-v6` worktree,
  which was **not read** (live-worktree constraint).
- **Why canon may need it:** if a parity-odd photon-helicity→bulk-$\omega$ coupling is real, it is the
  cross-sector primitive that closes the rotation↔bulk trade (Op14 family) — potentially the genesis
  driver.
- **Proposed symbol+name:** the **transducer** (handedness-coupling channel); $\delta L$ = transducer
  exchange quantum.
- **Status:** candidate-physics (transducer) / **UNVERIFIABLE-this-turn** ($\delta L$ — running-build
  worktree only; flag, do not cite as if committed).

---

## C. Hypotheses (framings the arc proposed; some Grant-ratified-framing, none canon-number)

### N10 — the order-parameter identification (standing-$V$ = the rim-crossing order parameter)
- **What it is:** "the longitudinal field is the ORDER-PARAMETER channel … identically zero in the
  unbroken free-wave (transverse-photon) state, nonzero **exactly where a phase change occurs**." The "3"
  is the order parameter of the substrate's freeze; the phase-space signature is the Smith-rim crossing
  $|\Gamma|\to1$; the order parameter = the standing-$V$ amplitude.
- **Where it arose:** `2026-06-10_matter-as-vapor-locked-pump_framing.md:252-254,258` (on origin/main,
  PR#151 — this one IS in canon as **ratified framing**); phase-space signature `v5 prereg:74` [branch].
- **Why canon may need it:** it is the unifying "why" for the longitudinal grade re-engaging only at
  saturation — already carried as ratified-framing, not as a derived number.
- **Proposed symbol+name:** the **order-parameter reading** of the standing-$V$ channel (framing, not a
  new symbol — $V$ already has its row).
- **Status:** hypothesis / Grant-ratified-framing (framing-class, NOT an emergence-class number).

### N11 — the Meissner-class picture (BEMF = persistent screening current)
- **What it is:** a field-reading of the snap as condensation + flux expulsion, in which "the BEMF = the
  persistent screening current". This is a **same-day tension** with the 2026-06-10 PORT-only BEMF ruling
  (corr 0.117): the ruling says BEMF is PORT-class only; the Meissner picture reads it as a field
  (screening current).
- **Where it arose:** `2026-06-10_genesis-v5-seeded-snap_prereg.md:48` [branch v5, UNMERGED].
- **Why canon may need it:** IF the Meissner analogy is load-bearing, the PORT-only ruling and this
  field-reading must be reconciled (or the analogy bounded to "Meissner-LIKE"). Surfaced as a tension,
  **not resolved** (flag-don't-fix) — it also feeds RENAME-QUEUE R2 in the registry.
- **Proposed symbol+name:** the **Meissner-class snap picture** (analogy, explicitly bounded).
- **Status:** hypothesis (Grant-ratified as a picture; in tension with the PORT-only ruling — for Grant
  to adjudicate).

---

## Summary for review

| # | Object | Status | In registry table? |
|---|---|---|---|
| N1 | latent tally (`latent_ledger`/`paid_ledger`) | engine-construct | yes, branch-tagged (operators/ledgers) |
| N2 | burst detector + FLASH burst (D6) | engine-construct | yes, branch-tagged |
| N3 | snap state machine + snapped-cell state | engine-construct → candidate | yes, branch-tagged |
| N4 | vent / birth pulse | candidate-physics | yes, branch-tagged (bulk) |
| N5 | pocket / void (the fourth object) | candidate-physics | no (review-pending) |
| N6 | motion-lock / snap-lock | candidate-physics | partial ($L_{bulk}$ row, branch-tagged) |
| N7 | electron self-spectrum $f_0$ | candidate-physics | no (review-pending) |
| N8 | geometric twin-pocket split | candidate-physics | no (review-pending) |
| N9 | transducer + $\delta L$ (v6) | candidate / UNVERIFIABLE | no (review-pending) |
| N10 | order-parameter identification | hypothesis / ratified-framing | reflected in $V$ row (canon framing) |
| N11 | Meissner-class snap picture | hypothesis (in tension) | no — feeds RENAME-QUEUE R2 |

**For Grant:** N5, N7, N8, N9, N11 are the genuinely unblessed objects for independent review. N9's
$\delta L$ is UNVERIFIABLE this turn (running-build worktree only). N11 carries a live same-day tension
with the PORT-only BEMF ruling. None are promoted; the registry names only the branch-tagged
engine-constructs, descriptively, pending your call.

