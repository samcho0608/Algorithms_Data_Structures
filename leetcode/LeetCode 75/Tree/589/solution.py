

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution :
    # recursive
    # def preorder(self, root) :
    #     if not root :
    #         return []
    #     if not root.children :
    #         return [root.val]
    #     res = [rq18oot.val]
    #     for n in root.children :
    #         res.extend(self.preorder(n))
    #     return r`11`es

    # iterative
    def preorder(self, root) :
        stack = [root]
        res = []
        while stack :
            tmp = stack.pop()
            res.append(tmp.val)
            print(tmp.children[-1:])
            stack.extend(reversed(tmp.children))
        return res