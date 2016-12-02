#!/usr/bin/env python3


with open('input.txt', 'r') as f:
  lines = f.readlines()

pad = ( [None, None,  '1', None, None],
        [None,  '2',  '3',  '4', None],
        [ '5',  '6',  '7',  '8',  '9'],
        [None,  'A',  'B',  'C', None],
        [None, None,  'D', None, None] )

x = 0
y = 2
position = pad[y][x]

for line in lines:
  l = ''.join(line.strip().split())

  for d in l:
    if (d == "L" and x != 0) and (pad[y][x-1] != None):
      x -= 1
    elif (d == "R" and x != 4) and (pad[y][x+1] != None):
      x += 1
    elif (d == "U" and y != 0) and (pad[y-1][x] != None):
      y -= 1
    elif (d == "D" and y != 4) and (pad[y+1][x] != None):
      y += 1
    else:
      pass
    
    position = pad[y][x]

  print('position=',position)

