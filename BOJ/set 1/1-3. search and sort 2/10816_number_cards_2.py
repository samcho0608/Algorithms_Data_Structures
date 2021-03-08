# from bisect import bisect_left as left, bisect_right as right
# from sys import stdin

# n = int(stdin.readline().strip())
# cards = stdin.readline().split()
# cards.sort()
# int(stdin.readline())
# targets = stdin.readline().split()
# occur = []

# for i in targets:
#     occur.append(right(cards, i) - left(cards, i))

# print(' '.join(map(str, occur)))


from collections import Counter
from sys import stdin

n = int(stdin.readline().strip())
cards = Counter(stdin.readline().split())
int(input())
print(' '.join([str(cards[i]) if i in cards else '0' for i in stdin.readline().split()]))