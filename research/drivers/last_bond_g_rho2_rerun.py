#!/usr/bin/env python3
"""G-RHO2 rerun v2 -- the off-limit sensitivity gate, re-sited BELOW its own crossover.

Prereg: research/2026-08-05_last-bond-g-rho2-rerun_prereg-FROZEN.md (frozen and pushed ALONE
at 503579b0, before this file existed).
Predecessor: research/2026-08-05_last-bond-kernel-collapse_{prereg-FROZEN,result}.md and
research/drivers/last_bond_kernel_collapse.py -- ALL BYTE-UNTOUCHED by this lane (gated: NC-BYTES).

This driver REUSES the v1 instrument; it reimplements nothing.  `last_bond_kernel_collapse`
is imported unmodified and its own `run_task2`, `run_task3`, `build_gates`, `build_self_tests`,
`z_load`, `gamma_from_zload` and `mp` precision configuration are the ones that execute here.
The ONLY thing this file changes is WHERE on the probe axis the G-RHO2 injections are placed:

    v1:  k_0 = eps * k_cold          eps in {1e-10, 1e-12, 1e-14}   -> delta = 3.16e4 .. 3.16
    v2:  k_0 = eps * om * Z_1        eps in {1e-6,  1e-8,  1e-10}   -> delta = 1e-6  .. 1e-10

with the dimensionless probe coordinate delta = k_0/(om*Z_1) and the crossover at delta = 1
(prereg section 2).  v1 sat ABOVE the crossover, on the plateau where the exponent is genuinely 0.

Engine fence: `src/ave` is NOT imported and NOT touched.

RUN PROTOCOL (disclosed).  The v1 TASK-1 corpus scan is TREE-STATE-DEPENDENT by the predecessor's
own section 1.3 -- its own outputs live inside the scanned tree, and this lane adds more files to
it -- so re-running it on this branch could not reproduce the shipped numbers and its failure to do
so would carry no information.  This driver therefore REPLAYS the shipped `task1_scan` block into
`build_gates`/`build_self_tests` instead of re-scanning.  G-SCAN and FT-SCAN are consequently
REPLAYED, NOT REPRODUCED; TASK 1 remains SCAN-NOT-CERTIFIED and is not touched.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))

import last_bond_kernel_collapse as v1  # noqa: E402  (the v1 instrument, imported unmodified)
from last_bond_kernel_collapse import mp  # noqa: E402  (its dps = 60 configuration, not a new one)

V1_JSON = HERE / "last_bond_kernel_collapse_results.json"

# ----------------------------------------------------------------------
# FROZEN (prereg section 3.1 / 4.2; no member may be added, removed or moved)
# ----------------------------------------------------------------------

EPS_V2_GATE = ["1e-6", "1e-8", "1e-10"]          # sub-crossover: 6, 8, 10 decades below delta = 1
EPS_V2_PLATEAU = ["1e+6", "1e+8", "1e+10"]       # FT-RHO2: 6, 8, 10 decades ABOVE delta = 1
EPS_V1_SITING = ["1e-10", "1e-12", "1e-14"]      # NC-RHO2-V1: the v1 siting, verbatim
RHO2_TOL_LO, RHO2_TOL_HI = "1.9", "2.1"          # UNCHANGED FROM v1, character for character
D_PRED_TOL = "1e-11"                             # D-RHO2-PRED: DIAGNOSTIC, explicitly NOT a gate

# The predecessor artifacts this lane must leave byte-untouched, and the commit this prereg was
# written against (pinned, not `origin/main`, so the control is reproducible).
V1_PIN_COMMIT = "c4fdced0"
V1_ARTIFACTS = [
    "research/drivers/last_bond_kernel_collapse.py",
    "research/drivers/last_bond_kernel_collapse_results.json",
    "research/drivers/last_bond_kernel_collapse_number_check.py",
    "research/2026-08-05_last-bond-kernel-collapse_result.md",
]


def operating_point() -> dict:
    """The G-RHO2 operating point, READ VERBATIM from the v1 driver's own frozen numerics."""
    S = mp.mpf("1e-9")
    ell = mp.mpf(v1.ELL_OVER_RSAT_LADDER[0])
    Z1 = S ** (1 - mp.mpf("0.5"))
    om = mp.mpf(v1.OM_OVER_OMC_GRID[1]) / ell      # the frozen middle rung, 1e-19
    k_cold = S / ell
    return {"S": S, "ell": ell, "Z1": Z1, "om": om, "k_cold": k_cold, "k0_cross": om * Z1}


