# #todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

# #Пример:
# #mass = [1,2,17,16,30,51,2,70,3,2]

# #Для числа 2 индексы двух ближайших чисел: 6 и 9

# #Пример:
# #mass = [1,2,17,54,30,89,2,1,6,2]
# #Для числа 1 индексы двух ближайших чисел: 0 и 7
# #Для числа 2 индексы двух ближайших чисел: 6 и 9

print("Input mass dimension")
dim = int(input())
i = 0
mass = list(range(dim))
while i < dim:
    print("Input", i, "element")
    mass[i] = int(input())
    i = i+1
print(mass)
print("Input object of interest (integer number)")
_object = int(input())
j = 0
k = 0
j_mem = 0
k_mem = 0
buffer = 1000
while j < (dim - 1):
    if mass[j] == _object:
        k = j + 1
        while k < (dim-1):
            if (mass[k] == _object) and ((k-j) < buffer):
                k_mem = k
                j_mem = j
                buffer = k - j
            k = k + 1
    j = j + 1
if k_mem == j_mem == 0:
    print("Number", _object, "isn't repeated")
else:
    print("For object of interest", _object, "first indexes of the nearest are", j_mem, "and", k_mem)
