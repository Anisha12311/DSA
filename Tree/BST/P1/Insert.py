class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        


def insert(root, key):
 
    if root is None:
        return  Node(key)
 
    current = root

    while True:
        
        if current.val > key:
            if current.left is None:
                current.left = Node(key)
                break
            current = current.left
            
        if current.val < key:
            if current.right is None:
                current.right = Node(key)
                break
            current = current.right
        
        
    return root


def searchElement(root, key):
    if root is None:
        return False
    
    
    while root:
        
        if root.val == key:
            print("found it",  root.val)
            return root
            
        if key < root.val:
            root = root.left
        else:
            root = root.right
    return False
  
def inorder(root):
    if root is None:
        return root
    
    inorder(root.left)
    print(root.val, end= " ")
    inorder(root.right)      
    
    return root
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
print(searchElement(r,35))
inorder(r)