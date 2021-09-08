import numpy as np
import pandas as pd
from math import floor, log10, isnan

def stats_arrays_to_pd(arr: np, label: str) -> pd:

  df = pd.DataFrame(arr)
  df.reset_index(inplace=True)
  df = df.melt(id_vars="index", var_name="stat", value_name=label)
  df.rename(columns={"index":"iter"}, inplace=True)
  df.set_index(["iter", "stat"], inplace=True)
  df.sort_values(["iter", "stat"], inplace=True)

  return(df)

def create_counts(df: pd, normalize: bool = False) -> pd:

  counts = pd.concat([df[col].value_counts(normalize) for col in df.columns], axis=1)
  counts.sort_index()
  return(counts)
  
def sig_figs(number, nsigfigs: int = 1) -> str:

  if isnan(number):
    return("NaN")

  if number == 0.0:
    return("-")
  
  try:
    ndigits = - int(floor(log10(abs(number)))) + (nsigfigs - 1)

  except ValueError:
    print(number)
    raise

  rounded = round(number, ndigits)
  return(str(rounded))
