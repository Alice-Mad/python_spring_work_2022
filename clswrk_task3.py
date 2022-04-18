# #:todo Релизовать функцию
# get_section(tuple_, elm)
#
# На вход принимает кортеж и случайный элемент.  Нужно вернуть новый кортеж начинающийся
# с первого вхождения элемента в исходный кортеж и заканчивающийся вторым его появлением.
# Если искомого элемента нет – вернуть пустой кортеж. Если элемент найден только один раз,
# то вернуть кортеж, с исходного элемента до конца.
import random


def get_section(elm, tuple_arg):
    k = -1
    m = 0
    elm_amount = tuple_arg.count(str(elm))
    result = tuple()
    if elm_amount == 0:
        result = tuple()
    elif elm_amount == 1:
        result = tuple_arg
    elif elm_amount == 2:
        c = 0
        for j in tuple_arg:
            if int(j) == elm and k == -1:
                k = c
            if int(j) == elm and k != -1:
                m = c
            c += 1
        result = tuple_arg[k:m+1]
    elif elm_amount > 2:
        print("There are more the two repeats of random number")
    return result


i = 0
tuple_ = tuple()
print("Input numbers (from 0 to 2) via space")
for x in input().split(" "):
    x = (x,)
    tuple_ = tuple_ + x
    i += 1
rand = random.randint(0, 2)
print("random is", rand)
print("tuple is", tuple_)
answer = get_section(rand, tuple_)
print("Result tuple is", answer)
