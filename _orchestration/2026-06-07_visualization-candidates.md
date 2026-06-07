# Visualization / animation candidates — electron-structure synthesis (2026-06-07)

Marked per Grant: implement once we have positive simulations, OR sooner if they'd help **adjudicate missing pieces/dynamics**. Two priority tags:
- **[ADJ]** adjudication-aid — would help Grant see/decide a *currently-open* dynamic NOW (before positive sims).
- **[POST]** post-positive-sim — render once the genesis/confinement sim returns positive.

| # | Visual | Shows | Tag | Type |
|---|--------|-------|-----|------|
| 1 | **Trefoil-on-sphere projection** | the rotor's real-space path = a spherical-trefoil curve (the real-space *shadow* of the phase-space `(2,3)`), time-averaging to the charge sphere; traced as the path of mutual tension between host node + neighbor nodes | **[ADJ]** | animation |
| 2 | **Interstitial Meissner/maglev B-bag** | the B-vortex bag levitating between saturated nodes (Meissner-expelled), frictionless; self-caging | [ADJ]+[POST] | animation |
| 3 | **Rotor = zitterbewegung** | the B-loop circulating at `ω_C`; the spherical envelope forming as time-average; mass↔spin one oscillation | **[ADJ]** | animation |
| 4 | **Spin double-cover (720°)** | the dipole double-covering the A–B bipartite lattice — returns to itself only after two sublattice cycles (= ½ spin) | **[ADJ]** | animation |
| 5 | **E↔node / B↔bond LC-ladder wave** | a wave propagating: E (voltage) charging node shunt-C, B (current) flowing through bond series-L between nodes | [ADJ] | animation |
| 6 | **Neighbor differential-torque field** | the host node's B/E field under the differential torque of its K4 neighbors — the tension field whose closed path is the trefoil | **[ADJ]** | static + animation |
| 7 | **Genesis: photon → self-trapped electron** | the ω-shear photon self-trapping into the confined loop (the canonical "electron = self-trapped photon") | [POST] | animation |
| 8 | **Annihilation `ω+(−ω)=0`** | two bags meeting, the inductive energy unwinding into 2γ | [POST] | animation |
| 9 | **Coherence/Reynolds spectrum** | qubit→Cooper-pair→…→classical along laminar→turbulent `Re_q`; decoherence = turbulence onset | [ADJ] | static/interactive |
| 10 | **RGB-LED spinor demo (physical lab)** | RGB strip on a physical loop, color-cycling with rotation — the color returns to start only after **two** full rotations (720°), demonstrating the spinor double-cover / spin-½ *live*; trefoil path traced in color | [POST]/lab | hardware |

**Adjudication-priority (render first, would unblock Grant's calls):** #1 (trefoil = neighbor-tension path — bears on the (2,3)-real-space-projection question + whether "3" tracks neighbor count), #3+#4 (spin/mass-one-oscillation + ½-spin double-cover — the spin-stabilization story), #6 (the differential-torque tension field — the trefoil's *origin*).

**Note:** these are diagnostic/communication aids, not load-bearing sims. None substitutes for the actual genesis/confinement run. Folded here so they survive compaction; the rotor + coherence research docs should reference this file.
