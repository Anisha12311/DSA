class TreeNode :
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False 
        
        
def insert(root, key):
    current = root
    
    for c in key:
        index = ord(c) - ord('a')
        if current.children[index] is None:
            current.children[index] = TreeNode()
        current = current.children[index]
    current.isEnd = True

def search(root, key):
    current = root
    
    for c in key:
        index = ord(c) - ord('a')
        if current.children[index] is None:
            return False
        
        current = current.children[index]
    return current.isEnd

def prefix(root, key):
    current = root
    
    for c in key:
        index = ord(c)- ord('a')
        
        if current.children[index] is None:
            return False
        current = current.children[index]
    
    return True    

arr = ["and", "ant", "do", "dad"]

tries = TreeNode()
for data in arr:
    insert(tries, data)
    
    
# searchKeys = ["do", "gee", "bat"]
# for searchData in searchKeys:
#     print(search(tries, searchData))

prefixKeys = ["ge", "ba", "do", "da"]

for prefixK in prefixKeys:
    print(prefix(tries, prefixK))
