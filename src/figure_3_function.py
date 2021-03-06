import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import os
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnchoredText


def make_figure_three(figure_path, sim_path):
    mpl.rcParams['font.family'] = 'Helvetica'
    csfont = {'fontname': 'Helvetica'}
    letter_fontsize = 24
    label_fontsize = 18
    df_noz = pd.read_csv(os.path.join(sim_path, 'mat_noz.csv'))
    df_noz['f1'] = pd.to_numeric(df_noz['f1'], errors='coerce')
    fig = plt.figure(figsize=(14.4, 8.5))
    ax1 = plt.subplot2grid((1, 2), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((1, 2), (0, 1), rowspan=1, colspan=1)

    sns.regplot(x='b0', y='f1', ax=ax1, data=df_noz, scatter=False, ci=99.9, order=3, line_kws={'linewidth': 1, 'linestyle':'-'}, color='#3e8abb')
    sns.regplot(x='b0', y='auc', ax=ax1, data=df_noz, scatter=False, ci=99.9, order=3, line_kws={'linewidth': 1, 'linestyle':'-'}, color='#3e8abb')
    sns.regplot(x='b0', y='r2', ax=ax1, data=df_noz, scatter=False, ci=99.9, order=3, line_kws={'linewidth': 1, 'linestyle':'-'}, color='#3e8abb')
    sns.regplot(x='b0', y='ew', ax=ax1, data=df_noz, scatter=False, ci=99.9, order=3, line_kws={'linewidth': 1, 'linestyle':'-'}, color='#f46d43')

    sns.regplot(x='b1', y='f1', ax=ax2, data=df_noz, scatter=False, ci=99.9, order=3, line_kws={'linewidth': 1, 'linestyle':'-'}, color='#3e8abb')
    sns.regplot(x='b1', y='auc', ax=ax2, data=df_noz, scatter=False, ci=99.9, order=3, line_kws={'linewidth': 1, 'linestyle':'-'}, color='#3e8abb')
    sns.regplot(x='b1', y='r2', ax=ax2, data=df_noz, scatter=False, ci=99.9, order=3, line_kws={'linewidth': 1, 'linestyle':'-'}, color='#3e8abb')
    sns.regplot(x='b1', y='ew', ax=ax2, data=df_noz, scatter=False, ci=99.9, order=3, line_kws={'linewidth': 1, 'linestyle':'-'}, color='#f46d43')

    #sns.regplot(x='b0', y='ew', ax=ax1, data=df_noz)
    #df_noz.plot(kind='scatter', x='b0', y='auc', ax=ax2)
    ax1.set_ylim(-.05,1)
    ax2.set_ylim(-.05,1)
    ax1.set_xlim(0, 1.2)
    ax2.set_xlim(0, 1.2)

    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax1.set_ylabel('Metric Value', csfont, fontsize=label_fontsize);
    ax2.set_ylabel('Metric Value', csfont, fontsize=label_fontsize);
    #ax2.set_ylabel('', csfont, fontsize=16);
    ax1.set_xlabel(r'$\mathrm{\beta_{0}}$', csfont, fontsize=label_fontsize);
    ax2.set_xlabel(r'$\mathrm{\beta_{1}}$', csfont, fontsize=label_fontsize);


    ax1.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax2.yaxis.set_minor_locator(plt.MaxNLocator(6))
    ax1.yaxis.set_minor_locator(plt.MaxNLocator(6))
    ax1.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax2.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax2.xaxis.set_minor_locator(plt.MaxNLocator(8))
    ax1.xaxis.set_minor_locator(plt.MaxNLocator(8))
    ax1.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=15)
    ax1.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=15)
    ax2.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=15)
    ax2.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=15)

    #make them black
    ax1.text(1.035, 0.61, 'AUC', fontsize=15, c='k') #c='#3e8abb'
    ax1.text(1.035, 0.2, 'F1', fontsize=15, c='k') #c='#3e8abb'
    ax1.text(1.035, 0.05, r'R$^2$', fontsize=15, c='k') #c='#3e8abb'
    ax1.text(1.035, 0, 'IMV', fontsize=15, c='k') # c='#f46d43'
    ax2.text(1.035, 0.725, 'AUC', fontsize=15, c='k') #c='#3e8abb'
    ax2.text(1.035, 0.525, 'F1', fontsize=15, c='k') #c='#3e8abb'
    ax2.text(1.035, 0.135, r'R$^2$', fontsize=15, c='k') #c='#3e8abb'
    ax2.text(1.035, 0.215, 'IMV', fontsize=15, c='k') # c='#f46d43'

    at = AnchoredText(
        r"$\beta_2$=0.3", prop=dict(size=15), frameon=True, loc='upper right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax1.add_artist(at)
    at = AnchoredText(
        r"$\beta_2$=0.3", prop=dict(size=15), frameon=True, loc='upper right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax2.add_artist(at)

    ax1.yaxis.grid(linestyle='--', alpha=0.25)
    ax1.xaxis.grid(linestyle='--', alpha=0.25)
    ax2.yaxis.grid(linestyle='--', alpha=0.25)
    ax2.xaxis.grid(linestyle='--', alpha=0.25)

    legend_elements = [Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=(255/255, 140/255, 0/255, 0.75),
                              markeredgecolor='k',
                              color='w', label=r'IMV', linestyle='-'),
                       Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=(62/255, 138/255, 187/255, 0.75),
                              markeredgecolor='k',
                              color='w', label=r'Alternative Metric', linestyle='-'),]
    ax1.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize-1, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax2.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize-1, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)

    #sns.despine()
    plt.setp(ax1.collections[1], alpha=.285)
    plt.setp(ax1.collections[3], alpha=.285)
#    plt.setp(ax1.collections[5], alpha=0.285)
#    plt.setp(ax1.collections[7], alpha=0.285)
    plt.setp(ax2.collections[1], alpha=.285)
    plt.setp(ax2.collections[3], alpha=.285)
#    plt.setp(ax2.collections[5], alpha=0.285)
#    plt.setp(ax2.collections[7], alpha=0.285)

    plt.tight_layout(pad=5.0)
    plt.savefig(os.path.join(figure_path, 'figure_3.pdf'), bbox_inches='tight')
