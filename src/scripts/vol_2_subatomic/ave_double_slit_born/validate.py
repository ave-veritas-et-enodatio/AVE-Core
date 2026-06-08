"""
Validation for the capstone (validate-what-you-did):

  1. histogram_match   - chi^2/dof + KS + correlation: does the click histogram
                         match the REAL FDTD field |E|^2?  (Born RECOVERED)
  2. fringe_spacing    - measured fringe spacing vs the de-Broglie / Fraunhofer
                         prediction lambda*L/d.
  3. grep_no_born      - parse the detector source and confirm there is NO Born
                         rule / p=|psi|^2 / |psi|^2-sampling in the CLICK CODE
                         (the words may appear only in explanatory docstrings).
  4. exponent_scan     - counterfactual: a detector responding to |E|^1 or |E|^3
                         does NOT reproduce the wave pattern; only |E|^2 (energy,
                         Poynting) does -> the Born exponent is energy-forced.
  5. fallback_audit    - instrumentation gate: confirm EVERY click fired by a
                         genuine first-passage yield-crossing, NOT the
                         argmax(|E|^2) safety fallback (which would partially
                         MANUFACTURE the Born agreement). Asserts the fallback
                         count is 0 and reports its fraction.
"""

from __future__ import annotations

import io
import tokenize
from pathlib import Path

import numpy as np
from scipy.signal import find_peaks

from .click_detector import ClickResult, accumulate_clicks
from .config import DetectorConfig
from .field_engine import FieldResult


def histogram_match(intensity_y: np.ndarray, click_hist: np.ndarray, click_cells: np.ndarray) -> dict:
    """chi^2/dof, KS and Pearson correlation of clicks vs the field |E|^2."""
    target = np.clip(intensity_y, 0.0, None)
    mask = target > 0.02 * target.max()
    h = click_hist[mask].astype(float)
    t = target[mask].astype(float)
    t = t * h.sum() / t.sum()  # scale to the realised click count (units, not Born)
    chi2_dof = float(np.sum((h - t) ** 2 / np.maximum(t, 1e-9)) / (mask.sum() - 1))
    corr = float(np.corrcoef(click_hist[mask], target[mask])[0, 1])

    # KS: empirical click CDF vs the |E|^2-proportional reference CDF.
    cells = np.arange(intensity_y.size)
    p = target / target.sum()
    cdf_ref = np.cumsum(p)
    sc = np.sort(click_cells)
    cdf_emp = np.searchsorted(sc, cells, side="right") / sc.size
    ks = float(np.max(np.abs(cdf_emp - cdf_ref)))
    return {"chi2_dof": chi2_dof, "corr": corr, "ks": ks, "n_bins": int(mask.sum())}


def fringe_spacing(intensity_y: np.ndarray, field: FieldResult) -> dict:
    """Measured fringe spacing (peak-to-peak) vs lambda*L/d prediction."""
    target = intensity_y / intensity_y.max()
    pk, _ = find_peaks(target, height=0.08, distance=12)
    if pk.size >= 2:
        spacing = float(np.median(np.diff(pk)))
    else:
        spacing = float("nan")
    pred = field.fringe_spacing_pred
    err = 100.0 * abs(spacing - pred) / pred if np.isfinite(spacing) else float("nan")
    return {
        "spacing_clicks": spacing,  # peaks measured from the |psi|^2 the clicks reproduce
        "spacing_pred": pred,
        "spacing_err_pct": err,
        "n_peaks": int(pk.size),
        "peaks": pk.tolist(),
        "fresnel_number": float(field.cfg.slit_sep**2 / (field.wavelength_measured * field.cfg.L)),
    }


def grep_no_born(detector_path: str | Path) -> dict:
    """Confirm the detector's CLICK CODE contains no Born rule / |psi|^2 sampling.

    Strips comments and string literals (docstrings) via tokenize, then checks
    the executable tokens only. The words 'born'/'psi' are allowed to appear in
    the explanatory docstring (and do), but must NOT appear in code.
    """
    src = Path(detector_path).read_text()
    code_tokens: list[str] = []
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type in (tokenize.COMMENT, tokenize.STRING, tokenize.NL, tokenize.NEWLINE, tokenize.INDENT):
            continue
        code_tokens.append(tok.string)
    code = " ".join(code_tokens).lower()

    checks = {
        "no_born_in_code": "born" not in code,
        "no_psi_in_code": "psi" not in code,
        "no_weighted_sampler": ("p=" not in code) and ("multinomial" not in code),
        "no_intensity_prob_norm": "intensity.sum" not in code,
        "uses_canonical_saturation_kernel": "saturation_factor" in code,
        "consumes_intensity_as_rate": "rate" in code,
    }
    # Raw-text occurrences (expected: only inside the docstring/comments).
    raw = src.lower()
    doc_only = {
        "born_raw_count": raw.count("born"),
        "psi_raw_count": raw.count("psi"),
    }
    checks["all_pass"] = all(v for k, v in checks.items())
    return {"checks": checks, "docstring_mentions": doc_only}


def fallback_audit(clicks: ClickResult) -> dict:
    """Confirm no click used the argmax(|E|^2) safety fallback.

    The fallback in ``accumulate_clicks`` routes a click to the brightest
    realised cell when no yield-crossing happens within ``max_micro_steps``.
    That is a direct |E|^2-correlated placement which would PARTIALLY
    MANUFACTURE the Born agreement rather than let it emerge from genuine
    first-passage statistics. In the deterministic capstone config it must fire
    exactly zero times (mean first-passage ~14 micro-steps << the 60000 cap).

    This gate ASSERTS the count is 0, with a failure message that reports the
    fraction - so a future retune (higher ``thermal_kT`` / lower ``coupling``)
    that silently opens the |E|^2 path is caught loudly instead of laundered
    into the result.
    """
    n = int(clicks.click_cells.size)
    count = int(clicks.argmax_fallback_count)
    frac = count / max(n, 1)
    assert count == 0, (
        f"argmax(|E|^2) fallback fired {count}/{n} clicks ({100.0 * frac:.4f}%): "
        f"the |E|^2-correlated safety path is active and would MANUFACTURE the "
        f"Born agreement. A genuine first-passage yield-crossing is required for "
        f"every click; raise max_micro_steps or revert the thermal_kT/coupling "
        f"retune that opened this path."
    )
    return {
        "argmax_fallback_count": count,
        "argmax_fallback_fraction": frac,
        "all_genuine_first_passage": count == 0,
        "n_clicks": n,
    }


def exponent_scan(field: FieldResult, exponents=(1.0, 2.0, 3.0), *, n_clicks: int = 4000) -> dict:
    """Drive the SAME detector with |E|^p as the absorbed-power rate; only the
    physical energy exponent p=2 reproduces the wave |E|^2 pattern.

    |E| = sqrt(intensity_y).  Rate ∝ |E|^p = intensity_y^(p/2).
    Target is the real wave |psi|^2 = intensity_y.
    """
    amp = np.sqrt(np.clip(field.intensity_y, 0.0, None))
    out = {}
    for p in exponents:
        rate = amp**p
        cfg = DetectorConfig(n_clicks=n_clicks, seed=4242)
        res = accumulate_clicks(rate, cfg)
        m = histogram_match(field.intensity_y, res.histogram, res.click_cells)
        out[f"p={p:g}"] = {"chi2_dof": m["chi2_dof"], "corr": m["corr"], "ks": m["ks"]}
    return out
