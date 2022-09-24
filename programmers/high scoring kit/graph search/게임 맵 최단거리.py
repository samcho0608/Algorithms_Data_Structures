# recursion

# def solution(maps) :
#     val = travel(maps, (0,0), 0)
#     return val

# def travel(maps, currLoc, stepSoFar) -> int:
#     x,y = currLoc
    
#     if x >= len(maps) or y >= len(maps[0]) or x < 0 or y < 0 or maps[x][y] == 0:
#         return -1

#     if x == len(maps) - 1 and y == len(maps[0]) - 1:
#         return stepSoFar + 1


#     maps[x][y] = 0

#     travels = [
#         travel(maps, (x,y + 1), stepSoFar + 1), 
#         travel(maps, (x,y - 1), stepSoFar + 1), 
#         travel(maps, (x + 1,y), stepSoFar + 1), 
#         travel(maps, (x - 1,y), stepSoFar + 1)
#     ]

#     retVal = min(
#         [t for t in travels if t >= 0]
#     ) if any([ t >= 0 for t in travels]) else -1
    
#     maps[x][y] = 1
#     return retVal

from collections import deque

def solution(maps):
    travelLocs = deque()
    travelLocs.append(((0,0)))
    visited = set()

    while travelLocs :
        x,y = travelLocs.popleft()
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return maps[x][y]



        for dx, dy in [(1,0),(-1,0), (0,1), (0,-1)] :
            nx, ny = x + dx, y + dy

            if nx >= 0 and \
                ny >= 0 and \
                nx < len(maps) and \
                ny < len(maps[0]) and \
                maps[nx][ny] > 0 and \
                    (nx, ny) not in visited:
                
                travelLocs.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
        visited.add((x,y))
        
    return -1



assert solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) == 11
assert solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]) == -1
assert solution([[1],[0]]) == -1