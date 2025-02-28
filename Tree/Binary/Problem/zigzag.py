from collections import deque

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def zigzag(root):
    
    stack = deque([root] )
    left_right = True
    result = []
    next_level = deque()
    
    while stack:
        node = stack.pop()   
        result.append(node.data)
        
        if left_right :         
            if node.left:
                next_level.append(node.left)  
            if node.right:
                next_level.append(node.right)
        
        else : 
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
                
        if not stack:
            stack, next_level = next_level, stack
            left_right =  not left_right
        
    return result       
            

r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(7)

print(zigzag(r1))