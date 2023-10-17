import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnchoredText


def lowess_with_confidence_bounds(
        x, y, eval_x, N=500, conf_interval=0.95, lowess_kw=None
):
    """
    Perform Lowess regression and determine a confidence interval by bootstrap resampling
    """
    # Lowess smoothing
    smoothed = sm.nonparametric.lowess(exog=x, endog=y, xvals=eval_x, **lowess_kw)

    # Perform bootstrap resamplings of the data
    # and  evaluate the smoothing at a fixed set of points
    smoothed_values = np.empty((N, len(eval_x)))
    for i in range(N):
        sample = np.random.choice(len(x), len(x), replace=True)
        sampled_x = x[sample]
        sampled_y = y[sample]

        smoothed_values[i] = sm.nonparametric.lowess(
            exog=sampled_x, endog=sampled_y, xvals=eval_x, **lowess_kw
        )

    # Get the confidence interval
    sorted_values = np.sort(smoothed_values, axis=0)
    bound = int(N * (1 - conf_interval) / 2)
    bottom = sorted_values[bound - 1]
    top = sorted_values[-bound]
    return smoothed, bottom, top


def plot_imv_v_altmet(fig_path, data_path, style_dict, fig_name):
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    colors = style_dict['colours']
    letter_fontsize = 24
    label_fontsize = 18
    df_noz = pd.read_csv(os.path.join(data_path, 'sims', 'imv_v_altmet', 'imv_v_altmet.csv'))
    df_noz['f1'] = pd.to_numeric(df_noz['f1'], errors='coerce')
    fig = plt.figure(figsize=(14.4, 8.5))
    ax1 = plt.subplot2grid((1, 2), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((1, 2), (0, 1), rowspan=1, colspan=1)

    #    smoothed_b0_f1 = sm.nonparametric.lowess(exog=df_noz['b0'], endog=df_noz['f1'], frac=0.2)
    #    smoothed_b0_auc = sm.nonparametric.lowess(exog=df_noz['b0'], endog=df_noz['auc'], frac=0.2)
    #    smoothed_b0_r2 = sm.nonparametric.lowess(exog=df_noz['b0'], endog=df_noz['r2'], frac=0.2)
    #    smoothed_b0_ew = sm.nonparametric.lowess(exog=df_noz['b0'], endog=df_noz['ew'], frac=0.2)
    #
    #    smoothed_b1_f1 = sm.nonparametric.lowess(exog=df_noz['b1'], endog=df_noz['f1'], frac=0.2)
    #    smoothed_b1_auc = sm.nonparametric.lowess(exog=df_noz['b1'], endog=df_noz['auc'], frac=0.2)
    #    smoothed_b1_r2 = sm.nonparametric.lowess(exog=df_noz['b1'], endog=df_noz['r2'], frac=0.2)
    #    smoothed_b1_ew = sm.nonparametric.lowess(exog=df_noz['b1'], endog=df_noz['ew'], frac=0.2)


    eval_x = np.linspace(0, 1, 30)
    smoothed_b0_f1, bottom_b0_f1, top_b0_f1 = lowess_with_confidence_bounds(
        df_noz['b0'], df_noz['f1'], eval_x, lowess_kw={"frac": 1})
    smoothed_b0_auc, bottom_b0_auc, top_b0_auc = lowess_with_confidence_bounds(
        df_noz['b0'], df_noz['auc'], eval_x, lowess_kw={"frac": 1})
    smoothed_b0_r2, bottom_b0_r2, top_b0_r2 = lowess_with_confidence_bounds(
        df_noz['b0'], df_noz['r2'], eval_x, lowess_kw={"frac": 1})
    smoothed_b0_ew, bottom_b0_ew, top_b0_ew = lowess_with_confidence_bounds(
        df_noz['b0'], df_noz['ew'], eval_x, lowess_kw={"frac": 1})

    ax1.plot(eval_x, smoothed_b0_f1, color=colors[0])
    ax1.plot(eval_x, bottom_b0_f1, color=colors[0], alpha=0.5, linestyle='--')
    ax1.plot(eval_x, top_b0_f1, color=colors[0], alpha=0.5, linestyle='--')
    ax1.fill_between(eval_x, bottom_b0_f1, top_b0_f1, color=colors[0], alpha=0.25)
    ax1.plot(eval_x, smoothed_b0_auc, color=colors[0])
    ax1.plot(eval_x, bottom_b0_auc, color=colors[0], alpha=0.5, linestyle='--')
    ax1.plot(eval_x, top_b0_auc, color=colors[0], alpha=0.5, linestyle='--')
    ax1.fill_between(eval_x, bottom_b0_auc, top_b0_auc, color=colors[0], alpha=0.25)
    ax1.plot(eval_x, smoothed_b0_r2, color=colors[0])
    ax1.plot(eval_x, bottom_b0_r2, color=colors[0], alpha=0.5, linestyle='--')
    ax1.plot(eval_x, top_b0_r2, color=colors[0], alpha=0.5, linestyle='--')
    ax1.fill_between(eval_x, bottom_b0_r2, top_b0_r2, color=colors[0], alpha=0.25)
    ax1.plot(eval_x, smoothed_b0_ew, color=colors[1])
    ax1.plot(eval_x, bottom_b0_ew, color=colors[1], alpha=0.5, linestyle='--')
    ax1.plot(eval_x, top_b0_ew, color=colors[1], alpha=0.5, linestyle='--')
    ax1.fill_between(eval_x, bottom_b0_ew, top_b0_ew, color=colors[1], alpha=0.25)


    smoothed_b1_f1, bottom_b1_f1, top_b1_f1 = lowess_with_confidence_bounds(
        df_noz['b1'], df_noz['f1'], eval_x, lowess_kw={"frac": 1/3})
    smoothed_b1_auc, bottom_b1_auc, top_b1_auc = lowess_with_confidence_bounds(
        df_noz['b1'], df_noz['auc'], eval_x, lowess_kw={"frac": 1/3})
    smoothed_b1_r2, bottom_b1_r2, top_b1_r2 = lowess_with_confidence_bounds(
        df_noz['b1'], df_noz['r2'], eval_x, lowess_kw={"frac": 1/3})
    smoothed_b1_ew, bottom_b1_ew, top_b1_ew = lowess_with_confidence_bounds(
        df_noz['b1'], df_noz['ew'], eval_x, lowess_kw={"frac": 1/3})

    ax2.plot(eval_x, smoothed_b1_f1, color=colors[0])
    ax2.plot(eval_x, bottom_b1_f1, color=colors[0], alpha=0.5, linestyle='--')
    ax2.plot(eval_x, top_b1_f1, color=colors[0], alpha=0.5, linestyle='--')
    ax2.fill_between(eval_x, bottom_b1_f1, top_b1_f1, color=colors[0], alpha=0.25)
    ax2.plot(eval_x, smoothed_b1_auc, color=colors[0])
    ax2.plot(eval_x, bottom_b1_auc, color=colors[0], alpha=0.5, linestyle='--')
    ax2.plot(eval_x, top_b1_auc, color=colors[0], alpha=0.5, linestyle='--')
    ax2.fill_between(eval_x, bottom_b1_auc, top_b1_auc, color=colors[0], alpha=0.25)
    ax2.plot(eval_x, smoothed_b1_r2, color=colors[0])
    ax2.plot(eval_x, bottom_b1_r2, color=colors[0], alpha=0.5, linestyle='--')
    ax2.plot(eval_x, top_b1_r2, color=colors[0], alpha=0.5, linestyle='--')
    ax2.fill_between(eval_x, bottom_b1_r2, top_b1_r2, color=colors[0], alpha=0.25)
    ax2.plot(eval_x, smoothed_b1_ew, color=colors[1])
    ax2.plot(eval_x, bottom_b1_ew, color=colors[1], alpha=0.5, linestyle='--')
    ax2.plot(eval_x, top_b1_ew, color=colors[1], alpha=0.5, linestyle='--')
    ax2.fill_between(eval_x, bottom_b1_ew, top_b1_ew, color=colors[1], alpha=0.25)

    #    sns.regplot(x='b0', y='f1', ax=ax1, data=df_noz, scatter=False, ci=99.9, order=3,
    #                line_kws={'linewidth': 1, 'linestyle':'-'}, color=colors[0])
    #    sns.regplot(x='b0', y='auc', ax=ax1, data=df_noz, scatter=False, ci=99.9, order=3,
    #                line_kws={'linewidth': 1, 'linestyle':'-'}, color=colors[0])
    #    sns.regplot(x='b0', y='r2', ax=ax1, data=df_noz, scatter=False, ci=99.9, order=3,
    #                line_kws={'linewidth': 1, 'linestyle':'-'}, color=colors[0])
    #    sns.regplot(x='b0', y='ew', ax=ax1, data=df_noz, scatter=False, ci=99.9, order=3,
    #                line_kws={'linewidth': 1, 'linestyle':'-'}, color=colors[1])
    #
    #    sns.regplot(x='b1', y='f1', ax=ax2, data=df_noz, scatter=False, ci=99.9, order=3,
    #                line_kws={'linewidth': 1, 'linestyle':'-'}, color=colors[0])
    #    sns.regplot(x='b1', y='auc', ax=ax2, data=df_noz, scatter=False, ci=99.9, order=3,
    #                line_kws={'linewidth': 1, 'linestyle':'-'}, color=colors[0])
    #    sns.regplot(x='b1', y='r2', ax=ax2, data=df_noz, scatter=False, ci=99.9, order=3,
    #                line_kws={'linewidth': 1, 'linestyle':'-'}, color=colors[0])
    #    sns.regplot(x='b1', y='ew', ax=ax2, data=df_noz, scatter=False, ci=99.9, order=3,
    #                line_kws={'linewidth': 1, 'linestyle':'-'}, color=colors[1])

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


    ax1.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(4))
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
                              markerfacecolor=colors[1],
                              markeredgecolor='k',
                              color='w', label=r'IMV', linestyle='-'),
                       Line2D([0], [0], markersize=8, marker='s',
                              markerfacecolor=colors[0],
                              markeredgecolor='k',
                              color='w', label=r'Alternative Metric', linestyle='-'),]
    ax1.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize-1, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax2.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize-1, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)

    #sns.despine()
    #    plt.setp(ax1.collections[1], alpha=.285)
    #    plt.setp(ax1.collections[3], alpha=.285)
    #    plt.setp(ax1.collections[5], alpha=0.285)
    #    plt.setp(ax1.collections[7], alpha=0.285)
    #    plt.setp(ax2.collections[1], alpha=.285)
    #    plt.setp(ax2.collections[3], alpha=.285)
    #    plt.setp(ax2.collections[5], alpha=0.285)
    #    plt.setp(ax2.collections[7], alpha=0.285)

    plt.tight_layout(pad=5.0)
    plt.savefig(os.path.join(fig_path, fig_name), bbox_inches='tight')
