# Написать игру "Поле чудес"

# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.

# Пример вывода:

# "Это слово обозначает наименьшую автономную часть языка программирования"

# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

# Введите букву: O

# O  ▒  ▒  ▒  ▒  ▒  O  ▒


# Введите букву: Я

# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

import random
words = ["сосна", "ель", "ясень"]
desc_ = ["хвойное дерево", "новогоднее дерево", "дерево из песни"]
word_number = random.randint(0, len(words)-1)
print(word_number)
i = 0
mnemonic = []
length = len(words[word_number])
while i < length:
    mnemonic.append("▒")
    i = i + 1
print("Guess the word", mnemonic)
print("Word's description: ", desc_[word_number])
attempt = 5
while True:
    counter_1 = 0
    counter_2 = 0
    print("Input your letter")
    letter = input()
    i = 0
    for j in words[word_number]:
        if j == letter:
            mnemonic[i] = letter
        else:
            counter_2 = counter_2 + 1
        if counter_2 == len(words[word_number]):
            attempt = attempt - 1
            if attempt == 1:
                print("Your letter is wrong. You  last attempt")
            elif attempt == 0:
                print("You lose")
            else:
                print("Your letter is wrong. You have", attempt, "attempts")
        i = i + 1
    for k in mnemonic:
        if k == "▒":
            continue
        else:
            counter_1 = counter_1 + 1
    if counter_1 == len(words[word_number]):
        print("You win!")
        break
    if attempt == 0:
        break
    print(mnemonic)