def rho2_exponent(eps_list: list[str], k0_of_eps) -> dict:
    """v1's G-RHO2 fit, body-for-body, parametrized ONLY by the injection siting.

    Reuses v1.z_load and v1.gamma_from_zload -- `Gamma + 1` is never formed by adding 1.
    """
    op = operating_point()
    Z1, om = op["Z1"], op["om"]
    pts = []
    for e_str in eps_list:
        k0 = k0_of_eps(mp.mpf(e_str))
        zb1 = Z1
        zb2 = 2 * Z1
        _, r1 = v1.gamma_from_zload(v1.z_load(k0, om, zb1), Z1)
        _, r2 = v1.gamma_from_zload(v1.z_load(k0, om, zb2), Z1)
        pts.append((k0, abs(r1 - r2)))
    exps = []
    for i in range(len(pts) - 1):
        (k1, d1), (k2, d2) = pts[i], pts[i + 1]
        exps.append(mp.log(d2 / d1) / mp.log(k2 / k1))
    fitted = sum(exps) / len(exps)
    return {
        "eps_values": list(eps_list),
        "injected_k0": [v1._s(k) for k, _ in pts],
        "probe_coordinate_delta": [v1._s(k / op["k0_cross"]) for k, _ in pts],
        "measured_abs_delta_resid": [v1._s(d) for _, d in pts],
        "per_pair": [v1._s(e) for e in exps],
        "measured_exponent": v1._s(fitted),
        "_fitted": fitted,
    }


def build_v2_gate() -> dict:
    """G-RHO2, re-sited.  Tolerance [1.9, 2.1] UNCHANGED from v1."""
    op = operating_point()
    r = rho2_exponent(EPS_V2_GATE, lambda e: e * op["om"] * op["Z1"])
    fitted = r.pop("_fitted")
    lo, hi = mp.mpf(RHO2_TOL_LO), mp.mpf(RHO2_TOL_HI)
    r["frozen"] = "fitted exponent of |dGamma/dZ_beyond| vs k_0 in [1.9, 2.1]"
    r["siting"] = "k_0 = eps * om * Z_1 (v2, SUB-crossover)"
    r["min_decades_below_crossover"] = 6
    r["pass"] = lo <= fitted <= hi
    return r


def build_ft_rho2() -> dict:
    """FT-RHO2: the same instrument in the PLATEAU must drive the gate OUTSIDE [1.9, 2.1]."""
    op = operating_point()
    r = rho2_exponent(EPS_V2_PLATEAU, lambda e: e * op["om"] * op["Z1"])
    fitted = r.pop("_fitted")
    lo, hi = mp.mpf(RHO2_TOL_LO), mp.mpf(RHO2_TOL_HI)
    r["frozen"] = (
        "re-siting into the plateau (eps in {1e+6,1e+8,1e+10}, 6-10 decades ABOVE the "
        "crossover) must drive the fitted exponent OUTSIDE [1.9, 2.1], i.e. G-RHO2 must FAIL"
    )
    r["siting"] = "k_0 = eps * om * Z_1 (PLATEAU, above crossover)"
    r["min_decades_above_crossover"] = 6
    r["fires"] = not (lo <= fitted <= hi)
    return r


