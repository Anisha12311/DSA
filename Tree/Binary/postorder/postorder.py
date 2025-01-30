class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end= " ")
        
        

root = TreeNode(1)

root.left = TreeNode(2)

root.left.left = TreeNode(4)

root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


post_order(root)