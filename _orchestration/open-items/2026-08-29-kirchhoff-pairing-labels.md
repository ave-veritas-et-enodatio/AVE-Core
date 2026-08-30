---
id: kirchhoff-pairing-labels
title: "Kirchhoff-method leaf: keep the LC leapfrog; relabel V/I parentheticals to TKI (voltage=stress, current=velocity) — not a #1020 rewrite"
status: PARKED
owner: grant
opened: 2026-08-29
source: manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md
anchor: "representing inductive flux or physical lattice strain between nodes"
---

Surfaced in the #1020 picture-lock, **outside that PR’s scope**. The leapfrog is standard Faraday + KCL: \(I \leftarrow I + (\Delta t/L)(V_A-V_B)\), \(V \leftarrow V + (\Delta t/C)\sum I\). Those two voltages are **one** KVL quantity (node difference = inductor voltage), not a Faraday/electrostatic mix-up. The defect is the **mechanical names**: strut \(I\) as “strain,” node \(V\) as “displacement or voltage,” update titled “Edge Strain Update.” TKI (`def-1mpanl`) pins \(I\) = velocity, \(V\) = stress, \(Q\) = displacement.

**Grant (2026-08-29, later):** agrees — Faraday and node voltage are one KVL quantity; the defect is mechanical names; leaf not edited this work. Wording PR parked as S1.
