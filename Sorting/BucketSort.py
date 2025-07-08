def bucket_sort(arr): 
    
    num_bucket = 10
    min_val = min(arr)
    max_val = max(arr)
    buckets = [[] for _ in range(num_bucket)]
    bucket_range = (max_val - min_val ) / num_bucket
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == num_bucket:
            index -= 1
            
        buckets[index].append(num)
    
    for i in range(num_bucket):
       buckets[i] = sorted(buckets[i]) 
        
    sorted_arr = []
    
    for bucket in buckets:
        sorted_arr.extend(bucket)
    print(sorted_arr)
    
    

arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
 
bucket_sort(arr)

