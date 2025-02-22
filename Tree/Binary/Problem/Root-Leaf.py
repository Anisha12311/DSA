class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def RootToLeaf(root):
    
    stack = [(root, str(root.data))]
    
    while stack:
        
        current , path = stack.pop()
        
        if current.left is None and current.right is None:
            print(path)
            
            
        if current.right :
            stack.append((current.right, path + '-> ' + str(current.right.data)))
            
        if current.left:
            stack.append((current.left, path + '-> ' + str(current.left.data)))
            
    
    
            
                

        
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)
r1.left.right.left = Node(10)

RootToLeaf(r1)