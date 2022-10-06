from math import ceil


class Solution :
    def middleNode(self, head):
        stk = []
        curr = head
        while curr :
            stk.append(curr)
            curr = curr.next
        return stk[int(ceil(len(stk)/2))]