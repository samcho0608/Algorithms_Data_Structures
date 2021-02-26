# ant warrior
# can't visit directly adjacent warehouses
# Given N warehouses
# find the biggest amount of food

# # Top Down
# n = int(input())
# warehouses = list(map(int, input().split()))
# d = [0] * n
# d[0] = warehouses[0]
# d[1] = max(d[0], warehouses[1])

# def bestFood(i):
#     if i == 0:
#         return warehouses[0]
#     if i == 1:
#         return warehouses[1]
#     if d[i]:
#         return d[i]

#     cannot = bestFood(i-1)
#     can = bestFood(i-2)
#     d[i] = max(can + warehouses[i], cannot)
#     return d[i]
    
# print(bestFood(n - 1))

# Bottom Up
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(d[0], array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])