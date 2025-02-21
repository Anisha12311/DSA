class BinaryNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def In_order(root):
    
    stack= []
    
    current = root
    
    
    while True:
        while current:
            stack.append(current)
            current = current.left
            
            
        if not stack:
            break
        
        current = stack.pop()
        
        print(current.data, end = " ")
        
        current = current.right
        
        
    
    
    
    


root = BinaryNode(10)

root.left = BinaryNode(8)

root.right = BinaryNode(2)

root.left.left = BinaryNode(3)

root.left.right = BinaryNode(5)


root.right.left = BinaryNode(6)


print(In_order(root))