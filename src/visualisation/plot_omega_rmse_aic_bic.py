from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import pandas as pd
import os
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.offsetbox import AnchoredText

def plot_omega_rmse_aic_bic(fig_path, data_path, style_dict, fig_name):
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    label_fontsize = 19
    letter_fontsize = 26
    data_path = os.path.join(data_path, 'sims', 'omega_rmse_aic_bic')
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
    rms_fit_cloglog = pd.read_csv(os.path.join(data_path, 'rms_fit_cloglog.csv'), index_col=0)
    rms_se_cloglog = pd.read_csv(os.path.join(data_path, 'rms_se_cloglog.csv'), index_col=0)
    rms_x_cloglog = pd.read_csv(os.path.join(data_path, 'rms_x_cloglog.csv'), index_col=0)
    rms_fit_xepsilon = pd.read_csv(os.path.join(data_path, 'rms_fit_xepsilon.csv'), index_col=0)
    rms_se_xepsilon = pd.read_csv(os.path.join(data_path, 'rms_se_xepsilon.csv'), index_col=0)
    rms_x_xepsilon = pd.read_csv(os.path.join(data_path, 'rms_x_xepsilon.csv'), index_col=0)
    rms_fit_x2 = pd.read_csv(os.path.join(data_path, 'rms_fit_x2.csv'), index_col=0)
    rms_se_x2 = pd.read_csv(os.path.join(data_path, 'rms_se_x2.csv'), index_col=0)
    rms_x_x2 = pd.read_csv(os.path.join(data_path, 'rms_x_x2.csv'), index_col=0)

    om_fit_cloglog = pd.read_csv(os.path.join(data_path, 'om_fit_cloglog.csv'), index_col=0)
    om_se_cloglog = pd.read_csv(os.path.join(data_path, 'om_se_cloglog.csv'), index_col=0)
    om_x_cloglog = pd.read_csv(os.path.join(data_path, 'om_x_cloglog.csv'), index_col=0)
    om_fit_xepsilon = pd.read_csv(os.path.join(data_path, 'om_fit_xepsilon.csv'), index_col=0)
    om_se_xepsilon = pd.read_csv(os.path.join(data_path, 'om_se_xepsilon.csv'), index_col=0)
    om_x_xepsilon = pd.read_csv(os.path.join(data_path, 'om_x_xepsilon.csv'), index_col=0)
    om_fit_x2 = pd.read_csv(os.path.join(data_path, 'om_fit_x2.csv'), index_col=0)
    om_se_x2 = pd.read_csv(os.path.join(data_path, 'om_se_x2.csv'), index_col=0)
    om_x_x2 = pd.read_csv(os.path.join(data_path, 'om_x_x2.csv'), index_col=0)

    aic_fit_cloglog = pd.read_csv(os.path.join(data_path, 'aic_fit_cloglog.csv'), index_col=0)
    aic_se_cloglog = pd.read_csv(os.path.join(data_path, 'aic_se_cloglog.csv'), index_col=0)
    aic_x_cloglog = pd.read_csv(os.path.join(data_path, 'aic_x_cloglog.csv'), index_col=0)
    aic_fit_xepsilon = pd.read_csv(os.path.join(data_path, 'aic_fit_xepsilon.csv'), index_col=0)
    aic_se_xepsilon = pd.read_csv(os.path.join(data_path, 'aic_se_xepsilon.csv'), index_col=0)
    aic_x_xepsilon = pd.read_csv(os.path.join(data_path, 'aic_x_xepsilon.csv'), index_col=0)
    aic_fit_x2 = pd.read_csv(os.path.join(data_path, 'aic_fit_x2.csv'), index_col=0)
    aic_se_x2 = pd.read_csv(os.path.join(data_path, 'aic_se_x2.csv'), index_col=0)
    aic_x_x2 = pd.read_csv(os.path.join(data_path, 'aic_x_x2.csv'), index_col=0)

    bic_fit_cloglog = pd.read_csv(os.path.join(data_path, 'bic_fit_cloglog.csv'), index_col=0)
    bic_se_cloglog = pd.read_csv(os.path.join(data_path, 'bic_se_cloglog.csv'), index_col=0)
    bic_x_cloglog = pd.read_csv(os.path.join(data_path, 'bic_x_cloglog.csv'), index_col=0)
    bic_fit_xepsilon = pd.read_csv(os.path.join(data_path, 'bic_fit_xepsilon.csv'), index_col=0)
    bic_se_xepsilon = pd.read_csv(os.path.join(data_path, 'bic_se_xepsilon.csv'), index_col=0)
    bic_x_xepsilon = pd.read_csv(os.path.join(data_path, 'bic_x_xepsilon.csv'), index_col=0)
    bic_fit_x2 = pd.read_csv(os.path.join(data_path, 'bic_fit_x2.csv'), index_col=0)
    bic_se_x2 = pd.read_csv(os.path.join(data_path, 'bic_se_x2.csv'), index_col=0)
    bic_x_x2 = pd.read_csv(os.path.join(data_path, 'bic_x_x2.csv'), index_col=0)

    ax1.plot(rms_x_x2['x'], rms_fit_x2['x'], color=style_dict['colours'][0])
    ax1.plot(rms_x_x2['x'], rms_fit_x2['x']+rms_se_x2['x'], color=style_dict['colours'][0], linewidth=0.25)
    ax1.plot(rms_x_x2['x'], rms_fit_x2['x']-rms_se_x2['x'], color=style_dict['colours'][0], linewidth=0.25)
    ax1.fill_between(rms_x_x2['x'],  rms_fit_x2['x']+rms_se_x2['x'],
                     rms_fit_x2['x']-rms_se_x2['x'], color=style_dict['colours'][0], alpha=0.15)
    ax1.plot(rms_x_xepsilon['x'], rms_fit_xepsilon['x'], color=style_dict['colours'][1])
    ax1.plot(rms_x_xepsilon['x'], rms_fit_xepsilon['x'] + rms_se_xepsilon['x'], color=style_dict['colours'][1], linewidth=0.25)
    ax1.plot(rms_x_xepsilon['x'], rms_fit_xepsilon['x'] - rms_se_xepsilon['x'], color=style_dict['colours'][1], linewidth=0.25)
    ax1.fill_between(rms_x_xepsilon['x'],  rms_fit_xepsilon['x']+rms_se_xepsilon['x'],
                     rms_fit_xepsilon['x']-rms_se_xepsilon['x'], color=style_dict['colours'][1], alpha=0.15)
    ax1.plot(rms_x_cloglog['x'], rms_fit_cloglog['x'], color=style_dict['colours'][2])
    ax1.plot(rms_x_cloglog['x'], rms_fit_cloglog['x']+rms_se_cloglog['x'], color=style_dict['colours'][2], linewidth=0.25)
    ax1.plot(rms_x_cloglog['x'], rms_fit_cloglog['x']-rms_se_cloglog['x'], color=style_dict['colours'][2], linewidth=0.25)
    ax1.fill_between(rms_x_cloglog['x'],  rms_fit_cloglog['x']+rms_se_cloglog['x'],
                     rms_fit_cloglog['x']-rms_se_cloglog['x'], color=style_dict['colours'][2], alpha=0.15)


    ax2.plot(om_x_x2['x'], om_fit_x2['x'], color=style_dict['colours'][0])
    ax2.plot(om_x_x2['x'], om_fit_x2['x'] + om_se_x2['x'], color=style_dict['colours'][0], linewidth=0.25)
    ax2.plot(om_x_x2['x'], om_fit_x2['x'] - om_se_x2['x'], color=style_dict['colours'][0], linewidth=0.25)
    ax2.fill_between(om_x_x2['x'],  om_fit_x2['x'] + om_se_x2['x'],
                     om_fit_x2['x'] - om_se_x2['x'], color=style_dict['colours'][0], alpha=0.15)
    ax2.plot(om_x_xepsilon['x'], om_fit_xepsilon['x'], color=style_dict['colours'][1])
    ax2.plot(om_x_xepsilon['x'], om_fit_xepsilon['x'] + om_se_xepsilon['x'], color=style_dict['colours'][1], linewidth=0.25)
    ax2.plot(om_x_xepsilon['x'], om_fit_xepsilon['x'] - om_se_xepsilon['x'], color=style_dict['colours'][1], linewidth=0.25)
    ax2.fill_between(om_x_xepsilon['x'],  om_fit_xepsilon['x'] + om_se_xepsilon['x'],
                     om_fit_xepsilon['x'] - om_se_xepsilon['x'], color=style_dict['colours'][1], alpha=0.15)
    ax2.plot(om_x_cloglog['x'], om_fit_cloglog['x'], color=style_dict['colours'][2])
    ax2.plot(om_x_cloglog['x'], om_fit_cloglog['x'] + om_se_cloglog['x'], color=style_dict['colours'][2], linewidth=0.25)
    ax2.plot(om_x_cloglog['x'], om_fit_cloglog['x'] - om_se_cloglog['x'], color=style_dict['colours'][2], linewidth=0.25)
    ax2.fill_between(om_x_cloglog['x'],  om_fit_cloglog['x'] + om_se_cloglog['x'],
                     om_fit_cloglog['x'] - om_se_cloglog['x'], color=style_dict['colours'][2], alpha=0.15)

    ax3.plot(aic_x_x2['x'], aic_fit_x2['x'], color=style_dict['colours'][0])
    ax3.plot(aic_x_x2['x'], aic_fit_x2['x'] + aic_se_x2['x'], color=style_dict['colours'][0], linewidth=0.25)
    ax3.plot(aic_x_x2['x'], aic_fit_x2['x'] - aic_se_x2['x'], color=style_dict['colours'][0], linewidth=0.25)
    ax3.fill_between(aic_x_x2['x'], aic_fit_x2['x'] + om_se_x2['x'],
                     aic_fit_x2['x'] - aic_se_x2['x'], color=style_dict['colours'][0], alpha=0.15)
    ax3.plot(aic_x_xepsilon['x'], aic_fit_xepsilon['x'], color=style_dict['colours'][1])
    ax3.plot(aic_x_xepsilon['x'], aic_fit_xepsilon['x'] + aic_se_xepsilon['x'], color=style_dict['colours'][1], linewidth=0.25)
    ax3.plot(aic_x_xepsilon['x'], aic_fit_xepsilon['x'] - aic_se_xepsilon['x'], color=style_dict['colours'][1], linewidth=0.25)
    ax3.fill_between(aic_x_xepsilon['x'], aic_fit_xepsilon['x'] + aic_se_xepsilon['x'],
                     aic_fit_xepsilon['x'] - aic_se_xepsilon['x'], color=style_dict['colours'][1], alpha=0.15)
    ax3.plot(aic_x_cloglog['x'], aic_fit_cloglog['x'], color=style_dict['colours'][2])
    ax3.plot(aic_x_cloglog['x'], aic_fit_cloglog['x'] + aic_se_cloglog['x'], color=style_dict['colours'][2], linewidth=0.25)
    ax3.plot(aic_x_cloglog['x'], aic_fit_cloglog['x'] - aic_se_cloglog['x'], color=style_dict['colours'][2], linewidth=0.25)
    ax3.fill_between(aic_x_cloglog['x'], aic_fit_cloglog['x'] + aic_se_cloglog['x'],
                     aic_fit_cloglog['x'] - aic_se_cloglog['x'], color=style_dict['colours'][2], alpha=0.15)

    ax4.plot(bic_x_x2['x'], bic_fit_x2['x'], color=style_dict['colours'][0])
    ax4.plot(bic_x_x2['x'], bic_fit_x2['x'] + bic_se_x2['x'], color=style_dict['colours'][0], linewidth=0.25)
    ax4.plot(bic_x_x2['x'], bic_fit_x2['x'] - bic_se_x2['x'], color=style_dict['colours'][0], linewidth=0.25)
    ax4.fill_between(bic_x_x2['x'], bic_fit_x2['x'] + om_se_x2['x'],
                     bic_fit_x2['x'] - bic_se_x2['x'], color=style_dict['colours'][0], alpha=0.15)
    ax4.plot(bic_x_xepsilon['x'], bic_fit_xepsilon['x'], color=style_dict['colours'][1])
    ax4.plot(bic_x_xepsilon['x'], bic_fit_xepsilon['x'] + bic_se_xepsilon['x'], color=style_dict['colours'][1], linewidth=0.25)
    ax4.plot(bic_x_xepsilon['x'], bic_fit_xepsilon['x'] - bic_se_xepsilon['x'], color=style_dict['colours'][1], linewidth=0.25)
    ax4.fill_between(bic_x_xepsilon['x'], bic_fit_xepsilon['x'] + bic_se_xepsilon['x'],
                     bic_fit_xepsilon['x'] - bic_se_xepsilon['x'], color=style_dict['colours'][1], alpha=0.15)
    ax4.plot(bic_x_cloglog['x'], bic_fit_cloglog['x'], color=style_dict['colours'][2])
    ax4.plot(bic_x_cloglog['x'], bic_fit_cloglog['x'] + bic_se_cloglog['x'], color=style_dict['colours'][2], linewidth=0.25)
    ax4.plot(bic_x_cloglog['x'], bic_fit_cloglog['x'] - bic_se_cloglog['x'], color=style_dict['colours'][2], linewidth=0.25)
    ax4.fill_between(bic_x_cloglog['x'], bic_fit_cloglog['x'] + bic_se_cloglog['x'],
                     bic_fit_cloglog['x'] - bic_se_cloglog['x'], color=style_dict['colours'][2], alpha=0.15)

    ax1.set_ylim(0, 0.06)
    ax2.set_ylim(-0.003, 0.03)
    ax3.set_ylim(-1, 10)
    ax4.set_ylim(-1, 10)

    ax1.yaxis.grid(linestyle='--', alpha=0.25)
    ax1.xaxis.grid(linestyle='--', alpha=0.25)
    ax2.yaxis.grid(linestyle='--', alpha=0.25)
    ax2.xaxis.grid(linestyle='--', alpha=0.25)
    ax3.yaxis.grid(linestyle='--', alpha=0.25)
    ax3.xaxis.grid(linestyle='--', alpha=0.25)
    ax4.yaxis.grid(linestyle='--', alpha=0.25)
    ax4.xaxis.grid(linestyle='--', alpha=0.25)

    ax1.set_ylabel('RMSE', fontsize=16)
    ax2.set_ylabel('IMV', fontsize=16)
    ax3.set_ylabel('AIC', fontsize=16)
    ax4.set_ylabel('BIC', fontsize=16)

    ax1.set_xlabel('N', fontsize=16)
    ax2.set_xlabel('N', fontsize=16)
    ax3.set_xlabel('N', fontsize=16)
    ax4.set_xlabel('N', fontsize=16)

    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax4.set_title(r'D.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)


    custom_xticks = [1.69897, 2.69897, 4.39794]
    custom_xtick_labels = ['50', '500', '25000']
    ax1.set_xticks(custom_xticks)
    ax1.set_xticklabels(custom_xtick_labels)

    ax2.set_xticks(custom_xticks)
    ax2.set_xticklabels(custom_xtick_labels)

    ax3.set_xticks(custom_xticks)
    ax3.set_xticklabels(custom_xtick_labels)

    ax4.set_xticks(custom_xticks)
    ax4.set_xticklabels(custom_xtick_labels)

    ax1.tick_params(axis='both', which='major', labelsize=12)
    ax2.tick_params(axis='both', which='major', labelsize=12)
    ax3.tick_params(axis='both', which='major', labelsize=12)
    ax4.tick_params(axis='both', which='major', labelsize=12)

    from matplotlib.ticker import MaxNLocator
    max_ticks = 5
    ax1.yaxis.set_major_locator(MaxNLocator(max_ticks))
    ax2.yaxis.set_major_locator(MaxNLocator(max_ticks))
    ax3.yaxis.set_major_locator(MaxNLocator(max_ticks))
    ax4.yaxis.set_major_locator(MaxNLocator(max_ticks))

    colors1 = [(0, 28/255, 84/255, 100/255),
               (232/255, 152/255, 24/255, 100/255),
               (207/255, 32/255, 42/255, 100/255)]

    legend_elements = [Line2D([0], [0], markersize=0, marker='s',
                              markerfacecolor=style_dict['colours'][0],
                              markeredgecolor='k',
                              color=style_dict['colours'][0], label=r'x$^2$ (Fit)', linewidth=1.5),
                       Line2D([0], [0], markersize=0, marker='s',
                              markerfacecolor=style_dict['colours'][1],
                              markeredgecolor='k',
                              color=style_dict['colours'][1], label=r'x+$\varepsilon$ (Fit)', linewidth=1.5),
                       Line2D([0], [0], markersize=0, marker='s',
                              #markerfacecolor=colors[2],
                              markeredgecolor='k',
                              color=style_dict['colours'][2], label=r'cloglog (Fit)', linewidth=1.5),
                       Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=colors1[0],
                              markeredgecolor='k',
                              color=colors1[0], label=r'x$^2$ (CI)', linewidth=0,
                              ),
                       Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=colors1[1],
                              markeredgecolor='k',
                              color=colors1[1], label=r'x+$\varepsilon$ (CI)', linewidth=0),
                       Line2D([0], [0], markersize=8, marker='s',
                              #markerfacecolor=colors[2],
                              markeredgecolor='k',
                              color=colors1[2], label=r'cloglog (CI)', linewidth=0),
                       ]

    ax2.legend(handles=legend_elements, loc='upper right', frameon=True,
               fontsize=label_fontsize-8, framealpha=1, facecolor='w', edgecolor='k',
               ncols=2, handletextpad=0.25
               )


    ax1.set_xlim(1.225,)
    ax2.set_xlim(1.225,)
    ax3.set_xlim(1.225,)
    ax4.set_xlim(1.225,)

    ax1.annotate('x$^2$', (1.5, rms_fit_x2['x'][1]), fontsize=12, color=style_dict['colours'][0])
    ax1.annotate('x+$\epsilon$', (1.4, rms_fit_xepsilon['x'][1]), fontsize=12, color=style_dict['colours'][1])
    ax1.annotate('cloglog', (1.25, rms_fit_cloglog['x'][1]), fontsize=12, color=style_dict['colours'][2])

    ax2.annotate('x$^2$', (1.5, om_fit_x2['x'][1]), fontsize=12, color=style_dict['colours'][0])
    ax2.annotate('x+$\epsilon$', (1.4, om_fit_xepsilon['x'][1]), fontsize=12, color=style_dict['colours'][1])
    ax2.annotate('cloglog', (1.25, om_fit_cloglog['x'][1]), fontsize=12, color=style_dict['colours'][2])

    ax3.annotate('x$^2$', (1.5, aic_fit_x2['x'][1]), fontsize=12, color=style_dict['colours'][0])
    ax3.annotate('x+$\epsilon$', (1.4, aic_fit_xepsilon['x'][1]), fontsize=12, color=style_dict['colours'][1])
    ax3.annotate('cloglog', (1.25, aic_fit_cloglog['x'][1]), fontsize=12, color=style_dict['colours'][2])

    ax4.annotate('x$^2$', (1.5, bic_fit_x2['x'][1]), fontsize=12, color=style_dict['colours'][0])
    ax4.annotate('x+$\epsilon$', (1.4, bic_fit_xepsilon['x'][1]), fontsize=12, color=style_dict['colours'][1])
    ax4.annotate('cloglog', (1.25, bic_fit_cloglog['x'][1]), fontsize=12, color=style_dict['colours'][2])

    at = AnchoredText(
        r"$\mathrm{\beta}$=0.05", prop=dict(size=15), frameon=True, loc='upper right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax1.add_artist(at)

    plt.tight_layout()
    plt.savefig(os.path.join(fig_path, fig_name), bbox_inches='tight')