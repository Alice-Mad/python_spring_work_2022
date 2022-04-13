# todo: 7.1 Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# todo: 7.2 Дано целое число A. Проверить истинность высказывания: «Число A является нечетным».
# Примечание: В задании  требуется вывести логическое значение True, если выражение
# для введеных исходных данных является истинным, и значение False в противном случае.

print('Input numeric A')
A = float(input())
even_check = (A % 2 == 0)
odd_check = (A % 2 != 0 and A == int(A))
float_check = (A != int(A))
print('numeric A is even -', even_check)
print('numeric A is odd -', odd_check)
print('type of numeric A is float -', float_check)

