#  Give an algorithm for finding maximum element in binary tree.



class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
        
        
def maximum_element(root):
    
    s1 = [root]
    s2 = []
    
    max = root.data
    while s1:
        
        current = s1.pop()
        
        s2.append(current)
        
        if max < current.data:
            max = current.data
            
        if current.left:
            s1.append(current.left)
            
            
        if current.right:
            s1.append(current.right)
            
    while s2:
        print(s2.pop().data, end= " ")
    
    print("max", max)    
        
        
root = TreeNode(12)

root.left = TreeNode(2)

root.left.left = TreeNode(42)

root.left.right = TreeNode(11)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

maximum_element(root)





# Give an algorithm for searching an element in binary tree.




def search_element(root, val):
    
    s1 = [root]
    s2 = []
    
    max = root.data
    while s1:
        
        current = s1.pop()
        if val == current.data:
            print(f"Found the value {val} == {current.data}")
            return
        s2.append(current)
        
        if max < current.data:
            max = current.data
            
        if current.left:
            s1.append(current.left)
            
            
        if current.right:
            s1.append(current.right)
            
    while s2:
        print(s2.pop().data, end= " ")
    
    print("max", max)    
        
        
root = TreeNode(12)

root.left = TreeNode(2)

root.left.left = TreeNode(42)

root.left.right = TreeNode(11)

root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

search_element(root,3)