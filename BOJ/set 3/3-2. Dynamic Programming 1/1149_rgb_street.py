from sys import stdin
r = stdin.readline

n = int(r())
houses = [list(map(int, r().strip().split()))]


for i in range(1, n):
    houses.append(list(map(int, r().strip().split())))
    for j in range(3):
        houses[i][j] = min([houses[i][j] + houses[i-1][a] for a in range(3) if a != j])
print(min(houses[n-1]))