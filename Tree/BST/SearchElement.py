class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def search_element(root, val):
    if not root:
        return None
    
    while root:
        print(root.data, val)
        if root.data == val:
            print( 'Found it')
            return root

        elif val > root.data:
            root = root.right
            
        else:
            root = root.left
            
    return None
                 
                

        
r1 = Node(5)
r1.left = Node(2)
r1.right = Node(8)
r1.left.left = Node(1)
r1.left.right = Node(4)
r1.right.left = Node(6)
r1.right.right = Node(7)
r1.left.right.left = Node(3)

print(search_element(r1, 4)
)