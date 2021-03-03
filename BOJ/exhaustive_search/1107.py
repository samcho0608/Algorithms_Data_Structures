# remove has 0-9 and + -
# infinitely many channels
# - at 0 just stays in 0

# some number buttons broken
# currently at 100

# minimum number to get to channel N

# nums = set(range(10))
# n = input() # target number
# m = int(input())

# nums -= set(map(int, input().split()))
# start = 100

# int_n = int(n)
# s = ''
# count = 0
# for i,j in enumerate(n):
#     digit = int(j)

    
#     options = [str(start)]
#     res = [abs(int_n - start)]
#     if not nums:
#         break

#     if digit >= min(nums):
#         low = max([num for num in nums if num <= digit])
#         options.append(low)
#         res.append(abs(int_n - int(s + str(low) + n[i+1:])))
#     if digit <= max(nums):
#         high = min([num for num in nums if num >= digit])
#         options.append(high)
#         res.append(abs(int_n - int(s + str(high) + n[i+1:])))

#     index = res.index(min(res))
#     if index == 0:
#         s = options[0]
#         break
#     s += str(options[index])
#     count += 1


# results = [abs(int_n - start)]
# if s:
#     results.append(abs(int_n - int(s)) + count)

# print(min(results))












nums = set(range(10))
n = input() # target number
m = int(input())

nums -= set(map(int, input().split()))
start = 100

int_n = int(n)
s = ''
count = 0
for i,j in enumerate(n):
    digit = int(j)

    
    options = [str(start)]
    res = [abs(int_n - start)]
    if not nums:
        break

    if digit >= min(nums):
        low = max([num for num in nums if num <= digit])
        options.append(low)
        res.append(abs(int_n - int(s + str(low) * (len(n) - i))))
    if digit <= max(nums):
        high = min([num for num in nums if num >= digit])
        options.append(high)
        res.append(abs(int_n - int(s + str(high) * (len(n) - i))))

    index = res.index(min(res))
    if index == 0:
        s = options[0]
        break
    s += str(options[index])
    count += 1


results = [abs(int_n - start)]
if s:
    results.append(abs(int_n - int(s)) + count)

print(min(results))