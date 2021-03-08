from sys import stdin

coordinates = []
for i in range(int(stdin.readline().strip())):
    x,y = map(int, stdin.readline().split())
    coordinates.append((x,y))

for i in sorted(sorted(coordinates, key = lambda x : x[1]), key = lambda x: x[0]):
    print(' '.join(map(str, i)))