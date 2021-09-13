import numpy as np
import pandas as pd
# from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

# Limits for the extent
x_start = 0.
x_end = 18.
y_start = 0.
y_end = 18.
extent = [x_start, x_end, y_start, y_end]

def graph_corr_data(ax, data: pd.core.frame.DataFrame, col: str) -> pd.core.frame.DataFrame:

  # Get correlation data
  transposed = data.pivot("iter", "stat", col)
  corr = np.corrcoef(transposed.values.T)  
  corr_masked = corr + np.triu(np.full_like(corr, fill_value=np.nan))
  corr_masked = corr_masked[1:, :-1]

  # Graph data  
  ax.imshow(corr_masked, extent=extent, interpolation='None', cmap='Greens_r', vmax = .1, vmin=-.3)

  # Add the text
  size = corr_masked.shape[0]
  jump_x = (x_end - x_start) / (2.0 * size)
  jump_y = (y_end - y_start) / (2.0 * size)
  x_positions = np.linspace(start=x_start, stop=x_end, num=size, endpoint=False)
  y_positions = np.linspace(start=y_end-jump_y*2, stop=y_start-jump_y*2, num=size, endpoint=False)

  for y_index, y in enumerate(y_positions):
    for x_index, x in enumerate(x_positions):
      label = "{:.3f}".format(corr_masked[y_index, x_index].item())
      text_x = x + jump_x
      text_y = y + jump_y
      
      if label != "nan": 
        ax.text(text_x, text_y, label, color='black', ha='center', va='center',
        fontsize='medium')

  # Add title
  ax.set_title(col)

def setup_fig(data):

  size_of_each_graph = 5
  ncols = 3
  num_graphs = len(data.columns)
  nrows = int((num_graphs+ncols-1) / ncols)
  fig_width = size_of_each_graph*ncols
  fig_height = size_of_each_graph*nrows

  fig, axes = plt.subplots(nrows, ncols, figsize=(fig_width, fig_height))
  return(fig, axes, axes.flatten())
  

def analyse(data: pd.core.frame.DataFrame) -> list:

  shuffled_data = data.groupby("iter").sample(frac=1)
  shuffled_data.index = data.index
  shuffled_data.reset_index(inplace=True)

  fig, axes, flat_axes = setup_fig(data)

  for i, ax in enumerate(flat_axes):

    if i < len(data.columns):
      col = data.columns[i]
      graph_corr_data(ax, shuffled_data, col)
      ax.set_axis_off()
      ax.set_frame_on(True)
    
    else:
      ax.set_axis_off()

  fig.tight_layout()

  # colour bar
  first_axis = flat_axes[0].images[0]
  mappable = ScalarMappable(norm=first_axis.norm, cmap=first_axis.get_cmap())
  fig.colorbar(mappable, location="bottom", ax=flat_axes, 
  aspect=64, shrink=0.95,
  pad=0.05)

  return(fig)