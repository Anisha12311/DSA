class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def all_ancestors(root, node_val):
    stack = [(root, str(root.data))]
    
    while stack:
        node, path = stack.pop()
        
        if node.data == node_val:
            return path
        
        if node.left:
            stack.append((node.left, path + ',' + str(node.left.data)))
            
        if node.right:
            stack.append((node.right, path + ',' + str(node.right.data)))
            
    
      
                

        
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(7)

print(all_ancestors(r1,5))