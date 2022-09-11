def alg_dop(matrix, del_row, del_col):
    new_matrix = [
        row[:del_col] + row[del_col + 1:]
        for row in matrix[:del_row] + matrix[del_row + 1:]
    ]
    return new_matrix


def determine(matrix):
    if len(matrix) != len(matrix[0]):
        print('Матрица должна быть квадратной')
        return

    if len(matrix) == 1:
        return matrix[0][0]


    det = 0

    for i in range(len(matrix)):
        det += pow(-1, i + 2) * matrix[0][i] * determine(alg_dop(matrix, 0, i))
    return det



mtrx = [
    [0, 3, -1, 1],
    [1, 2, 0, 0],
    [0, 4, 3, 5],
    [2, -1, -4, -2]
]

print(determine(mtrx))


