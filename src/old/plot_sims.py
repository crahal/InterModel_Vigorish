import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import matplotlib as mpl
mpl.rcParams['font.family'] = 'Arial'
csfont = {'fontname': 'Arial'}

def plot_sim1(mat_noz, mat_wz):
    fig = plt.figure(figsize=(14, 9), tight_layout=True)
    ax1 = plt.subplot2grid((2, 3), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2, 3), (0, 1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((2, 3), (0, 2), rowspan=1, colspan=1)
    ax4 = plt.subplot2grid((2, 3), (1, 0), rowspan=1, colspan=1)
    ax5 = plt.subplot2grid((2, 3), (1, 1), rowspan=1, colspan=1)
    ax6 = plt.subplot2grid((2, 3), (1, 2), rowspan=1, colspan=1)

    ax1.scatter(x=mat_noz['b0'][2:], y=mat_noz['ew'][2:], facecolor='w', color='#377eb8')
    ax1.scatter(x=mat_noz['b0'][0:2], y=mat_noz['ew'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)

    ax2.scatter(x=mat_noz['b1'][2:], y=mat_noz['ew'][2:], facecolor='w', color='#377eb8')
    ax2.scatter(x=mat_noz['b1'][0:2], y=mat_noz['ew'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)

    ax3.scatter(x=mat_noz['b2'][2:], y=mat_noz['ew'][2:], facecolor='w', color='#377eb8')
    ax3.scatter(x=mat_noz['b2'][0:2], y=mat_noz['ew'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)

    ax4.scatter(x=mat_wz['b0'][2:], y=mat_wz['ew'][2:], facecolor='w', color='#377eb8')
    ax4.scatter(x=mat_wz['b0'][0:2], y=mat_wz['ew'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)

    ax5.scatter(x=mat_wz['b1'][2:], y=mat_wz['ew'][2:], facecolor='w', color='#377eb8')
    ax5.scatter(x=mat_wz['b1'][0:2], y=mat_wz['ew'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)

    ax6.scatter(x=mat_wz['b2'][2:], y=mat_wz['ew'][2:], facecolor='w', color='#377eb8')
    ax6.scatter(x=mat_wz['b2'][0:2], y=mat_wz['ew'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)

    ax1.set_title(r'A.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax4.set_title(r'D.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax5.set_title(r'E.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax6.set_title(r'F.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)

    ax1.set_ylabel(r'IMV', **csfont, fontsize=14)
    ax4.set_ylabel(r'IMV', **csfont, fontsize=14)
    ax4.set_xlabel(r'$\beta_0$', **csfont, fontsize=14)
    ax5.set_xlabel(r'$\beta_1$', **csfont, fontsize=14)
    ax6.set_xlabel(r'$\beta_2$', **csfont, fontsize=14)

    ax1.set_ylim(-.025, ax1.get_ylim()[1])
    ax1.set_xlim(-.15, ax1.get_xlim()[1])
    ax1.spines['bottom'].set_bounds(0, ax1.get_xlim()[1])
    ax1.spines['left'].set_bounds(0, ax1.get_ylim()[1])
    ax2.set_ylim(-.025, ax2.get_ylim()[1])
    ax2.set_xlim(0.85, ax2.get_xlim()[1])
    ax2.spines['bottom'].set_bounds(1, ax2.get_xlim()[1])
    ax2.spines['left'].set_bounds(0, ax2.get_ylim()[1])
    ax3.set_ylim(-.025, ax3.get_ylim()[1])
    ax3.set_xlim(0.85, ax3.get_xlim()[1])
    ax3.spines['bottom'].set_bounds(1, ax3.get_xlim()[1])
    ax3.spines['left'].set_bounds(0, ax3.get_ylim()[1])
    ax4.set_ylim(-.025, ax4.get_ylim()[1])
    ax4.set_xlim(-.15, ax4.get_xlim()[1])
    ax4.spines['bottom'].set_bounds(0, ax4.get_xlim()[1])
    ax4.spines['left'].set_bounds(0, ax4.get_ylim()[1])
    ax5.set_ylim(-.025, ax5.get_ylim()[1])
    ax5.set_xlim(0.85, ax5.get_xlim()[1])
    ax5.spines['bottom'].set_bounds(1, ax5.get_xlim()[1])
    ax5.spines['left'].set_bounds(0, ax5.get_ylim()[1])
    ax6.set_ylim(-.025, ax6.get_ylim()[1])
    ax6.set_xlim(0.85, ax6.get_xlim()[1])
    ax6.spines['bottom'].set_bounds(1, ax6.get_xlim()[1])
    ax6.spines['left'].set_bounds(0, ax6.get_ylim()[1])
    sns.despine()
    # new edits
    ax1.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax4.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax5.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax6.yaxis.set_major_locator(plt.MaxNLocator(3))

    ax1.tick_params(axis='both', which='major', labelsize=15)
    ax2.tick_params(axis='both', which='major', labelsize=15)
    ax3.tick_params(axis='both', which='major', labelsize=15)
    ax4.tick_params(axis='both', which='major', labelsize=15)
    ax5.tick_params(axis='both', which='major', labelsize=15)
    ax6.tick_params(axis='both', which='major', labelsize=15)


    plt.savefig(os.path.join(os.getcwd(), '..', 'results', 'figures',
                             'sim1.pdf'),
                bbox_inches='tight')
    plt.savefig(os.path.join(os.getcwd(), '..', 'results', 'figures',
                             'sim1.png'),
                bbox_inches='tight')


def plot_sim2(mat_noz, mat_wz):
    fig = plt.figure(figsize=(14, 9), tight_layout=True)
    ax1 = plt.subplot2grid((2, 3), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2, 3), (0, 1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((2, 3), (0, 2), rowspan=1, colspan=1)
    ax4 = plt.subplot2grid((2, 3), (1, 0), rowspan=1, colspan=1)
    ax5 = plt.subplot2grid((2, 3), (1, 1), rowspan=1, colspan=1)
    ax6 = plt.subplot2grid((2, 3), (1, 2), rowspan=1, colspan=1)

    ax1.scatter(x=mat_noz['ew'][2:], y=mat_noz['r2'][2:], facecolor='w', color='#377eb8')
    ax1.scatter(x=mat_noz['ew'][0:2], y=mat_noz['r2'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)
    ax2.scatter(x=mat_noz['ew'][2:], y=mat_noz['auc'][2:], facecolor='w', color='#377eb8')
    ax2.scatter(x=mat_noz['ew'][0:2], y=mat_noz['auc'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)
    ax3.scatter(x=mat_noz['ew'][2:], y=mat_noz['f1'][2:], facecolor='w', color='#377eb8')
    ax3.scatter(x=mat_noz['ew'][0:2], y=mat_noz['f1'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)

    ax4.scatter(x=mat_wz['ew'][2:], y=mat_wz['r2'][2:], facecolor='w', color='#377eb8')
    ax4.scatter(x=mat_wz['ew'][0:2], y=mat_wz['r2'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)
    ax5.scatter(x=mat_wz['ew'][2:], y=mat_wz['auc'][2:], facecolor='w', color='#377eb8')
    ax5.scatter(x=mat_wz['ew'][0:2], y=mat_wz['auc'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)
    ax6.scatter(x=mat_wz['ew'][2:], y=mat_wz['f1'][2:], facecolor='w', color='#377eb8')
    ax6.scatter(x=mat_wz['ew'][0:2], y=mat_wz['f1'][0:2], facecolor='#ff7f00', color='#ff7f00',
                s=100, edgecolor='k', linewidth=0.5)

    ax1.set_title(r'A.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax4.set_title(r'D.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax5.set_title(r'E.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax6.set_title(r'F.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)

    ax1.set_ylabel(r'R$^2$', **csfont, fontsize=16)
    ax4.set_ylabel(r'R$^2$', **csfont, fontsize=16)
    ax2.set_ylabel(r'AUC', **csfont, fontsize=16)
    ax5.set_ylabel(r'AUC', **csfont, fontsize=16)
    ax3.set_ylabel(r'F1', **csfont, fontsize=16)
    ax6.set_ylabel(r'F1', **csfont, fontsize=16)
    ax4.set_xlabel(r'IMV', **csfont, fontsize=16)
    ax5.set_xlabel(r'IMV', **csfont, fontsize=16)
    ax6.set_xlabel(r'IMV', **csfont, fontsize=16)

    ax1.set_ylim(-.05, 1)
    ax1.set_xlim(-.035, ax1.get_xlim()[1])
    ax1.spines['bottom'].set_bounds(0, ax1.get_xlim()[1])
    ax1.spines['left'].set_bounds(0, ax1.get_ylim()[1])

    ax2.set_ylim(-.05, 1)
    ax2.set_xlim(-.035, ax2.get_xlim()[1])
    ax2.spines['bottom'].set_bounds(0, ax2.get_xlim()[1])
    ax2.spines['left'].set_bounds(0, ax2.get_ylim()[1])

    ax3.set_ylim(-.05, 1)
    ax3.set_xlim(-.035, ax3.get_xlim()[1])
    ax3.spines['bottom'].set_bounds(0, ax3.get_xlim()[1])
    ax3.spines['left'].set_bounds(0, ax3.get_ylim()[1])
    sns.despine()

    ax4.set_ylim(-.05, 1)
    ax4.set_xlim(-.035, ax4.get_xlim()[1])
    ax4.spines['bottom'].set_bounds(0, ax4.get_xlim()[1])
    ax4.spines['left'].set_bounds(0, ax4.get_ylim()[1])

    ax5.set_ylim(-.05, 1)
    ax5.set_xlim(-.035, ax2.get_xlim()[1])
    ax5.spines['bottom'].set_bounds(0, ax5.get_xlim()[1])
    ax5.spines['left'].set_bounds(0, ax5.get_ylim()[1])

    ax6.set_ylim(-.05, 1)
    ax6.set_xlim(-.035, ax6.get_xlim()[1])
    ax6.spines['bottom'].set_bounds(0, ax6.get_xlim()[1])
    ax6.spines['left'].set_bounds(0, ax6.get_ylim()[1])
    sns.despine()

    ax1.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax4.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax5.yaxis.set_major_locator(plt.MaxNLocator(3))
    ax6.yaxis.set_major_locator(plt.MaxNLocator(3))

    ax1.tick_params(axis='both', which='major', labelsize=15)
    ax2.tick_params(axis='both', which='major', labelsize=15)
    ax3.tick_params(axis='both', which='major', labelsize=15)
    ax4.tick_params(axis='both', which='major', labelsize=15)
    ax5.tick_params(axis='both', which='major', labelsize=15)
    ax6.tick_params(axis='both', which='major', labelsize=15)


    plt.savefig(os.path.join(os.getcwd(), '..', 'results', 'figures',
                             'sim2.pdf'),
                bbox_inches='tight')
    plt.savefig(os.path.join(os.getcwd(), '..', 'results', 'figures',
                             'sim2.png'),
                bbox_inches='tight')


def plot_sim3(mat_noz, mat_wz):
    fig = plt.figure(figsize=(14, 12), tight_layout=True)
    ax1 = plt.subplot2grid((3, 3), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((3, 3), (0, 1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((3, 3), (0, 2), rowspan=1, colspan=1)
    ax4 = plt.subplot2grid((3, 3), (1, 0), rowspan=1, colspan=1)
    ax5 = plt.subplot2grid((3, 3), (1, 1), rowspan=1, colspan=1)
    ax6 = plt.subplot2grid((3, 3), (1, 2), rowspan=1, colspan=1)
    ax7 = plt.subplot2grid((3, 3), (2, 0), rowspan=1, colspan=1)
    ax8 = plt.subplot2grid((3, 3), (2, 1), rowspan=1, colspan=1)
    ax9 = plt.subplot2grid((3, 3), (2, 2), rowspan=1, colspan=1)

    ax1.scatter(x=mat_noz['b0'][2:], y=mat_noz['r2'][2:], facecolor='w', color='#377eb8')
    ax2.scatter(x=mat_noz['b1'][2:], y=mat_noz['r2'][2:], facecolor='w', color='#377eb8')
    ax3.scatter(x=mat_noz['b2'][2:], y=mat_noz['r2'][2:], facecolor='w', color='#377eb8')
    ax4.scatter(x=mat_noz['b0'][2:], y=mat_noz['auc'][2:], facecolor='w', color='#377eb8')
    ax5.scatter(x=mat_noz['b1'][2:], y=mat_noz['auc'][2:], facecolor='w', color='#377eb8')
    ax6.scatter(x=mat_noz['b2'][2:], y=mat_noz['auc'][2:], facecolor='w', color='#377eb8')
    ax7.scatter(x=mat_noz['b0'][2:], y=mat_noz['f1'][2:], facecolor='w', color='#377eb8')
    ax8.scatter(x=mat_noz['b1'][2:], y=mat_noz['f1'][2:], facecolor='w', color='#377eb8')
    ax9.scatter(x=mat_noz['b2'][2:], y=mat_noz['f1'][2:], facecolor='w', color='#377eb8')

    ax1.set_title(r'A.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)
    ax4.set_title(r'D.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)
    ax5.set_title(r'E.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)
    ax6.set_title(r'F.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)
    ax7.set_title(r'G.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)
    ax8.set_title(r'H.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)
    ax9.set_title(r'I.', fontsize=24, loc='left', x=-.05, **csfont, y=1.025)

    ax1.set_ylabel(r'R$^2$', **csfont, fontsize=16)
    ax4.set_ylabel(r'AUC', **csfont, fontsize=16)
    ax7.set_ylabel(r'F1', **csfont, fontsize=16)

    ax7.set_xlabel(r'$\beta_0$', **csfont, fontsize=14)
    ax8.set_xlabel(r'$\beta_1$', **csfont, fontsize=14)
    ax9.set_xlabel(r'$\beta_2$', **csfont, fontsize=14)

    ax1.set_ylim(-.035, (ax1.get_ylim()[1]+(ax1.get_ylim()[1])/20))
    ax1.set_xlim(-.225, ax1.get_xlim()[1])
    ax1.spines['bottom'].set_bounds(0, ax1.get_xlim()[1])
    ax1.spines['left'].set_bounds(0, ax1.get_ylim()[1])

    ax2.set_ylim(-.035, (ax2.get_ylim()[1]+(ax2.get_ylim()[1])/20))
    ax2.set_xlim(.775, ax2.get_xlim()[1])
    ax2.spines['bottom'].set_bounds(1, ax2.get_xlim()[1])
    ax2.spines['left'].set_bounds(0, ax2.get_ylim()[1])

    ax3.set_ylim(-.035, (ax3.get_ylim()[1]+(ax3.get_ylim()[1])/20))
    ax3.set_xlim(.775, ax3.get_xlim()[1])
    ax3.spines['bottom'].set_bounds(1, ax3.get_xlim()[1])
    ax3.spines['left'].set_bounds(0, ax3.get_ylim()[1])

    ax4.set_ylim(.525, (ax4.get_ylim()[1]+(ax4.get_ylim()[1])/20))
    ax4.set_xlim(-.225, ax4.get_xlim()[1])
    ax4.spines['bottom'].set_bounds(0, ax4.get_xlim()[1])
    ax4.spines['left'].set_bounds(0.55, ax4.get_ylim()[1])

    ax5.set_ylim(.525, (ax5.get_ylim()[1]+(ax5.get_ylim()[1])/20))
    ax5.set_xlim(.775, ax5.get_xlim()[1])
    ax5.spines['bottom'].set_bounds(1, ax5.get_xlim()[1])
    ax5.spines['left'].set_bounds(0.55, ax5.get_ylim()[1])

    ax6.set_ylim(.525, (ax6.get_ylim()[1]+(ax6.get_ylim()[1])/20))
    ax6.set_xlim(.775, ax6.get_xlim()[1])
    ax6.spines['bottom'].set_bounds(1, ax6.get_xlim()[1])
    ax6.spines['left'].set_bounds(0.55, ax6.get_ylim()[1])

    ax7.set_ylim(-.05, (ax7.get_ylim()[1]+(ax7.get_ylim()[1])/20))
    ax7.set_xlim(-.225, ax7.get_xlim()[1])
    ax7.spines['bottom'].set_bounds(0, ax7.get_xlim()[1])
    ax7.spines['left'].set_bounds(0, ax7.get_ylim()[1])

    ax8.set_ylim(-.05, (ax8.get_ylim()[1]+(ax8.get_ylim()[1])/20))
    ax8.set_xlim(.775, ax8.get_xlim()[1])
    ax8.spines['bottom'].set_bounds(1, ax8.get_xlim()[1])
    ax8.spines['left'].set_bounds(0, ax8.get_ylim()[1])

    ax9.set_ylim(-.05, (ax9.get_ylim()[1]+(ax9.get_ylim()[1])/20))
    ax9.set_xlim(.775, ax9.get_xlim()[1])
    ax9.spines['bottom'].set_bounds(1, ax9.get_xlim()[1])
    ax9.spines['left'].set_bounds(0, ax9.get_ylim()[1])

    ax1.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax3.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax4.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax5.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax6.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax7.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax8.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax9.yaxis.set_major_locator(plt.MaxNLocator(4))

    ax1.tick_params(axis='both', which='major', labelsize=15)
    ax2.tick_params(axis='both', which='major', labelsize=15)
    ax3.tick_params(axis='both', which='major', labelsize=15)
    ax4.tick_params(axis='both', which='major', labelsize=15)
    ax5.tick_params(axis='both', which='major', labelsize=15)
    ax6.tick_params(axis='both', which='major', labelsize=15)
    ax7.tick_params(axis='both', which='major', labelsize=15)
    ax8.tick_params(axis='both', which='major', labelsize=15)
    ax9.tick_params(axis='both', which='major', labelsize=15)


    sns.despine()
    plt.savefig(os.path.join(os.getcwd(), '..', 'results', 'figures',
                             'sim3.pdf'),
                bbox_inches='tight')
    plt.savefig(os.path.join(os.getcwd(), '..', 'results', 'figures',
                             'sim3.png'),
                bbox_inches='tight')

def main():
    data_dir = os.path.join(os.getcwd(), '..', 'data', 'sims')
    mat_noz = pd.read_csv(os.path.join(data_dir, 'mat_noz.csv'), index_col=0)
    mat_wz = pd.read_csv(os.path.join(data_dir, 'mat_wz.csv'), index_col=0)
    plot_sim1(mat_noz, mat_wz)
    plot_sim2(mat_noz, mat_wz)
    plot_sim3(mat_noz, mat_wz)

if __name__ == '__main__':
    main()