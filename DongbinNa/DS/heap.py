import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable, reverse=False):
    h = []
    result = []
    r = -1 if reverse else 1
    for value in iterable:
        heapq.heappush(h,value*r)
    for i in range(len(h)):
        result.append(r*heapq.heappop(h))
    return result

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)
for i in range(n):
    print(res[i])
res = heapsort(arr,reverse=True)
for i in range(n):
    print(res[i])