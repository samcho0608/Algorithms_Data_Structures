# increasing length
# lexicographical order

# stable sort
# complex sort

# if we want order a then order b
# we sort in b first then in a

from sys import stdin
n = int(input())

words = set()
for i in range(n):
    words.add(stdin.readline().strip())

for i in sorted(sorted(words), key=lambda x: len(x)):
    print(i)