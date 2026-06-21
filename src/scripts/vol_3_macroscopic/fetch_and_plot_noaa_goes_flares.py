"""
AVE Solar Weather Comparison — ILLUSTRATIVE (synthesized timeline, NOT a NOAA fetch).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
Despite the script name "fetch_and_plot_noaa_goes_flares", this script does
NOT live-fetch NOAA GOES satellite data. As acknowledged at lines 24-27, the
"empirical layout" is SYNTHESIZED from known historical Solar Cycle 23/24/25
maximum dates with empirical flare clustering — NOT pulled from the actual
NOAA GOES X-ray flux JSON catalog.

The plotted "flare data" is a Monte-Carlo placeholder for what the actual
fetch should produce. The AVE Solar Diode model's I-V FWHM = 0.46 Years
prediction overlay IS the AVE-distinct claim; quantitative falsification
against real NOAA data requires the live-fetch path (currently bypassed).

Recommended cleanup (queued): implement live NOAA GOES SWPC fetch via
their public JSON endpoint or NOAA Data Service API and replace the
synthesized timeline. Until then, this script is ILLUSTRATIVE — it does
not constitute empirical validation despite the name.

Title softened 2026-05-17: was "AVE Empirical Validation: NOAA GOES
Satellite vs. Topological Solar Weather" — corrected to clarify the fetch
is synthesized, not real.

FIGURE-STYLE (2026-06-21, Vol-3 Phase-3b regen): restyled through
``ave.viz.style`` (house print profile, Okabe-Ito palette, legend off the
data, no baked raster title). Currency fix (LF-03): the prior raster title /
scatter label claimed "Empirical Validation: NOAA GOES Satellite Telemetry"
and labelled the synthesized Monte-Carlo scatter as live "Empirical NOAA
GOES" telemetry. That is FALSE — the timeline is synthesized and the AVE
0.46-yr FWHM is a forward prediction awaiting a live NOAA GOES fetch. The
baked title is removed (caption belongs in the LaTeX \\caption{}); the
synthesized series is now labelled as illustrative/synthesized, not as
empirical telemetry. No physics/data values changed.
"""

import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style
from ave_path_util import sim_output

style.apply("print")


def simulate_empirical_noaa_overlay() -> None:
    print("[*] Generating ILLUSTRATIVE (synthesized) Solar-cycle vs AVE Topological Diode overlay...")

    # We simulate the empirical layout since live-fetching the entire 40-year
    # NOAA GOES JSON catalog can be flaky without an API key or stable endpoint.
    # We use known historical Solar Maximum dates and empirical flare clustering
    # to demonstrate the overlay. THIS IS SYNTHESIZED, NOT A NOAA FETCH.

    # Solar Cycles (Approximate Maxima dates)
    # Cycle 23 Max: 2001.3
    # Cycle 24 Max: 2014.3
    # Cycle 25 Max: ~2024.5 (Current)

    years = np.linspace(1995, 2026, 2000)

    # Simulate the 11-Year AC Dynamo Voltage for the past 30 years
    # 11-year period, aligned to peak roughly at the known Maxima
    dynamo_voltage = 50.0 + 49.5 * np.cos((2 * np.pi * (years - 2001.3)) / 11.0)

    # AVE Theoretical: Macroscopic Avalanche Equation (from previous script)
    V_BD = 100.0
    I_S = 1e-3
    V_T = 15.0
    AVALANCHE_N = 1.8

    v_ratio = np.clip(dynamo_voltage / V_BD, 0, 0.999)
    m_factor = 1.0 / (1.0 - (v_ratio) ** AVALANCHE_N)
    theoretical_emission = I_S * (np.exp(dynamo_voltage / V_T) - 1.0) * m_factor

    # Find Theoretical FWHM bounds for plotting
    np.max(theoretical_emission)
    # half_max = max_emission / 2.0  # bulk lint fixup pass

    # Generate Synthesized Scatter (placeholder for GOES X and M class flares)
    # Flares in reality strictly cluster around the high-voltage peaks
    np.random.seed(42)  # For reproducible synthesized scatter

    empirical_years = []
    empirical_intensities = []

    for _ in range(300):  # 300 major flares over 30 years
        # Rejection sampling: events are 100x more likely when voltage is high
        rand_yr = np.random.uniform(1995, 2026)
        v_at_yr = 50.0 + 49.5 * np.cos((2 * np.pi * (rand_yr - 2001.3)) / 11.0)

        # Synthesized probability of a flare is tightly coupled to the avalanche curve
        v_ratio_rand = np.clip(v_at_yr / V_BD, 0, 0.99)
        m_rand = 1.0 / (1.0 - (v_ratio_rand) ** AVALANCHE_N)
        prob = (np.exp(v_at_yr / V_T) * m_rand) / (np.exp(100.0 / V_T) * 100)  # normalized

        if np.random.random() < prob * 5:  # Amplify to get enough scatter dots
            empirical_years.append(rand_yr)
            # Intensity randomly assigned based on class regimes
            intensity = np.random.uniform(5.0, 100.0)  # M and X class
            empirical_intensities.append(intensity)

    # Rendering — house style (white print profile, Okabe-Ito palette)
    fig, ax = plt.subplots(figsize=style.figsize("wide"))

    # Plot Theoretical Avalanche Envelope (the AVE-distinct claim)
    ax.plot(
        years,
        theoretical_emission,
        color=style.COLORS["ave"],
        linestyle="-",
        lw=2,
        label="AVE topological diode: avalanche emission envelope",
    )

    # Plot Dynamo Base Voltage (Scaled visually)
    ax.plot(
        years,
        dynamo_voltage,
        color=style.COLORS["accent"],
        linestyle="-.",
        lw=1.5,
        label="AC topological dynamo (magnetic winding)",
    )

    # Plot synthesized (illustrative) flare scatter — NOT live NOAA telemetry
    ax.scatter(
        empirical_years,
        empirical_intensities,
        color=style.COLORS["data"],
        marker="x",
        alpha=0.8,
        s=40,
        label="Synthesized flare scatter (illustrative placeholder, not NOAA fetch)",
    )

    # Annotate FWHM Zones — A-034 forward prediction (0.46-yr FWHM), validation pending
    # Cycle 23
    ax.axvspan(
        2001.3 - 0.23,
        2001.3 + 0.23,
        color=style.COLORS["comparison"],
        alpha=0.2,
        label="AVE A-034 forward prediction: 0.46-yr avalanche FWHM (pending NOAA fetch)",
    )
    # Cycle 24
    ax.axvspan(2001.3 + 11.0 - 0.23, 2001.3 + 11.0 + 0.23, color=style.COLORS["comparison"], alpha=0.2)
    # Cycle 25
    ax.axvspan(2001.3 + 22.0 - 0.23, 2001.3 + 22.0 + 0.23, color=style.COLORS["comparison"], alpha=0.2)

    ax.set_yscale("log")
    ax.set_ylim([1, 1e4])
    ax.set_xlim([1995, 2026])

    # No baked title — caption belongs in the LaTeX \caption{}.
    ax.set_xlabel(style.axis_label("Time", "t", "yr"))
    ax.set_ylabel(style.axis_label("Emission intensity / dynamo voltage", "", "arb. units"))
    style.legend(ax, where="below", ncol=1)

    output_path = sim_output("noaa_goes_empirical_validation.png")
    style.save(fig, output_path)
    print(f"[*] Saved ILLUSTRATIVE synthesized solar-cycle overlay (NOT NOAA telemetry): {output_path}")
    plt.close(fig)


if __name__ == "__main__":
    simulate_empirical_noaa_overlay()
