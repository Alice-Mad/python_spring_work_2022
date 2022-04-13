##todo: Самостоятельная работа

# Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения с остатком.

print('Input numeric #1')
num1 = float(input())
print('Input numeric #2')
num2 = float(input())
_sum = num1+num2
print('sum =', num1+num2)
print('diff =', num1-num2)
print('ratio =', num1/num2)
print('prod =', num1*num2)
ratio_int = num1//num2
print('ratio int =', ratio_int)
print('excess =', num1 % num2)
print('raising =', num1**num2)
