dimension = int(input('Dimension Please: '))

snail = [0 for i in range(dimension)]
snail = [snail.copy() for i in range(dimension)]

#  1  2  3  4  5
# 16 17 18 19  6
# 15 24 25 20  7
# 14 23 22 21  8
# 13 12 11 10  9

i = j = 0
num = 1
hor = ltr = True
max_val = len(snail) * len(snail[0])
while num <= max_val:

    while True:
        snail[i][j] = num
        num += 1

        # if not turn for horizontal slide
        if not hor or num > max_val:
            break

        prev = j
        # if left to right add 1 else subtract 1
        j += 1 if ltr else -1

        # if hit the end
        if j < 0 or j > len(snail[0]) - 1 or snail[i][j] != 0:
            hor = not hor
            ltr = not ltr
            i += j - prev
            j = prev

    prev = i
    i += -1 if ltr else 1

    if i < 0 or i > len(snail) - 1 or snail[i][j] != 0:
        hor = not hor
        j += prev - i
        i = prev

for i in snail:
    for j in i:
        print("%3d" % j, end =" ")
    print()