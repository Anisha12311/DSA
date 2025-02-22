class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def find_height(root):
    queue = [root]
    current_level_count = 1
    
    next_level_count = 0
    tree_height = -1
    
    while queue:
        current = queue.pop(0)
        
        current_level_count -=1
        
        if current.left:
            queue.append(current.left)
            next_level_count +=1
            
        if current.right:
            queue.append(current.right)
            next_level_count += 1
            
        if current_level_count == 0:
            tree_height += 1
            current_level_count = next_level_count
            
            next_level_count = 0
            
    return tree_height
            
                

        
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)

print(find_height(r1))