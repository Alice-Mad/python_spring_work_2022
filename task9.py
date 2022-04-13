# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

print("Input first integer numeric")
f_num = int(input())
print("Input second integer numeric")
s_num = int(input())
print("Input third integer numeric")
t_num = int(input())
if f_num >= s_num and f_num > t_num:
    if f_num > s_num:
        print("First number is the greatest one")
    else:
        print("First and second numbers are the greatest ones")
elif s_num >= t_num and s_num > f_num:
    if s_num > t_num:
        print("Second number is the greatest one")
    else:
        print("Second and third numbers are the greatest ones")
elif t_num >= f_num and t_num > s_num:
    if t_num > f_num:
        print("Third number is the greatest one")
    else:
        print("First and third numbers are the greatest ones")
else:
    print("Three numbers are uqual")
