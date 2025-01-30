class BinaryNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        

def post_order(root):
    
    s1 = [root]
    s2 = []
    
    while s1:
        
        current = s1.pop()
        
        s2.append(current)
        
        if current.left:
            s1.append(current.left)
            
        if current.right:
            s1.append(current.right)
            
            
    while s2:
        print(s2.pop().data, end = " ")    


root = BinaryNode(1)

root.left = BinaryNode(2)

root.left.left = BinaryNode(4)

root.left.right = BinaryNode(5)

root.right = BinaryNode(3)
root.right.left = BinaryNode(6)
root.right.right = BinaryNode(7)

post_order(root)
