# Different way of expressing year
# 1 <= E <= 15
# 1 <= S <= 28
# 1 <= M <= 19

e,s,m = map(int, input().split())
count = 1
while e != 1 or s != 1 or m != 1:
    e-=1
    s-=1
    m-=1
    count +=1

    if not e:
        e = 15
    if not s:
        s = 28
    if not m:
        m = 19
print(count)