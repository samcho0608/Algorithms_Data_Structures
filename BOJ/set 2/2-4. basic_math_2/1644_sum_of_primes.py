# Sieve of Eratosthenes
# Two pointer

def sieve(n):
    prime = [True for i in range(n + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p]:
            prime[p*2::p] = [False] * (n//p - 1)
        p += 1
    return [i for i,j in enumerate(prime) if j]

n = int(input())
primes = sieve(n + 1)
l = len(primes)
res = 0
low = up = p_sum = 0
while True:
    if p_sum >= n:
        p_sum -= primes[low]
        low += 1
    else:
        if up == l:
            break
        p_sum += primes[up]
        up += 1
    if p_sum == n:
        res += 1

print(res)