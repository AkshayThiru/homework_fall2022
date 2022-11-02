import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    params = {"horizon" : [5, 15, 30], "numseq" : [100, 1000], "ensemble" : [1, 3, 5],}
    for key in params.keys():
        logs = dict()
        for param in params[key]:
            logs[key + str(param)] = "data/hw4_q4_reacher_" + key + str(param) + "_batch1000_reacher-cs285-v0_*?/events*"
        results = get_section_results(logs)

        fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=False, dpi=150)
        colors = iter(cm.rainbow(np.linspace(0, 1, len(params[key]))))

        for l in results.keys():
            xdata, ydata, _ = get_plot_data(results[l])
            c = next(colors)
            ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=l)
        ax.hlines(xmin=xdata[0], xmax=xdata[-1], y=-325, lw=1, ls="--", color="k")

        ax.legend(loc="lower right")
        plt.title(f"Eval_AverageReturn for reacher env with {key} param")
        ax.set_xticks(np.arange(0, xdata[-1]+1, step=2))
        plt.setp(ax, xlabel="Number of iterations")
        plt.setp(ax, ylabel="Eval average return")

        fig.tight_layout()
        plt.show()