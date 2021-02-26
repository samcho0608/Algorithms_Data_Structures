# in a sorted array with length N
# find the occurrence of element X

from bisect import bisect_right, bisect_left

n, x = map(int, input().split())
numlist = list(map(int, input().split()))
count = bisect_right(numlist, x) - bisect_left(numlist, x)
print(count if count else -1)