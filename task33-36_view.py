import random


class View:
    def render(self, data):
        pass


class LoginView(View):
    def render(self, data):
        print("~~~ Приложение прохождения тестов ~~~")
        data[0] = input("Введите свой логин:")
        data[1] = input("Введите свой пароль:")


class StartView(View):
    def render(self, data):
        print("""
        ~~~ Приложение прохождения тестов ~~~
        Нажмите "1" для авторизации
        Нажмите "0" для регистрации
        """)
        data[0] = input()


class TestView(View):

    def render(self, data):
        """Метод реализует отрисовку экранной формы выбора билета"""
        if len(data) == 0:
            print("Вы успешно выполнили все тесты. Зачёт сдан")
        else:
            while True:
                print(data)
                flag = 0
                theme = input("Введите номер темы, по которой Вы хотите выполнить тест: ")
                for t in data:
                    if t[0] == int(theme):
                        flag = 1
                    else:
                        continue
                if flag == 1:
                    break
                else:
                    print("Теста с данным номером темы не существует или он уже успешно выполнен Вами")
            return theme


class QuestionView(View):

    def render(self, data):
        """Метод реализует отрисовку вопроса с вариантами ответа и строкой выбора варианта"""
        a_list = data[2]
        random.shuffle(a_list)
        print("Вопрос №", data[0], ": ", data[1][0])
        print("1: ", a_list[0][1])
        print("2: ", a_list[1][1])
        print("3: ", a_list[2][1])
        print("4: ", a_list[3][1])
        while True:
            answer = int(input("Введите номер выбранного Вами ответа: "))
            if answer == 1 or answer == 2 or answer == 3 or answer == 4:
                break
            else:
                print("Введён неправильный символ")
        answer_lst = a_list[answer-1]
        return answer_lst

    # class RegistrationView(View):
    #     def render(self, data):
