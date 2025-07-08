def bubble(arr):
   
    for i in range(len(arr)-1):
        swap = False
        print("Main")
        for j in range(len(arr)-1-i):
            print("test")
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
               swap = True
        if not swap :
            break

    return arr

    
arr = [1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6]
print(bubble(arr))