import sys

n = int(sys.stdin.readline())

table = [0] * 10001

for i in range(n):
    table[int(sys.stdin.readline())] += 1

for i, val in enumerate(table):
    if val:
        print((str(i)+'\n') * val, end='')