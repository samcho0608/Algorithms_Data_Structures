from sys import stdin
r = stdin.readline

h = int(r())
prev_lev = list(map(int, r().split()))
for i in range(h-1):
    curr_lev = list(map(int, r().split()))
    for i in range(len(prev_lev)):
        if i == 0:
            curr_lev[i] += prev_lev[i]
        curr_lev[i + 1] += max(prev_lev[i], prev_lev[i + 1]) \
            if i != len(prev_lev) - 1 else prev_lev[i]

    prev_lev = curr_lev


print(max(prev_lev))