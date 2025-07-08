def InsertionSort(arr):
    
    for i in range(1,len(arr)):
        temp = arr[i]
        
        j = i-1
        
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j = j-1
            
        print(j,temp )
        arr[j+1] = temp
    
    return arr
    
arr = [5,4,10,1,6,2]

print(InsertionSort(arr))
