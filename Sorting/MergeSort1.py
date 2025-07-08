arr = [38, 27, 43, 10]

def merge(arr, lb, mid, ub):
    i = lb
    j = mid + 1
    k = lb
    b = []
    
    while i <= mid and j <= ub:
        print("test")
        if arr[i] < arr[j]:
            b.append(arr[i])
            i+=1
        else:
            b.append(arr[j])
            j+=1
        k += 1
        
    if i > mid:
        while j<=ub:
            b.append(arr[j])
            j+=1 
            k+=1
    else:
        while i <= mid:
            b.append(arr[i])
            i += 1
            k += 1
    
    for i in range(len(b)):
        arr[lb+ i] = b[i]

def merge_sort(arr, left, right):
    if left < right : 
        mid =  (left+right)//2
        print(mid, left, right)
        merge_sort(arr, left , mid)
        merge_sort(arr, mid+1 , right)
        merge(arr, left, mid, right)
    return arr
left = 0
right = len(arr)-1  
print(merge_sort(arr, left, right))