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
# ## How Can We Compare Stat Arrays?
# 
# When comparing stat arrays, it is helpful to reduce the six ability scores to a single number representing how good the roll is. One simple way to do this would be to just add up the six scores. 
# 
# However, I consider having an ability score of 18 rather than 16 to be much better than having an ability score of 12 rather than 10. The former will probably increase your primary ability score and thus be used much more, while the latter many only have a small impact as it is probably not your character's primary focus.
# 
# This is also reflected in the point buy method, which has a supralinear relationship for scores of 14+. Given this seems like a popular method of stat array generation, I have decided to adopt the costs for each ability score from the stat array. Because the point buy table only covers scores between 8 and 15, I have extended the table per the following schedule.
# ```{glue:} point_buy_fig
# ```
#  
# ## Simulations
# 
# We can now convert our stat arrays to a single "point buy budget". The distribution of results is shown below.
# ```{glue:} point_buy_dist_fig
# ```
