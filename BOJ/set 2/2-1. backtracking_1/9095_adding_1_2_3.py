# how to show a certain number as sum of 1 2 3
from sys import stdin
r = stdin.readline

for i in range(int(r())):
    n = int(r())
    d = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1:
            d[1] = 1
        elif i == 2:
            d[2] = 2
        elif i == 3:
            d[3] = 4
        else:
            d[i] = d[i-1] + d[i-2] + d[i-3]

    print(d[n])