# #todo: Написать функцию вычисления длины отрезка
# Условие
# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2),
# вычисляющую расстояние между точкой (x1,y1) и (x2,y2). Ввод значений считайте функцией input()
# и выведите результат работы этой функции.

# Примеры входа:
# 0
# 0
# 1
# 1

# выходные данные:
# 1.41421
i = 0
crd_tuple = tuple()


def distance(crd_t):
    x1 = float(crd_t[0])
    y1 = float(crd_t[1])
    x2 = float(crd_t[2])
    y2 = float(crd_t[3])
    dist = ((x1-x2)**2+(y1-y2)**2)**0.5
    return dist


print("Input coordinates of two points by next subsequence via spaces:x1 y1 x2 y2")
for x in input().split(" "):
    x = (x,)
    crd_tuple = crd_tuple + x
    i += 1
answer = distance(crd_tuple)
print("Distance between these two point equals", answer)
