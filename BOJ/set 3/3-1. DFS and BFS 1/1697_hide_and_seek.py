from collections import deque
n,k = map(int, input().split())

q = deque()
d = [0] * 100001
q.append(n)
while q:
    curr = q.popleft()
    if curr == k:
        break
    for np in (curr-1, curr+1, 2*curr):
        if 0 <= np <= 100000 and not d[np]:
            q.append(np)
            d[np] = d[curr] + 1

print(d[k])

# solution
# def c(n,k):
#     if n>=k:
#         return n-k
#     elif k == 1:
#         return 1
#     elif k%2:
#         return 1+min(c(n,k-1),c(n,k+1))
#     else:
#         return min(k-n, 1+c(n,k//2))
    
# n, k = map(int,input().split())
# print(c(n,k))