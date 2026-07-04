"""Carrier declaration — the lattice-identity vocabulary + the instrument-scope guard.

ENGINE-HARDENING ARC item 5 (`_orchestration/2026-07-04_engine-upgrade-program.md`
§5). The D1 ratification (2026-07-03, `_orchestration/2026-07-03_srs-migration-
policy.md`) made the CARRIER load-bearing: srs-z3 is the production carrier; the
historical diamond-z4 (`TETRA_OFFSETS`) net is a NON-CANONICAL INSTRUMENT
(statics-pathological — its `L_D` connects only same-parity nodes, an 8–16-dim
frozen nullspace). The policy set three standing rules; this module makes rule (3)
— "every future engine verdict declares its carrier" — MACHINE-ENFORCED at the
lattice-construction and diamond-stencil-consumption boundaries.

THE GUARD. A consumer of the diamond stencil must ACKNOWLEDGE it is using a
non-canonical instrument by passing an explicit `instrument_scope="…"` string that
names WHY the instrument is being used (a reason, not a rubber-stamp). Constructing
a diamond-carrier operator without that acknowledgment either RAISES (new
construction) or emits a DeprecationWarning (frozen-provenance drivers whose
byte-identical output backs a merged result — KEEP-BOTH; breaking them would
rewrite committed behavior). This makes an accidental diamond-carrier verdict (the
class the D1 ruling flags) impossible to ship silently.

α-CLEAN: no physical constant on this path (pure identity vocabulary + a guard).
"""

from __future__ import annotations

import warnings
from enum import Enum


class Carrier(str, Enum):
    """The lattice carrier a construction / operator / verdict speaks.

    Values are the D1-ratified vocabulary (capability-map §8b.0 / migration policy):

      SRS_Z3        the chiral Laves z=3 (10,3)-a srs net — the PRODUCTION carrier
                    (Axiom-1's object). Carries chirality; well-posed L_srs (nullspace
                    dim 1 = the physical DC mode).
      DIAMOND_Z4    the achiral bipartite-FCC TETRA_OFFSETS net — a NON-CANONICAL
                    INSTRUMENT (statics-pathological; two non-communicating
                    sublattices). Retained as a documented instrument (the α / Lorentz
                    chains were hosted here). Consuming its stencil REQUIRES an
                    instrument_scope acknowledgment.
      CARTESIAN_REF the 7-pt continuum FDTD reference / cross-check carrier
                    (CrystalEngine / MasterEquationFDTD). Not srs, not diamond.
      K_SPACE       the spectral / Bloch-eigensolve carrier (Debye spectrum, band
                    structure).
    """

    SRS_Z3 = "srs-z3"
    DIAMOND_Z4 = "diamond-z4-instrument"
    CARTESIAN_REF = "cartesian-reference"
    K_SPACE = "k-space"

    @property
    def is_instrument(self) -> bool:
        """True for a non-canonical instrument carrier that requires acknowledgment."""
        return self is Carrier.DIAMOND_Z4


def coerce_carrier(value: "Carrier | str") -> Carrier:
    """Accept a Carrier or its string value; raise on an unknown carrier."""
    if isinstance(value, Carrier):
        return value
    try:
        return Carrier(value)
    except ValueError as exc:
        allowed = ", ".join(repr(c.value) for c in Carrier)
        raise ValueError(f"unknown carrier {value!r}; declared vocabulary is: {allowed}") from exc


def require_instrument_scope(
    carrier: "Carrier | str",
    instrument_scope: str | None,
    *,
    site: str = "",
    frozen_provenance: bool = False,
) -> str:
    """Guard: a DIAMOND_Z4 (instrument) consumer must acknowledge with instrument_scope.

    Args:
        carrier           : the carrier being consumed.
        instrument_scope  : the caller's explicit acknowledgment string (a REASON the
                            non-canonical instrument is being used — e.g. "stage-2
                            native-cage merged-result reproduction"). Required non-empty
                            for a DIAMOND_Z4 consumer.
        site              : a human label for the call site (used in the message).
        frozen_provenance : True ⇒ this consumer backs a merged byte-identical result;
                            a missing acknowledgment emits a DeprecationWarning rather
                            than raising (KEEP-BOTH — do NOT break committed behavior).
                            False ⇒ a missing acknowledgment RAISES (new construction).

    Returns the acknowledged instrument_scope (or a "" for a non-instrument carrier,
    which needs no acknowledgment).
    """
    car = coerce_carrier(carrier)
    if not car.is_instrument:
        return instrument_scope or ""  # non-instrument carriers need no acknowledgment

    ok = bool(instrument_scope) and str(instrument_scope).strip() != ""
    if ok:
        return str(instrument_scope)

    where = f" at {site}" if site else ""
    msg = (
        f"diamond-z4 is a NON-CANONICAL INSTRUMENT (D1 ratification 2026-07-03){where}: "
        'consuming its stencil requires an explicit instrument_scope="…" acknowledgment '
        "naming WHY the non-canonical carrier is used (statics-pathological; the srs-z3 "
        "production carrier is the default for new work)."
    )
    if frozen_provenance:
        warnings.warn(msg + " [frozen-provenance: warned, not raised — KEEP-BOTH]", DeprecationWarning, stacklevel=3)
        return ""
    raise ValueError(msg)


__all__ = ["Carrier", "coerce_carrier", "require_instrument_scope"]
