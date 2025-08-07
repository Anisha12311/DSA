
def partition(arr, lb, ub):
    pivot = lb
    start = lb
    end = ub
    
    while start < end:
        while start <= end and  arr[start] <= arr[pivot]:
            start += 1
        while arr[end] > arr[pivot]:
            end -= 1
    
        print("end", end, start)
        if start < end: 
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot] = arr[pivot], arr[end]
    return end

def quick_sort(arr, lb, ub):
    
    if lb < ub:
        loc = partition(arr, lb, ub)
        quick_sort(arr, lb, loc-1)
        quick_sort(arr, loc+1, ub)    
    
    return arr       
        

arr = [7,6,10,5,9,2,1,15,7]

print(quick_sort(arr, 0, len(arr)-1))