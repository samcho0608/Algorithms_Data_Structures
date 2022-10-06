class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution :
    # stack method
    def reverseList(self, head):
        if not head :
            return None
        stk = []
        curr = head
        while curr :
            stk.append(curr)
            curr = curr.next

        
        resHead = stk.pop()
        curr = resHead
        while stk :
            curr.next = stk.pop()
            curr = curr.next
        curr.next = None
        return resHead