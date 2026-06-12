"""Pytest collection policy for src/tests.

Default ``make test`` runs substrate keepers + harness wiring only.
LOOP GAP / srs genesis version drivers are opt-in via ``make test-genesis``.
"""

collect_ignore_glob = [
    "test_chiral_lattice_v*.py",
    "test_chiral_lattice_phase*.py",
    "test_chiral_lattice_vector_phase*.py",
    "test_genesis_*.py",
]
