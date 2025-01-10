class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
    
    def isEmpty(self):
        return len(self.stack) == 0
             
    def pop(self):
        
        if not self.isEmpty():
            self.stack.pop()
            return 
        else : 
            print("Empty list")
            return
        
    def peek(self):
        
        if not self.isEmpty():
            return self.stack[-1]
        print("List empty")
        return
    def size(self):
        return len(self.stack)    

    def display(self):
        print(self.stack)

stack = Stack()

stack.push(10)        
stack.push(20)        
stack.push(30)        
stack.push(40)        
stack.push(50)

# stack.pop()
# stack.pop()

print(stack.peek())
print(stack.peek())


stack.display()        