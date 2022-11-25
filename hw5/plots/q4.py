import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    ### Easy env - unsupervised
    logs = {
        "awac_lambda0.1" : "data/hw5_expl_q4_awac_easy_unsupervised_lam0.1_PointmassEasy-v0_*?/events*",
        "awac_lambda1" : "data/hw5_expl_q4_awac_easy_unsupervised_lam1_PointmassEasy-v0_*?/events*",
        "awac_lambda2" : "data/hw5_expl_q4_awac_easy_unsupervised_lam2_PointmassEasy-v0_*?/events*",
        "awac_lambda10" : "data/hw5_expl_q4_awac_easy_unsupervised_lam10_PointmassEasy-v0_*?/events*",
        "awac_lambda20" : "data/hw5_expl_q4_awac_easy_unsupervised_lam20_PointmassEasy-v0_*?/events*",
        "awac_lambda50" : "data/hw5_expl_q4_awac_easy_unsupervised_lam50_PointmassEasy-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = -30.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 6)))
    
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
    plt.suptitle(f"Learning curves for PointmassEasy-v0 (unsupervised)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Easy env - supervised
    logs = {
        "awac_lambda0.1" : "data/hw5_expl_q4_awac_easy_supervised_lam0.1_PointmassEasy-v0_*?/events*",
        "awac_lambda1" : "data/hw5_expl_q4_awac_easy_supervised_lam1_PointmassEasy-v0_*?/events*",
        "awac_lambda2" : "data/hw5_expl_q4_awac_easy_supervised_lam2_PointmassEasy-v0_*?/events*",
        "awac_lambda10" : "data/hw5_expl_q4_awac_easy_supervised_lam10_PointmassEasy-v0_*?/events*",
        "awac_lambda20" : "data/hw5_expl_q4_awac_easy_supervised_lam20_PointmassEasy-v0_*?/events*",
        "awac_lambda50" : "data/hw5_expl_q4_awac_easy_supervised_lam50_PointmassEasy-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = -30.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 6)))
    
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
    plt.suptitle(f"Learning curves for PointmassEasy-v0 (supervised)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Medium env - unsupervised
    logs = {
        "awac_lambda0.1" : "data/hw5_expl_q4_awac_medium_unsupervised_lam0.1_PointmassMedium-v0_*?/events*",
        "awac_lambda1" : "data/hw5_expl_q4_awac_medium_unsupervised_lam1_PointmassMedium-v0_*?/events*",
        "awac_lambda2" : "data/hw5_expl_q4_awac_medium_unsupervised_lam2_PointmassMedium-v0_*?/events*",
        "awac_lambda10" : "data/hw5_expl_q4_awac_medium_unsupervised_lam10_PointmassMedium-v0_*?/events*",
        "awac_lambda20" : "data/hw5_expl_q4_awac_medium_unsupervised_lam20_PointmassMedium-v0_*?/events*",
        "awac_lambda50" : "data/hw5_expl_q4_awac_medium_unsupervised_lam50_PointmassMedium-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = -60.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 6)))
    
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
    plt.suptitle(f"Learning curves for PointmassMedium-v0 (unsupervised)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Easy env - supervised
    logs = {
        "awac_lambda0.1" : "data/hw5_expl_q4_awac_medium_supervised_lam0.1_PointmassMedium-v0_*?/events*",
        "awac_lambda1" : "data/hw5_expl_q4_awac_medium_supervised_lam1_PointmassMedium-v0_*?/events*",
        "awac_lambda2" : "data/hw5_expl_q4_awac_medium_supervised_lam2_PointmassMedium-v0_*?/events*",
        "awac_lambda10" : "data/hw5_expl_q4_awac_medium_supervised_lam10_PointmassMedium-v0_*?/events*",
        "awac_lambda20" : "data/hw5_expl_q4_awac_medium_supervised_lam20_PointmassMedium-v0_*?/events*",
        "awac_lambda50" : "data/hw5_expl_q4_awac_medium_supervised_lam50_PointmassMedium-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = -60.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 6)))
    
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
    plt.suptitle(f"Learning curves for PointmassMedium-v0 (supervised)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()
