def count_sort(arr):
    n = len(arr)
    k= max(arr) + 1
    count = [0] * k
    b = [0] * n
    for i in range(n):
        count[arr[i]] += 1
    
    for j in range(1, len(count)):
        count[j] = count[j] + count[j-1]
        
    for i in range(n -1, -1, -1):
        count[arr[i]] -= 1
        b[count[arr[i]]] = arr[i]
    print(count)
    return b
        

    
arr = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
print(count_sort(arr))