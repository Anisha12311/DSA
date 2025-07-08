arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]


def bubble(arr):
    swapped = 1
    if swapped : 
        for step in range(len(arr)):
            swapped = 0
            for i in range(len(arr)- step-1):
                print(step, i)
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1] , arr[i]
                    swapped = 1
            
# print(bubble(arr))


def selection(arr):
    for step in range(len(arr)):
        min = step
        for i in range(step+1, len(arr)):
            if arr[i] < arr[min]:
                min = i
                
        arr[step], arr[min] = arr[min] , arr[step]
    return arr           
# print(selection(arr))

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while key < arr[j-1] and j >=1 :
            arr[j] = arr[j-1]   
            j -=1
            
        arr[j] = key
    return arr
        
    
# print(insertion(arr))

def merge(lb, ub):
    i = j = 0
    sorted_arr = []
    print(lb, len(lb))
    while i < len(lb) and j < len(ub):
        if lb[i] < ub[j]:
            sorted_arr.append(lb[i])
            i+= 1
        else:
            sorted_arr.append(ub[j])
            j += 1

    sorted_arr.extend(lb[i:])
    sorted_arr.extend(ub[j:])
    
    return sorted_arr
    
    
def merge_sort(arr):
    
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
        
    return merge(left, right)
        
    
    
# print(merge_sort(arr))

def partition(arr,lb, ub):
    p = lb
    left = lb + 1
    right = ub
    while left < right:
        
        while left <= right and arr[left]< arr[p]  :
            left += 1
            
        while left <= right and arr[right] > arr[p] :
            right -= 1
          
        if left < right:
              arr[left], arr[right] = arr[right], arr[left]
              
    
    arr[right], arr[p] = arr[p], arr[right]
        
    return right

def quick_sort(arr, lb, ub):

    if lb < ub:
        loc = partition(arr, lb, ub)
        quick_sort(arr, lb, loc-1)
        quick_sort(arr, loc +1, ub)
    return arr  
    
print(quick_sort(arr, 0, len(arr)-1))