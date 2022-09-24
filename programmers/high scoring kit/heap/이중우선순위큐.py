

from heapq import heapify, heappop, heappush


# 풀기는 풀었는데 마음에 안 듬
def solution(operations):
    maxHeap = []
    minHeap = []
    heapify(maxHeap)
    heapify(minHeap)
    
    for o in operations :
        opType, val = o.split()
        val = int(val)
        if opType == "I" :
            heappush(maxHeap, -val)
            heappush(minHeap, val)
        else :
            if not maxHeap or not minHeap :
                continue
            if val > 0 :
                heappop(maxHeap)
            else :
                heappop(minHeap)
            
            # 아래의 코드가 마음에 안 드는 부분
            #   O(5N) ~= O(N)이 뜨긴 하는데 반복이라 뭔가... 이거보다 더 좋은 방법이 있으면 좋을듯
            h = set([-s for s in maxHeap]).intersection(set(minHeap))
            maxHeap = list([-s for s in h])
            minHeap = list(h)
            heapify(maxHeap)
            heapify(minHeap)
    
    if not maxHeap :
        return [0,0]
        
    maxVal = -heappop(maxHeap)
    minVal = heappop(minHeap) if minHeap else maxVal
    return [maxVal, minVal]


assert solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]) == [0,0]
assert solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]) == [333, -45]