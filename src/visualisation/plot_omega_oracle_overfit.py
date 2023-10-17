import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
import numpy as np
from matplotlib.ticker import FixedLocator, FormatStrFormatter
from matplotlib.lines import Line2D


def plot_omega_oracle_overfit(fig_path, data_path, style_dict, fig_name):
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    letter_fontsize = 23
    label_fontsize = 18
    colors = style_dict['colours']
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 8))

    data_path = os.path.join(data_path, 'sims', 'omega_oracle_overfit')
    omega_0_001 = pd.read_csv(os.path.join(data_path, 'omega_0_0.01.csv'))
    oracle_001 = pd.read_csv(os.path.join(data_path, 'oracle_0.01.csv'))
    overfit_001 = pd.read_csv(os.path.join(data_path, 'overfit_0.01.csv'))

    omega_0_01 = pd.read_csv(os.path.join(data_path, 'omega_0_0.1.csv'))
    oracle_01 = pd.read_csv(os.path.join(data_path, 'oracle_0.1.csv'))
    overfit_01 = pd.read_csv(os.path.join(data_path, 'overfit_0.1.csv'))

    omega_0_05 = pd.read_csv(os.path.join(data_path, 'omega_0_0.5.csv'))
    oracle_05 = pd.read_csv(os.path.join(data_path, 'oracle_0.5.csv'))
    overfit_05 = pd.read_csv(os.path.join(data_path, 'overfit_0.5.csv'))


    ax1.plot(oracle_001['x'], oracle_001['predict'], color=colors[0])
    ax1.fill_between(oracle_001['x'],
                     oracle_001['predict'] - 3.291 * oracle_001['se'],
                     oracle_001['predict'] + 3.291 * oracle_001['se'], color=colors[0],
                     alpha=0.15)

    ax1.plot(overfit_001['x'], overfit_001['predict'], color=colors[1])
    ax1.fill_between(overfit_001['x'],
                     overfit_001['predict'] - 3.291 * overfit_001['se'],
                     overfit_001['predict'] + 3.291 * overfit_001['se'], color=colors[1],
                     alpha=0.15)

    ax1.plot(omega_0_001['x'], omega_0_001['predict'], color=colors[2])
    ax1.fill_between(omega_0_001['x'],
                     omega_0_001['predict'] - 3.291 * omega_0_001['se'],
                     omega_0_001['predict'] + 3.291 * omega_0_001['se'], color=colors[2],
                     alpha=0.15)

    ax2.plot(oracle_01['x'], oracle_01['predict'], color=colors[0])
    ax2.fill_between(oracle_01['x'],
                     oracle_01['predict'] - 3.291 * oracle_01['se'],
                     oracle_01['predict'] + 3.291 * oracle_01['se'], color=colors[0],
                     alpha=0.15)

    ax2.plot(overfit_01['x'], overfit_01['predict'], color=colors[1])
    ax2.fill_between(overfit_01['x'],
                     overfit_01['predict'] - 3.291 * overfit_01['se'],
                     overfit_01['predict'] + 3.291 * overfit_01['se'], color=colors[1],
                     alpha=0.15)

    ax2.plot(omega_0_01['x'], omega_0_01['predict'], color=colors[2])
    ax2.fill_between(omega_0_01['x'],
                     omega_0_01['predict'] - 3.291 * omega_0_01['se'],
                     omega_0_01['predict'] + 3.291 * omega_0_01['se'], color=colors[2],
                     alpha=0.15)

    ax3.plot(oracle_05['x'], oracle_05['predict'], color=colors[0])
    ax3.fill_between(oracle_05['x'],
                     oracle_05['predict'] - 3.291 * oracle_05['se'],
                     oracle_05['predict'] + 3.291 * oracle_05['se'], color=colors[0],
                     alpha=0.15)

    ax3.plot(overfit_05['x'], overfit_05['predict'], color=colors[1])
    ax3.fill_between(overfit_05['x'],
                     overfit_05['predict'] - 3.291 * overfit_05['se'],
                     overfit_05['predict'] + 3.291 * overfit_05['se'], color=colors[1],
                     alpha=0.15)

    ax3.plot(omega_0_05['x'], omega_0_05['predict'], color=colors[2])
    ax3.fill_between(omega_0_05['x'],
                     omega_0_05['predict'] - 3.291 * omega_0_05['se'],
                     omega_0_05['predict'] + 3.291 * omega_0_05['se'], color=colors[2],
                     alpha=0.15)

    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)
    ax3.set_title(r'C.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)

    xticks = [np.log10(50), np.log10(100), np.log10(500), np.log10(1000), np.log10(5000), np.log10(10000)]
    from matplotlib.ticker import FixedLocator, FormatStrFormatter

    for axx in [ax1, ax2, ax3]:
        axx.set_ylim(-0.15, 0.25)
        axx.set_xlim(1, np.log10(12000))
        axx.set_xticks(xticks)
        axx.set_xticklabels([50, '', 500, '', 5000, ''], **csfont)

        # Use FixedLocator to set custom tick positions
        axx.yaxis.set_major_locator(FixedLocator(axx.get_yticks()))

        # Use FormatStrFormatter to set the format of tick labels and fontsize
        axx.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

        # Set the fontsize for both x and y axis labels
        axx.tick_params(axis='both', labelsize=16)

        axx.set_xlabel('N', fontsize=letter_fontsize)
        axx.locator_params(nbins=4, axis='y')
        axx.yaxis.grid(linestyle='--', alpha=0.35)
        axx.xaxis.grid(linestyle='--', alpha=0.35, which='major')


    from matplotlib.offsetbox import AnchoredText
    at = AnchoredText(
        r"$\mathrm{\beta}_1$=0.01", prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax1.add_artist(at)

    at = AnchoredText(
        r"$\mathrm{\beta}_1$=0.1", prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax2.add_artist(at)

    at = AnchoredText(
        r"$\mathrm{\beta}_1$=0.5", prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax3.add_artist(at)

    legend_elements = [Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=colors[0],
                              markeredgecolor='k',
                              color='w', label=r'Oracle', linestyle='none'),
                       Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=colors[1],
                              markeredgecolor='k',
                              color='w', label=r'Overfit', linestyle='none'),
                       Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=colors[2],
                              markeredgecolor='k',
                              color='w', label=r'$\omega_0$', linestyle='none'),
                       ]
    ax1.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize, framealpha=1, facecolor='w',
               edgecolor='k', handletextpad=0.25)

    ax1.set_ylabel('IMV', fontsize=letter_fontsize - 2)
    ax1.annotate('Oracle', (oracle_001['x'][0] - .5, oracle_001['predict'][0]), fontsize=13)
    ax1.annotate('Overfit', (overfit_001['x'][0] - .525, overfit_001['predict'][0]), fontsize=13)
    ax1.annotate(r'$\omega_0$', (omega_0_001['x'][0] - .25, omega_0_001['predict'][0]), fontsize=13)

    ax2.annotate('Oracle', (oracle_01['x'][0] - .5, oracle_01['predict'][0]), fontsize=13)
    ax2.annotate('Overfit', (overfit_01['x'][0] - .525, overfit_01['predict'][0]), fontsize=13)
    ax2.annotate(r'$\omega_0$', (omega_0_01['x'][0] - .25, omega_0_01['predict'][0]), fontsize=13)

    ax3.annotate('Oracle', (oracle_05['x'][0] - .5, oracle_05['predict'][0]), fontsize=13)
    ax3.annotate('Overfit', (overfit_05['x'][0] - .525, overfit_05['predict'][0]), fontsize=13)
    ax3.annotate(r'$\omega_0$', (omega_0_05['x'][0] - .25, omega_0_05['predict'][0]), fontsize=13)

    plt.tight_layout(pad=3.0)
    plt.savefig(os.path.join(fig_path, fig_name), bbox_inches='tight')
