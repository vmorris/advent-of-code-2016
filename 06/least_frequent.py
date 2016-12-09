#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

import collections

letters = [""]*8

def least_freq(c):
  ''' given a Counter object, return the key with the least counts '''
  return min(c.items(), key=lambda x: x[1])[0]

if __name__ == "__main__":
  with open('input.txt', 'r') as f:
    for line in f:
      for i,l in enumerate(line.strip()):
        letters[i] = letters[i] + l
   
    result = "" 
    for l in letters:
      result += least_freq(collections.Counter(l))

    print(result)
