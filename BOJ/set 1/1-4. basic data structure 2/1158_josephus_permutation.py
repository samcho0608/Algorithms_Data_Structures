from sys import stdin

n,k = map(int, stdin.readline().split())

ppl = list(range(1, n + 1))
stack = []
count = 1
i = 0
while ppl:
    if count == k:
        stack.append(ppl.pop(i))
        count = 1
    else:
        i += 1
        count += 1
    if i >= len(ppl):
        i = 0

print(f'<{", ".join(map(str, stack))}>')

# More mathematical way
# n, m = map(int, input().split())
# l = list(range(1, n + 1))
# r = []
# index = 0

# while l:
#     index = (index + m - 1) % len(l)
#     r.append(str(l.pop(index)))

# print('<', ', '.join(r), '>', sep='')