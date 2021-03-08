# given n
# find the ways to place n queens
# in an n x n board where non of them can attack each other

# from sys import stdin

# n = int(stdin.readline().strip())

# d = [0] * n
# def dfs(index, i):
#     d[index] = i
#     count = 0
#     for j in range(n):
#         if abs(i-j) != abs(d[i] - d[j]):
#             if i == n-1:
#                 count += 1
#             else:
#                 count += dfs(j)
#     d[i] = 0
#     return count

# count = 0

# for i in range(n):
#     count += dfs(i)

# print(count)

# o x o o
# o o o x
# x o o o
# o o x o

# o x o o o
# o o o x o
# x o o o o
# o o x o o
# o o o o x

from sys import stdin

n = int(stdin.readline().strip())
col = [False] * n
diag1 = [False] * (2 * n - 1) # / : [x + y]
diag2 = [False] * (2 * n - 1) # \ :[y - x + n - 1]
ans = 0

def dfs(i):
    global ans
    if i == n:
        ans += 1
        return

    for j in range(n):
        if not(col[j] or diag1[i+j] or diag2[i - j + n - 1]):
            col[j] = diag1[i+j] = diag2[i-j+n-1] = True
            dfs(i+1)
            col[j] = diag1[i+j] = diag2[i-j+n-1] = False



dfs(0)
print(ans)