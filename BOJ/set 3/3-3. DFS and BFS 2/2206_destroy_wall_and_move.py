from sys import stdin
from collections import deque
r = stdin.readline
n,m = map(int, r().strip().split())
mapp = [list(map(int, list(r().strip()))) for i in range(n)]
visited = [[[0,0] for _ in range(m)] for i in range(n)]
visited[0][0][0] = 1

def bfs():
    q = deque()
    q.append((0,0,0))
    while q:
        y,x,used = q.popleft()
        if y == n - 1 and x == m - 1:
            return visited[y][x][used]
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny, nx = y + dy, x + dx
            if ny in range(n) and nx in range(m) and not visited[ny][nx][used]:
                if not mapp[ny][nx]:
                    q.append((ny,nx,used))
                    visited[ny][nx][used] = 1 + visited[y][x][used]
                elif not used:
                    q.append((ny,nx, 1))
                    visited[ny][nx][1] = 1 + visited[y][x][used]
    return -1


print(bfs())






# SOLUTION:
# def main():
#     s = [[n - 1, m - 1, 1]]
#     visited = [[-1] * m for _ in range(n)]

#     uxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     dist = 1
#     while s:
#         ns = []
#         for x, y, j in s:
#             if x == 0 and y == 0:
#                 return dist
#             for dx, dy in uxy:
#                 c = x + dx
#                 d = y + dy
#                 if c < 0 or c >= n or d < 0 or d >= m:
#                     continue

#                 if (not wall[c][d]) and (visited[c][d] < j):
#                     visited[c][d] = j
#                     ns.append([c, d, j])

#                 elif j and wall[c][d]:
#                     visited[c][d] = 1
#                     ns.append([c, d, 0])
#         s = ns
#         dist += 1
#     return -1
# print(main())