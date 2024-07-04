import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from big_fun import get_w, get_ew, get_vw
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D


def plot_A_EPZP(fig_path, style_dict, fig_name):
    mpl.rcParams['font.family'] = style_dict['font']
    csfont = {'fontname': style_dict['font']}
    cmap = mpl.colors.LinearSegmentedColormap.from_list("", [style_dict['colours'][1],
                                                                         style_dict['colours'][0]])
    letter_fontsize = 23
    label_fontsize = 17
    line_width = style_dict['line_width']
    fig = plt.figure(figsize=(14,7))
    ax1 = plt.subplot2grid((1, 2), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((1, 2), (0, 1), rowspan=1, colspan=1)
    dicts_abovehalf = {}
    for a in np.arange(start=0.5, stop=0.9999, step=0.0001):
        dicts_abovehalf[a] = get_w(a, 0.5, [(0.5, 0.9999)])
    ax1.plot(dicts_abovehalf.keys(), dicts_abovehalf.values(),
             '-', color=style_dict['colours'][0], linewidth=line_width)
    ax1.set_ylabel(r'w', fontsize=label_fontsize, **csfont);
    ax1.set_xlabel(r'A', fontsize=label_fontsize, **csfont);
    ax1.set_ylim(ax1.get_ylim()[0], 1.02)

    pv = np.divide(list(range(50, 101, 1)), 100)
    del_list = np.divide(list(range(1, 11, 1)), 100)
    norm = plt.Normalize(0.01, 0.1)
    for i in range(1, len(del_list)):
        incrementer = del_list[i]
        pv0 = sorted(i for i in pv if (i + incrementer) < 1)
        p1 = pv0 + incrementer
        y = get_ew(pv0, p1)
        points = np.array([pv0, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lc = LineCollection(segments, cmap=cmap, norm=norm)
        lc.set_array(p1 - pv0)
        lc.set_linewidth(line_width)
        line = ax2.add_collection(lc)
        y = get_ew(pv0, p1) / np.sqrt(get_vw(pv0, p1))
        points = np.array([pv0, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lc = LineCollection(segments, cmap=cmap, norm=norm)
        lc.set_array(p1 - pv0)
        lc.set_linewidth(line_width)
        lc.set_linestyle('--')
        line = ax2.add_collection(lc)
    clb = plt.colorbar(line, ax=ax2)
    clb.set_label(r'$w_1-w_0$', fontsize=label_fontsize, labelpad=5, **csfont)
    ax2.set_ylabel(r'Values of E(P) and Z(P)', fontsize=label_fontsize, **csfont);
    ax2.set_xlabel(r'w$_0$', fontsize=label_fontsize, **csfont);
    ax2.set_ylim(0, 0.5)
    ax2.set_xlim(0.475, 1)
    legend_elements = [Line2D([0], [0], color='k', lw=1, linestyle='-',
                              label=r'E(P)', alpha=1),
                       Line2D([0], [0], color='k', lw=1, linestyle='--',
                              label=r'Z(P)', alpha=1), ]
    ax2.legend(handles=legend_elements, loc='upper left', frameon=True,
               fontsize=label_fontsize, framealpha=1, facecolor='w', edgecolor=(0, 0, 0, 1))
    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', y=1.025, x=-.05, **csfont)
    for ax in [ax1, ax2]:
        ax.grid(axis='both', linestyle='--', alpha=0.25)
        ax.tick_params(axis='both', labelsize=13)
    plt.subplots_adjust(wspace=2.5, hspace=0.25)
    plt.tight_layout(pad=3)
    plt.savefig(os.path.join(fig_path, fig_name + '.eps'), format='eps', dpi=600,
                bbox_inches='tight')
    plt.savefig(os.path.join(fig_path, fig_name + '.tiff'),
                dpi=600,
                format="tiff",
                pil_kwargs={"compression": "tiff_lzw"},
                bbox_inches='tight')
    plt.savefig(os.path.join(fig_path, fig_name + '.pdf'),
                bbox_inches='tight')
