def array_to_linked_list(array) :
    if not array :
        return None

    head = ListNode(array[0])
    ptr = head
    i = 1
    while i < len(array) :
        ptr.next = ListNode(array[i])
        ptr = ptr.next
        i += 1
    return head

def linked_list_to_array(ll) :
    result = []
    ptr = ll
    while ptr :
        result.append(ptr.val)
        ptr = ptr.next
    return result

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
