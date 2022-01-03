import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from matplotlib.lines import Line2D
import os


def make_figure_six(figure_path, data_path ):

    mpl.rcParams['font.family'] = 'Helvetica'
    csfont = {'fontname': 'Helvetica'}
    letter_fontsize = 27
    label_fontsize = 22
    data_path = os.path.join(data_path, 'GSS')
    gss1 = pd.read_csv(os.path.join(data_path, 'GSS_imv_output1.csv'), index_col=0)
    gss2 = pd.read_csv(os.path.join(data_path, 'GSS_imv_output2.csv'), index_col=0)
    gssZ = pd.read_csv(os.path.join(data_path, 'GSS_Z.csv'), index_col=['Group.1'])

    fig = plt.figure(figsize=(16, 8), tight_layout=True)
    ax1 = plt.subplot2grid((9, 1), (0, 0), rowspan=6, colspan=1)
    ax2 = plt.subplot2grid((9, 1), (6, 0), rowspan=3, colspan=1)
    gss1['x'].plot(ax=ax1, marker='s', markersize=8,
                   markerfacecolor='#f46d43',
                   c='#f46d43',  # markeredgecolor='k', # linestyle='--',
                   markeredgewidth=0.0)
    gss2['x'].plot(ax=ax1, marker='s', markersize=8,
                   markerfacecolor='#3e8abb',
                   c='#74add1',  # markeredgecolor='k', # linestyle='--',
                   markeredgewidth=0.0)
    gssZ['x'].plot(ax=ax2, c='k')

    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', y=1.02, x=-.05, **csfont)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', y=1.02, x=-.05, **csfont)

    legend_elements = [Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor='#f46d43',
                              markeredgecolor='k',
                              color='w', label=r'Additive', linestyle='none'),
                       Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor='#3e8abb',
                              markeredgecolor='k',
                              color='w', label=r'Interactive', linestyle='none'), ]
    ax1.legend(handles=legend_elements, loc='upper left', frameon=False,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax2.set_ylim(0.4, 0.8)
    ax1.set_ylim(0, 0.32)
    ax1.set_xticklabels([])
    ax1.set_xlim(1970, 2020)
    ax2.set_xlim(1970, 2020)

    ax1.hlines(0.091, ax1.get_xlim()[0], ax1.get_xlim()[1],
               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)

    ax1.hlines(0.048, ax1.get_xlim()[0], ax1.get_xlim()[1],
               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)

    ax1.hlines(0.0099, ax1.get_xlim()[0], ax1.get_xlim()[1],
               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)

    ax1.annotate(r'Sports Book',
                 xy=(2014, 0.095), xycoords='data', **csfont,
                 xytext=(2014, 0.097), fontsize=label_fontsize-4, textcoords='data', )
    ax1.annotate(r'Baccarat',
                 xy=(2014, 0.052), xycoords='data', **csfont,
                 xytext=(2014, 0.055), fontsize=label_fontsize-4, textcoords='data', )
    ax1.annotate(r'Blackjack',
                 xy=(2014, 0.0139), xycoords='data', **csfont,
                 xytext=(2014, 0.015), fontsize=label_fontsize-4, textcoords='data', )
    ax2.hlines(0.5, ax1.get_xlim()[0], ax1.get_xlim()[1],
               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)
    ax1.set_ylabel('IMV based on demographics\nrelative to prevalence', **csfont, fontsize=label_fontsize-2)
    ax2.set_ylabel('Proportion\nGOP', **csfont, fontsize=label_fontsize-2)
    ax2.set_xlabel('Time', **csfont, fontsize = label_fontsize)
    #sns.despine()
    ax1.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax1.tick_params(axis='both', which='major', labelsize=label_fontsize-2)
    ax2.tick_params(axis='both', which='major', labelsize=label_fontsize-2)
    plt.savefig(os.path.join(figure_path, 'figure_6.pdf'), bbox_inches='tight')
