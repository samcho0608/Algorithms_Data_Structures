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
r = stdin.readline

M = 2*10**6
primes = [True for i in range(M + 1)]
primes[0] = primes[1] = False
p = 2
while p*p <= M:
    if primes[p]:
        primes[p*2::p] = [False] * (M//p - 1)
    p += 1
primes = [i for i,j in enumerate(primes) if j]

def isPrime(x):
    for p in primes:
        if p**2 > x :
            break
        if x % p == 0:
            return False
    return True

ans = ''
for i in range(int(r())):
    n = sum(map(int, r().split()))
    works = True
    if n < 4:
        works = False
    elif n % 2 == 0:
        works = True
    else:
        works = isPrime(n-2)
    ans += ('YES' if works else 'NO') + '\n'
print(ans)