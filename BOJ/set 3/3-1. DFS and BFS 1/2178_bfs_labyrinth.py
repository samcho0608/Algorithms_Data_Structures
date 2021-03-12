# sam is in a n x m labyrinth
# sam starts at (1,1) and the exit is at (n,m)
# 0 for where the monster is
# 1 for where u can move to

# find the min num of squares sam should visit to exit
# count includes start and exit

# My implementation
# n, m = map(int, input().split())
# graph = [list(input()) for i in range(n)]

# def dfs(i,j):
#     global graph
#     if graph[i][j] == '0':
#         return 0
#     if (i,j) == (n - 1, m - 1):
#         return 1
#     moves = []
#     graph[i][j] = '0'
#     if i + 1 in range(n):
#         moves.append(dfs(i+1,j))
#     if i - 1 in range(n):
#         moves.append(dfs(i-1,j))
#     if j + 1 in range(m):
#         moves.append(dfs(i,j+1))
#     if j - 1 in range(m):
#         moves.append(dfs(i,j-1))
#     graph[i][j] = '1'
#     moves = [i for i in moves if i > 0]
#     return min(moves) + 1 if moves else 0

# print(dfs(0,0))


# solution
n, m = map(int, input().split())
graph = [list(map(int, input())) for i in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    queue = [(x,y)]
    while queue:
        x,y = queue.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx not in range(n) or ny not in range(m):
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.insert(0, (nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
