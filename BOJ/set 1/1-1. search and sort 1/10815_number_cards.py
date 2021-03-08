import sys

n = int(sys.stdin.readline())

cards = set(map(int, sys.stdin.readline().split()))

int(input())

print(' '.join(['1' if i in cards else '0' for i in list(map(int, sys.stdin.readline().split()))]))