class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.eq = None
        self.right = None
        self.isEnd = False
        
        

def insert(root, word):
    if not root:
        root = Node(word[0])
        
    if word[0]< root.data:
        root.left = insert(root.left, word)
    elif word[0] > root.data:
        root.right = insert(root.right, word)
        
    else:
        if len(word) > 1:
            root.eq = insert(root.eq, word[1:])
        else:
            root.isEnd = True
    return root       
            
def search(root, word):
    if not root:
        return False
    
    if word[0] < root.data:
        return search(root.left, word)
    
    elif word[0] > root.data:
        return search(root.right, word)
    
    else:
        if len(word) > 1:
            return search(root.eq, word[1:])
        else:
            return root.isEnd
        
root = Node('')
insert(root, 'cat')
insert(root, "cats")
insert(root, "up")
insert(root, "bug")

print("Found" if search(root, "cats") else "Not Found")
print("Found" if search(root, "bu") else "Not Found")
print("Found" if search(root, "up") else "Not Found")