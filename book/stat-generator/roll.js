"use strict";

let possibleDice = JSON.parse('[{"top": 1, "front": 2, "back": 5, "bottom": 6, "left": 3, "right": 4}, {"top": 1, "front": 3, "back": 4, "bottom": 6, "left": 5, "right": 2}, {"top": 1, "front": 4, "back": 3, "bottom": 6, "left": 2, "right": 5}, {"top": 1, "front": 5, "back": 2, "bottom": 6, "left": 4, "right": 3}, {"top": 2, "front": 1, "back": 6, "bottom": 5, "left": 4, "right": 3}, {"top": 2, "front": 3, "back": 4, "bottom": 5, "left": 1, "right": 6}, {"top": 2, "front": 4, "back": 3, "bottom": 5, "left": 6, "right": 1}, {"top": 2, "front": 6, "back": 1, "bottom": 5, "left": 3, "right": 4}, {"top": 3, "front": 1, "back": 6, "bottom": 4, "left": 2, "right": 5}, {"top": 3, "front": 2, "back": 5, "bottom": 4, "left": 6, "right": 1}, {"top": 3, "front": 5, "back": 2, "bottom": 4, "left": 1, "right": 6}, {"top": 3, "front": 6, "back": 1, "bottom": 4, "left": 5, "right": 2}, {"top": 4, "front": 1, "back": 6, "bottom": 3, "left": 5, "right": 2}, {"top": 4, "front": 2, "back": 5, "bottom": 3, "left": 1, "right": 6}, {"top": 4, "front": 5, "back": 2, "bottom": 3, "left": 6, "right": 1}, {"top": 4, "front": 6, "back": 1, "bottom": 3, "left": 2, "right": 5}, {"top": 5, "front": 1, "back": 6, "bottom": 2, "left": 3, "right": 4}, {"top": 5, "front": 3, "back": 4, "bottom": 2, "left": 6, "right": 1}, {"top": 5, "front": 4, "back": 3, "bottom": 2, "left": 1, "right": 6}, {"top": 5, "front": 6, "back": 1, "bottom": 2, "left": 4, "right": 3}, {"top": 6, "front": 2, "back": 5, "bottom": 1, "left": 4, "right": 3}, {"top": 6, "front": 3, "back": 4, "bottom": 1, "left": 2, "right": 5}, {"top": 6, "front": 4, "back": 3, "bottom": 1, "left": 5, "right": 2}, {"top": 6, "front": 5, "back": 2, "bottom": 1, "left": 3, "right": 4}]');
let distribution = JSON.parse('{"65": 0.014, "66": 0.0443, "67": 0.0924, "68": 0.161, "69": 0.2538, "70": 0.3714, "71": 0.4893, "72": 0.6024, "73": 0.7066, "74": 0.7974, "75": 0.8698, "76": 0.9177, "77": 0.9532, "78": 0.9769, "79": 0.9905, "80": 0.9979, "81": 1.0}');
// let pointBuyMapping = JSON.parse('{"3": -5, "4": -4, "5": -3, "6": -2, "7": -1, "8": 0, "9": 1, "10": 2, "11": 3, "12": 4, "13": 5, "14": 7, "15": 9, "16": 11, "17": 14, "18": 18}');
let distributionOrig = JSON.parse('{"52": 0.0001, "53": 0.0006, "54": 0.0015, "55": 0.0036, "56": 0.007, "57": 0.0114, "58": 0.0182, "59": 0.0272, "60": 0.0384, "61": 0.0533, "62": 0.074, "63": 0.0986, "64": 0.1313, "65": 0.1703, "66": 0.2122, "67": 0.2589, "68": 0.3094, "69": 0.3642, "70": 0.4189, "71": 0.4789, "72": 0.5394, "73": 0.6008, "74": 0.6587, "75": 0.7148, "76": 0.7653, "77": 0.8108, "78": 0.8506, "79": 0.8851, "80": 0.9141, "81": 0.938, "82": 0.9584, "83": 0.9732, "84": 0.9844, "85": 0.9921, "86": 0.9965, "87": 0.9989, "88": 0.9998, "89": 1.0}');

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}

