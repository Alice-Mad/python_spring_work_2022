# # :todo Написать функцию is_ascending(list_) проверки на монотонность?
# Функция принимает список и определяет  является ли он монотонно возрастающим
# (то есть проверяет верно ли, что каждый элемент этого списка больше предыдущего).
# В качестве результата возвращайте  YES, если массив монотонно возрастает и NO в противном случае.

# Пример:
# mass = [ 2, 5, 7]

# def is_ascending(list_):
#     ваша реализация


# result = is_ascending(mass)
# print(result)
# YES
i = 0
mass = tuple()
j_inst = float()
counter = int()
print("Input array - numbers via spaces")
for x in input().split(" "):
    x = (x,)
    mass = mass + x
    i += 1
print(mass)
for j in mass:
    j = float(j)
    if j > j_inst:
        j_inst = j
        counter = counter + 1
if counter == len(mass):
    print("YES")
else:
    print("NO")
