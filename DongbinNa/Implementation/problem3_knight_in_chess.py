
y, x = map(int, input().split())

# my implementation
op = [-2,-1,1, 2]
count = 0
for dx in op:
    for dy in op:
        if abs(dx * dy) == 2:
            if y + dy in range(1,9) and x + dx in range(1,9):
                count += 1

print(count)

# solution
steps = [(i,j) for i in (-2,-1,1,2) for j in (-2,-1,1,2) if abs(i * j) == 2]
count = 0
for step in steps:
    ny += step[0]
    nx += step[1]

    if nx in range(1,9) and ny in range(1,9):
        count += 1

print(count)