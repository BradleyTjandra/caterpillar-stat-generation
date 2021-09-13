#!/usr/bin/env python
# coding: utf-8

# Alternative Methods
# ============================
# 
# The Improved Goblin method allows us to generate random stats, while reducing the chances that characters are be incredibly powerful or weak. However, there are even more potential ways we could generate stats. This seciton considers these, and sees how effectively they a) allow for variability in stats and b) reduce variability in overall character strength.
# 
# ## Desiderata with Alternative Stat Methods 
# 
# Here are some desiderata we have for ways to generate stats:
# 
# 1. It allows players to have different stats. 
# 2. It makes stats somewhat random, so that players do not feel compelled to min-max to avoid being weaker than other players. 
# 3. It reduces the chances that players will have much better or worse stats than other players.
# 4. It still allow players to have incredibly bad or incredibly good stats - but then the other stats will be good or bad to partially offset this.
# 
# I acknowledge these desiderata are somewhat subjective, but for _me_ they make a good game.
# 
# ## Possible alternative methods
# 
# A couple of methods have been raised as part of this discussion:
# 
# 1. Using the 13th Age's method
# 2. Instead of using the bottom faces, rolling a new set of 3d6
# 
# For each of these, I will show the resulting distribution of stats, the distribution of character point budgets, and provide some commentary. I will compare these to 4d6-drop-lowest and Improved Goblin.
# 
# ## 13th Age method
# 
# For the 13th Age method, I have used a "Base" of 12, to better reflect that the average stat from 4d6-drop-lowest is around 12. I have also used d8's instead of d6's, as they provide a similar spread of individual stats to the other two methods. The distribution of results can be seen below.
# 
# ```{glue:} 13th_age_fig
# ```
# 
# Looking at the individual stats (the left-hand chart), the 13th Age method shape is a lot simpler - as each stat is generated from only a couple of dice. It has a similar shape to 4d6-drop-lowest, with a peak and mean of around 12. Despite having a minimum stat roll of 5 (as opposed to the other methods with a minimum of 3), the spread is relatively similar.
# 
# Considering the overall point buy budget (the right-hand chart), the 13th Age method has a significantly lower spread. This is to be expected as the method forces the sum of all stats to be 72. Any differences in characters is purely because some characters will have stats above 15, which are considered more valuable. 
# 
# This method provides a much narrower range of characters, and is a very simple way of generating characters. While some may consider this lack of diversity a negative, it seems like a viable alternative to keep characters adequately similar. Some may also not like the symmetry, and prefer a negative skew where most of the stats are high, with a small possibility for very low (<5) stats. As opposed to the 13th Age method where there is slightly less chance for high numbers, offset by no chance of very low stats.
# 
# ## Rolling a new set of 3d6
# 
# Under this method, you do the Improved Caterpillar method as usual. However instead of adding the bottom faces, you simply re-roll the 3d6. This has the advantage of not requiring you to reference faces which are not visible. The distribution of this method can be seen below.
# 
# ```{glue:} one_random_fig
# ```
# 
# For individual stats, the distributions are very similar: The means are all around 12, the standard deviations all around 3.0, and the interquartile ranges (not shown) are the same.
# 
# However, for distribution of overall character strength (the right-hand chart) the "Roll again" method is somewhat in-between the two methods (although slightly closer to 3d6-drop-lowest). This intuitively makes sense: While using the bottom face of the caterpillar makes one stat anti-correlated to the fourth, fifth and sixth stat, re-rolling the dice makes this stat independent of all other stats. And independent stats is the situation for 4d6-drop-lowest.
# 
# This method doesn't really constrain character strength that much. It does mean that "hidden" faces are not used in the calculation (which some may see as a pro) and that the dice need to be re-rolled (which some may see as a con), but these seem like relatively unimportant considerations.
# 
# ## Summary
# 
# There are some other methods of generating stats randomly, which have their upsides and downsides. Which is better is - to a degree - a matter of preference. I personally believe the Improved Caterpillar method is a strong option. The next two sections provide the code used to generate this graph, and a small widget to roll your own stats.
