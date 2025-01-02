arr = [1,2,3,4,5]


# traverse
for i in arr:
    print(i)  # o(n)
    

[1,2,3,4,5]  
    
#Insertion

def array_insert(element, index):
    new_arr = [1,2,3,4,5]
    
    if index < 0 or index > len(new_arr):
        raise IndexError("Index is out of bounds")
    
    if element is None:
        raise IndexError("Element should be insert")
    
    new_arr.insert(index, element)
                
    return new_arr


print(array_insert('0',5))

def array_insert2(element, index):
    new_arr = [1,2,3,4,5]
    
    if index < 0 or index > len(new_arr)-1:
        return "Index is out of bound"
    result = []
    if element:
        for i in range(len(new_arr) + 1):
            if i < index:
               result.append(new_arr[i])  
            elif i == index:
                result.append(element)
            else:
                result.append(new_arr[i-1])           
    return result


print(array_insert2(23,4))
    
    
# Deletion

def array_delete(index):
    new_arr = [1,2,3,4,5]

    if index < 0 or index > len(new_arr):
        raise IndexError("Index is out of bounds")
    
    del new_arr[index]
    return new_arr


print(array_delete(3))


# Search


def array_search(index):
    new_arr = [1,2,3,4,5]

    if index < 0 or index > len(new_arr):
        raise IndexError("Index is out of bounds")
    
    return new_arr[index]


print("Search index",array_search(2))


def array_search(element):
    new_arr = [1,12,3,4,5]

    for i in range(len(new_arr)):
        if new_arr[i] == element:
            return i
        
    return -1


print("Search element",array_search(12))


# Update

def array_update(index , element):
    new_arr = [1,2,3,4,5]
    
    if index < 0 or index > len(new_arr)-1:
        return "Index is out of bound"  
    
    if element is None :
        raise IndexError("Element should be insert")
    
    for i in range(len(new_arr)):
        if i == index : 
            new_arr[i] = element
            
    return new_arr


print(array_update(3, 25))    




# Reverse arrays


arr1 =  [8,10,7,5,7,12,13,15]

print(arr1[::-1])

print(arr1[-2:])

print(arr1[6:1:-1])


# Find Max and Min element

arr2 =  [8,10,7,5,7,12,13,15]
    

print(min(arr2))


max_value = arr2[0]
min_value = arr2[0]

for num in range(len(arr2)):
    if max_value < arr2[num]:
        max_value = arr2[num]
        
    if min_value > arr2[num]:
        min_value = arr2[num]
        
print("Max", max_value)
print("Min", min_value)
