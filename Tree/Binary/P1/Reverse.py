
class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    
def reverse_level_order(root):
    queue = [root]
    stack = []
    while queue:
        temp = queue.pop(0)
       
        if temp.right:
           queue.append(temp.right)
             
        if temp.left:
            queue.append(temp.left)
            
        stack.append(temp.data)
        
    while stack:
        print(stack.pop() , end=' ')
   
def deleteNode(root):
    
    s1 = [root]
    s2 = []
    
    while s1 :
        temp = s1.pop()
        s2.append(temp)
        if temp.right : 
            s1.append(temp.right)
            
        if temp.left:
            s1.append(temp.left)
            
        
    while s2:
        node = s2.pop()
        
        print("delete node", node.data)
        
        node.left = None
        node.right = None
        
        del node
    
    
    
def height(root):
    
    stack = [root]
    max_height = 0
    while stack:
        temp = stack.pop()
        
        if temp.left or temp.right:
            max_height += 1
            
        if temp.right :
            stack.append(temp.right)
            
        if temp.left:
            stack.append(temp.left)
            
            
    return max_height


def find_leaf(root):
    
    stack = [root]
    count = 0
    while stack:
        temp = stack.pop()
        
        if  (not temp.left and  temp.right ) or (temp.left and not temp.right):
            count +=1 
            
            
        if temp.right:
            stack.append(temp.right)
            
        if temp.left:
            stack.append(temp.left)
            
    return count
      
      
def max_level(root):
    
    queue = [root]
    max_sum = 0
    level = 0
    max_level = 0
    
    while queue:
        current_sum = 0
        temp = queue.pop(0)
        
        if temp.left or temp.right:
            level += 1
        
        if temp.left:
            current_sum += temp.left.data
            queue.append(temp.left)
        if temp.right:
            current_sum += temp.right.data
            queue.append(temp.right)
               
        if current_sum > max_sum:
            max_sum = current_sum
            max_level = level
            
    return max_level


def level(root):
    queue = [root]
    level = 0
    while queue:
        temp = queue.pop(0)
        
        
        if temp.left or temp.right:
            level += 1
                
        if temp.left : 
            queue.append(temp.left)
            
        if temp.right:
            queue.append(temp.right)
            
            
    return level

root = TreeNode(1)

root.left = TreeNode(2)
root.right  = TreeNode(43)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(65)
root.right.right = TreeNode(7)

# reverse_level_order(root)
# deleteNode(root)
 
# print(height(root))
# print(find_leaf(root))
print(max_level(root))
# print(level(root))