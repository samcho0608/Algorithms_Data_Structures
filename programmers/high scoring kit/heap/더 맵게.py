#  PriorityQueue 쓰니까 효율성에서 안 좋음. 걍 heapq 쓰는게 나을듯

import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while True:
        minVal = heapq.heappop(scoville)
        if minVal >= K :
            return count
        
        if len(scoville) == 0 :
            return -1

        newVal = calculateMixedScoville(minVal, heapq.heappop(scoville))
        heapq.heappush(scoville, newVal)
        count += 1


def calculateMixedScoville(leastSpicy, secondLeastSpicy) :
    return 2 * secondLeastSpicy + leastSpicy

assert solution([1, 2, 3, 9, 10, 12], 7) == 2
assert solution([1,2],100) == -1