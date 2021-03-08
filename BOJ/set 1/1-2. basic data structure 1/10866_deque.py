import sys
n = int(sys.stdin.readline())

queue = []
s = ''
for i in range(n):
    cmd = sys.stdin.readline().strip()
    if 'pop_front' == cmd or 'pop_back' == cmd:
        s += ((queue[0] if cmd == 'pop_front' else queue[-1]) + '\n') if queue else '-1\n'
        if queue:
            if cmd == 'pop_front':
                del queue[0]
            else:
                del queue[-1]
    elif 'size' == cmd:
        s += str(len(queue)) + '\n'
    elif 'empty' == cmd:
        s += '1\n' if not queue else '0\n'
    elif 'front' == cmd:
        s += (queue[0] + '\n') if queue else '-1\n'
    elif 'back' == cmd:
        s += (queue[-1] + '\n') if queue else '-1\n'
    else:
        push = cmd.split()
        if push[0] == 'push_front':
            queue.insert(0, push[1])       
        else:
            queue.append(push[1])

print(s)