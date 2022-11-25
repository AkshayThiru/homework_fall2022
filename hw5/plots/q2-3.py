import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    logs = {
        "dyn" : "data/hw5_expl_q2_dqn_PointmassMedium-v0_*?/events*",
        "cql_alpha0.02" : "data/hw5_expl_q2_alpha0.02_PointmassMedium-v0_*?/events*",
        "cql_alpha0.1" : "data/hw5_expl_q2_alpha0.1_PointmassMedium-v0_*?/events*",
        "cql_alpha0.5" : "data/hw5_expl_q2_alpha0.5_PointmassMedium-v0_*?/events*",
    }
    results = get_section_results(logs)

    ### Learning curves
    y_hline = -40.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 4)))
    
    for key in logs.keys():
        xdata, ydata, _ = get_plot_data(results[key])
        xdata = xdata * int(1e3)
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=key)
    
    ax.hlines(xmin=xdata[0], xmax=xdata[-1], y=y_hline, lw=1, ls="--", color="k")
    ax.legend(loc="lower right")
    ax.set_xticks(np.arange(0, xdata[-1]+1e4, step=int(1e4)))
    ax.ticklabel_format(axis="x", style="sci", scilimits=(3, 3))
    plt.setp(ax, xlabel="Number of iterations")
    plt.suptitle(f"Learning curves for PointmassMedium-v0")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()
