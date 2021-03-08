# L : move the cursor to the left once(if at the very front, ignore)
# D : move the cursor to the right once(if at the very end, ignore)
# B : backspace a character
# P $ : add the character '$' to the left of the cursor

# cursor starts at the very end of the string

# _a_p_p_l_e_

# https://wayhome25.github.io/python/2017/06/14/time-complexity/
# The issue was with the Big-O of the list, string manipulation

import sys

left = list(sys.stdin.readline().strip())
right = []

for i in range(int(sys.stdin.readline().strip())):
    cmd = sys.stdin.readline().strip()
    if cmd == 'L':
        if left:
            right.append(left.pop())
    elif cmd == 'D':
        if right:
            left.append(right.pop())
    elif cmd == 'B':
        if left:
            left.pop()
    else:
        left.append(cmd.split()[1])

print(''.join(left + list(reversed(right))))