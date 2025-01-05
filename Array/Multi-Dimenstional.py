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

