class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def ExistingSumPath(root, sum):
    
    stack = [(root, root.data, str(root.data))]
    
    while stack:
        current, sum_val, path = stack.pop()
        
        
        if sum_val == sum:
            print(path)
            
        if current.right:
            stack.append((current.right, sum_val + current.right.data, path + '-> ' + str(current.right.data)))
            
        if current.left:
            stack.append((current.left, sum_val + current.left.data, path + '-> ' + str(current.left.data)))
    

r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)
r1.left.right.left = Node(10)

ExistingSumPath(r1,18)