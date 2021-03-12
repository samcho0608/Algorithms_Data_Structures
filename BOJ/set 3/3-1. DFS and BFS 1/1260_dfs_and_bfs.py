from sys import stdin
r = stdin.readline
graph = dict()

v,e,s = map(int, r().strip().split())
for _ in range(e):
    v1,v2 = map(int, r().strip().split())
    try:
        graph[v1].append(v2)
    except:
        graph[v1] = [v2]
    try:
        graph[v2].append(v1)
    except:
        graph[v2] = [v1]
for i in graph.values():
    i.sort(reverse = True)

def dfs(s):
    stack = [s]
    visited = {}
    res = ''
    while stack:
        a = stack.pop()
        try:
            if visited[a]:
                continue
        except:
            visited[a] = True
            res += str(a) + ' '
            try:
                stack += [i for i in graph[a]]
            except:
                pass
    print(res)
        


def bfs(s):
    queue = [s]
    visited = {}
    res = ''
    while queue:
        a = queue.pop()
        try:
            if visited[a]:
                continue
        except:
            visited[a]= True
            res += str(a) + ' '
            try:
                queue = graph[a] + queue
            except:
                pass
    print(res)

dfs(s)
bfs(s)