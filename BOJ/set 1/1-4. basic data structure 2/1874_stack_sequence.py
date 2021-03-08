from sys import stdin
n = int(stdin.readline())
sequence = [int(stdin.readline()) for i in range(n)]
sequence.reverse()
stack = []
res = []
for i in range(1, n + 1):
    stack.append(i)
    res.append('+')
    while stack and stack[-1] == sequence[-1]:
        stack.pop()
        res.append('-')
        sequence.pop()

if stack:
    print('NO')
else:
    for r in res:
        print(r)