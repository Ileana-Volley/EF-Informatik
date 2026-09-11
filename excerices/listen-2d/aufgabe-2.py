#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [9, 9, 9], [1, 8, 7]]
#matrix = [[1, 2, 3, 4, 5],[4, 5, 6, 5, 4], [7, 8, 9, 9, 9], [9, 9, 9, 8, 7]]
matrix = [[1, 2], [4, 5], [6, 7], [8, 9], [10, 11]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f'[i: {i}, j: {j}] =', matrix[i][j])