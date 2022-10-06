class Solution :
    # iterative
    def levelOrder(self, root) :
        stack = []
        if root :
            stack.append([root])
        for lvl in stack :
            lvlNodes = []
            for n in lvl :
                if n.left :
                    lvlNodes.append(n.left)
                if n.right :
                    lvlNodes.append(n.right)
            if lvlNodes :
                stack.append(lvlNodes)
        return [[n.val for n in lvl] for lvl in stack]