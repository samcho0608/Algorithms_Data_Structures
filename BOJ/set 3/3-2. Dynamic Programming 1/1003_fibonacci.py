from sys import stdin
r = stdin.readline

n = int(r())
nums = []
greatest = 0
for _ in range(n):
    i = int(r())
    if i > greatest:
        greatest = i
    nums.append(i)
d = [(1,0),(0,1)] + [False] * (greatest - 1)
if greatest > 1:
    for i in range(2, greatest + 1):
        d[i] = (d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1])
for n in nums:
    print(*d[n])