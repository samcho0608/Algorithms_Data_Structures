# Repeat below till N == 1:
    # 1. N -= 1
    # 2. N //= K if N % K == 0
# least number of operations

n, k = map(int, input().split())

count = 0

while True:
    remainder = n % k
    n -= remainder
    count += remainder
    if n < k:
        break
    n //= k
    count += 1

count += n - 1
print(count)