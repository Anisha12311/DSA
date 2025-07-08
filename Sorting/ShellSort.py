import math
def ShellSort(arr):
    
    n = len(arr)
    gap = math.floor(n / 2)
    
    while gap >=1:
        
        for j in range(gap, n):
            
            for i in range(j-gap, -1, -gap):
                if arr[i+gap] > arr[i]:
                    break
                else:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
        gap = math.floor(gap/2)

        
    return arr
    
arr = [23, 29, 15,19 , 31, 7, 9, 5, 2]
print(ShellSort(arr))