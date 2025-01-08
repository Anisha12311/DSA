class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        


class DoubleLL:
    def __init__(self):
        self.head = None
    
    def ListLength(self):
        length = 0
        temp = self.head
        
        while temp:
            temp = temp.next
            length += 1
        return length
    
    def append(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            temp = self.tail
            temp.next = new_node
            new_node.prev = temp
            self.tail = new_node
    
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail =  new_node
            
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node           
    
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def insertAtPosition(self,data, position):
        new_node = Node(data)
        length = self.ListLength()
        print(length)
        if position < 0 or position > length:
            return
        
        if position == 0:
            self.insertAtBegin(data)
        else:
            temp = self.head
            for _ in range(position-1):
                temp = temp.next
                
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node
    
    def search(self, data):
        
        if self.head is None:
            return 
        
        temp = self.head
        
        while temp:
            if temp.data == data:
                print("found data", temp.data)
                return 
            
            temp = temp.next
        print("not found")    
        
    def traverse(self):
        temp = self.head
        while temp :
            print(temp.data ,end= "<-> ")
            temp = temp.next
        print('None')    
    
double = DoubleLL()

double.append(1)
double.append(2)                     
double.append(3)           
double.append(4)           
double.append(5)

# double.insertAtBegin(34)
# double.insertAtBegin(35)

# double.insertAtEnd(55)
# double.insertAtEnd(51)

# double.insertAtPosition(34,1)
double.search(3)
double.traverse()           
