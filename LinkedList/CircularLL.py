class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class CircularLL:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                
            temp.next = new_node
            new_node.next = self.head
    
    def insertAtBegin(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            
        else :
            temp = self.head
            
            while temp.next != self.head:
                temp = temp.next
                
            new_node.next = self.head
            temp.next = new_node
            
            self.head = new_node        
    
    def deleteAtBegin(self):
        if self.head is None:
            print("False")
            
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                
            temp.next = self.head.next
            self.head = temp.next
    
    def deleteAtEnd(self):
        if self.head is None:
            print("false")
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
                
            temp.next = self.head
    
    def search(self, data):
        if self.head is None:
            print("list is empty")
            
        else:
            temp = self.head
            while True:
                if temp.data == data:
                    print( f"Found data {temp.data}")
                    return
                temp = temp.next
                
                if temp == self.head:
                    break
            print("Not found")
    def traverse(self):
        
        if self.head is None:
            print("List is empty")
        temp = self.head    
        while True:
            print(f"[{temp.data} -> {temp.next.data if temp.data else None}]")
            temp = temp.next
            if temp == self.head:
                break
        print("Head")
        
        
circular = CircularLL()

circular.append(1)
circular.append(2)
circular.append(3)
circular.append(4)
circular.append(5)
circular.append(6)
circular.insertAtBegin(34)

circular.search(6)
# circular.deleteAtBegin()
# circular.deleteAtBegin()
# circular.deleteAtEnd()

circular.traverse()