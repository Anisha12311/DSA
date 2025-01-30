class BinaryNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        


def In_order_recursion(root):
    stack = []
    current = root
    
    while True:
        while current:
            stack.append(current)
            current = current.left
            
        if not stack:
            break
        
        current = stack.pop()
        print(current.data, end = " ")
        current = current.right
        


root = BinaryNode(1)

root.left = BinaryNode(2)

root.left.left = BinaryNode(4)

root.left.right = BinaryNode(5)

root.right = BinaryNode(3)
root.right.left = BinaryNode(6)
root.right.right = BinaryNode(7)


In_order_recursion(root)