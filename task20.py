# #todo: Выведите все строки данного файла в обратном порядке.
# # Для этого считайте список всех строк при помощи метода readlines().
#
# Содержимое файла import_this.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# выходные данные
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.
f = open("import_this.txt", "w")
lines = [
    "Beautiful is better than ugly.\n",
    "Explicit is better than implicit.\n",
    "Simple is better than complex.\n",
    "Complex is better than complicated.\n",
]
f.writelines(lines)
f.close()
f = open("import_this.txt", "r")
lst = (f.readlines())
f.close()
print(lst)
y = 1
while True:
    obj = lst[len(lst)-y]
    print(obj[0:(len(obj)-2)])
    if y == len(lst):
        break
    y += 1
