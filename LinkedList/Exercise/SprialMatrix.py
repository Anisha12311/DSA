matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]

# output = [1,2,3,4,5,10,15,14,13,12,11,6,7,8,9,10]


def SpiralMatrix(matrix):
    top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
    result = []
    while top < bottom and left < right :
        print(right)
        for i in range(left, right):
            result.append(matrix[top][i])
            
        top +=1
        
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
            
        right -=1
        
        if not(top < bottom and left < right):
            break
        
        for i in range(right -1, left-1,-1):
            result.append(matrix[bottom-1][i])
            
        bottom -=1
        
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
           
        left +=1 
        
        
    print(result)
    
SpiralMatrix(matrix)