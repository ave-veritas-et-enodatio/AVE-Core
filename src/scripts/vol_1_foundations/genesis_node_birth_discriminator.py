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
    # stepped=True → cardinality read AFTER genuine engine evolution (measured
    # path). stepped=False → config-read only (install-tautology; excluded from
    # the 'measured paths' count in the result doc). R3 repair (2026-07-12).
    stepped: bool = True


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
    # R1 repair (2026-07-12): the D2 battery is now all THREE landed seed modes
    # at a stated fidelity, not the single photon_lock/fast=True leg the driver
    # shipped with. Record the leg identity so the per-fidelity table is honest.
    seed_mode: str = "photon_lock"
    fast: bool = True


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


# The three landed fixed-N seed modes (loop_gap_seeds.SeedMode). The shipped
# driver banked ONLY photon_lock; R1 broadens the D2 battery to all three at a
# stated fidelity. bin (i) needs persistence PASS on ≥1 landed path.
LANDED_SEED_MODES: tuple[str, ...] = ("pair", "photon_lock", "graded_a0")


def d2_loop_gap_persistence(
    N: int = 10,
    *,
    seed_mode: str = "photon_lock",
    bulk_density_on: bool = True,
    fast: bool = True,
) -> D2Report:
    """D2: P11-style drive-off persistence on fixed-N harness (FIREABLE).

    One battery leg. ``seed_mode`` ∈ ``LANDED_SEED_MODES``; ``fast=True`` is the
    banked SMOKE fidelity, ``fast=False`` is production. Config (banked, frozen
    off #654 §Gates 2): N, rank 4, bulk_density_on, front_target=A_YIELD,
    n_drive_mult=0.5, n_quiet_mult=1.5.
    """
    r = run_loop_gap_probe(
        f"d2_persistence_{seed_mode}",
        N=N,
        rank_target=4,
        seed_mode=seed_mode,
        bulk_density_on=bulk_density_on,
        front_target=A_YIELD if bulk_density_on else None,
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=fast,
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
        seed_mode=seed_mode,
        fast=fast,
    )


def d2_battery(
    N: int = 10,
    *,
    fast: bool = True,
    bulk_density_on: bool = True,
) -> list[D2Report]:
    """R1: full D2 battery — ALL THREE landed seed modes at one fidelity."""
    return [
        d2_loop_gap_persistence(
            N=N, seed_mode=m, bulk_density_on=bulk_density_on, fast=fast
        )
        for m in LANDED_SEED_MODES
    ]


def d2_battery_persists(reports: list[D2Report]) -> bool:
    """bin (i) D2 criterion: persistence PASS on ≥1 landed fixed-N path."""
    return any(r.persistence_pass for r in reports)


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


D1_VIOLATION_HALT = "D1_CARDINALITY_VIOLATION_HALT"


def adjudicate_bin(
    *,
    d1_ok: bool,
    d2_persist: bool,
    d3_not_entailed: bool,
    d4_ran: bool = False,
    d4_absurd: bool = False,
) -> str:
    """Frozen bins (i)–(v) from the prereg + one OUT-OF-BIN halt (R2).

    R2 gate-structure repair (2026-07-12): a cardinality mutation (``d1_ok=False``)
    is the fork-(B) signature — the single most consequential possible firing. The
    shipped adjudicator fell through to ``ii_A_WEAKENED`` for EVERY ``d1_ok=False``
    case, mislabelling a real N→N+1 event as an (A)-*weakening*. It is deliberately
    NOT in the frozen bin table: it HALTS for Grant adjudication rather than being
    mis-binned. This check is FIRST — a cardinality violation dominates D2/D3.
    """
    if not d1_ok:
        return D1_VIOLATION_HALT
    if not d3_not_entailed:
        return "iii_B_NECESSITY_CLAIM_FAILS"
    if d4_ran and d4_absurd:
        return "iv_B_COSMOLOGY_ABSURD"
    if d1_ok and d2_persist and d3_not_entailed:
        return "i_A_SUPPORTED"
    if d1_ok and (not d2_persist) and d3_not_entailed:
        return "ii_A_WEAKENED"
    return "ii_A_WEAKENED"


def run_suite(
    *, include_d2: bool = True, N_harness: int = 10, fast: bool = True
) -> dict[str, Any]:
    """Run D1 (2 measured + 1 structural) + D3; optionally the D2 battery.

    R1: when ``include_d2`` is set, run the FULL battery (all three landed seed
    modes at ``fast`` fidelity) and adjudicate per-fidelity — bin (i) needs
    persistence PASS on ≥1 landed path. R3: the harness D1 leg is config-read
    only (``stepped=False``) — structural, excluded from the measured count.
    """
    d1_reports = [
        d1_crystal_engine(),  # measured: 40 real steps, shape read after
        d1_master_equation(),  # measured: 40 real steps, shape read after
    ]
    # R3: harness D1 is a config-read only (no step) — an install-tautology on a
    # fixed mesh. Kept in the report as STRUCTURAL (stepped=False) so run_suite
    # stays a fast keeper (stepping rank-4 here would make it engine_sim), but
    # excluded from the 'measured paths' count in the result doc.
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
        stepped=False,
    )
    d1_reports.append(d1_harness)

    d3 = d3_necessity_corpus()
    d2: list[D2Report] | None = None
    if include_d2:
        d2 = d2_battery(N=N_harness, fast=fast)

    d1_ok = all(r.invariant for r in d1_reports)
    d2_persist = d2_battery_persists(d2) if d2 is not None else False
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
        "fidelity": ("smoke" if fast else "production") if include_d2 else "n/a",
        "d1": [asdict(r) for r in d1_reports],
        "d1_measured_paths": sum(1 for r in d1_reports if r.stepped),
        "d1_structural_paths": sum(1 for r in d1_reports if not r.stepped),
        "d2": [asdict(r) for r in d2] if d2 is not None else None,
        "d2_any_persist": d2_persist if include_d2 else None,
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
    import argparse
    import json

    ap = argparse.ArgumentParser(description="Genesis node-birth D1–D4 discriminator suite.")
    ap.add_argument("--no-d2", action="store_true", help="D1+D3 only (fast); skip the D2 battery")
    ap.add_argument(
        "--production",
        action="store_true",
        help="run the D2 battery at production fidelity (fast=False; ~5–15 min/leg)",
    )
    ap.add_argument("--N", type=int, default=10, help="harness N (default 10, banked config)")
    args = ap.parse_args()

    out = run_suite(
        include_d2=not args.no_d2,
        N_harness=args.N,
        fast=not args.production,
    )
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
