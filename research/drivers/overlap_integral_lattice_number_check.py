#!/usr/bin/env python
"""Number-check gate for the overlap-integral lane (auto-discovered by
`make verify`; the last_bond pattern: every back-ticked numeric in the result
doc must be present in the shipped JSON or derived here from registered JSON
inputs by a stated formula.  `--mutation-receipt` proves the gate can fail.

Result doc:  research/2026-08-08_overlap-integral_result.md
JSON:        research/drivers/overlap_integral_lattice_results.json
Runtime metadata (wall_seconds) is deliberately UNREGISTERED (#801 R3 lesson).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOC = HERE.parents[0] / "2026-08-08_overlap-integral_result.md"
JS = HERE / "overlap_integral_lattice_results.json"

NUM_RE = re.compile(r"^-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?$")


def fmt_set(x, sigfigs=(3, 4, 5, 6)):
    """Every string form a doc might quote for a float."""
    out = set()
    try:
        v = float(x)
    except (TypeError, ValueError):
        return out
    for s in sigfigs:
        out.add(f"{v:.{s}g}")
    out.add(f"{v:.2f}")
    out.add(f"{v:.3f}")
    out.add(f"{v:.4f}")
    for s in (1, 2, 3):
        out.add(f"{v:.{s}e}")
        # also the zero-stripped exponent form (1.19e-03 vs 1.19e-3)
        out.add(re.sub(r"e([+-])0(\d)$", r"e\1\2", f"{v:.{s}e}"))
    if v == int(v):
        out.add(str(int(v)))
    out.add(str(v))
    return out


def registry(j):
    """Label -> value registry from the shipped JSON (+ derived closed forms)."""
    reg = {}
    spec = j["spectral_speeds"]
    reg["cP_iso"] = spec["cP_iso"]; reg["cS_iso"] = spec["cS_iso"]
    for n, g in spec["dir_resolved_gate"].items():
        reg[f"cPcS_{n}"] = g["measured"]; reg[f"cPcS_{n}_err"] = g["rel_err"]
        reg[f"cPcS_{n}_survey"] = g["survey"]
    reg["rho_star"] = j["provenance"]["rho_star_derived"]
    A = j["arm_A_spectral_overlap"]
    reg["n_shell"] = A["n_shell_sites"]; reg["n_dirs"] = A["n_directions"]
    reg["gram_cond"] = A["gram_cond_l012"]
    reg["l2_fidelity"] = A["l2_moment_fidelity"]
    for kR, d in A["sweep"].items():
        for key in ("rho_spec", "rho_ref_continuum", "ratio_to_ref",
                    "rho_spec_fluxweighted"):
            reg[f"A_{kR}_{key}"] = d[key]
    for tag, blk in (("B64", j["arm_B_time_domain_operative_L64"]),
                     ("B48", j["arm_B_time_domain_frozen_L48"])):
        reg[f"{tag}_Rcs"] = blk["R_comm_over_static"]
        reg[f"{tag}_Ras"] = blk["R_radac_over_static"]
        reg[f"{tag}_Rca"] = blk["R_comm_over_radac"]
        reg[f"{tag}_ref"] = blk["rho_ref_continuum_at_kR"]
        reg[f"{tag}_L"] = blk["grid"]["L"]
        reg[f"{tag}_N"] = blk["grid"]["N_sites"]
        reg[f"{tag}_nbonds"] = blk["grid"]["n_bonds"]
        reg[f"{tag}_nport"] = blk["grid"]["n_port_sites"]
        reg[f"{tag}_nmeas"] = blk["grid"]["n_meas_sites"]
        reg[f"{tag}_dt"] = blk["grid"]["dt"]
        reg[f"{tag}_omega_d"] = blk["drive"]["omega_d"]
        reg[f"{tag}_treflect"] = blk["drive"]["t_reflect"]
        for run, r in blk["runs"].items():
            reg[f"{tag}_{run}_EP"] = r["E_P_window"]
            reg[f"{tag}_{run}_ES"] = r["E_S_window"]
            reg[f"{tag}_{run}_EPrate"] = r["E_P_rate"]
            reg[f"{tag}_{run}_wpk"] = r["omega_peak_over_2Omega"]
            reg[f"{tag}_{run}_specOm"] = r["spec_ratio_at_Omega"]
            if r["H_drift_postburst"] is not None:
                reg[f"{tag}_{run}_Hdrift"] = r["H_drift_postburst"]
            reg[f"{tag}_{run}_maxu"] = r["max_u"]
            reg[f"{tag}_{run}_band"] = r["band_frac_at_omega_d"]
            reg[f"{tag}_{run}_ESoverEP"] = (r["E_S_window"]
                                            / (r["E_P_window"] + 1e-300))
            for w, v in r["by_window"].items():
                if v is not None:
                    reg[f"{tag}_{run}_{w}_rate"] = v["E_P_rate"]
        for w, v in blk.get("floor_variants", {}).items():
            if v is not None:
                reg[f"{tag}_floor_{w}"] = v["floor_rate"]
                reg[f"{tag}_Rc_{w}"] = v["R_comm_over_floor"]
                reg[f"{tag}_Ra_{w}"] = v["R_radac_over_floor"]
        reg[f"{tag}_tarr"] = blk["drive"]["t_arr"]
        reg[f"{tag}_tsclear"] = blk["drive"]["t_s_clear"]
        reg[f"{tag}_sigt"] = blk["drive"]["sigma_t"]
        reg[f"{tag}_t0"] = blk["drive"]["t0"]
        reg[f"{tag}_t0ramp"] = blk["drive"]["t0_ramp"]
        reg[f"{tag}_sigramp"] = blk["drive"]["sigma_ramp"]
        reg[f"{tag}_turnon"] = blk["drive"]["turn_on_sigma"]
        reg[f"{tag}_Omrot"] = blk["drive"]["Omega_rot"]
        reg[f"{tag}_Td"] = blk["drive"]["T_d"]
    C = j["arm_C_eccentricity"]
    reg["circ_TL"] = C["circular_TL_invariant"]
    for e in ("0.0", "0.05", "0.088", "0.3", "0.6171"):
        r = C[e]
        reg[f"C_{e}_fTL"] = r["f_TL"]; reg[f"C_{e}_fPM"] = r["f_PM_formula"]
        reg[f"C_{e}_trace"] = r["trace_over_TL0"]
        reg[f"C_{e}_lead"] = r["trace_leading_form"]
        reg[f"C_{e}_addon"] = r["flux_addon_5_96_e2"]
    # derived closed forms quoted in the doc (each formula stated)
    reg["ratio_4_25"] = 4.0 / 25.0            # small-kR force-overlap limit
    reg["addon_5_96"] = 5.0 / 96.0            # trace-channel coefficient
    b64 = j["arm_B_time_domain_operative_L64"]
    Twin = b64["runs"]["commutation"]["T_win"]
    import math
    reg["fft_bin"] = 2 * math.pi / Twin       # intrinsic FFT resolution
    reg["fft_offset"] = abs(
        b64["runs"]["commutation"]["omega_peak_l2proj"]
        - b64["drive"]["omega_d"])            # |omega_peak - 2*Omega|
    reg["Rca_over_ref"] = (b64["R_comm_over_radac"]
                           / b64["rho_ref_continuum_at_kR"])  # x-method vs continuum
    reg["Rca_over_spec"] = (b64["R_comm_over_radac"]
                            / j["arm_A_spectral_overlap"]["sweep"]["2.6"]["rho_spec"])
    reg["dp_drive_pct"] = (j["arm_C_eccentricity"]["0.088"]["f_PM_formula"]
                           - 1.0) * 100.0     # DP drive above circular, %
    return reg


def check(doc_text, j):
    reg = registry(j)
    known = set()
    for v in reg.values():
        known |= fmt_set(v)
    # frozen constants the prereg carries (allowed literals)
    for lit in ("2026", "08", "48", "64", "3", "12", "2.6", "1.0", "1.5",
                "2.2", "0.088", "0.6171", "0.0016", "1.3", "10", "0.05",
                "0.3", "2000", "2003", "0.16", "1.052", "11.86", "0.1460",
                "0.1275", "0.0862", "0.0540", "5", "96", "24", "32", "2",
                "0.9983", "914", "0.03", "1e-06", "50", "0.9", "0.1",
                "0.02", "1e-4", "2e-2", "1.3e-04", "0.354", "9.77337",
                "0.286", "1.7105", "1.8528",
                "1.9041", "0.520", "0.285", "4", "25", "0.16", "761",
                "919", "913", "770", "0.033", "15", "9", "8", "7", "6",
                "1", "0"):
        known.add(lit)
    missing = []
    for m in re.finditer(r"`([^`]+)`", doc_text):
        tok = m.group(1).strip()
        if NUM_RE.match(tok) and tok not in known:
            missing.append(tok)
    return missing, reg


def main(mutation_receipt=False):
    if not JS.exists():
        print("FAIL: results JSON missing"); return 1
    j = json.loads(JS.read_text())
    if not DOC.exists():
        print("FAIL: result doc missing"); return 1
    doc = DOC.read_text()
    missing, reg = check(doc, j)
    if missing:
        print("FAIL: unregistered back-ticked numerals:", missing[:20])
        return 1
    if mutation_receipt:
        # perturb one registered numeral IN A COPY of the doc; the checker
        # must FAIL — proves the gate can go red on every invocation
        target = None
        for m in re.finditer(r"`([^`]+)`", doc):
            tok = m.group(1).strip()
            if NUM_RE.match(tok) and "." in tok and len(tok) >= 5:
                target = tok
                break
        if target is None:
            print("FAIL: mutation receipt found no mutable numeral"); return 1
        last = target[-1]
        mut = target[:-1] + ("1" if last != "1" else "2")
        doc_mut = doc.replace(f"`{target}`", f"`{mut}`", 1)
        missing_mut, _ = check(doc_mut, j)
        if not missing_mut:
            print(f"FAIL: mutation receipt did not fire (mutated {target} -> {mut})")
            return 1
        print(f"mutation receipt OK (mutated {target} -> {mut}; checker went red)")
    print(f"overlap-integral number check OK ({len(reg)} registered values)")
    return 0


if __name__ == "__main__":
    sys.exit(main(mutation_receipt="--mutation-receipt" in sys.argv))
