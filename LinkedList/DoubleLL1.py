class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        
        
class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count+=1
            curr = curr.next
            
        return count   
    # Insert Element
    
    def insert(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail        
            self.tail = new_node
            
    def insertBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node     
      
    def insertPosition(self, data, position) :
        len = self.length()
        new_node = Node(data)
        
        if position <=0 or position > len +1:
            print("Out of Index and invalid index")
            return
        
        if position ==1:
            self.insertBegin(data)
            return
        
        if position == len + 1:
            self.insert(data)
            return
        curr = self.head
        for _ in range(position-2):
            curr = curr.next

        print("Curr", curr.data)
        new_node.next = curr.next
        
        new_node.prev = curr
        
        if curr.next:
            curr.next.prev = new_node
            
        curr.next = new_node  
    
    # Delete Element
    
    def deleteEnd(self):
        # o(1)
        if self.head is None:
            print(False)
            return
        
        if self.head == self.tail:
            print(True)
            self.head = None
            self.tail = None
            
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            print(True)

    def deleteBegin(self):
        
        if self.head is None:
            print(False)
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None         
            print(True)    
        else :
            curr = self.head
            self.head = curr.next
            self.head.prev = None           
     
    def deletePosition(self, position):
        len = self.length() 
        if position > len + 1 or position <= 0:
            print("Out of index")
            return
        
        if position == 1:
            self.deleteBegin()
            return
        
        if position == len+1:
            self.deleteEnd()
            
        curr = self.head
        for _ in range(position -2):
            curr = curr.next
            
        print("curr", curr.data)
            
        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
    
    # Find Element
    
    def findElement(self, data):
        if self.head is None:
            print(False)
            return
        
        if self.head.data == data:
            print(True)
            return
        
        else : 
            curr = self.head
            while curr:
                if curr.data == data:
                    print(True)
                    return 
                curr = curr.next
                
        print(False)
    
    def findElementByP(self,position):
        
        len = self.length()
        
        if position > len+1 or position <= 0 :
            print(False)
            return
        curr = self.head
        for i in range(position-1):
            curr = curr.next
            
        print(curr.data)
        print(True)
            
    #  Reverse Element
    
    def reverse(self):
        if self.head is None or self.head == self.tail:
            print(False)
            return
                
        curr = self.head
        temp = None
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
            
        if temp:
            self.head = temp.prev  
        
    def traverse(self):
        
        curr = self.head         
        while curr:      
            print(curr.data, end=" <=> ")       
            curr = curr.next    
        print(None)
    
      
    
double = DoubleLL()

double.insert(1)
double.insert(2)
double.insert(3)
double.insert(4)
double.insert(15)
double.insert(26)

# double.insertBegin(45)
# double.insertPosition(33,4)

# double.deleteEnd()
# double.deleteBegin()
# double.deletePosition(6)

double.findElementByP(6)
double.reverse()

double.traverse()    
