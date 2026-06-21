"""Tests for the shared AVE house figure style (``ave.viz.style``).

Dogfoods the figure module on its own contract: ``apply`` sets the expected
rcParams (white print bg / dark screen bg), the semantic palette has every key,
``axis_label`` formats correctly including the dimensionless case, ``save``
writes the expected files and flags a baked title (ave-figure-discipline Axis 4),
and the figsize presets are sane.

Fast + offline: forces the Agg backend, no display, no network.
"""

import warnings

import matplotlib

matplotlib.use("Agg")  # headless before any pyplot import side effects

import matplotlib as mpl  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import pytest  # noqa: E402

from ave.viz import style  # noqa: E402


@pytest.fixture(autouse=True)
def _restore_rc():
    """Snapshot/restore global rcParams so profile flips don't leak across tests."""
    saved = mpl.rcParams.copy()
    try:
        yield
    finally:
        mpl.rcParams.update(saved)


# ---------------------------------------------------------------------------
# apply() — profiles set the expected rcParams
# ---------------------------------------------------------------------------
def test_apply_print_is_white_background():
    style.apply("print")
    assert mpl.rcParams["figure.facecolor"] in ("white", (1.0, 1.0, 1.0, 1.0))
    # text/axes black in print
    assert mpl.rcParams["text.color"] in ("black", (0.0, 0.0, 0.0, 1.0))
    # constrained_layout on (Axis 3: kills overlap)
    assert mpl.rcParams["figure.constrained_layout.use"] is True
    # legend frame off, grid on
    assert mpl.rcParams["legend.frameon"] is False
    assert mpl.rcParams["axes.grid"] is True


def test_apply_screen_is_dark_background():
    style.apply("screen")
    fc = mpl.rcParams["figure.facecolor"]
    # dark, not white
    assert fc not in ("white", (1.0, 1.0, 1.0, 1.0))
    assert mpl.rcParams["text.color"] in ("white", (1.0, 1.0, 1.0, 1.0))


def test_print_and_screen_differ_in_background():
    style.apply("print")
    print_fc = mpl.rcParams["figure.facecolor"]
    style.apply("screen")
    screen_fc = mpl.rcParams["figure.facecolor"]
    assert print_fc != screen_fc


def test_apply_sets_okabe_ito_color_cycle():
    style.apply("print")
    cycle = mpl.rcParams["axes.prop_cycle"].by_key()["color"]
    # AVE blue leads the cycle
    assert cycle[0].lower() == style.COLORS["ave"].lower()


def test_palette_shared_across_profiles():
    # COLORS is a module constant — same on both profiles.
    style.apply("print")
    print_palette = dict(style.COLORS)
    style.apply("screen")
    assert dict(style.COLORS) == print_palette


def test_apply_rejects_unknown_profile():
    with pytest.raises(ValueError):
        style.apply("rainbow")


# ---------------------------------------------------------------------------
# COLORS — semantic palette completeness
# ---------------------------------------------------------------------------
def test_colors_has_all_semantic_keys():
    for key in ("ave", "comparison", "data", "accent", "muted"):
        assert key in style.COLORS, f"missing semantic colour: {key}"
        assert style.COLORS[key].startswith("#"), f"{key} not a hex colour"


def test_colormaps_are_print_safe_names():
    # Perceptually-uniform sequential + colourblind-safe diverging; `hot` retired.
    assert style.CMAP_SEQ in ("magma", "viridis")
    assert style.CMAP_DIV == "RdBu_r"
    # And they actually resolve to real matplotlib colormaps.
    assert mpl.colormaps[style.CMAP_SEQ] is not None
    assert mpl.colormaps[style.CMAP_DIV] is not None


# ---------------------------------------------------------------------------
# axis_label — canonical "Quantity $symbol$ [unit]"
# ---------------------------------------------------------------------------
def test_axis_label_with_unit():
    assert style.axis_label("Frequency", "f", "Hz") == "Frequency $f$ [Hz]"


def test_axis_label_dimensionless():
    assert style.axis_label("Strain", r"\delta n", "") == r"Strain $\delta n$ [dimensionless]"
    # None unit also → dimensionless
    assert style.axis_label("Ratio", "R", None) == "Ratio $R$ [dimensionless]"


def test_axis_label_symbol_only():
    assert style.axis_label("", "f", "Hz") == "$f$ [Hz]"


def test_axis_label_strips_whitespace_unit():
    assert style.axis_label("Field", "E", "  V/m ") == "Field $E$ [V/m]"


# ---------------------------------------------------------------------------
# figsize — presets
# ---------------------------------------------------------------------------
def test_figsize_presets():
    for kind in ("single", "double", "wide", "square"):
        w, h = style.figsize(kind)
        assert w > 0 and h > 0


def test_figsize_rejects_unknown_kind():
    with pytest.raises(ValueError):
        style.figsize("gigantic")


# ---------------------------------------------------------------------------
# save — writes files, replaces suffix per-format, title discipline
# ---------------------------------------------------------------------------
def test_save_writes_pdf_and_png(tmp_path):
    style.apply("print")
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 4], color=style.COLORS["ave"])
    ax.set_xlabel(style.axis_label("Time", "t", "s"))
    out = tmp_path / "fig"
    written = style.save(fig, out)
    plt.close(fig)
    assert (tmp_path / "fig.pdf").exists()
    assert (tmp_path / "fig.png").exists()
    assert set(p.suffix for p in written) == {".pdf", ".png"}


def test_save_replaces_existing_suffix(tmp_path):
    # save(fig, "x.png") still emits BOTH x.pdf and x.png (suffix is replaced).
    style.apply("print")
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    style.save(fig, tmp_path / "x.png")
    plt.close(fig)
    assert (tmp_path / "x.pdf").exists()
    assert (tmp_path / "x.png").exists()


def test_save_warns_on_baked_axes_title(tmp_path):
    style.apply("print")
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.set_title("A baked title that should live in LaTeX caption")
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        style.save(fig, tmp_path / "titled")
    plt.close(fig)
    assert any("baked title" in str(w.message) for w in caught)


def test_save_strict_raises_on_baked_suptitle(tmp_path):
    style.apply("print")
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    fig.suptitle("A baked suptitle")
    with pytest.raises(AssertionError):
        style.save(fig, tmp_path / "titled", strict=True)
    plt.close(fig)


def test_save_clean_figure_no_warning(tmp_path):
    style.apply("print")
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    ax.set_xlabel(style.axis_label("Time", "t", "s"))
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        style.save(fig, tmp_path / "clean")
    plt.close(fig)
    assert not any("baked title" in str(w.message) for w in caught)


# ---------------------------------------------------------------------------
# Public API surface re-exported from the package
# ---------------------------------------------------------------------------
def test_package_reexports_api():
    import ave.viz as viz

    for name in ("apply", "COLORS", "CMAP_SEQ", "CMAP_DIV", "axis_label", "save", "figsize"):
        assert hasattr(viz, name), f"ave.viz missing {name}"
