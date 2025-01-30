class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
        


def In_order(root):
    
    if root: 
        
        In_order(root.left)
        
        print(root.data, end = " ")
        
        In_order(root.right)
        
        

root = TreeNode(1)

root.left = TreeNode(2)

root.left.left = TreeNode(4)

root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


In_order(root)