def build_nc_rho2_v1() -> dict:
    """NC-RHO2-V1: the v1 siting through the v2 code path must reproduce the v1 record byte-exact."""
    op = operating_point()
    r = rho2_exponent(EPS_V1_SITING, lambda e: e * op["k_cold"])
    r.pop("_fitted")
    shipped = json.loads(V1_JSON.read_text(encoding="utf-8"))["gates"]["G-RHO2"]
    mismatches = []
    if r["measured_exponent"] != shipped["measured_exponent"]:
        mismatches.append(
            f"G-RHO2.measured_exponent: v2 `{r['measured_exponent']}` != v1 `{shipped['measured_exponent']}`"
        )
    if r["per_pair"] != shipped["per_pair"]:
        mismatches.append(f"G-RHO2.per_pair: v2 {r['per_pair']} != v1 {shipped['per_pair']}")
    r["frozen"] = (
        "re-running the v1 siting (eps*k_cold) through the v2 code path must reproduce the "
        "shipped failing exponent AND both shipped per-pair values, byte-exact"
    )
    r["v1_shipped_exponent"] = shipped["measured_exponent"]
    r["v1_shipped_per_pair"] = shipped["per_pair"]
    r["n_mismatches"] = len(mismatches)
    r["mismatches"] = mismatches
    r["pass"] = not mismatches
    return r


def build_d_rho2_pred(gate: dict) -> dict:
    """D-RHO2-PRED -- a DIAGNOSTIC, explicitly NOT a gate (prereg section 4.3)."""
    dev = abs(mp.mpf(gate["measured_exponent"]) - 2)
    tol = mp.mpf(D_PRED_TOL)
    return {
        "_class": "DIAGNOSTIC, NOT A GATE -- certification does not ride on this",
        "frozen": "the measured G-RHO2 mean exponent equals 2 to within 1e-11 (prereg section 3.2)",
        "derived_expected_exponent": "2",
        "derived_predicted_deviation": v1._s(mp.mpf("0.6786") * (mp.mpf("1e-6") ** 2 + mp.mpf("1e-8") ** 2) / 2),
        "measured_deviation_from_2": v1._s(dev),
        "agrees": dev <= tol,
    }


# ----------------------------------------------------------------------
# NEGATIVE CONTROLS -- byte-exact reproduction of the v1 record
# ----------------------------------------------------------------------

REPRO_CLASS = {
    "G-BOND": "RECOMPUTED", "G-ROW": "RECOMPUTED", "G-RHO": "RECOMPUTED",
    "G-COLD": "RECOMPUTED", "G-UNIT": "RECOMPUTED", "G-PLANE": "RECOMPUTED",
    "G-PREC": "RECOMPUTED", "G-COND": "RECOMPUTED", "G-NC-ARITH": "RECOMPUTED",
    "G-NC-SIGN": "FILE-READ", "G-NC-ECHO": "FILE-READ",
    "G-SCAN": "REPLAYED",
    "FT-BOND": "RECOMPUTED", "FT-ROW": "RECOMPUTED", "FT-RHO": "RECOMPUTED",
    "FT-PLANE": "RECOMPUTED", "FT-ARITH": "RECOMPUTED", "FT-COND": "RECOMPUTED",
    "FT-SCAN": "REPLAYED",
}


def _compare_block(label: str, got: dict, want: dict, mismatches: list[str]) -> int:
    """EXACT STRING EQUALITY on the shipped renderings.  Returns the number of fields compared."""
    n = 0
    for key in sorted(set(got) | set(want)):
        if key not in got:
            mismatches.append(f"{label}.{key}: MISSING from the v2 recomputation")
            continue
        if key not in want:
            mismatches.append(f"{label}.{key}: NOT PRESENT in the v1 shipped record")
            continue
        a, b = json.dumps(got[key], sort_keys=True), json.dumps(want[key], sort_keys=True)
        n += 1
        if a != b:
            mismatches.append(f"{label}.{key}: v2 {a} != v1 {b}")
    return n


