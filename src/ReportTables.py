from importlib import reload
from myst_nb import glue

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as mtick

import CorrelationAnalysis
import StatArrays
import PandasHelper

from IPython.display import display

class ReportTables:

  def __init__(self, num_iterations = 10_000):
    # Generate stats
    self.num_iterations = num_iterations
    stats_to_generate_4d6 = {
      "caterpillar" : StatArrays.caterpillar_stat_array,
      "improved caterpillar" : StatArrays.caterpillar_stat_array2,
      "4d6 drop lowest" : StatArrays.four_d_six_drop_lowest,
    }

    stats_to_generate = stats_to_generate_4d6
    stats_pd = pd.concat([
      PandasHelper.stats_arrays_to_pd(
        [stat_generator() for i in range(self.num_iterations)],
        stat_label
      ) for stat_label, stat_generator in stats_to_generate.items()
      ], 
      axis=1
    )

    self.set_data(stats_pd)

  # Analysis of stats
  def show_point_buy_distribution(self):

    fig, axes = plt.subplots()
    line_plot = lambda ax, df, c: ax.plot(df.index, df[c], label=c)

    point_buy_counts = PandasHelper.create_counts(self.point_buy, normalize=True)
    [line_plot(axes, point_buy_counts, c) for c in point_buy_counts.columns]
    axes.set_ylabel(f"Distribution (out of {self.num_iterations:,} samples)")
    axes.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=1))
    axes.set_xlabel("Point buy budget")
    axes.legend()
    axes.grid(True)

    fig.tight_layout()
    plt.show()

    # Analysis of stats
  def show_stats_distribution(self):

    fig, axes = plt.subplots()
    line_plot = lambda ax, df, c: ax.plot(df.index, df[c], label=c)

    stat_counts = PandasHelper.create_counts(self.stats, normalize=True)
    [line_plot(axes, stat_counts, c) for c in stat_counts.columns]
    num_samples = StatArrays.num_ability_scores*self.num_iterations
    axes.set_ylabel(f"Distribution (out of {num_samples:,} samples)")
    axes.set_xlabel("Ability score")
    axes.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=1))
    axes.legend()
    axes.grid(True)

    fig.tight_layout()
    plt.show()

  def set_data(self, stats):

    point_buy = stats.replace(StatArrays.point_buy_dict).groupby("iter").sum()
    totals = stats.groupby("iter").sum()

    self.stats = stats
    self.point_buy = point_buy
    self.totals = totals
  
  def show_summary_statistics_stats(self):

    display(self.stats.describe().applymap(PandasHelper.sig_figs, nsigfigs=3))

  # print("Summary Statistics of Point Buy Budget")
  # display(point_buy.describe().applymap(PandasHelper.sig_figs, nsigfigs=3))

  # print("Summary Statistics of Total Ability Scores")
  # display(totals.describe().applymap(PandasHelper.sig_figs, nsigfigs=3))

  # print("Number (%) of records with 2+ stats above 15 and only 0 or 1 stat below 10")
  # high_stats = (stats_pd > 15).groupby("iter").sum()
  # low_stats = (stats_pd < 10).groupby("iter").sum()
  # extreme_stats = ((high_stats > 1) & (low_stats < 2))
  # display(pd.DataFrame( { 
  #   "count" : extreme_stats.sum(), "%" : extreme_stats.mean()
  #   }))

  # print("Number (%) of records with only 0 or 1 stat above 15 and 3+ stats below 10")
  # high_stats = (stats_pd > 15).groupby("iter").sum()
  # low_stats = (stats_pd < 10).groupby("iter").sum()
  # extreme_stats = ((high_stats < 2) & (low_stats > 2))
  # display(pd.DataFrame( { 
  #   "count" : extreme_stats.sum(), "%" : extreme_stats.mean()
  #   }))
    
  # print("Number (%) of records with 3+ stats above 13 and only 0 or 1 stat below 10")
  # high_stats = (stats_pd > 13).groupby("iter").sum()
  # low_stats = (stats_pd < 10).groupby("iter").sum()
  # extreme_stats = ((high_stats > 2) & (low_stats < 2))
  # display(pd.DataFrame( { 
  #   "count" : extreme_stats.sum(), "%" : extreme_stats.mean()
  #   }))

  # print("Number (%) of records with only 0 or 1 stats above 13 and 2+ stats below 10")
  # high_stats = (stats_pd > 13).groupby("iter").sum()
  # low_stats = (stats_pd < 10).groupby("iter").sum()
  # extreme_stats = ((high_stats < 2) & (low_stats > 1))
  # display(pd.DataFrame( { 
  #   "count" : extreme_stats.sum(), "%" : extreme_stats.mean()
  #   }))
    
  # # Correlation analysis
  # display(CorrelationAnalysis.analyse(stats_pd))

  # # Graphs
  # fig, axes = plt.subplots(ncols=2)
  # fig.set_figwidth(10)
  # line_plot = lambda ax, df, c: ax.plot(df.index, df[c], label=c)

  # fig.tight_layout()
  # plt.show()

  # count = PandasHelper.create_counts(
  #   stats_pd.reset_index().pivot(index="iter", columns="stat", values="improved caterpillar"),
  #   normalize=True)
  # fig, ax = plt.subplots()
  # axes = [line_plot(ax, count, c) for c in count.columns]
  # ax.set_ylabel(f"Distribution of improved caterpillar \nmethod (out of {num_iterations:,} samples)")
  # ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=1))
  # ax.set_xlabel("Score")
  # ax.legend()
  # ax.grid(True)
  # plt.show()