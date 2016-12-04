#!/usr/bin/env python3


with open('input.txt', 'r') as f:
  lines = f.readlines()

count = 0

for line in lines:
  a,b,c = map(int, line.split())
  print("a=",a,"b=",b,"c=",c)
  if (a+b <= c):
    print(a,"+",b,"LE",c)
    continue
  elif (b+c <= a):
    print(b,"+",c,"LE",a)
    continue
  elif (a+c <= b):
    print(a,"+",c,"LE",b)
    continue
  else:
    count += 1

print(count)
