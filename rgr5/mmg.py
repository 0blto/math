def cool_printer(matrix):
    for i in range(len(matrix)):
        print('|', end=' ')
        for j in range(len(matrix[0])):
            print('{:>3f}'.format(matrix[i][j]), end=' ')
        print('|')
    print('')

def time_to_exit():
    input('Press any key to exit')
    exit(0)

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
    determinant = 0

    for i in range(len(matrix)):
        determinant += pow(-1, i + 2) * matrix[0][i] * determine(alg_dop(matrix, 0, i))
    return determinant


def solve(matrix):
    n = len(matrix)

    determinant = determine([matrix[i][:n] for i in range(n)])

    if determinant == 0:
        return None

    for i in range(n - 1):
        max_i = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_i][i]):
                max_i = j
        
        if max_i != i:
            for j in range(n + 1):
                matrix[i][j], matrix[max_i][j] = matrix[max_i][j], matrix[i][j]

        for j in range(i + 1, n):
            div = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= div * matrix[i][k]

    answers = [0] * n

    for i in range(n-1, -1, -1):
        static = 0
        for j in range(i+1, n):
            static += answers[j] * matrix[i][j]
        answers[i] = (matrix[i][n] - static) / matrix[i][i]
    return matrix, answers

#your matrix
a = [
    [3, -2, -3, 0],
    [2, -3, -4, 3],
    [1, 5, 3, 1]
]

result_matrix, answer = solve(a)
if answer is None:
    print("Матрица несовместна.")
    time_to_exit()

print('Преобразованная матрица')
cool_printer(result_matrix)

print("Неизвестные:")
for i in answer:
    print('   {:>3f}'.format(i))
print('')

time_to_exit()




