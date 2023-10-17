import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnchoredText

def plot_se_vs_sd(fig_path, data_path, style_dict, fig_name):

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14,12))
    df1 = pd.read_csv(os.path.join(data_path, 'sims',
                                   'se_vs_sd', 'se_vs_sd_1.csv'))
    df2 = pd.read_csv(os.path.join(data_path, 'sims',
                                   'se_vs_sd', 'se_vs_sd_2.csv'))
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}

    eval_x = np.linspace(0, 10000, 10000)
#    smoothed_df1_N_se, bottom_df1_N_se, top_df1_N_se = lowess_with_confidence_bounds(
#        df1['N'], df1['se'], eval_x, lowess_kw={"frac": 1/3})
#    smoothed_df1_N_omsd, bottom_df1_N_omsd, top_df1_N_omsd = lowess_with_confidence_bounds(
#        df1['N'], df1['om.sd'], eval_x, lowess_kw={"frac": 1/3})
#    smoothed_df2_N_se, bottom_df2_N_se, top_df2_N_se = lowess_with_confidence_bounds(
#        df2['N'], df2['se'], eval_x, lowess_kw={"frac": 1/3})
#    smoothed_df2_N_omsd, bottom_df2_N_omsd, top_df2_N_omsd = lowess_with_confidence_bounds(
#        df2['N'], df2['om.sd'], eval_x, lowess_kw={"frac": 1/3})

    ax1.scatter(df1['N'], df1['se'], s=100, color=style_dict['colours'][0],
                marker='o', alpha=1, facecolor='w')
    ax2.scatter(df1['N'], df1['se'], s=100, color=style_dict['colours'][0],
                marker='o', alpha=1, facecolor='w')
    ax3.scatter(df2['N'], df2['se'], s=100, color=style_dict['colours'][1],
                marker='o', alpha=1, facecolor='w')
    ax4.scatter(df2['N'], df2['om.sd'], s=100, color=style_dict['colours'][1],
                marker='o', alpha=1, facecolor='w')
    ax1.tick_params(axis='both', which='major', labelsize=14)
    ax2.tick_params(axis='both', which='major', labelsize=14)
    ax3.tick_params(axis='both', which='major', labelsize=14)
    ax4.tick_params(axis='both', which='major', labelsize=14)
    ax1.set_ylim(-.02, .32)
    ax2.set_ylim(-.02, .32)
    ax3.set_ylim(-.02, .32)
    ax4.set_ylim(-.02, .32)
    ax1.set_xlim(-500, 10500)
    ax2.set_xlim(-500, 10500)
    ax3.set_xlim(-500, 10500)
    ax4.set_xlim(-500, 10500)
    ax1.set_axisbelow(True)
    ax1.grid(linestyle='--', linewidth='1', alpha=0.4)
    ax2.set_axisbelow(True)
    ax2.grid(linestyle='--', linewidth='1', alpha=0.4)
    ax3.set_axisbelow(True)
    ax3.grid(linestyle='--', linewidth='1', alpha=0.4)
    ax4.set_axisbelow(True)
    ax4.grid(linestyle='--', linewidth='1', alpha=0.4)
    ax1.set_title(r'A.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax4.set_title(r'D.', fontsize=22, loc='left', x=-.05, **csfont, y=1.025)
    ax1.set_ylabel(r'Standard Error', **csfont, fontsize=16)
    ax1.set_xlabel(r'N', **csfont, fontsize=16)
    ax2.set_ylabel(r'SD ($\omega$)', **csfont, fontsize=16)
    ax2.set_xlabel(r'N', **csfont, fontsize=16)
    ax3.set_ylabel(r'Standard Error', **csfont, fontsize=16)
    ax3.set_xlabel(r'N', **csfont, fontsize=16)
    ax4.set_ylabel(r'SD ($\omega$)', **csfont, fontsize=16)
    ax4.set_xlabel(r'N', **csfont, fontsize=16)
    at = AnchoredText(r"$\beta$=0.1", prop=dict(size=15), frameon=True, loc='upper right')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax1.add_artist(at)
    at2 = AnchoredText(r"$\beta$=0.1", prop=dict(size=15), frameon=True, loc='upper right')
    at2.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax2.add_artist(at2)
    at3 = AnchoredText(r"$\beta$=0.5", prop=dict(size=15), frameon=True, loc='upper right')
    at3.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax3.add_artist(at3)
    at4 = AnchoredText(r"$\beta$=0.5", prop=dict(size=15), frameon=True, loc='upper right')
    at4.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax4.add_artist(at4)
    plt.subplots_adjust(wspace=0.3, hspace=0.275)
    plt.savefig(os.path.join(fig_path, fig_name), bbox_inches='tight')