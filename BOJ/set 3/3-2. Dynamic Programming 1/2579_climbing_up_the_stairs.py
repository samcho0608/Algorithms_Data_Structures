from sys import stdin
r = stdin.readline

n = int(r())
steps = [0] + [int(r()) for _ in range(n)]
d = [0] * (301)
d[1] = steps[1]
if n > 1:
    d[2] = steps[1] + steps[2]
if n > 2:
    for n in range(3, n + 1):
        d[n] = steps[n] + max(d[n-3] + steps[n-1], d[n-2])

print(d[n])