def run_negative_controls() -> dict:
    shipped = json.loads(V1_JSON.read_text(encoding="utf-8"))
    scan_replayed = shipped["task1_scan"]

    t2 = v1.run_task2()
    t3 = v1.run_task3()
    gates = v1.build_gates(t2, t3, scan_replayed)
    sts = v1.build_self_tests(scan_replayed)

    mism: list[str] = []
    n_fields = 0
    n_blocks = 0
    for name in sorted(REPRO_CLASS):
        src = gates if name.startswith("G-") else sts
        ref = shipped["gates"] if name.startswith("G-") else shipped["self_tests"]
        n_fields += _compare_block(name, src[name], ref[name], mism)
        n_blocks += 1

    # G-RHO2 in the v1-shipped rendering must also come back unchanged when v1's OWN code runs it
    n_fields += _compare_block("G-RHO2(v1-code)", gates["G-RHO2"], shipped["gates"]["G-RHO2"], mism)
    n_blocks += 1

    rows_ok = t2["n_rows"] == shipped["task2_row"]["n_rows"]
    if not rows_ok:
        mism.append(f"NC-ROWS: v2 {t2['n_rows']} != v1 {shipped['task2_row']['n_rows']}")

    return {
        "NC-GATES+NC-FT": {
            "frozen": (
                "every field of every v1 gate and self-test reproduces the shipped rendering "
                "with EXACT STRING EQUALITY, and every pass/fires flag reproduces"
            ),
            "n_blocks_compared": n_blocks,
            "n_fields_compared": n_fields,
            "n_mismatches": len(mism),
            "mismatches": mism,
            "reproduction_class": REPRO_CLASS,
            "replayed_not_reproduced": ["G-SCAN", "FT-SCAN"],
            "pass": not mism,
        },
        "NC-ROWS": {
            "frozen": "run_task2() returns the shipped n_rows",
            "measured_n_rows": t2["n_rows"],
            "v1_shipped_n_rows": shipped["task2_row"]["n_rows"],
            "pass": rows_ok,
        },
        "_v1_gate_pass_flags": {k: bool(v["pass"]) for k, v in sorted(gates.items())},
        "_v1_self_test_fire_flags": {k: bool(v["fires"]) for k, v in sorted(sts.items())},
    }


