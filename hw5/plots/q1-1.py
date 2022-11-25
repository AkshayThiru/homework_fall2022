import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    ### Easy env
    logs = {
        "random" : "data/hw5_expl_q1_easy_random_PointmassEasy-v0_*?/events*",
        "rnd" : "data/hw5_expl_q1_easy_rnd_PointmassEasy-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = -25.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=False, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 2)))
    
    for key in logs.keys():
        xdata, ydata, _ = get_plot_data(results[key])
        xdata = xdata * int(1e3)
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=key)
    ax.hlines(xmin=xdata[0], xmax=xdata[-1], y=y_hline, lw=1, ls="--", color="k")

    ax.legend(loc="lower right")
    plt.title(f"Learning curves for PointmassEasy-v0")
    ax.set_xticks(np.arange(0, xdata[-1]+1e4, step=int(1e4)))
    ax.ticklabel_format(axis="x", style="sci", scilimits=(3, 3))
    plt.setp(ax, xlabel="Number of iterations")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Hard env
    logs = {
        "random" : "data/hw5_expl_q1_hard_random_PointmassHard-v0_*?/events*",
        "rnd" : "data/hw5_expl_q1_hard_rnd_PointmassHard-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = -30.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=False, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 2)))
    
    for key in logs.keys():
        xdata, ydata, _ = get_plot_data(results[key])
        xdata = xdata * int(1e3)
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=key)

    ax.legend(loc="lower right")
    plt.title(f"Learning curves for PointmassHard-v0")
    ax.set_xticks(np.arange(0, xdata[-1]+1e4, step=int(1e4)))
    ax.ticklabel_format(axis="x", style="sci", scilimits=(3, 3))
    plt.setp(ax, xlabel="Number of iterations")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()