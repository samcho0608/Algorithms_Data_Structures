# Efficient currency unit composition
# Given N types of currencies
# Find the min number of currency required to form M won

# # Solution
n, m= list(map(int, input().split()))
currency = set()
for i in range(n):
    currency.add(int(input()))

d = [10001] * (m + 1)
d[0] = 0

# for c in currency:
#     for j in range(c, m + 1):
#         if d[j - c] != 10001:
#             d[j] = min(d[j], d[j-c] + 1)

# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])





# My implementation
# n is number of currency
# currency set of currencies
# m is target number

for c in currency:
    for i in range(c, m + 1):
        if i % c == 0:
            d[i] = min(d[i] , i // c)
        elif d[i % c] != 10001:
            d[i] = min(d[i], i // c + d[i % c])

print(d[m] if d[m] != 10001 else -1)