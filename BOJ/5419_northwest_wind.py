# NOT FINISHED

# y has to decrease
# x has to increase

# how many possible pairs?

from sys import stdin
r = stdin.readline
res = ''

for _ in range(int(r())):
    crds = []
    num = 0
    for c in range(int(r())):
        crds.append(tuple(map(int, r().strip().split())))
        num += 1

    crds.sort(key = lambda x: (x[0],-x[1]))
    
    cnt = 0
    for i, j in enumerate(crds):
        for k in range(i+1, num):
                if crds[k][1] <= j[1]:
                    cnt += 1
    res += str(cnt) + '\n'

print(res, end='')