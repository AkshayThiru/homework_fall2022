import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    logs = {
        "obstacles" : "data/hw4_q3_obstacles_obstacles-cs285-v0_*?/events*",
        "reacher" : "data/hw4_q3_reacher_reacher-cs285-v0_*?/events*",
        "cheetah" : "data/hw4_q3_cheetah_cheetah-cs285-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = {"obstacles" : -20.0, "reacher" : -250.0, "cheetah" : 350.0}
    for key in logs.keys():
        fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=False, dpi=150)
        colors = iter(cm.rainbow(np.linspace(0, 1, 1)))

        xdata, ydata, _ = get_plot_data(results[key])
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=key)
        ax.hlines(xmin=xdata[0], xmax=xdata[-1], y=y_hline[key], lw=1, ls="--", color="k")

        ax.legend(loc="lower right")
        ax.set_xticks(np.arange(0, xdata[-1]+1, step=2))
        plt.setp(ax, xlabel="Number of iterations")
        plt.setp(ax, ylabel="Eval average return")

        fig.tight_layout()
        plt.show()