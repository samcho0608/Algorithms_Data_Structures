# n, m = map(int, input().split())
# spots = [list(input()) for i in range(n)]
# count = 0
# visited = []

# # my implementation
# def dfs(i,j):
#     global visited
#     if spots[i][j] == '0':
#         visited.append((i,j))
#         for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
#             ni, nj = i+di, j+dj
#             if ni not in range(n) or nj not in range(m) or (ni,nj) in visited:
#                 continue
#             dfs(ni, nj)

# for i in range(n):
#     for j in range(m):
#         if (i,j) not in visited and spots[i][j] == '0':
#             count += 1
#             dfs(i,j)

# print(count)

# solution
n, m = map(int, input().split())
graph = [list(input()) for i in range(n)]

def dfs(x,y):
    if x not in range(n) or y not in range(m):
        return False
    if graph[x][y] == '0':
        graph[x][y] = '1'
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1

print(result)