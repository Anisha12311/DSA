class Node : 
    def __init__(self, data):
        self.data = data
        self.next = None
        


class circular:
    def __init__(self):
        self.head = None
    
    
    def counting(self):
        count = 1
        curr = self.head
        if self.head is None:
            return 0
        while curr.next != self.head:
            curr = curr.next
            count+=1
        return count
    
    
        
    def insert(self, data):
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            new_node.next = self.head
        else : 
            
            curr = self.head
            
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node      
            new_node.next = self.head
            
    def insertStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            
        else :
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
                
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node
                
    def deleteLastNode(self):
        
        if self.head is None:
            print(False)
            return
        if self.head.next == self.head:
            print(True)

            self.head = None
            return
        curr = self.head
        
        while curr.next.next != self.head:
            curr = curr.next
            
        curr.next = self.head
      
    def deleteFirstNode(self):
        if self.head is None:
            return 
        
        
        if self.head.next == self.head:
            self.head = None
            return
        
        curr = self.head
        
        while curr.next != self.head:
            curr = curr.next
            
        curr.next = self.head.next
        self.head = self.head.next
            
                 
        
    def traverse(self):
        curr = self.head
        
        if self.head is None:
            return "Empty"
        while True:
            print(curr.data, end= " = ")
            curr = curr.next
            if curr == self.head:
                break
        
        print('Head')
        
cc = circular()

cc.insert(1)
cc.insert(2)

cc.insert(3)
cc.insert(14)

# print(cc.counting())

# cc.insertStart(34)
# cc.deleteLastNode()
cc.deleteFirstNode()
cc.traverse()