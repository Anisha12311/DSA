class Node:
    def __init__(self,data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
        
def delete_node(root,key):
    
    if not root:
        return None
    
    if key < root.data:
        root.left = delete_node(root.left, key)
        
    elif key > root.data:
        root.right = delete_node(root.right, key)
        
        
    else:
        
        if not root.left:
            return root.right
        
        elif not root.right:
            return root.left
        
        
        curr = root.right
        
        while curr.left:
            curr = curr.left
            
        root.data = curr.data
        
        root.right = delete_node(root.right, curr.data)
        
    return root
    
    
def deleteNode(root, key):
    
    if not root:
        return False
    
    
    
    
def in_order(root):
    
    if not root:
        return []
    in_order(root.left)
    print(root.data)
    in_order(root.right)
    
        
    
r1 = Node(5)
r1.left = Node(2)
r1.right = Node(8)
r1.left.left = Node(1)
r1.left.right = Node(4)
r1.right.left = Node(6)
r1.right.right = Node(7)
r1.left.right.left = Node(3)
 
delete_node(r1,4)

in_order(r1)
    
    
    