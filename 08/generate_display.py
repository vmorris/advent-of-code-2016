#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

debug = False

display = [ ['.']*50,
            ['.']*50,
            ['.']*50,
            ['.']*50,
            ['.']*50,
            ['.']*50 ]

def print_display():
  for line in display:
    print(''.join(line))
  print()

def tokenize_instruction(line):
  return line.strip().split()

def turn_on_pixel(x, y):
  display[y][x] = '#'

def turn_on_rect(area):
  if debug:
    print('inside turn_on_rect...')
  x, y = map(int, area[1].split('x'))
  if debug:
    print('   x =',x,', y =',y)
  for i in range(y):
    for j in range(x):
      display[i][j] = '#'

def rotate_right(l, n):
  result = l[-n:] + l[:-n]
  return result

def rotate_vertical(l, n):
  for _ in range(n):
    temp = display[5][l]
    display[5][l] = display[4][l] 
    display[4][l] = display[3][l]
    display[3][l] = display[2][l]
    display[2][l] = display[1][l]
    display[1][l] = display[0][l]
    display[0][l] = temp

def rotate_line(t):
  xy = int(t[2].split('=')[1])
  val = int(t[4])
  if debug:
    print('inside rotate_rect...')
  if t[1] == 'row':
    if debug:
      print('   rotating row y=', xy, 'by', val)
    display[xy] = rotate_right(display[xy], val)
  elif t[1] == 'column':
    if debug:
      print('   rotating column x=', xy, 'by', val)
    rotate_vertical(xy, val)
  else:
    exit(1)

if __name__ == '__main__':

  print_display()

  with open('input.txt', 'r') as f:
    lines = f.readlines()

  for line in lines:
    if debug:
      print("Instruction:",line)
    tokens = tokenize_instruction(line)
    if tokens[0] == 'rect':
      turn_on_rect(tokens)
    elif tokens[0] == 'rotate':
      rotate_line(tokens)
    else:
      exit(1)
    print_display()

  result = 0

  for line in display:
    result += line.count('#')

  print(result)
