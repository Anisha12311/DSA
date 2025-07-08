class Node :
    def  __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1
        
        
    
class AVLTree:
    def get_height(self, root):    
        return root.height if root else 0
    
    def get_balanced(self, root):
        return self.get_height(root.left)-self.get_height(root.right) if root else 0
    
    def right_rotate(self, z):
        y = z.left
        
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        return y
    
    def left_rotation(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        
        return y
    
    
        
    def insert(self,root, data):
        
        if not root:
            return Node(data)
        
        elif data < root.data : 
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balanced = self.get_balanced(root)
        
        if balanced > 1 and data < root.left.data : 
            return self.right_rotate(root)
        
        if balanced < -1 and data > root.right.data:
            return self.left_rotation(root)
        
        
        if balanced > 1 and data > root.left.data:
            root.left = self.left_rotation(root.left)
            return self.right_rotate(root)
        
        if balanced < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotation(root)
        
        
        return root
    
    def pre_order(self,root):
        if root:
            print(root.data, end= '-> ')
            
            self.pre_order(root.left)
            self.pre_order(root.right)
            
            
            
tree = AVLTree()

root = None

values = [10, 20, 30, 40, 50, 25]

for val in values:
    root = tree.insert(root, val)
    
tree.pre_order(root)
        
        
        
        
