from sys import stdin

n1, n2 = map(int, stdin.readline().strip().split())
gcf = 1
i = 2
while i <= n1 and i <= n2:
    if n1 % i != 0 or n2 % i != 0:
        i += 1
    else:
        gcf *= i
        n1 //= i
        n2 //= i

print(gcf)
print(gcf * n1 * n2)

# Solution
def gcd(x, y):
    if y != 0:
        return gcd(y, x%y)
    else :
        return x
def lcm(x, y):
    return (x*y)//gcd(x,y)
N, M = map(int, input().split())

print(gcd(N, M))
print(lcm(N, M))