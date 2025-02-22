class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def deepest_node(root):
    queue = [root]
    while queue:
        
        current = queue.pop(0)
        
        if current.left:
            
            queue.append(current.left)
        if current.right:
            
            queue.append(current.right)

    return current.data    
    
            
                

        
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)
r1.left.right.left = Node(10)

print(deepest_node(r1))