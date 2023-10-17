import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from big_fun import ll, get_w, get_ew, calc_r2

def plot_ffc_reeval(eval_df, fig_path, style_dict, fig_name):
    """Make the figure!"""
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    letter_fontsize = 26
#    mpl.rcParams['pdf.fonttype'] = 42
#    mpl.rcParams['ps.fonttype'] = 42
    label_fontsize = 19

    fig = plt.figure(figsize=(14, 12), tight_layout=False)
    ax1 = plt.subplot2grid((2, 3), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2, 3), (0, 1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((2, 3), (0, 2), rowspan=1, colspan=1)

    eval_df['r2_sub'] = eval_df['r2_sub'].astype(float)
    test = eval_df[(eval_df['r2_sub'] > 0)]
    layoff = test[test['outcome'] == 'layoff']
    jobTraining = test[test['outcome'] == 'jobTraining']
    eviction = test[test['outcome'] == 'eviction']

#    ax1.scatter(x=layoff['r2_sub'].astype(float), y=layoff['ew_sub_vs_prev'].astype(float),
#                linewidth=1,linestyle='-',
#                facecolor = ([29/255, 28/255, 84/255, 0.45]), s=75,
#                edgecolor = ([29/255, 28/255, 84/255, 1]))
    ax1.scatter(x=layoff['r2_sub'].astype(float),
                y=layoff['ew_sub_vs_LPM'].astype(float),
                linewidth=1,linestyle='-',
                #facecolor = ([232/255, 152/255, 24/255, 0.45]), s=75,
                #edgecolor = ([232/255, 152/255, 24/255, 1])
                facecolor = style_dict['colours'][0], s=75, alpha=0.75,
                edgecolor = 'k'
                )


#    ax2.scatter(x=jobTraining['r2_sub'].astype(float), y=jobTraining['ew_sub_vs_prev'].astype(float),
#                linewidth=1, linestyle='-',
#                facecolor = ([29/255, 28/255, 84/255, 0.45]), s=75,
#                edgecolor = ([29/255, 28/255, 84/255, 1]))
    ax2.scatter(x=jobTraining['r2_sub'].astype(float),
                y=jobTraining['ew_sub_vs_LPM'].astype(float),
                linewidth=1,linestyle='-',
                facecolor = style_dict['colours'][0], s=75, alpha=0.75,
                edgecolor = 'k'
                )

#    ax3.scatter(x=eviction['r2_sub'].astype(float), y=eviction['ew_sub_vs_prev'].astype(float),
#                linewidth=1, linestyle='-',
#                facecolor = ([29/255, 28/255, 84/255, 0.45]), s=75,
#                edgecolor = ([29/255, 28/255, 84/255, 1]))
    ax3.scatter(x=eviction['r2_sub'].astype(float),
                y=eviction['ew_sub_vs_LPM'].astype(float),
                linewidth=1,linestyle='-',
                #facecolor = ([232/255, 152/255, 24/255, 0.45]), s=75,
                #edgecolor = ([232/255, 152/255, 24/255, 1])
                facecolor = style_dict['colours'][0], s=75, alpha=0.75,
                edgecolor = 'k'
                )

    ax2.set_ylabel('')
    ax3.set_ylabel('')
    ax1.set_title(r'A.', fontsize=letter_fontsize,
                  loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=letter_fontsize,
                  loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=letter_fontsize,
                  loc='left', x=-.05, **csfont, y=1.025)
    ax1.set_xlabel(r'Pseudo R$^2$', **csfont, fontsize=label_fontsize)
    ax2.set_xlabel(r'Pseudo R$^2$', **csfont, fontsize=label_fontsize)
    ax3.set_xlabel(r'Pseudo R$^2$', **csfont, fontsize=label_fontsize)
    ax1.set_ylabel(r'IMV (Layoff)', **csfont, fontsize=label_fontsize)
    ax2.set_ylabel(r'IMV (Job Training)', **csfont, fontsize=label_fontsize)
    ax3.set_ylabel(r'IMV (Eviction)', **csfont, fontsize=label_fontsize)

    ymin = np.min(np.array([ax1.get_ylim()[0], ax2.get_ylim()[0], ax3.get_ylim()[0]]))
    ymax = np.max(np.array([ax1.get_ylim()[1], ax2.get_ylim()[1], ax3.get_ylim()[1]]))
    xmin = np.min(np.array([ax1.get_xlim()[0], ax2.get_xlim()[0], ax3.get_xlim()[0]]))
    xmax = np.max(np.array([ax1.get_xlim()[1], ax2.get_xlim()[1], ax3.get_xlim()[1]]))

    #ax1.spines['bottom'].set_bounds(0, ax1.get_xlim()[1])
    #ax1.spines['left'].set_bounds(-.005, ax1.get_ylim()[1])
    #ax2.spines['bottom'].set_bounds(0, ax2.get_xlim()[1])
    #ax2.spines['left'].set_bounds(-.03, ax2.get_ylim()[1])

    #ax3.spines['bottom'].set_bounds(0, ax3.get_xlim()[1])
    #ax3.spines['left'].set_bounds(-.003, ax3.get_ylim()[1])

#    ax1.vlines(0.008366, ax1.get_ylim()[0], ax1.get_ylim()[1],
#               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)
#    ax1.hlines(0.003953, ax1.get_xlim()[0], ax1.get_xlim()[1],
#               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)
#    ax2.vlines(0.049448, ax2.get_ylim()[0], ax2.get_ylim()[1],
#               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)
#    ax2.hlines(0.0280576, ax2.get_xlim()[0], ax2.get_xlim()[1],
#               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)
#    ax3.vlines(0.014316, ax3.get_ylim()[0], ax3.get_ylim()[1],
#               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)
#    ax3.hlines(0.00265, ax3.get_xlim()[0], ax3.get_xlim()[1],
#               linestyle=[(0, (10, 10, 10, 10))], color='k', linewidth=0.5, alpha=0.5)

#    legend_elements = [#Line2D([0], [0], markersize=8, marker='o',
#                       #       markerfacecolor=([29/255, 63/255, 110/255, 0.45]),
#                       #       markeredgecolor=([29/255, 63/255, 110/255, 1]),
#                       #       label=r'w$_0$ = $\bar{y}_{\mathrm{Train}}$', linestyle='none'),
#                       Line2D([0], [0], markersize=8, marker='o',
#
#                              markerfacecolor=([29 / 255, 28 / 255, 84 / 255, 0.45]),# s=75,
#                              markeredgecolor=([29 / 255, 28 / 255, 84 / 255, 1]),
#                              markerfacecolor=([232/255, 152/255, 24/255, 0.45]),
#                              markeredgecolor=([232/255, 152/255, 24/255, 1]),
#                              label=r'w$_0$ = bench', linestyle='none')]
#    ax3.legend(handles=legend_elements, loc='lower right', frameon=True,
#               fontsize=label_fontsize-2, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
#
#    ax1.annotate(r'Pseudo R$^2$: bench',
#                 xy=(0.0085, -.0225), xycoords='data', **csfont,
#                 xytext=(0.0105, -0.022), fontsize=14, textcoords='data',
#                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=-0.25", linewidth=0.5,
#                                 edgecolor='k'))
#
#    ax1.annotate(r'E(W): bench vs. $\widebar{y}_{\mathrm{Train}}$',
#                 xy=(0.0275, 0.0037), xycoords='data', **csfont,
#                 xytext=(0.0105, -0.012), fontsize=14, textcoords='data',
#                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3, rad=0.25", linewidth=0.5,
#                                 edgecolor='k'))
    at = AnchoredText(r'$\widebar{y}_{\mathrm{Train}}$ = 0.209',
                      prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax1.add_artist(at)
    at = AnchoredText(r'$\widebar{y}{_\mathrm{Train}}$ = 0.235',
                      prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax2.add_artist(at)
    at = AnchoredText(r'$\widebar{y}_{\mathrm{Train}}$ = 0.060',
                      prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax3.add_artist(at)

    increment = 10
    for axx in [ax1, ax2, ax3]:
        axx.yaxis.grid(linestyle='--', alpha=0.2)
        axx.xaxis.grid(linestyle='--', alpha=0.2)
        axx.yaxis.set_major_locator(plt.MaxNLocator(5))
        axx.tick_params(axis='both', which='major', labelsize=17)
        axx.set_ylim(ymin+(ymin/increment), ymax+(ymax/increment))
        axx.set_xlim(xmin-0.01, xmax+(xmin/increment))

    sns.despine(trim=True)
    plt.tight_layout(pad=1.5)
    plt.savefig(os.path.join(fig_path, fig_name), bbox_inches='tight')


def build_df(prob_subm):
    eval_df = pd.DataFrame(columns=['outcome', 'account', 'prev', 'r2_LPM', 'r2_sub',
                                    'a_prev', 'a0', 'a1', 'wprev', 'w0', 'w1',
                                    'ew_LPM_vs_prev', 'ew_sub_vs_LPM', 'ew_sub_vs_prev'])
    indexer = 0
    for outcome in prob_subm['outcome'].unique():
        for account in prob_subm[prob_subm['outcome'] == outcome]['account'].\
                sort_values(ascending=False).unique():
            temp = prob_subm[(prob_subm['outcome'] == outcome) &
                             (prob_subm['account'] == account)]
            eval_df.at[indexer, 'outcome'] = outcome
            eval_df.at[indexer, 'account'] = account
            ybar_train = temp['ybar_train'].unique()[0]  # eyeball and unit test
            # prev = temp['truth'].mean()
            prev = ybar_train  # ask ben about this
            sub_pred = temp['prediction']
            lpm_pred = temp['prediction_LPM']
            truth = temp['truth']
            eval_df.at[indexer, 'prev'] = prev
            eval_df.at[indexer, 'r2_LPM'] = calc_r2(truth, lpm_pred, ybar_train)
            eval_df.at[indexer, 'r2_sub'] = calc_r2(truth, sub_pred, ybar_train)
            eval_df.at[indexer, 'a_prev'] = ll(truth, prev)
            eval_df.at[indexer, 'a0'] = ll(truth, lpm_pred)
            eval_df.at[indexer, 'a1'] = ll(truth, sub_pred)
            eval_df.at[indexer, 'wprev'] = get_w(ll(truth, prev))
            eval_df.at[indexer, 'w0'] = get_w(ll(truth, lpm_pred))
            eval_df.at[indexer, 'w1'] = get_w(ll(truth, sub_pred))
            eval_df.at[indexer, 'ew_LPM_vs_prev'] = get_ew(get_w(ll(truth, prev)),
                                                           get_w(ll(truth, lpm_pred)))
            eval_df.at[indexer, 'ew_sub_vs_prev'] = get_ew(get_w(ll(truth, prev)),
                                                           get_w(ll(truth, sub_pred)))
            eval_df.at[indexer, 'ew_sub_vs_LPM'] = get_ew(get_w(ll(truth, lpm_pred)),
                                                          get_w(ll(truth, sub_pred)))
            indexer = indexer + 1
        outcome_df = eval_df[eval_df['outcome'] == outcome]
        outcome_positive = outcome_df[outcome_df['r2_sub'].astype(float)>0].copy()
        outcome_positive.loc[:, 'incremental'] = outcome_positive['r2_sub'] -\
                                                 outcome_positive['r2_LPM']
        print('We have ' + str(len(outcome_df)) +\
              ' submissions for ' + outcome)
        print('We have ' + str(len(outcome_df[outcome_df['r2_sub'] > 0])) +\
              ' submissions for ' +
              outcome + ' which have an r2>0')
        print('The min E(w) for ' + outcome + ' vs prev is ' +\
              str(outcome_df['ew_sub_vs_prev'].min()))
        print('The min E(w) for ' + outcome + ' vs benchmark is ' +\
              str(outcome_df['ew_sub_vs_LPM'].min()))
        print('The max E(w) for ' + outcome + ' vs prev is ' +\
              str(outcome_df['ew_sub_vs_prev'].max()))
        print('The max E(w) for ' + outcome + ' vs benchmark is ' +\
              str(outcome_df['ew_sub_vs_LPM'].max()))
        print('The E(w) for ' + outcome + ' of benchmark vs prev is :' +\
              str(outcome_df['ew_LPM_vs_prev'].unique()[0]))
        print('The max R2 for ' + outcome + ' vs prev is :' +\
              str(outcome_df['r2_sub'].max()))
        print('The R2 for ' + outcome + ' of benchmark is :' +\
              str(outcome_df['r2_LPM'].unique()[0]))
        print('The diff between R2 of bestr submission for ' +\
              outcome + ' vs benchmark is :' + str(outcome_df['r2_sub'].max() -\
                                                   outcome_df['r2_LPM'].unique()[0]))
        print('Spearmans Rho for incremental r2 and ew for ' +\
              outcome + ': ' +
              str(outcome_positive['incremental'].astype('float64').\
                  corr(outcome_positive['ew_sub_vs_LPM'].astype('float64'))))
    eval_df.to_csv(os.path.join(os.getcwd(), '..', 'data',
                                'FFC', 'processed',
                                'processed_FFC_data.csv'))
    return eval_df


def clean_subm(subm):
    """clean for subm"""
    temp_subm = subm.copy()
    temp_subm_list = []
    for account in temp_subm['account'].unique():
        for outcome in temp_subm['outcome'].unique():
            temp = temp_subm[(temp_subm['outcome'] == outcome) &
                             (temp_subm['account'] == account)]
            if (temp['prediction'].max() <= 1) and (temp['prediction'].min() >= 0):
                temp_subm_list.append(temp)
    temp_subm = pd.concat(temp_subm_list)
    return temp_subm


def clean_prob_subm(subm):
    """clean for subm"""
    prob_subm = subm.copy()
    prob_subm_list = []
    for account in subm['account'].unique():
        for outcome in subm['outcome'].unique():
            temp = subm[(subm['outcome'] == outcome) &
                        (subm['account'] == account)]
            if (len(temp[(temp['prediction'] > 0) &
                         (temp['prediction'] < 1)]) > 0) and \
                    (temp['prediction'].max() < 1) and \
                    (temp['prediction'].min() > 0):
                prob_subm_list.append(temp)
    prob_subm = pd.concat(prob_subm_list)
    return prob_subm


def load_data(data_dir):
    """Load the FFC data"""
    subm = pd.read_csv(os.path.join(data_dir, 'private',
                                    'submissions.csv'),
                       low_memory=False)
    bench = pd.read_csv(os.path.join(data_dir,
                                     'intermediate_files',
                                     'benchmarks_long.csv'),
                        low_memory=False)
    return subm, bench


def preprocess_data(subm, bench):
    """DOCSTRINGS here"""
    # Drop the bench for only things we're interested in
    bench = bench[(bench['account'] == 'benchmark_logit_full') &
                  (bench['prediction'].notnull()) &
                  (bench['truth'].notnull())]
    # Couple of 'does it smell right' checks on bench:
    print('Check len(bench) is (i.e. 1013 + 994 + 1104): ', len(bench))
    print('Check max IDs for any outcome (1104): ',
          len(bench['challengeID'].unique()))
    subm = subm[subm['truth'].notnull()]
    # Drop the submissions for only things we're interested in
    subm = subm[subm['outcome_name'].str.contains('D.') |
                subm['outcome_name'].str.contains('E.') |
                subm['outcome_name'].str.contains('F.') &
                (subm['prediction'].notnull())]
    # Couple of 'does it smell right' checks on subm:
    print('Check max IDs used across all team\outcome (1104): ',
          len(subm['challengeID'].unique()))
    print('Number of accounts in the subm file: ', len(subm['account'].unique()))
    subm = clean_subm(subm)
    prob_subm = clean_prob_subm(subm)
    # nb overwriting this as LPM rather than logit in their account field
    bench = bench.rename({'prediction': 'prediction_LPM'}, axis=1)
    prob_subm = pd.merge(prob_subm, bench[['outcome_name',
                                           'challengeID',
                                           'prediction_LPM']],
                         how='left', left_on=['outcome_name', 'challengeID'],
                         right_on=['outcome_name', 'challengeID'])
    subm = pd.merge(subm, bench[['outcome_name',
                                 'challengeID',
                                 'prediction_LPM']],
                    how='left', left_on=['outcome_name', 'challengeID'],
                    right_on=['outcome_name', 'challengeID'])
    return subm, prob_subm, bench


def plot_ffc(fig_path, data_dir, style_dict, fig_name):
    data_dir = os.path.join(data_dir, 'FFC')
    subm, bench = load_data(data_dir)
    subm, prob_subm, bench = preprocess_data(subm, bench)
    eval_df = build_df(prob_subm)
    plot_ffc_reeval(eval_df, fig_path, style_dict, fig_name)
