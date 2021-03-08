from sys import stdin
r = stdin.readline

board = [list(map(int, r().strip().split())) for i in range(9)]
rows = [set(range(1, 10)) - set(b) for b in board]
cols = [set(range(1, 10)) - {b[i] for b in board} for i in range(9)]
boxes = [[set(range(1,10)) - {board[i+y][j+x] for y in range(3) for x in range(3)} for j in range(0,9,3)] for i in range(0,9,3)]
zeroes = [(i,j) for i, b in enumerate(board) for j,x in enumerate(b) if x == 0]



def dfs(i):
    if i == len(zeroes):
        return True
    y,x = zeroes[i]

    options = rows[y] & cols[x] & boxes[y//3][x//3]
    if not options:
        return False
    ans = False
    for o in options:
        board[y][x] = o
        rows[y].remove(o)
        cols[x].remove(o)
        boxes[y//3][x//3].remove(o)
        if dfs(i+1):
            ans = True
            break
        rows[y].add(o)
        cols[x].add(o)
        boxes[y//3][x//3].add(o)
    return ans

dfs(0)
for b in board:
    print(' '.join(map(str, b)))

# Think about a way to do a bitwise method
