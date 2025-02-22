class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def find_size(root):
    queue  = [root]
    
    count = 0
    while queue:
        node = queue.pop(0)
        count =  count +1
        if node.left:
            queue.append(node.left)
            
        if node.right:
            queue.append(node.right)
            
    return count

        
r1 = Node(1)
r1.left = Node(2)
r1.right = Node(3)
r1.left.left = Node(4)
r1.left.right = Node(5)
r1.right.left = Node(6)
r1.right.right = Node(8)

print(find_size(r1))