# Only the patterns below allowed
# ()
# (())
# ()()

from sys import stdin

n = int(stdin.readline().strip())
res = []
for i in range(n):
    line = list(stdin.readline().strip())
    rights = []
    while True:
        end = line.pop()
        if end == ')':
            rights.append(end)
        else:
            if rights:
                rights.pop()
            else:
                res.append('NO')
                break
        if not line:
            res.append('YES' if not rights else 'NO')
            break

for r in res:
    print(r)

# from sys import stdin

# n = int(input())
# for _ in range(n):
#     str_ = stdin.readline().strip()
#     stack = 0
#     for chr_ in str_:
#         if chr_ == '(':
#             stack += 1
#         else:
#             stack -= 1
#             if stack < 0:
#                 break
#     if stack == 0:
#         print('YES')
#     else:
#         print('NO')