class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
             
        else:      
            self.tail.next = new_node
            self.tail = new_node
    
    
    def insertBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def listLength(self):
        length = 0
        temp = self.head
        while temp:
            temp = temp.next
            length +=1
        return length
    
    def insertAtPosition(self,position,data):
        length = self.listLength()
        new_node = Node(data)
        
        if position > length or position < 0:
            return False
        
        if position == 0:
            self.insertBegin(data)
            return
        
        
        
        temp = self.head
        
        for _ in range(position-1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        
        if position == length:
            self.tail = new_node
           
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def update(self,data,index):
        length = self.listLength()
        if index < 0 or  index > length-1:
            return False
        
        if index == 0 :
            self.head.data = data
        temp = self.head    
        if index > 0:
            for _ in range(index):
                temp = temp.next               
            
            if temp:
            
                temp.data = data
    
    def deleteFirst(self):
        if self.head :
            self.head = self.head.next
            
        else : 
            print('false')
    
    def deletePosition(self, data, position):
        length = self.listLength()
        
        
    
    def removeLast(self):
        
        if self.head is None:
            return 
        else :
            temp = self.head
            
            while temp.next.next:
                temp = temp.next
            temp.next = None
    def deletePosition(self, position):
        length = self.listLength()
        if position > length-1 or position<0 :
            return 
        if position == 0 :
            self.head = None
            self.tail = None
            
        else : 
                temp = self.head
                for _ in range(position-2):
                    temp = temp.next
                if temp.next and temp.next.next:
                        
                    temp.next = temp.next.next
                
        
                     
    def traverse(self):
        temp = self.head
        
        while temp:
            print(temp.data, end= "-> ")
            temp = temp.next

        print(None)
    
        
        
list =  LinkedList()

list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
# list.removeLast()
# list.insertBegin(0)
# list.insertBegin(-1)
# list.insertAtPosition(4,11)
# list.insertAtPosition(2,12)
# list.insertAtEnd(32)
# list.update(23,4)

list.deletePosition(4)

list.traverse()