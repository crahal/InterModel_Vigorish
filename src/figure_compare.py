import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def make_compare(figure_path, data_path):
    df = pd.read_csv(os.path.join(data_path, 'sims', 'compare.csv'), index_col=0)
    plt.rcParams['axes.facecolor']='white'
    plt.rcParams['savefig.facecolor']='white'
    g = sns.PairGrid(df, diag_sharey=False, despine=True, height=2.5, aspect=0.8)
    g.map_lower(sns.scatterplot, color='#3e8abb')
    g.map_upper(sns.kdeplot, color='#6488b9')
    g.map_diag(sns.histplot, facecolor=(255/255, 69/255, 0/255, 0.5), fill=True, edgecolor='k', bins=8)
    csfont = {'fontname': 'Helvetica'}
    for ax in plt.gcf().axes:
        l = ax.get_xlabel()
        ax.set_xlabel(l,fontsize=18, **csfont)
        l = ax.get_ylabel()
        ax.set_ylabel(l, fontsize=18, **csfont)
        ax.tick_params(axis='both', which='major', labelsize=12)
    g.savefig(os.path.join(figure_path, "compare.pdf"))