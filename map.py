from csv import *

def setupMap(map_file):
    map = []
    with open(map_file) as csvfile:
        r = reader(csvfile, delimiter=',')
        for row in r:
            map.append((row[0], row[1], int(row[2])))
    return map


# def setupPackages(pk_file):
#     packages = []
#     with open(pk_file) as csvfile:
#         r = reader(csvfile, delimiter=',')
#         for row in r:
#             pk = Package(row[0])
#             pk.office = row[1]
#             pk.address = row[2]
#             packages.append(pk)
#     return packages


def isEdge(map, u, v):
    for edge in map:
        if edge[0] == u and edge[1] == v:
            return True
        if edge[0] == v and edge[1] == u:
            return True
    return False


# *** ONLY ISSUE
# What's the order he wants to enqueue the adjacent edges?
# Is it based on the order he put it on the text file?
# Or does he want to order it alphabetically?

# Breadth-First Search
def bfs(G, office):
    path = {office:[office]}
    queue = [office]

    while len(queue) > 0:
        current = queue.pop(0)

        # all adjacent edges
        edges = [edge for edge in G if any(vertex == current for vertex in edge[:2])]

        for edge in edges:
            adj_vertex = edge[0] if edge[0] != current else edge[1]
            if adj_vertex not in path:
                queue.append(adj_vertex)
                path[adj_vertex] = path[current] + [adj_vertex]

    for key, value in sorted(path.items()):
        print('    {} : {}'.format(key, value))

# Depth-First Search
def dfs(G, office):
    path = dict()
    prev_path = []
    stack = [office]

    while len(stack) > 0:
        current = stack.pop()
        # skip the stacks added early that already found its path during previous dfs
        if current in path:
            continue

        path[current] = prev_path + [current]
        
        # all adjacent edges
        edges = [edge for edge in G if any(vertex == current for vertex in edge[:2])]

        for edge in edges:
            adj_vertex = edge[0] if edge[0] != current else edge[1]
            if adj_vertex not in path:
                stack.append(adj_vertex)
        
        prev_path = path[current]

    for key, value in sorted(path.items()):
        print('    {} : {}'.format(key, value))            

# Dijikstra
def dijkstra(G, office):
    weights = {}
    weights[office] = 0
    path = {office:[office]} # if in path, means checked
    queue = [office]

    while len(queue) > 0:
        current = queue.pop(0)

        # all adjacent edges
        edges = [edge for edge in G if any(vertex == current for vertex in edge[:2])]

        for edge in edges:
            adj_vertex = edge[0] if edge[0] != current else edge[1]
            new_weight = weights[current] + edge[2]

            if adj_vertex not in path:
                queue.append(adj_vertex)

            if adj_vertex not in path or new_weight < weights[adj_vertex]:
                path[adj_vertex] = path[current] + [adj_vertex]
                weights[adj_vertex] = new_weight

    for key, value in sorted(path.items()):
        print('    {} : {}'.format(key, value))
            

m = setupMap("map.txt")

print('BFS: ')
bfs(m, 'UPS')
print()
print('DFS: ')
dfs(m, 'UPS')
print()
print('Dijkstra: ')
dijkstra(m, 'UPS')