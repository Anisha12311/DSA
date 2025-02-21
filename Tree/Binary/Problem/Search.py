class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
def Search_element(root, data):
    
    stack = [root]
    
    while stack:
        
        node = stack.pop()
        
        if node.data == data:
            return "Found the element"
        
        if node.left:
            stack.append(node.left)
            
        if node.right:
            stack.append(node.right)
            
    return "Not found"
    


r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)


print(Search_element(r1,13))