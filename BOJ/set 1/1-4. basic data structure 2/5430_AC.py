# R is reversing the array
# D is poping the first number
# error raised when using D on an empty array

from sys import stdin
r = stdin.readline
res = []
# for _ in range(int(r())):
#     error = False
#     p = r().strip()
#     r()
#     l = r().strip()[1:-1]
#     if l:
#         l = list(map(int, l.split(',')))
#     else:
#         l = []
#     i = 0
#     while i < len(p):
#         if i != len(p) - 1 and p[i] == p[i + 1] == 'R':
#             i += 2
#             continue
#         if p[i] == 'R':
#             l.reverse()
#         else:
#             if l:
#                 l.pop(0)
#             else:
#                 error = True
#                 break
#         i += 1
    
#     res.append(l if not error else 'error')

# for r in res:
#     print(r)


for _ in range(int(r())):
    p = r().strip()
    r()
    l = r().strip()[1:-1]
    if l:
        l = list(map(int, l.split(',')))
    else:
        l = []
    f = 0
    b = len(l)
    reverse = False
    error = False
    for i in p:
        if i == 'R':
            reverse = not reverse
        else:
            if b > f:
                if reverse:
                    b -= 1
                else:
                    f += 1
            else:
                error = True
                break
    
    l = l[f:b]
    if reverse:
        l.reverse()
    print(f'[{",".join(map(str, l))}]' if not error else 'error')