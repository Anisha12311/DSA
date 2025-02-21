
from collections import deque
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        

def isIdentical(r1,r2):
    
    if not r1 and not r2:
        return True
    
    if not r1 or not r2:
        return False
    
    q1 = deque([r1])
    q2 = deque([r2])
    
    
    while q1 and q2:
        
        n1 = q1.popleft()
        n2 = q2.popleft()
        
        if n1.data != n2.data:
            return False
        
        if n1.left and n2.left:
            q1.append(n1.left)
            q2.append(n2.left)
            
        elif n1.left or n2.left:
            return False
        
        
        if n1.right and n2.right:
            q1.append(n1.right)
            q2.append(n2.right)
            
        elif n1.right or n2.right:
            return False
        
    
    return not q1 and not q2
        




if __name__ == "__main__":
    r1 = Node(1)
    r1.left = Node(2)
    r1.right = Node(3)
    r1.left.left = Node(4)
    
    
    r2 = Node(1)
    r2.left = Node(2)
    r2.right = Node(2)
    r2.left.left = Node(4)
    print("heelo")
    if isIdentical(r1,r2):
        print("Yes")
    else:
        print("No")
        
        
    
    
    
    
