# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.

print('Input A')
A = float(input())
print('Input B')
B = float(input())
print('Input C')
C = float(input())
(A, B, C) = (B, C, A)
print('New A is', A)
print('New B is', B)
print('New C is', C)
