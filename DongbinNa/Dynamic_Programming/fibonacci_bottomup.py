d = [0,1,1, *(0 for i in range(97))]

for i in range(3,100):
    d[i] = d[i-1] + d[i-2]

print(d[99])