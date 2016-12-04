#!/usr/bin/env python3


def valid_triangle(a,b,c):
  if (a+b <= c) or (b+c <= a) or (a+c <= b):
    return False
  else:
    return True

with open('input.txt', 'r') as f:
  lines = f.readlines()

count = 0
i = 0
while i < len(lines):
  a1,a2,a3 = map(int, lines[i].strip().split())
  b1,b2,b3 = map(int, lines[i+1].strip().split())
  c1,c2,c3 = map(int, lines[i+2].strip().split())
  if valid_triangle(a1,b1,c1):
    count += 1
  if valid_triangle(a2,b2,c2):
    count += 1
  if valid_triangle(a3,b3,c3):
    count += 1
  i += 3


print(count)
