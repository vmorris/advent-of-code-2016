#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

import hashlib

code = [None, None, None, None, None, None, None, None]

def print_code():
  print("".join(['_' if v is None else v for v in code]))

i = 0
while None in code:
  to_encode = "ffykfhsq"+str(i)
  encoded = hashlib.md5(to_encode.encode('utf-8')).hexdigest()
  if encoded.startswith("00000") and encoded[5].isdigit():
    try:
      if code[int(encoded[5])] == None:
        code[int(encoded[5])] = encoded[6]
        print_code()
    except IndexError:
      pass
  i += 1
  

