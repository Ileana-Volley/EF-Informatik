print('[')
def pretty_print(mat2d):
    for zeile in mat2d:
        print(f'{zeile},')


pretty_print([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pretty_print([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6]])
print(']')