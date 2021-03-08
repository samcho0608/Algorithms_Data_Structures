from sys import stdin
r = stdin.readline
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

count = 0
r()
for i in map(int, r().strip().split()):
    if isPrime(i):
        count += 1
print(count)