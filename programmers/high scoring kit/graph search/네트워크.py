# given computer connections, find the number of separate groups; not connected to each other

from collections import deque


def solution(n, computers):
    toVisit = [ 1 for i in range(n)] # toVisit[0] means visited, 1 otherwise
    networkCount = 0 # count of separate networks formed

    for i in range(n) :     # for each computer identified by index
        if toVisit[i] == 0 :    # skip if already visited
            continue
        toVisit[i] = 0      # mark it visited
        networkCount += 1   # count it as a new group since it wouldn't have come to this point if it's not a new group

        inQ = deque([i])            # perform bfs through the connection from this computer and mark each visited computer visited
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