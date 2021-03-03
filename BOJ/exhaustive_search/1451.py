# TODO
# Think about 6 possible cases you can divide rect into

n,m =map(int,input().split())

rect = [list(map(int,list(input()))) for i in range(n)]
nums = []
for i in rect:
    nums.extend(i)
nums.sort(reverse=True)

# 0 1 2 are max indices
maxes = nums[:3]
coord = []
for i in range(n):
    for j in range(m):
        if rect[i][j] in maxes:
            coord.append((i,j))

sums = []
for c in coord:
    greatest = 0
    i,j = c
    p_sum = rect[i][j]
    while True:
        i -= 1
        if i not in range(n) or (i,j) in coord:
            break
        p_sum += rect[i][j]
    i,j = c
    while i in range(n):
        i += 1
        if i not in range(n) or (i,j) in coord:
            break
        p_sum += rect[i][j]
    i,j = c
    greatest = max(greatest, p_sum)
    p_sum = rect[i][j]
    while True:
        j -= 1
        if j not in range(m) or (i,j) in coord:
            break
        p_sum += rect[i][j]
    i,j = c
    while i in range(n):
        j += 1
        if j not in range(m) or (i,j) in coord:
            break
        p_sum += rect[i][j]
    i,j = c
    greatest = max(greatest, p_sum)
    sums.append(greatest)

mult = 1
for i in sums:
    mult *= i
print(mult)

