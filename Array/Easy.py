# https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/

# https://leetcode.com/problems/two-sum/description/

num = [2,7,11,12]
target = 9

def two_sum(num, target):
    map = {}
    
    for i in range(len(num)):
        sec_value = target - num[i]
        
        if sec_value in map:
            return [i, map[sec_value]]
            
        
        map[num[i]] = i
       
print(two_sum(num, target))



# https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-03

nums = [10,4,-8,7]

def number_split(nums):
    total_sum = sum(nums)
    valid_split = 0
    left_sum = 0

    for i in range(len(nums)-1):
        left_sum += nums[i]
        right_sum = total_sum-left_sum
        
        if left_sum >= right_sum:
            valid_split += 1
            
    return valid_split

        
print(number_split(nums))


# Second Largest Element in an Array

nums1 = [10,4,12,7]
# sort_num = sorted(nums)
# print(sort_num[-2])


def largest_s_element(nums):
    
    if len(nums)<2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for i in nums:
        
        if largest < i : 
            second_largest = largest
            largest = i
        elif second_largest < i and i != largest:
            second_largest = i
            
    return second_largest if second_largest!= float('-inf')  else None
        
            
                

print(largest_s_element(nums1))

# Third Largest Element in an Array


def largest_t_element(nums):
    if len(nums) < 3:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    third_largest = float('-inf')
    
    for num in nums:
        
        if largest < num:
            third_largest = second_largest
            second_largest  = largest
            largest = num
            
        elif second_largest < num and num != largest:
            third_largest = second_largest
            second_largest = num
            
        elif third_largest < num and num != largest and num != second_largest:
            third_largest = num
            
    return third_largest


print("Third",largest_t_element(nums1))


# Maximum product of a triplet (subsequence of size 3) in array
arr = [1, -4, 3, -6, 7, 0]
def max_product(arr):
    if len(arr) < 3:
        return -1
    num = sorted(arr)
    max1 = num[-1] * num[-2] * num[-3]
    max2 = num[0] * num[1] * num[-1]
    
    max_product1 = max(max1, max2)    
    return max_product1


print("Max Product ", max_product(arr))
    
    
# Maximum consecutive one’s (or zeros) in a binary array

arr_ones  = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
arr_ones2 = [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

def max_ones(nums):
    
    ones = 0
    
    
    for num in nums:
        
        if num == 1:
            ones += 1
        else: 
            ones = 0
            
    return ones 

print("Ones ", max_ones(arr_ones2))
        
        
# Move all zeros to end of array

zeros = [10, 20, 30]
zeros1 = [1, 2, 0, 4, 3, 0, 5, 0]
zeros2 = [0, 0]

def move_zeros(zeros):
    
    non_zeros = []
    with_zeros = []
    
    if 0 in zeros:
        for num in zeros:
            if num != 0:
                non_zeros.append(num)
                
            elif num == 0:
                with_zeros.append(num)
    
        return non_zeros + with_zeros
    
    return zeros

    
print("Zeros : ",move_zeros(zeros2))


# Reverse an Array in groups of given size (Reverse three three group)

arr_reverse = [1, 2, 3, 4, 5, 6, 7, 8]
arr_reverse1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K = 5 
K1 = 3

def reverse_arr(arr,k):
    
    if k > len(arr):
        return arr[::-1]
    total = 0
    result = []
    while total < len(arr):
        first = arr[total:total+k]
       
        result.extend(first[::-1])
        total += k
    return result
    
    
print("Reverse array", reverse_arr(arr_reverse, K))
    
# Rotate an Array by d – Counterclockwise or Left


arr_rotate = [1, 2, 3, 4, 5, 6]
arr_rotate1 = [1, 2, 3]
d = 2
d1 = 4

def rotate_arr(arr,d):
    result = []
    d = d % len(arr)
    print(d)
    
    first = arr[:d]
    second = arr[d:]
    result  = second + first
    
    return result

print("Rotate arr", rotate_arr(arr_rotate, d))