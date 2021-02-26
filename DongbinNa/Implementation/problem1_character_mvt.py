# N x N square
# (1,1) top left
# (N,N) bottom right
# start at (1,1) and return the final position
# after the line of input
# LRUD

n = int(input())

mvt = input().split()

h = v = 1

dv = [0,0,-1,1]
dh = [-1, 1, 0,0]
d = ['L', 'R', 'U', 'D']

for m in mvt:
    i = d.index(m)
    nv = v + dv[i]
    nh = h + dh[i]

    if nh < 1 or nv < 1 or nh > n or nv > n:
        continue
    
    v, h = nv, nh

print((v, h))

# # my solution
# for i in mvt:
#     if i == 'R':
#         if x == n:
#             continue
#         x += 1
#     elif i == 'L':
#         if x == 1:
#             continue
#         x -= 1
#     elif i == 'U':
#         if y == 1:
#             continue
#         y -= 1
#     else:
#         if y == n:
#             continue
#         y += 1
# 
# print(x,y)