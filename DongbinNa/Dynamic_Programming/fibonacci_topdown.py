d = [0] * 100
def fibonacci(n):
    if n in (1,2):
        return 1
    if d[n]:
        return d[n]
    d[n] = fibonacci(n-1) + fibonacci(n-2)
    return d[n]

print(fibonacci(99))
print(d)