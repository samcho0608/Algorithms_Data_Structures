# Given ranges l,u
# Find all prime numbers with in the range

# for i in range(*(int(i) for i in input().split())):
#     isPrime = True
#     for j in range(2, i):
#         if i % j == 0:
#             isPrime = False
#             break

#     if isPrime:
#         print(i)

# l,u = (int(i) for i in input().split())
# primes = [i for i in range(2,l) if all(i % j != 0 for j in range(2,i))]
# exclude = len(primes)
# for i in range(l, u):
#     if all(i % p != 0 for p in primes):
#         primes.append(i)

# for i in primes[exclude:]:
#     print(i)



# Sieve of Eratosthenes
from math import sqrt
def findPrimes(n):
    if n == 2 or n == 3:
        return list(range(2, n + 1))
        
    primes = findPrimes(int(sqrt(n)))
    primes.extend(i for i in range(primes[0] + 1, n) if all(i % j != 0 for j in primes))
    return primes

l,u = (int(i) for i in input().split())
primes = findPrimes(int(sqrt(u)) + 1) 
for i in range(l,u + 1):
    if i != 1 and (i in primes or all(i % j != 0 for j in primes)):
        print(i)
