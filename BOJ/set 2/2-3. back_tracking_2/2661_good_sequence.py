# sequence formed only with 1,2,3
# if there are two adjacent same subsequence, it's a bad sequence
# find the smaller number created with the sequence
from sys import stdin
n = int(stdin.readline())
def dfs(s, l):
    for i in range(1, (l+1)//2 + 1):
        for idx in range(l-i):
            if s[idx:idx+i] == s[idx+i:idx+2*i]:
                return
    if l == n:
        return s
    for i in ('1','2','3'):
        a = dfs(s+i, l + 1)
        if a:
            return a
s = dfs('',0)
print(s)