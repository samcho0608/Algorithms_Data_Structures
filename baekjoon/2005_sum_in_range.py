length, target = map(int, input().split())

array = list(map(int, input().split()))

begin = end = count = p_sum = 0

while True:
    if p_sum < target:
        if end >= length:
            break
        p_sum += array[end]
        end += 1
    else:
        p_sum -= array[begin]
        begin += 1
    if p_sum == target:
        count += 1
print(count)