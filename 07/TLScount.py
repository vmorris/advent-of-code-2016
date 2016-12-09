#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

def tokenize_IP(ip):
  ''' given an IP string, return two lists, one which contains the contents of any found square brakets
      and second list contains strings outside square brackets '''
  inside = []
  outside = []
  tokens = ip.split('[')
  for token in tokens:
    if ']' in token:
      # inside, followed by outside
      a,b = token.split(']')
      inside.append(a)
      outside.append(b)
    else:
      # outside found
      outside.append(token)
  return inside, outside

def has_ABBA(line):
  ''' given a line, search for ABBA pattern '''
  for i in range(len(line)-3):
    if line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
      return True
  return False

if __name__ == "__main__":
  count = 0
  with open('input.txt', 'r') as f:
    for line in f:
      inside, outside = tokenize_IP(line.strip())
      good_line = False
      for i in outside:
        if has_ABBA(i):
          good_line = True
      for i in inside:
        if has_ABBA(i):
          good_line = False
      if good_line:
        count += 1

  print(count)
