from bisect import bisect_left
n = int(input())

stack = []

for i in range(n):
    num = int(input())
    if num not in stack:
        stack.append(num)
        # stack.insert(bisect_left(stack,num),num)

stack.sort()

for i in stack:
    print(i)