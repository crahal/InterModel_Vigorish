import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FixedLocator, FormatStrFormatter


def plot_p0_v_p1(fig_path, data_path, style_dict, fig_name):
    colors = style_dict['colours']
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    letter_fontsize = 24
    label_fontsize = 18
    data_path = os.path.join(data_path, 'sims', 'p0_v_p1')

    dfm0 = pd.read_csv(os.path.join(data_path, 'omega_m_0.csv'))
    dfpm0 = pd.read_csv(os.path.join(data_path, 'omega_pm_0.csv'))
    dfm1 = pd.read_csv(os.path.join(data_path, 'omega_m_1.csv'))
    dfpm1 = pd.read_csv(os.path.join(data_path, 'omega_pm_1.csv'))
    dfm2 = pd.read_csv(os.path.join(data_path, 'omega_m_2.csv'))
    dfpm2 = pd.read_csv(os.path.join(data_path, 'omega_pm_2.csv'))
    dfm3 = pd.read_csv(os.path.join(data_path, 'omega_m_3.csv'))
    dfpm3 = pd.read_csv(os.path.join(data_path, 'omega_pm_3.csv'))
    dfm4 = pd.read_csv(os.path.join(data_path, 'omega_m_4.csv'))
    dfpm4 = pd.read_csv(os.path.join(data_path, 'omega_pm_4.csv'))
    dfm5 = pd.read_csv(os.path.join(data_path, 'omega_m_5.csv'))
    dfpm5 = pd.read_csv(os.path.join(data_path, 'omega_pm_5.csv'))
    dfm6 = pd.read_csv(os.path.join(data_path, 'omega_m_6.csv'))
    dfpm6 = pd.read_csv(os.path.join(data_path, 'omega_pm_6.csv'))
    dfm7 = pd.read_csv(os.path.join(data_path, 'omega_m_7.csv'))
    dfpm7 = pd.read_csv(os.path.join(data_path, 'omega_pm_7.csv'))

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 12))
    ax1.plot(dfm0['x'], dfpm0['fitted'],
             color=style_dict['colours'][0],
             lw=style_dict['line_width'], linestyle='--')
    ax1.plot(dfm1['x'], dfpm1['fitted'],
             color=style_dict['colours'][1],
             lw=style_dict['line_width'], linestyle='-')
    ax1.set_ylim(-0.1, 1)
    ax2.plot(dfm2['x'], dfpm2['fitted'],
             color=style_dict['colours'][0],
             lw=style_dict['line_width'], linestyle='--')
    ax2.plot(dfm3['x'], dfpm3['fitted'],
             color=style_dict['colours'][1],
             lw=style_dict['line_width'], linestyle='-')
    ax2.set_ylim(-0.1, 1)
    ax3.plot(dfm4['x'], dfpm4['fitted'],
             color=style_dict['colours'][0],
             lw=style_dict['line_width'], linestyle='--')
    ax3.plot(dfm5['x'], dfpm5['fitted'],
             color=style_dict['colours'][1],
             lw=style_dict['line_width'], linestyle='-')
    ax3.set_ylim(-0.1, 1)
    ax4.plot(dfm6['x'], dfpm6['fitted'],
             color=style_dict['colours'][0],
             lw=style_dict['line_width'], linestyle='--')
    ax4.plot(dfm7['x'], dfpm7['fitted'],
             color=style_dict['colours'][1],
             lw=style_dict['line_width'], linestyle='-')
    ax4.set_ylim(-0.1, 1)

    for ax in [ax1, ax2, ax3, ax4]:
        ax.xaxis.set_major_locator(plt.MaxNLocator(5))
        ax.yaxis.set_major_locator(plt.MaxNLocator(4))
        ax.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=18)
        ax.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=18)
        ax.set_xlabel(r'$\psi$', fontsize=label_fontsize+4, **csfont)
        ax.grid(linestyle='--', alpha=0.25, axis='both')
        ax.set_xlim(-0.01, 0.21)
        ax.hlines(xmin=-0.01, xmax = 0.21, y=0, color='k', linestyle='-')
    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax3.set_title(r'C.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax4.set_title(r'D.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax1.set_ylabel(r'R$^2$', fontsize=label_fontsize+4, **csfont)
    ax2.set_ylabel(r'F1', fontsize=label_fontsize+4, **csfont)
    ax3.set_ylabel(r'AUC', fontsize=label_fontsize+4, **csfont)
    ax4.set_ylabel(r'IMV', fontsize=label_fontsize+4, **csfont)
    legend_elements = [Line2D([0], [0], markersize=0, marker='s',
                              markerfacecolor=colors[1],
                              markeredgecolor='k',
                              lw=2,
                              color=colors[1], label=r'p', linestyle='-'),
                       Line2D([0], [0], markersize=0, marker='s',
                              markerfacecolor=colors[0],
                              lw=2,
                              markeredgecolor='k',
                              color=colors[0], label=r'p1', linestyle='--'),]
    ax1.legend(handles=legend_elements, loc='upper left', frameon=True,# title='$\omega$',title_fontsize=22,
               fontsize=label_fontsize+1, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25)
    plt.tight_layout(pad=2.5)
    plt.savefig(os.path.join(fig_path, fig_name), bbox_inches='tight')