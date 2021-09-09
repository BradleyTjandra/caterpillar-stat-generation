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
import sys
sys.path.append("../src/")
print("hello")


# In[2]:


# Set up report tables
import ReportTables
from importlib import reload
reload(ReportTables)
report_tables = ReportTables.ReportTables()


# In[3]:


report_tables.show_stats_distribution()


# 
# 
# The average ability score is 12. The following chart shows the distribution of stats generated from caterpillar and 4d6-drop-lowest, run over 10,000 characters (and hence producing 60,000 stats). 
# 
# Overall means that the probability of a character having a certain stat is roughly the same whether you use caterpillar or 4d6-drop-lowest - when looking at a single stat from either method. This is good, as in general we don't want to be using a stat generation method if it produces much higher or lower stats.
