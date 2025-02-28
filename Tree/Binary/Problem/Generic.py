class TreeNode:
    def __init__(self, data, first_child = None, next_child = None):
        self.data = data
        self.first_child = first_child
        self.next_child = next_child
        
        
def generic_tree(root):
    pass




root = TreeNode(1)
root.first_child = TreeNode(2)
root.first_child.next_sibling = TreeNode(3)
root.first_child.next_sibling.next_sibling = TreeNode(4)
root.first_child.first_child = TreeNode(5)
root.first_child.first_child.next_sibling = TreeNode(6)
root.first_child.next_sibling.first_child = TreeNode(7)
    