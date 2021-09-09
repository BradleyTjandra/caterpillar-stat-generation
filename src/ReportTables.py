from importlib import reload
from myst_nb import glue

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

import CorrelationAnalysis
import StatArrays
import PandasHelper

from IPython.display import display

def run():

  # Generate stats
  num_iterations = 10_000
  stats_to_generate = {
    "Caterpillar" : StatArrays.caterpillar_stat_array,
    "Improved Caterpillar" : StatArrays.caterpillar_stat_array2,
    "4d6-drop-lowest" : StatArrays.four_d_six_drop_lowest,
  }
  stats = pd.concat([
    PandasHelper.stats_arrays_to_pd(
      [stat_generator() for i in range(num_iterations)],
      stat_label
    ) for stat_label, stat_generator in stats_to_generate.items()
    ], 
    axis=1
  )
  point_buy = stats.replace(StatArrays.point_buy_dict).groupby("iter").sum()
  totals = stats.groupby("iter").sum()

  # Line plot function
  line_plot = lambda ax, df, c: ax.plot(df.index, df[c], label=c)

  # Create stat distribution graph
  fig, axes = plt.subplots()
  stat_counts = PandasHelper.create_counts(stats, normalize=True)
  [line_plot(axes, stat_counts, c) for c in stat_counts.columns]
  num_samples = StatArrays.num_ability_scores*num_iterations
  axes.set_ylabel(f"Distribution (out of {num_samples:,} samples)")
  axes.set_xlabel("Ability score")
  percent_formatter = matplotlib.ticker.PercentFormatter(xmax=1, decimals=1)
  axes.yaxis.set_major_formatter(percent_formatter)
  axes.legend()
  axes.grid(True)
  glue("stats_distribution_fig", fig, display=False)
  plt.close()
  # fig.close()

  # Create summary stats
  summary_stats = stats.describe().applymap(PandasHelper.sig_figs, nsigfigs=3)
  glue("summary_stats_df", summary_stats, display=False)

  # Create fig of point buy cost schedule
  point_buy_costs = [[k, v] for k, v in StatArrays.point_buy_dict.items()]
  point_buy_costs_df = pd.DataFrame(point_buy_costs, columns = ["Score", "Cost"])
  point_buy_orig = point_buy_costs_df.loc[ \
    (point_buy_costs_df.Score >= 8) \
    & (point_buy_costs_df.Score <= 15)
  ]
  point_buy_fig, axes = plt.subplots()
  axes.plot(point_buy_costs_df.Score, point_buy_costs_df.Cost, label="Point buy costs")
  axes.plot(point_buy_orig.Score, point_buy_orig.Cost, label="Extended for above 15 and below 8")
  axes.set_ylabel(f"Cost")
  axes.set_xlabel("Ability score")
  axes.set_ylim(-20, 20)
  axes.legend()
  axes.grid(True)
  glue("point_buy_fig", point_buy_fig, display=False)
  plt.close()

  point_buy_dist_fig, axes = plt.subplots()
  line_plot = lambda ax, df, c: ax.plot(df.index, df[c], label=c)

  # Create point buy budget distribution
  point_buy_counts = PandasHelper.create_counts(point_buy, normalize=True)
  [line_plot(axes, point_buy_counts, c) for c in point_buy_counts.columns]
  axes.set_ylabel(f"Distribution (out of {num_iterations:,} samples)")
  percent_formatter = matplotlib.ticker.PercentFormatter(xmax=1, decimals=1)
  axes.yaxis.set_major_formatter(percent_formatter)
  axes.set_xlabel("Point buy budget")
  axes.legend()
  axes.grid(True)

  point_buy_dist_fig.tight_layout()
  glue("point_buy_dist_fig", point_buy_dist_fig, display=False)
  plt.close()

  # Create summary of point buy budget
  point_buy_summ = point_buy.describe().applymap(PandasHelper.sig_figs, nsigfigs=3)
  glue("summary_point_buy_df", point_buy_summ, display=False)

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
