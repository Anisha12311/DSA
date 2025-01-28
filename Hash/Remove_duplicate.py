char_array = ['a', 'b', 'c', 'a', 'b', 'd']


def remove_duplicate(arr):
    
    result = []
    
    new_set = set()
    
    for char in arr:
        if char not in new_set:
            new_set.add(char)
            result.append(char)
            
    return result


print(remove_duplicate(char_array))



def remove_duplicate1(arr):
        
    new_set = set()
    
    n = len(arr)

    i = 0
    
    while i < n:
        
        if arr[i] not in new_set:
            new_set.add(arr[i])
            i += 1
            
        else : 
            arr[i] = arr[n-1]
            n -=1
            
    return arr[:n]

print(remove_duplicate1(char_array))