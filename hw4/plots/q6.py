import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    logs = {
        "sac_baseline_rlen0" : "data/hw4_q6_cheetah_rlen0_cheetah-cs285-v0_*?/events*",
        "dyna_rlen1" : "data/hw4_q6_cheetah_rlen1_cheetah-cs285-v0_*?/events*",
        "mbpo_rlen10" : "data/hw4_q6_cheetah_rlen10_cheetah-cs285-v0_*?/events*",
    }
    results = get_section_results(logs)

    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=False, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 3)))

    for l in results.keys():
        xdata, ydata, _ = get_plot_data(results[l])
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=l)
    ax.hlines(xmin=xdata[0], xmax=xdata[-1], y=1000, lw=1, ls="--", color="k")

    ax.legend(loc="lower right")
    ax.set_xticks(xdata)
    ax.set_ylim([-1000, 1200])
    plt.title("Eval_AverageReturn for cheetah env (SAC, Dyna, MBPO)")
    plt.setp(ax, xlabel="Number of iterations")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()