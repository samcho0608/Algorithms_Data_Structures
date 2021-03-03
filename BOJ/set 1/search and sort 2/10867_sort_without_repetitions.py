from sys import stdin

int(input())
nums = set(map(int, stdin.readline().split()))

print(' '.join(map(str, sorted(nums))))
