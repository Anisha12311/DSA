col_num = 3
row_num = 3

multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col] = row * col
        
print(multi_list)

row, col = (5,5)

two_arr = [[1] *col] *row

print(two_arr)

two_d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


flat_arr = [item for subitems in two_d_array for item in subitems]

print(flat_arr)


# write the python code to transpose the matrix 


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []
    
    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    rotation = [row[::-1] for row in transpose]
    return rotation


print(transpose_matrix(matrix))


# Diagonal Sum

def diagonal_sum(matrix):
    if not matrix or not isinstance(matrix, list):
        return []
    
    n = len(matrix)
    sum_diagonal = 0
    
    for i in range(n):
        sum_diagonal += matrix[i][i]
        
        sum_diagonal += matrix[i][n-i-1]
        
    if n%2!=0:
        
        sum_diagonal -=matrix[n//2][n//2]
            
    return sum_diagonal
        
    
    
print(diagonal_sum(matrix))

# Write a program to traverse a 2D array in a spiral order
matrix3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
def spiral_order(matrix):
    
    if not matrix or not matrix[0]:
        return []
    
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    
    result = []
    while top <= bottom and left <= right:
        for col in range(left, right+1):
            result.append(matrix[top][col])
        top+=1
        
        
        for row in range(top,bottom+1):
            result.append(matrix[row][right])
        right -=1
        
        
        if top<=bottom :
            
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
                
            bottom-=1
        
        if left <= right :
            for row in range(bottom ,top-1 ,-1):
                result.append(matrix[row][left])
                
            left += 1
    return result    
        
    
    
print("spiral",spiral_order(matrix3))