# #todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.
import random

# ? подскажите, пожалуйста, в части чего можно провести рефакторинг этого кода при помощи функций,
# если тут нет нескольких вызовов одного и того же функционала из разных мест глобальной программы?
# Заранее спасибо


def attempt_count(att):
    if att == 1:
        print("Your letter is wrong. You have your last attempt")
    elif att == 0:
        print("You lose")
    else:
        print("Your letter is wrong. You have", att, "attempts")


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
            attempt_count(attempt)
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
