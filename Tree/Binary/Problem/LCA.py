class Node:
    def __init__(self, data, left = None, right = None):
        self.val = data
        self.left = left
        self.right = right
    
    
def LAC(root):
    if not root:
        return []
       
    stack = [(root, root.val)]
    minvalue = 0
    while stack:
        
        node, value = stack.pop()
        
        
        if value > node.left and node.left.left and node.left.right:
            
            stack.append((node.left, node.left.value))
        
            
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)
r1.left.right.left = Node(10)

print(LAC(r1))