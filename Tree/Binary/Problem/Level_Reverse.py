class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def Level_reverse(root):
    
    if not root:
        return []
    
    queue = [root]
    stack = []
    
    while queue:
        
        current = queue.pop(0)
        
        stack.append(current.data)
        
        if current.right:
            queue.append(current.right)
            
        if current.left:
            queue.append(current.left)
            
            
    return stack[::-1]
    
    


r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(7)


print(Level_reverse(r1))