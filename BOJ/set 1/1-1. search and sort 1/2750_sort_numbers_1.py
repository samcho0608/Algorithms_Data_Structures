# review just in case

def bs(l,n,low,up):
    if low >= up:
        return up

    mid = (up + low) // 2
    if l[mid] == n:
        return mid

    return bs(l, n, low, mid) if n < l[mid] else bs(l,n, mid + 1, up)



    
n = int(input())
nums = [int(input())]
for i in range(n - 1):
    t = int(input())
    nums.insert(bs(nums, t, 0, len(nums)), t)

for i in nums:
    print(i)