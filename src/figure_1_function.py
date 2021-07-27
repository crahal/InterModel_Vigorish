import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import os
import numpy as np


def bracket(ax, csfont, pos=[0, 0], scalex=1, scaley=1, text="", textkw={}, linekw={}):
    x = np.array([0, 0.05, 0.45, 0.5])
    y = np.array([0, -0.01, -0.01, -0.02])
    x = np.concatenate((x, x + 0.5))
    y = np.concatenate((y, y[::-1]))
    ax.plot(x * scalex + pos[0], y * scaley + pos[1], clip_on=False,
            transform=ax.get_xaxis_transform(), **linekw)
    ax.text(pos[0] + 0.5 * scalex, (y.min() - 0.03) * scaley + pos[1], text,
            transform=ax.get_xaxis_transform(), fontsize=16, **csfont,
            ha="center", va="center", **textkw)


def make_figure_one(figure_path):
    mpl.rcParams['font.family'] = 'Helvetica'
    csfont = {'fontname': 'Helvetica'}
    fig = plt.figure(figsize=(12, 6), tight_layout=True)
    ax1 = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
    sns.despine(left=True, right=True, bottom=True, top=True)
    ax1.annotate("  Baseline Prediction ",
                 xy=(0.4, 8), xycoords='data', **csfont,
                 xytext=(0.4, 8), fontsize=16, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w", linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5", linewidth=0.5, edgecolor='k')
                 )

    ax1.annotate("Enhanced Prediction",
                 xy=(0.4, 4), xycoords='data', **csfont,
                 xytext=(0.4, 4), fontsize=16, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w", linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5", linewidth=0.5, edgecolor='k')
                 )

    ax1.annotate(r'w$_1$',
                 xy=(2.5, 4), xycoords='data', **csfont,
                 xytext=(2.5, 4), fontsize=16, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w", linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5", linewidth=0.5, edgecolor='k')
                 )

    ax1.annotate(r'w$_0$',
                 xy=(2.5, 8), xycoords='data', **csfont,
                 xytext=(2.5, 8), fontsize=16, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w", linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5", linewidth=0.5, edgecolor='k'),
                 )

    ax1.annotate("Single-Blind\nBet",
                 xy=(3.65, 6), xycoords='data', **csfont,
                 xytext=(3.65, 6), fontsize=16, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w", linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5", linewidth=0.5, edgecolor='k'),
                 ha='center', va='center'
                 )

    ax1.annotate("Inter-Model\n Vigorish",
                 xy=(5.05, 6), xycoords='data', **csfont,
                 xytext=(5.05, 6), fontsize=16, textcoords='data',
                 bbox=dict(boxstyle="round, pad=1", fc="w", linewidth=0.5, edgecolor=(0, 0, 0, 1)),
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.5", linewidth=0.5, edgecolor='k'),
                 ha='center', va='center'
                 )

    ax1.annotate('', xytext=(1.6, 8), xy=(2.4, 8),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=-0.3", fc='#f46d43'),
                 va='center')

    ax1.annotate('', xytext=(1.58, 4), xy=(2.4, 4),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=0.3", fc='#f46d43'),
                 va='center')

    ax1.annotate('', xytext=(2.75, 8), xy=(3.4, 6.6),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=-0.2", fc='#3e8abb'),
                 va='center')
    ax1.annotate('', xytext=(2.75, 4), xy=(3.4, 5.4),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=0.2", fc='#3e8abb'),
                 va='center')

    ax1.annotate('', xytext=(4.075, 6), xy=(4.65, 6),
                 arrowprops=dict(arrowstyle="-|>", mutation_scale=35,
                                 connectionstyle="arc3,rad=0", fc="w"),
                 va='center')

    bracket(ax1, csfont, text="Observed Data", pos=[0.3, 0.2],
            scalex=1.2, scaley=1.75,
            linekw=dict(color='#f46d43', lw=1.5))
    bracket(ax1, csfont, text="Analogous Physical\nSystems", pos=[1.95, 0.2],
            scalex=1.125, scaley=1.75,
            linekw=dict(color='#3e8abb', lw=1.5))
    bracket(ax1, csfont, text="Scale-invariant\ninference", pos=[4.55, 0.2],
            scalex=1, scaley=1.75,
            linekw=dict(color="k", lw=1.5))

    ax1.get_yaxis().set_ticks([])
    ax1.get_xaxis().set_ticks([])
    ax1.set_ylim(1, 9)
    ax1.set_xlim(0, 6)
    plt.savefig(os.path.join(figure_path, 'figure_1.pdf'), bbox_inches='tight')
