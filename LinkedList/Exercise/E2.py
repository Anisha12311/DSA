import math
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
    
    def sortInsert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        if data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            
        
        curr = self.head
        
        
        while curr.next and curr.next.data < data:
            curr = curr.next
            
        new_node.next = curr.next
        curr.next = new_node
        
        
    def traverse(self):
        curr = self.head
        
        while curr:
            
            print(curr.data, end="->")
            
            curr = curr.next
        
        print(None)    
    
    def  middleElement(self):
        
        len = self.length()
        if self.head is None:
            return
        position = math.ceil(len/2) 
        
        print("position", position) 
        curr = self.head
        for _ in range(position-1):
            curr = curr.next
        print(curr.data)
        
    def lengthEven(self):
        len = self.length() 
        if len%2 == 0:
            print("Even")
            return
        else :
            print("Odd")
            return
     
    def reversePair(self):
        
        if not self.head and not self.head.next:
            return
        curr = self.head
        temp1 = None
        temp2 = None
        
        
        while curr and curr.next:
            
            if temp1:
                temp1.next.next = curr.next
                
            temp1 = curr.next
            curr.next = curr.next.next
            temp1.next = curr
            
            if temp2 == None : 
                temp2 = temp1
                
            curr = curr.next
        self.head = temp2               
    def kthNode(self,temp, k):
        count = 0
        while temp and count < k - 1:
            temp = temp.next
            count += 1
        return temp if temp else None   
    def reverse(self, temp):
        
        prev = None
        
        while temp:
            
            next_node = temp.next
            temp.next  = prev
            prev = temp
            temp = next_node
        return prev    
        
    def reverseKthNode(self,k):
        temp = self.head
        new_head = None
        prev_tail = None
        
        len = self.length()
        
        if len < k : 
            return
        while temp:
            
            kth_node =   self.kthNode(temp, k)
            if kth_node is None : 
                prev_tail.next = next_node
                break
            print("K node", kth_node.data)

            next_node = kth_node.next
            kth_node.next = None
            
            new_head = self.reverse(temp)
            
            if temp == self.head:
                self.head = kth_node
                
            else : 
                prev_tail.next = kth_node
            
            prev_tail = temp
            temp = next_node            
            
        new_head
        
    def evenBegin(self):
        
        even_head = even_tail = None
        odd_head = odd_tail = None
        
        current = self.head
        
        while current:
            
            if current.data %2 == 0 :
                if even_head is None:
                    even_head = even_tail = current
                    
                else:
                    even_tail.next = current
                    even_tail = current
                    
            else:
                if odd_head is None:
                    odd_head = odd_tail = current
                    
                else:
                    odd_tail.next = current
                    odd_tail = current
                    
            current = current.next
            
            
        if even_head is None:
            self.head = odd_head
            return
            
        if odd_head is None:
            self.head = even_head
            return
            
            
        even_tail.next = odd_head
        odd_tail.next = None
        
        self.head = even_head
  
  
    def fractionalNode(self,k):
        
        len = self.length()
        
        position = math.ceil(len/k)
        
        print(position)
        current = self.head
        for _ in range(position-1):
            
            current = current.next
            
        print(current.data)
            

node = SList()

node.insert(1)
node.insert(2)
node.insert(3)
node.insert(14)
node.insert(5)
node.insert(6)


node.insert(7)




# node.sortInsert(7)
# node.sortInsert(-1)

# node.middleElement()

# node.lengthEven()
# node.reverseKthNode(9)

# node.evenBegin()

node.fractionalNode(2)

node.traverse()