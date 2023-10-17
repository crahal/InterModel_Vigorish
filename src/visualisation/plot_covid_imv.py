import os
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from scipy.stats.stats import pearsonr
from matplotlib.offsetbox import AnchoredText
warnings.simplefilter(action='ignore', category=FutureWarning)


def plot_covid_imv(fig_path, data_path, style_dict, fig_name):
    df1 = pd.read_csv(os.path.join(data_path, 'symptomtracker',
                                   'results_2020-04-24_imv_small_firstwave_100folds_noseeds_stratified.csv'),
                      index_col=0)
    df1 = df1.rename({'imv': 'firstwave_smallmodel'}, axis=1)

    df2 = pd.read_csv(os.path.join(data_path, 'symptomtracker',
                                   'results_2020-04-24_imv_compared_firstwave_100folds_noseeds_stratified.csv'),
                      index_col=0)
    df2 = df2.rename({'imv': 'firstwave_compared'}, axis=1)

    df3 = pd.read_csv(os.path.join(data_path, 'symptomtracker',
                                   'results_2021-03-24_imv_small_firstyear_100folds_noseeds_stratified.csv'),
                      index_col=0)
    df3 = df3.rename({'imv': 'firstyear_smallmodel'}, axis=1)

    df4 = pd.read_csv(os.path.join(data_path, 'symptomtracker',
                                   'results_2021-03-24_imv_compared_firstyear_100folds_noseeds_stratified.csv'),
                      index_col=0)
    df4 = df4.rename({'imv': 'firstyear_compared'}, axis=1)

    df5 = pd.read_csv(os.path.join(data_path, 'symptomtracker',
                                   'results_2021-03-24_imv_full_firstyear_100folds_noseeds_stratified.csv'),
                      index_col=0)
    df5 = df5.rename({'imv': 'firstyear_fullmodel'}, axis=1)

    df6 = pd.read_csv(os.path.join(data_path, 'symptomtracker',
                                   'results_2020-04-24_imv_full_firstwave_100folds_noseeds_stratified.csv'),
                      index_col=0)
    df6 = df6.rename({'imv': 'firstwave_fullmodel'}, axis=1)

    roc_data = pd.read_csv(os.path.join(data_path, 'symptomtracker',
                                        'results_2020-04-24_rocauc_small_firstwave_100folds_noseeds_stratified.csv'),
                           index_col=0)

    roc_data = roc_data.rename({'roc': 'firstyear_roc'}, axis=1)

    #imv_data = pd.read_csv(os.path.join(os.getcwd(), '..', 'data', 'imv_data.csv'), index_col='fold')
    imv_data = pd.merge(df1, df2, left_index=True, right_index=True)
    imv_data = pd.merge(imv_data, df3, left_index=True, right_index=True)
    imv_data = pd.merge(imv_data, df4, left_index=True, right_index=True)
    imv_data = pd.merge(imv_data, df5, left_index=True, right_index=True)
    imv_data = pd.merge(imv_data, df6, left_index=True, right_index=True)

    imv_data1 = pd.DataFrame(index=range(0, 400), columns = ['IMV', 'Model', 'Date'])

    imv_data1.loc[0:99, 'IMV'] = imv_data['firstwave_smallmodel'].tolist()
    imv_data1.loc[0:99, 'Model'] = 'Small Model'
    imv_data1.loc[0:99, 'Date'] = 'First Wave'

    imv_data1.loc[100:199, 'IMV'] = imv_data['firstyear_smallmodel'].tolist()
    imv_data1.loc[100:199, 'Model'] = 'Small Model'
    imv_data1.loc[100:199, 'Date'] = 'First Year'

    imv_data1.loc[200:299, 'IMV'] = imv_data['firstyear_fullmodel'].tolist()
    imv_data1.loc[200:299, 'Model'] = 'Large Model'
    imv_data1.loc[200:299, 'Date'] = 'First Year'

    imv_data1.loc[300:399, 'IMV'] = imv_data['firstwave_fullmodel'].tolist()
    imv_data1.loc[300:399, 'Model'] = 'Large Model'
    imv_data1.loc[300:399, 'Date'] = 'First Wave'

    imv_data1['IMV'] = imv_data1['IMV'].astype(float)


    fig, ((ax1, ax2)) = plt.subplots(1, 2, figsize=(16, 8.5))
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    letter_fontsize = 24
    label_fontsize = 18
    nbins=15
    colors = style_dict['colours']


    sns.regplot(y=roc_data['roc_auc'],
                x=imv_data['firstwave_smallmodel'],
                scatter_kws = {'color': colors[1],
                               'edgecolor': 'k',
                               's': 0},
                line_kws = {'color': 'w',
                            'lw': 0,
                            }, ci=95, ax=ax1)
    ax1.collections[1].set_edgecolor(c=(0,0,0,1))
    ax1.collections[1].set_alpha(1)


    ax1.tick_params(axis='both', which='major', labelsize=16)

    sns.regplot(y=roc_data['roc_auc'],
                x=imv_data['firstwave_smallmodel'],
                scatter_kws = {'color': colors[1],
                               'edgecolor': colors[0],
                               's': 150,
                               'alpha':1},
                line_kws = {'color': colors[0],
                            'lw':1.5, 'alpha':1,
                            'linestyle': '--'}, ci=0, ax=ax1)


    legend_elements1 = [Patch(facecolor='w', edgecolor='#000000',
                              label='95% CI'),
                        Line2D([0], [0], color=colors[0], lw=2, linestyle='--',
                               label=r'Best Fit', alpha=0.85),
                        Line2D([], [], color="white", marker='o', markerfacecolor=colors[1],
                               label='Individual Fold', markersize=15, markeredgecolor='k')
                        ]

    ax1.legend(handles=legend_elements1, loc='upper left', frameon=True,
               fontsize=label_fontsize-4, framealpha=1, facecolor='w',
               edgecolor=(0, 0, 0, 1),
               ncol=1,
               #title='IMV(Prevalence, Small Model)',
               #title_fontsize=label_fontsize-5
               )
    ax1.set_xlabel('IMV Across Folds', fontsize=label_fontsize+2)
    ax1.set_ylabel('ROC-AUC Across Folds', fontsize=label_fontsize+2)
    ax1.grid(linestyle='--', linewidth='1', alpha=0.4)
    ax1.set_xlim(-.3, .3)
    ax1.set_ylim(.3, 1)

    at = AnchoredText(
        r"Pearson's $r$="+str(round((pearsonr(roc_data['roc_auc'],imv_data['firstwave_smallmodel'])[0]),3)) , prop=dict(size=15), frameon=True, loc='lower right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax1.add_artist(at)

    from PIL import ImageColor
    from matplotlib.collections import PolyCollection

    my_color1 = (65/255, 85/255, 140/255, 0.1)
    my_color2 = (232/255, 152/255, 24/255, 0.1)

    sns.violinplot(
        data=imv_data1, y="IMV", x="Date", hue="Model",
        bw=.25, cut=0, split=True, ax=ax2, inner='box',
        palette={'Small Model': my_color1, 'Large Model': my_color2},
    )
    for violin in ax2.collections:
        violin.set_alpha(0.8)

    ax2.legend(loc='upper right', frameon=True,
               fontsize=label_fontsize-4, framealpha=1, facecolor='w',
               edgecolor=(0, 0, 0, 1),
               ncol=1,
               #title='IMV(Prevalence, Small Model)',
               #title_fontsize=label_fontsize-5
               )



    ax2.tick_params(axis='both', which='major', labelsize=18)
    ax2.set_ylabel('IMV Across Folds', fontsize=label_fontsize+2)
    ax2.grid(linestyle='--', linewidth='1', alpha=0.4)
    ax2.set_ylim(-.3, .3)


    ax2.set_xlabel("")

    ax1.set_title('A.', loc='left', fontsize=letter_fontsize, y=1.025)
    ax2.set_title('B.', loc='left', fontsize=letter_fontsize, y=1.025)


    sns.despine()
    plt.tight_layout()
    plt.subplots_adjust(hspace = .1, wspace=0.2)
    plt.savefig(os.path.join(fig_path, fig_name))