DIRECTIONS = {
    'up': (1, 0),
    'down': (-1, 0),
    'left': (0, 1),
    'right': (0, -1),
}


def add_tuples(tuple1, tuple2):
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def traverse(matrix):
    for i, iv in enumerate(matrix):
        for j, jv in enumerate(matrix[i]):
            cell = matrix[i][j]
            if cell != '0' and cell != 'X':
                print(cell, i, j)


T = int(input())

for _ in range(T):
    N, M = [int(i) for i in input().split()]
    matrix = [['C' for x in range(N)] for y in range(M)]

    X = int(input())
    for _ in range(X):
        row, column = [int(i) for i in input().split()]
        matrix[row - 1][column - 1] = '0'

    Y = int(input())
    for _ in range(Y):
        row, column = [int(i) for i in input().split()]
        matrix[row - 1][column - 1] = 'X'

    for row in matrix:
        print(row)

    traverse(matrix)
