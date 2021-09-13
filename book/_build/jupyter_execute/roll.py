#!/usr/bin/env python
# coding: utf-8

# Generate Stats 
# ====================
# 
# To activate, click the rocket ship icon (top-right of window) and then click "Live Code". Wait for a notice to appear saying "Launching from mybinder.org: ready", and click "run" in the window below.

# In[1]:


import random
from scipy.spatial.transform import Rotation
import numpy as np

class Die:

  def __init__(self) -> None:
    self.left = 0
    self.right = 0
    self.top = 0
    self.bottom = 0
    self.front = 0
    self.back = 0

    self.unrolled_die = np.array([
      [-1, 0, 0], # 1 - facing left
      [ 0, 1, 0], # 2 - facing top
      [ 0, 0,-1], # 3 - facing front
      [ 0, 0, 1], # 4 - facing back
      [ 0,-1, 0], # 5 - facing bottom
      [ 1, 0, 0]  # 6 - facing right
    ])

    self.top_and_front_positions = np.array([
      [0, 1, 0],
      [0, 0,-1]
    ])

  def get_adjacent_edges(self, face: int) -> list:
    
    return ([i for i in range(1,7) if i not in [face, 7-face]])

  def sample(self) -> None:

    top_face = random.randint(1, 6)
    front_face = random.choice(self.get_adjacent_edges(top_face))

    top_face_coords = self.unrolled_die[top_face-1]
    front_face_coords = self.unrolled_die[front_face-1]
    top_and_front_faces = np.vstack((
      top_face_coords,
      front_face_coords
    ))

    # transformation representing the roling of the die
    transformation = np.dot(
      np.linalg.pinv(top_and_front_faces),
      self.top_and_front_positions
    )
    
    # make sure the left face rotates in tandem with the top and front faces
    col = np.where(np.all(transformation == 0, axis=0))[0]
    row = np.where(np.all(transformation == 0, axis=1))[0]
    transformation[row, col] = 1.0
    transformation[row, col] = np.linalg.det(transformation)

    rolled_die = np.dot(
      self.unrolled_die,
      transformation
    )

    left_face_coord = [-1, 0, 0]
    left_face_idx = np.where(
      np.all(rolled_die == left_face_coord, axis=1)
      )[0].item()
    left_face = left_face_idx + 1

    self.top = top_face
    self.front = front_face
    self.left = left_face
    
    self.bottom = 7 - self.top
    self.back = 7 - self.front
    self.right = 7 - self.left

  def __str__(self):
    output = f"top: {self.top}\n"
    output += f"front: {self.front}\n"
    output += f"back: {self.back}\n"
    output += f"bottom: {self.bottom}\n"
    output += f"left: {self.left}\n"
    output += f"right: {self.right}\n"
    return(output)


def get_dice(number: int) -> list:
  
  dice = []
  for i in range(number):
    d = Die()
    d.sample()
    dice.append(d)
  return(dice)

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

stat_array = caterpillar_stat_array2()

for i, stat in enumerate(stat_array):
  print(f"Stat {i+1} is {stat}")

print("--------------")
print(f"Total is {sum(stat_array)}")


# In[ ]:




