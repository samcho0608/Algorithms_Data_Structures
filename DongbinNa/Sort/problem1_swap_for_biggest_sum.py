# sam has two arrays A and B each of length N
# all elements are natural numbers
# Sam can make max K number of swaps between A and B
# Objective is to make the sum of A elements to be the
# greatest after swapping max K number of times

# Design
# 1. sort the A in ascending and B in descending
# 2. swap until element in a is greater

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
for i in range(n):
    if a[i] > b[i] or not k:
        break
    a[i], b[i] = b[i], a[i]
    k -= 1

print(sum(a))