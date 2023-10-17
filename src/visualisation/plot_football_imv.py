import pandas as pd
import os
from statsmodels.nonparametric.smoothers_lowess import lowess
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnchoredText

def plot_football_imv(fig_path, data_path, style_dict, fig_name):

    colors = style_dict['colours']
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    letter_fontsize = 23

    football_all = pd.read_csv(os.path.join(data_path, 'football', 'football_all.csv'),
                               index_col=0)
    football_eng = pd.read_csv(os.path.join(data_path, 'football', 'football_England.csv'),
                               index_col=0)
    football_nl = pd.read_csv(os.path.join(data_path, 'football', 'football_Netherlands.csv'),
                              index_col=0)

    result = lowess(football_all.x, football_all.index)
    x_smooth_all = result[:, 0]
    y_smooth_all = result[:, 1]
    result = lowess(football_eng.x, football_eng.index)
    x_smooth_eng = result[:, 0]
    y_smooth_eng = result[:, 1]
    result = lowess(football_nl.x, football_nl.index)
    x_smooth_nl = result[:, 0]
    y_smooth_nl = result[:, 1]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 9))

    ax1.plot(football_all, color=colors[0], linestyle='--', marker=None, zorder=-1,
             linewidth = style_dict['line_width'])
    ax1.scatter(football_all.index, football_all.x, marker='o', color='w',
                s=80, edgecolor=colors[0], zorder=3, linestyle='None')
    ax1.plot(x_smooth_all, y_smooth_all, color=colors[1],
             linewidth = style_dict['line_width'])

    ax2.plot(football_eng, color=colors[0], linestyle='--', marker=None, zorder=-1,
             linewidth = style_dict['line_width'])
    ax2.scatter(football_eng.index, football_eng.x, marker='o', color='w',
                s=80, edgecolor=colors[0], zorder=3, linestyle='None')
    ax2.plot(x_smooth_eng, y_smooth_eng, color=colors[1],
             linewidth = style_dict['line_width'])

    ax3.plot(football_nl, color=colors[0], linestyle='--', marker=None, zorder=-1,
             linewidth = style_dict['line_width'])
    ax3.scatter(football_nl.index, football_nl.x, marker='o', color='w',
                s=80, edgecolor=colors[0], zorder=3, linestyle='None')
    ax3.plot(x_smooth_nl, y_smooth_nl, color=colors[1],
             linewidth = style_dict['line_width'])

    ax1.set_ylim(0.0, 0.42)
    ax2.set_ylim(0.0, 0.42)
    ax3.set_ylim(0.0, 0.42)
    ax1.set_xlim(1993, 2020)
    ax2.set_xlim(1993, 2020)
    ax3.set_xlim(1993, 2020)

    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', y=1.015, x=-.05, **csfont)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', y=1.015, x=-.05, **csfont)
    ax3.set_title(r'C.', fontsize=letter_fontsize, loc='left', y=1.015, x=-.05, **csfont)

    # ax1.set_yticklabels(ax1.get_yticks(), **csfont, fontsize=15)
    # ax2.set_yticklabels(ax2.get_yticks(), **csfont, fontsize=15)
    # ax3.set_yticklabels(ax3.get_yticks(), **csfont, fontsize=15)
    #
    # ax1.set_xticklabels(ax1.get_xticks(), **csfont, fontsize=15)
    # ax2.set_xticklabels(ax2.get_xticks(), **csfont, fontsize=15)
    # ax3.set_xticklabels(ax3.get_xticks(), **csfont, fontsize=15)

    ax1.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax2.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax3.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax1.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax1.tick_params(axis='both', which='major', labelsize=15)
    ax2.tick_params(axis='both', which='major', labelsize=15)
    ax3.tick_params(axis='both', which='major', labelsize=15)

    ax1.yaxis.grid(linestyle='--', alpha=0.35)
    ax1.xaxis.grid(linestyle='--', alpha=0.35, which='major')

    ax2.yaxis.grid(linestyle='--', alpha=0.35)
    ax2.xaxis.grid(linestyle='--', alpha=0.35, which='major')

    ax3.yaxis.grid(linestyle='--', alpha=0.35)
    ax3.xaxis.grid(linestyle='--', alpha=0.35, which='major')

    ax1.set_ylabel('IMV', fontsize=letter_fontsize - 4, **csfont)

    legend_elements = [Line2D([0], [0], markersize=8, marker='o',
                              markerfacecolor='w',
                              markeredgecolor=colors[0],
                              color='#1D3F6E', label=r'IMV', linestyle='--'),
                       Line2D([0], [0],
                              color=colors[1],
                              label=r'LOESS', linestyle='-')
                       ]
    ax1.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=16, framealpha=1, facecolor='w',
               edgecolor='k', handletextpad=0.25)

    at = AnchoredText(
        r"All", prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax1.add_artist(at)

    at = AnchoredText(
        r"England", prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax2.add_artist(at)

    at = AnchoredText(
        r"Netherlands", prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax3.add_artist(at)
    plt.tight_layout(pad=3)
    plt.savefig(os.path.join(fig_path, fig_name), bbox_inches='tight')
