
class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    
def max_element(root):
    stack = [root]
    max_element = 0
    if not root :
        return []
    while stack:
        current_node = stack.pop()
        
        max_element += 1
        
        if current_node.right:
            stack.append(current_node.right) 
            
        if current_node.left:
            stack.append(current_node.left)
        
    return max_element
        
def max_value(root):
    stack = [root]
    max_val = 0
    
    if not root :
        return []
    while stack:
        
        current_node = stack.pop()
        
        if max_val < current_node.data:
            max_val = current_node.data
            
        if current_node.right:
            stack.append(current_node.right) 
            
        if current_node.left:
            stack.append(current_node.left)
    return max_val


def search_element(root, data):
    
    if not root:
        return False
    
    
    stack = [root]
    
    while stack:
        current_node = stack.pop()
        
        if current_node.data == data:
            return True
        
        if current_node.right:
            stack.append(current_node.right) 
            
        if current_node.left:
            stack.append(current_node.left)
    
    return False


def insert_element(root, data):
    
    stack = [root]
    new_node = TreeNode(data)
    while stack:
        current_node = stack.pop()
        
        if not current_node.right:
            current_node.right = new_node
            return root
        else:
            stack.append(current_node.right)
            
        if not current_node.left:
           
            current_node.right = new_node
            return root
        else:
            stack.append(current_node.left)
    
def traversal(root):
    
    stack = [root]
    
    while stack:
        current_node = stack.pop()
        print(current_node.data, end= '-> ')  
        if current_node.right:
            stack.append(current_node.right) 
            
        if current_node.left:
            stack.append(current_node.left)
    print(None)       

root = TreeNode(1)

root.left = TreeNode(2)
root.right  = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(max_element(root))
print(max_value(root))

print(search_element(root, 5))
insert_element(root,15)
traversal(root)