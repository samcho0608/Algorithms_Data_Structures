from sys import stdin
r = stdin.readline

res = []
for _ in range(int(r())):
    n, m = map(int, r().split())

    q = list(map(int, r().split()))
    if q.count(q[m]) == 1:
        res.append(len([i for i in q if i >= q[m]]))
    else:
        c = 0
        while q:
            if q[0] == max(q):
                del q[0]
                c += 1
                if not m:
                    break
                m -= 1
            else:
                q.append(q.pop(0))
                if not m:
                    m = len(q) - 1
                else:
                    m -= 1

        res.append(c)

for r in res:
    print(r)