def _git_blob_id(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def build_nc_bytes() -> dict:
    """NC-BYTES: the four predecessor artifacts are byte-identical to the pinned commit."""
    rows, bad = [], []
    for rel in V1_ARTIFACTS:
        local = _git_blob_id(REPO / rel)
        try:
            ref = subprocess.run(
                ["git", "rev-parse", f"{V1_PIN_COMMIT}:{rel}"],
                cwd=REPO, capture_output=True, text=True, check=True,
            ).stdout.strip()
        except Exception as exc:  # noqa: BLE001
            ref = f"UNAVAILABLE({type(exc).__name__})"
        ok = local == ref
        rows.append({"path": rel, "blob_local": local, "blob_at_pin": ref, "identical": ok})
        if not ok:
            bad.append(rel)
    return {
        "frozen": (
            f"each predecessor artifact's blob id equals its blob id at {V1_PIN_COMMIT} -- "
            "this lane touched none of them"
        ),
        "pin_commit": V1_PIN_COMMIT,
        "artifacts": rows,
        "n_modified": len(bad),
        "modified": bad,
        "pass": not bad,
    }


def main() -> None:
    t0 = time.time()
    nc = run_negative_controls()
    nc_bytes = build_nc_bytes()
    nc_rho2_v1 = build_nc_rho2_v1()
    gate = build_v2_gate()
    ft = build_ft_rho2()
    diag = build_d_rho2_pred(gate)
    op = operating_point()

    controls = {
        "NC-GATES+NC-FT": nc["NC-GATES+NC-FT"],
        "NC-ROWS": nc["NC-ROWS"],
        "NC-RHO2-V1": nc_rho2_v1,
        "NC-BYTES": nc_bytes,
    }

    task2_gates = ["G-BOND", "G-ROW", "G-RHO", "G-COLD", "G-UNIT", "G-PLANE",
                   "G-NC-SIGN", "G-NC-ECHO", "G-NC-ARITH"]
    task2_fts = ["FT-BOND", "FT-ROW", "FT-RHO", "FT-PLANE", "FT-ARITH"]
    task2_ok = (
        gate["pass"]
        and ft["fires"]
        and all(v["pass"] for v in controls.values())
        and all(nc["_v1_gate_pass_flags"][k] for k in task2_gates)
        and all(nc["_v1_self_test_fire_flags"][k] for k in task2_fts)
    )

    out = {
        "_prereg": "research/2026-08-05_last-bond-g-rho2-rerun_prereg-FROZEN.md",
        "_prereg_commit": "503579b0",
        "_predecessor": "research/2026-08-05_last-bond-kernel-collapse_result.md",
        "_method": (
            "The v1 instrument is IMPORTED UNMODIFIED and reused; only the G-RHO2 injection "
            "siting moves, from k_0 = eps*k_cold (v1, ABOVE the crossover) to k_0 = eps*om*Z_1 "
            "(v2, 6-10 decades BELOW it).  The crossover delta = k_0/(om*Z_1) = 1 is derived in "
            "prereg section 2 from the shipped v1 parameters alone."
        ),
        "_non_claim": (
            "DERIVATION result.  Mints no clm-/def-; propagates to no KB/manuscript leaf; changes "
            "no solidity; edits no falsification ledger; src/ave byte-untouched and not imported.  "
            "Certifies TASK 2 of the predecessor and NOTHING ELSE.  TASK 1 remains "
            "SCAN-NOT-CERTIFIED and is not touched; TASK 3 is not touched; BIN-C-DISJOINT is not "
            "revisited.  The print-language consequence is RECORDED for the propagation pass, "
            "NOT executed here."
        ),
        "_frozen_numerics": {
            "eps_v2_gate": EPS_V2_GATE,
            "eps_v2_plateau": EPS_V2_PLATEAU,
            "eps_v1_siting": EPS_V1_SITING,
            "rho2_tolerance": [RHO2_TOL_LO, RHO2_TOL_HI],
            "d_pred_tolerance": D_PRED_TOL,
            "dps": v1.DPS,
        },
        "operating_point": {
            "S": v1._s(op["S"]),
            "ell_over_rsat": v1.ELL_OVER_RSAT_LADDER[0],
            "p_RHO_A": v1.P_BRANCHES["RHO-A"],
            "om_over_omC": v1.OM_OVER_OMC_GRID[1],
            "Z_1": v1._s(op["Z1"]),
            "om": v1._s(op["om"]),
            "k_cold": v1._s(op["k_cold"]),
            "k0_crossover_om_Z1": v1._s(op["k0_cross"]),
            "eps_crossover_in_v1_parametrization": v1._s(op["k0_cross"] / op["k_cold"]),
        },
        "gates": {"G-RHO2": gate},
        "self_tests": {"FT-RHO2": ft},
        "diagnostics": {"D-RHO2-PRED": diag},
        "negative_controls": controls,
        "v1_reproduced_pass_flags": nc["_v1_gate_pass_flags"],
        "v1_reproduced_fire_flags": nc["_v1_self_test_fire_flags"],
        "certification": {
            "task2": "ROW-CERTIFIED" if task2_ok else "ROW-NOT-CERTIFIED",
            "task1": "SCAN-NOT-CERTIFIED (unchanged; not touched by this lane)",
            "task3": "CERTIFIED (unchanged; not touched by this lane)",
        },
    }
    digest_src = json.dumps(out, sort_keys=True, ensure_ascii=False)
    out["_digest"] = hashlib.sha256(digest_src.encode("utf-8")).hexdigest()[:16]
    out["_runtime_sec"] = round(time.time() - t0, 2)

    dst = HERE / "last_bond_g_rho2_rerun_results.json"
    dst.write_text(json.dumps(out, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"[g-rho2-v2] digest={out['_digest']}")
    print(f"[g-rho2-v2] crossover k_0 = om*Z_1 = {out['operating_point']['k0_crossover_om_Z1']}")
    print(f"[g-rho2-v2] G-RHO2   exponent={gate['measured_exponent']}  "
          f"{'PASS' if gate['pass'] else 'FAIL'}")
    print(f"[g-rho2-v2] FT-RHO2  exponent={ft['measured_exponent']}  "
          f"{'FIRES' if ft['fires'] else 'DOES NOT FIRE'}")
    print(f"[g-rho2-v2] D-RHO2-PRED dev={diag['measured_deviation_from_2']}  "
          f"{'AGREES' if diag['agrees'] else 'DISAGREES'}")
    for k, v in controls.items():
        print(f"[g-rho2-v2] {k:16s} {'PASS' if v['pass'] else 'FAIL'}")
    print(f"[g-rho2-v2] TASK 2: {out['certification']['task2']}")


if __name__ == "__main__":
    main()
