# with scare level k, an explorer must join a group of x or more people to go on a journey
# biggest number of possible groups 

scareLevel = list(map(int, input().split()))

scareLevel.sort()
count = 0
member = 0
for i in scareLevel:
    member += 1
    if member >= i:
        count += 1
        member = 0

print(count)