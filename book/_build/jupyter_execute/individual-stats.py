#!/usr/bin/env python
# coding: utf-8

# # Individual Stats
# 
# This section compares the distribution of individual stats between 4d6-drop-lowest, Goblin's caterpillar method, and the Improved Goblin method. I find that using each method, the distribution of possible individual stats is the same under each method. This both corroborates what Goblin found, and verifies that the Improved Goblin method continues to be consistent with 4d6-drop-lowest.
# 
# ## Simulations
# 
# To perform this, I ran a simulation of 10,000 characters, each with 6 stats each, producing 60,000 stats. The distribution of these results is visible below.

# In[1]:


# Set up link to python code
# HIDDEN
import sys
sys.path.append("../src/")


# In[2]:


# Set up report tables
# NO CODE

import ReportTables
from importlib import reload
reload(ReportTables)
report_tables = ReportTables.ReportTables()


# In[3]:


# NO CODE
report_tables.show_stats_distribution()


# The two caterpillar methods (blue and yellow lines) have a very similar shape. Meanwhile, 4d6-drop-lowest (green) has a smoother curve than the caterpillar methods, and is appears to have a slightly higher range of scores. However, overall the three distributions appear fairly similar.
# 
# ## Summary Statistics
# This similarity can also be seen by looking at some summary statistics of the three methods.

# In[4]:


# NO CODE

reload(ReportTables)
report_tables.show_summary_statistics_stats()


# The three methods have very similar means and standard deviations (std). Also for all methods, 25% of stats are 10 or lower, and 25% are 14 or higher. This reinforces the view that the distributions are very similar.
