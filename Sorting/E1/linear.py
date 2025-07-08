arr = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]

def count_sort(arr):
    bucket_size = max(arr) + 1
    count = [0] * bucket_size
    buckets = [0] * len(arr)
    for i in range(len(arr)):
        count[arr[i]] = count[arr[i]] + 1
      
    for i in range(1, len(count)):
        count[i] = count [i] + count[i-1]  
        
    for i in range( len(arr)-1,-1, -1):
        count[arr[i]] -= 1
        buckets[count[arr[i]]] = arr[i]
    return buckets

# print(count_sort(arr))


def bucket_sort(arr):
    num_buckets = 10
    bucket_range = (max(arr) - min(arr))/ num_buckets
    buckets = [[] for _ in range(num_buckets)]
    sorted_arr = []
    for num in arr:
        index = int((num - min(arr))/ bucket_range)
        if index == num_buckets:
            index -=1 
            
        buckets[index].append(num)
        
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])
        
    for bucket in buckets:
        sorted_arr.extend(bucket)
    return sorted_arr 
arr1 = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    
# print(bucket_sort(arr1))


def count_sort1(arr, exp):
    n = len(arr)
    count = [0] * 10
    output = [0] * n
    
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for i in reversed(range(n)):
        index = (arr[i] // exp) % 10
        count[index] -= 1
        output[count[index]] = arr[i]
    
    for i in range(n):
        arr[i] = output[i]
    
    
def radix_sort(arr):
    
    if not arr:
        return arr
    
    max_val = max(arr)
    
    exp = 1
    
    while max_val // exp > 0:
        count_sort1(arr, exp)
        exp *= 10
    return arr 
arr2 = [170, 45, 75, 90, 802, 24, 2, 66]

print(radix_sort(arr2))