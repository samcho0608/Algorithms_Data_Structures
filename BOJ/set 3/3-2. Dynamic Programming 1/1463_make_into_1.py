n = int(input())
d = [0] * (n + 1)
for i in range(2,n+1):
    d[i] = 1 + min(d[i//3] + i % 3, d[i//2] + i % 2) 
print(d[n])
