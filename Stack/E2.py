# Next Greater Element (NGE) for every element in given Array


arr = [1, 3, 2, 4]

def greater_element(arr):
    n = len(arr)
    result = [-1] *n
    
    for i in range(n):
        
        for j in range(i+1, n):
            if arr[j]> arr[i]:
                result[i] = arr[j]
                break
            
    return result

print(greater_element(arr))


#Nearest smaller numbers on left side in an array


arr1 = [1, 6, 4, 10, 2, 5]

def smaller_number(arr):
    n = len(arr)
    result = [] 
    
    for i in range(n):
        found = False
        for j in range(i-1,-1, -1):
            if arr[j]< arr[i]:
                found = True
                result.append(arr[j])
                break
        if not found:
            result.append("_")            
    return result

print(smaller_number(arr1))