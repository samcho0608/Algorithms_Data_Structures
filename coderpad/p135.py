# This question was asked by Apple.

# Given a binary tree, find a minimum path sum from root to a leaf.

# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1

from collections import deque

class Node :
    def __init__(self, value, left, right):
        self.left = left
        self.right = right
        self.value = value

def min_path(root) :
    q = deque([(root, root.value)])
    min_path_to_leaves = float('inf')

    while q :
        node, path_sum = q.popleft()

        if not node.left and not node.right :
            min_path_to_leaves = min(path_sum, min_path_to_leaves)
            continue

        if node.left :
            q.append((node.left, path_sum + node.left.value))
        if node.right :
            q.append((node.right, path_sum + node.right.value))

    return min_path_to_leaves

