class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class circle:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        
        newNode = Node(data)
        
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
            
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head
            
            
    def insertFirst(self, data):
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            
            newNode.next = self.head
            self.tail.next = newNode
            self.head = newNode
    
    def deleteLast(self):
        if not self.head:
            return 
        
        current = self.head
        prev = current
        while current.next != self.head:
            prev = current
            current = current.next
                    
        # Update references to remove the last node
        prev.next = self.head
        self.tail = prev
    
    def deleteFirst(self):
        if not self.head:
            print(False)
            return
        
        self.tail.next = self.head.next
        self.head = self.head.next
        
    def isCircle(self):
        current = self.head
        while current:
            current = current.next
            if current == self.head:
                print(True)
                return
            
        print(False)
                    
    def traverse(self):
        if not self.head:
            return 'Empty'
        current = self.head

        while True:
            print(current.data, end= '-> ')
            current = current.next
            
            if current == self.head:
                break
            
            
            
c = circle()

c.insert(1)
c.insert(2)
c.insert(3)
c.insert(4)
# c.insertFirst(12)
# c.deleteLast()
c.deleteFirst()
c.isCircle()
c.traverse()

        