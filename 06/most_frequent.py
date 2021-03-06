#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

import collections

letters = [""]*8


if __name__ == "__main__":
  with open('input.txt', 'r') as f:
    for line in f:
      for i,l in enumerate(line.strip()):
        letters[i] = letters[i] + l
   
    result = ""
 
    for l in letters:
      result += collections.Counter(l).most_common(1)[0][0]

    print(result)

