arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 8

def binarySearch(arr, target):
    low = 0
    high = len(arr) -1
    
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == target:
            return 1
        
        elif arr[mid] < target:
            low = mid + 1
        else : 
            high = mid -1
            
    return -1
            

print(binarySearch(arr,target))


arr = [1,2,3,2,4,6,7]

def duplicate(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return True
        
    return False
print(duplicate(arr))


def alternative_dup(arr):
    hash_map = {}
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1   
        else : 
            hash_map[arr[i]] = 0    
    for val in hash_map.values():
        if val >= 1:
            return True
    return False    
print(alternative_dup(arr))


arr1 = [4,4,4,3,6,3,6,2,6,2,1,4]

def max_element(arr):
    hash_map = {}
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else : 
            hash_map[arr[i]] = 0
    sorted_dict = sorted(hash_map.items(), key = lambda item : item[1])
    return sorted_dict[-1][0]

print(max_element(arr1))

def max_element2(arr):
    max_val = 0
    max_index = float('-inf')
    n = len(arr)
    for i in range(n):
        arr[arr[i] % n] += n
    for i in range(n):
        if arr[i]/n > max_val:
            max_val = arr[i]/n
            max_index = i
    return max_index
    
print(max_element2(arr1))


def number_occuring(arr3):
    result = 0
    for num in arr3:
        result ^= num
    return result
arr3 = [1,2,3,2,3,1,1]
print(number_occuring(arr3))


def repeat_num(nums):
    result = []
    for i in range(len(nums)):
        print(nums)
        if nums[abs(nums[i])] > 0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
        else : 
            result.append(abs(nums[i]))
    return result
nums = [4,2,4,5,2,3,1]
print(repeat_num(nums))