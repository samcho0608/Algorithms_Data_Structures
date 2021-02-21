# sieve of Ertosthenes
def sieve(n):
    prime = [True for i in range(n + 1)]
    prime[0] = prime[1] = False
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    return [i for i,j in enumerate(prime) if j]