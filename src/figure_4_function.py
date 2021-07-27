import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import os
from matplotlib.lines import Line2D


def make_figure_four(figure_path):
    mpl.rcParams['font.family'] = 'Helvetica'
    csfont = {'fontname': 'Helvetica'}
    letter_fontsize = 24
    label_fontsize = 18
    df_wz1 = pd.read_csv(os.path.join(os.getcwd(), 'data', 'sims', 'mat_wz1.csv'))
    df_wz2 = pd.read_csv(os.path.join(os.getcwd(), 'data', 'sims', 'mat_wz2.csv'))
    df_wz3 = pd.read_csv(os.path.join(os.getcwd(), 'data', 'sims', 'mat_wz3.csv'))
    df_wz1['f1'] = pd.to_numeric(df_wz1['f1'], errors='coerce')
    df_wz2['f1'] = pd.to_numeric(df_wz2['f1'], errors='coerce')
    df_wz3['f1'] = pd.to_numeric(df_wz3['f1'], errors='coerce')

    df_wz1['f1.diff'] = pd.to_numeric(df_wz1['f1.diff'], errors='coerce')
    df_wz2['f1.diff'] = pd.to_numeric(df_wz2['f1.diff'], errors='coerce')
    df_wz3['f1.diff'] = pd.to_numeric(df_wz3['f1.diff'], errors='coerce')

    fig = plt.figure(figsize=(16, 12), tight_layout=True)
    ax1 = plt.subplot2grid((2, 3), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2, 3), (0, 1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((2, 3), (0, 2), rowspan=1, colspan=1)
    ax4 = plt.subplot2grid((2, 3), (1, 0), rowspan=1, colspan=1)
    ax5 = plt.subplot2grid((2, 3), (1, 1), rowspan=1, colspan=1)
    ax6 = plt.subplot2grid((2, 3), (1, 2), rowspan=1, colspan=1)

    sns.regplot(x='b2', y='f1', ax=ax1, data=df_wz1, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='auc', ax=ax1, data=df_wz1, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='r2', ax=ax1, data=df_wz1, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='ew0', ax=ax1, data=df_wz1, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color=(244/255, 109/255, 67/255, 1))

    sns.regplot(x='b2', y='f1', ax=ax2, data=df_wz2, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='auc', ax=ax2, data=df_wz2, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='r2', ax=ax2, data=df_wz2, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='ew0', ax=ax2, data=df_wz2, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color=(244/255, 109/255, 67/255, 1))

    sns.regplot(x='b2', y='f1', ax=ax3, data=df_wz3, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='auc', ax=ax3, data=df_wz3, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='r2', ax=ax3, data=df_wz3, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='ew0', ax=ax3, data=df_wz3, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color=(244/255, 109/255, 67/255, 1))

    sns.regplot(x='b2', y='f1.diff', ax=ax4, data=df_wz1, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='auc.diff', ax=ax4, data=df_wz1, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='r2.diff', ax=ax4, data=df_wz1, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='ew', ax=ax4, data=df_wz1, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color=(244/255, 109/255, 67/255, 1))

    sns.regplot(x='b2', y='f1.diff', ax=ax5, data=df_wz2, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='auc.diff', ax=ax5, data=df_wz2, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='r2.diff', ax=ax5, data=df_wz2, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='ew', ax=ax5, data=df_wz2, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#f46d43')

    sns.regplot(x='b2', y='f1.diff', ax=ax6, data=df_wz3, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='auc.diff', ax=ax6, data=df_wz3, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='r2.diff', ax=ax6, data=df_wz3, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#3e8abb')
    sns.regplot(x='b2', y='ew', ax=ax6, data=df_wz3, scatter=False, ci=99, order=3, line_kws={'linewidth': 0.9, 'linestyle':'--'}, color='#f46d43')

    ax1.set_ylim(-.1,1)
    ax2.set_ylim(-.1,1)
    ax3.set_ylim(-.1,1)
    ax4.set_ylim(-.1, 0.7)
    ax5.set_ylim(-.1, 0.7)
    ax6.set_ylim(-.1, 0.7)

    ax1.set_xlim(-.05, 1.2)
    ax2.set_xlim(-.05, 1.2)
    ax3.set_xlim(-.05, 1.2)
    ax4.set_xlim(-.05, 1.2)
    ax5.set_xlim(-.05, 1.2)
    ax6.set_xlim(-.05, 1.2)

    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax4.set_title(r'D.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax5.set_title(r'E.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax6.set_title(r'F.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)

    ax1.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax4.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax5.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax6.yaxis.set_major_locator(plt.MaxNLocator(3))

    ax1.yaxis.set_minor_locator(plt.MaxNLocator(6))
    ax2.yaxis.set_minor_locator(plt.MaxNLocator(6))
    ax3.yaxis.set_minor_locator(plt.MaxNLocator(6))
    ax4.yaxis.set_minor_locator(plt.MaxNLocator(6))
    ax5.yaxis.set_minor_locator(plt.MaxNLocator(6))
    ax6.yaxis.set_minor_locator(plt.MaxNLocator(6))

    ax1.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax2.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax3.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax4.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax5.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax6.xaxis.set_major_locator(plt.MaxNLocator(4))

    ax1.xaxis.set_minor_locator(plt.MaxNLocator(8))
    ax2.xaxis.set_minor_locator(plt.MaxNLocator(8))
    ax3.xaxis.set_minor_locator(plt.MaxNLocator(8))
    ax4.xaxis.set_minor_locator(plt.MaxNLocator(8))
    ax5.xaxis.set_minor_locator(plt.MaxNLocator(8))
    ax6.xaxis.set_minor_locator(plt.MaxNLocator(8))


    ax1.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=15)
    ax1.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=15)
    ax2.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=15)
    ax2.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=15)
    ax3.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=15)
    ax3.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=15)
    ax4.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=15)
    ax4.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=15)
    ax5.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=15)
    ax5.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=15)
    ax6.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=15)
    ax6.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=15)


    ax1.set_xlabel('', csfont, fontsize=label_fontsize);
    ax2.set_xlabel('', csfont, fontsize=label_fontsize);
    ax3.set_xlabel('', csfont, fontsize=label_fontsize);
    ax4.set_xlabel(r'$\mathrm{\beta_{2}}$', csfont, fontsize=label_fontsize);
    ax5.set_xlabel(r'$\mathrm{\beta_{2}}$', csfont, fontsize=label_fontsize);
    ax6.set_xlabel(r'$\mathrm{\beta_{2}}$', csfont, fontsize=label_fontsize);

    ax1.set_ylabel('Metric (Value)', csfont, fontsize=label_fontsize);
    ax2.set_ylabel('', csfont, fontsize=label_fontsize);
    ax3.set_ylabel('', csfont, fontsize=label_fontsize);
    ax4.set_ylabel('Metric (Difference)', csfont, fontsize=label_fontsize);
    ax5.set_ylabel('', csfont, fontsize=label_fontsize);
    ax6.set_ylabel('', csfont, fontsize=label_fontsize);

    ax1.text(0.75, -0.05, r'$\mathrm{\beta_0 =0}$,   $\mathrm{\beta_1 =0.5}$', fontsize=12.5, c='k')
    ax2.text(0.75, -0.05, r'$\mathrm{\beta_0 =0.5}$,   $\mathrm{\beta_1 =0.5}$', fontsize=12.5, c='k')
    ax3.text(0.75, -0.05, r'$\mathrm{\beta_0 =0.5}$,   $\mathrm{\beta_1 =0.1}$', fontsize=12.5, c='k')

    ax4.text(0.75, -0.06, r'$\mathrm{\beta_0 =0}$,   $\mathrm{\beta_1 =0.5}$', fontsize=12.5, c='k')
    ax5.text(0.75, -0.06, r'$\mathrm{\beta_0 =0.5}$,   $\mathrm{\beta_1 =0.5}$', fontsize=12.5, c='k')
    ax6.text(0.75, -0.06, r'$\mathrm{\beta_0 =0.5}$,   $\mathrm{\beta_1 =0.1}$', fontsize=12.5, c='k')

    legend_elements = [Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=(255/255, 140/255, 0/255, 0.6),
                              markeredgecolor='k',
                              color='w', label=r'IMV', linestyle='-'),
                       Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=(62/255, 138/255, 187/255, 0.5),
                              markeredgecolor='k',
                              color='w', label=r'Alternative Metric', linestyle='-'),]

    ax1.legend(handles=legend_elements, loc='upper left', frameon=False,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax2.legend(handles=legend_elements, loc='upper left', frameon=False,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax3.legend(handles=legend_elements, loc='upper left', frameon=False,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax4.legend(handles=legend_elements, loc='upper left', frameon=False,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax5.legend(handles=legend_elements, loc='upper left', frameon=False,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax6.legend(handles=legend_elements, loc='upper left', frameon=False,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)

    plt.setp(ax1.collections[1], alpha=.285)
    plt.setp(ax1.collections[3], alpha=.285)
#    plt.setp(ax1.collections[5], alpha=0.285)
#    plt.setp(ax1.collections[7], alpha=0.285)
    plt.setp(ax2.collections[1], alpha=.285)
    plt.setp(ax2.collections[3], alpha=.285)
#    plt.setp(ax2.collections[5], alpha=0.285)
#    plt.setp(ax2.collections[7], alpha=0.285)
    plt.setp(ax3.collections[1], alpha=.285)
    plt.setp(ax3.collections[3], alpha=.285)
#    plt.setp(ax3.collections[5], alpha=0.285)
#    plt.setp(ax3.collections[7], alpha=0.285)
    plt.setp(ax4.collections[1], alpha=.285)
    plt.setp(ax4.collections[3], alpha=.285)
#    plt.setp(ax4.collections[5], alpha=0.285)
#    plt.setp(ax4.collections[7], alpha=0.285)
    plt.setp(ax5.collections[1], alpha=.285)
    plt.setp(ax5.collections[3], alpha=.285)
#    plt.setp(ax5.collections[5], alpha=0.285)
#    plt.setp(ax5.collections[7], alpha=0.285)
    plt.setp(ax6.collections[1], alpha=.285)
    plt.setp(ax6.collections[3], alpha=.285)
#    plt.setp(ax6.collections[5], alpha=0.285)
#    plt.setp(ax6.collections[7], alpha=0.285)

    ax1.text(1.035, 0.74, 'AUC', fontsize=15, c='#3e8abb')
    ax1.text(1.035, 0.66, 'F1', fontsize=15, c='#3e8abb')
    ax1.text(1.035, 0.425, 'IMV', fontsize=15, c=(244/255, 109/255, 67/255,1))
    ax1.text(1.035, 0.18, r'R$^2$', fontsize=15, c='#3e8abb')
    ax2.text(1.035, 0.74, 'AUC', fontsize=15, c='#3e8abb')
    ax2.text(1.035, 0.57, 'F1', fontsize=15, c='#3e8abb')
    ax2.text(1.035, 0.25, 'IMV', fontsize=15, c=(244/255, 109/255, 67/255,1))
    ax2.text(1.035, 0.17, r'R$^2$', fontsize=15, c='#3e8abb')
    ax3.text(1.035, 0.74, 'AUC', fontsize=15, c='#3e8abb')
    ax3.text(1.035, 0.53, 'F1', fontsize=15, c='#3e8abb')
    ax3.text(1.035, 0.22, 'IMV', fontsize=15, c=(244/255, 109/255, 67/255,1))
    ax3.text(1.035, 0.13, r'R$^2$', fontsize=15, c='#3e8abb')
    ax4.text(1.035, 0.24, 'IMV', fontsize=15, c=(244/255, 109/255, 67/255,1))
    ax4.text(1.035, 0.165, r'R$^2$', fontsize=15, c='#3e8abb')
    ax4.text(1.035, 0.115, 'AUC', fontsize=15, c='#3e8abb')
    ax4.text(1.035, 0.06, 'F1', fontsize=15, c='#3e8abb')
    ax5.text(1.035, 0.28, 'F1', fontsize=15, c='#3e8abb')
    ax5.text(1.035, 0.18, 'IMV', fontsize=15, c=(244/255, 109/255, 67/255,1))
    ax5.text(1.035, 0.14, r'R$^2$', fontsize=15, c='#3e8abb')
    ax5.text(1.035, 0.10, 'AUC', fontsize=15, c='#3e8abb')
    ax6.text(1.035, 0.53, 'F1', fontsize=15, c='#3e8abb')
    ax6.text(1.035, 0.2, 'IMV', fontsize=15, c=(244/255, 109/255, 67/255,1))
    ax6.text(1.035, 0.2, 'AUC', fontsize=15, c='#3e8abb')
    ax6.text(1.035, 0.125, r'R$^2$', fontsize=15, c='#3e8abb')
    sns.despine()

    plt.savefig(os.path.join(figure_path, 'figure_4.pdf'), bbox_inches='tight', transparent=False)
