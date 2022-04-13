# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".
print("Input four-place number")
four_num = input()
if len(four_num) != 4:
    print("You have input NOT a four-place number")
else:
    if four_num[0] == four_num[3]:
        if four_num[1] == four_num[2]:
            print("This four-place number IS mirror-like")
    else:
        print("This four-place number IS NOT mirror-like")
