class BinaryNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def Post_order(root):
    
    s1 = [root]
    s2 = []
    
    while s1:
        current = s1.pop()
        
        s2.append(current.data)
        
        if current.left:
            s1.append(current.left)
            
        if current.right:
            s1.append(current.right)
    
    while s2:
        print(s2.pop(), end= " ")

root = BinaryNode(10)

root.left = BinaryNode(8)

root.right = BinaryNode(2)

root.left.left = BinaryNode(3)

root.left.right = BinaryNode(5)


root.right.left = BinaryNode(6)


print(Post_order(root))