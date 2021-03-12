from sys import stdin
r = stdin.readline

v = int(r())
g = {}
for e in range(int(r())):
    v1, v2 = map(int, r().split())
    try:
        g[v1].append(v2)
    except:
        g[v1] = [v2]
    try:
        g[v2].append(v1)
    except:
        g[v2] = [v1]

cnt = 0
stack = [1]
visited = [0] * (v + 1)
while stack:
    curr = stack.pop()
    if not visited[curr]:
        cnt += 1
        visited[curr] = 1
        try:
            stack += g[curr]
        except:
            pass
print(cnt-1)