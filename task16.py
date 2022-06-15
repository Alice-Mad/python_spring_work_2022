# #todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.

import random


def your_word():
    # функция формирует массив, содержащий слово для отгадывания (нулевой элемент), его описание (первый элемент) и
    # начальный вид мнемоники (второй элемент)
    words = ["сосна", "ель", "ясень"]
    desc_ = ["хвойное дерево", "новогоднее дерево", "дерево из песни"]
    word_number = random.randint(0, len(words) - 1)
    i = 0
    mnemonic = []
    length = len(words[word_number])
    while i < length:
        mnemonic.append("▒")
        i = i + 1
    lst = [words[word_number], desc_[word_number], mnemonic]
    return lst


def game(lst):
    # функция предназначена непосредственно для проведения игры и принимает входными данными массив, сформированный
    # в функции your_word

    def letter_mnemo(letter, lst):
        # функция проверяет введённую игроком букву на наличие в загаданном слове
        # и при положительном результате меняет мнемосхему, добавляя букву(ы)
        i = 0
        for j in lst[0]:
            if j == letter:
                lst[2][i] = letter
            i += 1
        return lst[2]

    def mistake_count(letter, word, mistakes):
        # функция ведёт подсчёт допущенных игроком ошибок
        counter = 0
        for j in word:
            if j != letter:
                counter = counter + 1
        if counter == len(lst[0]):
            mistakes += 1
        return mistakes

    def check_win(lst, m):
        check = 0
        counter = 0
        for k in lst[2]:
            if k == "▒":
                continue
            else:
                counter = counter + 1
        if counter == len(lst[0]):
            check = 1
        if m == 5:
            check = 0
        print(lst[2])
        return check

    mistakes = 0
    while True:
        _l = input("Input your letter: ")
        lst[2] = letter_mnemo(_l, lst)
        mistakes_refresh = mistakes
        mistakes = mistake_count(_l, lst[0], mistakes)
        if mistakes != mistakes_refresh:
            if mistakes == 4:
                answer = "Your letter is wrong. Your last attempt"
            elif mistakes == 5:
                answer = "You lose"
                break
            else:
                answer = ("Your letter is wrong. You have " + str(5-mistakes) + " attempts")
            print(answer)
        check = check_win(lst, mistakes)
        if check == 0:
            continue
        else:
            print("----------------------")
            print(lst[2])
            print("You win!")
            break


guess_pack = your_word()
print("Guess the word", guess_pack[2])
print("Word's description: ", guess_pack[1])
game(guess_pack)
