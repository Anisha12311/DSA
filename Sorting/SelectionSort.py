def selection(arr):
    
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j]< arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [4.4, 3.3, 5.5, 7.7, 2.2, 1.1 , 6.6]
print(selection(arr))