# sieve of Eratosthenes
def sieve(n):
    prime = [True for i in range(n + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p]:
            prime[p*2::p] = [False] * (n//p - 1)
        p += 1
    return [i for i,j in enumerate(prime) if j]