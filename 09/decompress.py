#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

import re

p = re.compile('(^\w*)(\([0-9]+x[0-9]+\))(.*)')

debug = True

def process(code):
  match = re.search(p, code)
  if not match:
    return code
  else:
    if debug:
      print("Match found:")
      print("  mg1=", match.group(1))
      print("  mg2=", match.group(2))
      print("  mg3=", match.group(3))
    # get our next expansion from the match
    a, b = match.group(2).split('x')
    chars = int(a[1:])
    multiple = int(b[:-1])
    to_keep = match.group(1)
    remaining_code = match.group(3)
    repeated = remaining_code[:chars]*multiple
    # when we return here, we need to fix up the results while unwinding
    return to_keep + repeated + process(remaining_code[chars:])
    
  

if __name__ == '__main__':

  with open('input.txt', 'r') as f:
    code = f.readline()

  result = process(code)
  if debug:
    print("RESULT=",result)
  print(len(result))

