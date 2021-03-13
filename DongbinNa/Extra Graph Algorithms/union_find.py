# def find_parent(parent,x):
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# path comparession method
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v,e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

cycle = False
for i in range(e):
    a,b = map(int, input().split())
    # you can check if there is a cycle using this
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    union_parent(parent, a, b)