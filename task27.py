# #todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
# написать Save Game по следующему сценарию:
# В запущенной игре по нажатию клавиши S появляется вывод:
# 1. Продолжить
# 2. Сохранить игру
#
# При выборе пункта 1. игра продолжается.
# При выборе пункта 2. пользователю предлагается ввести название для
# сохранения, после чего нужно сделать сериализацию состояния игры.
# Законсервировать все объекты которые отвечают за состоянии игры в файл
# game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.
#
# При старте игры пользователю должен предлагатся выбор
# 1. Новая игра
# 2. Восстановить игру
# При выборе 1. начинается новая игра.
# При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
# Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.

import pickle
import random
import os

while True:
    rand = 0
    guess_num = 0
    i = 0
    answer_num = ''
    print("""
        Choose th number of desired action:
        1 Start new game
        2 Load saved game
        """)
    start_load = input()
    if start_load == "1":
        rand = random.randint(0, 100)
        i = 1
        break
    elif start_load == "2":
        files = os.listdir('/home/frosia/python/save_game')
        print(files)
        choose_load = input("Input the name of file to load without '.pkl': ")
        with open(f"/home/frosia/python/save_game/{choose_load}.pkl", "rb") as f:
            obj_l = pickle.load(f)
            rand = obj_l['rand_num']
            i = obj_l['attempts']
            last_guess = obj_l['last_guess']
            last_answer = obj_l['last_answer']
            print(f"""
                ~~~ Your game was loaded ~~~
                    Now you have only {10-i} attempts
                    Your last input number was: {last_guess}
                    The answer for this number was: {last_answer}
                """)
            f.close()
        break
    else:
        continue
print(rand)
while True:
    print("Try to guess!")
    guess = input()
    answer = "null"
    if guess == "S" or guess == "s":
        print("""
            Choose the number of required action:
            1 Continue the game
            2 Save the game
            """)
        choice = input()
        if choice == "1":
            continue
        else:
            save_name = input("Input the name of your save-file without spaces: ")
            obj_s = {"rand_num": rand, "last_guess": guess_num, "last_answer": answer_num, "attempts": i}
            fd = open(f"/home/frosia/python/save_game/{save_name}.pkl", "wb")
            pickle.dump(obj_s, fd, pickle.HIGHEST_PROTOCOL)
            fd.close()
            print("Your game was saved. Bye!")
            break
    elif int(guess) > rand:
        answer = "Your number > random"
        print(answer)
        guess_num = guess
        answer_num = answer
        i += 1
    elif int(guess) < rand:
        answer = "Your number < random"
        print(answer)
        guess_num = guess
        answer_num = answer
        i += 1
    elif int(guess) == rand:
        print("You are the winner!")
        if i == 1:
            print("You used", i, "attempt")
        else:
            print("You used", i, "attempts")
        break
    else:
        print("Invalid input")
        continue
