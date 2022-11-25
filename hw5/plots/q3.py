import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from plots.plot_utils import *


if __name__ == "__main__":
    import glob

    ### Medium env
    logs = {
        "unsupervised_dyn" : "data/hw5_expl_q2_dqn_PointmassMedium-v0_*?/events*",
        "unsupervised_cql" : "data/hw5_expl_q2_cql_PointmassMedium-v0_*?/events*",
        "supervised_dqn" : "data/hw5_expl_q3_medium_dqn_PointmassMedium-v0_*?/events*",
        "supervised_cql" : "data/hw5_expl_q3_medium_cql_PointmassMedium-v0_*?/events*",
    }
    results = get_section_results(logs)

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
    plt.suptitle(f"Learning curves for PointmassMedium-v0 (num_exploration_steps=20000)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Hard env
    logs = {
        "unsupervised_dyn" : "data/hw5_expl_q2_dqn_PointmassHard-v0_*?/events*",
        "unsupervised_cql" : "data/hw5_expl_q2_cql_PointmassHard-v0_*?/events*",
        "supervised_dqn" : "data/hw5_expl_q3_hard_dqn_PointmassHard-v0_*?/events*",
        "supervised_cql" : "data/hw5_expl_q3_hard_cql_PointmassHard-v0_*?/events*",
    }
    results = get_section_results(logs)

    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 4)))
    
    for key in logs.keys():
        xdata, ydata, _ = get_plot_data(results[key])
        xdata = xdata * int(1e3)
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=key)
    
    ax.legend(loc="lower right")
    ax.set_xticks(np.arange(0, xdata[-1]+1e4, step=int(1e4)))
    ax.ticklabel_format(axis="x", style="sci", scilimits=(3, 3))
    plt.setp(ax, xlabel="Number of iterations")
    plt.suptitle(f"Learning curves for PointmassHard-v0 (num_exploration_steps=20000)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()


    ## num_exploration_steps = 10000


    ### Medium env
    logs = {
        "rnd" : "data/hw5_expl_q1_medium_rnd_PointmassMedium-v0_*?/events*",
        "supervised_dqn" : "data/hw5_expl_q3_medium_dqn_nes10000_PointmassMedium-v0_*?/events*",
        "supervised_cql" : "data/hw5_expl_q3_medium_cql_nes10000_PointmassMedium-v0_*?/events*",
    }
    results = get_section_results(logs)

    y_hline = -40.0
    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 3)))
    
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
    plt.suptitle(f"Learning curves for PointmassMedium-v0 (num_exploration_steps=10000)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Hard env
    logs = {
        "rnd" : "data/hw5_expl_q2_dqn_PointmassHard-v0_*?/events*",
        "supervised_dqn" : "data/hw5_expl_q3_hard_dqn_nes10000_PointmassHard-v0_*?/events*",
        "supervised_cql" : "data/hw5_expl_q3_hard_cql_nes10000_PointmassHard-v0_*?/events*",
    }
    results = get_section_results(logs)

    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 3)))
    
    for key in logs.keys():
        xdata, ydata, _ = get_plot_data(results[key])
        xdata = xdata * int(1e3)
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=key)
    
    ax.legend(loc="lower right")
    ax.set_xticks(np.arange(0, xdata[-1]+1e4, step=int(1e4)))
    ax.ticklabel_format(axis="x", style="sci", scilimits=(3, 3))
    plt.setp(ax, xlabel="Number of iterations")
    plt.suptitle(f"Learning curves for PointmassHard-v0 (num_exploration_steps=10000)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()

    ### Medium env (shifted rewards)
    logs = {
        "supervised_dqn" : "data/hw5_expl_q3_medium_dqn_PointmassMedium-v0_*?/events*",
        "supervised_shifted_cql" : "data/hw5_expl_q3_medium_cql_shift1_scale100_PointmassMedium-v0_*?/events*",
    }
    results = get_section_results(logs)

    fig, ax = plt.subplots(figsize=(10, 5), sharex=False, sharey=True, dpi=150)
    colors = iter(cm.rainbow(np.linspace(0, 1, 2)))
    
    for key in logs.keys():
        xdata, ydata, _ = get_plot_data(results[key])
        xdata = xdata * int(1e3)
        c = next(colors)
        ax.plot(xdata, ydata["Eval_AverageReturn"], ls="-", lw=1.5, c=c, label=key)
    
    ax.hlines(xmin=xdata[0], xmax=xdata[-1], y=-40.0, lw=1, ls="--", color="k")
    ax.legend(loc="lower right")
    ax.set_xticks(np.arange(0, xdata[-1]+1e4, step=int(1e4)))
    ax.ticklabel_format(axis="x", style="sci", scilimits=(3, 3))
    plt.setp(ax, xlabel="Number of iterations")
    plt.suptitle(f"Learning curves for PointmassMedium-v0 (num_exploration_steps=20000)")
    plt.setp(ax, ylabel="Eval average return")

    fig.tight_layout()
    plt.show()
