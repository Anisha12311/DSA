# To create a hashtable of given size, say n, we allocate an array of n/L (whose value is
# usually between 5 and 20) pointers to list, initialized to NULL. To perform Search/Insert/Delete
# operations, we first compute the index of the table from the given key by using hashfunction and
# then do the corresponding operation in the linear list maintained at that location. To get uniform
# distribution of keys over a hashtable, maintain table size as the prime number.


# Implement a separate chaining collision resolution technique. Also, discuss time
# complexities of each function.



class ListNode: 
    def __init__(self, key, data ):
        self.key = key
        self.data = data
        self.next = None
        
class HashTableNode:
    def __init__(self):
        self.bcount = 0
        self.next = None
        

class HashTable:
    Load_factor = 20
    def __init__(self, size):
        self.tsize = size // self.Load_factor
        self.table = [HashTableNode() for _ in range(self.tsize)]
        self.count = 0
    
    def hash_function(self, data):
        return data % self.tsize    
    
    def hash_search(self, data):
        index = self.hash_function(data)
        
        temp = self.table[index].next
        
        while temp:
            
            if temp.data == data:
                return True

            temp = temp.next
        
        return False
        
        
        
    
    def hash_insert(self, data):
        if self.hash_search(data):
            return False
        
        index = self.hash_function(data)
                
        new_node = ListNode(index, data)    
        
        if not new_node:
            print("Out of index")
            return -1
        
        new_node.next = self.table[index].next
        self.table[index].next = new_node
        self.table[index].bcount += 1
        self.count +=1
        
        if self.count / self.tsize > self.Load_factor :
            self.rehash()
            
        return True
        
                
            
    
    def hash_delete(self, data):
        
        index = self.hash_function(data)
        temp = self.table[index].next
        prev = None
        while temp:
            if temp.data == data:
                if prev:
                    prev.next = temp.next
                    
                else:
                    self.table[index].next = temp.next
                    
            prev = temp
            
            temp = temp.next
        
        
        
    def rehash(self):
        old_size = self.tsize
        old_table = self.table
        
        self.tsize = self.tsize * 2
        self.table = [HashTableNode() for _ in range(self.tsize)]
        
        
        for i in range(old_size):
            temp = old_table[i].next
            while temp:
                
                temp2 = temp
                index = self.hash_function(temp2.data)
                
                temp2.next = self.table[index].next
                self.table[index].next = temp2
    
    def iterate_table(self):
        result = []
        
        for i in range(self.tsize):
            bucket = []
            
            temp = self.table[i].next
            
            while temp : 
                
                bucket.append(temp.data)
                temp = temp.next
                
            result.append((i, bucket))
            
        return result            
            
        
        
if __name__ == '__main__':
    
    h = HashTable(100)
    
    h.hash_insert(10)
    h.hash_insert(20)
    h.hash_insert(30)
    h.hash_insert(33)

    h.hash_insert(56)

    print(h.hash_search(10))
    h.hash_delete(33)
    print(h.hash_search(33))


    
    
    for index, bucket_data in h.iterate_table():
        print(f"Index {index} : {bucket_data}")
    
