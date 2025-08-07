def bubble_sort(arr):
    n = len(arr)
    for _ in range(n-1):
        swapped = False
        for j in range(1,n):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if not swapped:
            break      
    return arr
arr = [10,4,43,5,57,91,45,9,7]

# print(bubble_sort(arr))


def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        key = arr[i]
        min = i
        for j in range(i, n):
            if arr[min] > arr[j]:
                min = j
        key, arr[min] = arr[min], key    
    return arr
# print(selection_sort(arr))

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        j  = i
        key = arr[i]
        while arr[j-1] > arr[j] and j>=1:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = key
    return arr 
    
# print(insertion_sort(arr))

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
            
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return arr
def merge_sort(arr):
    
    if len(arr) <=1:
        return arr
    n = len(arr)
    mid = n//2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
    
    
# print(merge_sort(arr))


def partition(arr, low, high):
    p = low
    
    i = low + 1
    j = high
    
    while i <= j:
        while i<=j and  arr[i] <= arr[p]:
            i += 1
        while arr[j] > arr[p]:
            j -= 1
        
       
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[p], arr[j] = arr[j], arr[p]
        
    return j
    
def quick_sort(arr, low, high):
    n = len(arr)
    
    if low < high :
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot -1)
        quick_sort(arr, pivot+1, high)
        
    return arr
arr = [10,4,43,5,57,91,45,9,7]

# print("Quick sort",quick_sort(arr,0, len(arr)-1))


def count_sort(arr):
    n = len(arr)
    count = [0] * (max(arr)+1)
    bucket = [0] * n
    for i in range(n):
        count[arr[i]] += 1 
    for j in range(1, len(count)):
        count[j] += count[j-1]
    for i in range(n-1 , -1, -1):
        count[arr[i]] -= 1
        bucket[count[arr[i]]] = arr[i]
    return bucket
    
    
arr1 =  [4, 3, 12, 1, 5, 5, 3, 9]
print(count_sort(arr1))


def bucket_sort(arr):
    n = len(arr)
    bucket = [[] for _ in range(n)]
    result = []
    for i in range(n):
        index = int(arr[i] * n)
        bucket[index].append(arr[i])
    
    for b in range(len(bucket)):
        bucket[b] = sorted(bucket[b])

    for b in bucket:
        result.extend(b)
    return result
arr2 = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

print(bucket_sort(arr2))