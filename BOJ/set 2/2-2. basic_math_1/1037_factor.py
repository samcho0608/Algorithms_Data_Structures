from sys import stdin
n = int(stdin.readline())
factors = list(map(int, stdin.readline().strip().split()))
factors.sort()
print(factors[0] * factors[-1])