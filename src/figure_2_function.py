import numpy as np
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import matplotlib as mpl
from big_fun import get_w, get_ew, get_vw
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.ticker import FormatStrFormatter
warnings.filterwarnings("ignore")


def make_figure_two(figure_path, sim_path):
    mpl.rcParams['font.family'] = 'Helvetica'
    csfont = {'fontname': 'Helvetica'}
    letter_fontsize = 21
    label_fontsize = 13
    fig = plt.figure(figsize=(14, 9))
    ax1 = plt.subplot2grid((2, 34), (0, 0), rowspan=1, colspan=16)
    ax2 = plt.subplot2grid((2, 34), (0, 18), rowspan=1, colspan=16)
    ax3 = plt.subplot2grid((2, 34), (1, 0), rowspan=1, colspan=16)
    ax4 = plt.subplot2grid((2, 34), (1, 18), rowspan=1, colspan=14)

    dicts_abovehalf = {}
    for a in np.arange(start=0.5, stop=0.99, step=0.001):
        dicts_abovehalf[a] = get_w(a, 0.5, [(0.5, 0.99)])
    ax1.plot(dicts_abovehalf.keys(), dicts_abovehalf.values(), '-', color='#3e8abb', linewidth=1.5)

#    dicts_belowhalf = {}
#    for a in np.arange(start=0.01, stop=0.49, step=0.01):
#        dicts_belowhalf[a] = get_w(a, 0.1, [(0.00, 0.5)])
#    ax1.plot(dicts_belowhalf.keys(), dicts_belowhalf.values(), '-', color='#3e8abb', linewidth=1.5)

    ax1.set_ylabel(r'w', fontsize=label_fontsize, **csfont);
    ax1.set_xlabel(r'A', fontsize=label_fontsize, **csfont);
    ax1.xaxis.grid(linestyle='--', alpha=0.2)
    ax1.yaxis.grid(linestyle='--', alpha=0.2)
    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)
    ax1.set_ylim(ax1.get_ylim()[0], 1)
    ax1.tick_params(axis='y', labelsize=13)
    ax1.tick_params(axis='x', labelsize=13)

    pv = np.divide(list(range(50, 101, 1)), 100)
    del_list = np.divide(list(range(1, 11, 1)), 100)
    norm = plt.Normalize(0.01, 0.1)
    for i in range(1, len(del_list)):
        incrementer = del_list[i]  # equiv to 'del' in R, reserved in py
        pv0 = sorted(i for i in pv if (i + incrementer) < 1)
        p1 = pv0 + incrementer
        y = get_ew(pv0, p1)
        points = np.array([pv0, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lc = LineCollection(segments, cmap='coolwarm', norm=norm)
        lc.set_array(p1 - pv0)
        lc.set_linewidth(1)
        line = ax2.add_collection(lc)
        y = get_ew(pv0, p1) / np.sqrt(get_vw(pv0, p1))
        points = np.array([pv0, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lc = LineCollection(segments, cmap='coolwarm', norm=norm)
        lc.set_array(p1 - pv0)
        lc.set_linewidth(1.5)
        lc.set_linestyle('--')
        line = ax2.add_collection(lc)
    clb = fig.colorbar(line, ax=ax2)
    clb.ax.set_title(r'$\delta$', y=1.01, fontsize=label_fontsize)

    clb.ax.set_yticklabels(clb.ax.get_yticks(), **csfont, fontsize=12)

    ax2.set_ylabel(r'Values of E(W) and Z(W)', fontsize=label_fontsize, **csfont);
    ax2.set_xlabel(r'w$_0$', fontsize=label_fontsize, **csfont);
    ax2.set_ylim(-.025, 0.5)
    ax2.set_xlim(0.475, 1)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)
    ax2.xaxis.grid(linestyle='--', alpha=0.2)
    ax2.yaxis.grid(linestyle='--', alpha=0.2)
    ax2.tick_params(axis='y', labelsize=13)
    ax2.tick_params(axis='x', labelsize=13)
    legend_elements = [Line2D([0], [0], color='#00846b', lw=1, linestyle='-',
                              label=r'E(W)', alpha=1),
                       Line2D([0], [0], color='#00846b', lw=1, linestyle='--',
                              label=r'Z(W)', alpha=1), ]
    ax2.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor=(0, 0, 0, 1))

    # C.
    vals = np.linspace(0.1, 1, 10, endpoint=True)
    x = np.linspace(0.5, 1, 10)
    for val in vals:
        if val == 0.1:
            ax3.plot(x, (val * x) + x, c='#3e8abb', label='IMV', linewidth=1)
            ax3.plot(x, (val * (1 - x)) + x, linestyle='dotted', c='#f46d43', label='Kelly Bet', linewidth=1.5)
        else:
            ax3.plot(x, (val * x) + x, c='#3e8abb', linewidth=1)
            ax3.plot(x, (val * (1 - x)) + x, linestyle='dotted', c='#f46d43', linewidth=1.5)
        ax3.set_ylim(0.5, 1)
        ax3.set_xlim(0.5, 1)
    ax3.set_ylabel(r'w$_1$', fontsize=label_fontsize, **csfont)
    ax3.set_xlabel(r'w$_0$', fontsize=label_fontsize, **csfont)
    ax3.legend(loc='lower right', frameon=True,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor=(0, 0, 0, 1))

    ax3.tick_params(axis='y', labelsize=13)
    ax3.tick_params(axis='x', labelsize=13)
    ax3.xaxis.grid(linestyle='--', alpha=0.3)
    ax3.yaxis.grid(linestyle='--', alpha=0.3)

    ax1.xaxis.grid(linestyle='--', alpha=0.3)
    ax1.yaxis.grid(linestyle='--', alpha=0.3)

    ax2.xaxis.grid(linestyle='--', alpha=0.3)
    ax2.yaxis.grid(linestyle='--', alpha=0.3)
    sns.despine()
    ax3.set_title(r'C.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)

    # d
    df = pd.DataFrame(index=[], columns=['prev', 'b1', 'r2', 'imv'])
    files = os.listdir(sim_path)

    for filename in files:
        if filename.startswith('r2'):
            df1 = pd.read_csv(os.path.join(sim_path, filename), index_col=0)
            df1 = df1.reset_index().rename({'index': 'b0'}, axis=1)
            df1['imv'] = float(filename.split('_')[-1].split('.csv')[0])
            df = df.append(df1, ignore_index=True)

    colors1 = ['#440154FF', '#3E4A89FF',
               '#26828EFF', '#35B779FF',
               '#B4DE2CFF']

    col = 0
    for imv in df['imv'].unique():
        df1 = df[df['imv'] == imv]
        ax4.plot(df1[df1['imv'] == imv]['b1'], df1[df1['imv'] == imv]['r2'], c=colors1[col])
        col = col + 1

    ax4.set_xticklabels(ax1.get_xticks(), **csfont, fontsize=17)
    ax4.set_yticklabels(ax1.get_yticks(), **csfont, fontsize=17)
    ax4.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax4.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax4.set_xlabel(r'$\mathrm{\beta_1}$', **csfont, fontsize=label_fontsize)
    ax4.set_ylabel(r'$\mathrm{R^2}$', **csfont, fontsize=label_fontsize)
    legend_elements = [Line2D([0], [0], markersize=10, marker='', alpha=1,
                              color=colors1[0], label=r'0.01', linestyle='-', linewidth=1),
                       Line2D([0], [0], markersize=0, marker='', alpha=1,
                              color=colors1[1], label=r'0.02', linestyle='-', linewidth=1),
                       Line2D([0], [0], markersize=0, marker='', alpha=1,
                              color=colors1[2], label=r'0.03', linestyle='-', linewidth=1),
                       Line2D([0], [0], markersize=0, marker='', alpha=1,
                              color=colors1[3], label=r'0.04', linestyle='-', linewidth=1),
                       Line2D([0], [0], markersize=0, marker='', alpha=1,
                              color=colors1[4], label=r'0.05', linestyle='-', linewidth=1),
                       ]
    ax4.set_title(r'D.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)
    ax4.tick_params(axis='y', labelsize=13)
    ax4.tick_params(axis='x', labelsize=13)
    sns.despine()
    ax4.set_xlim(0, 5)
    ax4.xaxis.grid(linestyle='--', alpha=0.2)
    ax4.yaxis.grid(linestyle='--', alpha=0.2)
    leg = ax4.legend(handles=legend_elements, loc='lower right', frameon=True,
                     fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.1,
                     ncol=1, handlelength=0.75)
    leg.set_title(title='$\omega$', prop={'size': label_fontsize})
    plt.subplots_adjust(wspace=2.5, hspace=0.25)
    plt.savefig(os.path.join(figure_path, 'figure_2.pdf'), bbox_inches='tight')
