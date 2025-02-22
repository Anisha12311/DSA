class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    
def post_order(root):
    
    s1 = [root]
    s2 = []
    
    while s1 :
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
            
    while s2:
        
        node = s2.pop()
        
    
        print(f"delete node : {node.data}")
        
        node.left = None
        node.right = None
        
        del node
    
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(7)


post_order(r1)