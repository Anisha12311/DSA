class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def isvalid_bst(root):
    
    if not root:
        return True
    
    
    stack = [(root, float('-inf'), float('inf'))]
    
    
    while stack:
        
        node, min_val, max_val = stack.pop()


        if not (min_val < node.data < max_val):
            print(min_val, node.data, max_val)
            return False
        
        
        if node.right :
            stack.append((node.right, node.data, max_val))
            
        if node.left:
            
            stack.append((node.left, min_val, node.data))
            
            
    return True    
    
                 
                

        
r1 = Node(5)
r1.left = Node(2)
r1.right = Node(8)
r1.left.left = Node(1)
r1.left.right = Node(4)
r1.right.left = Node(6)
r1.right.right = Node(10)
r1.left.right.left = Node(3)

print(isvalid_bst(r1))