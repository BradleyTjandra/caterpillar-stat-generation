import numpy as np
import pandas as pd

def summarise_corrs(data: pd.core.frame.DataFrame, col: str) -> pd.core.frame.DataFrame:
  transposed = data.pivot("iter", "stat", col)
  corr = np.corrcoef(transposed.values.T)
  corr_summ = pd.DataFrame(corr) \
    .reset_index() \
    .melt(id_vars="index", var_name="column", value_name=col) \
    .query("index > column")[col] \
    .describe()
  return(corr_summ)


def analyse(data: pd.core.frame.DataFrame) -> list:

  shuffled_data = data.groupby("iter").sample(frac=1)
  shuffled_data.index = data.index
  shuffled_data.reset_index(inplace=True)
  
  cols = data.columns
  summary = pd.concat([summarise_corrs(shuffled_data, c) for c in cols], axis=1)

  return(summary)