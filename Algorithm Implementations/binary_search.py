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