class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# def insert_bst(root, key):
    
#     if root is None:
#         return Node(key)
    
    
        
#     if key < root.data:
        
#         root.left = insert_bst(root.left, key)
        
#     else:
#         root.right = insert_bst(root.right, key)
    
    
#     return root         
                
# root = Node(5)
# root = insert_bst(root, 2)
# root = insert_bst(root, 8)
# root = insert_bst(root, 1)
# root = insert_bst(root, 4)
# root = insert_bst(root, 6)
# root = insert_bst(root, 9)

# # Insert new element
# root = insert_bst(root, 7)

# def inorder_traversal(root):
#     if root is None:
#         return
#     inorder_traversal(root.left)
#     print(root.data, end=" ")
#     inorder_traversal(root.right)

# # Print BST elements in sorted order
# inorder_traversal(root)
# # print(root)




def insert_element(root, key):
    
    if not root : 
        return Node(key)
    
    current = root
    
    while True:
        
        if key < current.data:
            if current.left is None:
                current.left = Node(key)
                break
            
            current = current.left
            
        else:
            if current.right is None:
                current.right = Node(key)
                
                break
            current = current.right
    
    return root        
            
root = Node(5)
root = insert_element(root, 2)
root = insert_element(root, 8)
root = insert_element(root, 1)
root = insert_element(root, 4)
root = insert_element(root, 6)
root = insert_element(root, 9)

# Insert new element
root = insert_element(root, 7)   


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)

# Print BST elements in sorted order
inorder_traversal(root)
      

