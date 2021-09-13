from importlib import reload

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import json

import CorrelationAnalysis
import StatArrays
import PandasHelper

from IPython.display import display

# Generate stats
num_iterations = 100_000
reload(StatArrays)
stats_to_generate_4d6 = {
  "caterpillar" : StatArrays.caterpillar_stat_array,
  "improved caterpillar" : StatArrays.caterpillar_stat_array2,
  "4d6 drop lowest" : StatArrays.four_d_six_drop_lowest,
  "caterpillar with extra 3d6" : StatArrays.caterpillar_with_one_random_die
}
stats_to_generate_3d6 = {
  "caterpillar" : StatArrays.caterpillar_3d6,
  "improved caterpillar" : StatArrays.caterpillar_v2_3d6,
  "3d6" : StatArrays.three_d_six,
}

stats_to_generate = stats_to_generate_4d6
stats_pd = pd.concat([
  PandasHelper.stats_arrays_to_pd(
    [stat_generator() for i in range(num_iterations)],
    stat_label
  ) for stat_label, stat_generator in stats_to_generate.items()
  ], 
  axis=1
)

# Analysis of stats
point_buy = stats_pd.replace(StatArrays.point_buy_dict).groupby("iter").sum()
totals = stats_pd.groupby("iter").sum()

print("Summary Statistics of Ability Scores")
display(stats_pd.describe().applymap(PandasHelper.sig_figs, nsigfigs=3))

print("Summary Statistics of Point Buy Budget")
display(point_buy.describe().applymap(PandasHelper.sig_figs, nsigfigs=3))

print("Summary Statistics of Total Ability Scores")
display(totals.describe().applymap(PandasHelper.sig_figs, nsigfigs=3))

print("Number (%) of records with 2+ stats above 15 and only 0 or 1 stat below 10")
high_stats = (stats_pd > 15).groupby("iter").sum()
low_stats = (stats_pd < 10).groupby("iter").sum()
extreme_stats = ((high_stats > 1) & (low_stats < 2))
display(pd.DataFrame( { 
  "count" : extreme_stats.sum(), "%" : extreme_stats.mean()
  }))

print("Number (%) of records with only 0 or 1 stat above 15 and 3+ stats below 10")
high_stats = (stats_pd > 15).groupby("iter").sum()
low_stats = (stats_pd < 10).groupby("iter").sum()
extreme_stats = ((high_stats < 2) & (low_stats > 2))
display(pd.DataFrame( { 
  "count" : extreme_stats.sum(), "%" : extreme_stats.mean()
  }))
  
print("Number (%) of records with 3+ stats above 13 and only 0 or 1 stat below 10")
high_stats = (stats_pd > 13).groupby("iter").sum()
low_stats = (stats_pd < 10).groupby("iter").sum()
extreme_stats = ((high_stats > 2) & (low_stats < 2))
display(pd.DataFrame( { 
  "count" : extreme_stats.sum(), "%" : extreme_stats.mean()
  }))

print("Number (%) of records with only 0 or 1 stats above 13 and 2+ stats below 10")
high_stats = (stats_pd > 13).groupby("iter").sum()
low_stats = (stats_pd < 10).groupby("iter").sum()
extreme_stats = ((high_stats < 2) & (low_stats > 1))
display(pd.DataFrame( { 
  "count" : extreme_stats.sum(), "%" : extreme_stats.mean()
  }))
  
# Correlation analysis
reload(CorrelationAnalysis)
CorrelationAnalysis.analyse(stats_pd)

# Graphs
fig, axes = plt.subplots(ncols=2)
fig.set_figwidth(10)
line_plot = lambda ax, df, c: ax.plot(df.index, df[c], label=c)

point_buy_counts = PandasHelper.create_counts(point_buy, normalize=True)
[line_plot(axes[0], point_buy_counts, c) for c in point_buy_counts.columns]
axes[0].set_ylabel(f"Distribution (out of {num_iterations:,} samples)")
axes[0].yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=1))
axes[0].set_xlabel("Point buy budget")
axes[0].legend()
axes[0].grid(True)

stat_counts = PandasHelper.create_counts(stats_pd, normalize=True)
[line_plot(axes[1], stat_counts, c) for c in stat_counts.columns]
axes[1].set_ylabel(f"Distribution (out of {StatArrays.num_ability_scores*num_iterations:,} samples)")
axes[1].set_xlabel("Ability score")
axes[1].yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=1))
axes[1].legend()
axes[1].grid(True)

fig.tight_layout()
plt.show()

count = PandasHelper.create_counts(
  stats_pd.reset_index().pivot(index="iter", columns="stat", values="improved caterpillar"),
  normalize=True)
fig, ax = plt.subplots()
axes = [line_plot(ax, count, c) for c in count.columns]
ax.set_ylabel(f"Distribution of improved caterpillar \nmethod (out of {num_iterations:,} samples)")
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=1))
ax.set_xlabel("Score")
ax.legend()
ax.grid(True)
plt.show()

for c in totals.columns:
  total_counts = totals.value_counts(c, normalize=True)
  total_counts.sort_index(inplace=True)
  print(c)
  print(json.dumps(total_counts.cumsum().round(4).to_dict()))

# Stats
'{"65": 0.014, "66": 0.0443, "67": 0.0924, "68": 0.161, "69": 0.2538, "70": 0.3714, "71": 0.4893, "72": 0.6024, "73": 0.7066, "74": 0.7974, "75": 0.8698, "76": 0.9177, "77": 0.9532, "78": 0.9769, "79": 0.9905, "80": 0.9979, "81": 1.0}'