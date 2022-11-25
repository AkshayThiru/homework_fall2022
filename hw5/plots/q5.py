import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    ### Easy env - unsupervised
    if True:
        logs = {
            "tau0.5" : "data/hw5_expl_q5_iql_easy_unsupervised_lam20_tau0.5_PointmassEasy-v0_*?/events*",
            "tau0.6" : "data/hw5_expl_q5_iql_easy_unsupervised_lam20_tau0.6_PointmassEasy-v0_*?/events*",
            "tau0.7" : "data/hw5_expl_q5_iql_easy_unsupervised_lam20_tau0.7_PointmassEasy-v0_*?/events*",
            "tau0.8" : "data/hw5_expl_q5_iql_easy_unsupervised_lam20_tau0.8_PointmassEasy-v0_*?/events*",
            "tau0.9" : "data/hw5_expl_q5_iql_easy_unsupervised_lam20_tau0.9_PointmassEasy-v0_*?/events*",
            "tau0.95" : "data/hw5_expl_q5_iql_easy_unsupervised_lam20_tau0.95_PointmassEasy-v0_*?/events*",
            "tau0.99" : "data/hw5_expl_q5_iql_easy_unsupervised_lam20_tau0.99_PointmassEasy-v0_*?/events*",
        }
        results = get_section_results(logs)

        y_hline = -30.0
        fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
        colors = iter(cm.rainbow(np.linspace(0, 1, 7)))
        
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
        plt.suptitle(f"Learning curves for PointmassEasy-v0 (unsupervised, awac_lambda=20)")
        plt.setp(ax, ylabel="Eval average return")

        fig.tight_layout()
        plt.show()

    ### Easy env - supervised
    logs = {
        "tau0.5" : "data/hw5_expl_q5_iql_easy_supervised_lam20_tau0.5_PointmassEasy-v0_*?/events*",
        "tau0.6" : "data/hw5_expl_q5_iql_easy_supervised_lam20_tau0.6_PointmassEasy-v0_*?/events*",
        "tau0.7" : "data/hw5_expl_q5_iql_easy_supervised_lam20_tau0.7_PointmassEasy-v0_*?/events*",
        "tau0.8" : "data/hw5_expl_q5_iql_easy_supervised_lam20_tau0.8_PointmassEasy-v0_*?/events*",
        "tau0.9" : "data/hw5_expl_q5_iql_easy_supervised_lam20_tau0.9_PointmassEasy-v0_*?/events*",
        "tau0.95" : "data/hw5_expl_q5_iql_easy_supervised_lam20_tau0.95_PointmassEasy-v0_*?/events*",
        "tau0.99" : "data/hw5_expl_q5_iql_easy_supervised_lam20_tau0.99_PointmassEasy-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = -30.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 7)))
    
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
    plt.suptitle(f"Learning curves for PointmassEasy-v0 (supervised, awac_lambda=20)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Easy env - unsupervised
    if True:
        logs = {
            "tau0.5" : "data/hw5_expl_q5_iql_medium_unsupervised_lam20_tau0.5_PointmassMedium-v0_*?/events*",
            "tau0.6" : "data/hw5_expl_q5_iql_medium_unsupervised_lam20_tau0.6_PointmassMedium-v0_*?/events*",
            "tau0.7" : "data/hw5_expl_q5_iql_medium_unsupervised_lam20_tau0.7_PointmassMedium-v0_*?/events*",
            "tau0.8" : "data/hw5_expl_q5_iql_medium_unsupervised_lam20_tau0.8_PointmassMedium-v0_*?/events*",
            "tau0.9" : "data/hw5_expl_q5_iql_medium_unsupervised_lam20_tau0.9_PointmassMedium-v0_*?/events*",
            "tau0.95" : "data/hw5_expl_q5_iql_medium_unsupervised_lam20_tau0.95_PointmassMedium-v0_*?/events*",
            "tau0.99" : "data/hw5_expl_q5_iql_medium_unsupervised_lam20_tau0.99_PointmassMedium-v0_*?/events*",
        }
        results = get_section_results(logs)

        y_hline = -50.0
        fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
        colors = iter(cm.rainbow(np.linspace(0, 1, 7)))
        
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
        plt.suptitle(f"Learning curves for PointmassMedium-v0 (unsupervised, awac_lambda=20)")
        plt.setp(ax, ylabel="Eval average return")

        fig.tight_layout()
        plt.show()

    ### Medium env - supervised
    if True:
        logs = {
            "tau0.5" : "data/hw5_expl_q5_iql_medium_supervised_lam20_tau0.5_PointmassMedium-v0_*?/events*",
            "tau0.6" : "data/hw5_expl_q5_iql_medium_supervised_lam20_tau0.6_PointmassMedium-v0_*?/events*",
            "tau0.7" : "data/hw5_expl_q5_iql_medium_supervised_lam20_tau0.7_PointmassMedium-v0_*?/events*",
            "tau0.8" : "data/hw5_expl_q5_iql_medium_supervised_lam20_tau0.8_PointmassMedium-v0_*?/events*",
            "tau0.9" : "data/hw5_expl_q5_iql_medium_supervised_lam20_tau0.9_PointmassMedium-v0_*?/events*",
            "tau0.95" : "data/hw5_expl_q5_iql_medium_supervised_lam20_tau0.95_PointmassMedium-v0_*?/events*",
            "tau0.99" : "data/hw5_expl_q5_iql_medium_supervised_lam20_tau0.99_PointmassMedium-v0_*?/events*",
        }
        results = get_section_results(logs)

        y_hline = -50.0
        fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
        colors = iter(cm.rainbow(np.linspace(0, 1, 7)))

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
        plt.suptitle(f"Learning curves for PointmassMedium-v0 (supervised, awac_lambda=20)")
        plt.setp(ax, ylabel="Eval average return")

        fig.tight_layout()
        plt.show()
