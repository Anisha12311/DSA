class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def Invert(root):
    
    if not root:
        return None
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        node.left, node.right = node.right, node.left
        
        
        if node.left:
            stack.append(node.left)
            
        if node.right:
            stack.append(node.right)

    return root

def In_order(root):
    
    stack = []
    current = root
    
    while stack or current:
        
        while current:
            stack.append(current)
            current = current.left
            
            
        if not stack:
            break
        
        current = stack.pop()
        
        print(current.data, end= " ")
        
        current = current.right
        
        
    return stack
    

if __name__ == "__main__":
    r1 = Node(1)
    r1.left = Node(2)
    r1.right = Node(3)
    r1.left.left = Node(4)
    r1.left.right = Node(5)

    
    In_order(r1)
    
    Invert(r1)
    
    print("After")
    
    In_order(r1)
    
    r2 = Node(1)
    r2.left = Node(2)
    r2.right = Node(2)
    r2.left.left = Node(4)
    