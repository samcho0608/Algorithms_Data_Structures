# given n elements in an array
# find the number of all possibilities where the sum is S

# example input
# 5 0
# -7 -3 -2 5 8

from itertools import combinations
from sys import stdin
r = stdin.readline

n, s = map(int, r().split())
array = list(map(int, r().split()))
count = 0
for i in range(1, n + 1):
    for c in combinations(array, i):
        if sum(c) == s:
            count += 1

print(count)