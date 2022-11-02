import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    logs = {
        "random" : "data/hw4_q5_cheetah_random_cheetah-cs285-v0_*?/events*",
        "cem_2" : "data/hw4_q5_cheetah_cem_2_cheetah-cs285-v0_*?/events*",
        "cem_4" : "data/hw4_q5_cheetah_cem_4_cheetah-cs285-v0_*?/events*",
    }
    results = get_section_results(logs)

    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=False, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 3)))

    for l in results.keys():
        xdata, ydata, _ = get_plot_data(results[l])
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=l)
    ax.hlines(xmin=xdata[0], xmax=xdata[-1], y=800, lw=1, ls="--", color="k")

    ax.legend(loc="lower right")
    ax.set_xticks(xdata)
    plt.title("Eval_AverageReturn for cheetah env (random shooting vs CEM)")
    plt.setp(ax, xlabel="Number of iterations")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()