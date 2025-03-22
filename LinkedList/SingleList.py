class Node :
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class SList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def length(self):
        curr  = self.head
        count = 0
        while curr:
            count +=1
            
            curr = curr.next
            
        return count
      
    # Insert Element
    
    def insert(self, data):
        newNode = Node(data)
        # o(1)
        if self.head == None:
            self.head = newNode
            self.tail = newNode

            
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def insertFirst(self, data):
        # o(1)
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode           
        else:
            newNode.next = self.head
            self.head = newNode
    
    def insertPosition(self, data, position):
        # o(n)
        len = self.length() 
        
        if position > len+1:
            print("Out of index")
            return
            
        if position <= 0:
            print("Not a valid position")
            return   
        
        if position == 1:
            self.insertFirst(data)
            return
        
        if position == len+1:
            self.insert(data)
            return
        
            
        newNode = Node(data)    
        curr = self.head
        prev = None
        for i in range(position-2):
            prev = curr
            curr = curr.next        
        prev.next = newNode
        newNode.next = curr
    
    # Delete Element
    
    def deleteEnd(self):
        # o(n)
        if self.head is None:
            print(False)
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print(True)
        else :
            prev = None
            curr = self.head
            while curr and curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            self.tail = prev
               
    def deleteBegin(self) :
        # o(1)
        if self.head is None:
            print(False)
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            print(True)
        else :
            self.head = self.head.next     
            print(True)   
     
    def deletePosition(self, position):
        # o(n)
        len = self.length()
        
        if position > len or position <= 0:
            print(False)
            return
        
        if position == 1:
            self.deleteBegin()
            return
        if position == len:
            self.deleteEnd()
            return
        
        prev = None
        curr = self.head
        for i in range(position -1):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        print(True)    

    
    # Search Element
    
    def findElement(self, data):
        # o(n)
        if self.head is None:
            print(False)
            return
                    
        else :
            curr = self.head
            
            while curr :
                
                if curr.data == data:
                    print(True, curr.data)
                    return
                
                curr = curr.next
            
        print(False)
        
        
    def findElementByP(self, position):
        
        # o(n)
        
        len = self.length()
        
        if position > len or position <= 0:
            print("Out of index or Invalid index")
            return
        
        curr = self.head
        
        for i in range(position-1):
            
            curr = curr.next
            
        print(curr.data)
     
    # Reverse 
    
    def reverse(self):
        
        
        if self.head is None or self.head == self.tail:
            print(False)
            return
            
        else :
            
            curr = self.head
           
            prev = None 
            print("trest")

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                
        
        self.head = prev     
                
                     
        
    def traverse(self):
        curr = self.head
        
        while curr:
            
            print(curr.data, end="->")
            
            curr = curr.next
        
        print(None)    
        

    
    
    
node = SList()

node.insert(1)
node.insert(12)
node.insert(3)
node.insert(4)
node.insert(5)
node.insert(61)

# node.insertFirst(10)
# node.insertPosition(50, 3)

# node.deleteEnd()
# node.deleteBegin()
# node.deletePosition(6)
# node.deletePosition(3)

# node.findElement(15)
# node.findElementByP(2)

node.reverse()
node.traverse()