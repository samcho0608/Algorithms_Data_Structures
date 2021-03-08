import sys
n = int(sys.stdin.readline())

stack = []
s = ''
for i in range(n):
    cmd = sys.stdin.readline().strip()
    if 'pop' == cmd:
        s += (stack.pop() + '\n') if stack else '-1\n'
    elif 'top' == cmd:
        s += (stack[-1] + '\n') if stack else '-1\n'
    elif 'size' == cmd:
        s += str(len(stack)) + '\n'
    elif 'empty' == cmd:
        s += '1\n' if len(stack) == 0 else '0\n'
    else:
        stack.append(cmd.split()[1])

print(s)