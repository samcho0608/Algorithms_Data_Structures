# len(priorities) in range(101)
# p in priorities in range(1,10)
# location in range(0, len(priorities))

from collections import deque

def solution(priorities : list[int], location : int):
    remainingPriorities = [0] * 10
    queue = deque()
    for i, p in enumerate(priorities) :
        remainingPriorities[p] += 1           # 우선 순위 개수 세기
        queue.append((i,p)) # deque에 우선수위랑 index 추가함
    
    index = 0
    while True :
        i,p = queue.popleft()
        if sum(remainingPriorities[p+1:]) > 0 : # p 이상의 우선 순위가 남아있을때
            queue.append((i,p))
        elif i == location :    # p가 현재 최대의 우선 순위이고, location의 위치일때
            return index + 1
        else :                  # location에 있지 않은데, 제일 높은 우선순위인 경우
            index += 1
            remainingPriorities[p] -= 1



assert solution([2, 1, 3, 2], 2) == 1
assert solution([1, 1, 9, 1, 1, 1], 0) == 5
assert solution([4,1,3,2], 2) == 2