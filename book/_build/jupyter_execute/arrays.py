#!/usr/bin/env python
# coding: utf-8

# # Stat Arrays
# 
# In the previous section we saw that the distribution of individual stats is very similar under any of the three methods. This begs the question, why bother with the more complex-to-follow caterpillar methods? 
# 
# The caterpillar methods are supposed to reduce the chance of players have very high or very low stats. This can be undesireable as it makes some characters much more powerful than others, and can make it for hard for a DM to balance encounters. This section shows that Goblin's caterpillar method does _not_ achieve this goal. However, the Improved Goblin method does.
# 
# ## What is too much volatility?
# 
# People have different standards about what is an "acceptable" amount of volatility between characters. Some parties are happy to have one player with many scores of 15 or higher, and another player with only one score above 15 and everything other stat below 12. For others, this difference would seem too large and would make the game less fun.
# 
# There's no right answer here. In my opinion, the volatility of 4d6-drop-lowest is a bit too large, and I would prefer something closer to the Improved Goblin method. However, it is possible to reduce the volatility of character stat arrays even further, for example 13th Age's [Base 13 Random method](https://www.13thagesrd.com/character-rules/#Base_13_Random_Stat_Generation_DATP).
# 
# ## How to compare volatility
# 
# When comparing volatility on stat arrays, it is helpful to reduce the six ability scores to a single number representing how good the roll is. One simple way to do this would be to just add up the six scores. However, I consider having an ability score of 18 rather than 16 to be much better than having an ability score of 12 rather than 10: The former will probably increase your primary ability score and thus be used much more, while the latter many only have a small impact as it is probably not your character's primary focus.
# 
# This is also reflected in the point buy method, which has a supralinear relationship for scores of 14+. Given this seems like a popular method of stat array generation, I have decided to adopt the costs for each ability score from the stat array. However, the point buy table only go from 8 to 15. Given our three dice methods allow us to generate scores between 3 and 18, we need to extend the table.
# 
# I have adopted the following schedule for this purpose:
# 
# However, across a character's stat array Goblin's caterpillar method does not significantly reduce the amount of volatility between different character's.** For example, the following table compares the probability of two scenarios: a player rolling "very good" stats (2+ stats above 15 and 0 or 1 stat below 10) or "very bad" stats (0 or 1 stat above 13 and 2+ stats below 10) stats.
# 
# |Scenario                                                 | 4d6-Drop<br>-Lowest | Goblin's <br>Caterpillar |
# |---------------------------------------------------------|:-------------------:|:------------------------:|
# | 2 or more stats above 15, <br>0 or 1 stat below 10 |         15%         |            14%           |
# | 0 or 1 stat above 13, <br>2 or more stats below 10 |         14%         |            18%           |
# 
# For these two cases, there doesn't seem to be much difference between the two methods. And in roughly one-third of cases, a player can be expected to fall into one of these two scenarios. While the above is just an example of two scenarios, the Caterpillar method in general is not better than 4d6-drop-lowest at other definitions of very good and bad stats.

# In[1]:


# Set up link to python code
# HIDDEN
import sys
sys.path.append("../src/")


# In[2]:


# NO CODE

import StatArrays
import matplotlib.pyplot as plt
import pandas as pd

point_buy_costs = [[k, v] for k, v in StatArrays.point_buy_dict.items()]
point_buy_costs_df = pd.DataFrame(point_buy_costs, columns = ["Score", "Cost"])
point_buy_orig = point_buy_costs_df.loc[   (point_buy_costs_df.Score >= 8)   & (point_buy_costs_df.Score <= 15)
]
fig, axes = plt.subplots()
axes.plot(point_buy_costs_df.Score, point_buy_costs_df.Cost, label="Point buy costs")
axes.plot(point_buy_orig.Score, point_buy_orig.Cost, label="Extended for above 15 and below 8")
axes.set_ylabel(f"Cost")
axes.set_xlabel("Ability score")
axes.set_ylim(-20, 20)
axes.legend()
axes.grid(True)

fig.tight_layout()
plt.show()


# In[ ]:




