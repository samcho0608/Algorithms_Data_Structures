# in a set {1..49}
# set S of k elements from {1..49}
from itertools import combinations
from sys import stdin
r = stdin.readline

while True:
    l = r().strip()
    if l == '0':
        break

    s = list(l.split())[1:]

    for i in combinations(s,6):
        print(' '.join(i))
    
    print()