# given computer connections, find the number of separate groups; not connected to each other

from collections import deque


def solution(n, computers):
    toVisit = [ 1 for i in range(n)]
    networkCount = 0

    for i in range(n) :
        if toVisit[i] == 0 :
            continue
        toVisit[i] = 0
        networkCount += 1

        inQ = deque([i])
        while inQ :
            curr = inQ.popleft()
            toVisit[curr] = 0

            for j in range(n) :
                if toVisit[j] != 0 and computers[curr][j] != 0:
                    inQ.append(j)

    return networkCount

assert solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])  == 1
assert solution(5, [[ 1 if j == i else 0 for j in range(5) ] for i in range(5)]) == 5
assert solution(5, [[ 1 for j in range(5) ] for i in range(5)]) == 1
assert solution(3, [[1,1,1],[1,1,1],[1,1,1]]) == 1