import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnchoredText

def plot_linear_v_quadratic(fig_path, data_path, style_dict, fig_name):
    m1x = pd.read_csv(os.path.join(data_path, 'sims',
                                   'linear_v_quadratic', 'm1x.csv'))
    fitted_m1 = pd.read_csv(os.path.join(data_path, 'sims',
                                         'linear_v_quadratic', 'm1_fitted.csv'))
    m2x = pd.read_csv(os.path.join(data_path, 'sims',
                                   'linear_v_quadratic', 'm2x.csv'))
    fitted_m2 = pd.read_csv(os.path.join(data_path, 'sims',
                                         'linear_v_quadratic', 'm2_fitted.csv'))
    fig, ax1 = plt.subplots(figsize=(14, 7), tight_layout=True)
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    colors = style_dict['colours']
    ax1.plot(m1x['z[, 1]'], fitted_m1['x'], color=style_dict['colours'][0],
             linewidth=style_dict['line_width'])
    ax1.plot(m2x['z[, 1]'], fitted_m2['x'], color=style_dict['colours'][1],
             linewidth=style_dict['line_width'])

    ax1.xaxis.grid(linestyle='--', alpha=0.25)
    ax1.yaxis.grid(linestyle='--', alpha=0.25)
    ax1.set_xlim(0, 2500)
    ax1.set_ylim(-0.02, 0.025)
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.set_ylabel('IMV', csfont, fontsize=22);
    ax1.set_xlabel('Sample Size', csfont, fontsize=22);

    legend_elements = [Line2D([0], [0], markersize=14, marker='s',
                       markerfacecolor=colors[1],
                       markeredgecolor='k',
                       color='w', label=r'Out-of-sample data', linestyle='-'),
                       Line2D([0], [0], markersize=14, marker='s',
                       markerfacecolor=colors[0],
                       markeredgecolor='k',
                       color='w', label=r'In-sample data', linestyle='-')]
    ax1.axhline(y=0, color='k', linestyle='--')
    ax1.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax1.legend(handles=legend_elements, loc='lower right', frameon=True,
               fontsize=18, framealpha=1, facecolor='w', edgecolor='k', handletextpad=0.25,
               title='    IMV comparing linear\nand quadratic fit based on:', title_fontsize=20)
    plt.savefig(os.path.join(fig_path, fig_name))