# given an integer X, one can choose one of the four following operations:
# 1. if divisible by 5, divide by 5
# 2. if divisible by 3, divide by 3
# 3. if divisible by 2, divide by 2
# 4. subtract 1

# find the smallest number of operations to get 1

# My Top Down method
# n = int(input())
# d = [0] * (n + 1)
# d[2] = 1
# d[3] = 1
# d[4] = 2
# d[5] = 1
# d[6] = 2
# d[7] = 3
# d[8] = 3
# d[9] = 2

# def findSol(i):
#     if i in (2,3,5):
#         return d[i]
#     options = []
#     options.append(d[i // 2] + i % 2 if d[i // 2] else findSol(i // 2) + i % 2)
#     options.append(d[i // 3] + i % 3 if d[i // 3] else findSol(i // 3) + i % 3)
#     options.append(d[i // 5] + i % 5 if d[i // 5] else findSol(i // 5) + i % 5)
#     d[i] = min(options) + 1
#     return d[i]

# print(findSol(n))

n = int(input())
d = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[n])