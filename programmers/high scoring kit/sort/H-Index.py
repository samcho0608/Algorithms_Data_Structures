def solution(citations):
    maxH = 0

    for i in range(1, len(citations) + 1) :
        if sum([c >= i for c in citations]) >= i :
            maxH = max(maxH, i)

    return maxH

assert solution([3, 0, 6, 1, 5]) == 3
assert solution([4,4,4]) == 3