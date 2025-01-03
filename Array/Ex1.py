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