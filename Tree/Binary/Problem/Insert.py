class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def Insert(root, data):
    queue = [root]
    
    if not root:
        return [] 
    newNode = Node(data)
    while queue:
        current = queue.pop(0)       
        if current.left is None:
            current.left =  newNode
            return
        else:
            queue.append(current.left)   
        if current.right is None:
            current.right = newNode
            return
        else:
            queue.append(current.right)



def Level_order(root):
    
    stack = [root]    
    while stack:
        current = stack.pop(0)
        
        print(current.data, end = " ")
        
        if current.left:
            stack.append(current.left)
            
        if current.right:
            stack.append(current.right)

    
        
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(7)

Insert(r1, 8)
Insert(r1, 10)

Level_order(r1)