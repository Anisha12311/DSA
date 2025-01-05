# Majority Element

arr_majority = [1, 1, 2, 1, 3, 5, 1]
arr_majority1 = [3, 3, 4, 2, 4, 4, 2, 4]



def majority_num(arr):
    map = {}
    count = 1
    for i in range(len(arr)):
        if arr[i] in map:
          map[arr[i]] = map[arr[i]] + 1
        else: 
            map[arr[i]] = count 
    freq = max(list(map.values()))
     
    if  len(arr)/2 < freq :
        return freq 
    else :
        return -1 
  
print("Majority Number ",  majority_num(arr_majority1))

# Majority Element II – Elements occurring more than ⌊N/3⌋ times

element = [2, 2, 3, 1, 3, 2, 1, 1]
ele1 = [3, 2, 2, 4, 1, 4]

def majority_el(arr):
    map = {}
    
    for i in range(len(arr)):
        if arr[i] in map:
            map[arr[i]] = map[arr[i]] + 1
        else:
            map[arr[i]] = 1
    result = [key for key, value in map.items() if value > len(arr)/3]
            
            
    return sorted(result)
    
print("majority 2 element ", majority_el(element))

# Stock Buy and Sell – Multiple Transaction Allowed


stock = [100, 180, 260, 310, 40, 535, 695]
stock1 = [4, 2, 2, 2, 4]
def stock_price(arr):
    sum = 0
    
    for i in range(1,len(arr)):
          
          if arr[i] > arr[i-1]:
              sum += arr[i] - arr[i-1]
        
    return sum   
        
print("stock_price ", stock_price(stock1))

# Minimize the Heights II

arr1 = [3, 9, 12, 16, 20]
arr2 = [1, 8, 10, 6, 4 ,6, 9, 1]

k2 = 7
def height(arr,k):
    new_arr = []
    for num in arr:
        if num <= k : 
                
            new_arr.append(abs(num+k))
        else:
            new_arr.append(abs(num-k))
            
    return max(new_arr) - min(new_arr)
        
print("Max Height ", height(arr2,k2))

# [8,1,3,13,11,13,2,8]

13-1