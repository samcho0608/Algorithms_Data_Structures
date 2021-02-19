def decimal_to_floating_point(x, n, p):
    """
    x: input decimal number
    n: number binary bits in the fraction part
    p: exponent range m ∈ [-p, p]
    
    returns
    f: fraction part binary bits

    m: exponent of 2 for this description
    """
    m = 0

    for i in range(-p, p+1):
        if 2 ** i > x:
            m = i - 1
            break

    binary = x * 2 ** (n - m)

    f = "0" * (n + 1)
    for i in reversed(range(n + 1)):
        multiple = 2 ** i
        if multiple <= binary:
            binary -= multiple
            f = f[:n - i] + '1' + f[n - i + 1 :]
    return f[1:], m

# print(decimal_to_floating_point(19.25,8,8))
print(decimal_to_floating_point(0.236,5,8))