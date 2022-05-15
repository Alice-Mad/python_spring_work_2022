# #todo: Найти сумму элементов матрицы,
# Написать msum(matrix), которая подсчитывает сумму всех элементов функцию
# Найти сумму всех элементов матрицы:
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21
#
# >>> msum(load_matrix('matrix.txt'))
# 423
import random


def msum(matrix):
    sum_ = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            sum_ = sum_ + matrix[i][j]
    return sum_


m = [[random.randint(0, 10) for x in range(2)] for y in range(2)]
print("Source matrix: ", m)
print("Matrix sum: ", msum(m))
