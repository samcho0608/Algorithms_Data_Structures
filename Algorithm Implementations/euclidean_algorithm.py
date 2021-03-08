def gcd(x, y):
    if y != 0:
        return gcd(y, x%y)
    else :
        return x
def lcm(x, y):
    return (x*y)//gcd(x,y)

# GCD
# def Euclidean(a, b):
#     while b != 0:
#         r = a % b
#         a = b
#         b = r
    
#     return a

# def Euclidean(a, b):

#   r = b % a

#   if r == 0:
#     return a

#   else:
#     return Euclidean(r, a)