from sys import stdin
from itertools import combinations as c
r = stdin.readline
n = int(r())
spec = [list(map(int, r().split())) for i in range(n)]
res = 100
indices = set(range(n))
combs = list(c(range(n), n//2))

for i in range(n):
    for j in range(i):
        spec[i][j] += spec[j][i]

for i in combs[:len(combs)//2]:
    n = 0
    for j in c(i, 2):
        x,y = j
        n += spec[y][x]
    for j in c(indices - set(i), 2):
        x,y = j
        n -= spec[y][x]
    
    n = abs(n)
    if n < res:
        res = n
print(res)

# Solution
# import sys
# from itertools import combinations as cb
# N = int(sys.stdin.readline()) // 2
# M = 2*N
# stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
# allstat = sum(newstat) // 2

# mins = 65535
# for l in cb(newstat[:-1], N):
#     mins = min(mins, abs(allstat - sum(l)))
# print(mins)