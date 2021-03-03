# given two arrays, only sort out the first to
# minimize the sum of product of elements in the same index of each array

# basically we gotta pair the minimum of the first array to be
# pair with the maximum of the second

import sys

n = int(input())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

res = 0
for i in range(n):
    res += sorted(a)[i] * sorted(b, reverse = True)[i]

print(res)