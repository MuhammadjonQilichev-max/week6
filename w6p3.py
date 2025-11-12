def sum_diagonals(matrix):
    n = len(matrix)
    total = 0
    
    for i in range(n):
        total += matrix[i][i]                   
        total += matrix[i][n - 1 - i]          
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]
    
    return total

matrix_4x4 = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(sum_diagonals(matrix_4x4))  


matrix_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum_diagonals(matrix_3x3))  

