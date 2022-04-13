# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.
print("Input year (after Christ)")
year_word = input()
length = len(year_word)
if length <= 2:
    print("It's earlier than first century")
else:
    if year_word[length-1] == "0":
        print("It's", year_word[0:length-2], "century")
    else:
        century = int(year_word[0:length-2])+1
        print("It's", century, "century")
