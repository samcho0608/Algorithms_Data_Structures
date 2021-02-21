





# def isPrime(n:int) -> bool:
#     if n < 4:
#         return n > 1
#     if n % 2 == 0 or n % 3 == 0:
#         return False

#     i = 5
#     while i ** 2 <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# from math import sqrt
# def sieve(n):
#     prime = [True for i in range(n + 1)]
#     prime[0] = prime[1] = False
#     p = 2
#     while p*p <= n:
#         if prime[p]:
#             for i in range(p * 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#     return [i for i,j in enumerate(prime) if j]

# import time
# start_time = time.time()

# This is erroneous bc 
# all primes are of form 6k +- 1
# but not all 6k+- 1 are primes
# def enough_primes(n):
#     plist = [2,3]
#     if n < 4:
#         return plist
#     i = 5
#     while i ** 2 <= n:
#         plist.extend([i, i + 2])
#         i += 6
#     return plist
# # print(enough_primes(int(input())))

# low, up = (map(int,input().split()))
# # print(len(squares & {i for i in range(low, up + 1)}))
# # squares = {i * j for i in {i ** 2 for i in enough_primes(up)} for j in range(1, up//i + 1)}
# # print(len({i for i in range(low, up + 1) if i not in squares}))

# squares = {i ** 2 for i in enough_primes(up)}
# count = 0
# while up >= low:
#     # if low not in squares:
#     if all(low % i != 0 for i in squares):
#         count += 1
#     low += 1
# print(count)

# print(f'{time.time() - start_time}s')


low, up = (map(int,input().split()))

# we assume all are not divisble
total = up - low + 1
nums = [False for i in range(total)]
p = 2
while p * p <= up:
    sq = p*p
    for i in range(low // sq + int(low % sq != 0), (up // sq) + 1):
        if not nums[sq *  i - low]:
            nums[sq *  i - low] = True
            total-=1

    p += 1
print(total)