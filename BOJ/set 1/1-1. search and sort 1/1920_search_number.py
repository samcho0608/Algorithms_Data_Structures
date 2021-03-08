# Lesson Learned, list slicing is SLOW

def merge_sort(l):
    if len(l) == 1:
        return l

    first = merge_sort(l[:len(l)//2])
    second = merge_sort(l[len(l)//2:])
    to_return = []
    while first and second:
        if first[0] < second[0]:
            to_return.append(first[0])
            first = first[1:]
        else:
            to_return.append(second[0])
            second = second[1:]

    to_return.extend(first if first else second)
    return to_return

#     *  
# 1 2 3 4 5
# mid = 2

#         *
# 1 2 3 4 5
# mid = 2
#       4 5
# mid = 0
#         5
# mid = 0


# even looks for the index
# def binary_search(l, num):
#     if len(l) == 1 and l[0] != num:
#         return -1
#     mid = len(l)//2
#     if num == l[mid]:
#         return mid

#     return_val = binary_search(l[:mid], num) if num < l[mid] else binary_search(l[mid+1:], num)
#     return -1 if return_val == -1 else return_val if num < l[mid] else mid + return_val + 1

# def binary_search(l, num):
#     if len(l) == 1:
#         return l[0] == num
#     mid = len(l) // 2
#     if l[mid] == num:
#         return True
#     return True and (binary_search(l[:mid], num) if num < l[mid] else binary_search(l[mid:], num))

def binary_search(l, n, low, up):
    if low >= up:
        return 0
    mid = (up + low) // 2
    if l[mid] == n:
        return 1
    return 1 * (binary_search(l, n, low, mid) if n < l[mid] else binary_search(l, n, mid + 1, up))

int(input())
nums = list(map(int, input().split()))
int(input())
target = list(map(int,input().split()))
# nums = merge_sort(nums)
nums.sort()
for i in target:
    print(int(binary_search(nums, i, 0, len(nums))))