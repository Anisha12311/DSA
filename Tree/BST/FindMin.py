class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def find_min(root):
    
    if not root:
        return None
    
    
    while root.left is not None:
        
        root = root.left
        
    return root.data
    
    
def find_max(root):
    
    if not root:
        return None
    
    while root.right != None:
        
        root = root.right
        
    return root.data
                 
                

        
r1 = Node(5)
r1.left = Node(2)
r1.right = Node(8)
r1.left.left = Node(1)
r1.left.right = Node(4)
r1.right.left = Node(6)
r1.right.right = Node(10)
r1.left.right.left = Node(3)

print(find_min(r1))

print(find_max(r1))