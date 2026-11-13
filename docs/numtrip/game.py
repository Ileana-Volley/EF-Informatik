print('[')
def spielfeld(mat2d):
    for zeile in mat2d:
        print(f'  {zeile}')



spielfeld([[4, 2, 2, 2, 2], [4, 8, 8, 2, 4], [2, 2, 8, 8, 8], [8, 8, 2, 8, 2], [4, 16, 16, 8, 4]])
print(']')

for y in range(len(mat2d)):
    for x in range(len(mat2d)):
        print(mat2d [x],[y])