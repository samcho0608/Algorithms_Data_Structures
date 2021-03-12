# 2n = a + b
# n > 1
# a,b prime numbers

# check for all even numbers < 1000000
# find the pair where b-a is the greatest

# input
# 8
# 20
# 42
# 0

# output
# 8 = 3 + 5
# 20 = 3 + 17
# 42 = 5 + 37
    
from sys import stdin
# specialized to exclude 2
def sieve(n):
    prime = [True for i in range(n + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p]:
            prime[p*2::p] = [False] * (n//p - 1)
        p += 1
    prime[2] = False
    return prime
primes = sieve(1000000)
indices = [i for i, j in enumerate(primes) if j]
ans = ''
while True:
    n = int(stdin.readline())
    if not n:
        break
    for i in indices:
        if primes[i] and primes[n-i]:
            ans += f'{n} = {i} + {n-i}' + '\n'
            break
print(ans)