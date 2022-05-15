# #todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы.
# Решить с использованием списковых включений.
#
#
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||
def transpose(source_matrix):
    columns = len(source_matrix)
    strings = len(source_matrix[1])
    matrix = [[source_matrix[j][i] for j in range(columns)] for i in range(strings)]
    return matrix


m = [[1, 2, 3], [4, 5, 6]]
print("Source matrix", m)
print("Transposed matrix", transpose(m))
