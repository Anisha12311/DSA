
def bubble_sort(arr):
   
    for _ in range(len(arr)-1):
        swapped = False
        for j in range(1, len(arr)):
            if arr[j] < arr[j-1] :
                swapped = True
                arr[j], arr[j-1] = arr[j-1], arr[j]    

        if not swapped :
            break
    return arr
arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]
print(bubble_sort(arr))

def selection_sort(arr):
    
    for i in range(len(arr)-1):
        key = arr[i]
        min = key
        for j in range(len(arr)):
            if min > arr[j]:
                min = arr[j]
        key, min = min, key
        
    return arr

print(selection_sort(arr))


def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]        
        j = i
        
        while arr[j] < arr[j-1] and j >= 1:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key

    return arr

# print(insertion_sort(arr))

def partition(arr,lb, ub):
    p = lb
    left = lb
    right = ub
    while left < right:
        
        while arr[left]< arr[p] and left < right:
            left += 1
            
        while arr[right] > arr[p] and left < right:
            right -= 1
          
        if left < right:
              arr[left], arr[right] = arr[right], arr[left]
              
    
    arr[right], arr[p] = arr[p], arr[right]
        
    return right

def quick_sort(arr, lb, ub):
    if len(arr)<=1:
        return arr
    
    if lb < ub:
        loc = partition(arr, lb, ub)
        quick_sort(arr, lb, loc-1)
        quick_sort(arr, loc +1, ub)
        
    
print(quick_sort(arr, 0, len(arr)-1))