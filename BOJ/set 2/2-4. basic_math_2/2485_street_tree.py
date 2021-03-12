# 
# from functools import reduce
from sys import stdin
from math import gcd
r = stdin.readline
n = int(r())
prev = int(r())
d = []
for i in range(n-1):
    curr = int(r())
    d.append(curr - prev)
    prev = curr
n= len(d)
f = gcd(*d)
print(sum(_//f for _ in d) - n)