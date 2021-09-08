# The Caterpillar Method for D&D Character Stat Generation

## tl;dr

Goblin's [caterpillar method](https://goblinshenchman.wordpress.com/2020/08/15/caterpillar-method-for-character-stat-generation/) of generating stats doesn't actually reduce the probability that some players will roll really good stats, and others will roll really low stats.

There is a better method. Follow Goblin's method as indicated, but instead of one stat being the sum of the *top* of the caterpillar, set one stat to be equal to the sum of the *bottom* (or "belly") of the caterpillar.

For example, to replicate the 4d6-drop-lowest:

* **Stat 1:** Add up the front face
* **Stat 2:** Add up the *bottom* face - this is the only change to Goblin's method.
* **Stat 3:** Add up the back 
* **Stat 4:** Add up all exposed faces on the left-most cube
* **Stat 5:** Add up all exposed faces on the right-most cube
* **Stat 6:** Add up all exposed faces on the centre cube. If the front face is a 4, 5 or 6, then also add the bottom face.

## Summary

### Context

Recently Goblin's Henchman (Goblin) shared an [article on their blog](https://goblinshenchman.wordpress.com/2020/08/15/caterpillar-method-for-character-stat-generation/) about using different sides of the same dice to generate stats for characters in D&D.

The suggested method sounds appealing because it aims to a) allow players to have different stats; b) make those stats somewhat random; and c) reduce the chances that players will have much better or worse stats than other players.

I wanted to investigate how well it meets these three criteria, and whether we can do any better in our statistics. I focus mostly on the 4d6-drop-lowest ("4d6kh3") method, as that is my preferred method of stat generation.

### Comparing individual stats to 4d6-drop-lowest

**For individual stats, Goblin's caterpillar method produces a similar distribution of stats to 4d6-drop-lowest.** The average ability score is 12. The following chart shows the distribution of stats generated from caterpillar and 4d6-drop-lowest, run over 10,000 characters (and hence producing 60,000 stats). ^^Insert chart^^.

Overall means that the probability of a character having a certain stat is roughly the same whether you use caterpillar or 4d6-drop-lowest - when looking at a single stat from either method. This is good, as in general we don't want to be using a stat generation method if it produces much higher or lower stats.

### Comparing overall stat arrays to 4d6-drop-lowest

**However, across a character's stat array Goblin's caterpillar method does not significantly reduce the amount of volatility between different character's.** For example, the following table compares the probability of two scenarios: a player rolling "very good" stats (2+ stats above 15 and 0 or 1 stat below 10) or "very bad" stats (0 or 1 stat above 13 and 2+ stats below 10) stats.

|Scenario                                                 | 4d6-Drop<br>-Lowest | Goblin's <br>Caterpillar |
|---------------------------------------------------------|:-------------------:|:------------------------:|
| 2 or more stats above 15, <br>0 or 1 stat below 10 |         15%         |            14%           |
| 0 or 1 stat above 13, <br>2 or more stats below 10 |         14%         |            18%           |

For these two cases, there doesn't seem to be much difference between the two methods. And in roughly one-third of cases, a player can be expected to fall into one of these two scenarios. While the above is just an example of two scenarios, the Caterpillar method in general is not better than 4d6-drop-lowest at other definitions of very good and bad stats.

### Improving the caterpillar method

**There is a better method. Follow Goblin's method as indicated, but instead of one stat being the sum of the *top* of the caterpillar, set one stat to be equal to the sum of the *bottom* (or "belly") of the caterpillar.** Let's called this the Improved Goblin's method (or maybe the Hobgoblin's method?). This keeps a similar distribution for individual stats as 4d6-drop-lowest (like Goblin's method.) However, it also reduces the probability of players having very different statistics. This can be seen by comparing the probability of a player rolling the same very good or very bad stats as we showed above.

|                                                         | 4d6<br>-drop-lowest | Goblin's <br>Caterpillar | Improved<br>Goblin's |
|---------------------------------------------------------|:-------------------:|:------------------------:|:--------------------:|
| 2 or more stats above 15, <br>only 0 or 1 stat below 10 |         15%         |            14%           |          5%          |
| Only 0 or 1 stat above 13, <br>2 or more stats below 10 |         14%         |            18%           |          10%         |

There is now less than one-sixth probability of rolling a "very good" or "very bad" roll.

## Context

Recently Goblin's Henchman (Goblin) shared an [article on their blog](https://goblinshenchman.wordpress.com/2020/08/15/caterpillar-method-for-character-stat-generation/) about using different sides of the same dice to generate stats for characters in D&D.

The suggested method sounds appealing to me because it purports to:

1. It allows players to have different stats. This makes it better than the standard array and (to some extent) point-buy.
2. It makes stats somewhat random, so that players can have more unique characters without needing to worry about whether they should be min-maxing. This makes it better than point-buy
3. Reduce the chances that players will have much better or worse stats than other players. This makes it better than 4d6-drop-lowest.
4. It generally produces higher numbers. This makes it better than the standard array (where the average score is 10.5) or 3d6.

These desiderata may not be important for you, but I felt they were sometimes issues enough that the potential for a different approach interests me.

I wanted to investigate how well it meets these three criteria, and whether we can do any better in our statistics. I focus mostly on the 4d6-drop-lowest ("4d6kh3") method, as that is my preferred method of stat generation.

All of the code used to generate these statistics can be seen here ^^link.

## Comparing individual stats to 4d6-drop-lowest

Goblin's analysis focuses on the distribution of individual stats. If we do this, we can see that Goblin's method and 4d6-drop-lowest have a similar 