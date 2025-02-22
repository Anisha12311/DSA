class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
def Max_level(root):
    
    if not root:
        return 0
    
    
    q = [root]
    max_level = 1
    level = 1
    max_sum = float('-inf')
    
    
    while q:
        
        level_sum = 0
        next_level = []
        
        for node in q:
            
            level_sum += node.data
            
            if node.left:
                next_level.append(node.left)
                
            if node.right:
                next_level.append(node.right)

        if level_sum > max_sum :
            max_sum = level_sum
            max_level = level
            
        q = next_level
        level += 1
        
    return max_level
        
        
        
    
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)
r1.left.right.left = Node(10)
r1.left.right.right = Node(11)

print(Max_level(r1))