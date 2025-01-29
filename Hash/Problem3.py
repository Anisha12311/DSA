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


# Given an array of n numbers, create an algorithm which displays all pairs whose sum is S.

arr = [2,4,5,1,7,8,3,3] 
s = 6

def find_pairs(arr,s):
    result = set()
    pairs = []

    for i in arr:
        second = s-i
        if second in result:
            pairs.append((i, second))          
        result.add(i)
    return pairs


print(find_pairs(arr,s))