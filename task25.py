# #todo: Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.
#
# Input             	            Output
# apple	                        aple
# 25.04.2022 Good morning !!	    godmrni

print("Input your text")
string = input()
text = str()
for i in string:
    if i.isalpha() is True:
        text = text + i
text = text.lower()
alphabet = "abcdefghigklmnopqrstuvwxyz"
basic_dict = dict()
new_dict = dict()
result = str()
for k in alphabet:
    search = text.find(k)
    if search != -1:
        basic_dict[search] = k
for key in sorted(basic_dict):
    new_dict[key] = basic_dict[key]
for key, val in new_dict.items():
    result = result + val
print("THE RESULT IS:")
print(result)
