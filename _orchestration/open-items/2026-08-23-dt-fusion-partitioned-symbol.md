---
id: dt-fusion-partitioned-symbol
title: simulate_dt_fusion imports a symbol the IP-partition stub no longer defines — restore, stub, or retire?
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-23
source: src/scripts/vol_6_periodic_table/simulations/spice_exporter.py
anchor: "The full SPICE export functionality has been moved to a private repository"
---

Found by the vol_6 import-repair lane (PR #992, 2026-08-23), minted per the lane's routed
question. `simulations/simulate_dt_fusion.py:5` imports `generate_fusion_netlist`, but the
IP-partition stub `simulations/spice_exporter.py` defines only `generate_spice_netlist` —
the fusion-netlist symbol was partitioned out entirely, with no stub preserving its
interface. The driver cannot run in this repo.

**Why Grant-gated:** restoring a partitioned-out symbol is a provenance/IP decision, not
hygiene — the options are (a) restore a public-safe stub or implementation of
`generate_fusion_netlist` (requires knowing what of it is L0-public vs partitioned), (b)
stub it to raise with a named pointer at the private repo (the pattern the partition used
for the exporter itself), or (c) retire the driver to `_archive` as partition-orphaned.
The new import-smoke GATE 2 carries it as a strict-xfail, so it is visible and guarded
either way; six sibling alias-unregistered sites ride the same xfail set and are pure
hygiene (no ruling needed — any lane may fix them).
