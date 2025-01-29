# Given two arrays of unordered numbers, check whether both arrays have the same set of numbers?

A = [2,5,6,8,10,5,5]
B = [2,5,5,8,10,5,6]



def frequency(A, B):
    
    fre_A = {}
    
    for i in A:
        
        if i in fre_A:
            fre_A[i] += 1
            
        else :
            fre_A[i] = 1
    
    
    for j in B:
        
        if j in fre_A:
            fre_A[j] -=1
            
    
    all_zeros = set(fre_A.values()) == {0}
            
    return all_zeros


    
    
    
print(frequency(A, B))


pairs = [(1, 3), (2, 6), (3, 5), (7, 4), (5, 3), (8, 7)]


def symmetric_pair(pair):
    
    table = {}
    result = []
    for key, value in pair:
        
        if value in table and table[value] == key :
            print("yes")
            result.append((value, key))
        else :
            table[key] = value
        
        
    
    return result 

print(symmetric_pair(pairs))



# Given m sets of integers that have n elements in them, provide an algorithm to
# find an element which appeared in the maximum number of sets?

sets = [
    {1, 2, 4},
    {4, 4, 5},
    {2, 4, 7},
    {8, 2, 4}
]

def feq_count(sets):
    
    table = {}
    
    for elements in sets:
        
        for s in elements:
            
            if s in table:
                table[s]  = table[s]+1
                
            else:
                table[s] = 1
    
    max_count = 0
    element_max = 0
    
    for element, count in table.items():
        
        if max_count < count:
            max_count = count
            element_max = element
            
        
                
    return element_max
        
    
    
print(feq_count(sets))


# Given two sets A and B, and a number K, Give an algorithm for finding whether there exists a pair of elements, one from A and one from B, that add up to K. 


A_set = [1,4,6]
B_set = [2,3,7]
k = 9

def set_pairs(A_set, B_set, k):
    
    for A in A_set:
        second = k-A
        
        if second in B_set:
            return f"AB = {A} + {second} = {k}"
    return False
    
print(set_pairs(A_set, B_set, k))


# Give an algorithm to remove the specified characters from a given string which are given in another string?


str1 = 'anisha'
sub_str = 'itsh'


def remove_char(str1, sub_str):
    if sub_str in str1:
        return str1.replace(sub_str, '')

print(remove_char(str1, sub_str))


str2 = 'anisha'
sub_str1 = 'itsh'


def remove_char1(str1, sub_str):
    
    str2_split = list(str2)
    sub_str_split = list(sub_str)
    
    for i in sub_str_split:
        
        if i in str2_split : 
            str2_split.remove(i)

    return str2_split
    
print(remove_char1(str1, sub_str))


# Give an algorithm for finding the first non-repeated character in a string. For example, the first non-repeated character in the string “abzddab” is ‘z’

char = 'abzzzddabtn'

def non_repeat(char):
    char_set = {}
    
    for ch in char:
        
        if ch in char_set:
            char_set[ch] += 1
        else :
            char_set[ch] = 1
        
    for key in char_set:        
        if char_set[key] == 1:
            return key
        
    
    return "False"
        
    
    

print(non_repeat(char))


#Given an array of n numbers, create an algorithm which displays all pairs whose sum is S.


