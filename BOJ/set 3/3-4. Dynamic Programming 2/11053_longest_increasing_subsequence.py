n = int(input())
soldiers = list(map(int, input().split()))

# # Solution
# soldiers.reverse()
# dp = [1] * n

# for i in range(1,n):
#     for j in range(0,i):
#         if soldiers[j] < soldiers[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(n-max(dp))


# save max number of soldiers till that index
d = [0] * n
d[0] = 1
d[1] = 1 if soldiers[1] > soldiers[0] else 2
for i in range(2, n):
    if soldiers[i] > soldiers[i - 1]:
        d[i] = max(d[i-1], d[i-2] + 1)
    else:
        d[i] = d[i - 1] + 1

print(n - d[n-1])