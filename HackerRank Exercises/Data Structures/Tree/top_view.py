class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
""" 

def topView(root):
    queue = [(root,0)]
    levels = [0]
    nodes = [root]
    while queue:
        node, lev = queue.pop()
        if node.left:
            queue.insert(0, (node.left, lev - 1))
        if node.right:
            queue.insert(0, (node.right, lev + 1))
        if lev not in levels:
            if lev < 0:
                levels.insert(0, lev)
                nodes.insert(0,node)
            else:
                levels.append(lev)
                nodes.append(node)
    
    for i in nodes:
        print(i.info, end = ' ')
        
    



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)