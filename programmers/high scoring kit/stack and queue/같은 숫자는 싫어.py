from collections import deque


def solution(arr):
    q = deque()
    for i in range(len(arr)) :
        if i == 0 :
            q.append(arr[i])
            continue

        lastVal = q.pop()
        
        q.append(lastVal)
        if arr[i] != lastVal :
            q.append(arr[i])

    answer = []
    while q :
        answer.append(q.popleft())
    return answer

assert solution([1,1,3,3,0,1,1]) == [1,3,0,1]
assert solution([4,4,4,3,3]) == [4,3]