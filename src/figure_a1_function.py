import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.preprocessing import StandardScaler
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter
nrmlzd = StandardScaler()


def make_figure_a1(figure_path, data_path):
    mpl.rcParams['font.family'] = 'Helvetica'
    csfont = {'fontname': 'Helvetica'}
    letter_fontsize = 23
    label_fontsize = 16
    data_path = os.path.join(data_path, 'HRS')
    hrs_desc = pd.read_csv(os.path.join(data_path, 'hrs_desc.csv'), index_col=0)
    fig = plt.figure(figsize=(14.4,7.2))
    ax1 = plt.subplot2grid((1, 2), (0, 0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((1, 2), (0, 1), rowspan=1, colspan=1)
    hrs_desc = hrs_desc.rename({'hibp': 'HiBP'}, axis=1)
    hrs_desc = hrs_desc.rename({'diab': 'Diab'}, axis=1)
    hrs_desc = hrs_desc.rename({'cancr': 'Cancr'}, axis=1)
    hrs_desc = hrs_desc.rename({'lung': 'Lung'}, axis=1)
    hrs_desc = hrs_desc.rename({'heart': 'Heart'}, axis=1)
    hrs_desc = hrs_desc.rename({'strok': 'Strok'}, axis=1)
    hrs_desc = hrs_desc.rename({'psych': 'Psych'}, axis=1)
    hrs_desc = hrs_desc.rename({'arthr': 'Arthr'}, axis=1)
    hrs_desc = hrs_desc.rename({'proxy': 'Proxy'}, axis=1)
    hrs_desc = hrs_desc.rename({'dead': 'Dead'}, axis=1)
    hrs_desc = hrs_desc.rename({'dead': 'Dead'}, axis=1)
    hrs_desc = hrs_desc.rename({'cog': 'Cog'}, axis=1)
    hrs_desc = hrs_desc.rename({'grip': 'Grip'}, axis=1)
    hrs_desc = hrs_desc.rename({'gait': 'Gait'}, axis=1)
    colors_long = ['#364B9A', '#4A7BB7', '#6EA6CD', '#98CAE1', '#C2E4EF',
                   '#FEDA8B', '#FDB366', '#F67E4B', '#3288bd', '#5e4fa2']
    colors = ['#d53e4f', '#f46d43', '#fdae61', '#3288bd', '#5e4fa2']
    colors3 = ['#d53e4f', '#fdae61', '#3288bd']
    cols = ["HiBP", "Diab", "Cancr", "Lung", "Heart", "Strok", "Psych", "Arthr", "Proxy", "Dead"]
    iterator = 0
    col_num = 0
    for col in cols:
        tmp = hrs_desc[hrs_desc[col].notnull()]
        tmp = tmp.groupby(['age'])[col].mean().reset_index()
        tmp = tmp[(tmp['age'] >= 60) & (tmp['age'] <= 90)].set_index('age')
        if (iterator % 2) == 0:
            dash = '--'
            col_num = col_num + 1
        else:
            dash = '-'
        iterator = iterator + 1
        tmp.plot(ax=ax1, c=colors[col_num - 1], alpha=.85, linestyle=dash, linewidth=1.25)
    cols = ["Cog", "Grip", "Gait"]
    iterator = 0
    for col in cols:
        tmp = hrs_desc[hrs_desc[col].notnull()].copy()
        tmp[col] = nrmlzd.fit_transform(tmp[[col]])
        tmp = tmp.groupby(['age'])[col].mean().reset_index()
        if col == 'Gait':
            age = 65
        else:
            age = 60
        if col == 'Grip':
            dash = '--'
        else:
            dash = '-'
        tmp = tmp[(tmp['age'] >= age) & (tmp['age'] <= 90)].set_index('age')
        tmp.plot(ax=ax2, c=colors3[iterator], alpha=.85, linestyle=dash, linewidth=1.25)
        iterator = iterator + 1
    ax2.set_ylabel('Standardized Mean', csfont, fontsize=label_fontsize);
    ax1.set_ylabel('Prevalence', csfont, fontsize=label_fontsize);
    ax2.set_xlabel('Age', csfont, fontsize=15);
    ax1.set_xlabel('Age', csfont, fontsize=15);
    ax1.set_title(r'A.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1)
    ax2.set_title(r'B.', fontsize=letter_fontsize, loc='left', x=-.05, **csfont, y=1)
    ax1.legend(loc='upper center', frameon=True, ncol=5,
               fontsize=10, framealpha=0.9, facecolor='w', edgecolor='k', handletextpad=0.5)
    ax2.legend(loc='upper center', frameon=True, ncol=3,
               fontsize=12, framealpha=0.8, facecolor='w', edgecolor='k', handletextpad=0.25)
    ax1.set_ylim(0, 0.99999)
    ax1.set_xlim(55, 92)
    #ax1.spines['bottom'].set_bounds(55, ax1.get_xlim()[1])
    #ax1.spines['left'].set_bounds(0, 1)
    ax2.set_ylim(-1.0, .995)
    ax2.set_xlim(55, 92)
    #ax2.spines['bottom'].set_bounds(55, ax2.get_xlim()[1])
    #ax2.spines['left'].set_bounds(-1, 1)

    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    cols = ["HiBP", "Diab", "Cancr", "Lung", "Heart", "Strok", "Psych", "Arthr", "Proxy", "Dead"]
    iterator = 0
    col_num = 0
    for col in cols:
        tmp = hrs_desc[hrs_desc[col].notnull()]
        tmp = tmp.groupby(['age'])[col].mean().reset_index()
        tmp = tmp[(tmp['age'] >= 60) & (tmp['age'] <= 90)].set_index('age')
        y = tmp.reset_index()[col][0] - 0.0185
        x = tmp.reset_index()['age'][0] - 3.25
        if (iterator % 2) == 0:
            dash = '--'
            col_num = col_num + 1
        else:
            dash = '-'
        iterator = iterator + 1
        ax1.text(x, y, col, fontsize=10.5, c=colors[col_num - 1])

    cols = ["Cog", "Grip", "Gait"]
    iterator = 0
    col_num = 0
    for col in cols:
        if col == 'Gait':
            age = 0
        else:
            age = 5
        if col == 'Cog':
            shifter = 0.0
        else:
            shifter = 0
        tmp = hrs_desc[hrs_desc[col].notnull()]
        tmp[col] = nrmlzd.fit_transform(tmp[[col]])
        tmp = tmp[(tmp['age'] >= (65 - age)) & (tmp['age'] <= 90)].set_index('age')
        tmp = tmp.groupby(['age'])[col].mean().reset_index()
        y = tmp.reset_index()[col][0] + shifter
        x = tmp.reset_index()['age'][0] - 3
        iterator = iterator + 1
        ax2.text(x, y, col, fontsize=13, c=colors3[iterator - 1])

    ax1.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax2.yaxis.set_major_locator(plt.MaxNLocator(5))
    ax1.yaxis.set_minor_locator(plt.MaxNLocator(10))
    ax2.yaxis.set_minor_locator(plt.MaxNLocator(10))
    ax1.yaxis.grid(linestyle='--', alpha=0.25, which='both')
    ax1.xaxis.grid(linestyle='--', alpha=0.25, which='both')
    ax2.xaxis.grid(linestyle='--', alpha=0.25, which='both')
    ax2.yaxis.grid(linestyle='--', alpha=0.25, which='both')
    ax1.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=12)
    ax1.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=12)
    ax2.tick_params(axis='both', which='major', width=1.25, length=5, labelsize=12)
    ax2.tick_params(axis='both', which='minor', width=1.25, length=3, labelsize=12)

    sns.despine()
    plt.subplots_adjust(wspace=.25, hspace=0)
    plt.savefig(os.path.join(figure_path, 'figure_a1.pdf'), bbox_inches='tight')