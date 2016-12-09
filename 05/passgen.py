#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

import hashlib

digitsFound = 0
i = 0
while digitsFound < 8:
  to_encode = "ffykfhsq"+str(i)
  encoded = hashlib.md5(to_encode.encode('utf-8')).hexdigest()
  if encoded.startswith("00000"):
    print("to_encode:", to_encode)
    print(encoded[:6])
    digitsFound += 1
  i += 1
