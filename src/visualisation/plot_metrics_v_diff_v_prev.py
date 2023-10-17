import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def summary(x, **kwargs):
    label = x.describe()[['mean', 'std', 'min', '50%', 'max']].round()
    ax = plt.gca()
    ax.set_axis_off()
    ax.annotate(label.to_string(), xy=(0.1, 0.2), size=20, xycoords=ax.transAxes)


def plot_metrics_v_diff_v_prev(fig_path, data_path, style_dict, fig_name):
    df = pd.read_csv(os.path.join(data_path, 'sims', 'metrics_v_diff_v_prev',
                                  'metrics_v_diff_v_prev.csv'), index_col=0)
    plt.rcParams['axes.facecolor']='white'
    plt.rcParams['savefig.facecolor']='white'
    g = sns.PairGrid(df, diag_sharey=False, despine=True, height=2.5, aspect=0.8)
    g = g.map_lower(sns.scatterplot, color=style_dict['colours'][0])
    g.map_upper(sns.kdeplot, color=style_dict['colours'][1])
    g = g.map_diag(sns.histplot, facecolor=style_dict['colours'][2],
                   fill=True, edgecolor='k', bins=8, alpha=0.8)
    csfont = {'fontname': style_dict['font']}
    for ax in plt.gcf().axes:
        l = ax.get_xlabel()
        ax.set_xlabel(l,fontsize=18, **csfont)
        l = ax.get_ylabel()
        ax.set_ylabel(l, fontsize=18, **csfont)
        ax.tick_params(axis='both', which='major', labelsize=12)
    g.savefig(os.path.join(fig_path, fig_name))
