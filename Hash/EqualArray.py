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

