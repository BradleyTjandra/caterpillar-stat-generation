import Die
import numpy as np

point_buy_dict = {
  3 : -5,
  4 : -4,
  5 : -3,
  6 : -2,
  7 : -1,
  8 : 0,
  9 : 1,
  10 : 2,
  11 : 3,
  12 : 4,
  13 : 5,
  14 : 7,
  15 : 9,
  16 : 11,
  17 : 14,
  18 : 18,
}

num_ability_scores = 6

def get_dice(number: int) -> list:
  
  dice = []
  for i in range(number):
    d = Die.Die()
    d.sample()
    dice.append(d)
  return(dice)

def caterpillar_stat_array() -> list:
  
  dice = get_dice(3)
  
  # caterpillar method, as seen here
  # https://goblinshenchman.wordpress.com/2020/08/15/caterpillar-method-for-character-stat-generation/
  stat_array = []
  stat_array.append(dice[0].front + dice[1].front + dice[2].front)
  stat_array.append(dice[0].top + dice[1].top + dice[2].top)
  stat_array.append(dice[0].back + dice[1].back + dice[2].back)
  stat_array.append(dice[0].left + dice[0].back + dice[0].top + dice[0].front)
  stat_array.append(dice[2].right + dice[2].back + dice[2].top + dice[2].front)
  stat_array.append(dice[1].back + dice[1].top + dice[1].front + (dice[1].bottom if dice[1].front > 3 else 0))

  return(stat_array)

def caterpillar_stat_array2() -> list:
  
  dice = get_dice(3)
  
  stat_array = []
  stat_array.append(dice[0].front + dice[1].front + dice[2].front)
  stat_array.append(dice[0].bottom + dice[1].bottom + dice[2].bottom)
  stat_array.append(dice[0].back + dice[1].back + dice[2].back)
  stat_array.append(dice[0].left + dice[0].back + dice[0].top + dice[0].front)
  stat_array.append(dice[2].right + dice[2].back + dice[2].top + dice[2].front)
  stat_array.append(dice[1].back + dice[1].top + dice[1].front + (dice[1].bottom if dice[1].front > 3 else 0))

  return(stat_array)

def caterpillar_stat_array3() -> list:
  
  dice = get_dice(3)
  
  stat_array = []
  stat_array.append(dice[0].front + dice[1].front + dice[2].front)
  stat_array.append(dice[0].bottom + dice[1].bottom + dice[2].bottom)
  stat_array.append(dice[0].back + dice[1].back + dice[2].back)

  head1 = dice[0].left + dice[0].back + dice[0].top + dice[0].front
  head2 = dice[2].right + dice[2].back + dice[2].top + dice[2].front
  tail1 = -dice[0].left + dice[0].back + dice[0].top + dice[0].front
  tail2 = -dice[2].right + dice[2].back + dice[2].top + dice[2].front

  if head1 + tail2 > head2 + tail1:
    stat_array.extend([head1, tail2])
  else:
    stat_array.extend([head2, tail1])

  stat_array.append(dice[1].back + dice[1].top + dice[1].front)

  return(stat_array)

def caterpillar_with_one_random_die() -> list:
  
  dice = get_dice(3)
  
  stat_array = []
  stat_array.append(dice[0].front + dice[1].front + dice[2].front)
  stat_array.append(dice[0].back + dice[1].back + dice[2].back)
  stat_array.append(dice[0].left + dice[0].back + dice[0].top + dice[0].front)
  stat_array.append(dice[2].right + dice[2].back + dice[2].top + dice[2].front)
  stat_array.append(dice[1].back + dice[1].top + dice[1].front + (dice[1].bottom if dice[1].front > 3 else 0))
  stat_array.append(sum(np.random.randint(low = 1, high = 7, size = [3])))
  
  return(stat_array)

def four_d_six_drop_lowest() -> list:

  # roll four dice, and drop the lowest
  four_d_six = np.random.randint(low = 1, high = 7, size = [6, 4])
  drop_lowest = np.sort(four_d_six, axis=-1)[:, 1:]
  stat_array = list(drop_lowest.sum(axis=1))
  return(stat_array)


def three_d_six() -> list:

  # roll three dice
  three_d_six = np.random.randint(low = 1, high = 7, size = [6, 3])
  stat_array = list(three_d_six.sum(axis=1))
  return(stat_array)

def caterpillar_3d6() -> list:

  dice = get_dice(3)
  
  stat_array = []
  stat_array.append(dice[0].front + dice[1].front + dice[2].front)
  stat_array.append(dice[0].top + dice[1].top + dice[2].top)
  stat_array.append(dice[0].back + dice[1].back + dice[2].back)
  stat_array.append(dice[0].left + dice[0].back + dice[0].top + dice[0].front)
  stat_array.append(-dice[2].right + dice[2].back + dice[2].top + dice[2].front)
  stat_array.append(dice[1].back + dice[1].top + dice[1].front)

  return(stat_array)

def caterpillar_v2_3d6() -> list:

  dice = get_dice(3)
    
  stat_array = []
  stat_array.append(dice[0].front + dice[1].front + dice[2].front)
  stat_array.append(dice[0].bottom + dice[1].bottom + dice[2].bottom)
  stat_array.append(dice[0].back + dice[1].back + dice[2].back)
  stat_array.append(dice[0].left + dice[0].back + dice[0].top + dice[0].front)
  stat_array.append(-dice[2].right + dice[2].back + dice[2].top + dice[2].front)
  stat_array.append(dice[1].back + dice[1].top + dice[1].front)

  return(stat_array)