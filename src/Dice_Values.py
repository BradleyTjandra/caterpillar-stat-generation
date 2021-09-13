# Generate range of possible dice
import Die
import json
import StatArrays

dice = []
die = Die.Die()
for top in range(1, 7):
  adjacents = die.get_adjacent_edges(top)
  for front in adjacents:
    die.set_faces(top, front)
    dice.append(die.to_dict())


json.dumps(dice)

json.dumps(StatArrays.point_buy_dict)

# Possible dice 
# '[{"top": 1, "front": 2, "back": 5, "bottom": 6, "left": 3, "right": 4}, {"top": 1, "front": 3, "back": 4, "bottom": 6, "left": 5, "right": 2}, {"top": 1, "front": 4, "back": 3, "bottom": 6, "left": 2, "right": 5}, {"top": 1, "front": 5, "back": 2, "bottom": 6, "left": 4, "right": 3}, {"top": 2, "front": 1, "back": 6, "bottom": 5, "left": 4, "right": 3}, {"top": 2, "front": 3, "back": 4, "bottom": 5, "left": 1, "right": 6}, {"top": 2, "front": 4, "back": 3, "bottom": 5, "left": 6, "right": 1}, {"top": 2, "front": 6, "back": 1, "bottom": 5, "left": 3, "right": 4}, {"top": 3, "front": 1, "back": 6, "bottom": 4, "left": 2, "right": 5}, {"top": 3, "front": 2, "back": 5, "bottom": 4, "left": 6, "right": 1}, {"top": 3, "front": 5, "back": 2, "bottom": 4, "left": 1, "right": 6}, {"top": 3, "front": 6, "back": 1, "bottom": 4, "left": 5, "right": 2}, {"top": 4, "front": 1, "back": 6, "bottom": 3, "left": 5, "right": 2}, {"top": 4, "front": 2, "back": 5, "bottom": 3, "left": 1, "right": 6}, {"top": 4, "front": 5, "back": 2, "bottom": 3, "left": 6, "right": 1}, {"top": 4, "front": 6, "back": 1, "bottom": 3, "left": 2, "right": 5}, {"top": 5, "front": 1, "back": 6, "bottom": 2, "left": 3, "right": 4}, {"top": 5, "front": 3, "back": 4, "bottom": 2, "left": 6, "right": 1}, {"top": 5, "front": 4, "back": 3, "bottom": 2, "left": 1, "right": 6}, {"top": 5, "front": 6, "back": 1, "bottom": 2, "left": 4, "right": 3}, {"top": 6, "front": 2, "back": 5, "bottom": 1, "left": 4, "right": 3}, {"top": 6, "front": 3, "back": 4, "bottom": 1, "left": 2, "right": 5}, {"top": 6, "front": 4, "back": 3, "bottom": 1, "left": 5, "right": 2}, {"top": 6, "front": 5, "back": 2, "bottom": 1, "left": 3, "right": 4}]'

# Cumulative sum of point buy
# '{"17": 0.0095, "18": 0.0232, "19": 0.0394, "20": 0.0661, "21": 0.0988, "22": 0.1359, "23": 0.1821, "24": 0.2373, "25": 0.297, "26": 0.3502, "27": 0.4126, "28": 0.475, "29": 0.5399, "30": 0.6039, "31": 0.6582, "32": 0.7136, "33": 0.7656, "34": 0.8069, "35": 0.8458, "36": 0.8778, "37": 0.9078, "38": 0.9301, "39": 0.9524, "40": 0.9657, "41": 0.9743, "42": 0.9828, "43": 0.9896, "44": 0.9937, "45": 0.9966, "46": 0.9978, "47": 0.9986, "48": 0.9994, "49": 0.9999, "50": 1.0}'

# point buy mapping
# '{"3": -5, "4": -4, "5": -3, "6": -2, "7": -1, "8": 0, "9": 1, "10": 2, "11": 3, "12": 4, "13": 5, "14": 7, "15": 9, "16": 11, "17": 14, "18": 18}'

# Cumulative sum
# '{"65": 0.014, "66": 0.0443, "67": 0.0924, "68": 0.161, "69": 0.2538, "70": 0.3714, "71": 0.4893, "72": 0.6024, "73": 0.7066, "74": 0.7974, "75": 0.8698, "76": 0.9177, "77": 0.9532, "78": 0.9769, "79": 0.9905, "80": 0.9979, "81": 1.0}'