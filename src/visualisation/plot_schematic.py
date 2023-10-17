import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import os
import numpy as np


def bracket(ax, fontsize, csfont, pos=[0, 0], scalex=1,
            scaley=1, text="", textkw={}, linekw={}):
    x = np.array([0, 0.05, 0.45, 0.5])
    y = np.array([0, -0.01, -0.01, -0.02])
    x = np.concatenate((x, x + 0.5))
    y = np.concatenate((y, y[::-1]))
    ax.plot(x * scalex + pos[0], y * scaley + pos[1], clip_on=False,
            transform=ax.get_xaxis_transform(), **linekw)
    ax.text(pos[0] + 0.5 * scalex, (y.min() - 0.03) * scaley + pos[1], text,
            transform=ax.get_xaxis_transform(), fontsize=fontsize, **csfont,
            ha="center", va="center", **textkw)


def plot_schematic(fig_path, style_dict, fig_name):
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    fig = plt.figure(figsize=(12, 6), tight_layout=True)
    ax1 = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
    sns.despine(left=True, right=True, bottom=True, top=True)
    fontsize=18
    ax1.annotate("  Baseline Prediction ",
                 xy=(0.225, 8), xycoords='data', **csfont,
                 xytext=(0.225, 8), fontsize=fontsize, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w",
                           linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5",
                                 linewidth=0.5, edgecolor='k')
                 )

    ax1.annotate("Enhanced Prediction",
                 xy=(0.25, 4), xycoords='data', **csfont,
                 xytext=(0.25, 4), fontsize=fontsize, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w",
                           linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5",
                                 linewidth=0.5, edgecolor='k')
                 )

    ax1.annotate(r'w$_1$',
                 xy=(2.75, 4), xycoords='data', **csfont,
                 xytext=(2.75, 4), fontsize=fontsize, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w",
                           linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.5",
                                 linewidth=0.5, edgecolor='k')
                 )

    ax1.annotate(r'w$_0$',
                 xy=(2.75, 8), xycoords='data', **csfont,
                 xytext=(2.75, 8), fontsize=fontsize, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w",
                           linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5",
                                 linewidth=0.5, edgecolor='k'),
                 )

    ax1.annotate("Single-Blind\nBet",
                 xy=(4.25, 6), xycoords='data', **csfont,
                 xytext=(4.25, 6), fontsize=fontsize, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w",
                           linewidth=0.5,edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5",
                                 linewidth=0.5, edgecolor='k'),
                 ha='center', va='center'
                 )

    ax1.annotate("Inter-Model\n Vigorish",
                 xy=(5.75, 6), xycoords='data', **csfont,
                 xytext=(5.75, 6), fontsize=fontsize, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w", linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5",
                                 linewidth=0.5, edgecolor='k'),
                 ha='center', va='center'
                 )

    ax1.annotate('', xytext=(1.75, 8), xy=(2.625, 8),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=-0.3",
                                 fc=style_dict['colours'][0]),
                 va='center')

    ax1.annotate('', xytext=(1.75, 4), xy=(2.625, 4),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=0.3",
                                 fc=style_dict['colours'][0]),
                 va='center')

    ax1.annotate('', xytext=(3.05, 8), xy=(3.775, 6.6),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=-0.2",
                                 fc=style_dict['colours'][1]),
                 va='center')
    ax1.annotate('', xytext=(3.05, 4), xy=(3.775, 5.4),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=0.2",
                                 fc=style_dict['colours'][1]),
                 va='center')

    ax1.annotate('', xytext=(4.765, 6), xy=(5.25, 6),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=0",
                                 fc=style_dict['colours'][2]),
                 va='center')

    bracket(ax1, fontsize, csfont, text="Observed Data", pos=[0.225, 0.25],
            scalex=1.4, scaley=1.75,
            linekw=dict(color=style_dict['colours'][0], lw=1.5))
    bracket(ax1, fontsize, csfont, text="Analogous Physical\nSystems", pos=[2.275, 0.25],
            scalex=1.15, scaley=1.75,
            linekw=dict(color=style_dict['colours'][1], lw=1.5))
    bracket(ax1, fontsize, csfont, text="Scale-invariant\ninference", pos=[5.255, 0.25],
            scalex=1.0, scaley=1.75,
            linekw=dict(color=style_dict['colours'][2], lw=1.5))

    ax1.get_yaxis().set_ticks([])
    ax1.get_xaxis().set_ticks([])
    ax1.set_ylim(1, 9.25)
    ax1.set_xlim(0, 6.25)
    plt.savefig(os.path.join(fig_path, fig_name),
                bbox_inches='tight')
