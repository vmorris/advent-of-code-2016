#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

def changeDirection(start, new):
  ''' start is a cardinal direction N, S, E, W and
      new is L or R. returns the new cardinal direction.'''
  if not any(x in 'LR' for x in new):
    raise ValueError('new direction is not "L" or "R"')
  if start == "N":
    if new == "L":
      return "W"
    else: return "E"
  elif start == "S":
    if new == "L":
      return "E"
    else: return "W"
  elif start == "E":
    if new == "L":
      return "N"
    else: return "S"
  elif start == "W":
    if new == "L":
      return "S"
    else: return "N"
  else:
    raise ValueError('start must be "N", "S", "E", or "W".') 

with open('input.txt', 'r') as inputfile:
  data = list(map(str.lstrip, inputfile.read().strip().split(',')))

position = [0,0]
direction = "N"

for d in data:
  print("We are at", position, " and are facing", direction)
  print("Next move is", d)
  direction = changeDirection(direction, d[0])
  magnitude = int(d[1:])
  if direction == "N":
    position[1] += magnitude
  elif direction == "S":
    position[1] -= magnitude
  elif direction == "E":
    position[0] += magnitude
  elif direction == "W":
    position[0] -= magnitude
  else:
    raise ValueError('unable to determine changed cardinal direction')
   
print(abs(position[0]) + abs(position[1]))

