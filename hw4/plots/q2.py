import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    log = "data/hw4_q2_obstacles_singleiteration_obstacles-cs285-v0_*?/events*"
    result = get_result(log)

    fig, ax = plt.subplots(figsize=(6, 3), sharex=False, sharey=False, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 2)))

    xdata, ydata, _ = get_plot_data(result)
    c = next(colors)
    ax.plot(xdata, ydata["Eval_AverageReturn"], marker="o", ls="-", lw=1.5, c=c, label="Eval_AverageReturn")
    c = next(colors)
    ax.plot(xdata, ydata["Train_AverageReturn"], marker="o", ls="-", lw=1.5, c=c, label="Train_AverageReturn")
    ax.hlines(xmin=-1, xmax=1, y=-160, lw=1, ls="--", color="k")
    ax.hlines(xmin=-1, xmax=1, y=-50, lw=1, ls="--", color="k")
    
    ax.legend(loc="lower right")
    ax.set_xticks([0])
    plt.setp(ax, xlabel="Number of iterations")
    plt.setp(ax, ylabel="Average return")

    fig.tight_layout()
    plt.show()