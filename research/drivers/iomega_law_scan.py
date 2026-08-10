#!/usr/bin/env python3
"""iomega_law_scan.py — the I_omega(A)-law lane's scan instrument (prereg section 3).

Frozen prereg: research/2026-08-06_iomega-law_prereg-FROZEN.md (commit aa62941f, pushed ALONE).

Scan surface: the tracked blobs of the pinned base commit SCAN_PIN — which contains no
artifact of this lane by construction (SVA row-9 self-reference rule). research/_archive/**
is INCLUDED (the classification rule handles it).

Two methods per pattern, engines named, no pattern uses \\b:
  METHOD A: git grep -P against the pinned tree (PCRE2 as shipped with the installed git)
  METHOD B: CPython re over the same blob set

Output: research/drivers/iomega_law_scan_results.json (canonical, sorted keys; digest
excludes the _runtime_sec field).
"""
from __future__ import annotations

import hashlib
import json
import platform
import re
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "iomega_law_scan_results.json"

SCAN_PIN = "d129e7ac35d50aaaccca3a635fe3cf3b2b40a271"

# --- The frozen battery (prereg section 3.1). P-NC3/P-NC4 must be byte-identical to the
# v1 approach-leak prereg section 5.1 rows (gate G-NC-P34, checked below by extraction).
PATTERNS: dict[str, dict] = {
    "P-NC3": {
        "regex": r"I_\\?omega\s*\(\s*A\s*\)|I_\{?\\?omega\}?\s*\(\s*A\s*\)",
        "scope": None,
        "purpose": "v1 P3 reproduced byte-identically - reproduction control",
    },
    "P-NC4": {
        "regex": r"(I_\\?omega|micro.?inertia)[^\n]{0,40}(S\^|/\s*S|S\(A\))",
        "scope": None,
        "purpose": "v1 P4 reproduced byte-identically - reproduction control",
    },
    "P-I3a": {
        "regex": r"I_ω\s*(→|->)",
        "scope": None,
        "purpose": "archive Unicode prescription-arrow form (I_omega -> I_omega*S)",
    },
    "P-I3b": {
        "regex": r"I_ω\s*[·*]\s*S",
        "scope": None,
        "purpose": "archive Unicode product form",
    },
    "P-I3c": {
        "regex": r"I_ω\s*\(\s*A",
        "scope": None,
        "purpose": "Unicode functional form - discourse-vs-law classifier feed",
    },
    "P-I4": {
        "regex": r"(per.?node|node.?level)[^\n]{0,60}(moment of inertia|gyration)",
        "scope": None,
        "purpose": "per-node rotor moment / gyration definition",
    },
    "P-I5": {
        "regex": r"(ell_\{?node\}?|l_\{?node\}?|ℓ_\{?node\}?)[^\n]{0,60}(S\(|saturat|grade)",
        "scope": None,
        "purpose": "ell_node graded by S/saturation (CH-G receipt)",
    },
    "P-I6": {
        "regex": r"(self\.I_omega|self\.rho)\s*[*/]\s*S|I_omega\s*\*\s*S",
        "scope": "src/ave/",
        "scope_ext": ".py",
        "purpose": "kinetic-side kernel in landed engine code",
    },
    "P-CAT": {
        "regex": r"(inerti|kinetic|mass densit)[^\n]{0,60}(S\(A\)|√\(1|\\sqrt\{1|kernel)",
        "scope": "manuscript/ave-kb/common/universal-saturation-kernel-catalog.md",
        "purpose": "inertial row in the A-034 catalog",
    },
}

# Fireability sentinels (prereg section 3.3). The present sentinel is chosen and named here,
# before first run: a string verified present in the pinned tree.
SENTINEL_ABSENT = "IOMEGA_SENTINEL_ABSENT_2026_08_06"
SENTINEL_PRESENT = "Topo-Relativistic Impedance Divergence"


def sh(*args: str) -> str:
    return subprocess.run(args, cwd=REPO, capture_output=True, text=True, check=False).stdout


def tracked_blobs() -> list[str]:
    out = sh("git", "ls-tree", "-r", "--name-only", SCAN_PIN)
    return sorted(p for p in out.splitlines() if p)


def blob_text(path: str) -> str | None:
    r = subprocess.run(
        ["git", "show", f"{SCAN_PIN}:{path}"], cwd=REPO, capture_output=True, check=False
    )
    if r.returncode != 0:
        return None
    try:
        return r.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return None  # binary or non-utf8: skipped, counted


def in_scope(path: str, spec: dict) -> bool:
    scope = spec.get("scope")
    if scope is None:
        return True
    if not path.startswith(scope) and path != scope:
        return False
    ext = spec.get("scope_ext")
    if ext and not path.endswith(ext):
        return False
    return True


def method_a(regex: str, spec: dict) -> list[list]:
    """git grep -P at the pinned tree. Hits as [path, line_no, line_text]."""
    args = ["git", "grep", "-n", "-P", regex, SCAN_PIN]
    scope = spec.get("scope")
    if scope is not None:
        args += ["--", scope]
    out = sh(*args)
    hits = []
    for line in out.splitlines():
        # format: <pin>:<path>:<lineno>:<content>
        try:
            _pin, rest = line.split(":", 1)
            path, lineno, content = rest.split(":", 2)
        except ValueError:
            continue
        if not in_scope(path, spec):
            continue
        hits.append([path, int(lineno), content])
    return sorted(hits, key=lambda h: (h[0], h[1]))


