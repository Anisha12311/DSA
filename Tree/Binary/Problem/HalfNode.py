class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def HalfNode(root):
    
    queue = [root]
    count = 0
    while queue:
        
        current = queue.pop(0)
        
        if (current.left is None and current.right) or (current.left and current.right is None):
            count += 1
            
        if current.left:
            queue.append(current.left)
            
        if current.right:
            queue.append(current.right)
            
            
            
            
    return count
    
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)
r1.left.right.left = Node(10)

print(HalfNode(r1))