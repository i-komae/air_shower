from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "fig" / "peters-cycle.pdf"

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

energy = np.logspace(14, 18.3, 900)
rigidity_cutoff = 3.0e15
gamma = 2.70
delta_gamma = 0.45
smoothness = 4.0
components = [
    ("p", 1, 1.00, "#173f5f"),
    ("He", 2, 0.62, "#287271"),
    ("CNO", 7, 0.31, "#7b8b3d"),
    ("Si", 14, 0.18, "#c17c27"),
    ("Fe", 26, 0.20, "#a23e48"),
]

fig, ax = plt.subplots(figsize=(6.7, 4.3))
total = np.zeros_like(energy)
for label, charge, abundance, color in components:
    cutoff = charge * rigidity_cutoff
    flux = abundance * energy ** (-gamma) * (
        1.0 + (energy / cutoff) ** smoothness
    ) ** (-delta_gamma / smoothness)
    total += flux
    ax.plot(energy, energy**gamma * flux, color=color, linewidth=1.2, label=label)

ax.plot(energy, energy**gamma * total, color="black", linewidth=2.2, label="All particle")
ax.axvline(rigidity_cutoff, color="0.35", linestyle="--", linewidth=0.9)
ax.axvline(26 * rigidity_cutoff, color="0.35", linestyle=":", linewidth=0.9)
ax.text(rigidity_cutoff * 0.92, 1.56, r"$R_c$", ha="right", va="center")
ax.text(26 * rigidity_cutoff * 1.08, 1.56, r"$26R_c$", ha="left", va="center")
ax.set_xscale("log")
ax.set_xlim(1.0e14, 2.0e18)
ax.set_ylim(0, 2.05)
ax.set_xlabel(r"Energy $E$ [eV]")
ax.set_ylabel(r"Arbitrary $E^{2.7}J(E)$")
ax.grid(which="major", axis="both", color="0.88", linewidth=0.6)
ax.legend(ncol=2, loc="upper right")
fig.tight_layout()
fig.savefig(OUTPUT, metadata={"CreationDate": None, "ModDate": None})
