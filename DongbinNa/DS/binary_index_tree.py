# also called Fenwick Tree
import sys
input = sys.stdin.readline

# n : number of data
# m : number of change
# k : number of partial sum calculations
n,m,k = map(int, input().split())

arr = [0] * (n+1)
tree = [0] * (n+1)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result

def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1,n + 1):
    x = int(input())
    arr[i] = x
    update(i, x) 

for i in range(m + k):
    a,b,c = map(int, input().split())
    # if it's update operation
    if a== 1:
        update(b,c - arr[b])
        arr[b] = c
    # if it's interval sum operation
    else:
        print(interval_sum(b,c))