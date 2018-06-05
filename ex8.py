import random
def gen_matrix(n):
    matrix = []
    for i in range(n):
        line = []
            for j in range(n):
                line.append(random.randint(-10, 5))
            matrix.append()


def change_negatives(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                matrix[i][j] = 0

