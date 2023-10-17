import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_kelly_bet(fig_path, style_dict, fig_name):
    label_fontsize = 17
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    colors = style_dict['colours']
    fig = plt.figure(figsize=(6.5,6.5))
    ax3 = plt.subplot2grid((1, 1), (0, 0), rowspan=1, colspan=1)
    vals = np.linspace(0.1, 1, 10, endpoint=True)
    x = np.linspace(0.5, 1, 10)
    for val in vals:
        if val == 0.1:
            ax3.plot(x, (val * x) + x, c=colors[0], label='IMV',
                     linewidth=style_dict['line_width'])
            ax3.plot(x, (val * (1 - x)) + x, linestyle='dotted',
                     c=colors[1], label='Kelly Bet',
                     linewidth=style_dict['line_width'])
        else:
            ax3.plot(x, (val * x) + x, c=colors[0],
                     linewidth=style_dict['line_width'])
            ax3.plot(x, (val * (1 - x)) + x, linestyle='dotted',
                     c=colors[1],
                     linewidth=style_dict['line_width'])
        ax3.set_ylim(0.5, 1)
        ax3.set_xlim(0.5, 1)
    ax3.set_ylabel(r'w$_1$', fontsize=label_fontsize+4, **csfont)
    ax3.set_xlabel(r'w$_0$', fontsize=label_fontsize+4, **csfont)
    ax3.legend(loc='lower right', frameon=True,
               fontsize=label_fontsize, framealpha=1,
               facecolor='w', edgecolor=(0, 0, 0, 1))

    ax3.tick_params(axis='y', labelsize=15)
    ax3.tick_params(axis='x', labelsize=15)
    ax3.xaxis.grid(linestyle='--', alpha=0.25)
    ax3.yaxis.grid(linestyle='--', alpha=0.25)
    plt.savefig(os.path.join(fig_path, fig_name),
                bbox_inches='tight')