def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)
    
    return transposed


matrix_3x2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(transpose_matrix(matrix_3x2))

matrix_2x2 = [
    ['a', 'b'],
    ['c', 'd']
]
print(transpose_matrix(matrix_2x2))
