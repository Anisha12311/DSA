class Node:
    def __init__(self, data, left = None, right = None):
        self.val = data
        self.left = left
        self.right = right
        
def ExistingSumPath(root, sum):
    
    stack = [(root, root.val, str(root.val))]
    
    while stack: 
        
        node, val_sum, path = stack.pop()
        
        
        if val_sum == sum:
            return path
        
        if node.left:
            stack.append((node.left, val_sum+node.left.val, path + '->' + str(node.left.val)))
            
        if node.right:
            stack.append((node.right, val_sum + node.right.val, path + '-> ' + str(node.right.val) ))
            
        

r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)
r1.left.right.left = Node(10)

print(ExistingSumPath(r1,18))