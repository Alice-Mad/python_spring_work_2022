from db import DB
from profile import Profile
from view import *
import random


class Auth:
    """Класс относится к C-составляющей паттерна модели VCM."""
    """Класс содержит методы регистрации в системе, захода в систему и выхода из нее"""
    is_auth = False

    def registration(self):
        g_number = input("Введите номер своей группы: ")

        # подключаемся к БД для выгрузки перечня студентов
        my_db = DB()
        my_conn = my_db.get_connect()

        # получаем из БД данные, соответствующие введённому номеру группы
        cls_list = Profile("", "", "", "", "", "", g_number, "")
        group_list = cls_list.get_group_list(my_conn)
        if len(group_list) == 0:
            print("Данной группы не существует или в ней нет незарегистрированных студентов")
            a = Auth()
            a.registration()
        else:
            print(group_list)

        # выбираем студента, для которого будет проводиться регистрация
        id_s = input("Введите ваш порядковый номер: ")
        my_s = list()
        for sinfo_line in group_list:
            if id_s == str(sinfo_line[0]):
                my_s = sinfo_line
            else:
                continue

        if len(my_s) == 0:
            print("Незарегистрированного студента с таким порядковым номером не существует")
            a = Auth()
            a.registration()

        # регистрируем клиента
        login = (my_s[1][0] + my_s[2]).lower()
        print("Ваш логин: ", login)
        cls_register = Profile(login, "", my_s[2], my_s[1], "", "", "", my_s[0])
        cls_register.set_profile(my_conn)

        # проверяем, была ли осуществлена запись данных

        # подключаемся к БД для проверки корректности введённых данных
        my_db = DB()
        my_conn = my_db.get_connect()

        # получаем из БД данные, соответствующие введённому логину
        # print("login", login)
        cls_log = Profile(login, "", "", "", "", "", "", "")
        my_profile = cls_log.get_profile(my_conn)
        if my_profile is not None:
            print(f"""
            Вы успешно зарегистрированы
            Ваш логин: {my_profile[1]}
            Ваш пароль: {my_profile[2]}
            Вы автоматически вошли в систему
            """)
            Auth.is_auth = True
        else:
            print("Регистрация не пройдена")
            a = Auth()
            a.registration()
        return my_profile[0]

    def login(self):
        # получаем от пользователя его логин и пароль, выводя соответствующий render
        log_data = ["", ""]
        cls_loginview = LoginView()
        cls_loginview.render(log_data)

        # подключаемся к БД для проверки корректности введённых данных
        my_db = DB()
        my_conn = my_db.get_connect()

        # получаем из БД данные, соответствующие введённому логину
        cls_log = Profile(log_data[0], log_data[1], "", "", "", "", "", "")
        my_profile = cls_log.get_profile(my_conn)
        # print(my_profile)
        if my_profile is None:
            print("Пользователь с данным логином не существует")
            # повторно получаем от пользователя его логин и пароль, выводя соответствующий render
            cls_login = Auth()
            cls_login.login()
        elif my_profile[2] == log_data[1]:
            Auth.is_auth = True
            print("Ура! Вы вошли в систему")
        elif my_profile[2] != log_data[1]:
            print("Пароль неверный")
            # повторно получаем от пользователя его логин и пароль, выводя соответствующий render
            cls_login = Auth()
            cls_login.login()
        return my_profile[0]

    @staticmethod
    def logout():
        Auth.is_auth = False


class TestSystem:
    # Класс относится к C-составляющей паттерна модели VCM.
    # Класс взаимодействует с моделью и представлением. Включает всю бизнес логику системы прохождения теста

    def show_list(self, id_):
        """Метод реализует вывод списка тестов на экран"""
        # подключаемся к БД для получения перечня тестов по темам
        my_db = DB()
        my_conn = my_db.get_connect()

        # получаем перечень тестов
        with my_conn.cursor() as cur:
            cur.execute("""
                        select t.id_test, t.theme
                        from student_test st
                        full outer join test t
                        on st.id_test = t.id_test
                        where (st.id_student = (%s) and st."result" = false)
                        or (st.id_student = (%s) and st."result" is null)""",
                        [id_, id_])
            themes = cur.fetchall()
            cls_testlist = TestView()
            theme = cls_testlist.render(themes)
        return theme

    def show_question(self, id_question, q_number):
        # подключаемся к базе данных для получения текста вопроса
        my_db = DB()
        my_conn = my_db.get_connect()

        # получаем тест вопроса с нужным id
        with my_conn.cursor() as cur:
            cur.execute("""
                        SELECT question_text FROM question
                        WHERE id_question = (%s)""",
                        [id_question])
            q_text = cur.fetchone()

        # получаем варианты ответов на вопрос с нужным id
            cur.execute("""
                        SELECT * FROM answer
                        WHERE id_question = (%s)""",
                        [id_question])
            a_list = cur.fetchall()
            cls_printq = QuestionView()
            answer_lst = cls_printq.render([q_number, q_text, a_list])
        return answer_lst

    @staticmethod
    def run():
        while True:
            # выводим пользователю стартовый render для выбора авторизации или регистрации,
            # где 1 - это авторизация, а 0 - это регистрация
            start_data = [""]
            cls_startview = StartView()
            cls_startview.render(start_data)
            if start_data[0] == "1":
                # при запросе пользователем авторизации (1) вызываем класс авторизации
                a = Auth()
                my_id = a.login()
                break
            elif start_data[0] == "0":
                # при запросе пользователем регистрации (0) вызываем класс регистрации
                a = Auth()
                my_id = a.registration()
                break
            else:
                # при вводе пользователем другого символа (отличного от 0 и 1)
                # повторно просим выбрать регистрацию или авторизацию
                my_sw = TestSystem()
                my_sw.run()
# место склейки
        while True:
            my_sw = TestSystem()
            if Auth.is_auth:
                print("*", my_id)
                my_theme = int(my_sw.show_list(my_id))
                x = y = 0
                print("""
                Вам будет предложено ответить на 10 вопросов.
    
                Положительным результатом будет считаться:
                - дача правильных ответов на 8 и более вопросов;
                - ответы на все вопросы должны быть даны в течение 15 минут.
    
                Введите любой символ, чтобы перейти к выполнению теста и запустить отсчёт времени
                """)
                input()
                # сформируем тест, выбрав случайным образом 10 вопросов на выбранную студентом тему
                if my_theme == 0:
                    x = 0
                    y = 100
                elif my_theme == 1:
                    x = 100
                    y = 200
                elif my_theme == 2:
                    x = 200
                    y = 300
                q_list = list(range(x, y))
                random.shuffle(q_list)
                q_list = q_list[0:10]
                i = 1
                count = 0
                for q in q_list:
                    my_answer = my_sw.show_question(q, i)
                    if my_answer[2] is True:
                        count += 1
                    i += 1
                if count >= 8:
                    print("Вы успешно выполнили тест")
                else:
                    print("Тест не пройден. Попробуйте ещё")
            else:
                continue
