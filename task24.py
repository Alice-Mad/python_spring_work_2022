# #todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def text_transform(txt):
    alphabet = "abcdefghigklmnopqrstuvwxyz "
    txt = txt.strip()
    if txt.isdigit() is True:
        txt = alphabet[int(txt)-1]
    return txt


print("Input your text")
string = input()
print(string)
k = 0
text = str()
result = str()
for i in range(len(string)):
    if string[i] == " ":
        text = string[k:i]
        k = i
        result = result + text_transform(text)
    if i == (len(string)-1):
        text = string[k:]
        result = result + text_transform(text)
print(result)
