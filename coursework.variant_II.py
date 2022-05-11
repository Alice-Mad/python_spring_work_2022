# #todo: II вариант (алгоритм сортировки слиянием)
# Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
# в учебнике “Introduction to Algorithms”  на стр. 71 - 77.
#
# Задача.
# Перепишите процедуру  MERGE_SORT и отсортируйте последовательность
# A = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13] по возрастанию
from sympy import oo
A = [31, 41, 9, 26, 41, 58, -1, 6, 101, 13]
L = A[0:(len(A)//2)]
R = A[(len(A)//2):]
L.sort()
R.sort()
L.append(oo)
R.append(oo)
i = 0
j = 0
for k in range(0, len(A)):
    if L[i] <= R[j]:
        A[k] = L[i]
        i += 1
    else:
        A[k] = R[j]
        j += 1
print(A)
