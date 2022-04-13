# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

print('Input coordinate A')
A = float(input())
print('Input coordinate B')
B = float(input())
print('Input coordinate C')
C = float(input())
AC = abs(A-C)
BC = abs(B-C)
print('AC+BC length is', AC+BC)
