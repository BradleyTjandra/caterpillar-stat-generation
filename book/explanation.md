More Details
============================
# Context

Recently Goblin's Henchman shared an [article on their blog](https://goblinshenchman.wordpress.com/2020/08/15/caterpillar-method-for-character-stat-generation/) about using different sides of the same dice to generate stats for characters in D&D.

The suggested method sounds appealing because it aims to a) allow players to have different stats; b) make those stats somewhat random; and c) reduce the chances that players will have much better or worse stats than other players.

I wanted to investigate how well it meets these three criteria, and whether we can do any better in our statistics. I focus mostly on the 4d6-drop-lowest ("4d6kh3") method, as that is my preferred method of stat generation.

# Individual stats

For individual stats, Goblin's caterpillar method produces a similar distribution of stats to 4d6-drop-lowest.

The average ability score is 12. The following chart shows the distribution of stats generated from caterpillar and 4d6-drop-lowest, run over 10,000 characters (and hence producing 60,000 stats). 

[comment]: <> (Insert chart).

Overall means that the probability of a character having a certain stat is roughly the same whether you use caterpillar or 4d6-drop-lowest - when looking at a single stat from either method. This is good, as in general we don't want to be using a stat generation method if it produces much higher or lower stats.

# Stat arrays

**However, across a character's stat array Goblin's caterpillar method does not significantly reduce the amount of volatility between different character's.** For example, the following table compares the probability of two scenarios: a player rolling "very good" stats (2+ stats above 15 and 0 or 1 stat below 10) or "very bad" stats (0 or 1 stat above 13 and 2+ stats below 10) stats.

|Scenario                                                 | 4d6-Drop<br>-Lowest | Goblin's <br>Caterpillar |
|---------------------------------------------------------|:-------------------:|:------------------------:|
| 2 or more stats above 15, <br>0 or 1 stat below 10 |         15%         |            14%           |
| 0 or 1 stat above 13, <br>2 or more stats below 10 |         14%         |            18%           |

For these two cases, there doesn't seem to be much difference between the two methods. And in roughly one-third of cases, a player can be expected to fall into one of these two scenarios. While the above is just an example of two scenarios, the Caterpillar method in general is not better than 4d6-drop-lowest at other definitions of very good and bad stats.

# Improving the method

**There is a better method. Follow Goblin's method as indicated, but instead of one stat being the sum of the *top* of the caterpillar, set one stat to be equal to the sum of the *bottom* (or "belly") of the caterpillar.** Let's called this the Improved Goblin's method (or maybe the Hobgoblin's method?). This keeps a similar distribution for individual stats as 4d6-drop-lowest (like Goblin's method.) However, it also reduces the probability of players having very different statistics. This can be seen by comparing the probability of a player rolling the same very good or very bad stats as we showed above.

|                                                         | 4d6<br>-drop-lowest | Goblin's <br>Caterpillar | Improved<br>Goblin's |
|---------------------------------------------------------|:-------------------:|:------------------------:|:--------------------:|
| 2 or more stats above 15, <br>only 0 or 1 stat below 10 |         15%         |            14%           |          5%          |
| Only 0 or 1 stat above 13, <br>2 or more stats below 10 |         14%         |            18%           |          10%         |

There is now less than one-sixth probability of rolling a "very good" or "very bad" roll.