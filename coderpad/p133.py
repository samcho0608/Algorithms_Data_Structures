class Node :
    def __init__(self, value, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value
    
def next_bigger_node(node : Node) :
    # right 이 존재할 경우
    if node.right :
        # right의 left-most 자식 노드가 다음으로 가장 큼
        get_left_most_child(node.right)

    # right 이 존재하지 않는 경우
    else :
        # 부모 노드가 다음으로 가장 큼
        return node.parent

def get_left_most_child(node : Node) -> Node:
    curr = node
    while curr.left :
        curr = curr.left
    return curr