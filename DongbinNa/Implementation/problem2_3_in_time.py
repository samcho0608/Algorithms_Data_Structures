# given n
# find all times btwn 0h 0m 0s to nh 59min 59s
# that has 3 in it

n = int(input())

# my implementation
count = 0
nonh = len([i for i in range(60) if '3' in str(i)])
for i in range(n + 1):
    if '3' in str(i):
        count += 60 ** 2
        continue
    count += nonh * 60 * 2

count -= nonh ** 2

print(count)

# Solution
count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)