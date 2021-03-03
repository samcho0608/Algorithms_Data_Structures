# Gold Mine
# nxm mine, each cell containing a certain amt of gold
# starts on any row of first column and can move to right, right up, or right down
# for m-1 times

# find the max amt of gold one can find

n,m = map(int, input().split())

mine = [list(map(int, input().split())) for i in range(n)]
d = [[0] * m for i in range(n)]

for j in range(n):
    d[j][0] = mine[j][0]

for i in range(1, m):
    for j in range(n):
        options = [d[j][i-1]]
        if j + 1 in range(n):
            options.append(d[j+1][i-1])
        if j - 1 in range(n):
            options.append(d[j-1][i-1])
        d[j][i] = mine[j][i] + max(options)

print(max(d[n - 1][i] for i in range(m)))
