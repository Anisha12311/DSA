class Circular:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.size = 0
        self.queue = [None] *4
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == len(self.queue)
        
    def enqueue(self,data):
        
        if self.is_full():
            print("overflow")
            return
            
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % 4
        self.size += 1
        
    def dequeue(self):
        
        if self.is_empty():
            print("underflow")
            return 
        
        data = self.queue[self.front]
        
        self.queue[self.front] = None
        
        self.front = (self.front + 1) % 4
        self.size -= 1
        
        return data
        
        
    def display(self):
        print(self.queue)
        

circular = Circular()

circular.enqueue(1)
circular.enqueue(2)
circular.enqueue(3)
circular.enqueue(4)

circular.dequeue()
circular.dequeue()

circular.enqueue(6)
circular.enqueue(7)

circular.display()