def method_b(regex: str, spec: dict, blobs: list[str], texts: dict[str, str | None]) -> list[list]:
    rx = re.compile(regex)
    hits = []
    for path in blobs:
        if not in_scope(path, spec):
            continue
        text = texts.get(path)
        if text is None:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if rx.search(line):
                hits.append([path, i, line])
    return sorted(hits, key=lambda h: (h[0], h[1]))


def keyset(hits: list[list]) -> list[list]:
    return sorted({(h[0], h[1]) for h in hits})


def extract_v1_battery() -> dict[str, str]:
    """G-NC-P34: extract the P3/P4 regex cells from the v1 prereg at lane HEAD and
    unescape the markdown table pipes."""
    v1 = (REPO / "research/2026-08-05_approach-leak_prereg-FROZEN.md").read_text(encoding="utf-8")
    rows = {}
    for line in v1.splitlines():
        m = re.match(r"\|\s*`(P[34])`\s*\|\s*`(.+?)`\s*\|", line)
        if m:
            rows[m.group(1)] = m.group(2).replace("\\|", "|")
    return rows


def main() -> int:
    t0 = time.time()
    blobs = tracked_blobs()
    texts = {p: blob_text(p) for p in blobs}
    n_binary_or_undecodable = sum(1 for v in texts.values() if v is None)

    git_version = sh("git", "--version").strip()

    results: dict = {
        "meta": {
            "scan_pin": SCAN_PIN,
            "tracked_blob_count": len(blobs),
            "binary_or_undecodable_skipped": n_binary_or_undecodable,
            "engine_method_a": f"git grep -P (PCRE2), {git_version}",
            "engine_method_b": f"CPython re, Python {platform.python_version()}",
            "sentinel_present_choice": SENTINEL_PRESENT,
            "sentinel_absent_choice": SENTINEL_ABSENT,
        },
        "patterns": {},
        "gates": {},
    }

    g_scan_all_agree = True
    for pid, spec in PATTERNS.items():
        ha = method_a(spec["regex"], spec)
        hb = method_b(spec["regex"], spec, blobs, texts)
        agree = keyset(ha) == keyset(hb)
        g_scan_all_agree &= agree
        union = sorted({(h[0], h[1], h[2]) for h in ha} | {(h[0], h[1], h[2]) for h in hb})
        results["patterns"][pid] = {
            "regex": spec["regex"],
            "purpose": spec["purpose"],
            "scope": spec.get("scope"),
            "method_a_hits": len(ha),
            "method_b_hits": len(hb),
            "methods_agree": agree,
            "hits_union": [[p, n, t] for (p, n, t) in union],
        }

    # G-NC-P34: byte-identity of the reproduced regexes against the v1 prereg rows.
    v1rows = extract_v1_battery()
    nc_p3 = v1rows.get("P3") == PATTERNS["P-NC3"]["regex"]
    nc_p4 = v1rows.get("P4") == PATTERNS["P-NC4"]["regex"]
    results["gates"]["G-NC-P34"] = {
        "v1_P3_extracted": v1rows.get("P3"),
        "v1_P4_extracted": v1rows.get("P4"),
        "P3_byte_identical": nc_p3,
        "P4_byte_identical": nc_p4,
        "pass": bool(nc_p3 and nc_p4),
    }

    # FT-SCAN (fireability): absent sentinel 0/0 on both methods; present sentinel
    # identical non-empty hit sets.
    abs_spec = {"scope": None}
    ha_abs = method_a(re.escape(SENTINEL_ABSENT), abs_spec)
    hb_abs = method_b(re.escape(SENTINEL_ABSENT), abs_spec, blobs, texts)
    ha_pres = method_a(re.escape(SENTINEL_PRESENT), abs_spec)
    hb_pres = method_b(re.escape(SENTINEL_PRESENT), abs_spec, blobs, texts)
    ft_abs = len(ha_abs) == 0 and len(hb_abs) == 0
    ft_pres = len(ha_pres) > 0 and keyset(ha_pres) == keyset(hb_pres)
    results["gates"]["FT-SCAN"] = {
        "absent_counts": [len(ha_abs), len(hb_abs)],
        "present_counts": [len(ha_pres), len(hb_pres)],
        "present_sets_identical": keyset(ha_pres) == keyset(hb_pres),
        "fires": bool(ft_abs and ft_pres),
    }

    results["gates"]["G-SCAN"] = {"all_patterns_agree": g_scan_all_agree, "pass": g_scan_all_agree}

    canonical = json.dumps(results, sort_keys=True, ensure_ascii=False, indent=1)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
    results["digest_excluding_runtime"] = digest
    results["_runtime_sec"] = round(time.time() - t0, 3)

    OUT.write_text(
        json.dumps(results, sort_keys=True, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    ok = results["gates"]["G-SCAN"]["pass"] and results["gates"]["G-NC-P34"]["pass"] and results["gates"]["FT-SCAN"]["fires"]
    print(f"[iomega_law_scan] blobs={len(blobs)} digest={digest} "
          f"G-SCAN={results['gates']['G-SCAN']['pass']} G-NC-P34={results['gates']['G-NC-P34']['pass']} "
          f"FT-SCAN={results['gates']['FT-SCAN']['fires']}")
    for pid in sorted(PATTERNS):
        p = results["patterns"][pid]
        print(f"  {pid}: A={p['method_a_hits']} B={p['method_b_hits']} agree={p['methods_agree']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
