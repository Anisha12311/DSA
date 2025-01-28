
# Array Implementation 
class Queue:
    def __init__(self):
        self.queue = [None] *4
        self.front = 0
        self.rear = 0
        self.size = 0
     
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == len(self.queue)   
        
    def enqueue(self, data):
        
        if self.is_full():
            print("Over flow")
            return
        
        self.queue[self.rear] = data
        self.rear += 1
        self.size += 1    
    
    def dequeue(self):
        
        if self.is_empty():
            print("Under flow")
            return
        
        self.queue.pop(0)
        self.front += 1
        self.size -= 1

    def display(self):
        return self.queue  
            
            
            
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.dequeue()
queue.dequeue()


print(queue.display())


#Linked List Queue Implementation:


class NodeLink:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0    
        
    def enqueue(self,data):
        
        new_node = NodeLink(data)
        
        if self.is_empty():
            self.front = self.rear = new_node
            
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    def dequeue(self):
        
        if self.is_empty():
            print("false")
            
        else:
            self.front = self.front.next
            
    def display(self):
        current = self.front
        element = []
        while current:
            element.append(current.data)
            current = current.next
            
        return element
    
    
linked_queue = LinkedQueue()

linked_queue.enqueue(1)
linked_queue.enqueue(2)
linked_queue.enqueue(3)
linked_queue.enqueue(4)
linked_queue.enqueue(5)

linked_queue.dequeue()

print(linked_queue.display())