function getRandomDie() {
  let i = getRandomInt(0,24);
  return(possibleDice[i]);
}

let statElems = [1, 2, 3, 4, 5, 6].map( (item) => document.getElementById("stat"+item) );
let totalStats = document.getElementById("totalStats");
let comment = document.getElementById("comment");
let methodChoiceElem = document.getElementById("methodChoice");
let methodHeaderElem = document.getElementById("methodHeader");
let captionElem = document.getElementById("caption");

function onRerollClick() {

  if (methodChoiceElem.value == "goblin") origGoblinRoll();
  else improvedGoblinRoll();
  
}

function improvedGoblinRoll() {

  methodHeaderElem.innerHTML = 'Improved Caterpillar method'
  captionElem.innerHTML = 'Based on the <a href="https://bradleytjandra.github.io/caterpillar-stat-generation/">Improved Caterpillar method.';

  let dice = [1, 2, 3].map(getRandomDie);
  statElems[0].innerHTML = dice[0].front + dice[1].front + dice[2].front;
  statElems[1].innerHTML = dice[0].bottom + dice[1].bottom + dice[2].bottom;
  statElems[2].innerHTML = dice[0].back + dice[1].back + dice[2].back;
  statElems[3].innerHTML = dice[0].left + dice[0].back + dice[0].top + dice[0].front;
  statElems[4].innerHTML = dice[2].right + dice[2].back + dice[2].top + dice[2].front;
  statElems[5].innerHTML = dice[1].back + dice[1].top + dice[1].front;
  
  if (dice[1].front > 3) {
    statElems[5].innerHTML = parseInt(statElems[5].innerHTML) + dice[1].bottom;
  } 

  totalStats.innerHTML = statElems.reduce( (sum, elem) => {
    return(sum + parseInt(elem.innerHTML));
  }, 0);

  let cdf = distribution[parseInt(totalStats.innerHTML)];
  if (cdf < 0.5) {
    comment.innerHTML = `You scored in the bottom ${(cdf*100).toFixed(1)}% of stat arrays. How unlucky!`;
  } else {
    let better_than = 1 - distribution[parseInt(totalStats.innerHTML)-1];
    comment.innerHTML = `You scored in the top ${(better_than*100).toFixed(1)}% of stat arrays. Congrats!`;
  }
}

function origGoblinRoll() {

  methodHeaderElem.innerHTML = 'Original Goblin Caterpillar method'
  captionElem.innerHTML = '<div>Based on <a href="https://bradleytjandra.github.io/caterpillar-stat-generation/context.html#goblin-s-caterpillar-method/">Goblin\'s Caterpillar method.</a></div>';

  let dice = [1, 2, 3].map(getRandomDie);
  statElems[0].innerHTML = dice[0].front + dice[1].front + dice[2].front;
  statElems[1].innerHTML = dice[0].top + dice[1].top + dice[2].top;
  statElems[2].innerHTML = dice[0].back + dice[1].back + dice[2].back;
  statElems[3].innerHTML = dice[0].left + dice[0].back + dice[0].top + dice[0].front;
  statElems[4].innerHTML = dice[2].right + dice[2].back + dice[2].top + dice[2].front;
  statElems[5].innerHTML = dice[1].back + dice[1].top + dice[1].front;
  
  if (dice[1].front > 3) {
    statElems[5].innerHTML = parseInt(statElems[5].innerHTML) + dice[1].bottom;
  } 

  totalStats.innerHTML = statElems.reduce( (sum, elem) => {
    return(sum + parseInt(elem.innerHTML));
  }, 0);

  let cdf = distributionOrig[parseInt(totalStats.innerHTML)];
  if (cdf < 0.5) {
    comment.innerHTML = `You scored in the bottom ${(cdf*100).toFixed(1)}% of stat arrays. How unlucky!`;
  } else {
    let better_than = 1 - distributionOrig[parseInt(totalStats.innerHTML)-1];
    comment.innerHTML = `You scored in the top ${(better_than*100).toFixed(1)}% of stat arrays. Congrats!`;
  }
}

onRerollClick();