class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    
def max_depth(root):
    
    if not root:
        return 0
    
    stack = [(root, 1)]
    max_depth = 0
    while stack:
        
        node, depth = stack.pop()
        
        if node :
            max_depth = max(max_depth, depth)
            
            if node.left:
                stack.append((node.left, depth+1))
                
            if node.right:
                stack.append((node.right, depth+1))
                
        
    return max_depth

    
    

root = TreeNode(1)

root.left = TreeNode(2)

root.left.left = TreeNode(4)

root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)



print(max_depth(root))