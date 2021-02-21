# from math import sqrt
# def findPrimes(n):
#     if n == 2 or n == 3:
#         return list(range(2, n + 1))
        
#     primes = findPrimes(int(sqrt(n)))
#     primes.extend(i for i in range(primes[0] + 1, n) if all(i % j != 0 for j in primes))
#     return primes

# n = int(input())
# rt = 0
# while 1:
#     if int(sqrt(n)) > rt:
#         rt = int(sqrt(n))
#         primes = findPrimes(rt + 1)
#     if all(n % p != 0 for p in primes):
#         a = str(n)
#         if a == a[::-1]:
#             break
#     n += 1

# print(n)

def isPrime(n:int) -> bool:
    if n < 4:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input())
while 1:
    if isPrime(n) and str(n) == str(n)[::-1]:
        break
    n += 1
print(n)
        