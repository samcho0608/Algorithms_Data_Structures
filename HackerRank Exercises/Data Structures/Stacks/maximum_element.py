num = int(input())

stack = [0]
for i in range(num):
    query = [int(q) for q in input().split(' ')]
    if query[0] == 1:
        stack.append(max(query[1],stack[-1]))
    elif query[0] == 2:
        stack.pop()
    else:
        print(stack[-1])
