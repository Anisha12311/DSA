class Node : 
    def __init__(self, data):
        self.data = data
        self.next = None
        


class circular:
    def __init__(self):
        self.head = None
    
        
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
            
    
    def josephus_circle(self, k):
        current = self.head
        while current.next != current:  # Only one node remains
            for _ in range(k - 1):  # Move k-1 steps forward
                prev = current
                current = current.next
            # Remove the k-th node
            prev.next = current.next
            print(f"Eliminated: {current.data}")
            current = current.next  # Move to the next node
        self.head = current  # The last remaining node
        print("head", current.data)
        return current.data  # Survivor
  
                    
    
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
cc.insert(4)
cc.insert(5)
cc.insert(6)

cc.josephus_circle(2)

cc.traverse()