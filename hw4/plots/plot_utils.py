import glob
import numpy as np
import tensorflow as tf

from typing import Dict


def get_result(file: str, record_steps=False) -> Dict:
    """
        requires tensorflow==1.12.0
    """
    eventfile = glob.glob(file)[0]

    result = {
        # "Timesteps" : [],
        "Eval_AverageReturn" : [],
        "Eval_MinReturn" : [],
        "Eval_MaxReturn" : [],
        "Train_AverageReturn" : [],
        "Train_MinReturn" : [],
        "Train_MaxReturn" : [],
        "Num_Iter" : 0,
    }

    for e in tf.compat.v1.train.summary_iterator(eventfile):
        # if record_steps:
        #     result["Timesteps"].append(e.step)
        for v in e.summary.value:
            for k in result.keys():
                if v.tag == k:
                    result[k].append(v.simple_value)
    for k in result.keys():
        if result[k]:
            result["Num_Iter"] = len(result[k])
            break
    assert result["Num_Iter"] > 0, f"Empty eventfile: {eventfile}"

    return result

def get_section_results(logs: Dict[str, str]) -> Dict[str, Dict]:
    results = dict()
    for label, log in logs.items():
        results[label] = get_result(log)
    return results

def aggregate_results(results: Dict[str, Dict]) -> Dict:
    assert len(results) > 0, f"Empty results file"

    agg_results = dict()
    r = next(iter(results.values()))
    for k in r.keys():
        if not k == "Num_Iter":
            try:
                agg_results[k] = np.array([d[k] for d in results.values()])
            except Exception as e:
                raise e
    agg_results["Num_Iter"] = r["Num_Iter"]

    return agg_results

def get_plot_data(results: Dict) -> (np.ndarray, np.ndarray, np.ndarray):
    niter = results["Num_Iter"]
    xdata = np.arange(niter)

    ydata, edata = dict(), dict()
    for k, v in results.items():
        if not k == "Num_Iter":
            data = np.array(v)
            if len(data.shape) <= 1:
                data = data[None]
            assert data.shape[1] == niter, f"Number of datapoints in {k} (= {data.shape[1]}) is not the same as Num_Iter (= {niter})"
            ydata[k] = np.mean(data, axis=0)
            edata[k] = np.vstack((np.min(data, axis=0), np.max(data, axis=0)))

    return xdata, ydata, edata

"""
### Other commands for plotting:

fig, ax = plt.subplots(<num_h_plots>, <num_v_plots>, figsize=(12, 3), sharex=False, sharey=False, dpi=150)

from matplotlib.pyplot import cm
colors = iter(cm.rainbow(np.linspace(0, 1, <n>)))
c = next(colors)

ax.plot(xdata, ydata["<param>"], marker="o", ls="-", lw=1.5, c=c, label="<param>")
ax.hlines(xmin=<>, xmax=<>, y=<>, lw=1, ls="--", color="k")

ax.legend(loc="lower right")
ax.ticklabel_format(axis="x", style="sci", scilimits=(3,3))
ax.set_xticks(np.arange(0, xdata[-1]+1, step=2))
plt.setp(ax, xlabel="<xlabel>")
plt.setp(ax, ylabel="<ylabel>")

fig.tight_layout()
"""