import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

script_dir = Path(__file__).resolve().parent
output_path = script_dir / ".." / "fig" / "gh.pdf"

# =========================
# matplotlib の設定
# =========================
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "cm",
    "mathtext.fontset": "cm",
    "font.size": 14,
    "axes.grid": False,
    "grid.linestyle": "--",
    "xtick.direction": "in",
    "ytick.direction": "in",
    "axes.linewidth": 1.2,
    "legend.frameon": False,
})
# =========================
# Gaisser--Hillas 関数の例
# =========================
# 具体例としてのパラメータ
N_max = 1.0e6          # 最大粒子数
X_max = 700.0          # [g/cm^2]
X0 = -50.0             # [g/cm^2]
Lambda = 70.0          # [g/cm^2]

# 指数
alpha = (X_max - X0) / Lambda

# 描画範囲
X = np.linspace(X0 + 1.0, 1500.0, 2000)

# 各項
R = ((X - X0) / (X_max - X0)) ** alpha
D = np.exp((X_max - X) / Lambda)

# Gaisser--Hillas 関数
N = N_max * R * D

# 重ね描きしやすいように R, D を N_max でスケーリング
R_scaled = N_max * R
D_scaled = N_max * D

# =========================
# プロット
# =========================
fig, ax = plt.subplots(figsize=(7.2, 4.8))

ax.plot(X, N, label=r"$N(X)$", linewidth=2.0, color='k')
ax.plot(X, R_scaled, linestyle=":", linewidth=1.0,
        label=r"$N_{\max} R(X)$")
ax.plot(X, D_scaled, linestyle="-.", linewidth=1.0,
        label=r"$N_{\max} D(X)$")

# 極大位置の目安
ax.axvline(X_max, linestyle="--", linewidth=1.0,
           label=rf"$X_{{\max}}={X_max:.0f}\,\mathrm{{g/cm^2}}$", c='k')

ax.set_xlabel(r"$X\ [\mathrm{g/cm^2}]$")
ax.set_ylabel(r"$N(X)$")
ax.set_title("Example of the Gaisser--Hillas function")

ax.set_ylim(0, N_max*1.5)
# ax.set_yscale('log')

ax.legend()
plt.tight_layout()
plt.savefig(output_path)