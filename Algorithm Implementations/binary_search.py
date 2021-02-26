# checks if n is in the given array
def binary_search(l, n, low, up):
    if low >= up:
        return 0
    mid = (up + low) // 2
    if l[mid] == n:
        return 1
    return 1 * (binary_search(l, n, low, mid) if n < l[mid] else binary_search(l, n, mid + 1, up))

# returns the index of the target or where it should be
def bs(l,n,low,up):
    if low >= up:
        return up

    mid = (up + low) // 2
    if l[mid] == n:
        return mid

    return bs(l, n, low, mid) if n < l[mid] else bs(l,n, mid + 1, up)

# BS with while
# def bs(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         if target > array[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

# left most index to insert x
print(bisect_left(a, x))
# right most indext to insert x
print(bisect_right(a, x))

# to find the number in range [L, R]
print(bisect_right(a,5) - bisect_left(a, 3))