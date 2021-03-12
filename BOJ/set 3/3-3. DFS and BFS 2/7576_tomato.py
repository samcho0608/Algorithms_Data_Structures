from sys import stdin
from collections import deque
r = stdin.readline

n,m = map(int, r().split())
box = []
tomato = 0
q = deque()
for i in range(m):
    line = list(map(int, r().split()))
    for j in range(n):
        if line[j] == 0:
            tomato += 1
        if line[j] == 1:
            q.append((i,j))
    box.append(line)

def bfs(tomato):
    if tomato == 0:
        return 0
    delta = [(0,-1),(0,1),(-1,0),(1,0)]
    days = 0
    while q and tomato:
        y,x = q.popleft()
        for dy,dx in delta:
            ny, nx = y + dy, x + dx
            if ny in range(m) and nx in range(n) and not box[ny][nx]:
                box[ny][nx] = 1 + box[y][x]
                days = max(box[ny][nx], days)
                q.append((ny,nx))
                tomato -= 1
    return days - 1 if not tomato else -1
print(bfs(tomato))
