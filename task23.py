# #todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

def encryption(old_letter, shift):
    alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_small = "abcdefghigklmnopqrstuvwxyz"
    flag = 0
    ltr = 0
    while True:
        if (ltr - shift) > 25:
            jump = ltr - shift - 26
        else:
            jump = ltr - shift
        if old_letter == alphabet_small[ltr]:
            new_letter = alphabet_small[jump]
            break
        if old_letter == alphabet_big[ltr]:
            new_letter = alphabet_big[jump]
            break
        if old_letter != alphabet_small[ltr] and old_letter != alphabet_big[ltr]:
            flag = flag + 1
        ltr = ltr + 1
        if flag == 26:
            new_letter = old_letter
            break
    return new_letter


string_new = str()
string = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
print(string, "!!! Source string !!!")
for shft in range(-7, 7):
    string_new = str()
    for i in string:
        string_new = string_new + encryption(i, shft)
    print(string_new, shft)
