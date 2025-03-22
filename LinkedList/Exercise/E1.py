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


class NodeS :
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class SList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        newNode = NodeS(data)
        # o(1)
        if self.head == None:
            self.head = newNode
            self.tail = newNode

            
        else:
            self.tail.next = newNode
            self.tail = newNode
  
        
def mergeList(ss, cc):
    
    if ss.head is None:
        return cc.head
    
    if cc.head is None:
        return ss.head
    
    curr = ss.head
    
    while curr.next:
        curr = curr.next
        
    curr.next = cc.head
    
    return ss.head
    

def isCircular(head):
    if head is None:
        return False
    curr = head
    
    while curr.next:
        curr = curr.next
        if curr == head:
            return True
        
    return False
    
ss = SList()
ss.insert(1)
ss.insert(2)
ss.insert(3)

print(isCircular(ss.head))
      
cc = circular()
cc.insert(4)
cc.insert(5)
cc.insert(6)

print(isCircular(cc.head))
sl = mergeList(ss,cc)
print(isCircular(sl.head))

curr = ss.head

for _ in range(10):
    print(curr.data, end= '-> ' )
    
    curr = curr.next

