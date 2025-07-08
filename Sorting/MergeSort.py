

def Merge(left, right):
    
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            print("right[j]", right[j])
            sorted_arr.append(right[j])
            j += 1
    
    sorted_arr.extend(left[i:]) 
    sorted_arr.extend(right[j:])  
    print("sort", sorted_arr) 
    return  sorted_arr   
    

def MergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    print("left", left, right)
    return Merge(left, right)
    


    
arr = [15, 5, 24, 8 ,1 ,3, 16, 10, 20]

print(MergeSort(arr))