Context
============================

In D&D, character creation involves creating six numbers ("stats") which represent how good you are at six different areas. These six different stats become your "stat array".

There are numerous ways to create stat arrays. While some ways are deterministic (i.e. you get to choose what number each stat is, subject to some constraints), a common method to add some randomisation to this process is called "4d6-drop-lowest". Under this method, you roll four dice and sum up the numbers on the three highest dice. The resulting sum becomes one of your stats [^1]. This is repeated for the other five stats.

[^1]: This stat may receive additional bonuses or penalties based on other character building choices, but these do not interact with the initial stat array generation so I am ignoring them.
## Issues with 4d6-drop-lowest

While this method allows for some randomisation, it can also lead to characters with consistently high or low stats. This can have a few issues:

* Player characters in the same party may not be able perform at the same level, and one player may feel their character is less powerful. 
* It makes it harder for the Dungeon Master (DM) to design challenges for the players, as player characters may be more or less powerful than what the "standard rules" expect.
* It requires more work to balance encounters for the players, as what is very easy for one player character who rolled high stats may be incredibly difficult for another player who rolled lower stats. 

## Goblin's Caterpillar Method

Recently Goblin's Henchman (Goblin) shared an [article on their blog](https://goblinshenchman.wordpress.com/2020/08/15/caterpillar-method-for-character-stat-generation/) about using different sides of the same dice to generate stats for characters in D&D.

The general idea is that, instead of using 4d6-drop-lowest, you would roll the stats using the following rules:

* **Stat 1:** Add up the front face
* **Stat 2:** Add up the top face
* **Stat 3:** Add up the back face
* **Stat 4:** Add up all exposed faces on the left-most cube
* **Stat 5:** Add up all exposed faces on the right-most cube
* **Stat 6:** Add up all exposed faces on the centre cube. If the front face is a 4, 5 or 6, then also add the bottom face.

This purports to reduce the possibility that some characters will be much more powerful than others. However, as I show later in this article, it doesn't actually do a good job at achieving this. You are equally like to roll a very powerful character, or a very weak character, using this method as you are with 4d6-drop-lowest.

## Improved Caterpillar Method

However, Goblin's idea of using the opposite side of dice seems clever, and the method can be easily tweaked to correctly achieve a less variable character generation method. I call this the **Improved Caterpillar** method:

* **Stat 1:** Add up the front face
* **Stat 2:** Add up the *bottom* face - this is the only change to Goblin's method.
* **Stat 3:** Add up the back face
* **Stat 4:** Add up all exposed faces on the left-most cube
* **Stat 5:** Add up all exposed faces on the right-most cube
* **Stat 6:** Add up all exposed faces on the centre cube. If the front face is a 4, 5 or 6, then also add the bottom face.

## Summary

Stat generation is an important part of building characters in D&D. 4d6-drop-lowest and the Goblin Method don't do a good job at avoiding very strong or very weak characters. Instead, the Improved Caterpillar is a better stat generation method to use.

The next section will first consider how these three methods compare based on the average stat generated.