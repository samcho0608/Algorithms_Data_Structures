import sys
n = int(sys.stdin.readline())

queue = []
s = ''
for i in range(n):
    cmd = sys.stdin.readline().strip()
    if 'pop' == cmd:
        s += (queue[0] + '\n') if queue else '-1\n'
        if queue:
            del queue[0]
    elif 'size' == cmd:
        s += str(len(queue)) + '\n'
    elif 'empty' == cmd:
        s += '1\n' if not queue else '0\n'
    elif 'front' == cmd:
        s += (queue[0] + '\n') if queue else '-1\n'
    elif 'back' == cmd:
        s += (queue[-1] + '\n') if queue else '-1\n'
    else:
        queue.append(cmd.split()[1])

print(s)