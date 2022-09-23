# can only use when data are integers
# effective when there are multiple repeated values

def counting_sort(arr):
    counter = [0 for i in range(max(arr) + 1)]
    # count occurrences
    for i in arr:
        counter[i] += 1
    index = 0
    for val, occur in enumerate(counter):
        while occur:
            arr[index] = val
            # occur -= 1
            index += 1

arr = [0,3,9,4,4,5,8,8,3,4,0,9,3,9]
counting_sort(arr)
print(arr)