def elem(row, col):
    summ = 0
    for i in range(len(row)):
        summ += row[i] * col[i]
    return summ


def multiply_m(matrix1, matrix2):
    trans_matrix2 = [[0 for j in range(len(matrix2))] for i in range(len(matrix2[0]))]

    if len(matrix1[0]) != len(trans_matrix2[0]):
        print('Умножение невозможно')
        return

    result_matrix = [[0 for j in range(len(trans_matrix2))] for i in range(len(matrix1))]

    for i in range(len(matrix2)):
        for j in range(len(matrix2[0])):
            trans_matrix2[j][i] = matrix2[i][j]
    for i in range(len(matrix1)):
        for j in range(len(trans_matrix2)):
            result_matrix[i][j] = elem(matrix1[i], trans_matrix2[j])
    print_m(result_matrix)


def print_m(matrix):
    for i in range(len(matrix)):
        print('|', end=' ')
        for j in range(len(matrix[0])):
            print('{:>3d}'.format(matrix[i][j]), end=' ')
        print('|')
    print('')


print(106)
mtrx1 = [
    [-2, 1],
    [3, 4]
]
mtrx2 = [
    [-1, 3],
    [-2, 1]
]
multiply_m(mtrx1, mtrx2)

print(107)
mtrx1 = [
    [2, 1],
    [3, 2]
]
mtrx2 = [
    [1, -1],
    [1, 1]
]
multiply_m(mtrx1, mtrx2)

print(108)
mtrx1 = [
    [3, 5],
    [6, -1]
]
mtrx2 = [
    [2, 1],
    [-3, 2]
]
multiply_m(mtrx1, mtrx2)

print(109)
mtrx1 = [
    [-2, 3],
    [-5, -6]
]
mtrx2 = [
    [5, 2],
    [4, -7]
]
multiply_m(mtrx1, mtrx2)

print(110)
mtrx1 = [
    [-1, 7, 2],
    [4, 2, -3],
    [11, -6, 3]
]
mtrx2 = [
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
]
multiply_m(mtrx1, mtrx2)

print(111)
mtrx1 = [
    [-2, 1, -7],
    [3, 2, 2],
    [-4, 5, 1]
]
mtrx2 = [
    [3],
    [-1],
    [-2]
]
multiply_m(mtrx1, mtrx2)

print(112)
mtrx1 = [
    [1, 0, -3],
    [0, 2, -1],
    [4, -3, 2]
]
mtrx2 = [
    [5, -2, 0],
    [0 ,4, -3],
    [-3, 2, 0]
]
multiply_m(mtrx1, mtrx2)

print(113)
mtrx1 = [
    [2, 3, 4],
    [1, 2, 3],
    [-1, 0, 2]
]
mtrx2 = [
    [4, -3, 2],
    [-3, 2, 3],
    [1, -3, 2]
]
multiply_m(mtrx1, mtrx2)

print(114)
mtrx1 = [
    [1, -4, -2],

]
mtrx2 = [
    [2],
    [0],
    [3]
]
multiply_m(mtrx1, mtrx2)

print(115)
mtrx1 = [
    [-2],
    [3],
    [1]
]
mtrx2 = [
    [4, -1, 3]
]
multiply_m(mtrx1, mtrx2)

print(116)
mtrx1 = [
    [2, -3, 0, 4],
    [-4, 0, 2, 1]
]
mtrx2 = [
    [-1, 0],
    [0, -1],
    [3, 4],
    [-2, -1]
]
multiply_m(mtrx1, mtrx2)




