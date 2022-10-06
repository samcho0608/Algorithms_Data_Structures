class Solution :
    def detectCycle(self, head):
        t, h = head, head
        hasCycle = False
        while True :
            if t == None or h == None or h.next == None :
                break
            t = t.next
            h = h.next.next
            
            if t == h :
                hasCycle = True
                break
        if not hasCycle :
            return None
        t = head
        while t != h :
            t = t.next
            h = h.next
            if t == h :
                break
        return h