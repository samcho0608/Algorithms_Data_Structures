# r,c starting from 1
# 0 empty
# 1 house
# 2 chicken delivery
# chicken distance == |r1 - r2| + |c1 - c2|
#   distance from house to nearest chicken delivery

# given m, max number of chicken deliveries to stay opened,
# find the minimum possible chicken distance of the city(sum of all chicken distances)
from sys import stdin
from itertools import combinations as comb
r = stdin.readline

n,m = map(int, r().strip().split())
city = [r().strip().split() for i in range(n)]
ans = 1e9
houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == '1':
            houses.append((i,j))
        elif city[i][j] == '2':
            chickens.append((i,j))

dists = [list(map(lambda x : abs(x[0]-c[0]) + abs(x[1]-c[1]), houses)) for c in chickens]
for co in comb((i for i in range(len(chickens))), m):
    res = sum(map(min, zip(*[dists[i] for i in co])))


    if res < ans:
        ans = res
print(ans)

# ans = 1e9
# for co in comb(chickens, m):
#     res = 0
#     for h in houses:
#         min_dist = 101
#         r,c = h
#         for ch in co:
#             y,x = ch[0], ch[1]
#             dist = abs(r-y) + abs(c-x)
#             if dist <= min_dist:
#                 min_dist = dist
#         res += min_dist
#     if res < ans:
#         ans = res
            
# print(ans)

# # this had to be done with brute force
