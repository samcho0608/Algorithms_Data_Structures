# rice cake cutter
# there is an array of rice cakes
# cutter cuts rice cakes at height H
# sum of the cut off cakes' length must be greater than equal to M

# find the max height to cut to get at least M number of rice cakes
from bisect import bisect_right

n, m = map(int, input().split())
rice = list(map(int,input().split()))

# rice.sort()
# mid = len(rice) // 2
# prev_mid = len(rice)
# greatest = 0
# while True:
#     total = 2 * len(rice) - bisect_right(rice, rice[mid])
#     if total >= m:
#         if total < greatest:
#             break
#         greatest = total
#         h = rice[mid]
#     elif not mid:
#         h = -1
#         break

#     if total >= m:
#         prev_mid = mid
#         mid = mid + (prev_mid - mid) // 2
#         if mid == prev_mid:
#             break
#     else:
#         prev_mid = mid
#         mid = prev_mid // 2

# if h < 0:
#     h = min(rice) - 1
# print(h)

start = 0
end = max(rice)
greatest = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in rice:
        if i > mid:
            total += i - mid
    if total >= m:
        greatest = mid
        start = mid + 1
    else:
        end = mid - 1
print(greatest)