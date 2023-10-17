import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def plot_prev_b0_v_b1(fig_path, data_path, style_dict, fig_name):
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    letter_fontsize = 26
    mpl.rcParams['pdf.fonttype'] = 42
    mpl.rcParams['ps.fonttype'] = 42
    label_fontsize = 19
    df1 = pd.read_csv(os.path.join(data_path, 'sims', 'prev_b0_v_b1', 'df1.csv'))
    df2 = pd.read_csv(os.path.join(data_path, 'sims', 'prev_b0_v_b1', 'df2.csv'))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
    ax1.plot(df2['b0'], df2['b1'], color=style_dict['colours'][1], linestyle='-', linewidth=style_dict['line_width'])
    ax1.plot(df1['b0'], df1['b1'], color=style_dict['colours'][0], linestyle='--', linewidth=style_dict['line_width'])
    ax2.plot(df2['b1'], df2['r2'], color=style_dict['colours'][1], linestyle='-', linewidth=style_dict['line_width'])
    ax2.plot(df1['b1'], df1['r2'], color=style_dict['colours'][0], linestyle='--', linewidth=style_dict['line_width'])
    ax1.tick_params(axis='both', which='major', labelsize=16)
    ax2.tick_params(axis='both', which='major', labelsize=16)
    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1.025)

    ax1.set_xlabel(r'$\mathrm{\beta}_0$', **csfont, fontsize=label_fontsize)
    ax1.set_ylabel(r'$\mathrm{\beta}_1$', **csfont, fontsize=label_fontsize)
    ax2.set_xlabel(r'$\mathrm{\beta}_1$', **csfont, fontsize=label_fontsize)
    ax2.set_ylabel(r'$\mathrm{R}^2$', **csfont, fontsize=label_fontsize)
    ax1.yaxis.grid(linestyle='--', alpha=0.25)
    ax1.xaxis.grid(linestyle='--', alpha=0.25)
    ax2.yaxis.grid(linestyle='--', alpha=0.25)
    ax2.xaxis.grid(linestyle='--', alpha=0.25)

    legend_elements = [Line2D([0], [0], markersize=0, marker='s',
                              markerfacecolor=style_dict['colours'][1],
                              markeredgecolor='k',
                              color=style_dict['colours'][1], label=r'0.1', linestyle='-', linewidth=style_dict['line_width']),
                       Line2D([0], [0], markersize=0, marker='s',
                              markerfacecolor=style_dict['colours'][0],
                              markeredgecolor='k',
                              color=style_dict['colours'][0], label=r'0.01', linestyle='--', linewidth=style_dict['line_width'])]
    ax1.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize-1, framealpha=1, facecolor='w', edgecolor='k',handletextpad=0.25,
               title='$\omega$', title_fontsize=18)
    ax2.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize-1, framealpha=1, facecolor='w', edgecolor='k',handletextpad=0.25,
               title='$\omega$', title_fontsize=18)

    ax1.set_xlim(-.095, .575)
    ax1.set_ylim(-.2, 3.75)
    ax1.text(df1['b0'][0] + .025, df1['b0'][1], 'R$^2$ = 0', fontsize=15, c=style_dict['colours'][0])
    ax1.text(df2['b0'][0] - .075, df2['b0'][1] + 0.8, 'R$^2$ = 0.01', fontsize=15, c=style_dict['colours'][1])
    ax1.text(0.4, 2, 'R$^2$ = 0.38', fontsize=15, c=style_dict['colours'][0])
    ax1.text(0.4, 3.5, 'R$^2$ = 0.59', fontsize=15, c=style_dict['colours'][1])

    plt.tight_layout(pad=3.5)
    plt.savefig(os.path.join(fig_path, fig_name), bbox_inches='tight')