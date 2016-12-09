#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris


# wow this is devious guys... i see now i need a reverse polish notation
# what i have here actually works to calculate, but i kinda cheated.
# if there are any hanging characters in the string between multipliers
# (characters that aren't repeated), i completely miss the count!

# it's probably even worst than this :(


import string
translate_table = str.maketrans(string.ascii_uppercase, ' '*len(string.ascii_uppercase))

def process(code):
  code = code.translate(translate_table)
  to_multiply = code.split()
  adder = 0
  for x in to_multiply[::-1]:
    print(x)
    if ')(' in x: # more than 1 multipler here...
      _x = x.split(')(')
      print('More than 1 multipler here:', _x)
      # handle the last multiplier, and chop the trailing )
      a, b = map(int, _x.pop()[:-1].split('x'))
      tally = a * b
      print(' last set:', tally, '=', a, '*', b) 
      print(' len(_x)=', len(_x))
      if len(_x) > 1:
        # handle any middle multipliers, there should be no parens here
        for __x in _x[1:]:
          a, b = map(int, __x.split('x'))
          print(' middle set:', tally, '*=', b)
          tally *= b
      # handle first multipler, chop the leading (
      a, b = map(int, _x[0][1:].split('x'))
      print(' first set:', tally, '*=', b)
      tally *= b
      adder += tally
    else:
      # man it's too late to be doing this!
      a, b = map(int, x[1:-1].split('x'))
      adder += a * b
    print('ADDER=', adder)
  return adder
   
      
  

if __name__ == '__main__':

  with open('input.txt', 'r') as f:
    code = f.readline()

  print( process(code) )

