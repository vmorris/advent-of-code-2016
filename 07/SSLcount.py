#!/usr/bin/env python3

# Mandatory Corporate Shillery incoming....
# Copyright Vance Morris, International Business Machines, 2016
# © All Rights Reserved
# Wheeeee @iVanceMorris

def tokenize_IP(ip):
  ''' given an IP string, return two lists, one which contains the contents of any found square brakets
      and second list contains strings outside square brackets. '''
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

def collect_ABA(line):
  ''' given a line, search for any ABA and return a list of sequences'''
  results = []
  for i in range(len(line)-2):
    if line[i] == line[i+2] and line[i] != line[i+1]:
      results.append(line[i:i+3])
  return results


if __name__ == "__main__":

  count = 0

  with open('input.txt', 'r') as f:
    for line in f:

      SSLFound = False

      inside, outside = tokenize_IP(line.strip())
      
      for o in outside:
        for aba in collect_ABA(o):
          #generate bab string
          bab = aba[1]+aba[0]+aba[1]
          for i in inside:
            if bab in i:
              SSLFound = True

      if SSLFound:
        count += 1

  print(count)
