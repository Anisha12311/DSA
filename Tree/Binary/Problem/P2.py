class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    
    
def insert_element(root, element):
    
    queue = [root]
    
    while queue:
        
        current = queue.pop(0)
        
        
        if not current.left:
            current.left = TreeNode(element)
            break
        else:
            queue.append(current.left)
            
        if not current.right:
            current.right = TreeNode(element)
            break
        else:
            queue.append(current.right)
    
        

def level_order_traversal(root):
    
        queue = [root]
        
        while queue:
            
            current = queue.pop(0)
            
            print(current.data, end = " ")
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
                
                



# Give an algorithm for finding the size of binary tree


def finding_size(root):
    
    s1 = [root]
   
    
    size = 0
    
    while s1:
        
        current = s1.pop()
       
        size +=1
       
        if current.left:
           s1.append(current.left)
           
        if current.right:
            s1.append(current.right)
    print("size = ", size)
  
  
  
# Give an algorithm for printing the level order data in reverse order. For example,
# the output for the below tree should be: 4 5 6 7 2 3 1

def level_order_traversal_reverse(root):
    
        queue = [root]
        stack = []
        while queue:
            
            current = queue.pop(0)
            stack.append(current.data)
            
            if current.right:
                queue.append(current.right)

            if current.left:
                queue.append(current.left)


        while stack:
            print(stack.pop(), end=" ")


# Give an algorithm for deleting the tree.  

def level_order_traversal_delete(root):
    
        queue = [root]
        
        while queue:
            
            current = queue.pop(0)
            
            print(current.data, end = "\n")
            
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)
            current.left = current.right = None
            
        return None
    
root = TreeNode(1)

root.left = TreeNode(2)

root.left.left = TreeNode(4)

root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

level_order_traversal(root)

# insert_element(root, 4)
# insert_element(root, 34)
# print("\nAfter Insertion:")

level_order_traversal(root)


finding_size(root)

level_order_traversal_reverse(root)
print("\n Delete Node")
print(level_order_traversal_delete(root))


