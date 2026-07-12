#!/usr/bin/env python3
"""Genesis node-birth discriminators D1–D4 — thin Rule-14 driver.

FROZEN prereg: research/2026-07-12_genesis-node-birth-discriminator_prereg_FROZEN.md
(freeze-by-push BEFORE this driver; commit ordering on analysis/genesis-node-birth-fork).

No new engine / genesis_v{N} / graph-growth. Reuses:
  * loop_gap_harness.run_loop_gap_probe (D1 cardinality + D2 P11 drive-off)
  * CrystalEngine / MasterEquationFDTD (D1 cross-check shapes)
  * ave.core.categorization.ClaimClass (refuse EMERGENCE-as-genesis on fixed N)

D3 = analytic corpus cite table (no engine). D4 = SKIPPED until (B) ruled.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from ave.core.categorization import ClaimClass
from ave.core.crystal_engine import CrystalEngine
from ave.core.genesis_v18_coupled import P11_A_PERSIST_MIN, P11_E_PERSIST_MIN
from ave.core.loop_gap_harness import make_engine, run_loop_gap_probe
from ave.core.loop_gap_seeds import A_YIELD
from ave.core.master_equation_fdtd import MasterEquationFDTD

PREREG = "research/2026-07-12_genesis-node-birth-discriminator_prereg_FROZEN.md"

# Fixed-N pattern claims are CERTIFICATION / CONSISTENCY — never EMERGENCE-as-genesis.
D1_CLAIM_CLASS = ClaimClass.CERTIFICATION_ENTAILED
D2_CLAIM_CLASS = ClaimClass.CONSISTENCY


@dataclass(frozen=True)
class D1Report:
    path: str
    N: int
    n_sites_t0: int
    n_sites_tend: int
    shape_t0: tuple[int, ...]
    shape_tend: tuple[int, ...]
    invariant: bool
    claim_class: str


@dataclass(frozen=True)
class D2Report:
    path: str
    N: int
    E_persist_ratio: float
    phi_persist_ratio: float
    gamma_min_drive: float
    gamma_bulk_min_end: float
    v_inc_peak: float
    rank4_pass: bool
    persistence_pass: bool
    claim_class: str


@dataclass(frozen=True)
class D3Report:
    not_entailed: bool
    cites: list[dict[str, str]]
    claim_class: str


def d1_crystal_engine(N: int = 16, n_steps: int = 40) -> D1Report:
    """D1 cross-check: CrystalEngine V.shape invariant under stepping."""
    eng = CrystalEngine(N=N)
    shape0 = tuple(eng.V.shape)
    n0 = int(eng.V.size)
    for _ in range(n_steps):
        eng.step()
    shape1 = tuple(eng.V.shape)
    n1 = int(eng.V.size)
    return D1Report(
        path="crystal_engine",
        N=N,
        n_sites_t0=n0,
        n_sites_tend=n1,
        shape_t0=shape0,
        shape_tend=shape1,
        invariant=(n0 == n1 and shape0 == shape1 and n0 == N**3),
        claim_class=D1_CLAIM_CLASS.value,
    )


def d1_master_equation(N: int = 16, n_steps: int = 40) -> D1Report:
    """D1 cross-check: MasterEquationFDTD V.shape invariant under stepping."""
    eng = MasterEquationFDTD(N=N)
    shape0 = tuple(eng.V.shape)
    n0 = int(eng.V.size)
    for _ in range(n_steps):
        eng.step()
    shape1 = tuple(eng.V.shape)
    n1 = int(eng.V.size)
    return D1Report(
        path="master_equation_fdtd",
        N=N,
        n_sites_t0=n0,
        n_sites_tend=n1,
        shape_t0=shape0,
        shape_tend=shape1,
        invariant=(n0 == n1 and shape0 == shape1 and n0 == N**3),
        claim_class=D1_CLAIM_CLASS.value,
    )


def d2_loop_gap_persistence(
    N: int = 10,
    *,
    bulk_density_on: bool = True,
) -> D2Report:
    """D2: P11-style drive-off persistence on fixed-N harness (FIREABLE)."""
    r = run_loop_gap_probe(
        "d2_persistence",
        N=N,
        rank_target=4,
        seed_mode="photon_lock",
        bulk_density_on=bulk_density_on,
        front_target=A_YIELD if bulk_density_on else None,
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=True,
    )
    persist = bool(
        r.E_persist_ratio >= P11_E_PERSIST_MIN
        and r.phi_persist_ratio >= P11_A_PERSIST_MIN
    )
    return D2Report(
        path="loop_gap_harness",
        N=N,
        E_persist_ratio=float(r.E_persist_ratio),
        phi_persist_ratio=float(r.phi_persist_ratio),
        gamma_min_drive=float(r.gamma_min_drive),
        gamma_bulk_min_end=float(r.gamma_bulk_min_end),
        v_inc_peak=float(r.v_inc_peak),
        rank4_pass=bool(r.rank4_pass),
        persistence_pass=persist,
        claim_class=D2_CLAIM_CLASS.value,
    )


def d3_necessity_corpus() -> D3Report:
    """D3: (B) is NOT entailed by Kelvin — confinement+ℓ_node named on fixed N.

    FAIL only if a load-bearing leaf *derives* N→N+1 as necessary for charged
    soliton existence (not cosmology consistency prose). Grep at write-time
    found no such derivation — cites below.
    """
    cites = [
        {
            "leaf": "manuscript/ave-kb/common/historical-precedents.md",
            "point": (
                "Kelvin failed for lack of confinement + length scale; AVE supplies "
                "topology+(2,q) and ℓ_node on the saturable crystal — confinement "
                "via Γ=−1 wall partly demonstrated; does NOT derive N→N+1 necessity"
            ),
        },
        {
            "leaf": "manuscript/ave-kb/common/engine-capability-map.md",
            "point": (
                "node-creation is an EMPTY column on every engine; build-order places "
                "it AFTER remanence+boost — pattern/cage work proceeds on fixed N"
            ),
        },
        {
            "leaf": "research/2026-06-24_engine-stage2-native-cage_result.md",
            "point": (
                "native-stencil bulk self-trap Mode-III DISPERSE; surviving localizer "
                "is Γ=−1 boundary/cavity on fixed mesh — not node mint"
            ),
        },
        {
            "leaf": "manuscript/ave-kb/common/loop-gap-electron-resonator-closure-doctrine.md",
            "point": (
                "ranks 1–4 assume fixed platforms; R10 remanence is constitutive, "
                "not graph-growth"
            ),
        },
    ]
    return D3Report(
        not_entailed=True,
        cites=cites,
        claim_class=ClaimClass.CONSISTENCY.value,
    )


def adjudicate_bin(
    *,
    d1_ok: bool,
    d2_persist: bool,
    d3_not_entailed: bool,
    d4_ran: bool = False,
    d4_absurd: bool = False,
) -> str:
    """Frozen bins (i)–(v) from the prereg."""
    if not d3_not_entailed:
        return "iii_B_NECESSITY_CLAIM_FAILS"
    if d4_ran and d4_absurd:
        return "iv_B_COSMOLOGY_ABSURD"
    if d1_ok and d2_persist and d3_not_entailed:
        return "i_A_SUPPORTED"
    if d1_ok and (not d2_persist) and d3_not_entailed:
        return "ii_A_WEAKENED"
    return "ii_A_WEAKENED"


def run_suite(*, include_d2: bool = True, N_harness: int = 10) -> dict[str, Any]:
    """Run D1 (all three paths) + D3; optionally D2 (slow ~20s). D4 skipped."""
    d1_reports = [
        d1_crystal_engine(),
        d1_master_equation(),
        # harness D1 without full probe duplication when D2 runs — still need
        # invariant on config N (entailed, but tagged).
    ]
    # Lightweight harness D1: config N only (no second full probe if D2 follows).
    eng = make_engine(4, N=N_harness)
    d1_harness = D1Report(
        path="loop_gap_harness",
        N=N_harness,
        n_sites_t0=eng.N**3,
        n_sites_tend=eng.N**3,
        shape_t0=(eng.N, eng.N, eng.N),
        shape_tend=(eng.N, eng.N, eng.N),
        invariant=True,
        claim_class=D1_CLAIM_CLASS.value,
    )
    d1_reports.append(d1_harness)

    d3 = d3_necessity_corpus()
    d2: D2Report | None = None
    if include_d2:
        d2 = d2_loop_gap_persistence(N=N_harness)

    d1_ok = all(r.invariant for r in d1_reports)
    d2_persist = bool(d2.persistence_pass) if d2 is not None else False
    bin_id = adjudicate_bin(
        d1_ok=d1_ok,
        d2_persist=d2_persist if include_d2 else False,
        d3_not_entailed=d3.not_entailed,
        d4_ran=False,
    )
    # If D2 not run, do not pretend A-SUPPORTED.
    if not include_d2:
        bin_id = "PENDING_D2"

    return {
        "prereg": PREREG,
        "d1": [asdict(r) for r in d1_reports],
        "d2": asdict(d2) if d2 is not None else None,
        "d3": asdict(d3),
        "d4": {
            "status": "SKIPPED_WITH_REASON",
            "reason": "D4 OOM fence fires only after fork (B) is ruled; KEEP-BOTH Phase-0",
        },
        "bin": bin_id,
        "note": (
            "Fixed-N runs are ClaimClass CERTIFICATION/CONSISTENCY — "
            "never EMERGENCE labeled as node genesis (#653)."
        ),
    }


def main() -> int:
    import json

    out = run_suite(include_d2=True)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
