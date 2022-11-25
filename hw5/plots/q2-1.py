import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    logs = {
        "dyn" : "data/hw5_expl_q2_dqn_PointmassMedium-v0_*?/events*",
        "cql" : "data/hw5_expl_q2_cql_PointmassMedium-v0_*?/events*",
        "cql_scale10" : "data/hw5_expl_q2_cql_shift1_scale10_PointmassMedium-v0_*?/events*",
        "cql_scale100" : "data/hw5_expl_q2_cql_shift1_scale100_PointmassMedium-v0_*?/events*",
    }
    results = get_section_results(logs)

    ### Learning curves
    y_hline = -40.0
    fig, ax = plt.subplots(1, 2, figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 4)))
    
    for i, key in enumerate(logs.keys()):
        xdata, ydata, _ = get_plot_data(results[key])
        xdata = xdata * int(1e3)
        c = next(colors)
        ax[int(i >= 2)].plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=key)
    
    for i in range(2):
        ax[i].hlines(xmin=xdata[0], xmax=xdata[-1], y=y_hline, lw=1, ls="--", color="k")
        ax[i].legend(loc="lower right")
        ax[i].set_xticks(np.arange(0, xdata[-1]+1e4, step=int(1e4)))
        ax[i].ticklabel_format(axis="x", style="sci", scilimits=(3, 3))
        plt.setp(ax[i], xlabel="Number of iterations")
    plt.suptitle(f"Learning curves for PointmassMedium-v0")
    plt.setp(ax[0], ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Q-values
    fig, ax = plt.subplots(1, 2, figsize=(10, 5), sharex=False, sharey=False, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 4)))
    
    for i, key in enumerate(logs.keys()):
        xdata, ydata, _ = get_plot_data(results[key])
        xdata = xdata * int(1e3)
        c = next(colors)
        if key == "cql_scale10":
            ydata["Exploitation_Data_q-values"] = ydata["Exploitation_Data_q-values"] / 10.0 - 1.0
        elif key == "cql_scale100":
            ydata["Exploitation_Data_q-values"] = ydata["Exploitation_Data_q-values"] / 100.0 - 1.0
        ax[int(i >= 2)].plot(xdata[3:], ydata["Exploitation_Data_q-values"], ls="-", lw=1.5, c=c, label=key)
    
    for i in range(2):
        ax[i].legend(loc="lower right")
        ax[i].set_xticks(np.arange(0, xdata[-1]+1e4, step=int(1e4)))
        ax[i].ticklabel_format(axis="x", style="sci", scilimits=(3, 3))
        plt.setp(ax[i], xlabel="Number of iterations")
    plt.suptitle(f"Exploitation Data Q-values for PointmassMedium-v0")
    plt.setp(ax[0], ylabel="Q-values")

    fig.tight_layout()
    plt.show()
