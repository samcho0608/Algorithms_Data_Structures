# if divisible by 3, divide by 3
# if divisible by 2, divide by 2
# subtract 1

n = int(input())
d = [10 ** 6] * (n + 1)
d[0] = d[1] = 0
for i in range(1, n + 1):
    d[i] = min(d[i], d[i-1] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])