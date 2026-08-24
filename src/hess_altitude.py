from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "fig" / "hess-altitude.pdf"

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 10.5,
        "axes.linewidth": 0.9,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "legend.frameon": False,
    }
)

# Mean values in Hess's altitude bins. Horizontal errors show the bin widths.
lower = np.array([0, 0, 200, 500, 1000, 2000, 3000, 4000], dtype=float)
upper = np.array([0, 200, 500, 1000, 2000, 3000, 4000, 5200], dtype=float)
altitude = (lower + upper) / 2
altitude[0] = 0
xerr = np.vstack((altitude - lower, upper - altitude))
q1 = np.array([16.3, 15.4, 15.5, 15.6, 15.9, 17.3, 19.8, 34.4])
q2 = np.array([11.8, 11.1, 10.4, 10.3, 12.1, 13.3, 16.5, 27.2])

fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.errorbar(
    altitude,
    q1,
    xerr=xerr,
    fmt="o-",
    color="#173f5f",
    linewidth=1.5,
    markersize=4.5,
    capsize=2.5,
    label="Instrument 1",
)
ax.errorbar(
    altitude,
    q2,
    xerr=xerr,
    fmt="s-",
    color="#b5522e",
    linewidth=1.5,
    markersize=4.2,
    capsize=2.5,
    label="Instrument 2",
)
ax.axhline(q1[0], color="#173f5f", linewidth=0.8, linestyle=":", alpha=0.65)
ax.axhline(q2[0], color="#b5522e", linewidth=0.8, linestyle=":", alpha=0.65)
ax.set_xlim(-150, 5400)
ax.set_ylim(7, 38)
ax.set_xlabel("Altitude [m]")
ax.set_ylabel(r"Ionization rate [ions cm$^{-3}$ s$^{-1}$]")
ax.grid(axis="y", color="0.88", linewidth=0.6)
ax.legend(loc="upper left")
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"CreationDate": None, "ModDate": None})
