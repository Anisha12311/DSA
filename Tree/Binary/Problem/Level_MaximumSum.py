class Node:
    def __init__(self, data, left = None, right = None):
        self.val = data
        self.left = left
        self.right = right
    
    
def Level_MaxSum(root):
    if not root:
        return []
    stack = [(root, str(root.val))]
    result = []
    
    while stack:
        
        node , path = stack.pop()
        if node.left is None and node.right is None:
            result.append(path)
            
        if node.left:
            stack.append((node.left, path + '->' + str(node.left.val)))
            
        if node.right:
            stack.append((node.right , path + '->' + str(node.right.val)))
     
    return result       
            
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)
r1.left.right.left = Node(10)

print(Level_MaxSum(r1))