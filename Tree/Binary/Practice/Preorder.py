class BinaryNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def Pre_order_traversal(root):
    
    if not root:
        return []
    stack = [root]
    
    result = []
    
    while stack:
        
        node = stack.pop()
        
        result.append(node.data)
        
        if node.right:
            stack.append(node.right)
            
        if node.left:
            stack.append(node.left)
            
    return result
    


root = BinaryNode(10)

root.left = BinaryNode(8)

root.right = BinaryNode(2)

root.left.left = BinaryNode(3)

root.left.right = BinaryNode(5)


root.right.left = BinaryNode(6)


print(Pre_order_traversal(root))