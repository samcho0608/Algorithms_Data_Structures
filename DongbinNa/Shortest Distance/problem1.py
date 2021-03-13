# UNFINISHED


# there are N cities willing to send a message to each other
# 
from sys import stdin
r = stdin.readline
INF = int(1e9)

n, m, c = map(int, r().split())
graph = [[]] + [[INF if i != j else 0 for j in range(n+1)] for i in range(n)]
for _ in range(m):
    x,y,z = map(int, r().split())
    graph[y][x] = z

greatest = 0
cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            temp = graph[i][j]
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if (temp in (INF,0)) and graph[i][j] != INF:
                cnt += 1
            if graph[i][j] != INF:
                greatest = max(greatest, graph[i][j])
            
                
print(cnt, greatest)
# print(graph)
