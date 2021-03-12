from sys import stdin
r = stdin.readline

n = int(r())
apt = []
for __ in range(n):
    apt.append(list(map(int, list(r().strip()))))

cnt = 0
bldgs = []

for i in range(n):
    for j in range(n):
        if apt[i][j]:
            cnt += 1
            stack = [(i,j)]
            bldg_cnt = 0
            while stack:
                y,x = stack.pop()
                if apt[y][x]:
                    bldg_cnt += 1
                    apt[y][x] = 0
                    if y + 1 in range(n): stack.append((y+1,x))
                    if y - 1 in range(n): stack.append((y-1,x))
                    if x + 1 in range(n): stack.append((y,x+1))
                    if x - 1 in range(n): stack.append((y,x-1))
            bldgs.append(bldg_cnt)

print(cnt)
for b in sorted(bldgs):
    print(b)